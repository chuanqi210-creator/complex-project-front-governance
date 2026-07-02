import { useEffect, useMemo, useState } from "react";
import {
  ArrowsSplit,
  BracketsCurly,
  ChartLineUp,
  CheckCircle,
  ClipboardText,
  Compass,
  Database,
  FileMagnifyingGlass,
  FlowArrow,
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
    title: "强自治连续推进",
    text: "AI 默认按 7 个行为内核持续推进：恢复状态、判断项目性质、划清决策权、抓最高杠杆问题、轻量执行、按对象交付、留下 next_route。",
    icon: Target,
  },
  {
    title: "守住证据边界",
    text: "先分清模型发现、证据填充、混合推进或执行交付；每个主张都要知道证据能支撑到哪一层，不能把材料存在写成结论成立。",
    icon: ShieldCheck,
  },
  {
    title: "抗人工与上下文漂移",
    text: "问人前先证明必要性；能读的材料自己读，清楚的下一步直接走。同 session 自评只算 diagnostic，真正独立评审用事实账本和清上下文。",
    icon: PuzzlePiece,
  },
  {
    title: "可审查恢复链",
    text: "当前状态、行为回归、transcript 审查、黄金样例和完整性验证把项目推进变成可恢复、可复核、可继续的记录，而不是一次性口头承诺。",
    icon: UsersThree,
  },
];

const assets = [
  {
    name: "核心协议",
    role: "定义行为内核、双剖面项目性质、自适应判断、Loop 小闭环、评分迭代、风险边界和恢复规则。",
    file: "protocol/core.md",
  },
  {
    name: "当前状态",
    role: "记录当前恢复锚点、next_route、停止条件和活跃样例，不再维护长状态日志。",
    file: "protocol/current-state.md",
  },
  {
    name: "快速入口",
    role: "让新代理按 README、current-state、7 步行为内核和黄金样例启动。",
    file: "docs/quickstart.md",
  },
  {
    name: "完整性验证器",
    role: "检查当前核心文件、模板、样例、行为包和站点入口是否一致，不依赖旧长日志。",
    file: "tools/verify_complex_integrity.py",
  },
  {
    name: "行为回归包",
    role: "用 15 个高风险入口检查关键触发器、禁止行为和 Runtime Kit 记录是否仍被当前文档覆盖。",
    file: "docs/behavior-regression-cases.json",
  },
  {
    name: "Transcript 审查",
    role: "对真实 agent 回复做 marker-based 审查，检查必需行为、禁忌行为和人工复核问题。",
    file: "tools/review_behavior_transcript.py",
  },
  {
    name: "行为审查说明",
    role: "记录真实回复审查和端到端项目样本，衡量用户纠偏、证据边界和交付质量。",
    file: "docs/behavior-review.md",
  },
  {
    name: "5 分钟上手版",
    role: "让新代理先抓当前状态、7 步行为内核、项目性质和最小 Runtime Kit。",
    file: "docs/quickstart.md",
  },
  {
    name: "黄金样例",
    role: "展示 evidence_fill、model_discovery 和 independent_review 三类项目的最小可用运行现场。",
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
    title: "抗人工漂移",
    summary: "问人前先证明必要性，能推进就继续。",
    detail:
      "human_intervention_drift_guard、known_next_step_auto_execute_rule 和 context_pointer_first_intake 防止 AI 把低风险工作、材料整理和明确下一步甩回给用户。",
    icon: PuzzlePiece,
  },
  {
    title: "Prompt 连续性",
    summary: "每轮先把总规划、当前状态和本轮目标重水化。",
    detail:
      "complex_prompt_bootstrap_gate 先设计项目专用 prompt；round_prompt_rehydration_gate 确保后续 Plan 继承总规划，而不是只盯住眼前局部任务。",
    icon: CheckCircle,
  },
  {
    title: "能力与拓扑",
    summary: "显性判断工具、skill、API、账号、子代理和长期线程，但不机械打断。",
    detail:
      "capability_discovery_cadence_gate 以事件触发为主；无事件时 lightweight keep。外部写入、账号、付款和发布仍进入授权护栏。",
    icon: WarningDiamond,
  },
  {
    title: "独立评审",
    summary: "把同 session 诊断和真正 independent review 分开。",
    detail:
      "independent_review_context_separation 要求真正审查使用清上下文、独立 reviewer/thread 或事实账本；同 session 角色扮演只能标成 diagnostic。",
    icon: Package,
  },
  {
    title: "行为回归与黄金样例",
    summary: "用用例、真实回复审查、结果记录和填好样例验证新代理能否稳定落地。",
    detail:
      "behavior_regression_pack 覆盖 15 个高风险入口；review_behavior_transcript.py 检查真实回复；结果模板记录用户纠偏和人工评价；docs/examples 给出 evidence_fill、model_discovery 和 independent_review 的最小可恢复运行现场。",
    icon: ClipboardText,
  },
];

