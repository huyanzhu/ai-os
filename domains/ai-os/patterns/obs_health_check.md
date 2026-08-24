---
rule_id: obs_health_check
title: OBS 健康检查标准流程
category: Governance
trigger:
  - 需要执行 OBS 健康检查时
  - Phase Freeze Day 检查
  - Phase 切换前（与 Phase Exit Audit 联动）
condition: 治理维护场景
action:
  do:
    - 全量扫描所有 OBS 记录
    - 逐条审查状态: CLOSED / ACTIVE
    - CLOSED 需有完整 修复→验证→审计 证据链
    - ACTIVE 需注明原因和观测周期
    - 归档无僵尸 OBS、无 UNKNOWN 状态
  dont:
    - 允许 OBS 处于 UNKNOWN 状态
    - 关闭 OBS 但没有修复验证证据链
keywords:
  - obs
  - health
  - telemetry
  - monitoring
  - check

knowledge_position: Standalone
knowledge_cluster: 
epistemology_tag: PATTERN
confidence: HIGH
---

# OBS 健康检查方法论

## 触发时机

主实例在每个 Phase 切换前，或至少每 7 天一次，
应检查所有 ACTIVE 状态的 OBS 条目，判断其状态是否需要更新。

检查结果作为 Phase Exit Audit（Skill-005）的输入。

## 标准流程

1. 全量扫描所有 OBS
2. 逐条审查
3. 分类 CLOSED / ACTIVE
4. 记录最终结论
5. 归档

## 检查结果示例 (2026-06-14)

9 个 OBS 中 6 个 CLOSED（含完整修复→验证→审计链），3 个 ACTIVE（长期观察）。
无僵尸 OBS、无 UNKNOWN 状态。