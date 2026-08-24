---
rule_id: PROSE-STANDARD-001
title: 散文与注释编辑标准（保留完整命题 / 按位置覆盖 / 编辑判断）
category: Documentation Standards
trigger:
  - 写 / 评审 / 恢复 / 精简 / 审计散文与注释（Markdown、JSDoc、代码与测试注释、提示词、描述、诊断、CLI/UI 字符串）
  - 决定某处该不该有注释 / 某段该保留、删除、恢复还是重构
  - "trim the prose" / "this comment is unnecessary" / "restore this doc" / 审计可见文本
  - 编辑提示词、可见字符串、诊断文本（措辞即行为）
condition: 语料中的面向人/模型可见散文进入 AI-OS 或 workspace 项目时（编辑目标是保留契约，不是单向缩短；
  契约 = 调用方/被调用方/实现方/生产者/消费者依赖的义务、不变式、前置/后置条件或兼容性承诺）
action:
  do:
    - 要求显式 scope；缺失则报告所需输入并停止，不推断仓库级范围、不开始访谈；mode 默认 automatic，
      interactive 仅当用户显式要求提问/校准；mode 控制提问，不控制写权限（评审/审计只报不改，
      显式授权的写/修/精简任务才应用明确改动）
    - 扫描/评审/编辑排除 vendored/第三方依赖目录（排除放包含 glob 之后，避免重新纳入）与冻结归档快照
      （V2：task_cards/archive 等 archived 目录——只读，不现代化其散文与出链）
    - 编辑前识别段落里每个命题并保留相关成分：actor/action、条件/时序/顺序、模态（must/may/never）、
      负向保证与例外、所有权/副作用/失败模式/后果；只有每个事实子句都存活且结果更清晰时才删形容词/
      重复/叙述；字少本身不是改进
    - 使用点保留完整局部契约（行为/失败/所有权/后果）；架构/理由/算法/历史/扩展示例激进链接到拥有
      它的文档（一个解释只有一个家；本质契约事实可在局部重复）
    - 非显然理由（省略可能导致误用或错误简化）保留；否则陈述后果并链接理由的家
    - 按 12 类位置覆盖必需契约：公开 JSDoc（返回区别/throws/副作用/所有权/时序/取消/持久性）；内部
      注释（非局部结构与明显复杂的局部结构：不变式/竞态顺序/所有权/安全边界/意外失败行为，删控制流
      叙述与代码复述）；模块注释（角色/依赖/职责/非显然架构选择+链接）；测试（只解释非显然测试设计，
      删走读与清单）；cookbook（前置条件/必需动作/真实入口/可观察验证/简洁警告）；README（消费方契约：
      配置/语义/失败/局限/扩展点/模型可见效果，引用稳定模型可见文本，链接生成目录与跨包拥有者，保留
      持久缺口与维护者陷阱）；Agent Notes（V2：task card/pattern/SUCCESS_LOG 承重记录——保留独特理由/
      机制/备选/后果/已交付验证证据/指名覆盖缺口，implemented 现在时，删计划清单不删证据）；
      postmortem（事件序列/证据/因果链/影响/预防，删不建立因果的重复说服与实现细节）；skills 与 agent
      指令（行为护栏 + 显式范围限制如"guidance, not a script"，工作流简洁并链接唯一真相源）；示例与
      配置注释（访问限制/非显然接线或加载顺序/安全立场/重放行为/异常/可能误用，不复述配置已显示的）；
      提示词与可见字符串（措辞即行为——检查生成输出并跑行为验证，或说明为何无快照适用）；诊断（点名
      失败主体/路径、违反的规则、非显然时的纠正，删内部执行叙述）
    - 保留可搜索的机制名与有意义的模态/时序/负向强调；仅规范化装饰性强调
    - contract/boundary/shape/surface/seam/gate/vocabulary 是"用前检查"词不是禁用词：先问精确的
      规则/API/字段集/类型/校验/时序点/组件切分/失败状态是否把事实说得更好；词确实点名精确技术主体
      （调用方/被调用方契约、安全/进程边界）时保留
    - 工作流：①确认 scope/mode/当前分支或 PR base/适用 AGENTS.md（不检查无关分支）②先读 V2 文档
      标准（doc_standards/本 pattern）与拥有它的代码/文档再判断，陌生案例读边界案例沉淀 ③检查请求
      范围不只最大文件，用搜索与词数找候选再语义判断 ④候选分类 keep/add/trim/restore/restructure/
      defer，仅任务授权时应用明确改动，不为满足删除目标制造编辑 ⑤先改拥有者再改派生物，学到新规则
      后复查类似段落 ⑥跑最窄相关检查、文档门禁、git diff --check 与可见字符串行为测试；最终 diff
      确认无 vendored 路径，有意外匹配就报告而非声称干净 ⑦汇报检查范围/明确改动/刻意保留/延后案例/
      实际跑过的检查
    - 边界决策：仅当 ≥2 个版本都满足完整命题规则但权衡公认原则、且本 skill 未解决该权衡时才是
      borderline；automatic 应用明确编辑并如实报告，不为推进弱化命题；interactive 按主导原则分组、
      给 2-3 个可行版本并推荐一个、说明事实/结构差异、不给劣质干扰项，用户决定后把原则与版本提炼进
      examples（无评审叙述）并应用到范围内每个相似段落
  dont:
    - 无显式 scope 就推断仓库级范围或开始访谈；interactive 模式主动提问/校准
    - 编辑 vendored/第三方依赖目录或冻结归档快照
    - 编辑派生物而不先改拥有它的源/场景并重新生成
    - 删除会改变承诺行为（而非解释）的措辞；不为"字少"而删（小词数本身不是改进）
    - 复述代码已明示的内容；写控制流叙述/测试走读/评审历史/推理转录
    - 删除唯一归属处仍需链接的理由或架构解释（应在归属处保留并链接）
    - 弱化命题以推进任务；给劣质干扰项；汇报未跑过的检查
