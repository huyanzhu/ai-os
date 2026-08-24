---
rule_id: git_safety_net
title: Git 作为文件操作安全带
trigger:
  - 文件操作可能产生不可逆错误(编码写乱、文件误删、批量改坏、配置崩了)
  - 任何有 git 的项目
condition: 改文件前/后需要确认状态或恢复原样时
action:
  do:
    - 改文件之前先 git status 确认状态
    - 改乱之后 git diff 看实际改了啥
    - git checkout 恢复原样
  dont:
    - 不确认状态直接批量改文件
keywords:
  - git
  - safety
  - checkout
  - diff
  - status
  - encoding
  - recovery
  - 恢复
  - 回滚
  - 版本控制
alias:
  - git回滚
  - 文件恢复
  - git安全网
  - 文件安全
---

# Git 作为文件操作安全带

## 问题
文件操作可能产生不可逆的错误：编码写乱、文件误删、批量改坏、配置崩了。

## 解决
改文件之前先 git status 确认状态，改乱之后 git diff 看实际改了啥，git checkout 恢复原样。
git 不只是版本管理——它是文件操作的安全带。

## 环境
- 任何有 git 的项目
- 日期: 2026-06-29