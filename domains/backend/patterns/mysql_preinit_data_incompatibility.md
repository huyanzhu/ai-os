---
rule_id: mysql_preinit_data_incompatibility
title: MySQL 预初始化数据跨机器不兼容
trigger:
  - 从一台机器复制预初始化 MySQL data/ 目录到另一台机器
  - 跨机器迁移 MySQL 数据目录后启动失败
condition: MySQL 版本/配置/文件路径不同的机器间复制 data/ 目录
action:
  do:
    - 在新机器上重新执行 init.sql 初始化
  dont:
    - 直接复制 data/ 目录到不同机器(版本/配置/路径不同导致不兼容)
keywords:
  - mysql
  - data
  - init
  - compatibility
  - migration
  - cross-machine
  - 数据
  - 初始化
  - 兼容
  - 迁移
  - 跨机器
alias:
  - MySQL数据不兼容
  - 跨机器迁移
  - 数据目录复制
---

## 问题
预初始化的 MySQL 数据目录（data/）从一台机器复制到另一台机器后不兼容。
不同机器的 MySQL 版本、配置、文件路径不同导致数据目录无法直接使用。

## 错误现象
- 从开发机复制 data/ 到演示机后 MySQL 启动失败

## 解决
每次在新机器上重新执行 init.sql 初始化，不复制 data/ 目录。

## 环境
- MySQL 8.0+
- 日期: 2026-06-28