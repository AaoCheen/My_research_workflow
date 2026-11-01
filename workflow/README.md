# 如何使用这套工作流

这层只组织步骤与输入输出。具体执行规则、评审和 pilot 模板放在各自 `skills/` 中。

## 阶段与入口

| 当前任务 | 入口 | 输入 | 产物位置 |
| --- | --- | --- | --- |
| 从原始想法出发，阅读、改版、评审与最小 pilot | [idea-to-pilot.md](idea-to-pilot.md) | 原始想法、已有文献、评审、资源约束 | 项目的 `brainstorming/`；运行日志在实际工程中 |
| 论文 PDF 转 Markdown 并阅读 | [reading.md](reading.md) | PDF、阅读问题、关注的章节或表格 | `brainstorming/paper/`；解释与判断进入对应 idea 的评审目录 |
| 形成结构、起草和修改稿件 | [writing.md](writing.md) | 研究材料、已有结果、目标章节与写作要求 | 项目的 `writing/` 或既有论文目录 |
| 保留本轮讨论，方便下一次继续 | [会话模板](templates/session.md) | 本轮实际对话与产物路径 | 项目的 `sessions/` |

按当前任务选入口，不要求每次跑完整流程。写作也可以在实验之前用于整理计划，但稿件必须区分计划、假说和已有结果。

## 开始新项目

1. 明确实际项目根目录。可以用现有工程，也可以在本仓库的 `workspace/<project>/` 工作。
2. 需要项目说明时，从 [PROJECT.md](templates/PROJECT.md) 复制一份到项目中，填写目标、路径、当前阶段和本轮范围。
3. 只在需要时创建目录与材料。不要先生成空的实验结果、评审结论或全套稿件。

例如，要在本仓库内开启临时项目，可以手动执行：

```bash
# 从本仓库根目录运行；my-project 换成自己的项目名。
mkdir -p workspace/my-project/sessions
cp -n workflow/templates/PROJECT.md workspace/my-project/PROJECT.md
```

具体 idea 工作区可由 `aeons-idea-workflow` 的脚本初始化。已有目录先读取并复用。

## 恢复一次工作

给 LLM 一个明确的恢复任务：

```text
项目根目录是 /absolute/path/to/project。
先读 PROJECT.md（如有）、最新 sessions 记录和本轮相关产物。
核对当前实际文件，不仅根据摘要判断进度。
当前问题是：……；本轮允许修改的范围是：……。
选择并读取相应 SKILL.md 后，继续处理。
```

`PROJECT.md` 和会话摘要用于导航。idea 的正式版本、评审、`decisions.md` 和实测日志仍是各自事实的依据，不把旧摘要当作最新实验结果。

## 保存本轮工作

先把产物写入项目的对应目录，再按需要保存 `sessions/YYYY-MM-DD_topic.md`。会话摘要记录实际讨论、改动、证据路径、未解决问题和下一步；没有实际发言或文件依据的意见不能补写成人的决定。

普通聊天不要求落盘。需要逐字记录时使用实际导出的对话，LLM 整理的摘要应明确标为摘要。仓库不会自动读取或归档聊天历史。