const mechanismSteps = [
  {
    k: "01",
    title: "恢复真实状态",
    text: "先区分 current_basis、not_current_basis、用户最新请求、旧草稿和当前依据。",
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
    text: "默认强自治+护栏：AI 处理可逆低副作用细节，目标、授权、不可逆和高风险主张回问；问人前先证明必要性。",
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
    examples: "current_basis、project_nature、decision_rights、round_goal、next_route",
  },
  {
    name: "nature based",
    zh: "性质触发",
    examples: "evidence_fill、model_discovery、mixed、execution_delivery",
  },
  {
    name: "boundary based",
    zh: "边界触发",
    examples: "账号、API、付款、发布、外部写入、不可逆动作、高风险主张",
  },
  {
    name: "review based",
    zh: "评审触发",
    examples: "fact-ledger、清上下文评审、read-only audit、transcript review",
  },
];

const scenarios = [
  {
    id: "evidence",
    label: "证据填充型",
    icon: Database,
    claim: "模型、指标或判断框架已经确定，现在要用证据把结论填实。",
    lenses: ["project_nature_router", "evidence_matrix", "claim_readiness_ladder", "delivery_contract"],
    outputs: ["证据分层", "缺口与可声明边界", "检索/获取升级路径", "人看版交付"],
    downgrade: "证据不足时只写到对应层级，不能把材料存在、引用存在或局部验证写成结论成立。",
  },
  {
    id: "discovery",
    label: "模型发现型",
    icon: Graph,
    claim: "问题定义、研究框架、解释路径或故事线还没定，不能过早证据填表。",
    lenses: ["anti_premature_convergence_gate", "ibis_argument_map_gate", "thought_search_gate", "judgment_mode: exploratory"],
    outputs: ["候选框架", "issue / position / pro / con", "可区分探针", "收敛条件"],
    downgrade: "没有比较候选框架和反例之前，不能把一个局部证据缺口升级成主目标。",
  },
  {
    id: "execution",
    label: "执行交付型",
    icon: BracketsCurly,
    claim: "主要任务是实现、包装、交付、验证或说明当前成果。",
    lenses: ["round_goal", "Loop", "deliverable_contract_gate", "next_route"],
    outputs: ["窄目标", "最小验证", "交付边界", "下一轮恢复线索"],
    downgrade: "验证未覆盖的部分不能当作已完成；人看版和机器恢复记录要分开。",
  },
  {
    id: "review",
    label: "独立评审型",
    icon: UsersThree,
    claim: "需要客观检查某个输出或流程是否真的符合标准。",
    lenses: ["independent_review_context_separation", "read_only_audit_subagent_contract", "fact-ledger", "decision_log"],
    outputs: ["事实账本", "清上下文评审说明", "问题/证据/结论分离", "整改建议"],
    downgrade: "同 session 角色扮演只能算诊断，不应包装成真正独立评审。",
  },
  {
    id: "boundary",
    label: "高风险边界",
    icon: ShieldCheck,
    claim: "目标、授权、外部写入、公开口径、高风险主张或现实责任发生变化。",
    lenses: ["decision_rights_matrix", "external_state_write_guard", "manual_action_required", "ask_user_necessity_gate"],
    outputs: ["必须回问事项", "AI 可自主事项", "人工操作边界", "回滚/降级路线"],
    downgrade: "没有授权时只能做只读分析、计划或低风险小验证，不能替用户执行外部影响动作。",
  },
];

const comparisonRows = [
  ["推进方式", "先讨论方案或直接执行", "先跑 7 步行为内核，再按项目性质推进"],
  ["项目性质", "容易把所有任务都变成证据审计", "先判断 evidence_fill / model_discovery / mixed / execution_delivery"],
  ["人工介入", "安全起见频繁问是否继续", "问人前证明必要性；清楚低风险下一步自动推进"],
  ["材料处理", "要求用户整理、搬运、摘要", "用户给路径或文件时优先自行读取和归纳"],
  ["评审独立性", "同 session 扮演评审", "区分 diagnostic 自评和清上下文 independent review"],
  ["复杂度控制", "要么过度表格化，要么完全黑箱", "行为内核给主线，模板和案例按需启用"],
  ["恢复能力", "依赖聊天记忆", "用 current-state、next_route、样例和 verifier 恢复"],
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
            `complex_behavior_kernel` 是第一层。先确定本轮行为，再把规则分成常驻最小、风险触发、连续推进和当前状态验证，避免普通推进变成流程负担。
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
        title="它比一般项目推进更稳，也比厚重流程更轻。"
        copy="持续治理协议的优势不在于字段多，而在于它把常见误判压缩成可执行行为，并用行为回归、transcript 审查、结果记录、黄金样例和恢复链防止下一轮重新迷路。"
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
            text: "它有当前状态、next_route、验证器和黄金样例。下一次继续时不是靠记忆，而是按 current-state 恢复。",
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
          <p>当前页面用于解释协议价值与实现方法，不替代核心协议、当前状态和完整性验证。</p>
        </div>
        <button className="secondary-action compact" type="button" onClick={() => go("overview")}>
          回到概览
        </button>
      </footer>
    </>
  );
}
