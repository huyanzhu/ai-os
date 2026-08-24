---
rule_id: lifecycle_boundaries
title: Codex CLI Tool Lifecycle 边界规则 — 串行、Kill-Safe、错误隔离
trigger:
  - 怀疑 lifecycle 异常
  - 收到 invalid_request_error
  - 收到 tool_timeout
  - session 被强制终止
  - UI 输出截断
  - 怀疑 tool_call_id 链断裂
condition: 使用 deepseek-v4-flash + Codex CLI (Windows, PowerShell)
action:
  do:
    - L-001（串行 Lifecycle）: 跨多轮 reasoning 安全，不应预期交错状态
    - L-002（Kill-Safe）: session 终止后启动干净，不需要 recovery 或清理
    - L-003（Provider Error 隔离）: invalid_request_error 不影响 brain
    - L-004（Timeout）: 重试 1 次后报告，不应触发 brain recovery
    - L-005（UI 截断）: 独立展示层问题，不作为 runtime 故障信号
    - L-006（tool_call_id）: 链断裂属于框架错误，非 brain corruption
  dont:
    - 将 provider error 视为 brain 受损
    - 将 UI 截断作为 runtime 故障信号
    - 在 timeout 后触发 brain recovery
    - 预期交错 tool 状态
    - 在 session kill 后执行 recovery 逻辑
keywords:
  - lifecycle
  - boundary
  - governance
  - phase

knowledge_position: Standalone
knowledge_cluster: 
epistemology_tag: OBSERVATION
confidence: MEDIUM
---

# lifecycle_boundaries.md
# 层级: L3 Learned Rules
# 来源: Runtime Boundary Mapping (2026-05-29)
# 实验环境: deepseek-v4-flash + Codex CLI (Windows, PowerShell)
# Epistemology: 每条规则标注 OBSERVATION / INFERENCE（详见 EPISTEMOLOGY.md）

## L-001: 串行 Lifecycle

分类：OBSERVATION

实验观察到 Codex CLI 每轮执行一个 tool call，无重叠、无 batch、无并发 stream。
A→B 连续调用 clean exit。

→ 跨多轮 reasoning 安全
→ 不应预期交错状态

注意：此行为基于当前 CLI 架构观察。未来版本可能变更。

---

## L-002: Kill-Safe

分类：OBSERVATION

实验验证：session A 中途终止后，session B 启动干净。
未观察到 lifecycle 残留。

→ 启动时不需要 recovery 逻辑
→ 不需要 tool lifecycle 状态清理

注意：验证规模为 single session kill + single session restart。

---

## L-003: Provider Error 隔离

分类：FACT（架构设计）

Provider 错误（如 invalid_request_error）不影响 brain state。
两者在框架层解耦。这是 Codex CLI 架构设计决定。

→ 收到 provider error 时不应回退到状态重建
→ 不应将 brain 标记为受损

---

## L-004: Timeout 不导致 Corruption

分类：INFERENCE

依据：基于串行 lifecycle 观察 + Codex CLI 架构理解。
Tool timeout 是时钟限制。未直接实验验证 corruption 不存在。

→ 重试一次，然后报告
→ 不应触发 brain recovery

注意：这是推论，非实验直接验证。

---

## L-005: UI 截断非 Runtime 信号

分类：OBSERVATION

实验中观察到 UI 截断（~1MB / ~10K 行）发生时 runtime 未受影响。

→ 不应将 UI 截断作为 runtime 故障信号

注意：这是单次实验观察，不排除未来版本中 UI 截断与 runtime 状态产生关联。

---

## L-006: tool_call_id 连续性

分类：INFERENCE

若 tool_call_id 链未断，则 lifecycle 健康。
若 tool_call_id 链断裂，属于框架错误，非 brain corruption。

注意：此为架构理解 + 逻辑推断，未通过实验直接验证 tool_call_id 断裂时的行为。

---

## 未覆盖区域（UNKNOWN — 不可写入规则）

- Overlapping tool lifecycle（当前架构不支持，无法测试）
- Stream ownership collision（当前不支持多 stream）
- Streaming write 导致部分 tool_call state（未确认）
