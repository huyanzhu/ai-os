---
rule_id: false_signals
title: 常见误判信号列表 — 不应传播到 Brain State 分析
trigger:
  - invalid_request_error
  - insufficient_tool_messages
  - UI output 截断
  - tool_timeout
  - Session kill
  - Session killed
  - 会话终止
  - Tool call 跨多轮
  - Provider Error
  - Provider Failure
  - Model Provider Error
condition: 分析失败时，怀疑为 brain corruption / lifecycle failure / replay state
action:
  do:
    - 检查信号是否在 FALSE 列表中
    - 如果在列表中 → 不传播到 brain state 分析
    - 作为独立错误报告，不作为系统性 corruption
  dont:
    - 将 FALSE 列表中的信号认定为 brain corruption
    - 将 UI 截断作为 runtime 故障信号
    - 将单次异常视为系统性故障
    - 将环境问题误判为 Governance 问题
    - 在证据不足时升级为 Architecture 缺陷
keywords:
  - false
  - signal
  - governance
  - drift
  - misdiagnosis

knowledge_position: Standalone
knowledge_cluster: 
epistemology_tag: OBSERVATION
confidence: MEDIUM
---

# false_signals.md
# 层级: L3 Learned Rules
# 来源: Runtime Boundary Mapping (2026-05-29)
# 实验环境: deepseek-v4-flash + Codex CLI (Windows, PowerShell)

## 用途

列出曾被误认为 brain corruption、tool lifecycle failure 或 replay state 的信号。
每个信号的新解释拆分为 Architecture Note 和 Observation 两部分。

---

## 信号表

### invalid_request_error

- 旧解释：Brain state 受损
- Architecture Note（FACT）：Provider 侧协议错误，brain 未受影响。两者在框架层解耦。
- Observation（OBSERVATION）：实验中此错误发生时 brain 状态正常。

### insufficient_tool_messages

- 旧解释：Lifecycle 链断裂
- Architecture Note（FACT）：属于框架层消息计数检查机制。
- Observation（OBSERVATION）：实验中未观察到通过正常 reasoning/tool sequencing 触发。
  注意：实验规模有限，"未观察到"不等于"不可触发"。

### UI output 截断

- 旧解释：Tool runtime crash
- Architecture Note（FACT）：UI 为独立展示层，与 runtime tool 执行解耦。
- Observation（OBSERVATION）：实验中 UI 截断发生时 runtime 未受影响（~1MB / ~10K 行截断点）。

### tool_timeout

- 旧解释：Lifecycle hung
- Architecture Note（FACT）：Timeout 是客户端侧时钟限制机制。
- Inference（INFERENCE）：基于串行 lifecycle 架构理解，timeout 不导致 corruption。
  注意：未直接实验验证 corruption 不存在。

### Session kill

- 旧解释：Lifecycle 残留
- Observation（OBSERVATION）：实验中 session A 强制终止后 session B 启动干净。
  注意：验证规模为 single data point。

### Tool call 跨多轮

- 旧解释：Lifecycle 重叠怀疑
- Observation（OBSERVATION）：当前 CLI 串行模式，每轮一个 tool，多轮是正常行为。
  Architecture Note（FACT）：串行调度禁止重叠。

---

## 故障分析指引

分析失败时：
1. 首先检查信号是否在 FALSE 列表中
2. 如果是，不传播到 brain state 分析
3. 作为独立错误报告，不作为系统性 corruption



