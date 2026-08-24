---
rule_id: DEBUG-RECON-001
title: 端到端对账：UI 不符时读权威数据层还原代码路径
category: Debugging Methodology
trigger:
  - UI 表现与预期不符
  - 金额/状态对不上（结算/里程碑/验收）
condition: 界面或 API 响应与预期矛盾，需要判定"产品 bug 还是我测错了"
action:
  do:
    - 直接读权威数据层（SQLite/DB 整行），跳过 UI 与 API 响应
    - 还原「是哪条代码路径写出了当前这行」→ 对照「应该是哪条路径」
    - 差异点即根因定位（旁路/漏写/跳步都在数据行里显形）
  dont:
    - 在 UI 或可能过期的 API 响应上猜（会被缓存/渲染层掩盖真相）
    - 凭界面表现判定"是 bug 还是我测错了"
keywords:
  - 对账
  - 调试
  - 数据层
  - 还原
  - 结算
  - 根因
alias:
  - 端到端对账
  - 读数据层
  - debug recon

knowledge_position: Cluster
knowledge_cluster: FC-Debug Methodology
epistemology_tag: PATTERN
confidence: HIGH
---

# 端到端对账：读权威数据层还原代码路径

**来源**：ai-consultant provider 测试账号真实使用（2026-08-06）——任务级「验收完成」旁路跳过结算：点验收后任务显示 completed 但接单方没收到钱、里程碑没翻 accepted；同发布者另两个任务都正确结算 ¥99.99。靠直接读 data.db 才确认是「任务级验收」这条旁路跳过了结算与翻转——**如果只看界面，永远分不清是产品 bug 还是测错了**。

**核心**：UI 不符预期 → 不问界面，问数据。数据行会告诉你「哪条路径写出了它」，路径与预期路径的差异 = 根因。
