---
rule_id: discovery_bootstrap
title: Discovery Bootstrap — 扫描前先确认站在哪 + 锚点校准 + 否定结论复核
trigger:
  - 任何 Review / Audit / Cleanup / Migration 任务开始时
  - 让子 Agent 只读扫描整个仓库 / 知识库的任务开始时
  - Bootstrap Assembly 启动大规模 Reconciliation / Census 类任务时
condition: 即将开始扫描 / 普查 / 审计类任务
action:
  do:
    - 先确认 4 个根 (见 Pattern「Bootstrap Roots」)
    - 用"已知存在"的锚点文件 ls 校准子 Agent 实际扫到了哪
    - 凡"X 不存在 / 已失效"等全局否定结论, 必须 ls / find 独立复核后才采信
  dont:
    - 把子 Agent 的总结当事实, 未用锚点文件校准就行动
    - prompt 只给子目录路径却期待"全库"结论
    - 用 Glob 绝对路径替代 ls / find (部分环境不可靠)
    - 全局否定结论未经独立复核就进入修复 / 删除阶段
keywords:
  - discovery
  - bootstrap
  - 扫描
  - 普查
  - 审计
  - 子agent
  - 范围误判
  - 锚点校准
  - 否定结论复核
---

# Discovery Bootstrap

> 来源: AI-OS Reconciliation Sprint · Stage 1（2026-07-21 子 Agent 范围误判事故）
> 类型: Pattern
> 域: ai-os
> 关联: Guideline「Verify Before Trust」；依赖 Pattern「Bootstrap Roots」

## 模式

任何 Agent 在启动"检视 / 审计 / 清理 / 迁移"（Review / Audit / Cleanup / Migration）类任务之前，必须先完成一次 **Discovery Bootstrap**——先确认自己站在哪些根目录之上，再把扫描范围锚定到这些根，然后才开始扫描。

它已经不是"扫描范围校准"这种 Discovery 小技巧。它真正回答的是：**任何 Agent 开始工作之前，应该先知道自己站在哪里。** 这已经属于 Bootstrap，不是 Discovery 的附属物。以后 Review / Audit / Cleanup / Migration 全部可以复用。

具体三步：

1. 先确认 4 个根（见 Pattern「Bootstrap Roots」）：Product Root / AI-OS Root / Knowledge Root / Workspace Root。
2. 用"已知存在"的锚点文件校准子 Agent（或自己）实际扫到了哪——`ls known_file.md` 确认文件系统可达、路径格式正确。
3. 凡得出"X 不存在 / 已失效 / 已不成立"等全局否定结论，必须用 `ls` / `find` 独立复核后才可采信。

## 为什么

- 子 Agent 的总结描述的是它"以为"的，不一定是事实。只给子目录却期待"全库"结论时，它会把"在范围外"误判为"不存在"，并自信输出整份失真的 Census（如"文件都被删了、Census 已不成立"）。
- 这种失真比漏扫更危险：带结论的假阳性，会直接污染下游——Cleanup 会基于错误基线去删活知识。
- 根因仍是 Layer Synchronization 缺失：发现层（Discovery）与真实知识层（KB）未对齐。一次范围误判 = 发现层与知识层失同步。

## 触发条件

- 任何 Review / Audit / Cleanup / Migration 任务开始时
- 任何让子 Agent 只读扫描整个仓库 / 知识库的任务开始时
- Bootstrap Assembly 在启动大规模 Reconciliation / Census 类任务时注入此 Pattern

## 反模式

- 把子 Agent 的总结当事实，未用已知锚点文件校准就据此行动
- prompt 只给子目录路径，却期待"全库"结论
- 用 Glob 绝对路径（部分环境不可靠，连已知存在文件都返回空）替代 `ls` / `find`
- 全局否定结论未经独立复核就进入修复 / 删除阶段
