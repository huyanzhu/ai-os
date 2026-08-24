---
rule_id: skill_fusion_testing_tdd
title: Testing TDD（RED-GREEN-REFACTOR）
trigger:
  - 实现新逻辑/修 bug 前
  - 任何可能破坏现有行为的改动
keywords:
  - tdd
  - 测试
  - red-green-refactor
  - prove-it
  - 回归
action:
  do:
    - RED(写失败测试)→GREEN(最小实现通过)→REFACTOR(保持绿清理)；修 bug 用 Prove-It 先测复现；纯配置/文档/静态内容不用
---

# Testing TDD

## 是什么
以测试驱动开发的工程纪律能力。在 TaskStarted 时建立「先写失败测试、再写实现」的节奏，让每次改动都有可证明的正确性。

参考外部标杆：addyosmani/agent-skills 的 `test-driven-development` skill + `commands/test.toml`（RED-GREEN-REFACTOR、Prove-It 模式）；mattpocock/skills 的 `/tdd`。

## 什么时候用
TaskStarted 事件 → Testing Hook 在规划/实现前提示采用 TDD；提交前验证测试全绿。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 在动手写实现前手动模拟触发。）

## 核心循环
RED（写失败测试）→ GREEN（最小实现令其通过）→ REFACTOR（保持绿的前提下清理）→ 重复。

## 适用边界
- **用**：实现新逻辑/行为、修 bug（Prove-It：先用测试复现 bug）、改已有功能、加边界处理、任何可能破坏现有行为的改动。
- **不用**：纯配置变更、文档更新、无行为影响的静态内容变更。

## 输出格式
测试结果（pass/fail）+ 回归信号；重复出现的测试模式/陷阱 → Pattern；一次性发现 → Observation（经 knowledge-capture）。

## 参考来源（外部 Skill 融合）
- addyosmani/agent-skills (78.5k)：`test-driven-development` skill + `commands/test.toml`
- mattpocock/skills (171.8k)：`/tdd`、`/diagnose`

## 融合映射（来自 proposal 2026-07-16）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskStarted
- 输出格式 → Observation / Pattern

## 可装配工作模式（Assembled · 2026-08-24 D-043 接入）

> 外部 Skill 完整工作模式（obra/superpowers `test-driven-development` · 2026-08-24 接入）已
> 物化为可激活单位：`capabilities/test-driven-development.md`（Assembled / Conditional，
> 完整流程 = Iron Law → RED → Verify RED → GREEN → Verify GREEN → REFACTOR → 合理化拦截 →
> Red Flags → 检查清单）。本 pattern 保留为知识侧 Reference（核心循环 / 适用边界 / 融合映射）；
> 真实实现任务命中 trigger 时装载单位执行完整流程，知识检索仍命中本 pattern——两通道并存，
> 互补不重复。接入裁决见 evolution/decisions.md D-043。
