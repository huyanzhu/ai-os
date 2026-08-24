---
rule_id: STDERR-CHANNEL-001
title: 错误信息必须走 stderr（测试断言 err 会暴露输出通道问题）
category: Engineering Discipline
keywords:
  - stderr
  - stdout
  - 错误通道
  - CLI
  - 测试断言
trigger:
  - 写 CLI/脚本的错误输出时
  - 测试断言 stderr 失败时
  - 错误信息与正常输出混淆时
condition: 程序既有正常输出（stdout）又有错误输出
action:
  do:
    - 错误信息一律写 stderr（print(..., file=sys.stderr)），正常结果写 stdout
    - 测试同时断言 out 与 err——通道混用会被测试当场暴露（断言 err 失败）
    - 错误输出带非零退出码（成功 0 / 失败非 0），与通道分离成双保险
  dont:
    - 错误信息打 stdout（会污染正常输出、被管道/UI 误当成结果）
    - 只修测试不修通道（断言 err 失败是症状，根因是输出通道错了）
---
# 错误信息走 stderr

**来源**: Environment Test v3 Tester 真实经验（2026-08-08）——收尾时"修复 stderr 分流"：错误打 stdout → 测试断言 err 失败 → 改实现把错误改走 stderr。
