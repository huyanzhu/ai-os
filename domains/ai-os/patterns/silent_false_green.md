---
rule_id: SILENT-FALSE-GREEN-001
title: 测试命令的 cwd 陷阱：collected 0 items + 退出码 0 = 静默假绿（比报错危险）
category: Testing Methodology
keywords:
  - 测试
  - cwd
  - collected 0
  - 静默假绿
  - pytest
trigger:
  - 跑测试/验证命令时
  - pytest 报告 "collected 0 items" 或 "no tests ran" 时
  - 在子目录（如 src/）执行项目根目录的测试命令时
condition: 测试命令用相对路径（python -m pytest tests/），而执行目录不是项目根
action:
  do:
    - 看退出码之外，必须看 collected N（N>0 才算真跑）
    - 确认 cwd 在项目根目录再跑测试（tests/ 相对路径只在根目录解析正确）
    - 命令不灵时先查环境（cwd/解释器/依赖），再怀疑代码（environment_first 精神）
    - 把"必须在根目录执行"写进 README/约定，防后来者踩坑
  dont:
    - 把"退出码 0"当测试通过（假绿会让错误永远不被发现，比报错危险）
    - 在子目录直接跑相对路径测试命令
---
# 静默假绿：collected 0 items + 退出码 0

**来源**: Environment Test v5 Tester 事后实测发现（2026-08-08）——在 src/ 子目录执行 `python -m pytest tests/`，tests/ 解析成 src/tests/（不存在），pytest 返回 collected 0 items / no tests ran 且**退出码 0**——比报错更危险：会让人误以为测试通过了。注：Tester 复盘后额外实测的发现（非第一轮实验行为），经验本身真实有效。
