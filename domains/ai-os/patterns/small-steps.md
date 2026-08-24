---
rule_id: small_steps
title: Small Steps — 小 commit / 小 PR / 小步开发
trigger:
  - 任何开发任务开始时
  - Bootstrap Assembly 在 TaskStarted 时注入
  - 改动涉及多文件 / 多功能时
condition: 开发任务进行中
action:
  do:
    - 每完成一个功能立即提交
    - 保持小 commit (易回滚) / 小 PR (<400 lines, 易审查)
    - 每步可验证后再进下一步
  dont:
    - 一次改 10 个文件后才提交
    - 一个 PR 包含 3 个不相关的功能
keywords:
  - small-steps
  - commit
  - PR
  - 小步
  - 回滚
  - 审查
  - 风险
---

# Small Steps

> 来源: GitHub Flow, Linear Method
> 类型: Pattern
> 域: ai-os

## 模式

小 commit、小 PR、小步开发。每次改动尽量小，每完成一个功能立即提交。

## 为什么

- 小 PR 容易审查（<400 lines）
- 小 commit 容易回滚
- 小步开发降低风险——每步可验证

## 触发条件

- 任何开发任务开始时
- Bootstrap Assembly 在 TaskStarted 时注入

## 反模式

- 一次改 10 个文件后才提交
- 一个 PR 包含 3 个不相关的功能