keywords:
  - 散文
  - prose
  - 注释标准
  - comment standard
  - JSDoc
  - 保留完整命题
  - proposition
  - 契约
  - contract
  - 编辑判断
  - prose standard
  - 按位置覆盖
  - required coverage
  - 精简散文
  - trim prose
  - 恢复散文
  - restore prose
  - 可见字符串
  - 提示词
  - 诊断文本
  - 推理转录
  - reasoning transcript
  - 语义审查
alias:
  - dsh-prose-standard
  - 散文编辑标准
  - 注释编辑标准
  - 契约保留

knowledge_position: Cluster
knowledge_cluster: FC-Prose Standard
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 散文与注释编辑标准（保留完整命题 / 按位置覆盖 / 编辑判断）

**来源**：外部 Skill（Human 提供，Evolution Intake #11 / DSH Corpus #8）——deepseek-ai/deepseek-harness
的 `dsh-prose-standard` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-prose-standard/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol / D-023
doc_site_projection / D-024 doc_standards / D-025 simplification_audit / D-026 dependent_change_landing /
D-027 pre_push_evidence_gate：外部 Skill → domains patterns 进 experience_push 检索源；D-008 Human
确认知识/pattern 形态）收编为 V2 pattern。

**解决**：写、评审、恢复、精简、审计语料中的散文与注释——**写到足以保留契约为止，然后移除推理转录、
重复与装饰**。契约 = 调用方/被调用方/实现方/生产者/消费者依赖的义务、不变式、前置/后置条件或兼容性
承诺。本 skill 拥有**编辑判断与必需散文覆盖**；放置/预算/双语配对/文档门禁归 `doc_standards`
（D-024），会话推理转录猎杀修复归 `cot_leakage_trim`（D-030）。

