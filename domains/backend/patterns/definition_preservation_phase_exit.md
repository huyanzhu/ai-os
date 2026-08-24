---
rule_id: definition_preservation_phase_exit
title: 跨阶段 Definition Preservation — Phase Exit 强制检查
trigger:
  - Phase 过渡时 (Phase N → Phase N+1)
  - 标准版本升级时 (AIS 系列)
  - 审批标准修改时
condition: 跨阶段/标准升级场景
action:
  do:
    - 显式检查定义漂移：新旧标准对比
    - 标准升级后自动生成"旧条件→新状态"映射表
    - 执行 Skill-005 Level 3 Definition Preservation Check
    - 将 Definition Preservation Check 设为 Phase Exit 强制步骤
  dont:
    - 跳过旧流程完成条件的迁移检查
    - 假设新标准自动覆盖旧条件
keywords:
  - definition
  - preservation
  - phase
  - exit
  - audit

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# Definition Preservation 跨阶段实践

## 背景

Phase 4.4-B→C 过渡中多次暴露出定义漂移。
每次标准升级后，旧流程的隐含完成条件容易被丢失。

## 验证方法

Definition Preservation Check (Skill-005 Level 3)

## 经验要点

1. 跨阶段过渡时必须显式检查定义漂移
2. 标准升级后，旧流程的完成条件不会自动迁移
3. Definition Preservation Check 应作为 Phase Exit 的必选项

## 关联

- EXP-AER-001: Architecture Evolution Risk
- AIS-006: Change Management Standard
- KC-PATTERN-001: Definition Drift Prevention

## 来源

KC-20260614-004 (APPROVED)