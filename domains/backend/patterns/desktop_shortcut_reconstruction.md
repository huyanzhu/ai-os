---
rule_id: desktop_shortcut_reconstruction
title: 桌面快捷操作中心应只做索引引用，不持有架构数据
category: Architecture Design
trigger:
  - 桌面入口文档与实际系统架构不一致
  - Toolkit 架构层数与当前系统不符
condition: 桌面入口设计场景
action:
  do:
    - 桌面入口只做索引和引用，不重复存储架构数据
    - USER_MANUAL.md 作为权威来源
    - 架构升级后 Toolkit 与 USER_MANUAL.md 同步更新
  dont:
    - 在桌面入口中存储完整的架构数据副本
    - 架构升级后不同步更新桌面入口
keywords:
  - desktop
  - shortcut
  - index
  - architecture
  - toolkit
  - 桌面
  - 快捷方式
  - 架构
  - 索引
  - 工具
alias:
  - 桌面入口
  - 快捷操作中心
  - 桌面索引
knowledge_position: Standalone
knowledge_cluster:
epistemology_tag: PATTERN
confidence: HIGH
---

# 桌面快捷操作中心重构经验

## 问题

Operator Toolkit 原 README 停在 Phase 4.2-B，架构层只有 5 层（缺 4 层）。

## 解决方案

重构后升级至 Phase 4.4-C，新增 ARCHITECTURE_OVERVIEW.md（含踩坑地图）。关键设计：USER_MANUAL 作为权威来源，Toolkit 只做速览和引用，不持有架构数据。

## 经验要点

1. 桌面入口应只做索引和引用，不重复存储架构数据
2. 踩坑地图显著降低了新实例的问题排查时间
3. 架构升级后 Toolkit 与 USER_MANUAL.md 必须同步更新
