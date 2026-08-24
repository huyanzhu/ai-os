---
rule_id: skill_fusion_ui_beautification
title: UI Beautification 审美门禁（≥80 才出货）
trigger:
  - UI 收尾需要评审审美
  - 生成 UI 后检测 AI 味
keywords:
  - ui
  - 美化
  - 审美
  - rubric
  - ai味
  - 门禁
action:
  do:
    - 7 大类 0-100 评审(圆角混用/多强调色/纯黑文字/无层级/缺状态/机器人文案)，按提分幅度排序修复，≥80 才给用户看
---

# UI Beautification（美化 · frontend-design 的 Quality Gate 子程序）

## 是什么
UI 开发收尾阶段的**审美判断力 + 动效**能力。在「设计系统」（令牌/组件/一致性，解决"整齐"）
之上，补上"好看、不 AI 味、有动效"这一层。

**归位结论（2026-07-16）**：此前只有 `frontend-design`（设计系统结构层），「美化」被裁定为
独立维度并新建 Capability。经 index.html 样板验证有效（63→88，预测偏差 1 分）后，用户裁定
**降级为 `frontend-design` 的 Quality Gate 子程序**——保留独立审计语义，但不再单独跑，
由 frontend-design 收口时调用，作为「≥80 才出货」的门禁。

## 什么时候用
由 `frontend-design` 在 **`TaskCompleted@frontend` 收口**时调用，作为 ≥80 才出货的门禁
（详见 frontend-design 的「收口门禁」节）。保留手动应急触发入口（Agent 在 UI 收尾时手动跑）。
（当前 Lifecycle Hook 运行时未落地，门禁由 Agent 在收口时手动模拟执行。）

## 能力构成（来源已 GitHub API 核实）

### 1. 设计评审 rubric（来自 `bitjaru/styleseed` 764⭐，MIT）
核心哲学：**UI 显"AI 味"不是因为组件丑，而是"各部分互不认同"**（圆角混用、三个强调色、
纯黑文字、无层级、缺状态、机器人文案）。按 7 大类打 0–100 分，给出**按"提分幅度"排序**的修复清单；
作为 Quality Gate：**生成 UI 后先评审→修→复评，分数过 ~80 才给用户看**，不交一稿 incoherent UI。

| 大类 | 权重 | 典型扣分项（"AI 味"信号） |
|------|------|--------------------------|
| Coherence 一致性 | 20 | 混用圆角(尖卡+圆钮 −6)、≥2 强调色(−5)、**emoji 当图标**注入杂色(−6)、混用阴影/图标族(−3)、控件高度不一(−3) |
| Color discipline 色彩纪律 | 16 | **纯黑 `#000` 文字**(用 ~`#2A2A2A` −4)、硬编码 hex 不用语义令牌(−2)、OK 状态用状态色而非中性灰(−4)、**每行都上状态色**(无严重度层级 −4)、装饰色(金星/彩虹点 −3)、仅靠颜色无图标/文字(−4)、对比低于 WCAG AA(−6) |
| Hierarchy & type 层级排版 | 16 | 数字与单位非 ~2:1(−4)、全同字号无主次(−5)、任意字号无刻度(−4)、行高错(展示松/正文挤 −3) |
| Layout & spacing 布局间距 | 12 | 内容裸放页面无卡片(−6)、非 8px 栅格(7/13/19px −3)、组间距不大于组内距(−3)、同类型区块横排重复(−4) |
| States 状态 | 12 | 数据面缺 空/加载/错误 态(−5/个)、空态无下一步、错误甩锅不帮忙(−4) |
| UX writing 文案 | 12 | 按钮不命名动作("Submit"→"Send $2,400" −4)、错误甩锅系统腔(−4)、一词两义/废话("please/successfully" −2) |
| Motion & polish 动效打磨 | 12 | 临时淡入非统一命名感(−3)、动效延迟/阻塞内容(−4)、自定义动效无 `prefers-reduced-motion`(−3)、单层硬黑阴影非分层低透明着色(−2) |

评级：90+ A · 80–89 B · 70–79 C · 60–69 D · <60 F。每类下限 0，求和。

### 2. 动效原则（来自 `199-biotechnologies/motion-dev-animations-skill` 64⭐）
六原则：**Purposeful(服务功能) · Smooth(120fps) · Accessible(reduced-motion) · Performant(GPU-only transform/opacity) · Elegant(克制) · Consistent(统一 timing)**。
决策树：Entrance(入场, 0.6–0.8s, ease [0.22,1,0.36,1], stagger 0.1–0.2s) / Gesture(hover scale 1.05, tap 0.95, 弹簧 stiffness 300–400 damping 20) / Scroll(whileInView, viewport once+amount 0.3, 仅 transform/opacity) / Layout(FLIP)。

**适配当前静态多页项目（重要）**：motion-dev 原版面向 React/Next/Svelte/Astro（Motion.dev/Framer Motion），
**明确不支持静态无 JS 框架站点**。故本项目动效走：**原生 CSS animation/transition + 轻量 JS**，
遵守同一套原则（GPU-only、统一 timing、`prefers-reduced-motion` 兜底）。不引入 React 动效库。

### 3. 品牌皮肤（来自 styleseed `skins/`：toss / stripe / linear / raycast / arc / notion / vercel）
"灵感式"令牌集（颜色/圆角/阴影/动效值），用 `data-skin` 一类属性切换。可作为设计系统的
"审美预设"参考，给不同产品调性用（如金融用 stripe 风、工具用 linear 风）。非必须，按需取。

## 输出格式
美化审查报告（模板见 `templates/ui-beautification.md`）：
- `## Design Score: NN/100 (文件) 评级` + 7 大类分项扣分（带行号证据）
- `### Fix first` 按**提分幅度**排序的修复清单（非按严重度）
- 复评目标 ~80+ 才出货（即 frontend-design 的出货门禁）。**本子程序只评不改**，修复单交回 frontend-design 应用，或经用户/Agent 确认后执行。

## 参考来源（外部 Skill 融合，已核实 star + SKILL.md 存在）
- bitjaru/styleseed（764⭐，MIT）：`skills/styleseed-design-review`（74 规则 / 19 skills / 7 skins）
- 199-biotechnologies/motion-dev-animations-skill（64⭐）：Motion.dev 动效原则（静态站适配见上）
- 辅助（概念参考，星低未深验）：80x24/aesthetic-profile（AESTHETICS.md 固化品味）、
  thedavidmurray/claude-make-interfaces-feel-better（打磨 UI 原则）、
  nchemb/neej-frontend-craft（生产级独特前端+自评估）

## 融合映射（归位后，2026-07-16 裁定）
- 能力定义 → 现为 `frontend-design` 的 **Quality Gate 子程序**（审美判断力 rubric + 动效原则）
- 触发条件 → 由 `frontend-design` 收口时调用（`TaskCompleted@frontend` 门禁），保留手动应急入口
- 输出格式 → 门禁报告（Fix-first 清单）回流 frontend-design；审美规则沉淀 Observation / Pattern

## 适配当前项目注意
- ai-consultant 是静态多页 HTML、无构建链：动效走 CSS+轻量 JS，不引 React 库。
- 设计系统(`design-system.css`)已提供令牌/组件底子；本能力在其之上做"审美评分 + 反 AI 味 + 动效"。
- 验证方式（不写死）：下轮真实 UI 开发（如这 7 页的收尾美化）手动验证：评审 rubric 是否真帮 Agent 识别出 AI 味、分数是否真提升。
