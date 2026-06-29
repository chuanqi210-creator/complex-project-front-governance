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
    title: "把模糊目标变成可验证主张",
    text: "先问项目真正想证明什么，再区分愿景、输出、结果和长期影响，避免从一开始就把漂亮表达当成事实。",
    icon: Target,
  },
  {
    title: "把证据、风险和边界放到执行前",
    text: "在动手前建立 current_basis、evidence_matrix、resource_boundary 和 claim readiness，先知道哪些能说、哪些只能降级说。",
    icon: ShieldCheck,
  },
  {
    title: "把能力发现显性化",
    text: "启动时和关键阶段复盘 skill、工具、插件、API、子代理和外部方法，不靠临时想起，也不机械搜工具。",
    icon: PuzzlePiece,
  },
  {
    title: "把复杂度留给系统，不丢给用户",
    text: "用户可以只用自然语言触发。完整机器字段写进治理文件，用户可见层只保留主张、风险、下一步和必要选择。",
    icon: UsersThree,
  },
];

const assets = [
  {
    name: "v3 主协议",
    role: "定义阶段控制、证据矩阵、能力发现、风险边界和恢复规则。",
    file: "protocol/复杂项目启动前置治理协议_v3_核心版.md",
  },
  {
    name: "低摩擦入口",
    role: "把厚协议压缩成用户可以自然说出的 5 行启动方式。",
    file: "protocol/复杂项目启动_低摩擦用户入口_20260622.md",
  },
  {
    name: "路由表与经验库",
    role: "用大类路由和失败模式校准新项目，不再复制具体领域长模板。",
    file: "protocol/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md",
  },
  {
    name: "发布包与验证器",
    role: "把当前能力、恢复入口、变更清单和本地 verifier 绑定起来。",
    file: "protocol/前置治理协议发布包_20260622.md",
  },
];

const capabilityGroups = [
  {
    title: "材料与依据治理",
    summary: "先判定哪些材料是 current basis，哪些只是背景、草稿、历史或候选。",
    detail:
      "协议会登记 source、type、authority、supports_stage 和 current_basis reason。这样旧稿、生成内容和历史记录不会被误当成当前事实。",
    icon: FileMagnifyingGlass,
  },
  {
    title: "主张与证据地图",
    summary: "把项目目标拆成可以被证据支撑或降级的主张链。",
    detail:
      "通过 evidence_matrix、source_role_map 和 claim_readiness_ladder，区分来源能证明什么、不能证明什么，以及结论能到 idea、source-backed、local、small-loop、pilot 还是 public claim。",
    icon: Graph,
  },
  {
    title: "新领域治理构造",
    summary: "面对陌生项目，不先找旧模板，而是临时生成本轮治理镜头。",
    detail:
      "new_domain_governance_builder 至少生成 claim_ladder、evidence_contract、stakeholder_context、execution_validation、risk_ethics_permission、operation_handoff、transfer_boundary 和 deliverable_storyline。",
    icon: Compass,
  },
  {
    title: "能力发现与编排",
    summary: "显性复盘 skill、工具、插件、connector、API、外部方法和子代理。",
    detail:
      "capability_discovery_cadence_gate 规定何时重新考虑能力；skill_plugin_discovery_gate 和 side-effect gate 记录选用、拒绝、权限、副作用和授权边界。",
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
    title: "恢复链与机器看版",
    summary: "每轮留下 next_route、状态、验证结果和恢复入口。",
    detail:
      "append_eof_section_tool、latest_board_tail_check 和 verify_governance_recovery_tool 让后续代理能从最新机器看版恢复，而不是凭聊天记忆继续。",
    icon: ClipboardText,
  },
];

