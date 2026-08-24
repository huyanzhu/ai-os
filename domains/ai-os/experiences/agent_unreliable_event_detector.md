---
rule_id: agent_unreliable_event_detector
title: Agent 作为事件检测器不可靠（Knowledge）
trigger:
  - 生命周期事件没有被 Agent 主动执行
  - Agent 忘记创建 Task Card
  - 设计事件派发与 Runtime 接管方案
keywords:
  - agent
  - 事件检测
  - lifecycle
  - runtime
  - 不可靠
  - observation
---

# Knowledge: Agent 作为事件检测器不可靠

**来源**: Sprint 4-5 + Sprint 5 Review
**日期**: 2026-07-13
**类型**: 系统观察

---

## 内容

Agent 不会主动记住 AI-OS 的生命周期事件。在两轮 Sprint 中：

- Task Card 从未被 Agent 主动创建
- Pattern 从未被 Agent 主动搜索
- Review 只在流程要求时才执行

Agent 执行这些动作不是因为"知道该做"，而是因为外部提示（ONBOARD、Sprint Workflow、手动验证 Hook）。

**根因**：AI-OS 没有生命周期入口。所有机制依赖 Agent 自己记得。Agent 不是可靠的事件检测器。

**方向**：短期手动执行 Hook，记录数据。长期 Runtime 接管事件派发。当前阶段的"Agent 忘记"不是失败，它是 Runtime 接管的最佳证据。

**相关**: [[agent_pattern_injection_failure]] [[bootstrap_as_unified_entry]]
