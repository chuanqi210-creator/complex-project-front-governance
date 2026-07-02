import { useEffect, useMemo, useState } from "react";
import {
  ArrowsSplit,
  Books,
  BracketsCurly,
  ChartLineUp,
  CheckCircle,
  ClipboardText,
  Compass,
  Database,
  FileMagnifyingGlass,
  FlowArrow,
  GraduationCap,
  Graph,
  HouseLine,
  MapTrifold,
  Package,
  Path,
  PuzzlePiece,
  RocketLaunch,
  SealCheck,
  ShieldCheck,
  Stack,
  Target,
  UsersThree,
  WarningDiamond,
} from "@phosphor-icons/react";
import blueprintImage from "./assets/project-launch-blueprint.png";

const pages = [
  { id: "overview", label: "概览", icon: HouseLine },
  { id: "capabilities", label: "能力", icon: Stack },
  { id: "mechanism", label: "机制", icon: FlowArrow },
  { id: "scenarios", label: "场景", icon: MapTrifold },
  { id: "advantages", label: "优势", icon: ChartLineUp },
];

const coreOutcomes = [
  {
    title: "把厚协议压缩成稳定行为",
    text: "新项目先执行 7 个行为内核：恢复状态、判断项目性质、划清决策权、抓最高杠杆问题、轻量验证、按对象交付、留下恢复线索。",
    icon: Target,
  },
  {
    title: "先分清模型发现还是证据填充",
    text: "框架未定时保护候选路径和可区分探针；模型与指标已定时直接补证据、验证和交付边界，避免过早收敛或过度发散。",
    icon: ShieldCheck,
  },
  {
    title: "让 AI 动态判断，但守住护栏",
    text: "可逆、低副作用的路线、工具、Loop 和分工由 AI 自行判断；目标、授权、外部写入、不可逆动作和高风险主张必须回问。",
    icon: PuzzlePiece,
  },
  {
    title: "用样例和回归提高迁移稳定性",
    text: "行为回归包固定高风险入口，两个 Runtime Kit 黄金样例展示 evidence_fill 与 model_discovery 应该怎样短而可恢复地落地。",
    icon: UsersThree,
  },
];

const assets = [
  {
    name: "v3 主协议",
    role: "定义行为内核、双剖面项目性质、自适应判断、Loop 小闭环、评分迭代、风险边界和恢复规则。",
    file: "protocol/Complex项目持续治理协议_v3_核心版.md",
  },
  {
    name: "低摩擦入口",
    role: "把厚协议压缩成用户可以自然说出的持续治理入口。",
    file: "protocol/Complex项目持续治理_低摩擦用户入口_20260622.md",
  },
  {
    name: "路由表与经验库",
    role: "用大类路由和失败模式校准新项目，不再复制具体领域长模板。",
    file: "protocol/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md",
  },
  {
    name: "发布包与验证器",
    role: "把当前能力、恢复入口、变更清单和本地 verifier 绑定起来。",
    file: "protocol/持续治理协议发布包_20260622.md",
  },
  {
    name: "行为回归包",
    role: "用 8 个高风险入口检查关键触发器、禁止行为和 Runtime Kit 记录是否仍被当前文档覆盖。",
    file: "docs/behavior_regression_cases_20260702.json",
  },
  {
    name: "黄金样例",
    role: "展示 evidence_fill 和 model_discovery 两类项目的最小可用运行现场。",
    file: "docs/examples/",
  },
];