**可装配工作模式（Assembled / Conditional · D-037）**：本 pattern = 方法层知识（Searchable，
experience_push 检索源）。完整工作模式单位（剔除 repo 专属死引用后的整包，可装载激活）在
`capabilities/prose_standard.md`——命中 trigger（写/评审/恢复/精简/审计散文与注释、决定该不该有
注释、编辑提示词/可见字符串等）时装载该单位、执行完整流程；需要边界论证、不携带清单或与既有
知识互补关系时回读本 pattern（多关系：单位主体 + 知识引用 + 触发，D-034/D-037）。

## 什么时候用 / 不用
- **用**：写/评审/恢复/精简/审计 AI-OS 自身文档、代码与 workspace 项目中的散文与注释（Markdown、
  JSDoc、代码与测试注释、提示词、描述、诊断、CLI/UI 字符串）；决定某处该不该有注释、某段该保留/
  删除/恢复/重构；收到 "trim the prose"、"this comment is unnecessary"、"restore this doc"、
  "audit the prose" 类指令；审提示词、可见字符串、诊断文本（措辞即行为）。
- **不用**：文档放哪个层级、教程还是参考、写多长——那是 `doc_standards`；把文档发布成站点——那是
  `doc_site_projection`；收尾产出单份交付文档——那是 `doc-generation`；会话推理转录的猎杀与修复——
  那是 `cot_leakage_trim`（D-030）；代码功能本身的实现。

## 协议（AI-OS 上下文映射）
1. **输入与范围**——要求显式 `scope`；缺失则报告所需输入并停止，不推断仓库级范围、不开始访谈。
   `mode: automatic | interactive`，默认 automatic；interactive 仅当用户显式要求提问/校准。mode
   控制提问，不控制写权限：评审/审计任务只报不改；显式授权的写/修/精简任务才应用明确改动。
2. **排除与派生物**——扫描/评审/编辑排除 vendored/第三方依赖目录（排除规则放包含 glob 之后，避免
   重新纳入；只含 vendored 时报告无合格文件）；冻结归档快照（V2：task_cards/archive 等 archived
   目录）只读，仅为了解历史入站引用才看精确目标，不现代化其散文或出链。生成的目录/快照/夹具是
   派生物：先改拥有它的源/场景，再重新生成；生成器从拥有者散文提取摘要时，使摘要在该表面完整。
   双语配对无永久作者侧（V2 当前无配对基建——原则：任一语言都可作为作者侧，更新最小对应面并重录）。
3. **保留完整命题（编辑前先识别）**——编辑前识别段落里每个命题并保留相关成分：actor 与 action；
   条件、时序与顺序；模态（must/may/never）；负向保证与例外；所有权、副作用、失败模式与后果。
   只有每个事实子句都存活且结果更清晰时，才删形容词/重复/叙述；**字少本身不是改进**。
4. **局部契约与理由归属**——使用点保留完整局部契约（行为/失败/所有权/后果），调用方/维护者在那里
   就需要；架构/理由/算法/历史/扩展示例激进链接到拥有它的文档——一个解释只有一个家；本质契约事实
   可在局部重复。非显然理由（省略可能导致误用或错误简化）必须保留；否则陈述后果并链接理由的家。
