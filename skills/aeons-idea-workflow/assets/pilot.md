# {{idea_title}} — 最小 pilot

按当前需要使用“计划”或“结果”部分，分别生成如 `v002_pilot_01_plan.md` 与 `v002_pilot_01_result.md` 的文件；每个 run 独立保留。结果只在有实际执行记录后生成；无关项可以省略。

## 计划

- 对应 idea / SHA256：{{idea_version_path_and_hash}}
- Pilot / run ID：{{pilot_and_run_id}}
- 计划记录时间：{{planned_at}}
- 最危险的假设：{{critical_hypothesis}}
- 最小可区分预测：{{discriminating_prediction}}
- 数据/划分/来源/可见信息：{{data_and_information_access}}
- 方法与强简单对照：{{method_and_baseline}}
- 指标、重复或不确定性处理：{{metrics_and_uncertainty}}
- 时间/算力/API 等资源上限：{{resource_budget}}
- 继续、修改或停止的观察判据：{{advance_revise_stop_criteria}}
- 运行环境、配置与产物路径：{{planned_execution_and_artifacts}}
- 尚缺条件与本轮授权范围：{{missing_conditions_and_scope}}

## 实际结果

- 对应原计划 / SHA256 / run ID：{{plan_path_hash_and_run_id}}
- 实际执行时间、版本与条件：{{actual_execution}}
- 命令/配置/日志/原始输出：{{evidence_links}}
- 与计划的偏离及原因：{{deviations}}

| 方法 | 同条件下的实测结果 | 资源消耗 | 不确定性/限制 |
|---|---|---|---|
| {{method}} | {{measured_result}} | {{measured_cost_or_unmeasured}} | {{limitations}} |

{{supported_refuted_or_unresolved_hypothesis_and_next_action}}

研究者看过结果后的决定：{{actual_decision_and_source_or_pending}}
