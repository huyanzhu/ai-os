---
rule_id: platform_vision
title: AI Product Platform — Vision v1.0（唯一蓝图）
trigger:
  - 产品方向讨论
  - 五年视角规划
  - 平台蓝图
keywords:
  - platform
  - vision
  - 蓝图
  - AI Product Platform
  - product
---

# AI Product Platform — Vision v1.0

> 唯一蓝图。所有 Agent 共享。Vision 不变，Sprint 很小，实现一步验证一步。
>
> **骨架已冻结**: 用户旅程见 [PLATFORM_USER_JOURNEY.md](PLATFORM_USER_JOURNEY.md)。
> Vision 回答"为什么"。User Journey 回答"用户怎么走"。Architecture 回答"模块怎么连"。

---

## 一、5 年视角：最终形态

一个 AI 陪着用户从头走到尾。不是四个产品，是一个 AI 的四个状态。

```
用户进入平台
    │
    ▼
  AI Product Partner
    │
    ├─ Stage 1: Discovery     "我帮你发现问题"
    ├─ Stage 2: Builder        "我帮你定义需求"
    ├─ Stage 3: Marketplace    "我帮你找开发者"
    └─ Stage 4: Workspace      "我帮你管项目"

Developer Portal
    │
    ├─ 项目大厅（浏览 + 筛选）
    ├─ 开发者主页（技能 + 评分 + 作品）
    └─ 报价 / 接单 / 交付
```

### 三条完整路径

```
建议开发:   Discovery → Builder → Marketplace → Workspace
建议简化:   Discovery → 推荐方案池 → 留资 → 结束
不建议:     Discovery → 解释原因 → 欢迎回来 → 结束
```

### 基础设施（所有 Portal 共享）

```
Identity       — 微信扫码登录为主，登录后置
Memory         — 跨会话记忆（项目 / 对话 / 决策历史）
Notification   — 微信模板消息 + 站内通知
Payment        — 平台担保 + 托管付款
Project State  — 项目生命周期状态机
Review         — 双方互评
```

---

## 二、当前 Sprint：已完成

### Sprint 1: AI Product Partner — Discovery

```
Landing
  ↓
AI 对话（Hypothesis Engine）
  ↓
输出: Problem + 信心 + 建议（开发 / 简化 / 不做）
```

**已实现**:
- Hypothesis Engine 对话循环
- 假设 + 信心实时面板
- 三种建议输出
- Token 用量 + 成本追踪
- 限免体验 banner
- 登录未实现（体验后置，保存时弹）

**运行**: `node server.js` → `http://localhost:3001`
**模型**: deepseek-v4-flash

---

## 三、下一步

### Sprint 2: Builder 接入

```
Discovery "建议开发"
  ↓
自动进入 Builder
  ↓
Domain 识别 → Question Planner → Belief Propagation → Spec
  ↓
输出: Requirement Spec（decisions + pending + skipped + summary）
```

**Builder 已 Frozen**: `D:\AI\projects\requirement-builder\` 目录下，Sprint 1 闭环已验证。接入只是连线——Consultant 的 Problem 输出 → Builder 的输入。

### Sprint 3: Marketplace

```
Spec 一键发布 → 项目大厅 → 开发者浏览 → 报价 → 接单
```

### Sprint 4: Workspace + Payment

---

## 四、冻结

| 事项 | 状态 |
|------|:--:|
| AI-OS 的运行时接入 | ❌ 冻结（AI-OS 是独立系统，在设计验证中。平台当前不依赖 AI-OS 运行） |
| 平台蓝图大改 | ❌ 冻结（PLATFORM_ARCHITECTURE.md 为准） |
| Builder 功能扩展 | ❌ 冻结（直到 Sprint 2） |
| Marketplace 开发 | ❌ 冻结（直到 Sprint 3） |
| Payment / 担保系统 | ❌ 冻结（直到 Sprint 4） |
| 移动 App | ❌ 冻结 |

---

## 五、开发原则

1. **Vision 不变，Sprint 很小。** 一步一步实现，不跳。
2. **每步验证。** Discovery 有价值吗？Builder 有价值吗？用真实用户回答。
3. **基础设施提前规划，按需实现。** Identity 在"保存结果"时需要，届时再做。Memory 在"回头客"时触发，不要提前建。
4. **登录后置。** 先体验，再登录。进门弹登录 = 流失。
5. **AI 可以说"不"。** 建议简化和不建议开发不是死胡同，是完整路径。
