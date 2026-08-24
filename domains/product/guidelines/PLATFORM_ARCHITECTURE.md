---
rule_id: platform_architecture
title: Platform Architecture v1.1（AI Problem Solving Platform 架构）
trigger:
  - 平台架构设计
  - 模块边界讨论
  - 产品开发
keywords:
  - platform
  - architecture
  - 架构
  - problem
  - solution
  - task
  - product
---

# Platform Architecture v1.1

> 定义 AI Problem Solving Platform 的架构设计。
> 不定义 AI-OS。AI-OS 是另一个在设计中的系统，详见 AGENTS.md。
>
> **骨架已冻结**: 模块边界和连接点以 [PLATFORM_USER_JOURNEY.md](PLATFORM_USER_JOURNEY.md) 为准。

**状态**: Active
**更新**: 2026-07-13

---

## 一、Mission

> **帮助用户以最低总成本解决真实问题。**

总成本 = 时间 + 金钱 + 学习成本 + 风险。

不是教用户学会解决问题。是帮用户解决问题。

---

## 二、当前现实

| 维度 | 现状 |
|------|------|
| Consultant | Prompt 循环 + DeepSeek API。是一个 AI 应用，不是 Agent |
| Builder | 规则引擎 + 数值传播。浏览器 JS。独立于 Consultant 运行 |
| Task 流转 | 手动。Consultant 输出是文本，Builder 输入是用户重新填的表单 |
| 平台 AI 的角色 | 产品功能。对话追问，输出方案。不走 Lifecycle，不写 Pattern |

**平台是一个 Prompt 驱动的 AI 应用。Consultant 是产品，不是 Agent。**

Agent（开发这个平台的 Claude）运行在 AI-OS 上。平台本身不运行在 AI-OS 上。两者独立。

---

## 三、Core Objects

### Problem
用户真正的问题。不是用户说的功能。不是"我要做小程序"——是"每天花 3 小时重复回复菜单咨询"。

AI 的职责是把用户说的症状翻译成 Problem。

### Solution
解决 Problem 的方案。可以是开发、配置、SaaS、流程改进、什么都不做。方案由 AI 推荐，用户选择。

AI 最终输出始终三个方案：
- **方案一：自己完成** — 推荐工具、教程、时间、成本、难度。目标：成本最低
- **方案二：去其他平台** — 已有成熟方案直接推荐。不因竞争隐瞒。目标：最快解决
- **方案三：让我们帮你** — Task → Solution Provider → Workspace。不是推销，是新增一个选择

### Task
平台的统一交易单元。所有需求最终变成 Task。

```
Task
  ├── type: develop | configure | consult | errand（可扩展）
  ├── input: Problem（来自 Consultant 或用户直接输入）
  ├── spec: Spec | null（仅 develop 类型触发 Builder）
  ├── provider: Solution Provider | null
  ├── price: 固定价格 | 时薪 | 待报价
  ├── status: open → assigned → in_progress → delivered → completed
  └── chat: 用户 ↔ Provider 对话记录
```

### Solution Provider
解决问题的人。不是 Developer。可以是开发者、配置专家、咨询师、学生、设计师——任何有能力解决问题的人。

```
Solution Provider
  ├── 身份: 实名 + 微信绑定
  ├── 能力标签: [{名称, 经验次数, 评分}]
  ├── 可组装: true | false（未来 Assembler 使用）
  ├── 偏好: 独立项目 | 协作项目 | 都可以
  ├── 状态: 空闲 | 忙碌
  └── 履历: 已完成 Task 列表 + 评分
```

---

## 四、三个入口

```
                    Landing
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   我有问题         我有需求        我能解决问题
   (入口 1)         (入口 2)         (入口 3)
```

| 入口 | 用户状态 | 界面 | AI 角色 |
|------|------|------|------|
| ① 我有问题 | "我不知道怎么办" | 对话 | Consultant 追问 |
| ② 我有需求 | "我知道要做什么" | Task 发布 | AI 幕后整理 |
| ③ 我能解决问题 | "我可以帮别人" | Provider 中心 | AI 匹配 Task |

入口 ② 背后仍然调用 Consultant——用户填一句话 → AI 静默分析 → 自动生成结构化 Task。

---

## 五、AI 的职责与边界

### AI 做什么

