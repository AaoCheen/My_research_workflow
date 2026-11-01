# 设计参考与取舍

以下官方资料于 2026-10-31 的工作流讨论中核查。这里借鉴机制，不把它们作为本 skill 的安装依赖，也不复制其完整流程；使用时以研究者当前要求和本地材料为准。

| 来源 | 借鉴内容 | 本工作流的边界 |
|---|---|---|
| [K-Dense scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-brainstorming/SKILL.md) | 独立记录想法、稳定 ID 与来源、保留分歧和决策理由 | 人决定投入；不自动用评分选赢家 |
| [K-Dense scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md) | 先提取证据，再写有来源位置、影响、不确定性和改法的评论 | 不把“未报告”当“未做”，不默认给所有 AI 研究套医学证据分级 |
| [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 先理解现有材料和人的目标，再讨论方案与实施 | 不强制完整软件规划流程，不增加重复审批 |
| [Stanford Co-STORM](https://github.com/stanford-oval/storm) | 由来源支持的多视角提问，允许人主动引导讨论 | 只在复杂问题有收益时使用多视角；不要求部署其系统 |
| [Google AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) | 将生成、反思和演化分开 | AI 反馈不是实验验证；不默认自动循环或排名定题 |

本地已有的检索、Marker、选题评估与研究结构 skill 按当前任务需要调用。单纯引用这里的来源不表示本机已安装这些外部项目。
