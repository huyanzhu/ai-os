---
rule_id: architecture_review_container_redesign
title: AI-OS Architecture Review — Container Structure Redesign
trigger:
  - 目录结构重设计
  - Capability 不可导航
  - 按任务上下文组织知识
keywords:
  - architecture
  - container
  - 目录结构
  - domains
  - capability
  - review
---

# AI-OS Architecture Review — Container Structure Redesign

> 📌 GOVERNANCE
> - Status: Drift
> - Superseded By: —
> - SSOT: —
> - Owner: —
> - Note: 引用旧结构死路径 brain/patterns/ skills/operational/ docs/standards/

> **角色**: AI-OS Architecture Reviewer
> **日期**: 2026-07-14
> **范围**: 仅容器结构。不设计功能、不增加 Prompt、不讨论 Runtime。
> **输入**: Capability Inventory Audit (81 Capability, 64% Agent 未知)

---

## ① 根因分析

### 为什么 Skill-001, Skill-002, Skill-003 越来越多，Agent 越来越不知道如何使用？

**根因：AI-OS 按"文档类型"和"创建顺序"组织，而不是按"任务上下文"。**

当前组织逻辑：

```
skills/operational/Skill-000/  ← 按编号
skills/operational/Skill-001/  ← 按编号
docs/standards/AIS-001.md      ← 按编号
brain/patterns/success/        ← 按成功/失败
brain/patterns/failure/        ← 按成功/失败
registry/                      ← 按注册表类型
```

Agent 的导航逻辑是：

```
"我现在要做前端新功能开发。"
"我应该知道什么？"
```

当前结构无法回答这个问题。Agent 必须：
1. 知道所有 81 个 Capability 的存在
2. 知道每个 Capability 在哪个目录
3. 在当前任务中判断哪些 Capability 相关

这三个要求对 Agent 来说都不成立。而用编号命名（Skill-001, AIS-001）进一步恶化了问题——编号掩盖了 Capability 的用途，Agent 必须打开文件才知道内容。

**结论：不是 Agent 不努力。是目录结构本身不可导航。**

### 类比

```
当前 AI-OS = 图书馆按 ISBN 排书
           Agent 需要找到"前端开发"相关的书
           → 必须知道所有 ISBN → 不可能

目标 AI-OS = 图书馆按主题排书
           Agent 走到"前端"书架 → 找到所有相关书
           → 不需要知道任何编号
```

---

## ② 组织原则

### 当前原则（错误）

```
按文档类型:  skills/  standards/  patterns/  registry/
按创建顺序:  Skill-001  AIS-001  TAG-001
按作者/阶段: docs/history/  session/  _disabled/
```

### 目标原则

```
按任务上下文:  Agent 做 X 类型任务 → 去 X 目录 → 找到所有相关内容
按域:         前端/后端/产品/AI-OS — 每个域独立的知识空间
按生命周期:    TaskStarted → 需要什么 / TaskCompleted → 需要什么
```

### 命名原则

- 不编号。名字描述用途。
- 不用前缀区分类型（AIS-, TAG-, Skill-）。目录位置区分类型。
- 文件名 = 问题答案。Agent 看到文件名就知道内容。

---

## ③ 目录结构

```
AI-OS/
│
├── ONBOARD.md              ← 入口（不变）
├── AGENTS.md               ← Agent 宪法（不变）
├── CURRENT_PHASE.md        ← 当前阶段（不变）
│
├── identity/               ← 我是谁
│   ├── instance.md
│   └── INSTANCE_REGISTRY.md
│
├── lifecycle/              ← 什么时候发生什么
│   ├── events.md           ← TaskCreated/Started/Completed/Closed
│   └── hooks.md            ← 每个事件触发什么 Hook
│
├── workflows/              ← 怎么做（按任务类型）
│   ├── new-feature.md
│   ├── bug-fix.md
│   ├── refactor.md
│   ├── design.md
│   └── research.md
│
├── capabilities/           ← AI-OS 能做什么
│   ├── task-card.md        ← 任务追踪
│   ├── review.md           ← 五问 Review
│   ├── knowledge-capture.md← 经验沉淀
│   ├── pattern-injection.md← 经验注入
│   ├── context-assembly.md ← Bootstrap 装配
│   └── CAPABILITY_INDEX.md  ← 全部 Capability 索引
│
├── domains/                ← 知识（按域组织）
│   ├── frontend/
│   │   ├── patterns/       ← 可复用工程经验
│   │   ├── guidelines/     ← UX/UI 原则
│   │   └── experiences/    ← 一次性经验记录
│   ├── backend/
│   │   ├── patterns/
│   │   ├── guidelines/
│   │   └── experiences/
│   ├── product/
│   │   ├── patterns/
│   │   ├── guidelines/
│   │   └── experiences/
│   └── ai-os/
│       ├── patterns/       ← AI-OS 自身的工程经验
│       ├── guidelines/     ← AI-OS 设计原则
│       └── experiences/    ← Sprint 中暴露的问题
│
├── governance/             ← 规则和标准
│   ├── constitution.md     ← 不可变原则
│   ├── runtime-boundary.md ← 三方边界
│   ├── change-management.md← 变更治理
│   └── decisions.md        ← 架构决策记录
│
├── templates/              ← 模板（不变）
│   ├── task-card.md
│   ├── review.md
│   └── knowledge.md
│
├── runtime/                ← 运行时工具（不变）
│   └── io_runtime.ps1
│
├── env/                    ← 环境配置（不变）
│
├── proposals/              ← 提案（不变）
│
└── archive/                ← 历史归档
    ├── session/
    ├── experiments/
    └── docs/
```

