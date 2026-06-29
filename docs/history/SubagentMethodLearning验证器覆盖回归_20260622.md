# Subagent Method Learning 验证器覆盖回归

current_as_of: 2026-06-22

## 一、本轮问题

第 182 节已经把 `subagent_method_learning_trace` 写入主协议、路由表、发布包、变更清单和长日志，但 `verify_governance_recovery_tool --preset continuous-self-optimization` 的 required 覆盖只检查到 `source_authority_precedence_trace`，没有检查 `subagent_method_learning_trace`。

这会造成一个恢复链缺口：后续如果有人删掉或遗漏 `subagent_method_learning_trace`，综合恢复链仍可能返回 `failure_count: 0`，让“学习网上方法、skill、插件来提升子代理能力”退回装饰性引用。

## 二、小题执行

```yaml
micro_task_execution_check:
  task: 构造一个临时恢复链 fixture，保留 source_authority_precedence_trace，但删除 subagent_method_learning_trace
  expected_behavior: verifier preset 必须失败，并指出 protocol / route / long_log 缺少 subagent_method_learning_trace
  observed_before_fix: verifier 返回 failure_count 0，测试失败
  observed_after_fix: verifier 返回对应缺字段失败，完整测试套件输出 ok
  pass_fail: pass_after_fix
```

## 三、红绿测试

新增测试：

`/Users/chuchenqidawang/Documents/ai 科研/tools/test_verify_governance_recovery.py::test_preset_fails_when_subagent_method_learning_trace_missing`

红灯：测试构造的 fixture 包含 `verify_governance_recovery_tool`、`subagent_problem_decomposition_builder`、`source_role_map`、`skill_plugin_learning_loop`、`skill_plugin_project_fit_trace`、`source_authority_precedence_trace`，但不含 `subagent_method_learning_trace`。旧 verifier 返回 `failure_count: 0`，触发断言失败。

绿灯：`/Users/chuchenqidawang/Documents/ai 科研/tools/verify_governance_recovery.py` 将 `subagent_method_learning_trace` 加入 continuous-self-optimization preset 的 protocol / route / release / changelog / long_log required 覆盖。随后 `python3 tools/test_verify_governance_recovery.py` 输出 `ok`。

## 四、规则晋升边界

```yaml
rule_promotion_mechanism:
  candidate_rule_or_lens: subagent_method_learning_field_coverage
  source_experience_entries:
    - NASA_ORBIT来源权威优先级与子代理方法学习回归_20260622
    - SubagentMethodLearning验证器覆盖回归_20260622
  repeated_across_projects: yes
  abstracts_to_common_failure_mode: yes
  improves_new_domain_construction: yes
  anti_protocol_bloat_gate:
    trigger_signal: 新增核心治理字段后 verifier required 未同步
    observable_behavior: 缺字段 fixture 仍返回 failure_count 0
    required_evidence_or_check: red-green test + real recovery preset
    route_back_if_failed: 修 verifier preset，再更新机器看版
    user_friction_impact: low
  decision: write_to_protocol_and_verifier
```

## 五、失败模式

本轮归入既有失败模式 `verifier_required_field_drift`：主协议新增核心治理字段后，恢复链 preset 没有同步 required/forbid 检查，导致关键字段遗漏时恢复链仍误报通过。

