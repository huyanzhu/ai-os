---
rule_id: ASSERT-RECALC-001
title: 写端到端验证脚本前先独立核算断言
category: Testing Methodology
trigger:
  - 写端到端验证脚本/断言前
  - 涉及多笔金额/状态累计的断言
condition: 断言依赖手工心算或对被测代码结果的"感觉"
action:
  do:
    - 先纸面过一遍账（独立于被测代码重算：列出每笔、独立求和）
    - 断言值永远来自独立重算，不来自被测代码输出
    - 心算易漏项时，把中间量也写进断言注释（300−80+80+100−60=540 这样列全）
  dont:
    - 心算直接进断言（漏一项 = 把产品判错 = 白费一轮验证）
    - 断言值复制被测代码的中间结果（自证）
keywords:
  - 断言
  - 独立核算
  - 验证脚本
  - 心算
  - 对账
alias:
  - 断言独立核算
  - 先算账再断言
  - recalc assertions

knowledge_position: Cluster
knowledge_cluster: FC-Test Methodology
epistemology_tag: PATTERN
confidence: HIGH
---

# 写验证脚本前先独立核算断言

**来源**：ai-consultant 开发 Agent 真实使用（2026-08-06）——两次把产品判断成 bug：第一次漏算退款 ¥80（300−80+80+100−60 心算成 460，实际 540），第二次漏算 +80（500−80+100−60 又算错）——**产品功能全对，是断言心算错了，浪费两轮验证**。

**核心**：断言永远独立于被测代码重算。先纸面过账，再写断言；中间量列全（防止心算漏项）。