5. **按位置覆盖（12 类）**——这不是单向压缩：代码、类型、结构无法传达必需契约时**加或恢复散文**；
   事实已局部显然时**不加注释**。
   - **公开 JSDoc/API 注释**：调用方可见的返回区别、throws/rejections、副作用、所有权、时序、取消、
     持久性。
   - **内部注释**：非局部结构与明显复杂的局部结构——不变式、竞态顺序、所有权、安全边界、意外失败
     行为；删除控制流叙述与代码复述。
   - **模块注释**：模块的角色、依赖、职责、非显然架构选择；架构选择链接到拥有解释处。
   - **测试**：只解释非显然测试设计——为什么这个 fixture/断言/平台适配/真实入口/间接观察是必要的；
     删除走读与清单。
   - **Cookbook/操作手册**：前置条件、必需动作、真实入口路径、可观察验证、简洁警告。
   - **README**：消费方契约——配置、语义、失败、局限、扩展点、模型可见效果；引用包拥有的稳定
     模型可见文本；链接生成目录与跨包拥有者；保留持久缺口与维护者陷阱，不保留普通清理清单。
   - **Agent Notes**（V2 对应：task card / pattern / SUCCESS_LOG 承重记录）：保留独特理由、机制、
     备选、后果、已交付验证证据、指名覆盖缺口；implemented 记录以现在时陈述已交付现实；删除计划
     清单，不删除钉住决策的证据。
   - **Postmortem/复盘**：保留事件序列、证据、因果链、影响、预防；删除不建立因果的重复说服与
     实现细节。
   - **Skills 与 agent 指令**：陈述行为护栏与显式范围限制（如"guidance, not a script/checklist"）；
     工作流保持简洁并链接其唯一真相源。
   - **示例与配置注释**：解释访问限制、非显然接线或加载顺序、安全立场、重放行为、异常、可能误用；
     不复述配置已显示的条目。
   - **提示词与可见字符串**：措辞即行为；检查生成输出并跑行为验证，或说明为何无快照适用。
   - **诊断**：点名失败主体/路径、违反的规则、非显然时的纠正；删除内部执行叙述。
   - 保留可搜索的机制名与有意义的模态/时序/负向强调；仅规范化装饰性强调。
6. **词检查（不是禁用词）**——contract/boundary/shape/surface/seam/gate/vocabulary 是用前检查的词：
   先问精确的规则、API、字段集、类型、校验、时序点、组件切分或失败状态是否把事实说得更好；词确实
   点名精确技术主体（调用方/被调用方契约、安全/进程边界）时保留。
7. **工作流**——① 确认 scope、mode、当前分支或 PR base、适用的 AGENTS.md 文件；不检查无关分支。
   ② 先读 V2 文档标准（doc_standards / 本 pattern）与拥有它的代码或文档，再判断；陌生案例读本
   pattern 的边界案例沉淀。③ 检查请求的范围，不只最大文件；用搜索与词数找候选，再语义判断。
   ④ 每个候选分类 keep/add/trim/restore/restructure/defer；仅当任务授权编辑时应用明确改动，
   不为满足删除目标制造编辑。⑤ 先改拥有者再改派生物；学到新规则后复查类似段落。⑥ 跑最窄相关
   检查、文档门禁（V2 既有验证入口）、`git diff --check`、可见字符串行为测试；最终 diff 确认无
   vendored 路径，有意外匹配就报告，不声称干净排除。⑦ 汇报检查范围、明确改动、刻意保留、延后案例
   与实际跑过的检查。
8. **边界决策**——只有至少两个版本都满足完整命题规则、但权衡公认原则且本 skill 未解决该权衡时，
   才是 borderline；一个命题保持答案的重写不是 borderline。automatic：授权时应用明确编辑，真实
   borderline 如实报告不提问；**不为推进而弱化命题**。interactive：相似段落按主导原则分组；给出
   2-3 个可行版本、推荐一个、说明事实或结构差异；不给劣质干扰项；用用户要求的通道（PR 内联校准把
   推荐暂定版放 diff、备选挂同一行）。用户决定后，把原则与版本提炼进 examples（无 PR 历史/评审
   叙述——V2 沉淀到本 pattern 的边界案例区），并把学到的规则应用到范围内每个相似段落。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `vendor/` 具体路径约定与 `.agents/notes/` 树（notes/README 契约、
