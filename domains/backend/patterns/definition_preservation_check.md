---
rule_id: definition_preservation_check
title: 跨阶段过渡时执行 Definition Preservation Check
category: Governance
trigger:
  - Phase 过渡
  - 标准版本升级
  - 工作流定义修改
condition: 架构治理场景
action:
  do:
    - 获取变更前和变更后的验收条件清单
    - 逐项对比旧条件是否存在或其方式替代
    - 执行 Skill-005 Definition Preservation Check
    - BROKEN 禁止部署，重新评估
    - PARTIAL 标记风险，人工确认后部署
  dont:
    - 直接替换验收条件而不追溯旧条件
    - 假设"新版更好"而忽略旧版的有意设计
keywords:
  - definition
  - preservation
  - audit
  - check
  - freeze
  - 定义漂移

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# Definition Preservation 跨阶段实施

## 背景

Phase 4.4-B→C 过渡再次暴露出定义漂移。每次标准升级后，旧流程的隐性完成条件容易丢失。

## 验证方法

Definition Preservation Check (Skill-005 Level 3)

## 经验要点

1. 跨阶段过渡时必须显式检查定义漂移
2. 标准升级后，旧流程的完成条件不会自动迁移
3. Definition Preservation Check 应作为 Phase Exit 的必选项

## 【修复注记】2026-08-23 Integrity repair（Knowledge Space Maintenance v2）

- 原文件为已固化的 GBK 错位乱码（提交时即损坏，git HEAD 同样损坏）
- 修复方式：GBK 编码反转恢复 + 依据上下文补全明显丢失字符（约 27 处字符不可恢复）
- 原始损坏版本保留于备份：`D:\AI\scratch\tmp\a4-corrupted-backup-2026-08-23\`