---

## ④ Bootstrap Assembly 引用关系

```
Task Type (new_feature)
    │
    ▼
Lifecycle Stage (TaskStarted)
    │
    ▼
Bootstrap 查询
    │
    ├── workflows/new-feature.md        ← 这个任务怎么做
    ├── capabilities/task-card.md       ← 需要创建 Task Card
    ├── capabilities/context-assembly.md← 需要装配上下文
    ├── domains/{domain}/patterns/      ← 该域的可复用经验
    ├── domains/{domain}/guidelines/    ← 该域的设计原则
    └── domains/{domain}/experiences/   ← 该域的历史教训
    │
    ▼
Assemble → Agent 收到准备好的上下文
```

### 按任务类型的装配策略

| 任务类型 | 装配 |
|---------|------|
| new_feature | workflow + task-card + context-assembly + domain/patterns + domain/guidelines |
| bug_fix | workflow + domain/patterns + domain/experiences |
| refactor | workflow + domain/patterns + governance/decisions |
| design | workflow + domain/guidelines + domain/experiences |
| research | workflow + governance/decisions |

### 按域过滤

Assembly 第二步：域过滤。同是 `new_feature`，前端和后端需要的知识完全不同。

```
new_feature + frontend → domains/frontend/patterns/ + domains/frontend/guidelines/
new_feature + backend  → domains/backend/patterns/  + domains/backend/guidelines/
new_feature + product  → domains/product/guidelines/ + domains/product/experiences/
```

---

## ⑤ 迁移计划

### 需要迁移的

> ⚠️ BROKEN LINK (unresolved): 以下"当前路径"源均已不存在 —— `brain/`（目录已移除）、`skills/operational/`（已迁入 `archive/skills/operational/`）、`docs/standards/`（已不存在）。表格列出的是待迁移的旧结构，非可解析链接。

| 当前路径 | 目标路径 | 原因 |
|---------|---------|------|
| `brain/patterns/success/*.md` | `domains/{domain}/patterns/` | 按域重新分类 |
| `brain/patterns/failure/*.md` | `domains/{domain}/patterns/` | 成功/失败不应是顶层分类 |
| `brain/knowledge/*.md` | `domains/ai-os/experiences/` | Knowledge 是 AI-OS 自身的经验 |
| `skills/operational/Skill-000~010/` | `capabilities/` | 去掉编号，按用途命名 |
| `docs/standards/AIS-*.md` | `governance/` 或 `capabilities/` | 标准是治理文档或能力定义 |
| `registry/` (部分) | `capabilities/CAPABILITY_INDEX.md` + `identity/INSTANCE_REGISTRY.md` | 按职责拆分 |
| `projects/PLATFORM_USER_JOURNEY.md` | `domains/product/guidelines/` | 产品域的设计原则 |
| `projects/PLATFORM_VISION.md` | `domains/product/guidelines/` | 同上 |
| `proposals/` | 保留位置 | 不变 |
| `templates/` | 保留位置 | 不变 |

### 需要保留的

| 文件 | 原因 |
|------|------|
| `ONBOARD.md` | 根目录入口，Agent 唯一需要知道的位置 |
| `AGENTS.md` | Agent 宪法 |
| `CURRENT_PHASE.md` | 当前阶段状态 |
| `identity/INSTANCE_IDENTITY.md` | 实例身份 |
| `env/*.md` | 环境配置 |
| `runtime/*.ps1` | 运行时工具 |

### 需要废弃的

