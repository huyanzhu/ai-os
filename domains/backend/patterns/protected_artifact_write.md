---
rule_id: protected_artifact_write
title: 修改受保护文件前必须进入危险操作模式
trigger:
  - 写入 AGENTS.md / ARCHITECTURE_DECISIONS.md / Pattern 文件 / Registry 文件
  - Append / Replace / Move / Delete 受保护文件
  - 文件写入后出现乱码或内容丢失
alias:
  - 危险写入协议
  - 文件损坏
  - 追加丢失
  - BOM 污染
  - 写入验证
condition: 任何涉及 D:\AI\ 核心文件的修改操作时
action:
  do:
    [0m- ① 备份：修改前确认 git 中有可恢复的提交
    - ② 正确方式：用 [System.IO.File]::WriteAllText + UTF8Encoding(false)，禁止 Out-File -Append / Set-Content
    - ③ 立即验证：写入后立刻读取尾部，确认中文无乱码
    - ④ 再继续：验证通过后才进入下一步
  dont:
    - 不要用 Out-File / Set-Content / Add-Content 写受保护文件
    - 不要写完就走，不验证编码
    - 不要在同一操作中并行读写同一文件
    - 不要跳过 AGENTS.md 已有的 Sanity Check 流程
keywords:
  - 写入
  - 覆盖
  - 追加
  - append
  - out-file
  - set-content
  - add-content
  - 乱码
  - BOM
  - 编码
  - encoding
  - writealltext
  - 验证
  - 备份
  - 受保护文件

  - 写入
  - 保护
  - 覆盖
  - 追加
  - 危险操作
  - core file
epistemology_tag: PATTERN
confidence: HIGH
---

# 受保护文件写入协议

## 问题
直接对 AI-OS 核心文件（AGENTS.md、Architecture Decisions、Pattern、Registry）
执行写入/追加/替换，不经过验证，导致：
- 文件编码损坏（BOM 插入中间段 → 中文全部乱码）
- 内容丢失（错误覆盖 → git 恢复浪费时间）
- 无限循环写入（870MB 事故）

## 触发条件
以下任一文件被修改时，必须进入此协议：
- D:\AI\AGENTS.md
- D:\AI\registry\ARCHITECTURE_DECISIONS.md
- D:\AI\registry\MAINTENANCE_REGISTRY.md
- D:\AI\registry\CHANGE_REGISTRY.md
- D:\AI\registry\INSTANCE_REGISTRY.md
- D:\AI\brain\patterns\ 下所有文件
- D:\AI\CURRENT_PHASE.md

## 四步协议

 + "`	ext" + @"
① 有没有备份？
   → git log 确认可恢复的提交存在
   → 若不存在，先 git add + commit

② 有没有正确写入方式？
   → 统一使用 [System.IO.File]::WriteAllText + UTF8Encoding(False)
   → 禁止 Out-File / Set-Content / Add-Content

③ 写完立即验证
   → 读取文件末尾 5-10 行
   → 确认中文无乱码、行数合理、无重复段落 >100 次

④ 再继续
   → 验证通过后才进入下一步操作
" + "`" + @"

## 真实案例
2026-06-30：codex使用教程.txt 追加 section 十，用 Out-File -Append -Encoding UTF8，
BOM 插入中间段，后续中文全部变成 mojibake。git 恢复 → .NET 重写 → 两次才修好。
此 pattern 本身就是在踩了这个坑后创建的。

## 与现有规则的关系
AGENTS.md § Protected Artifact Write Protocol 已有 Sanity Check + Size Guard。
本 pattern 是操作层面的 checklist——确保每个写操作都走完四步，不跳过。

## 环境
- AI-OS Phase 7C
- Windows 11 + PowerShell
- 日期: 2026-06-30