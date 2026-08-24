---
rule_id: agent_bypassing_content_transport
title: Agent 绕过 Runtime 手工跨进程传输内容
trigger:
  - node -e
  - python -c
  - echo "..." |
  - shell pipe with content
  - PowerShell here-string passed to external process
  - 通过 shell 管道传输代码或文本内容
  - 跨进程传中文出现乱码
condition: Agent 需要把内容传给另一个进程（node、python、curl 等）时，手工通过 shell 管道拼接
action:
  do:
    - ① 用 Write 工具先写文件（Runtime 保证 UTF-8 编码）
    - ② 指向文件执行（node file.js，python file.py）
    - ③ 让 Runtime 处理跨进程的编码/转义/分隔符
  dont:
    - 不要用 node -e 传多行或含中文的代码
    - 不要用 python -c 传大段内容
    - 不要用 echo "..." | 传代码
    - 不要手工在 shell 里拼接跨进程内容管道
    - 不要假设 shell 和外部进程共享同一编码
keywords:
  - runtime boundary
  - content transport
  - encoding
  - pipe
  - node -e
  - python -c
  - powershell encoding
  - 跨进程
  - 编码损坏
  - 乱码

knowledge_position: Cluster
knowledge_cluster: Runtime Boundary
epistemology_tag: PATTERN
confidence: HIGH
---

# Runtime Boundary Violation — Agent 手工跨进程传输内容

## 问题

Agent 在需要执行代码时，手工通过 shell 管道拼接内容传给外部进程（`node -e`、`python -c`、`echo |` 等），
导致编码损坏（中文变乱码）、转义错误、或语法解析失败。

根源不是编码不对。根源是 Agent 跨过了 Runtime Boundary——内容传输是 Runtime 的职责。

## What

2026-07-11 LIFECYCLE-001B 实验中，Agent 用 PowerShell here-string 拼接 `node -e` 传参，
含中文的 JS 代码在跨进程传输时被双重编码损坏（PowerShell gb2312 → Node.js 不同代码页）。

`奶茶` → `濂惰尪`，`点餐` → `鐐归`。

## Why

```
PowerShell 内存 (UTF-16 LE — 正确)
  ↓ 传给外部进程 node
$OutputEncoding (gb2312) 做转换
  ↓
gb2312 字节流
  ↓ node 按 OEM 代码页解释
乱码
```

Agent 手工操作了内容通道——Runtime 没有机会介入。
如果走 Write → node file.js，Runtime 保证 UTF-8，不存在这个问题。

## Delta

Agent 不通过 shell 管道传输内容。

```
✗ node -e "...中文代码..."
✗ echo "...代码..." | node
✗ python -c "...大段内容..."

✓ Write 工具写文件 → node file.js
✓ Write 工具写文件 → python file.py
```

## 触发条件

任何时候 Agent 需要把代码或文本内容传给外部进程时：
- 先用 Write 工具写入文件
- 再让外部进程读文件
- 编码由 Runtime（Write 工具）保证

## 为什么放在 runtime-boundary/

这个 pattern 不是"编码失败"。编码损坏只是表象。
真正的模式是：**Agent 跨越了 Runtime 的内容传输边界**。

以后所有 stdin/stdout/temp file/socket 的边界问题，都引用同一个 pattern 和同一个原则：
**Runtime owns content transport.**
