---
rule_id: ai_os_evolution_loop
title: AI-OS Evolution Loop v2.1（Capability → Lifecycle → Runtime 三层架构）
trigger:
  - 设计 AI-OS 演化机制
  - Capability 审计
  - Bootstrap 装配策略
  - Lifecycle 事件设计
keywords:
  - ai-os
  - evolution
  - lifecycle
  - capability
  - runtime
  - bootstrap
  - assemble
---

# AI-OS Evolution Loop v2.1

> 📌 GOVERNANCE
> - Status: Drift
> - Superseded By: —
> - SSOT: 本文件（活跃副本）
> - Owner: —
> - Note: 与 archive/docs-root/ 双副本，字节重复+章节编号损坏；活跃副本为 SSOT

> 基于 Capability Inventory 审计（81 个 Capability，64% Agent 未知）更新。
> 核心修正：Agent 不应该成为事件派发器。Assemble > Inject。

**状态**: 当前理解（待下一轮 Sprint 验证）
**日期**: 2026-07-13

---

## 一、Evolution Loop

```
Development
  │
  ▼
Experience        ← 原始材料。本次开发中发生了什么。
  │
  ▼
Classification    ← 这是什么类型的经验？
  │                   │
  │   ┌───────────────┼───────────────┐
  │   ▼               ▼               ▼
  │ Pattern        Guideline       Decision
  │ (工程经验)     (产品/UX原则)   (架构决策)
  │                   │               │
  │   └───────────────┼───────────────┘
  │                   ▼
  ▼               Knowledge
Review            ← 三问 + 第四问 + 第五问
  │
  ▼
Proposal          ← AI-OS 改进方案
  │
  ▼
Git               ← 验证过的进入下一轮，不对的回滚
```

**关键变化**：Experience 不直接通向 Pattern。Classification 是中间层——不是所有经验都适合变成 Pattern。有些是 Guideline（产品原则），有些是 Decision（架构决策），有些只是 Observation（一次性记录）。

---

## 二、三层架构

AI-OS 由三个独立层组成：

```
Capability Layer    "有什么能力"
    │
    │   Capability Registry（独立注册表，不是 Bootstrap 的配置）
    │   Pattern、Task Card、Review、Memory、Telemetry、Knowledge……
    │   81 个 Capability 已定义，9 个 Ready 但从未被使用
    │
    ▼
Lifecycle Layer     "什么时候用"
    │
    │   TaskCreated → TaskStarted → TaskCompleted → TaskClosed
    │   Lifecycle 是 AI-OS 唯一稳定的轴。
    │   Agent 会换，模型会换，Runtime 会换。只有 Lifecycle 不会换。
    │
    ▼
Runtime Layer       "谁装配"
    │
    │   Runtime 在正确的生命周期节点，装配正确的 Capability。
    │   Agent 不知道 Capability 的存在。Agent 不知道装配发生过。
    │   Agent 只在准备好的台面上工作。
```

### 三层之间的关系

```
Capability Registry
        │
    ┌───┼───┐
    │   │   │
    ▼   ▼   ▼
Bootstrap  Review  Archive    ← 都是 Registry 的消费者
    │
    ▼
Lifecycle 事件
    │
    ▼
Runtime 装配 Capability → Agent 收到准备好的上下文
```

Capability Registry 不属于 Bootstrap。Bootstrap 是它的消费者之一。Review 也是。Archive 也是。以后任何模块都可以消费它。

---

## 三、Bootstrap Assembly Strategy

Bootstrap 不再是"搜索 Pattern"。Bootstrap 是**Context Builder**——根据任务类型，从多个 Registry 中装配正确的 Context。

```
Task Type → Bootstrap → Capability Registry → Assemble → Agent
                         Experience Registry
                         Decision Registry
                         Guideline Registry
```

### 按任务类型的装配策略

| 任务类型 | 装配内容 |
|---------|---------|
| new_feature | Experience + Pattern + Guideline + Task Card |
| bug_fix | Failure Pattern + Previous Bugs |
| refactor | Architecture + Decision + Pattern |
| research | Architecture + Decision + ADR |
| design | UX Guideline + Product Decision + Previous Experience |

**验证目标**：Bootstrap 本轮装配的内容，哪些真正帮助了开发？哪些没有价值？

