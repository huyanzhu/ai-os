---
rule_id: kaf-002-catch-all-trigger
title: Catch-All Trigger 治理 — KAF-002 闭环记录
trigger:
  - 发现 Trigger 可解释超过 50% 的不同故障类型时
  - Trigger Ambiguity Audit 判定 Misfire Rate > 20% 时
condition: Brain Normalization 阶段
action:
  do:
    - 执行 Trigger Ambiguity Audit
    - 执行 Trigger Governance Report（G1-G4 评级）
    - 将 G4 Catch-All 拆解为 Canonical Trigger
    - 执行 Blind Retrieval Test 验证
    - Precision ≥ 90% 且 Recall ≥ 90% → Brain Index Ready
  dont:
    - 在 Precision 极低时继续增加 Trigger
    - 用 Sematic Trigger 替代 Canonical Trigger
    - 将 Coverage Gap 和 Overfitting 混为一谈
keywords:
  - trigger
  - catch-all
  - kaf
  - precision
  - recall

knowledge_position: Standalone
knowledge_cluster: 
epistemology_tag: FACT
confidence: HIGH
---

# KAF-002 — Catch-All Trigger Governance

## Metadata

ID: KAF-002

Title: Catch-All Trigger Governance

Status: Closed

Result: Brain Index Ready

Date: 2026-06-02

---

## Problem Statement

发现 environment_first 存在 Trigger：

`操作失败且原因不明`

该 Trigger 实际表现为 Catch-All Trigger。

---

## Initial Metrics

Before Refactoring

| Metric                  | Value |
|-------------------------|-------|
| Precision               | 25%   |
| Recall                  | 100%  |
| Misfire Rate            | 75%   |
| Catch-All Trigger Count | 1     |
| G4 Trigger Count        | 1     |

---

## Root Cause

问题类型：Trigger Overfitting

Trigger：`操作失败且原因不明`

实际覆盖：
- Spring MVC 404
- Spring MVC 500
- Provider Error
- Model Error
- Tool Failure
- Network Failure
- Filesystem Failure
- Sandbox Failure

导致：高 Recall，低 Precision。

---

## Governance Process

### Phase 2.3-D — Trigger Ambiguity Audit
Misfire Rate = 75%。判定：Trigger Overfitting Confirmed。

### Phase 2.4-A — Trigger Governance Report
`操作失败且原因不明` 评级 G4 — Catch-All。

### Phase 2.4-B — Trigger Refactoring Design
替换为：network blocked, proxy blocked, filesystem write/read blocked, Desktop write denied, cwd inaccessible, sandbox restriction, unexpected runtime failure。

### Phase 2.4-C — Canonical Trigger Completion
- tool_boundary: PowerShell syntax error, unexpected command output
- false_signals: Provider Error, Provider Failure, Model Provider Error
- wechat_dev_pitfalls: 微信开发工具崩溃, DevTools Crash, WeChat DevTools Crash
- fresh_context: Token Limit Exceeded

---

## Final Metrics

Blind Retrieval Test v3

| Metric                  | Value |
|-------------------------|-------|
| Precision               | 100%  |
| Recall                  | ~91%  |
| Misfire Rate            | 0%    |
| Collision Rate          | ~4.5% |
| Catch-All Trigger Count | 0     |
| G4 Trigger Count        | 0     |

---

## Outcome

**Brain Index Ready**

---

## Lessons Learned

### Rule 1
Catch-All Trigger 必须避免。任何能够解释超过 50% 不同故障类型的 Trigger 都应视为高风险。

### Rule 2
优先治理 Precision。当 Precision 极低时，不要继续增加 Trigger，应先拆解 Trigger。

### Rule 3
Canonical Trigger 优于 Semantic Trigger。优先 `Permission Denied`，而不是 `操作失败且原因不明`。

### Rule 4
Trigger Coverage Gap 与 Trigger Overfitting 是两类不同问题，必须先区分。

---

## Governance Tag

Tags: Trigger Governance, Catch-All Removal, Precision Improvement, Brain Index Ready, KAF-002

---

## Closure

KAF-002 — Closed — Approved — Brain Index Ready
