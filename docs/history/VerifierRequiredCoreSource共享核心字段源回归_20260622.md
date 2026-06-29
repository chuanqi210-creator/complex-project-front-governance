# Verifier Required Core Source 共享核心字段源回归 2026-06-22

## 1. 本轮问题

第 210 节机器看版要求：下一轮优先用真实软件/工程小任务检验 worker 写文件、reviewer 审查、close_agent 生命周期和本地验证的组合。

本轮选择的真实软件维护小题是恢复链验证器自身：`verify_governance_recovery_tool --preset continuous-self-optimization` 的 required 字段先前在 protocol、route、release、changelog、long_log 五个 scope 中重复维护。新增 `agent_topology_selection_trace` 这类核心字段时，需要手工改多处，容易触发既有失败模式 `verifier_required_field_drift`。

本轮目标不是新增一个大规则，而是把该失败模式压实为一个更可维护的工具实现：核心 required 字段只维护一份，scope-specific extras 精确声明，测试必须防止未来退回五份手写列表。

## 2. 代理拓扑选择

```yaml
agent_topology_selection_trace:
  selected_topology: agents_as_tools_worker_plus_reviewer_loop
  final_answer_owner: main_agent
  state_write_boundary: "worker 只允许修改 tools/verify_governance_recovery.py 与 tools/test_verify_governance_recovery.py；reviewer 只读；主代理写协议与恢复链文档。"
  context_boundary: "worker 收到明确文件边界、TDD 要求和验收命令；reviewer 收到需求、文件路径和审查问题，不继承完整会话。"
  dependency_graph: "worker 先改代码；reviewer 复核；主代理本地验证并决定接受；文档写回在代码验收之后。"
  downgrade_to_inline_if: "worker 阻塞、越界修改、测试无法证明核心目标、reviewer 发现 Important 未修复。"
```

subagent_contract_index:

| contract_id | role | agent_id | status | integration_decision |
| --- | --- | --- | --- | --- |
| `contract-verifier-core-source-worker-001` | worker | `019eeef6-c987-7451-939b-d0aacae7aac1` | returned_and_closed | accepted_after_rework |
| `contract-verifier-core-source-reviewer-001` | reviewer | `019eeefa-bc6f-7c32-a9db-4499e736399b` | returned_and_closed | accepted |

## 3. 小题执行证据

micro_task_execution_check:

```yaml
task: 重构恢复链验证器 required 字段源，降低 verifier required 字段漂移风险。
files_allowed:
  - /Users/chuchenqidawang/Documents/ai 科研/tools/verify_governance_recovery.py
  - /Users/chuchenqidawang/Documents/ai 科研/tools/test_verify_governance_recovery.py
worker_red_green:
  first_red:
    command: python3 tools/test_verify_governance_recovery.py
    observed_failure: AttributeError: module has no attribute CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED
  reviewer_rework_red:
    command: python3 tools/test_verify_governance_recovery.py
    observed_failure: missing scope extras should raise ValueError
  final_green:
    - command: python3 tools/test_verify_governance_recovery.py
      observed: ok
    - command: python3 -m py_compile tools/verify_governance_recovery.py tools/test_verify_governance_recovery.py
      observed: exit 0
main_agent_local_checks:
  - all_core_fields_enter_all_five_scopes: true
  - protocol_extras_exact: [spawn_preflight, agent_return_status, subagent_lifecycle_ledger]
  - route_extras_exact: []
  - release_extras_exact: []
  - changelog_extras_exact: [subagent_lifecycle_ledger]
  - long_log_extras_exact: [subagent_lifecycle_ledger]
  - missing_or_extra_scope_extras_raise_ValueError: true
reviewer_result:
  first_review: Important findings on pseudo-shared-source test and missing exact extras test
  re_review: Critical/Important/Minor none; accept
pass_fail: pass
```

## 4. 代码行为变化

`tools/verify_governance_recovery.py`：

1. 新增 `CONTINUOUS_SELF_OPTIMIZATION_SCOPES`。
2. 新增 `CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED`。
3. 新增 `CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS`。
4. 新增 `build_continuous_self_optimization_required(...)`。
5. `CONTINUOUS_SELF_OPTIMIZATION_REQUIRED` 由 helper 生成。
6. helper 显式校验 extras key 必须与五个 scope 完全一致；缺失或多余 scope 抛 `ValueError`。

`tools/test_verify_governance_recovery.py`：

1. 用 AST 断言 `CONTINUOUS_SELF_OPTIMIZATION_REQUIRED` 必须由 `build_continuous_self_optimization_required(...)` 调用生成。
2. 断言 `agent_topology_selection_trace` 等核心字段自动进入五个 scope。
3. 断言 scope extras 精确匹配规格。
4. 断言缺失或多余 scope extras 会抛 `ValueError`。

## 5. 经验沉淀

本轮归入既有失败模式：

- `verifier_required_field_drift`：主协议新增核心治理字段或失败模式，但恢复链 preset 没有同步 required/forbid 检查。

本轮补充子型：

- `verifier_required_core_source_drift`：即使当前字段已同步，如果 required 字段仍在多个 scope 手写复制，未来新增字段仍可能漏改；如果测试只比较内容而不验证生成方式，也会出现伪共享源。

通用修正：

1. 核心字段维护一份。
2. scope 差异用 extras 精确声明。
3. helper 对 scope key 做完整性校验。
4. 测试同时验证行为、生成方式和负向异常。
5. worker 可做边界清楚的代码改动；reviewer 必须审 spec coverage，再审质量风险；主代理保留最终接收权。

## 6. 不能外推

本轮只能证明：

> 对恢复链验证器这个小型 Python 工具，`agents_as_tools_worker_plus_reviewer_loop` 拓扑能完成边界清楚的代码改动、审查返工、生命周期关闭和本地验证。

不能证明：

> 任意软件项目都适合并行 worker，或子代理 review 可以替代主代理最终验收，或外部系统写入可以不经授权直接交给 worker。