const capabilityGroups = [
  {
    title: "行为内核",
    summary: "先做 7 个稳定行为，再查具体 gate 名称。",
    detail:
      "complex_behavior_kernel 把新项目推进压缩为：恢复真实状态、判断项目性质、划清决策权、抓最高杠杆问题、轻量验证/执行、按对象交付、留下 next_route。",
    icon: FileMagnifyingGlass,
  },
  {
    title: "双剖面运行",
    summary: "区分证据填充型、模型发现型、混合型和执行交付型。",
    detail:
      "project_nature_router 决定本轮权重：固定模型任务少发散，未定框架任务先保留候选框架、IBIS 论据图和可区分探针。",
    icon: Graph,
  },
  {
    title: "自适应判断",
    summary: "让 AI 自行处理可逆细节，只在真实边界处回问。",
    detail:
      "adaptive_judgment_controller 与 decision_rights_matrix 区分 AI 可自主判断、需要用户确认、需要人工操作或必须阻塞的事项。",
    icon: Compass,
  },
  {
    title: "能力发现与编排",
    summary: "显性复盘 skill、工具、插件、connector、API、外部方法和子代理，但不机械打断。",
    detail:
      "能力和拓扑复查以事件触发为主；无事件时 lightweight keep，外部写入、账号、付款和发布必须进入授权护栏。",
    icon: PuzzlePiece,
  },
  {
    title: "真实小题验证",
    summary: "在大投入前先跑 5-30 分钟小题，暴露证据、执行或边界缺口。",
    detail:
      "micro_task_execution_check 要求有实际输入、执行证据、观察结果、pass/fail、remaining_gap 和 downgrade_rule，防止只写 expected behavior。",
    icon: CheckCircle,
  },
  {
    title: "高风险与外部状态边界",
    summary: "涉及外部系统、隐私、部署、交易、数据和安全时先降级、先授权。",
    detail:
      "external_state_write_guard、integration_lifecycle_gate、security_incident_response_guard、data_artifact_lineage_freshness_guard 和 software_delivery_state_boundary_guard 负责阻止越级表述。",
    icon: WarningDiamond,
  },
  {
    title: "交付物新鲜度",
    summary: "源文件改了，就检查 Word、PDF、网页、图片、发布包是否过期。",
    detail:
      "rendered_artifact_freshness、release_package_freshness 和 change_inventory 把源稿、渲染物、发布说明和恢复入口绑定，避免最终交付物 stale。",
    icon: Package,
  },
  {
    title: "行为回归与黄金样例",
    summary: "用用例和填好样例验证新代理能否稳定落地。",
    detail:
      "behavior_regression_pack 覆盖 8 个高风险入口；docs/examples 给出 evidence_fill 和 model_discovery 的最小可恢复运行现场。",
    icon: ClipboardText,
  },
];

const mechanismSteps = [
  {
    k: "01",
    title: "恢复真实状态",
    text: "先区分 current_basis、not_current_basis、用户最新请求、旧草稿和历史记录。",
    output: "current_basis",
  },
  {
    k: "02",
    title: "判断项目性质",
    text: "先分清 evidence_fill、model_discovery、mixed 或 execution_delivery，以及当前是否已收敛。",
    output: "project_nature_router",
  },
  {
    k: "03",
    title: "划清决策权",
    text: "默认强自治+护栏：AI 处理可逆低副作用细节，目标、授权、不可逆和高风险主张回问。",
    output: "decision_rights_matrix",
  },
  {
    k: "04",
    title: "抓最高杠杆问题",
    text: "每轮只处理最能降低返工或推动交付的主问题，不被局部资料缺口和工具兴趣劫持。",
    output: "round_goal",
  },
  {
    k: "05",
    title: "轻量验证或执行",
    text: "按不确定性和副作用选择 no-op、小 Loop、工具烟测、只读子代理或直接执行。",
    output: "loop / probe",
  },
  {
    k: "06",
    title: "按对象交付",
    text: "人看版、机器恢复版、老师/专家/第三方版分开，不把机器字段直接包装成人话。",
    output: "delivery_contract",
  },
  {
    k: "07",
    title: "留下恢复线索",
    text: "写清 next_route、route_reason、未决问题、能力/拓扑状态和必要回滚路线。",
    output: "next_route",
  },
];

const gateTypes = [
  {
    name: "always minimum",
    zh: "常驻最小",
    examples: "current_basis、evidence_matrix、decision_log、traceability_matrix",
  },
  {
    name: "risk based",
    zh: "风险触发",
    examples: "安全、隐私、交易、部署、数据谱系、软件交付状态",
  },
  {
    name: "continuous only",
    zh: "连续优化专用",
    examples: "meta project profile、iteration quality bar、trigger continuation",
  },
  {
    name: "recovery only",
    zh: "恢复链专用",
    examples: "latest board tail check、append EOF、recovery verifier",
  },
];

