---
rule_id: artifact_exists_not_consumed
title: Artifact Exists ≠ Consumed — Task 实例必须主动消费 Contract/Plan
trigger:
  - 创建新 Task 实例时
  - Task 实例在非 Main 启动的场景 (单独对话启动)
  - Contract 生成后未触发 Consumption Log 更新
  - Plan 生成被跳过或延迟
condition: Task 实例启动场景
action:
  do:
    - Task 实例启动时自动扫描 Contract (Owner = self)
    - Task 实例启动时自动扫描 Plan (Task ID 匹配 Contract)
    - 无 Contract → 禁止自主推断任务目标，请求 Main
    - 无 Plan → 请求 Main 生成
    - Task 完成时自动提示收尾 (不自动执行)
  dont:
    - Task 实例自行推断任务目标，绕过 Contract 约束
    - 完成任务后不触发 Skill-003 提示
keywords:
  - artifact
  - consumed
  - exists
  - knowledge
  - phase

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# KC-PATTERN-003: Artifact Exists ≠ Consumed

## 模式摘要

Task Contract / Execution Plan 在 tasks/ 目录中生成了，但 Task 实例在运行时没有自动读取或消费这些制品。Agent 自主推断任务目标，绕过 Contract 的约束边界，导致行为不可控。

## 典型症状

- Task 实例启动后没有读取 tasks/contracts/ 中的对应 Contract
- Task 实例自行推断任务目标，与 Contract 定义不一致
- Execution Plan 已生成但 Task 实例不知道其存在
- Task 完成但没有执行 Skill-003 收尾，TASK_INBOX 为空
- Main 实例不知道 Task 已完成

## 根因

工作流定义不完整:
1. AIS-003 定义了"实例是什么"但未定义"Runtime 必须做什么"
2. AIS-004 定义了"完成后的交握"但未定义"完成时主动提示收尾"
3. Skill-004 在实例链中未自动触发

## 现有防护

- EXP-AER-002 (Runtime Consumption Failure)
- AIS-003 v1.3 / AIS-004 v1.1 (计划中)

## 来源

KC-PATTERN-003 (APPROVED)