| 职责 | 说明 |
|------|------|
| 理解问题 | 把模糊症状翻译成 Problem |
| 推荐方案 | 基于最低总成本原则，推荐 Solution |
| 整理需求 | 对话结束后自动整理为结构化描述 |
| 辅助匹配 | 根据 Task 匹配最适合的 Provider（不屏蔽，只排序） |

### AI 不做什么

| 不负责 | 原因 |
|------|------|
| 替用户决定 | 用户最终选择 |
| 替 Provider 定价 | 市场定价 |
| 判断对错 | 只分析，不裁决 |

### AI 的实现方式

> 当前：AI = 模型 + Prompt + 追问逻辑。不是 Agent。
> 未来：当 AI-OS 成熟时，平台 AI 可以迁移为 AI-OS 上的 Agent，获得记忆、身份、权限等能力。

---

## 六、Consultant 行为规范（摘要）

完整规范见 `ai-consultant/CONSULTANT_CONSTITUTION.md`。核心原则：

1. **Problem First** — 先理解问题，不先讨论方案
2. **Hypothesis Driven** — 每次提问服务于一个假设
3. **Multiple Hypotheses** — 至少维护 2-3 个假设
4. **Admit Uncertainty** — 信心不足时不猜，继续问
5. **AI First but User Choice** — AI 分析，用户选择
6. **Transparent Reasoning** — 所有结论说明原因
7. **Minimize Mistakes Over Speed** — 宁愿多问，不带偏用户
8. **Lowest Total Cost** — 推荐方案以总成本最低为原则

---

## 七、Task 生命周期

```
open          用户发布 / Consultant 创建
  ↓
assigned      Provider 接单
  ↓
in_progress   开始执行
  ↓
delivered     交付物提交
  ↓
completed     用户确认完成 → 双方互评
```

状态机贯穿所有 Task 类型。

---

## 八、模块职责与状态

| 模块 | 职责 | 状态 |
|------|------|:--:|
| Landing | 三入口分流 | 未实现 |
| Consultant | Hypothesis Driven 追问 | ✅ 已实现（Prompt 循环） |
| Builder | develop 类型 Task → 生成 Spec | ✅ 已实现（规则引擎） |
| Task Network | 统一 Task 发布、匹配、状态流转 | 未实现 |
| Provider Center | Provider 注册、档案、接单 | 未实现 |
| Workspace | 协作、交付、验收 | 未实现 |

当前模块之间不连通。Consultant → Builder 的 Task 传递是手动的。

---

## 九、与 AI-OS 的关系

```text
Agent（Claude）
  │  运行在 AI-OS 上
  │  走 Lifecycle、写 Pattern、跨项目积累经验
  │
  ▼
AI-OS
  │  服务于 Agent，不服务于平台
  │  Runtime · Memory · Lifecycle · Pattern · Observation
  │
  ▼
正在开发的项目 = AI Problem Solving Platform
  │  Consultant、Builder、Marketplace...
  │  这是 Agent 当前的工作内容
  │  不是 AI-OS 的组成部分
```

**关键**：
- 平台不是运行在 AI-OS 上。Agent 运行在 AI-OS 上。Agent 当前的工作是开发平台。
- Consultant 不是 Agent。Consultant 是 Agent 正在开发的一个 AI 应用产品。
- AI-OS 的进化来自 Agent 完成工作后的 Lifecycle Review，不是来自"平台上线后收集数据"。

---

## 十、Frozen

以下内容已冻结，不得推翻，只能提出增量修改：

- Builder 是模块，不是独立产品
- Consultant = Hypothesis Engine + Constitution 八原则
- Task 是统一交易单元（四种类型，可扩展）
- Provider 不是 Developer。任何能解决问题的人都是 Provider
- AI First but User Choice
- 最低总成本原则
- 三个入口，不是一条线性流程
- Consultant 输出三方案（自己完成 / 去其他平台 / 让我们帮你），"让我们帮你"是平台的差异化路径

---

## 十一、Future（不在此版本讨论）

| 能力 | 说明 | 触发版本 |
|------|------|:--:|
| Solution Library | 标准化方案库 | V2 |
| Assembler | AI 拆解 + 自动组队 | V3 |
| AI-OS 接入 | 平台 AI 迁移为 AI-OS Agent | V3+ |
| Payment / 担保 | 平台托管付款 | V2 |
