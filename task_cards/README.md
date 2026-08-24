# task_cards/ — Working Memory 第一形态（V2 · 2026-08-20）

> **这是什么**：Working Memory 能力在 V2 的**第一 realization**，直接复刻 v1 的 Task Card 实现（多卡目录 + active/archive），不是新设计。
> **为什么存在**：先让历史能力以 v1 已知可工作的形态回到 V2 生命系统，被真实 Agent 使用，再通过 3–6 观察重塑（第一形态 ≠ 终局）。
> **与 CURRENT_GOAL 的关系（2026-08-20 更新）**：CURRENT_GOAL.md **已删除**——task_cards 已被真实使用证明可替代（V2 自建任务全程以 task_cards 为工作记忆）；resume.py **已删除**（无锚态无用，入口职责由 ONBOARD/task_card 承接）。
> **实现原则（用户 2026-08-20）**：先通过 v1 的实现进行——本目录即 v1 实现原样（模板 + 手工建卡/归档，无新造工具）；观察后如需才补。
> **结构**：active/ 支持**项目文件夹**（如 `<项目>/`），项目文件夹内含 `PROJECT.md`（项目级工作记忆）+ 各 Phase 任务卡；平铺单卡仍可用。`list` 显示子目录名（目录名天然可关联）。项目文件夹在运行时按需创建。

---

## 结构

```text
task_cards/
├── README.md                 ← 本文件
├── _TASK_CARD_template.md    ← 第一版卡片模板（v1 原始模板原样）
├── active/                   ← 进行中卡片
│   ├── <项目>/               ← 项目文件夹（运行时创建）
│   │   ├── PROJECT.md        ← 项目级工作记忆（跨 Phase 复用更新）
│   │   └── TASK-YYYYMMDD-001.md
│   └── TASK-YYYYMMDD-001.md  ← 平铺单卡（任务级）
└── archive/                  ← 已关闭卡片
    └── TASK-YYYYMMDD-001.md
```

## 工作方式（v1 原样，第一形态）

```text
任务开始 → 复制模板到 active/，命名 TASK-YYYYMMDD-001.md，填 Header + Goal
任务进行 → 更新 Current Status / Next Action / Resume Point / Event Log
任务收口 → 填 Outcome / Knowledge Used / Close Checklist
任务关闭 → 仅当任务已完成且已获用户确认后归档（`archive TASK-ID --confirm`）；阶段/项目未完保持 active（2026-08-21 门槛）
项目级（2026-08-22 实验）→ 项目文件夹内建 `PROJECT.md` 记录项目状态（进度/技术债/下一步），Phase 间复用更新；跨 Phase 连续性由项目卡承载（不再只靠 README）
```

## 观察点（3–6，随真实使用记录，不预先设计）

- Agent 是否自然建卡/读卡/更新卡/归档？
- 在什么时机（开工/中途/卡住/收口）被使用？
- 什么字段被重复读取？什么字段没人看？
- 是否真的减少了"重新支付已支付成本"（对比 v1 的 CURRENT_GOAL 历史基线）？
- 是否与其他能力组合（experience_push / wrapup / SUCCESS_LOG）？
- **项目级 vs 任务级工作记忆**：Agent 是否自发建项目文件夹/项目卡？项目卡是否被后续 Phase 消费更新？

> 观察结果记录在任务卡 Event Log；任务后按收尾约定写回。

## 纪律

- 不预设计字段（模板保持 v1 原样，Freeze 直到真实使用暴露需求）；
- 不围绕本目录建系统（它不是中心，是 94 能力之一的观察样本）；
- CURRENT_GOAL 已删除（被替代）；resume.py 已删除（入口由 ONBOARD/task_card 承接）；
- **先不新造工具**：v1 使用方式 = 手工复制模板 + 移入/移出目录；保持原样观察。
