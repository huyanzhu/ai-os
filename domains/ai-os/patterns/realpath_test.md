---
rule_id: REALPATH-TEST-001
title: 真实用户行为路径测试（主动走最顺手的路）
category: Testing Methodology
trigger:
  - 新功能验证（API 测试全绿之后）
  - 涉及多人协作/状态流转的功能（发布/托管/验收/结算）
condition: API 层测试通过但真实用户路径未验证
action:
  do:
    - 主动走一遍「真实用户最顺手的路径」——含捷径/绕路/图省事的操作（如任务级确认验收而非逐里程碑）
    - 用真人 UI 采样（发布→托管→逐里程碑→验收）作为 API 测试的补充
    - 追问一句：真实用户会怎么走"最顺手的那条路"？那条路正是 bug 藏身地
  dont:
    - 只测"接口正不正确"就交付（API 全绿 ≠ 真实路径安全）
    - 假设用户会按文档/规范路径走（真实用户走捷径）
keywords:
  - 真实用户
  - 行为路径
  - UI 采样
  - 验收
  - 走捷径
  - 对抗
alias:
  - 真实路径测试
  - 行为路径测试
  - 走最顺手的路
  - realpath test

knowledge_position: Cluster
knowledge_cluster: FC-Test Methodology
epistemology_tag: PATTERN
confidence: HIGH
---

# 真实用户行为路径测试

**来源**：ai-consultant 开发 Agent 真实使用（2026-08-06）——生命周期真人 UI 采样（发布→托管→逐里程碑→验收）抓到 API 测试全绿抓不到的 P0：需求方点任务级「确认验收」绕过逐里程碑结算，接单方实收 ¥0。**API 测试验证"接口正不正确"，采样验证"真实用户会怎么走"；真实用户走捷径/走错路，捷径正是 bug 藏身地。**

**关联**：与必达教训 §1.5 第二条「测试按角色流覆盖（含对抗路径）」同源——本文件是其正面方法论版（主动走真实路径），对抗路径是防守版（主动越权尝试）。
