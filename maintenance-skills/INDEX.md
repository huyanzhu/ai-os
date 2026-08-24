# maintenance-skills/INDEX.md — 维护能力发现入口（discovery surface）

> 2026-08-23 建立（D-015）。语义：让我知道"有什么维护能力"；**不是完整定义**——需要时打开 Skill 本体。
> 职责面：Maintenance（AI-OS 基础设施）；**不进普通 task_start**。

## 一、体检（观察入口 · 单列）

| 入口 | 职责 | 状态 |
|---|---|---|
| health-check | 只读扫描基础设施 → Finding / Severity / Infrastructure / Suggested Maintenance Skill / Evidence；不自动修，交 Human 裁决 | 已建立（首个体检待跑） |

## 二、维修（维护 Skill 注册表）

| Skill | 职责 | 触发 | 状态 | 裁决 |
|---|---|---|---|---|
| knowledge-space-maintenance | Knowledge Space + 记录生命周期维护（Consolidation + Integrity + Structure + Index/Discovery + Provenance + **Lifecycle/Archive**） | duplicate/overlap / malformed / incomplete frontmatter / stale-inconsistent index / orphaned / supersession / archive-prune / obsolete-rejection | 已建立（v3 · Lifecycle facet 2026-08-24 Intake #5） | D-013/D-014/D-016/D-022 |
