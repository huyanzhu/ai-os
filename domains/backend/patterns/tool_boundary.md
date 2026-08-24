---
rule_id: tool_boundary
title: Tool 失败时优先判断是否超出工具能力边界
trigger:
  - tool 执行失败
  - tool failure
  - 工具返回意外结果
  - tool call 结果异常
  - PowerShell syntax error
  - unexpected command output
  - escalation approved but failed
  - approval granted but write denied
  - sandbox tracking lock
  - prefix rule reset
  - writer initialized but cannot write
condition: 错误信号已通过 environment_first.md Level 1 筛选 — 非权限关键词命中，或 escalate 后仍失败
action:
  do:
    # ──────────────────────────────────────────────
    # 通用 Tool Boundary 检查
    # ──────────────────────────────────────────────
    - 检查是否为 sandbox 限制（Desktop 写入、网络、GUI）
    - 检查是否为 GUI 自动化限制（窗口激活、坐标偏移、权限）
    - 检查是否为 provider 限制（stream truncation、token 上限、模型兼容性）
    - 检查是否为 shell 语法差异（PowerShell vs cmd、escape 规则）
    - 检查是否为 filesystem 限制（权限、路径长度、编码）

    # ──────────────────────────────────────────────
    # EFP-001: Escalation Failure 分类
    # Tool Boundary Analysis 必须区分 escalate 的两种失效模式：
    # ──────────────────────────────────────────────
    - 若 escalate 已执行但仍失败:
        → 执行 Escalation Failure Classification:
          1. escalate unavailabledisable
             - 特征: Agent 不可直接请求 escalate（如 Task 实例无此能力）
             - 根因: AIS-003 Capability 约束
             - 方案: fallback（先写可写目录再人工移动）

          2. escalate available but ineffective
             - 特征: escalate 已批准、权限已提升、操作仍被拒绝
             - 根因: Sandbox Tracking Lock / Prefix Rule 非持久化 / Component Gap
             - 方案: 见 escalation_workflow.md EFP-001 诊断流程

    - 检查结果记录:
        - escalate 路径是否可用
        - 若可用，是否生效
        - 不生效的根因（tracking lock / rule reset / component gap / env）
  dont:
    - 将 tool limitation 误判为 reasoning failure
    - 将 tool limitation 误判为 governance corruption
    - 将 tool limitation 误判为 architecture flaw
    - 在 escalate 前执行 Tool Boundary Analysis（应由 environment_first.md Level 1 路由）
    - 将 escalate available but ineffective 误判为 escalate unavailable
    - 将 escalate unavailable 与 escalate ineffective 混为一谈
keywords:
  - tool
  - boundary
  - escalation
  - analysis
  - level

knowledge_position: Cluster
knowledge_cluster: FC-002 Escalation
epistemology_tag: PATTERN
confidence: HIGH
related_rules:
  - environment_first.md (前置决策路由 — Level 2 分析入口)
  - escalation_workflow.md (Level 1 escalate 执行路径 + EFP-001 诊断)
  - WFI-004 (本规则 — Escalation Failure Pattern 分类)
---
alias:
  - 工具能力边界
  - 工具故障诊断



# Tool Capability Boundary
# 层级: Learned Rule (Tools)
# 版本: v1.2 (WFI-004 — Escalation Failure Pattern)
# 来源: 多个 session 中反复验证的 tool limitation 模式 / 2026-06-15 EFP-001 Audit

## 规则

优先判断当前问题是否超出工具能力边界。

## 触发时序

此规则在 WFI-005 三级决策模型中属于 **Level 2**：

```
Level 1 (Permission First) → 权限关键词? → 优先 escalate
                             非权限关键词? → Level 2

Level 2 (Tool Boundary) → 分析工具/环境边界
                          escalate 后仍失败 → EFP-001 分类

Level 3 (Systemic) → 环境/工具/escalate 正常仍失败 → 怀疑架构/定义
```

## Escalation Failure 分类

当 escalate 已执行但仍失败时，必须区分两种根本不同的模式：

| 类型 | 含义 | 根因示例 | 方案 |
|------|------|---------|------|
| **escalate unavailable** | Agent 无法直接请求 escalate | Task 实例无 escalate 能力 (AIS-003 Capability) | Fallback: 写入可写路径 + 人工移动 |
| **escalate available but ineffective** | escalate 已批准但操作仍被拒绝 | Sandbox Tracking Lock / Prefix Rule 非持久化 / Component Runtime Gap | 见 escalation_workflow.md EFP-001 |

**禁止将"escalate 可用但不生效"误判为"escalate 不可用"**——两者的 fallback 方案完全不同。

## 常见边界

- sandbox: 阻止 Desktop/system 写入、网络限制、GUI
- GUI automation: 窗口激活不稳定、坐标偏移、权限要求
- provider: stream truncation、token 限制、模型兼容性
- shell: PowerShell vs cmd 语法差异、escape 规则
- filesystem: 权限、路径长度、编码不一致（Shell 编码差异、BOM、UTF-8 vs GBK）

## 禁止

把 tool limitation 误判为：
- reasoning failure
- governance corruption
- architecture flaw

## 来源

- Desktop 无法写入 → sandbox limitation，非 governance 问题
- SendKeys 引号 escape 失败 → shell limitation，非 reasoning 错误
- pwsh 命令在 PowerShell 中行为不同 → shell mismatch
- Telemetry Writer 初始化成功但无法写入 → Component Runtime Permission Gap (EFP-001)
- prefix_rule 批准后仍未持久生效 → Rule Non-Persistence (EFP-001)
  - 工具
  - 边界
  - escalation
  - 分析
  - 能力

- workspace 文件 escalate 写入成功后同文件被追踪锁定 → Sandbox Tracking Lock (EFP-001)