---

## 四、当前阶段：Capability Optimization

Capability 审计已完成（81 个，64% Agent 未知）。
Lifecycle 模型已稳定（连续两轮 4/4 事件执行）。

当前阶段的目标不是"增加 Capability"，而是**优化 Bootstrap 的装配策略**——根据任务类型，把正确的 Capability 装配给 Agent，并记录哪些装配真正产生了价值。

---

## 三、核心原则

1. **AI-OS 不应围绕 Agent 设计，而应围绕 Lifecycle 设计。** Agent 只是 Lifecycle 的一个参与者，不是所有者。

2. **Agent 不应该成为事件派发器。** 这不是"Agent 做得不好"，是"这件事不属于 Agent 的职责"。Agent 的职责是推理和决策，不是记住 AI-OS 的生命周期。派发事件是 Runtime 的职责。

3. **Assemble，不是 Inject。** Inject 的隐喻是"往 Agent 脑子里塞东西"——Agent 还是主体。Assemble 的隐喻是"根据当前任务，把需要的零件装配成完整的工具台"——Runtime 是主体，Agent 是工具台的使用者。

4. **Capability 不应该由 Agent 发现，而应该由 Runtime 在正确的生命周期节点主动装配。** 审计数据：81 个 Capability，Agent 只知道 4 个。不是 Agent 不努力——Agent 本来就不应该知道。

5. **Knowledge 是中间层。** 不是所有 Experience 都值得变成 Proposal，不是所有 Knowledge 都适合变成 Pattern。

6. **验证 Lifecycle Model，不是验证 Agent。** 如果 Lifecycle 定义错了，Runtime 自动执行这个错误定义，比手动执行更危险。验证目标是"事件定义是否正确、Hook 挂载是否正确"，不是"Agent 记得执行的比例"。

---

## 四、Capability Inventory 审计结论

**审计日期**: 2026-07-13
**审计范围**: 81 个 Capability

| 指标 | 数据 |
|------|:----:|
| Capability 总数 | 81 |
| Agent 完全不知道 | 52 (64%) |
| Agent 知道但不使用 | 25 (31%) |
| Agent 真正使用 | 4 (5%) |
| Ready 但从未激活 | 9 (11%) |

**核心发现**：Agent 使用的 4 个 Capability 恰好是 ONBOARD 流程中明确要求读取的文件。其余 77 个对 Agent 来说不存在。Capability 的位置决定了使用率——在 ONBOARD 流程中的 → Agent 会用；在 docs/standards/ 下的 → Agent 不会碰。

**结论**：文档定义 ≠ 运行时行为。AIS-001~006、TAG-001、Skill-000~005 全部定义完整，但没有任何运行时机制确保它们被执行。

---

## 五、验证路径

### 当前阶段：手动验证 Lifecycle Model

验证目标：
- Lifecycle 四个事件是否完整、是否有遗漏
- Hook 挂载是否正确
- Capability 装配顺序是否合理

验证指标：**Lifecycle Model Reliability**（不是 Agent Reliability）

### 验证通过后：Runtime 接管

```
Lifecycle 事件
    │
    ▼
Runtime 查询 Capability Registry
    │
    ▼
装配当前任务需要的 Capability
    │
    ▼
Agent 在准备好的台面上工作
```

Agent 不知道 Capability 存在。Agent 不知道装配发生过。Agent 只知道"这个台面上有我需要的一切"。

---

## 六、与之前版本的关键变化

| v2.0 | v2.1 | 原因 |
|------|------|------|
| Hook Layer 作为中间层 | Capability → Lifecycle → Runtime 三层 | 审计发现 Capability 是独立实体，不是 Hook 的附属 |
| Pattern Hook 是独立 Hook | Pattern 是 Capability，不是 Hook | Bootstrap 是 Capability 的装配者，Pattern 是被装配的零件 |
| Agent 作为事件检测器 | Agent 不应该成为事件派发器 | 审计数据：77/81 未知。不是"忘了"，是"不该由 Agent 做" |
| Inject（注入） | Assemble（装配） | Runtime 是主体，Agent 是使用者 |
| 验证 Agent 可靠性 | 验证 Lifecycle Model 可靠性 | 指标错了——如果 Lifecycle 定义错误，Agent 100% 可靠也没用 |
