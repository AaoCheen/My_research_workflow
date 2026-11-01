#!/usr/bin/env python3
"""初始化 idea 工作区、只读查看进度，或保存原文的不可覆盖版本；仅使用标准库。"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ORIGINS = ("human", "ai-assisted", "literature-inspired", "mixed", "unspecified")
IDEA_ID = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
VERSION = re.compile(r"v([0-9]{3,})\.md\Z")


def within(path: Path, root: Path) -> Path:
    """防止既有符号链接把项目写入指向项目外。"""
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"工作区路径越出项目边界: {path}")
    return resolved


def project_layout(value: Path) -> dict[str, Path]:
    root = value.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"项目目录必须已经存在: {root}")
    base = within(root / "brainstorming", root)
    candidates = [base / name for name in ("paper", "papers") if (base / name).exists()]
    if len(candidates) > 1:
        raise ValueError("paper/ 与 papers/ 同时存在，请先确定使用哪个目录；脚本不会合并或迁移。")
    paper = candidates[0] if candidates else base / "paper"
    paths = {"project_root": root, "brainstorming": base, "paper": paper,
             "idea": base / "idea", "idea_review": base / "idea_review"}
    for name, path in paths.items():
        within(path, root)
        if path.exists() and not path.is_dir():
            raise ValueError(f"预期目录却发现文件: {name}: {path}")
    return paths


def legacy_paths(layout: dict[str, Path]) -> list[str]:
    root, base = layout["project_root"], layout["brainstorming"]
    found = [p for p in (root / "my_idea", base / "my_idea") if p.exists()]
    if base.is_dir():
        found.extend(p for p in sorted(base.iterdir())
                     if p.is_dir() and p.name.endswith("_review") and p != layout["idea_review"])
    return [str(p.relative_to(root)) for p in found]


def canonical_versions(folder: Path) -> list[Path]:
    versions = []
    for path in folder.glob("v*.md"):
        match = VERSION.fullmatch(path.name)
        number = int(match.group(1)) if match else 0
        if not match or number < 1 or path.name != f"v{number:03d}.md":
            raise ValueError(f"非规范版本文件，需先人工检查: {path}")
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"版本必须是普通文件: {path}")
        versions.append(path)
    return sorted(versions, key=lambda p: int(VERSION.fullmatch(p.name).group(1)))


def load_ledger(folder: Path, idea_id: str, files: list[Path]) -> dict:
    ledger = folder / "versions.json"
    if ledger.is_symlink():
        raise ValueError(f"版本记录必须是普通文件: {ledger}")
    if not ledger.exists():
        if files:
            raise ValueError(f"已有版本但缺少 versions.json；保留原文，先补核实过的来源记录: {folder}")
        return {"schema_version": 1, "idea_id": idea_id, "versions": []}
    if ledger.is_symlink() or not ledger.is_file():
        raise ValueError(f"版本记录必须是普通文件: {ledger}")
    data = json.loads(ledger.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("idea_id") != idea_id or not isinstance(data.get("versions"), list):
        raise ValueError(f"无法识别版本记录: {ledger}")
    if any(not isinstance(row, dict) for row in data["versions"]):
        raise ValueError(f"版本记录包含非对象条目: {ledger}")
    recorded = [row.get("version") for row in data["versions"]]
    if recorded != [p.stem for p in files]:
        raise ValueError(f"版本文件与 versions.json 不一致，请先检查；不会覆盖已有文件: {folder}")
    for row, path in zip(data["versions"], files):
        if hashlib.sha256(path.read_bytes()).hexdigest() != row.get("sha256"):
            raise ValueError(f"已有版本内容与记录哈希不同: {path}；请保留改动并核对版本来源。")
    return data


def status(layout: dict[str, Path]) -> dict:
    root = layout["project_root"]
    ideas = []
    if layout["idea"].is_dir():
        for folder in sorted(layout["idea"].iterdir()):
            if not folder.is_dir():
                continue
            row = {"idea_id": folder.name, "versions": [], "warnings": []}
            try:
                within(folder, root)
                files = canonical_versions(folder)
                ledger = load_ledger(folder, folder.name, files)
                for path, record in zip(files, ledger["versions"]):
                    review = layout["idea_review"] / folder.name / f"{path.stem}_review.md"
                    row["versions"].append({
                        "version": path.stem, "path": str(path.relative_to(root)),
                        "sha256": record["sha256"], "origin": record.get("origin", "unspecified"),
                        "review_path": str(review.relative_to(root)), "review_exists": review.is_file(),
                    })
                row["latest_version"] = files[-1].stem if files else None
            except (ValueError, OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
                row["warnings"].append(str(exc))
            ideas.append(row)
    return {
        "project_root": str(root),
        "directories": {name: str(path.relative_to(root)) for name, path in layout.items() if name != "project_root"},
        "initialized": all(p.is_dir() for name, p in layout.items() if name != "project_root")
            and all((layout["paper"] / name).is_dir() for name in ("pdf", "md", "metadata")),
        "legacy_paths": legacy_paths(layout),
        "ideas": ideas,
        "note": "review_exists 仅表示文件存在，不表示评审通过、人的批准或 pilot 已完成。",
    }


def initialize(layout: dict[str, Path]) -> dict:
    root = layout["project_root"]
    targets = [layout["brainstorming"], layout["paper"],
               *(layout["paper"] / name for name in ("pdf", "md", "metadata")),
               layout["idea"], layout["idea_review"]]
    for target in targets:
        within(target, root)
        if target.exists() and not target.is_dir():
            raise ValueError(f"目录位置被文件占用，未创建工作区: {target}")
    for target in targets:
        target.mkdir(parents=True, exist_ok=True)
    result = status(layout)
    result["action"] = "initialized"
    result["note"] += " 已有目录、README、原始想法、专题 review 均保持原样；未执行迁移。"
    return result


def snapshot(args: argparse.Namespace, layout: dict[str, Path]) -> dict:
    if not IDEA_ID.fullmatch(args.idea_id):
        raise ValueError("idea-id 仅允许小写字母、数字和连字符，首位为字母/数字，最多 64 字符。")
    if not args.reason.strip():
        raise ValueError("--reason 不能为空。")
    source = args.source_file.expanduser().resolve()
    if not source.is_file():
        raise ValueError(f"来源必须是已存在的文件: {source}")
    content = source.read_bytes()
    if not content:
        raise ValueError("来源文件为空，不创建空 idea 版本。")
    root = layout["project_root"]
    folder = within(layout["idea"] / args.idea_id, root)
    files = canonical_versions(folder) if folder.exists() else []
    data = load_ledger(folder, args.idea_id, files)
    digest = hashlib.sha256(content).hexdigest()
    if data["versions"] and data["versions"][-1]["sha256"] == digest:
        return {"action": "unchanged", "idea_id": args.idea_id,
                "version": data["versions"][-1]["version"], "sha256": digest,
                "note": "与最新版本内容相同；未生成新版本、未修改来源或记录。"}
    number = int(files[-1].stem[1:]) + 1 if files else 1
    version = f"v{number:03d}"
    destination = within(folder / f"{version}.md", root)
    if source == destination:
        raise ValueError("来源和目标相同；不会覆盖来源。")
    folder.mkdir(parents=True, exist_ok=True)
    lock = folder / ".snapshot.lock"
    try:
        handle = lock.open("x", encoding="utf-8")
    except FileExistsError as exc:
        raise ValueError(f"发现 snapshot 锁，请确认没有其他写入或中断任务: {lock}") from exc
    try:
        with handle:
            handle.write("本锁只在保存快照时存在；中断后请核对版本文件与 ledger 再清理。\n")
        # 获得锁后重读，防止并发调用覆盖另一进程刚保存的版本记录。
        current = canonical_versions(folder)
        if [p.name for p in current] != [p.name for p in files]:
            raise ValueError("版本在本次操作中改变，请重新执行 snapshot。")
        load_ledger(folder, args.idea_id, current)
        temporary = folder / ".versions.json.tmp"
        if temporary.exists() or temporary.is_symlink():
            raise ValueError(f"发现未完成的版本记录临时文件，请先核对: {temporary}")
        record = {"version": version, "file": destination.name, "sha256": digest,
                  "origin": args.origin, "reason": args.reason,
                  "source_file": str(source), "created_utc": datetime.now(timezone.utc).isoformat()}
        data["versions"].append(record)
        # xb 拒绝覆盖任何已有目标；来源原文不做包装或文字改写。
        with destination.open("xb") as out:
            out.write(content)
        try:
            with temporary.open("x", encoding="utf-8") as out:
                out.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            temporary.replace(folder / "versions.json")
        except Exception:
            # 原文快照保留供核查；不自动删除可能已有其他来源的临时文件。
            raise
    finally:
        lock.unlink()
    return {"action": "created", "idea_id": args.idea_id, "version": version,
            "path": str(destination.relative_to(root)), "sha256": digest,
            "origin": args.origin, "note": "已保存原文；没有生成评审、人的决策、批准状态或 pilot 结果。"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("init", "创建三类目录，保留现有文件；已有 papers 时复用它"),
                            ("status", "只读显示目录、遗留路径、版本与评审文件存在性"),
                            ("snapshot", "从显式来源保存原文快照；相同内容不重复建版")):
        child = sub.add_parser(name, help=help_text)
        child.add_argument("--project-root", required=True, type=Path, help="已存在的项目根目录")
    snap = sub.choices["snapshot"]
    snap.add_argument("--idea-id", required=True)
    snap.add_argument("--source-file", required=True, type=Path)
    snap.add_argument("--origin", choices=ORIGINS, default="unspecified")
    snap.add_argument("--reason", required=True, help="本版保存或修改的真实原因；不等于人的批准")
    args = parser.parse_args()
    try:
        layout = project_layout(args.project_root)
        result = initialize(layout) if args.command == "init" else status(layout) if args.command == "status" else snapshot(args, layout)
    except (ValueError, OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