archived 目录机制）、`docs/AGENTS.md` 标准之家与 lightweight routine path 链、package README
requirements 的仓库表单、`references/examples.md` 具体文件（V2 边界案例沉淀进本 pattern）、JSDoc
类型等价围栏、翻译 triplet（foo.md + foo.zh.md + foo.i18n.yaml）契约、dsh-doc-standards 与
dsh-trim-cot-leakage 子 skill 引用（分别独立收编：doc_standards → D-024；trim-cot-leakage →
D-030 → `cot_leakage_trim`）在 V2 无对应物；**原样整体不适合独立装配**。若未来真实项目本身就是
deepseek-harness 类仓库，直接装载原文 `evolution/intake/dsh-prose-standard/SKILL.md`（本 pattern
只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `doc_standards`（D-024）= 文档放置/层级/预算/语料审计——管"放哪、写成什么形态、多长"；本文 =
  散文编辑判断/契约保留/按位置覆盖——管"写什么、保留什么、删什么"。原文自述分工即如此：本 skill
  拥有编辑判断与必需散文覆盖，doc-standards 管放置、预算、双语配对、文档门禁——互补不重复。
- `doc_site_projection`（D-023）= 发布投影；`doc-generation` = 单份交付文档产出——不同工作面。
- `simplification_audit`（D-025）= 代码面简化审计（哪些既有面值得移除）；其 Proposal 触达文档/
  README/JSDoc 改动时，散文编辑判断由本文补充——互补。
- senior-engineer Review 方法层（D-011 融合 dsh-code-review）= 评审纪律（证据优先/阻塞闸门/深度
  检查/汇报），其"注释陈述非显然契约、标记实现叙述与评审历史"与本文"内部注释保留非显然契约、删除
  控制流叙述"同原则——评审纪律判定该标记什么，本文提供该写/该删什么的编辑标准；dsh-prose-standard
  在 code-review 融合时被列为不携带（独立 skill，不并入 review 方法层），本次作为独立 intake 收编。
- `knowledge-space-maintenance`（D-016/D-022）= domains 知识语料的维护（frontmatter/索引/去重/
  生命周期）；本文的 Agent Notes 覆盖规则适用于 task card/pattern/SUCCESS_LOG 承重记录，具体维护
  动作仍由维护 Skill 执行——互补。
- 同族 `cot_leakage_trim`（D-030，会话推理转录猎杀）已独立收编；本文保留"移除推理转录"目标，
  会话视角泄漏的分类、保留规则与过纠正陷阱由该 pattern 承载——本文提供一般编辑判断，该 pattern
  提供专项分类修复纪律。

## 检查清单（散文/注释编辑中自测）
- [ ] scope 显式了吗（缺失则报告所需输入并停止）？
- [ ] 编辑前识别了每个命题（actor/action、条件/时序、模态、负向保证、所有权/失败）？
- [ ] 删除只发生在每个事实子句都存活且更清晰时；没有为"字少"而删？
- [ ] 非显然契约在局部完整保留；架构/理由/历史链接到唯一归属（一个解释一个家）？
- [ ] 12 类位置覆盖检查过了吗（公开 JSDoc/内部注释/模块注释/测试/cookbook/README/Agent Notes/
      postmortem/skills 指令/示例与配置注释/提示词与可见字符串/诊断）？
- [ ] 没有复述代码已明示的内容；没有控制流叙述/测试走读/评审历史/推理转录？
- [ ] vendored 与冻结归档被排除；派生物先改源再重新生成？
- [ ] 只应用了任务授权的编辑；borderline 如实报告、未弱化命题？
- [ ] 汇报列了检查范围、明确改动、刻意保留、延后案例与实际跑过的检查？

## 相关对象（2026-08-24 Re-Mapping 物化 · D-035）

- cot_leakage_trim（本对象为其 REQUIRED BACKGROUND，双向）；doc_standards（双向）；bilingual_doc_pairing（作者侧编辑标准 → 配对同步输入，双向）；senior-engineer Review 面（评审输入，非成员）
- 工作模式单位：`capabilities/prose_standard.md`（Assembled；本 pattern 为 Reference）