const scenarios = [
  {
    id: "research",
    label: "研究 / 数据 / 模型",
    icon: Database,
    claim: "模型、数据集或研究结论是否能支撑当前项目判断。",
    lenses: ["claim_ladder", "evidence_contract", "execution_validation", "data_artifact_lineage_freshness_guard"],
    outputs: ["数据产物谱系", "字段证据状态", "复现与刷新边界", "不能外推结论"],
    downgrade: "没有来源快照、质量验证或复现配方时，只能写 source-backed 或待复现，不能写可决策。",
  },
  {
    id: "software",
    label: "软件 / 开源 / 产品",
    icon: BracketsCurly,
    claim: "代码、PR、CI、release 或 package 到底证明了哪一级交付状态。",
    lenses: ["execution_validation", "operation_handoff", "software_delivery_state_boundary_guard", "integration_lifecycle_gate"],
    outputs: ["issue/PR/CI/release 状态表", "部署与真实使用缺口", "rollback/monitoring 边界", "交付推进清单"],
    downgrade: "PR 合并或 CI 通过不能外推为生产可用；缺 release、deployment、usage 证据时必须停在对应状态。",
  },
  {
    id: "education",
    label: "教育 / 公共服务",
    icon: GraduationCap,
    claim: "课程、支教、公益或公共服务是否真的改善了对象状态，而不是只完成活动。",
    lenses: ["stakeholder_context", "risk_ethics_permission", "execution_validation", "claim_lane_binding"],
    outputs: ["服务对象与授权边界", "活动产出到结果证据链", "低摩擦反馈闸门", "公共成效降级规则"],
    downgrade: "活动场次、照片或宣传材料只能证明执行发生，不能直接证明学习成效、服务改善或长期影响。",
  },
  {
    id: "governance",
    label: "组织 / 商业 / 治理",
    icon: UsersThree,
    claim: "资源配置、政策方案、商业模式或组织流程是否具备可执行与可追踪依据。",
    lenses: ["decision_log", "stakeholder_context", "operation_handoff", "source_authority_precedence_trace"],
    outputs: ["关键取舍记录", "权威来源优先级", "执行责任与申诉边界", "验收与复盘路径"],
    downgrade: "方案获批、名单发布或合同存在不能自动证明公平、履约完成、商业可行或治理有效。",
  },
  {
    id: "culture",
    label: "传播 / 文化 / 设计",
    icon: Books,
    claim: "传播作品、文化活动、设计方案是否能支撑理解、参与、转化或长期影响。",
    lenses: ["deliverable_storyline", "stakeholder_context", "execution_validation", "transfer_boundary"],
    outputs: ["受众与场景假设", "传播证据分层", "作品到行动的链条", "影响边界说明"],
    downgrade: "曝光、获奖或内容发布不能直接证明认知改变、行为转化或文化传承效果。",
  },
  {
    id: "risk",
    label: "高风险横切",
    icon: ShieldCheck,
    claim: "健康、安全、法律、隐私、财务、未成年人等风险是否已被授权、降级或转人工。",
    lenses: ["risk_ethics_permission", "external_state_write_guard", "security_incident_response_guard", "deployment_readiness_gate"],
    outputs: ["授权与敏感数据边界", "外部写入守卫", "部署/披露/监控证据", "manual_action_required"],
    downgrade: "缺授权、回滚、监控、隐私或监管证据时，只能做只读分析或小闭环，不能代为执行高影响动作。",
  },
];

const comparisonRows = [
  ["推进方式", "先讨论方案或直接执行", "先建立主张、证据、资源边界和阶段路由"],
  ["项目范围", "容易被当前材料或熟悉领域收窄", "用新领域构造器覆盖真实项目与跨域场景"],
  ["工具使用", "临时想起、临时调用、难复盘", "任务开始与阶段切换时显性复盘能力候选和拒绝理由"],
  ["风险管理", "执行后才发现证据、授权或交付边界不够", "执行前给出 downgrade_rule 和 claim readiness"],
  ["复杂度控制", "要么过度表格化，要么完全黑箱", "机器字段内部承担，用户可见层压缩到高杠杆信息"],
  ["停止条件", "持续优化容易空转", "有 trigger-based continuation 和 iteration quality bar"],
  ["恢复能力", "依赖聊天记忆", "用机器看版、变更清单、发布包和 verifier 恢复"],
];