| 文件/目录 | 原因 |
|-----------|------|
| `docs/standards/AIS-001, AIS-002` | 内容已合并到 lifecycle/ 和 governance/ |
| `skills/operational/Skill-*` 编号目录 | 迁移到 capabilities/ 后删除 |
| `brain/patterns/success/` + `brain/patterns/failure/` 目录 | 改为 domains/{domain}/patterns/ |
| `brain/knowledge/` 目录 | 改为 domains/ai-os/experiences/ |
| `session/` 目录 | 移至 archive/session/ |
| `docs/history/` `docs/plans/` `docs/automation/` | 移至 archive/ |
| `registry/` (部分文件) | 拆分后删除 |
| `_disabled/` | 移至 archive/ |

### 需要合并的

| 合并 | 结果 |
|------|------|
| `AGENTS.md` + `lifecycle/events.md` + `lifecycle/hooks.md` | 生命周期定义统一在 lifecycle/ 下 |
| `skills/` 下的所有 SKILL.md | 统一为 capabilities/ 下的独立文件 |
| 分散在 docs/ registry/ brain/ 的治理文档 | 统一到 governance/ |
| 39 个 patterns 按 domain 重新分类 | 每个 domain 一个 patterns/ 目录 |

---

## ⑥ 风险分析

| 风险 | 严重度 | 缓解 |
|------|:--:|------|
| 迁移过程中丢失文件引用 | 高 | 保留原始目录 30 天，确认无 Broken Link 后删除 |
| Pattern 按域分类后 Agent 仍不会搜索 | 中 | 这是 Bootstrap 的问题，不是目录结构的问题。新结构会降低搜索成本，但不解决"Agent 不搜索"的问题 |
| 迁移后 AGENTS.md 引用路径失效 | 中 | 迁移同步更新 AGENTS.md 中所有路径引用 |
| Git 历史丢失 | 低 | Git 保留所有历史，迁移只是 mv 操作 |
| 迁移太激进导致 Human 找不到文件 | 中 | 根目录保留入口文件 (ONBOARD/AGENTS/CURRENT_PHASE)，其余按新结构 |

---

## ⑦ 核心收益

**迁移前**：Agent 面对 81 个 Capability，需要知道每个在哪个目录、哪个编号、什么用途。

**迁移后**：Agent 走到 `workflows/new-feature.md` → 自动指向 `capabilities/` + `domains/frontend/`。不需要知道任何编号。

**一句话**：从"Agent 必须知道所有 Capability"变成"Bootstrap 根据任务类型和域，自动指向正确的目录"。

---

## ⑧ 补充（GPT Review）

### 补充 1：Workflow 不是 Capability 的平级

Capability 是 Workflow 在执行过程中调用的积木。关系是：

```
Workflow ──uses──→ Capability
```

不是：

```
Workflow
Capability    ← 两个并列
```

**修正**：`capabilities/` 是 Workflow 的"工具箱"。Agent 不直接接触 Capability 目录——Agent 只接触 Workflow。Workflow 内部引用 Capability。

### 补充 2：Bootstrap 增加 Resolver 层

当前：

```
Task Type → Domain → Lifecycle Stage → Assembly
```

以后 Domain 会细分（frontend 下有 Landing、Dashboard、Settings...），需要 Resolver 根据上下文路由。

```
Task Type (new_feature)
    ↓
Domain (frontend)
    ↓
Sub-domain (Landing)
    ↓
Lifecycle Stage (TaskStarted)
    ↓
Resolver          ← 新增
    │
    ├── Workflow  (new-feature)
    ├── Capability (task-card, review, pattern-injection)
    ├── Guideline  (domains/product/guidelines/)
    ├── Pattern    (domains/frontend/patterns/)
    └── Experience (domains/frontend/experiences/)
    │
    ▼
Assembly → Agent
```

Resolver 的职责：根据当前上下文决定装什么。以后 Runtime 直接替换 Resolver，整个 Bootstrap 不用动。

### 补充 3：核心原则

> **Agent 永远不应该知道系统里有哪些 Capability。**
>
> Agent 只应该知道：**Bootstrap 给了我什么。**

Capability Inventory 是给 AI-OS 维护者看的。Assembly 才是给 Agent 看的。

这是 **Assembly > Inventory** 原则。

### 补充 4：Domain 永远不能调用 Domain

`domains/frontend/` 里不要写"去看 product/xxx"。Bootstrap 负责跨域装配。Domain 只负责存。

```
Bootstrap: 装 frontend + product + ai-os
Agent:     只看 Assembly（已经是三个域拼好的结果）
```