const mechanismSteps = [
  {
    k: "01",
    title: "低摩擦触发",
    text: "用户只描述目标、材料和期待结果；AI 自动识别是否为重大项目、连续任务或新领域。",
    output: "compressed_user_entry",
  },
  {
    k: "02",
    title: "动态阶段控制",
    text: "先判断 light、standard、deep 或 continuous 深度，再决定推进、压缩、加深、并行、回退或询问。",
    output: "dynamic_stage_controller",
  },
  {
    k: "03",
    title: "能力盘点",
    text: "在执行前扫描本地 skill、工具、插件、API、外部方法和子代理边界，写明选用与拒绝。",
    output: "capability_discovery_cadence_gate",
  },
  {
    k: "04",
    title: "构造证据镜头",
    text: "围绕最终主张生成临时领域 trace，从经验库抽取相近失败模式，只拿方法，不复制旧模板。",
    output: "new_domain_governance_builder",
  },
  {
    k: "05",
    title: "选择必要 guard",
    text: "通过 gate_activation_matrix 区分常驻、风险触发、连续优化和恢复专用检查，控制摩擦。",
    output: "gate_activation_matrix",
  },
  {
    k: "06",
    title: "跑小题验证",
    text: "用一个小闭环验证最危险的主张或边界，把观察结果写成降级规则。",
    output: "micro_task_execution_check",
  },
  {
    k: "07",
    title: "收束与恢复",
    text: "输出启动方案、证据矩阵、风险边界、下一步路由、发布包状态和机器看版。",
    output: "handoff + verifier",
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
    outputs: ["issue/PR/CI/release 状态表", "部署与真实使用缺口", "rollback/monitoring 边界", "交付启动清单"],
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
  ["启动方式", "先讨论方案或直接执行", "先建立主张、证据、资源边界和阶段路由"],
  ["项目范围", "容易被当前材料或熟悉领域收窄", "用新领域构造器覆盖真实项目与跨域场景"],
  ["工具使用", "临时想起、临时调用、难复盘", "启动与阶段切换时显性复盘能力候选和拒绝理由"],
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
          <strong>项目启动前置治理</strong>
          <small>Complex Project Front Governance</small>
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
        <img className="hero-image" src={blueprintImage} alt="项目启动蓝图视觉图，展示证据地图、风险边界和六步治理流程" />
        <div className="hero-overlay">
          <p className="eyebrow">适用于复杂项目启动前</p>
          <h1>把复杂项目，从模糊想法变成可执行启动方案</h1>
          <p className="hero-copy">
            这套前置治理协议不是一份普通项目清单，而是一套启动前的判断系统：它先看清目标、证据、能力、风险和停止条件，再让项目进入执行。
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
          <h2>复杂项目最大的风险，往往发生在“开始之前”。</h2>
          <p>
            项目初期最容易把目标说大、把证据看轻、把工具当能力、把一次输出当真实成效。前置治理协议把这些隐性风险提前显性化，并把下一步压缩成一个能执行、能验证、能恢复的启动方案。
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
          <h2>不是更多流程，而是更清楚的启动条件。</h2>
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
        title="它把项目启动前的关键治理工作，拆成可执行能力。"
        copy="这些能力不是每次全量展开。协议会按项目风险、阶段深度和用户摩擦动态激活，确保重项目不失控，小项目不过度治理。"
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
                  <span>让启动方案更可追踪、可验证、可降级，不靠一次性判断赌方向。</span>
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
        title="协议内部是一组低摩擦 gate、路由器和恢复链。"
        copy="它先决定本轮需要多深，再选择必要的证据镜头、能力发现、小题验证和风险边界。核心不是多填表，而是防止项目在错误层级上启动。"
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
            `gate_activation_matrix` 把规则分成四类：常驻最小、风险触发、连续优化专用、恢复链专用。这样协议既能覆盖复杂项目，又不会让普通启动变成流程负担。
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
        title="它不是单一领域模板，而是新项目启动的通用治理方式。"
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
        title="它比普通项目启动更稳，也比厚重流程更轻。"
        copy="前置治理协议的优势不在于字段多，而在于它把常见误判前移，把风险语言降级，把能力发现和恢复链变成可复用机制。"
      />

      <section className="comparison-card">
        <div className="comparison-header">
          <span>对比维度</span>
          <span>普通启动</span>
          <span>前置治理协议</span>
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
            title: "比项目管理清单更前置",
            text: "它不只问任务拆分和时间线，还先判断哪些主张能成立、证据缺什么、风险能不能越级。",
            icon: ArrowsSplit,
          },
          {
            title: "比一次性咨询更可迭代",
            text: "真实小题和反膨胀机制让协议能继续学习，但连续两轮没有新共性缺口就停止。",
            icon: SealCheck,
          },
          {
            title: "比全量治理更低摩擦",
            text: "用户只需要说目标和材料，复杂字段由 AI 维护；只有会降低返工时才问高杠杆问题。",
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
          <strong>复杂项目启动前置治理协议</strong>
          <p>当前页面用于解释协议价值与实现方法，不替代协议正文、发布包或恢复链验证。</p>
        </div>
        <button className="secondary-action compact" type="button" onClick={() => go("overview")}>
          回到概览
        </button>
      </footer>
    </>
  );
}
