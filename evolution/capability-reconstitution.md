# Capability Reconstitution Skill（2026-08-22）

> **可复用的是过程，不是答案。** A16 做成 Task Card、A11 加"请采纳"都是某次重塑的结果；真正复用的是下面这条链。

---

## 过程

```text
你拿到一个 Capability
  ↓
① 先问 5 个问题
  ↓
② 找到最小 realization
  ↓
③ 把它放进真实 V2 Environment
  ↓
④ 让 Work Instance 正常工作（不为其改变任务）
  ↓
⑤ 看它为什么被用 / 不被用
  ↓
⑥ 找到真正阻碍（区分：环境不可达 / 未进决策空间 / 概念缺失 / 被承接 / 条件未触发）
  ↓
⑦ 只做最小 reshape
  ↓
⑧ 再进入真实工作
  ↓
⑨ 确认它是否真的变得可消费（且跨期 persistence）
```

## 形态判定（先判定，再找 realization）— 2026-08-23 修正

一个 Capability / Skill 有三种消费形态，先判定再选 realization：

```text
知识（Knowledge）   —— 被检索、被读、被采纳     → domains/ + experience_push
能力工具（Tool）     —— 被调用                  → tools/（因真实摩擦长出）
角色/整包（Assembled）—— 被装载进任务工作上下文   → capabilities/（保持完整）
```

- 外部 Skill **默认先保持完整**；只有真实证据证明需要拆成原子方法时才拆进 domains。
- **对象关系优先（2026-08-24 D-034，取代 D-033 的单选顺序）**：不把 Skill 压成单一落点；先建立 **Profile** 并识别关系：
  ├── 自身语义 / 工作面 / Facet
  ├── Domains / Knowledge
  ├── Existing Capability / Skill
  ├── 关联领域 / 关联职责面
  ├── Work Context / Exposure Candidates / Growth Relations
  再判断：哪些关系物化、哪些引用、哪些融合、哪些保持独立、哪些拒绝 → 决定 Exposure → 决定物理承载。
- **Physical placement is a realization decision, not the semantic identity of the object.**（domains/、capabilities/、maintenance-skills/、tools/ 都是承载方式，不是"它是什么"的答案。）
- 引用 D-004 先例 ≠ 默认拆知识；"方法型" ≠ 必然 Knowledge（可能是 Work-Mode / Conditional / Assembled 的候选，需关系判定）。
- Global / Callable / Searchable / Conditional / Assembled 是 Exposure/Activation 模式，不是 Capability 的类型。
- 角色整包类 → 注册 capabilities/INDEX.md；裁决引 decisions.md。

## 三维度与成长判定（2026-08-23 冻结 · D-009）

处理任何新对象时，三个维度正交、顺序固定：

```text
① Object Semantics   —— 这是什么？（Knowledge / Evidence / Capability / Skill / Facet / Tool / Memory）
② Growth             —— 它与已有对象怎么发展？（先判断关系）
③ Exposure           —— Agent 怎么得到/激活它？（后决定暴露）
```

- 成长操作：Reuse / Attach / Extend / Specialize / Consolidate / Merge / Promote / Migrate / Retire（Fusion 只是其中一种，不强行套用）。
- 默认局部；重复的独立需求才产生 Shared Candidate。
- 新 Skill 流程：保持完整 → 识别 Facet / Capability Surface → 与现有 Capability Space 比较 → 判定成长关系 → 记录到 `evolution/growth.md` → 再决定 Exposure。
- **接入收口（D-020 R5）**：对象进入 V2 时必须在既有载体（INDEX / MAP / TOOL_RUNTIME / README / 启动链之一）登记并验证一条有效 **Exposure Path**，结果写入 growth.md / decisions——**不新建注册表**；"接入完成" = 文件落位 + Exposure Path 有效（D-019）。

## ① 先问 5 个问题

```text
1. 这个 Capability 是什么？（本体，不引用历史命名）
2. 它怎么工作？（历史实现形态）
3. 用过哪些东西？（已知联系 / Primitive）
4. 它和谁有关？（Relation / 其他 Capability）
5. Agent 怎么可能自然遇到它？（最小 Environment / 触发条件）
```

## ⑥ 阻碍分类（决定 reshape 方向）

```text
环境不可达     → 修入口 / 必经路径
未进决策空间   → 把对象推进注意空间（如 A11 候选+摘要）
概念缺失       → 收尾/工作流加判断入口（如 A19 / Learning Closure）
被承接         → 记录承接者，不独立重建（如 D07→A22）
条件未触发     → 等自然场景，不制造（如 I02）
```

## 判定纪律

```text
✓ 只加判断入口，不强制产生内容（防"为填而填"）
✓ "无"也是有效输出（如 Learning Closure 判断"单次发生不沉淀"）
✓ 第一次成功 ≠ 真正进入 V2——需跨期 persistence
✓ 能力命运允许：独立 / 融合 / 承接 / Transform / Preserve / Superseded
```

## 证据纪律

```text
Trace（访问序列/工具调用/产物）= What
Reasoning（推理日志，按需读）= Why
Artifact（实际产出）= Result
三者交叉，推理不单独证明
```

---

*实践样本见 exemplars/；方法背景见 D:\AI_v2\reconstitution\05_METHODS。*