function useHashRoute() {
  const normalize = () => {
    const id = window.location.hash.replace("#", "");
    return pages.some((page) => page.id === id) ? id : "overview";
  };
  const [route, setRoute] = useState(normalize);

  useEffect(() => {
    const onHashChange = () => setRoute(normalize());
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  const go = (id) => {
    window.location.hash = id;
    setRoute(id);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return [route, go];
}

function IconBadge({ icon: Icon, tone = "green" }) {
  return (
    <span className={`icon-badge ${tone}`} aria-hidden="true">
      <Icon size={22} weight="duotone" />
    </span>
  );
}

function Header({ route, go }) {
  return (
    <header className="site-header">
      <button className="brand" type="button" onClick={() => go("overview")}>
        <span className="brand-mark" aria-hidden="true">
          <RocketLaunch size={24} weight="fill" />
        </span>
        <span>
          <strong>Complex 项目持续治理</strong>
          <small>Complex Project Continuous Governance</small>
        </span>
      </button>
      <nav className="main-nav" aria-label="页面导航">
        {pages.map((page) => {
          const Icon = page.icon;
          return (
            <button
              className={route === page.id ? "nav-item active" : "nav-item"}
              type="button"
              key={page.id}
              onClick={() => go(page.id)}
            >
              <Icon size={18} weight="duotone" />
              <span>{page.label}</span>
            </button>
          );
        })}
      </nav>
    </header>
  );
}

function Overview({ go }) {
  return (
    <div className="page-stack">
      <section className="hero-section">
        <img className="hero-image" src={blueprintImage} alt="项目治理蓝图视觉图，展示证据地图、风险边界和持续治理流程" />
        <div className="hero-overlay">
          <p className="eyebrow">适用于复杂项目持续推进</p>
          <h1>把复杂项目，推进成可恢复、可验证、可交付的连续行动</h1>
          <p className="hero-copy">
            这套持续治理协议不是一串 gate 名称，而是一套行为内核：每轮先恢复真实状态，判断项目性质和决策边界，再选择一个最高杠杆问题，用最轻有效动作推进，并留下下一轮能接上的恢复线索。
          </p>
          <div className="hero-actions">
            <button className="primary-action" type="button" onClick={() => go("mechanism")}>
              看它如何运行
            </button>
            <button className="secondary-action" type="button" onClick={() => go("capabilities")}>
              查看治理能力
            </button>
          </div>
        </div>
      </section>

      <section className="intro-grid">
        <div className="intro-panel">
          <p className="section-kicker">它解决的问题</p>
          <h2>复杂项目最大的风险，往往来自“规则很多，但本轮行为不稳”。</h2>
          <p>
            项目推进中最容易把目标说大、把证据看轻、把工具当能力、把局部资料缺口当主线。Complex 现在先用行为内核压缩复杂度，再按项目性质选择模型发现、证据填充、执行交付或混合路线。
          </p>
        </div>
        <div className="signal-list">
          {coreOutcomes.map((item) => (
            <article className="signal-card" key={item.title}>
              <IconBadge icon={item.icon} />
              <div>
                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="deliverables-section">
        <div className="section-heading">
          <p className="section-kicker">最终交付给项目的东西</p>
          <h2>不是更多流程，而是更清楚的行动条件。</h2>
        </div>
        <div className="deliverable-grid">
          {[
            ["问题与价值主张", "项目到底要解决什么，成功主张如何被验证。"],
            ["证据地图", "已有材料、权威来源、现场证据和未知缺口分别在哪里。"],
            ["能力与工具计划", "当前应使用哪些 skill、工具、API、子代理，哪些不该用。"],
            ["小题验证方案", "用最低成本先验证最危险假设或最高杠杆链路。"],
            ["风险边界说明", "哪些话不能说满，哪些动作要授权，哪些结论要降级。"],
            ["执行与恢复看版", "下一步路线、交付物、验证命令和机器可恢复状态。"],
          ].map(([title, text]) => (
            <article className="deliverable-card" key={title}>
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="asset-section">
        <div className="section-heading">
          <p className="section-kicker">我们已经把它做成了什么</p>
          <h2>一套可维护的协议系统，而不是一句提示词。</h2>
        </div>
        <div className="asset-table">
          {assets.map((asset) => (
            <article className="asset-row" key={asset.name}>
              <div>
                <strong>{asset.name}</strong>
                <p>{asset.role}</p>
              </div>
              <code>{asset.file}</code>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

function Capabilities() {
  const [open, setOpen] = useState(capabilityGroups[0].title);
  return (
    <div className="content-page">
      <PageTitle
        label="协议能做什么"
        title="它把复杂项目推进，压缩成少数稳定行为。"
        copy="这些能力不是每次全量展开。协议先判断项目性质和自治边界，再按不确定性、风险和交付对象动态激活需要的能力。"
      />
      <div className="capability-layout">
        <div className="capability-list">
          {capabilityGroups.map((item) => (
            <button
              className={open === item.title ? "capability-item open" : "capability-item"}
              type="button"
              key={item.title}
              onClick={() => setOpen(item.title)}
            >
              <IconBadge icon={item.icon} tone="soft" />
              <span>
                <strong>{item.title}</strong>
                <small>{item.summary}</small>
              </span>
            </button>
          ))}
        </div>
        <div className="capability-detail">
          {capabilityGroups
            .filter((item) => item.title === open)
            .map((item) => (
              <article key={item.title}>
                <IconBadge icon={item.icon} />
                <h2>{item.title}</h2>
                <p className="large-copy">{item.summary}</p>
                <p>{item.detail}</p>
                <div className="detail-note">
                  <strong>项目作用</strong>
                  <span>让行动方案更可追踪、可验证、可降级，不靠一次性判断赌方向。</span>
                </div>
              </article>
            ))}
        </div>
      </div>
    </div>
  );
}

function Mechanism() {
  return (
    <div className="content-page">
      <PageTitle
        label="实现方法"
        title="先行为内核，再按需调用路由器和 guard。"
        copy="它先把本轮压缩成一个可执行主线，再选择必要的证据、模型发现、能力发现、小题验证和风险边界。核心不是多填表，而是防止项目在错误层级上推进。"
      />

      <section className="timeline">
        {mechanismSteps.map((step) => (
          <article className="timeline-step" key={step.k}>
            <div className="step-index">{step.k}</div>
            <div className="step-body">
              <h3>{step.title}</h3>
              <p>{step.text}</p>
            </div>
            <code>{step.output}</code>
          </article>
        ))}
      </section>

      <section className="mechanism-grid">
        <article className="mechanism-panel">
          <h2>动态激活，而不是全量硬跑</h2>
          <p>
            `complex_behavior_kernel` 是第一层，`gate_activation_matrix` 是第二层。先确定本轮行为，再把规则分成常驻最小、风险触发、连续优化专用和恢复链专用，避免普通推进变成流程负担。
          </p>
          <div className="gate-grid">
            {gateTypes.map((gate) => (
              <div className="gate-card" key={gate.name}>
                <strong>{gate.zh}</strong>
                <span>{gate.name}</span>
                <p>{gate.examples}</p>
              </div>
            ))}
          </div>
        </article>

        <article className="mechanism-panel">
          <h2>主张就绪阶梯</h2>
          <p>
            每个结论都必须绑定证据层级。证据不足时，协议不让语言越级，从而防止把来源存在、测试通过、PR 合并或活动完成写成真实影响成立。
          </p>
          <div className="ladder">
            {["idea_or_candidate", "source_backed", "locally_verified", "small_loop_validated", "pilot_ready", "production_or_public_claim_ready"].map(
              (level, index) => (
                <div className="ladder-row" key={level}>
                  <span>{index + 1}</span>
                  <strong>{level}</strong>
                </div>
              ),
            )}
          </div>
        </article>
      </section>
    </div>
  );
}

function Scenarios() {
  const [activeId, setActiveId] = useState("software");
  const active = useMemo(() => scenarios.find((item) => item.id === activeId), [activeId]);
  const ActiveIcon = active.icon;

  return (
    <div className="content-page">
      <PageTitle
        label="适用场景"
        title="它不是单一领域模板，而是复杂项目推进的通用治理方式。"
        copy="协议默认按最终主张选择主类，再叠加高风险标签。下面每个场景都展示它会优先检查什么、输出什么、以及不能外推到哪里。"
      />

      <section className="scenario-shell">
        <div className="scenario-tabs" role="tablist" aria-label="项目场景">
          {scenarios.map((scenario) => {
            const Icon = scenario.icon;
            return (
              <button
                type="button"
                role="tab"
                aria-selected={scenario.id === activeId}
                className={scenario.id === activeId ? "scenario-tab active" : "scenario-tab"}
                key={scenario.id}
                onClick={() => setActiveId(scenario.id)}
              >
                <Icon size={20} weight="duotone" />
                <span>{scenario.label}</span>
              </button>
            );
          })}
        </div>

        <article className="scenario-detail">
          <IconBadge icon={ActiveIcon} />
          <h2>{active.label}</h2>
          <div className="scenario-block">
            <strong>要证明的核心主张</strong>
            <p>{active.claim}</p>
          </div>
          <div className="scenario-block">
            <strong>优先启用镜头</strong>
            <div className="chip-row">
              {active.lenses.map((lens) => (
                <span className="chip" key={lens}>{lens}</span>
              ))}
            </div>
          </div>
          <div className="scenario-block">
            <strong>典型输出</strong>
            <ul className="clean-list">
              {active.outputs.map((output) => (
                <li key={output}>{output}</li>
              ))}
            </ul>
          </div>
          <div className="downgrade-box">
            <WarningDiamond size={22} weight="duotone" />
            <span>{active.downgrade}</span>
          </div>
        </article>
      </section>
    </div>
  );
}

function Advantages() {
  return (
    <div className="content-page">
      <PageTitle
        label="对比优势"
        title="它比普通项目推进更稳，也比厚重流程更轻。"
        copy="持续治理协议的优势不在于字段多，而在于它把常见误判压缩成可执行行为，并用行为回归包、黄金样例和恢复链防止下一轮重新迷路。"
      />

      <section className="comparison-card">
        <div className="comparison-header">
          <span>对比维度</span>
          <span>普通推进</span>
          <span>持续治理协议</span>
        </div>
        {comparisonRows.map(([dimension, ordinary, governed]) => (
          <div className="comparison-row" key={dimension}>
            <strong>{dimension}</strong>
            <p>{ordinary}</p>
            <p>{governed}</p>
          </div>
        ))}
      </section>

      <section className="advantage-grid">
        {[
          {
            title: "比提示词更强",
            text: "它有文件、路由、验证器、经验库和恢复入口。下一次继续时不是靠记忆，而是按机器看版恢复。",
            icon: Path,
          },
          {
            title: "比项目管理清单更重证据",
            text: "它不只问任务拆分和时间线，还持续判断项目是在发现模型、填充证据、混合推进还是执行交付。",
            icon: ArrowsSplit,
          },
          {
            title: "比一次性咨询更可迭代",
            text: "真实小题和反膨胀机制让协议能继续学习，但连续两轮没有新共性缺口就停止。",
            icon: SealCheck,
          },
          {
            title: "比全量治理更低摩擦",
            text: "用户只需要说目标和材料，复杂字段由 AI 维护；可逆细节 AI 自行判断，授权、不可逆和高风险边界再回问。",
            icon: RocketLaunch,
          },
        ].map((item) => (
          <article className="advantage-card" key={item.title}>
            <IconBadge icon={item.icon} />
            <h3>{item.title}</h3>
            <p>{item.text}</p>
          </article>
        ))}
      </section>
    </div>
  );
}

function PageTitle({ label, title, copy }) {
  return (
    <section className="page-title">
      <p className="section-kicker">{label}</p>
      <h1>{title}</h1>
      <p>{copy}</p>
    </section>
  );
}

export function App() {
  const [route, go] = useHashRoute();

  const page = {
    overview: <Overview go={go} />,
    capabilities: <Capabilities />,
    mechanism: <Mechanism />,
    scenarios: <Scenarios />,
    advantages: <Advantages />,
  }[route];

  return (
    <>
      <Header route={route} go={go} />
      <main>{page}</main>
      <footer className="site-footer">
        <div>
          <strong>Complex 项目持续治理协议</strong>
          <p>当前页面用于解释协议价值与实现方法，不替代协议正文、发布包或恢复链验证。</p>
        </div>
        <button className="secondary-action compact" type="button" onClick={() => go("overview")}>
          回到概览
        </button>
      </footer>
    </>
  );
}
