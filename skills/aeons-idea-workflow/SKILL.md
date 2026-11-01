---
name: aeons-idea-workflow
description: 用于科研选题的持续迭代：保留人类原始 idea，组织论文，按具体版本评审，记录人的取舍，完成最小 pilot 后再决定是否定题并交接工程与论文。适用于启动或继续 brainstorm、阅读后修改方向、复审新版本和检查定题条件；单篇论文摘要、单次润色或已有方案的代码实现通常不需要完整流程。
---

# Aeon's Idea Workflow

目标：让研究者从一个原始想法，经文献、讨论与最小实验，形成有证据支持的研究投入决定。终点是**实际完成最小 pilot，阅读其结果后，由研究者决定继续、修改或停止**。计划、AI 评分或多轮一致意见都不能替代实验结果；pilot 通过也不保证完整论文效果或录用。

用户决定方向和关键取舍。整理、检索、转换、已授权的改稿和实验在授权范围内连续完成，无需逐步重复确认。讨论中提出的选项不能自动记成用户已采纳；保留用户已经拒绝或暂缓的建议，出现相关新证据时再讨论。

## 开始或恢复

先读当前用户请求、项目说明、已有 idea/评审与决策记录。确定是在发散、查证、改版、复审、pilot 还是交接阶段，只做当前阶段需要的工作。用户只问状态时做只读检查。

每个项目使用自己的 `brainstorming/`；skill 本体、脚本和工具环境保留在项目外。新项目默认结构：

```text
brainstorming/
  paper/
    pdf/
    md/
    metadata/
  idea/
    001-topic/
      draft.md
      v001.md
      v002.md
      versions.json
      decisions.md
  idea_review/
    001-topic/
      v001_review.md
      v002_review.md
      reading_list.md
      v002_pilot_01_plan.md
      v002_pilot_01_result.md
      v002_handoff_01.md
```

按需要产生文件，不能一开始就生成空的 pilot 结果或交接文档。已有 `papers/`、`my_idea/` 或专题 review 目录时先读并复用；不要因调用 skill 就批量迁移、改名或建立重复论文库。新建项目遵循 `paper/idea/idea_review`；旧布局的迁移单独按用户要求执行。

稳定 idea ID 不随标题改变；明显不同的方向可分支成新 ID，并记录源 idea。人可编辑 `draft.md` 或自己的原稿；需要评审时保存成不可覆盖的 `vNNN.md` 快照。版本间保留内容与来源，不覆盖最初想法。

## 核心循环

1. **独立保留想法。** 接受零散原文、草图或长文。先记录用户的想法，再给 AI 扩展；发散时帮助探索机制和替代路径，不急于用审稿打分淘汰。人可以亲自修改，也可以委托 AI 整理成新版本；AI 代写应标明来源，不能自动标为人的正式决定。
2. **围绕疑问查证。** 优先查最接近、最可能改变判断的工作，保留支持和反面证据。论文共用一份库，不为各 idea 重复复制。记录完整来源、版本/DOI、下载/转换状态、读取范围；只有摘要时不能声称看过全文。Markdown 的表格、公式和图内文字需要时回查 PDF。
3. **绑定版本评审。** 每份 review 注明 idea ID、被评版本路径和 SHA256、评审日期及本轮问题。明确区分原文事实、评审推论、待实验假说；具体指出近邻重合、替代解释、资源约束和最有判别力的下一步。AI 改进建议与人的取舍分别记录。可用 [review 模板](assets/review.md)。
4. **人决定，再改版。** 在 `decisions.md` 简记采纳、拒绝/暂缓、理由及下轮疑问，给出实际用户表达的出处；没有回复时保持“待决定”。不要要求逐条回应整篇 review。获授权后可直接产出新版本，保留差异和来源。
5. **有新信息才复审。** 新的核心假说、直接近邻、人的阅读观察或 pilot 结果都可触发；否则建议阅读、验证或暂停。后续优先写增量 review，保留旧评审。发现版本内容被编辑后哈希不同，就把旧 review 视为针对旧内容；不能悄悄刷新旧绑定使其看似仍有效。
6. **做最小 pilot 再定题。** 选最危险且可观测的假设，用有判别力的简单对照和有限资源验证。执行前写明数据/模型/指标、继续/修改/停止判据与预算；实测结果、日志及限制另存。失败或不确定时回到循环。详见 [pilot 与交接](references/pilot-and-handoff.md)。

