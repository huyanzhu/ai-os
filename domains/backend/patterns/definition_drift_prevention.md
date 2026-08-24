---
rule_id: definition_drift_prevention
title: Definition Drift 防护 — 标准升级时旧条件自动迁移
trigger:
  - 新标准版本发布 (AIS 系列)
  - Phase 过渡 (Phase N → Phase N+1)
  - 审批标准修改 (增加/删除验收条件)
  - 工作流定义重写
condition: 标准升级或 Phase 过渡场景
action:
  do:
    - 生成"旧条件→新状态"映射表
    - 执行 Skill-005 Level 3 Definition Preservation Check
    - 标记所有旧完成条件在新标准中的对应状态 (COVERED / PARTIAL / NEW / LOST)
  dont:
    - 仅关注"新流程应该做什么"而忽略"旧流程完成条件是否仍被覆盖"
keywords:
  - definition
  - drift
  - prevention
  - governance
  - consistency

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# KC-PATTERN-001: Definition Drift Prevention

## 模式摘要

标准版本升级时，如果仅替换或修改了某个流程的定义而未显式继承旧流程的完成条件，会导致行为悄无声息地发生变化。旧条件消失、新条件未覆盖，形成"定义漂移"。

## 典型症状

- Phase 迁移后，ONBOARD.md 仍描述旧版本的 Phase 信息
- Task 实例注册完成后，Session 目录、WORKING_STATE.md 等旧流程产物未自动生成
- 新标准升级后，旧流程中的某个验证步骤不再被执行，但无报错
- Agent 行为与文档描述不符，但非 Agent 错误

## 根因

新标准只关注"新流程应该做什么"，没有显式检查"旧流程的完成条件是否仍被覆盖"。
架构演进速度 > 定义连续性维护速度。

## 现有防护

- Skill-005 Level 3 Definition Preservation Check
- EXP-AER-001 (Architecture Evolution Risk)

## 来源

KC-PATTERN-001 (APPROVED)