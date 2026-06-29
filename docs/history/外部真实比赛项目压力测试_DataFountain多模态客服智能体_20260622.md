# 外部真实比赛项目压力测试：DataFountain 多模态客服智能体

current_as_of：2026-06-22

来源入口：

1. DataFountain 竞赛列表：`https://www.datafountain.cn/competitions`
2. 具体赛题页：`https://www.datafountain.cn/competitions/1165`

## 一、为什么选择这个项目

本轮必须从现实时间外部项目池中选样本，不能继续从当前工作区或 ai 科研材料里取样。

选择 DataFountain「具有多模态能力的客服智能体设计」的原因：

1. 它是当前可打开的外部真实竞赛项目，赛题页显示赛程覆盖 2026-03-16 至 2026-08-31，其中初赛评审、决赛准备和线下决赛仍与 2026-06-22 的当前时间相关。
2. 它不是支教、社会实践或实验论文，而是 AI 产品/数据竞赛/智能体系统项目，能测试协议是否跨域。
3. 它有真实主办方、奖金、用户规模、A/B 榜、提交物、评分维度和决赛机制。
4. 它天然暴露“比赛成绩是否等于真实服务能力”的治理问题。

## 二、赛题事实抽取

| 字段 | 本轮抽取事实 | 来源层级 | 备注 |
| --- | --- | --- | --- |
| 项目名称 | 具有多模态能力的客服智能体设计 | B 平台/赛事页 | 需以赛题页为准 |
| 主办方 | 中国电子学会 & 睿创微纳 | B 平台/赛事页 | 如果进入正式报告，应继续核验主办方官网或通知 |
| 赛程 | 报名和初赛提交从 2026-03-16 到 2026-06-20；初赛评审 2026-06-21 到 2026-07-05；决赛名单 2026-07-06；决赛准备到 2026-08 中下旬 | B 平台/赛事页 | current_as_of 2026-06-22 时，报名/初赛提交已结束，初赛评审进行中 |
| 任务 | 基于举办方材料构建知识库，设计多模态客服智能体，回答用户问题 | B 平台/赛事页 | 任务含 RAG、多模态理解、多轮对话、幻觉抑制 |
| 数据/支持 | 20 万字以上说明书及插图；AB 榜单；约 400 道客服问题；LLM 裁判评分 | B 平台/赛事页 | 原始数据需登录/下载后再核验 |
| 评分信号 | 页面给出 1-5 分质量等级，关注回答是否回应问题、结构、图文配合和理解提升 | B 平台/赛事页 | 需要建立 LLM judge 校准和人工抽检 |
| 可外推边界 | 只能说明竞赛规则下的提交表现，不能直接说明可部署客服系统质量 | 本轮推断 | 需要运行期、成本、安全、隐私、人工兜底等额外证据 |

## 三、该项目暴露的协议缺口

### 缺口 1：竞赛成绩不等于真实部署能力

一个智能体在 A/B 榜或 LLM 裁判下表现好，并不自动说明它可以进入真实客服场景。

真实服务还需要回答：

1. 是否能处理赛题外用户问题。
2. 是否能在低延迟、低成本、稳定并发下运行。
3. 是否有人工转接和失败兜底。
4. 是否有隐私、日志、合规和数据留存方案。
5. 是否能识别说明书之外的问题并拒答或澄清。

### 缺口 2：LLM 裁判不是免审计的“客观指标”

LLM 裁判能提高评测效率，但不能自动代表真实用户满意度或业务价值。

必须追踪：

1. 裁判提示词和评分维度是否稳定。
2. 是否有人工样本复核。
3. 是否测试裁判偏差、长度偏好、格式偏好和幻觉漏判。
4. 是否存在针对裁判的提示工程过拟合。
5. A 榜和 B 榜是否能有效防止 leaderboard 过拟合。

### 缺口 3：AI 作品容易从“演示系统”滑向“产品承诺”

比赛项目往往要求提交结果、代码、文档或演示，但真实产品还需要：

1. 运行环境和依赖锁定。
2. 模型版本、知识库版本和数据更新时间。
3. 错误样例库和 bad case 处置流程。
4. 用户体验指标：澄清率、一次解决率、转人工率、误导率。
5. 维护责任：谁更新知识库，谁处理模型退化，谁审核高风险回答。

## 四、需要新增的协议结构

建议新增 `competition_to_deployment_trace`：

```yaml
competition_to_deployment_trace:
  project_name:
  project_type: data_competition | ai_agent | product_demo | social_practice | entrepreneurship | research_project | open_source
  source_url:
  current_as_of:
  competition_stage:
  official_task:
  official_deliverables:
  evaluation_metric_or_judge:
  leaderboard_or_review_process:
  baseline_or_comparison:
  data_access_and_split:
  leakage_or_overfitting_risks:
  reproducibility_requirements:
  demo_to_deployment_gap:
  real_user_or_field_validation_needed:
  safety_privacy_compliance_risks:
  cannot_claim_from_competition_score:
```

## 五、最小结论门

如果后续要用比赛成绩、赛题案例或 AI 智能体作品支撑项目汇报，必须至少满足：

1. 写清赛题页 current_as_of 和赛程状态。
2. 区分官方任务、平台评分、团队实现、真实场景价值。
3. 说明 leaderboard / LLM judge 只能支撑什么，不能支撑什么。
4. 给出真实部署前必须补的验证：用户测试、人工复核、bad case、成本延迟、安全隐私、人工兜底。
5. 如果没有运行期证据，最终只能写“竞赛场景下的方案表现”或“可部署潜力”，不能写成“已经解决真实客服问题”。

## 六、协议修正目标

本轮应写回协议的新约束：

1. AI、数据科学、算法竞赛、智能体、产品 demo 类项目，必须维护 `competition_to_deployment_trace`。
2. 新失败模式命名为 `leaderboard_reality_gap`：把竞赛成绩、榜单分数、LLM 裁判或 demo 效果误当成真实世界可用性。
3. 执行前闸门新增：是否区分官方赛题指标、团队实现证据、真实部署验证和不能外推的结论。