整理一次具体循环或决定下一步时，按需读 [运行约定](references/workflow.md)。

## 已有能力按阶段调用

这些是可选协作能力，不是必须安装的整套依赖。调用某个 skill 时先读取其当前 `SKILL.md`，结合用户范围使用，不复制整段规则到每份 review。

| 当前需要 | 可用能力 | 选用边界 |
|---|---|---|
| 广泛了解领域、核对近邻或反证 | `deep-research`；可用学术检索或 web | 小问题定向查证即可，不强制每轮完整综述 |
| PDF → 带图片 Markdown | `marker-pdf-to-md` | 复用已有工具环境；不把普通纯文本提取冒充 Marker 输出 |
| 收敛候选、评估投入价值 | `idea-evaluator` | 选题判断不是录用预测；不默认每轮评分或让评分替人决策 |
| 形成技术路线与论证关系 | `tech-paper-template`；基准方向用 `benchmark-paper-template` | 文献和 pilot 支持什么，方案就主张到什么程度 |
| 精确核对引用 | `nature-ref-verifier` 或直接查原出版来源 | 按需要核实，不要求每轮全量重验 |
| 工程或论文正文 | 对应实现/写作能力 | 本工作流先留下基于实际 pilot 和人的决定的交接材料 |

能力缺失时尽可能完成不依赖它的工作，标清剩余需求；不要未经要求安装外部框架、创建服务或定时任务。研究引用、数据与结果必须可追溯，不能通过反复生成增强证据强度。

## 轻量脚本

`scripts/idea_workspace.py` 只管理目录与原文快照，不替研究者评审、采纳建议或判定定题。以下命令从 `My_research_workflow` 仓库根目录运行；安装为 skill 后，也可从实际安装目录定位脚本。项目位置始终通过显式参数指定：

```bash
# 只读进度，未初始化也不写文件。
python skills/aeons-idea-workflow/scripts/idea_workspace.py \
  status --project-root /absolute/project

# 在用户已要求开始工作流时初始化；保留已有 papers/ 和用户文件。
python skills/aeons-idea-workflow/scripts/idea_workspace.py \
  init --project-root /absolute/project

# 保存原文的新版本；来源文件保留，内容相同时不产生重复版本。
python skills/aeons-idea-workflow/scripts/idea_workspace.py \
  snapshot --project-root /absolute/project \
  --idea-id 001-topic --source-file /absolute/user-idea.md \
  --origin human --reason '独立记录的初始想法'
```

只有确为人的原文才用 `--origin human`；代写或来源不明时使用适当来源标签。`snapshot` 不初始化整套工作区；已存在版本缺少记录、哈希不符或命名异常时，先核查真实历史，不自动补造来源。脚本参数详见其 `--help`。不需要脚本时也可按相同约定维护 Markdown。

## 结束本轮

简要交代：本轮改变了什么、依据是什么、当前仍未知什么、下一步是什么。用户只想讨论时在对话里讨论，不自动生成新文件。需要人的决定时提出影响最大的具体问题，并保留尚未答复的状态。

正式定题须有适用于当前研究问题的实测 pilot 和人的实际决定。可以直接匹配被测版本，也可以记录新旧版本差异与证据适用关系后复用原 run；仅改标题/措辞无需重跑，实质改变被测主张或实验条件时补验证。保留原 run 的版本/哈希，不把旧结果重新绑定到新版本。计划、结果与交接按版本/run ID 保存，保留历史。可按 [handoff 模板](assets/handoff.md)交接到用户指定的工程/论文路径。小规模 pilot 与后续工程执行遵循本轮已给授权和预算，不因安装或调用本 skill 就启动实验。

可借鉴方法的来源与取舍见 [来源说明](references/design-sources.md)；它们是设计参考，不是运行时依赖。
