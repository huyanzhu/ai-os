---
rule_id: skill_fusion_security_check
title: Security Check 安全审查
trigger:
  - 代码完成/commit 前需要安全审查
  - 涉及输入校验/认证/密钥/供应链
keywords:
  - security
  - 安全
  - 审查
  - 注入
  - xss
  - 供应链
action:
  do:
    - 审查范围：diff/注入面(SQL/命令/路径/模板/XSS)/认证授权/密钥凭证/供应链/不安全默认值；分级 high/medium/low/info
---

# Security Check

## 是什么
在「代码完成」时，对本次改动做安全审查的能力。识别安全漏洞与弱点，产出分级 findings + 报告，可沉淀为 Pattern / Observation。

参考外部标杆：trailofbits/skills 的 `c-review`（安全代码审查，输出 SARIF）、`static-analysis`（CodeQL/Semgrep）、`supply-chain-risk-auditor`、`insecure-defaults`、`zeroize-audit`。取其「能力概念」适配本项目（JS/TS/Python），不搬运 C/C++ 专用工具链。

## 什么时候用
TaskCompleted 事件 → Security Check Hook 自动触发。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 在 commit / 完成前手动模拟触发。）

## 审查范围（默认）
- 本次 diff / 新增文件
- 输入校验与注入面：SQL / 命令 / 路径 / 模板注入、XSS
- 认证、授权、会话、密钥与凭证处理
- 依赖与供应链：第三方包风险、锁文件完整性
- 不安全默认值、敏感数据清零、日志中的敏感信息

## 输出格式
分级报告（severity: high / medium / low / info），含位置、类别、描述、修复建议。
模板：templates/security-check.md
可沉淀：重复出现的漏洞类 → Pattern；一次性发现 → Observation（经 knowledge-capture）。

## 参考来源（外部 Skill 融合）
- trailofbits/skills (6.1k star)：c-review、static-analysis、supply-chain-risk-auditor、insecure-defaults、zeroize-audit
- 审计定位：68-cap 中唯一确认缺失项（2026-07-13 capability_inventory）

## 融合映射（来自 proposal 2026-07-16）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskCompleted
- 输出格式 → Observation / Pattern
