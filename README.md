# AI-OS

**一个 Agent Operating Environment。**

Agent 在这里完成真实工作；工作产生的证据、缺口和需求进入 Evolution，让 AI-OS 自己成长。

AI-OS 面向 Agent 运行。它不是给 Agent 提供一堆能力，而是在 Agent 工作流的关键 **Hook** 上，让知识、工具和可装配能力按需进入决策空间——通过可验证的辅助能力，降低 Agent 的认知、执行、协作成本。

**Work 使用 AI-OS，Evolution 改变 AI-OS。**

## Work + Evolution

```text
Work      → 用 AI-OS 完成真实工作
Evolution → 用真实工作产生的证据、缺口和需求，改变 AI-OS 本身
```

```text
Work → Evidence / Gap / Want → Evolution → Growth → Maintenance → Work
```

## How AI-OS Works

Agent 的工作流里有一组可介入、可发现、可激活的 **Hook**（介入点）；能力、知识、工具通过 **Exposure** 挂载到 Hook 上。Work 在每个 Hook 上发现可用对象 → 采纳 / 不采纳 → 行动 → 下一个 Hook。

```text
Work
  ↓
Workflow Hooks
  ↓
Discover / Decide / Activate
  ↓
Knowledge · Capabilities · Tools
  ↓
Real Work
  ↓
Evidence / Gap / Want
  ↓
Evolution
  ↓
Recompose / Fuse / Extend / Accept / Split
  ↓
Exposure
  ↓
Work
```

## Exposure Modes

对象进入 Agent 工作流的方式（**不是对象类型**）：

```text
Global      → 默认存在（宪法 / 原则）
Callable    → 需要时调用（工具）
Searchable  → 任务驱动发现（知识）
Conditional → 条件满足时触发（工作模式）
Assembled   → 按需装载完整工作方式（整包能力）
```

## How AI-OS Evolves

Evolution 从真实工作的 Evidence / Gap / Want 中，重新理解、融合、重组、迁移或淘汰能力，并把新的形态重新暴露给 Work。Skill 不是静态集合——它可以通过**自融合、升级、完整收纳、拆分**等方式持续重组，并在工作中通过 Hook 自己出现：

```text
Evidence / Gap / Want
  ↓
Relationship Mapping
  ↓
Growth（接纳 / 融合 / 扩展 / 复用 / 归并 / 拆分 / 拒绝）
  ↓
Exposure Design
  ↓
Attach to Work Hooks
```

## Core Facilities

| 设施 | 作用 |
|---|---|
| Working Memory | 任务卡（task_cards），恢复任务上下文与跨阶段状态 |
| Retrieval | 在 Hook 上发现相关知识与能力（task_start / experience_push）；外部记忆为显式 opt-in（`AIOS_EXTERNAL_MEMORY`） |
| Capabilities | 保存可装配工作方式（capabilities/） |
| Knowledge | 领域知识库（domains/） |
| Tools | 执行具体操作（tools/） |
| Evolution Workspace | 处理 AI-OS 的成长（evolution/） |
| Maintenance | 保持基础设施健康（maintenance-skills/） |
| Evidence Ledger | 保存真实使用与验证状态（AI-OS_SUCCESS_LOG.md） |

## 试试

```text
git clone https://github.com/huyanzhu/ai-os.git
cd ai-os
# 给你的 Agent 一句话：
# "接入 AI-OS"
```

陌生 Agent 已验证这条路径可复现：接入 → 开工统一发现 → 装载能力 → 干活 → 收尾。

## 为什么

大多数 Agent 系统解决的是"让 Agent 有能力"；AI-OS 更关注"让 Agent 在工作流中正确遇到这些能力，并让这些能力随真实工作持续演化"。能力、知识、工作记忆和环境不会静止——它们从真实工作的证据中成长，而不是只堆文件。

## 验证

- ✅ Fresh Work Instance（隔离目录：接入 → 发现 → 真实任务 → 收尾）
- ✅ Fresh Evolution Instance（隔离目录：接入 → 体检 → 发现清单）
- ✅ Capability Exposure（条件触发装载：doc_standards / TDD 等）
- ✅ Skill Growth / Fusion（外部 Skill 整包物化、Facet 融合）
- ✅ Maintenance / Health Check（只读体检 + 维护 Skill）

> 诚实姿态：**integrated ≠ consumed ≠ valuable**。能力状态如实标注——多数单位 Q1–Q5 UNKNOWN，证据见承重账本。

## Project Status

已发布公开版本（Apache-2.0）。本体已冻结，等待真实用户 / 真实项目产生下一轮 Evidence；已知未验证项保持 UNKNOWN，不制造任务清零。

## Agent 接入（启动顺序）

1. 读 `ONBOARD.md`（身份 / 宪法 / 原则）
2. 读 `TOOL_RUNTIME.md`（工具：是什么、什么时候用）
3. 开工前跑 `python tools/task_start.py`（统一开工发现：任务卡 + 知识 + 能力）

## License

[Apache License 2.0](LICENSE)
