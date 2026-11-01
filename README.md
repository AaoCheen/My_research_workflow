# My_research_workflow

我个人使用的科研 skills 与工作流程。这里维护可复用的方法和指令，具体研究材料与 LLM 对话放在各自工作区。

## 三类目录

```text
My_research_workflow/
  skills/                    # 独立能力：SKILL.md、参考说明、模板和必要脚本
  workflow/                  # 使用流程：阶段顺序、选哪个 skill、怎样开始与恢复
    templates/               # 项目说明与会话记录的空白模板
  workspace/                 # 实际工作：项目材料、写作产物、LLM 对话
    README.md                # 工作区说明，上传 GitHub
    <project>/               # 具体项目，默认不上传
```

- **skills** 回答“这件事怎么做”。skill 以指示为主，也可以带脚本和模板。
- **workflow** 回答“当前做到哪、下一步调用谁、输入输出是什么”。详细规则继续放对应 skill，避免维护两份。
- **workspace** 保存真实工作。项目中的 `sessions/` 放对话记录与恢复摘要，`brainstorming/` 放文献、idea 和评审，`writing/` 放稿件。

已有项目继续使用原目录，不必把 TAFFC 的论文、代码或对话搬进来。这里的 `workspace/<project>/` 也可以用于新项目或临时工作。

## Skills

| 阶段 | Skill | 用途 |
| --- | --- | --- |
| Idea | [aeons-idea-workflow](skills/aeons-idea-workflow/SKILL.md) | 原始想法、文献、版本评审、人的取舍、最小 pilot 与交接 |
| 阅读准备 | [marker-pdf-to-md](skills/marker-pdf-to-md/SKILL.md) | 使用现有 Marker 环境将 PDF 转为 Markdown 和图片，检查转换产物 |
| 论文结构 | [tech-paper-template](skills/tech-paper-template/SKILL.md) | 技术论文的问题、挑战、方法与贡献逻辑 |
| 论文结构 | [benchmark-paper-template](skills/benchmark-paper-template/SKILL.md) | Benchmark / Evaluation 论文的构建、评测与发现结构 |
| 起草 | [paper-writer](skills/paper-writer/SKILL.md) | 根据已有材料起草章节或全文 |
| 起草 | [intro-drafter](skills/intro-drafter/SKILL.md) | 起草或重组 Introduction |
| 修改 | [paper-polish](skills/paper-polish/SKILL.md) | 语法、衔接、措辞、证据强度与中译英 |
| 修改 | [academic-humanizer](skills/academic-humanizer/SKILL.md) | 减少学术文本中的空泛、机械重复和模板化表达 |
| 核查 | [nature-ref-verifier](skills/nature-ref-verifier/SKILL.md) | 逐条核对参考文献字段与来源 |
| 核查 | [pre-submission-reviewer](skills/pre-submission-reviewer/SKILL.md) | 投稿前检查逻辑、语言、格式与图表问题 |

Marker 已在本机配置；这里只保留使用方法，不提供下载、安装教程。其他 skills 中提到的外部检索、Zotero 或协作 skills 按需使用，文件被收录不代表所有外部服务已配置。保留各 skill 原有的来源和许可字段。

## 日常使用

先看 [workflow/README.md](workflow/README.md)，再选当前任务需要的流程：

- [Idea → 最小 pilot](workflow/idea-to-pilot.md)
- [PDF 转换与文献阅读](workflow/reading.md)
- [论文结构、起草、修改与核查](workflow/writing.md)

给 LLM 的任务需要明确**项目路径、目标文件和当前问题**。例如：

```text
工作项目：/absolute/path/to/project。
先读 skills/aeons-idea-workflow/SKILL.md，
再读项目已有的 idea、评审和决策记录，判断当前阶段并继续本轮工作。
保留原始想法，区分 AI 建议与我实际作出的决定。
```

这里的相对路径以本仓库为起点；不在仓库目录对话时，给出实际绝对路径。已安装的 skill 可以直接按名字调用；仓库副本和已安装副本需要分别维护，Git 提交不会自动更新本机安装。

对话本身不会自动写入这个仓库。需要保留时，导出原始对话，或让 LLM 按 [会话模板](workflow/templates/session.md)整理摘要并标明记录类型。具体工作区见 [workspace/README.md](workspace/README.md)。

## 自己提交并上传

远程仓库已经建好，`origin` 已配置。每次修改后，在终端自行执行：

```bash
cd /home/ca/big_space/my_project/TAFFC/tmp/My_research_workflow

# 先查看本轮改动；未跟踪的新文件会显示在 status 中。
git status --short
git diff --stat
git diff

# 只暂存工作流、skills 和工作区说明。
git add README.md .gitignore skills/ workflow/ workspace/README.md
git diff --cached --stat

git commit -m "Organize research skills and workflows"
git push origin main
```

以后按实际改动调整提交说明即可。`workspace/` 下的真实项目内容被 `.gitignore` 排除；不用重新创建仓库，也不需要用 `gh` 才能推送。
