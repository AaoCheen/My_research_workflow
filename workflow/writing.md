# 论文结构、起草、修改与核查

先明确目标稿件、章节、已有证据、术语约定，以及本轮是搭结构、起草还是改现稿。沿用项目既有论文目录；新项目可用 `writing/`。

| 当前需要 | 使用哪个 skill | 给它什么 |
| --- | --- | --- |
| 理清研究问题与全文论证关系 | [tech-paper-template](../skills/tech-paper-template/SKILL.md) | 问题、近邻、方法、已有结果与不足 |
| 组织 Benchmark / Evaluation 论文 | [benchmark-paper-template](../skills/benchmark-paper-template/SKILL.md) | 构建流程、评测框架、实验发现与适用边界 |
| 从材料起草章节或全文 | [paper-writer](../skills/paper-writer/SKILL.md) | 可追溯的作者材料、已确认结果、目标章节 |
| 专门写或重组 Introduction | [intro-drafter](../skills/intro-drafter/SKILL.md) | 背景、问题、挑战、方案与贡献材料 |
| 修改已有文字或做学术中译英 | [paper-polish](../skills/paper-polish/SKILL.md) | 原文、目标语气、术语和允许调整的范围 |
| 减少空泛、机械重复和模板化表达 | [academic-humanizer](../skills/academic-humanizer/SKILL.md) | 现稿与必须保留的含义、证据强度和术语 |
| 核对引用信息 | [nature-ref-verifier](../skills/nature-ref-verifier/SKILL.md) | 参考文献列表与能获取的原始来源 |
| 投稿前整体检查 | [pre-submission-reviewer](../skills/pre-submission-reviewer/SKILL.md) | 当前完整稿件、格式要求、图表与引用 |

按问题选 skill；不必把同一段落依次送过所有修改工具。正文、参考文献和图表分别留在实际项目中，不回写到 skills 的指令文件。

## 两种常用任务

从材料起草：

```text
工作项目：/absolute/project；目标文件：……。
使用 paper-writer，依据……起草……章节。
术语约定见……，能使用的结果和来源见……。
无法确认的论据先列为问题，不补写不存在的数据或引用。
```

修改现稿：

```text
工作项目：/absolute/project；目标文件：……。
使用 paper-polish，只修改本轮指定段落，
保持研究含义、证据强度和项目术语；需要改变科学含义时单独指出。
本轮重点是……。
```

项目已有明确段落顺序、双语同步或术语约定时，把对应文件一起交给 LLM。会话中的写作取舍可记入 `sessions/`；稿件以实际目标文件为准。
