---
rule_id: powershell_dollar_colon_namespace
title: PowerShell 中 $Name: 被解析为命名空间引用需用 ${Name}: 或单引号
trigger:
  - PowerShell 脚本中 $Name: 导致语法错误
  - 需要在字符串中使用 $Name: 形式
condition: PowerShell 中 $Name: 被解析为命名空间引用而非字面量字符串
action:
  do:
    - 改用 ${Name}: 形式
    - 使用单引号字符串 '$Name:'
  dont:
    - 直接写 $Name: (被解析为 PowerShell 命名空间引用)
keywords:
  - powershell
  - dollar
  - colon
  - namespace
  - syntax
  - variable
  - 命名空间
  - 语法
  - 变量
  - 冲突
alias:
  - PowerShell变量冲突
  - 美元符号冒号
  - 命名空间冲突
---

## 问题
PowerShell 中 $Name: 被解析为 PowerShell 名空间引用，而不是字面量字符串。
需要用 ${Name}: 或 '$Name:' 来避免解析。

## 错误现象
- 脚本中 $Name: 导致语法错误

## 解决
改为 ${Name}: 或使用单引号字符串 "$Name:"

## 环境
- Windows PowerShell 5.1+
- 日期: 2026-06-28