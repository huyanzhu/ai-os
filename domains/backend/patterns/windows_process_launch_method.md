---
rule_id: windows_process_launch_method
title: Windows Start-Process 与 cmd /c start 行为差异
trigger:
  - PowerShell Start-Process 启动某些进程(如 mysqld.exe)挂起或启动失败
  - Start-Process 导致进程启动后立即退出
condition: Start-Process 与 cmd /c start 对某些进程行为不同
action:
  do:
    - 使用 cmd /c start "" mysqld.exe 替代 Start-Process
  dont:
    - 对 mysqld.exe 等进程使用 Start-Process
keywords:
  - windows
  - start-process
  - cmd
  - launch
  - process
  - powershell
  - 启动
  - 进程
  - 方法
  - mysqld
alias:
  - Windows进程启动
  - Start-Process差异
  - cmd启动
---

## 问题
PowerShell 的 Start-Process 和 cmd /c start 对某些进程（如 mysqld.exe）的行为不同。
Start-Process 可能导致进程挂起或启动失败。

## 错误现象
- Start-Process mysqld.exe 导致 MySQL 启动后立即退出

## 解决
使用 cmd /c start "" mysqld.exe 替代 Start-Process

## 环境
- Windows
- 日期: 2026-06-28