# AI-OS Line Registry（职责面注册 · 2026-08-24 收敛）

> 核心原则（D-018 修正）：**Work 是目的，Evolution 是手段；除了 Work，任何职责面都是为了 Work 而工作。**
> agent 只有两类：Work agent（使用 AI-OS）与 Evolution agent（让 AI-OS 持续服务 Work）。**line / 职责面 ≠ agent 类型。**
> 新发现的职责（如维护与体检、防止死亡）**默认归演化线内部**，只有 Human 明确判定需要独立处理时才另立。
> 架构语言（D-019）：对象以 Global / Callable / Searchable / Conditional / Assembled 之一或多种 Exposure Mode 进入 Agent 世界；Registry / INDEX / MAP / TOOL_RUNTIME 是 Exposure 的实现载体；**新增对象 ≠ 新线，只有 Purpose 改变才产生 Line Candidate。**

## 当前职责面

| 职责面 | Purpose | 内部职责 | 基础设施（均为演化线资产） | State |
|---|---|---|---|---|
| **Work** | 怎么把事情做好 | 使用 AI-OS 做真实工作 | workspaces/ + task_cards/ + domains/ + capabilities/ + task_start | operational |
| **Evolution** | 让 AI-OS 持续服务 Work | ① 成长：intake / fusion / reshape / consolidation ② 维护：体检（health-check）+ 修复（maintenance-skills/）③ 存在性保障：收尾登记 + 体检双向审计 + 接入收口 | evolution/（workspace / decisions / growth / intake）+ maintenance-skills/ + health-check + lines.md | operational |

> 维护与体检、防止死亡**不是独立线**——它们是演化线的基础设施：health-check（审计）、maintenance-skills/（修复 Skill 家）、登记纪律（存在性保障）。

## 新职责的处理流程（默认并回演化）

```text
真实摩擦 / 新需求
  ↓
发现新的职责模式
  ↓
默认：它是演化线内部的职责（成长 / 维护 / 存在性保障之一）
  ↓
只有 Human 明确判定需要独立 agent 职责面时才另立
```

## Candidates（苗头登记，不预建）

- **Observation / Evidence**（NC-001 族）：苗头，默认归演化线观察类基础设施候选
- **Retrieval**（检索质量）：已暴露需求，归 maintenance-skills 候选（retrieval-maintenance），不独立成线
- **Learning**：概念苗头

> 规则：任何新职责先作为演化线内部职责长；只有 Human 裁决独立才另立，不预先设计。
