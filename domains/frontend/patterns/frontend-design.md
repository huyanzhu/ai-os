---
rule_id: skill_fusion_frontend_design
title: Frontend Design 前端统一装配点
trigger:
  - 开始前端/UI 任务
  - 需要设计规范/工程模式
keywords:
  - frontend
  - ui
  - 设计
  - 令牌
  - utility-first
  - 组件
action:
  do:
    - 设计令牌统一/Utility-First CSS/组件即源码(仅React)/前端工程实践；静态多页用共享 CSS 变量替代 Tailwind/shadcn
---

# Frontend Design

## 是什么
前端 / UI 开发时的设计与工程能力。在开始前端任务时，把「设计规范 + 工程模式」推到 Agent 面前，避免每次从零手写、跨页面不一致。

**冲突处理结论（2026-07-16）**：前端知识此前仅以 2 条 domain pattern 存在（`domains/frontend/patterns/`），薄且无 Capability 装配入口。本能力走「上位/补充」：收编已有 pattern + 外部标杆，成为前端任务的统一装配点。

## 什么时候用
TaskStarted 事件（domain = frontend / design）→ Frontend Hook 装配本能力。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 在开始前端/UI 任务时手动触发。）

## 能力构成
1. **设计规范** — 设计令牌（颜色/间距/圆角/字体/阴影）统一；组件一致性；响应式；可访问性。参考 vercel-labs `web-design-guidelines`（100+ UI 审计规则）、anthropics `frontend-design`。
2. **Utility-First CSS** — 见 `domains/frontend/patterns/tailwind_thinking.md`（Skill-009）。样式用 utility classes 表达，靠设计令牌保证一致。
3. **组件即源码** — 见 `domains/frontend/patterns/shadcn_ui_thinking.md`（Skill-010）。Radix + Tailwind，组件复制进项目可改。**仅 React 项目适用**。
4. **前端工程实践** — 状态/数据流、性能、结构组织。参考 addyosmani `frontend-ui-engineering`、wshobson `tailwind-design-system`。
5. **生成层（构图 · "选手"）** — 见 `capabilities/ui-composition.md`。给定屏幕意图（空状态/对话框/卡片/表单/导航），**主动提案构图**（间距节奏、层级、微交互、动效），把 styleseed `skins` 运营化为 P1–P7 pattern、motion-dev 决策树运营化为 P7 动效系统。这是补全"设计系统（基元）+ 门禁（裁判）"之间缺失的**生成中间层**——否则 UI 能力链是空的。

## 适配当前项目（重要）
ai-consultant 是**静态多页 HTML、无构建链**：
- ✅ 直接可用：设计令牌 / Utility-First 思维 / 设计规范审查
- ⚠️ 有条件：Tailwind 需 CDN 或构建；shadcn(React) 不适用于纯静态多页 → 用「共享 CSS 变量文件」替代（与现有 `index.html` 的 `:root` 一脉相承）

## 全链工作流（设计系统 → 生成构图 → 审美门禁）
UI 能力三段合一，缺一不可：
1. **基元**（`frontend-design` / design-system.css）：令牌 + 组件 + Anti-AI-taste 防御契约，保证"建不出错"。
2. **生成（选手）**（`ui-composition`）：搭界面时按屏幕意图主动套 P1–P7 构图 pattern，产出"好看"的初稿——不是写完再补，是**开发时主动走**。
3. **审核（裁判）**（`ui-beautification` 门禁）：收口跑 7 类 rubric，≥80 才出货。

## 收口门禁（C-UI-Beautification Quality Gate）
UI 不是"写完就出货"。`frontend-design` 在 **`TaskCompleted@frontend`** 收口时，调用
`C-UI-Beautification` 跑 7 类 rubric（Coherence/Color/Hierarchy/Layout/States/UX-writing/Motion，
满分 100），**≥80（B）才标记完成并出货**；低于 80 返回 Fix-first 清单、不标记完成。
- rubric 明细与权重见 `capabilities/ui-beautification.md`。
- "AI 味"防御（单半径刻度 / 单品牌绿 / SVG 图标非 emoji / 语义令牌 / motion+reduced-motion）
  已固化进 `design-system.css` 的「Anti-AI-taste defense contract」，让大部分违规**构造上不可能**。
- 当前 Lifecycle Hook 运行时未落地，门禁由 Agent 在收口时手动模拟执行。

## 输出格式
设计系统文件 / 组件规范 / UI 审查报告；可复用的 UI 范式 → Pattern（补进 domains/frontend/patterns）；一次性发现 → Observation。

## 参考来源（外部 Skill 融合，已核实 star）
- vercel-labs/agent-skills (29.1k)：web-design-guidelines
- wshobson/agents (37.9k)：tailwind-design-system
- addyosmani/agent-skills (78.5k)：frontend-ui-engineering
- anthropics/skills (161.4k)：frontend-design
- 已有 domain pattern：tailwind_thinking(Skill-009)、shadcn_ui_thinking(Skill-010)

## 融合映射（来自 proposal 2026-07-16，2026-07-16 归位裁定）
- 能力定义 → 本 Capability（收编已有 pattern + 外部标杆）+ `ui-composition`（生成层"选手"）+ `C-UI-Beautification`（收口门禁"裁判"）
- 三段链 → 基元(frontend-design/design-system) → 生成(ui-composition/P1–P7) → 审核(ui-beautification/≥80 Gate)
- 触发条件 → Lifecycle Hook: TaskStarted (frontend/design) 装配；TaskCompleted@frontend 触发门禁
- 输出格式 → Observation / Pattern；门禁报告（Fix-first）回流；构图 pattern 沉淀进 design-system / domains/frontend/patterns
