# Skill/Plugin 学习闭环回归

current_as_of：2026-06-22

## 一、本轮缺口

用户提出：可以通过学习网上的方法、skill、插件等，提升构建子代理解决问题的能力，并融入主协议。

旧协议已有 `skill_plugin_discovery_record`，也要求主代理读取必要 skill/plugin 指令，但它只证明“发现过、读过或准备转包给子代理”。缺少一等公民级闭环：发现问题、读完指令、抽取硬约束、小题试用、采纳/拒收、写回协议、同步验证器、恢复链记录。

本轮新增失败模式：

`skill_plugin_learning_loop_gap`：用户明确要求学习网上方法、skill 或插件，或任务明显触发某个 skill/plugin，但协议只记录了发现名称，没有证明主代理读完指令、抽取硬约束、完成小题试用、写回规则、同步验证器和恢复链引用，导致“学过”无法迁移成下一次可执行能力。

## 二、学习材料与来源角色

| 来源 | 本轮证据角色 | 可支撑内容 | 不可支撑内容 |
| --- | --- | --- | --- |
| 本地 `superpowers:using-superpowers` | skill 使用规则 | 触发 skill 后必须读取当前 `SKILL.md`，不能靠记忆 | 不能替代具体任务的验收 |
| 本地 `superpowers:test-driven-development` | 变更纪律 | 新增验证器行为先写红灯测试，再写实现 | 不能证明协议文本已经同步 |
| 本地 `superpowers:verification-before-completion` | 完成前验证纪律 | 成功声明前必须运行新鲜验证命令 | 不能替代人工判断 |
| 本地 `superpowers:dispatching-parallel-agents` | 子代理拆题方法 | 独立问题按边界清楚的任务分派，并行后主代理整合 | 不能授权无边界并行写文件 |
| 本地 `superpowers:subagent-driven-development` | 子代理执行方法 | fresh subagent per task，先 spec review 再 quality review | 不要求每个小改都 spawn |
| `tool_search` 发现的 `multi_agent_v1` | 当前工具能力 | 可实际 spawn / wait / close 子代理 | 不能证明子代理结果无需复核 |
| OpenAI Agents SDK multi-agent docs | 外部方法参照 | manager / handoff / tool-orchestration 可以组合，主控需保留整合责任 | 不能证明本地协议字段自动正确 |
| Microsoft AutoGen agent docs | 外部方法参照 | assistant agent 可作为工具型协作者，设计选择影响可靠性 | 不能证明通用 agent 适合所有任务 |

参考链接：

1. https://openai.github.io/openai-agents-python/multi_agent/
2. https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html

## 三、子代理只读审计

本轮实际调用两个只读审计子代理：

```yaml
subagent_lifecycle_ledger:
  - contract_id: audit_skill_plugin_loop_protocol_gap_20260622
    agent_id: 019eee20-177a-7963-93f7-d8479a875a10
    role: read_only_audit
    agent_return_status: done
    accepted_items:
      - skill_plugin_learning_loop
      - instruction_read_status
      - practice_micro_task_ref
      - adoption_decision
      - protocol_writeback_ref
      - verifier_requirement_ref
      - recovery_chain_ref
    integration_decision: accepted
    close_status: closed
  - contract_id: audit_skill_plugin_recovery_gap_20260622
    agent_id: 019eee20-33de-7cb3-9ad7-01860dac474c
    role: read_only_audit
    agent_return_status: done
    accepted_items:
      - real_recovery_chain_smoke_test
      - current_board_should_carry_actual_tool_and_subagent_state
      - changelog_stale_text_fix
    integration_decision: accepted
    close_status: closed
```

采纳原因：两个审计都指向同一个缺口，即 skill/plugin 学习没有闭环；第二个审计还提醒，增强 verifier 后真实恢复链会先失败，必须同步主协议、路由表、发布包、变更清单和长日志。

未采纳边界：没有把每一种插件或 skill 写成具体模板，避免重新走“场景覆盖式目录”的旧问题。

## 四、小题实测回归

```yaml
micro_task_execution_check:
  task: 让恢复链验证器在缺少 skill_plugin_learning_loop 时失败
  input_material:
    - tools/verify_governance_recovery.py
    - tools/test_verify_governance_recovery.py
  action_taken:
    - 先新增缺字段夹具和断言
    - 运行测试观察旧 verifier 误报通过
    - 再把 skill_plugin_learning_loop 纳入 preset required
    - 更新完整夹具使通过样例包含新字段
  actual_execution_evidence:
    red_test: python3 tools/test_verify_governance_recovery.py 曾因旧 verifier 返回 failure_count 0 而失败
    green_test: python3 tools/test_verify_governance_recovery.py 输出 ok
  observed_result: verifier 能区分“只有旧子代理字段”和“已有 skill/plugin 学习闭环字段”
  pass_fail: pass
  remaining_gap: 下一轮应用到真实项目或复杂交付，不只继续修工具字段
```

## 五、写回协议

写回文件：

1. `/Users/chuchenqidawang/Desktop/复杂项目启动前置治理协议_v3_核心版.md`
2. `/Users/chuchenqidawang/Documents/ai 科研/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md`
3. `/Users/chuchenqidawang/Documents/ai 科研/tools/verify_governance_recovery.py`
4. `/Users/chuchenqidawang/Documents/ai 科研/tools/test_verify_governance_recovery.py`
5. `/Users/chuchenqidawang/Documents/ai 科研/前置治理协议发布包_20260622.md`
6. `/Users/chuchenqidawang/Documents/ai 科研/持续优化变更清单_20260622.md`
7. `/Users/chuchenqidawang/Documents/ai 科研/前置治理协议_二十个跨渠道项目逆向校验实验.md`

新增或收紧字段：

```yaml
skill_plugin_learning_loop:
  trigger:
  discovery_question:
  selected_skill_or_plugin:
  instruction_source:
  instruction_read_status: not_needed | read_complete | read_blocked
  key_constraints_extracted:
  practice_micro_task_ref:
  practice_result: not_needed | pass | fail | blocked
  adoption_decision: adopt | partially_adopt | reject | backlog
  protocol_writeback_ref:
  verifier_requirement_ref:
  recovery_chain_ref:
```

## 六、规则晋升判断

```yaml
anti_protocol_bloat_gate:
  new_rule_or_trace: skill_plugin_learning_loop
  trigger_signal: 用户要求学习网上方法、skill、插件，或任务显然触发本地 skill/plugin
  observable_behavior: 机器看版能看到读完状态、小题证据、采纳决定、写回和验证器引用
  required_evidence_or_check: verify_governance_recovery_tool preset 缺字段会失败
  route_back_if_failed: 回到阶段 3 补学习闭环，而不是继续写抽象经验
  user_friction_impact: 不增加用户字段负担，由 AI 自动填写
  replaces_or_tightens_existing_rule: 收紧 skill_plugin_discovery_record
  decision: write_to_protocol
```

## 七、下一轮约束

下一轮如果继续提升 agent/subagent 能力，应优先选择真实项目或真实交付中的任务，使用 `skill_plugin_learning_loop` 记录学到的 skill/plugin 是否真能降低摩擦、减少幻觉或提高交付质量。若恢复链已经通过，不应连续停留在 verifier 字段层。
