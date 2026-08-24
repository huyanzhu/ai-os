---
rule_id: bootstrap_roots
title: Bootstrap Roots — 任何任务开始前先确认 4 个根
trigger:
  - 任何 Agent 任务初始化 (Bootstrap Assembly) 时
  - 跨目录 / 跨仓库的普查、迁移、清理任务开始时
  - 即将执行 Review / Audit / Cleanup / Migration 前
condition: Agent 任务初始化, 未确认所在根目录
action:
  do:
    - 开始执行前依次确认 4 根: Product Root / AI-OS Root / Knowledge Root / Workspace Root
    - 每个根的答案必须指向真实存在的目录 (用 ls / find 核实)
    - 4 根未确认前, Discovery / 扫描 / 普查结果不可采信
  dont:
    - 任务开始即扫描, 未先确认 4 根
    - 假设"当前目录就是全部", 忽略父目录 / 兄弟目录的知识资产
    - 把默认 cwd 当成 Product / AI-OS / Knowledge 根
keywords:
  - bootstrap
  - roots
  - 根目录
  - discovery
  - 普查
  - 迁移
  - 清理
  - 范围误判
  - 站在哪
---

# Bootstrap Roots（四根原则）

> 来源: AI-OS Reconciliation Sprint（2026-07-21，由"扫错根目录致 Census 失真"事故泛化）
> 类型: Pattern（Bootstrap 层基础原则）
> 域: ai-os
> 关联: Pattern「Discovery Bootstrap」

## 模式

任何 Agent 在开始执行（Review / Audit / Cleanup / Migration / 任意任务）之前，必须依次回答 4 个根，且答案必须指向**真实存在**的目录：

1. **Product Root** —— 产品代码与产品级文档所在根（如 `d:\AI\projects\ai-consultant`）
2. **AI-OS Root** —— AI-OS 框架 / 规范所在根（如 `d:\AI`）
3. **Knowledge Root** —— AI-OS 知识库所在根（如 `d:\AI\domains\ai-os`）
4. **Workspace Root** —— 当前工作区 / 会话产出根

四个根未确认前，Discovery / 扫描 / 普查的结果**不可采信**。

## 为什么

- 今天最贵的教训：一次"把 AI-OS 知识库当成不存在"的范围误判，差点让 Stage 2 基于错误基线去删活知识。根因不是"工具不准"，是 Agent 开始工作前**没确认自己站在哪**。
- 知识资产与产品运行时往往不在同一根（AI-OS 知识库在父目录 `d:\AI`，产品在 `d:\AI\projects\ai-consultant`）。不先钉死根，任何"全库"结论都是空中楼阁。
- 这是 Knowledge ≠ Documentation、Layer Synchronization 的前端防线：Bootstrap 先把"站在哪"说清，后续所有知识操作才有锚。

## 触发条件

- 任何 Agent 任务初始化（Bootstrap Assembly）时注入
- 尤其：跨目录 / 跨仓库的普查、迁移、清理任务

## 反模式

- 任务开始即扫描，未先确认 4 根
- 假设"当前目录就是全部"，忽略父目录 / 兄弟目录的知识资产
- 把"默认 cwd"当成 Product / AI-OS / Knowledge 根
