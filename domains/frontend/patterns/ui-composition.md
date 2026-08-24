---
rule_id: skill_fusion_ui_composition
title: UI Composition 构图生成层（friendly-precise）
trigger:
  - 给定屏幕意图(空状态/对话框/卡片/表单/导航)需要主动构图
  - UI 生成层缺'选手'
keywords:
  - ui
  - 构图
  - 间距
  - 层级
  - 微交互
  - friendly-precise
action:
  do:
    - 主动提案构图(间距节奏/层级取舍/微交互/字体编排)；品牌融合 Toss(温暖留白)+Stripe(精确刻度)=friendly-precise(单一绿强调+柔分层阴影)
---

# UI Composition（构图 · UI 能力的"生成层"）

## 是什么
UI 能力的**中间组件**——给定"这是一个空状态 / 对话框 / 卡片列表 / 表单 / 导航"等
屏幕意图，主动**提案构图**（间距节奏、层级取舍、东西放哪、微交互、字体编排）。

它补上 `frontend-design`（设计系统：给一致基元，解决"整齐"）与
`ui-beautification`（审美 rubric：批判抓 AI 味，解决"不 incoherent"）之间**缺失的一块**：
前者只会"拼方正"，后者只会"判好坏"，**两者都不会主动产出好看的构图**。本能力就是那个"选手"。

> 来源：被 `skill_research_beautification_20260716.md` 标为"非必须/按需取"的 styleseed
> `skins/`（toss/stripe/linear/raycast/arc/notion/vercel）本就是**生成式审美预设**，
> 以及 motion-dev 决策树（Entrance/Gesture/Scroll/Layout）。本能力把它们**运营化**为可复用
> 构图 pattern，而非仅供"参考"。

## 品牌适配（本项目的"皮肤"）
本项目是微信绿品牌、中文咨询市场、浅色主题静态多页。从 7 套 skin 里取最贴合的两套哲学融合：
- **Toss（韩系金融）**：温暖、圆润、留白慷慨、大触控区、柔分层阴影 → 友好好用感
- **Stripe（精密 SaaS）**：精确、克制、清晰间距刻度、单一强调色 → 专业精致感

融合方向命名为 **`friendly-precise`**：慷慨留白（Toss）+ 精确间距刻度（Stripe）+
单一绿强调（品牌）+ 柔分层阴影。其余 skin（linear 暗色/vercel 高对比/arc 花哨）作灵感，
不套用（与本品牌调性冲突）。

## 构图 Pattern（生成层核心 · 屏幕意图 → 主动提案）
每个 pattern 给**具体令牌值**，可直接落到 design-system 令牌，避免"凭感觉"。

### P1 空状态（EmptyState）— rubric States −5/个 高频失分
- 垂直居中；SVG 图标 40px、`opacity .4`、单色（`--text-muted`）
- 标题 `15/600` `--text-secondary`；提示 `13px` `max-width:320px` `--text-muted`
- 可选动作按钮，与提示 `12px` 间距
- 节奏：图标→标题→提示→按钮 各 `12px` 间隔，**不**用模态、不甩锅

### P2 对话框 / 浮层（Dialog）— Coherence 重灾区
- 遮罩 `scrim`：`rgba(0,0,0,.4)` + `backdrop-filter: blur(4px)`
- 卡片 `radius-lg 16`、内边距 `24/32`、单一强调按钮
- 入场：`scale .96→1` + `opacity 0→1` `300ms cubic-bezier(.22,1,.36,1)`；退场反向
- 多步流程用 stepper（design-system 已有）

### P3 卡片 / 列表项（Card）
- `radius 12`、表面、`1px` 边框、内边距 `16`
- hover：`translateY(-2px)` + `shadow` `200ms`（design-system `.card-hover` 已备）
- 入场：列表项 `stagger 80ms` 淡入上移 8px
- 同型区块**勿**横排重复 → 用栅格 `8px` 基

### P4 表单（Form）
- 输入 `radius-sm 8`、`1px` 边框；聚焦：`border` 强调 + `ring 3px` 强调 `@20%`
- 标签/输入 `12px` 间距；错误**内联** `12px` 错误色（非模态甩锅）
- 全站 `8px` 栅格，组间距 > 组内距

### P5 主导航 / 顶栏（Nav）
- sticky 顶；`backdrop-filter: blur(8px)`；底边 `1px` 发丝线；高 `56/64`；项间距 `8`

### P6 按钮（Button）
- `radius 12`（sm `8`）、高 `40/36`、字重 `600`、**按动作命名**
- hover：亮度/微移；active：`scale .97`（design-system `.btn` 体系已备）

### P7 动效系统（Motion）— 来自 motion-dev 决策树，生成式规则
- **Entrance**：`fade+rise 8px`、`300ms ease(.22,1,.36,1)`、`stagger .08–.16s`
- **Gesture**：hover `scale 1.02 / translateY(-2px)`、tap `.97`、弹簧 `stiffness 300–400 damping 20`
- **Scroll**：`whileInView` once + amount `.3`，仅 `transform/opacity`
- **全局**：所有动效遵守 `prefers-reduced-motion`（design-system 兜底已备）；只用 `--motion-*` 令牌

## 什么时候用（融入开发，而非仅参考）
`frontend-design` 在 **搭界面时**调用本能力：先取 design-system 基元 → **按屏幕意图套 P1–P7
主动提案构图** → 再交 `ui-beautification` 门禁审（≥80 出货）。三件套构成"完整 UI 能力链"：
```
design-system（基元/一致）  →  ui-composition（生成/构图）  →  ui-beautification（批判/门禁）
       手                           选手                              裁判
```
**关键**：本能力是"选手"，必须**在开发时主动走**，不是写完再补。缺它，UI 能力链中间是空的。

## 输出格式
- 构图提案 → `Pattern`（落 `domains/frontend/patterns`，如 P1–P7 已固化为 design-system 类）
- 一次性构图决策 → `Observation`
- 与 `ui-beautification` 配合：本能力产出"好看构图"，门禁判"是否真好看、有无 AI 味"

## 来源（运营化，非仅参考）
- `bitjaru/styleseed` skins（toss/stripe/linear/…）：取 Toss+Stripe 哲学融合为 `friendly-precise`
- `199-biotechnologies/motion-dev-animations-skill`：Entrance/Gesture/Scroll/Layout 决策树 → P7
- 适配：静态多页 → 原生 CSS animation/transition + 轻量 JS，不引 React 动效库
