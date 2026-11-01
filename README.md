# My_research_workflow

个人科研工作流与 AI skills 集合。目前先整理 **idea 阶段**，后续按实际使用逐步扩展。

## 已收录

| 阶段 | Skill | 用途 |
| --- | --- | --- |
| Idea | [aeons-idea-workflow](skills/aeons-idea-workflow/SKILL.md) | 保留原始想法，围绕文献迭代版本，记录评审与人的取舍，完成最小 pilot 后决定继续、修改或停止 |

AI 协助整理、检索、评审和已授权的实验，研究者决定方向与关键取舍。计划、评分与多轮 AI 共识不能替代真实实验结果。

## 目录

```text
skills/
  aeons-idea-workflow/
    SKILL.md                    # 工作流入口
    agents/openai.yaml          # Codex 显示信息
    scripts/idea_workspace.py   # 目录初始化、状态查看和原文快照
    assets/                    # review、pilot、handoff 模板
    references/                # 运行约定、交接说明与设计参考
```

仓库保存可复用的工作流和模板。具体项目的 idea、论文与实验结果保存在各自项目中。

## 在 Codex 中使用

克隆仓库后，在仓库根目录执行以下命令，把 skill 复制到个人 skills 目录。若已有同名安装，先比较内容并自行选择是否替换；命令会在目录已存在时停止。

```bash
python3 - <<'PY'
import os
import shutil
from pathlib import Path

codex_dir = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()
source = Path("skills/aeons-idea-workflow")
destination = codex_dir / "skills" / source.name
destination.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(source, destination)
print(f"Installed: {destination}")
PY
```

重新打开 Codex 会话后，可以这样提出任务：

```text
使用 $aeons-idea-workflow，先查看当前项目已有的 idea 和评审，再继续本轮迭代。
```

`deep-research`、`idea-evaluator`、`marker-pdf-to-md` 等是按需使用的可选协作 skills，本仓库不包含它们。缺少这些能力时，仍可使用工作流约定和目录脚本。

## 独立使用目录脚本

需要 Python 3.9 或更新版本；脚本仅使用标准库。从本仓库根目录运行，`--project-root` 指向一个已经存在的项目目录。

```bash
# 只读查看状态；不会创建文件。
python3 skills/aeons-idea-workflow/scripts/idea_workspace.py \
  status --project-root /absolute/path/to/project

# 在项目中创建 brainstorming/paper、idea、idea_review 等目录。
python3 skills/aeons-idea-workflow/scripts/idea_workspace.py \
  init --project-root /absolute/path/to/project

# 保存原始想法快照，并记录来源与 SHA256；相同内容不重复建版。
python3 skills/aeons-idea-workflow/scripts/idea_workspace.py \
  snapshot --project-root /absolute/path/to/project \
  --idea-id 001-topic --source-file /absolute/path/to/idea.md \
  --origin human --reason '保存我的原始想法'
```

只有确为人的原文时使用 `--origin human`；AI 代写或混合来源应选择相应标签。运行 `snapshot --help` 查看所有选项。

完整约定见 [SKILL.md](skills/aeons-idea-workflow/SKILL.md)，设计来源见 [来源说明](skills/aeons-idea-workflow/references/design-sources.md)。
