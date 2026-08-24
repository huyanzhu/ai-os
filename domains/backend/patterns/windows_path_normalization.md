---
rule_id: windows_path_normalization
title: Windows 路径归一化陷阱(点号目录与反斜杠)
trigger:
  - Windows + Java 项目包名含点号(如 com.tourism)
  - 同时存在 com.tourism(单目录含点号)和 com\tourism(两层目录)两种写法
  - 使用 PowerShell 执行文件删除操作
condition: Windows 文件系统将 \ 和 . 路径归一化，Remove-Item com\tourism 可能解析为 com.tourism
action:
  do:
    - 删除操作前先用 Test-Path 确认路径指向正确目录
    - 使用绝对路径而非相对路径
    - 删除前先 Get-ChildItem 列出文件确认
  dont:
    - 对含点号的包名目录使用含反斜杠的分隔写法删除
keywords:
  - windows
  - path
  - normalization
  - powershell
  - dot
  - backslash
  - 路径
  - 反斜杠
  - Java
  - 包名
---
alias:
  - Windows路径问题
  - 路径分隔符
  - 反斜杠转义



# Windows Path Normalization Trap (Dot vs Backslash)

## 问题
在多项目混合开发的 Java 项目中，Maven 生成的包目录结构为 com.tourism（点号作为目录名），
但 PowerShell 命令中写为 com\\tourism（反斜杠分隔的两层目录）。

当运行 Remove-Item "D:\\...\\com\\tourism" -Recurse -Force 时，
PowerShell 可能将路径解析为 com.tourism（Windows 路径归一化），
导致删除了真实的源文件目录而非预期的空目录。

## 错误现象
- maven 编译突然失败，提示找不到实体类、Mapper
- Get-ChildItem 显示 com.tourism（点号）下有文件，但 Test-Path "com.tourism\\entity" 返回 False
- 源文件目录 com.tourism\\entity\\, com.tourism\\mapper\\, com.tourism\\config\\ 等被清空

## 原因
Windows 文件系统在某些情况下会将 \\ 和 . 进行路径归一化。
当存在 com.tourism 目录且执行 Remove-Item com\\tourism 时，
PowerShell 可能将 com\\tourism 解析为 com.tourism 目录本身。
Java 的包名目录（含点号）和文件系统的目录结构在这种操作下容易混淆。

## 解决
1. 删除操作前先用 Test-Path 确认路径指向正确的目录
2. 使用绝对路径而非相对路径
3. 删除前先列出文件确认：
   \\\powershell
   Get-ChildItem "D:\\path\\to\\com.tourism" -Name  # 检查实际内容
   Remove-Item "D:\\path\\to\\com.tourism" -Recurse -Force  # 只用确认后的路径
   \\\
4. Java 项目中如果目录名含点号，避免使用含反斜杠的分隔写法

## 适用条件
- Windows 系统
- Java 项目，包名含点号（如 com.tourism）
- 同时存在 com.tourism（单目录含点号）和 com\\tourism（两层目录）两种写法
- 使用 PowerShell 执行文件删除操作

## 环境
- Windows 11
- PowerShell 5.1+
- Maven 项目，package = com.tourism
- 日期: 2026-06-26
  - Windows
  - 路径
  - 反斜杠
  - 正斜杠
  - Java

