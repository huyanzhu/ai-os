---
rule_id: BROWSER-GIF-EVIDENCE-001
title: 浏览器 UI 演示录制证据纪律（真实树录制 / 状态帧捕获 / 编码验证 / 资产分支发布）
category: Evidence & Verification
trigger:
  - 录制 / 生成 / 制作展示浏览器工作流的 GIF（"record a gif" / "make a demo gif" / "record the browser flow"）
  - 演示 Web UI 交互 / 浏览器或 Web 应用工作流的截图序列 / 动图
  - 给"改变用户可见 GUI 行为的 pull request"附演示 GIF（PR 证据）
  - 审查 / 核验某个演示 GIF 证明的是什么（真实树 vs fixture、真实模型轮 vs 假数据）
  - "attach a GIF to the PR" / "show a demo in the PR body" / "prove the UI works"
condition: 需要一段**真实、可核对**的 UI 演示（录制本身是证据，不是装饰）：GIF 声称展示某个树的真实
  行为，读者需要知道它来自哪个 commit、什么运行条件、是否真的跑了模型/真实服务
action:
  do:
    - 先判定录制与发布分离：录制只产生帧图 + 本地 .gif 产物，不触碰远端状态；发布（推资产分支 + 嵌入
      PR body）是单独的最终步骤，只在任务包含"把 GIF 附到 PR"时执行，绝不直接提交到 PR 自身分支
    - 按 PR 分阶段（staging）：要求干净 worktree 并记录精确 commit（git rev-parse HEAD），从该树构建；
      一个端口一个 server，配全新 scratch 状态根（环境变量指向的 home/workspace/session）；给浏览器
      全新隔离上下文（无法创建时先清该 origin 的 cookie 与 site storage）
    - 一个 storyboard = 一次证据运行：所有发布的帧来自同一 server / 同一状态根 / 同一真实场景；捕获
      自动化失败 → 丢弃帧、从全新根重跑，绝不拼接两次运行（splicing）的帧
    - 录制只记录观察到的 setup 支持的声明：先确认 origin、构建态（built vs dev）、transport、
      fixture/mock 模式；生产默认会打开 headless 无法驱动的原生系统表面时，用应用正常配置选择官方
      浏览器可操作的生产后端并在 provenance 中陈述 override——fixture / mock transport / test-only
      hook 不是可接受的替代
    - 真实 server / 真实 API 演示绝不使用 fixture 查询、mock transport、合成事件注入或 test-only hook
      （用户显式要求 fixture 录制除外）；凭证不可用或 server 起不来 → 报告限制，不换 fixture 凑数；
      不读取、不暴露凭证值（用应用正常配置路径 + 良性演示 prompt）
    - 状态帧捕获：选 3–6 个讲清一个故事的语义状态（如 typed → running → settled → detail），偏好
      语义状态变化而非连续录制，省略不帮助观看者的加载抖动；全程同一 viewport 与 crop；帧按字典序命名
      （00-initial.png / 01-typed.png / …）
    - 帧存仓库 gitignored 目录下的帧子目录（先 mkdir，写进不存在的目录会 ENOENT）；截图前等具体 UI
      条件（唯一 label / 已启用控件 / document title 变化 / 响应完成），locator 必须恰好解析一个元素；
      Playwright accessible-name 用 exact: true；不用固定延时当状态到达的证据
    - 完成谓词匹配精确文本元素（trimmed text 全等预期回复），绝不用 body.textContent.includes 之类
      子串（prompt echo 也会满足子串）
    - 声明涉及工具调用/拒绝/恢复时，加 detail/trajectory 帧展示工具身份、状态或稳定错误码与下游结果
      （仅聊天结果证明不了工具路径行为）
    - 瞬态（spinner / running row）用慢前台操作驱动（如 sleep 15）+ 在同一个浏览器脚本调用内轮询具体
      DOM 标记并截图——跨工具调用轮询的状态会因回合 settle 丢失；设计 prompt 使所需状态真实发生
      （要模型前台等待慢命令 + settle 哨兵如 "reply with the single word done"）
    - 不捕获 secrets、个人数据、无关 tab、瞬态通知；展示状态可见后即停掉不必要长的真实 API 运行
    - 编码：帧时长按帧给（最终稳定态最长）；缺 ffmpeg/ffprobe/python 时报告依赖，不擅自安装软件；
      超 --max-bytes 先降 --max-width 再降 --colors/--fps；--force 只在精确确认输出路径后用
    - 验证产物：读编码器 JSON summary（输出路径/源与编码帧数/尺寸/时长/字节）；看编码后的 GIF 本身
      而非只看源帧（查看器只渲首帧时用 ffmpeg 解码代表帧检查顺序/palette/末帧停留）；git status
      确认帧与产物只落在 ignored 路径；返回绝对 GIF 路径并陈述 transport（real API / fixture / other）
    - 发布（仅任务包含"附到 PR"时）：GIF 只进专用 orphan assets 分支（名 <series>-assets；先
      git ls-remote --heads origin '*assets*' 列既有），绝不进 PR 分支或任何并入长命分支的分支；
      推送前验证资产分支只含 media + staged 校验和与本地已验证产物一致；既有分支走 shallow
      single-branch scratch clone，新系列走 fresh shallow clone + git switch --orphan；只 append
      commit，绝不删除/重写/force-push 资产分支（merged PR body 永久引用其 URL）
    - 发布验证：推送后经认证 GitHub API 或 raw 请求确认远端路径/字节/校验和/200/image/gif content
      type（匿名 404 不证伪私有仓库资产，认证验证）；编辑 PR body 前重读其 live head 并与 GIF 旁
      记录的 commit 对比，移动了 → 停并重录；编辑后重读 live head 必须仍在该 commit；用 GitHub
      Markdown API 渲染 body 确认预期 <img> 出现；嵌入用 raw blob URL（?raw=true 必需）
    - 汇报：GIF 旁陈述演示的确切 commit SHA、服务的 tree 与 origin、任何 mode flags / 浏览器状态
      例外、是否跑了真实模型轮——让 reviewer 知道录制到底证明了什么
  dont:
    - 不把录制与发布混在一起；不把 GIF 提交进 PR 分支或长命分支
    - 不用 fixture / mock transport / 合成事件 / test-only hook 顶替真实 server / 真实 API 录制
      （用户显式要求 fixture 录制除外）；不静默替换不可用条件，报告限制
    - 不读取/不回显凭证值；不捕获 secrets、个人数据、无关 tab、瞬态通知
    - 不对另一个 commit 的构建录 GIF（misattribute 证据）；不拼接不同运行的帧
    - 不用固定延时当状态到达证明；不用子串匹配当完成谓词（prompt echo 假阳性）
    - 不把跨工具调用轮询到的状态当同一时刻状态（回合 settle 之间状态已丢）
    - 不只验证源帧（编码后的顺序/palette/末帧停留必须看编码产物本身）
    - 不 force-push / 重写 / 删除资产分支；不在 PR head 移动后仍贴旧录制的 GIF
keywords:
  - 浏览器演示
  - browser gif
  - record gif
  - UI demo
  - 演示录制
  - 截图
  - screenshot
  - 帧捕获
  - frame capture
  - 证据链
  - evidence chain
  - 真实树录制
  - 状态帧
  - state-based capture
  - 完成谓词
  - completion predicate
  - 资产分支
  - assets branch
  - PR 证据
  - GUI PR
  - 演示 GIF
  - provenance
  - 录制来源
  - playwright
  - 浏览器自动化
alias:
  - record-browser-gif
  - browser gif evidence
  - 录制浏览器 GIF
  - 录制演示
  - 演示 GIF 证据
  - UI 演示录制

knowledge_position: Cluster
knowledge_cluster: FC-Evidence & Verification
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 浏览器 UI 演示录制证据纪律（真实树录制 / 状态帧捕获 / 编码验证 / 资产分支发布）

**来源**：外部 Skill（Human 提供，Evolution Intake #14 / DSH Corpus #11）——deepseek-ai/deepseek-harness
的 `record-browser-gif` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/record-browser-gif/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards / D-025 simplification_audit / D-026
dependent_change_landing / D-027 pre_push_evidence_gate / D-028 prose_standard / D-029
bilingual_doc_pairing / D-030 cot_leakage_trim：外部 Skill → domains patterns 进 experience_push
检索源；D-008 Human 确认知识/pattern 形态）收编为 V2 pattern。

**解决**：生产一段**短、真实、可核对**的 UI 演示 GIF——录制本身是证据：GIF 声称展示某个 pull
request 树的真实行为，读者必须能从 artifact + 旁边陈述的 provenance 精确知道它来自哪个 commit、
什么运行条件、是否真的跑了模型轮。**核心不变量：录制与发布分离；一个 storyboard 只来自一次隔离
运行；真实条件不得用 fixture 替代；发布的产物必须与验证过的本地 artifact 逐字节一致。**

## 方法层

### 1. 录制与发布分离
- 录制只产生帧图与一个本地 `.gif` 产物，**从不改动远端状态**。
- 发布（推 assets 分支 + 嵌入 PR body）是单独的最终步骤，**只在任务包含"把 GIF 附到 PR"时执行**；
  发布**绝不触碰 PR 自己的分支**。
- 保留要求的录制条件：真实 server / 真实 API 演示不得用 fixture 查询、mock transport、合成事件
  注入或 test-only hook。凭证或 server 不可用 → **报告限制**，不换 fixture 凑数。永不读取或暴露
  凭证值：走应用正常配置路径 + 良性演示 prompt。

### 2. 按 PR 分阶段（staging）
- 为特定 PR 录的 GIF 必须演示**该 PR 的树**：干净 worktree，`git rev-parse HEAD` 记录精确 commit，
  再从该树构建（deepseek-harness 是 `pnpm run build && pnpm run build:web`；V2/其他项目用该仓库
  自己的构建命令）。对另一 commit 的构建录制 = misattribute 证据。
- 一个端口一个 server，从该树启动，带全新 scratch 状态根（`DSH_HOME` 类环境变量 / workspace /
  session）；浏览器也用全新隔离上下文或 profile（无法创建 → 先清该 origin 的 cookie 与 site
  storage），持久化客户端状态不得影响证据。API key 走应用正常配置路径（root `.env`），永不回显。
- **一个 storyboard = 一次证据运行**：每个发布帧都来自该 server、该状态根、该真实场景。捕获自动化
  失败 → 丢弃帧、从全新根重跑；**绝不拼接两次运行的帧**。
- 切换 PR 时停旧 server：按 PID 或命令行精确匹配停（宽泛 `pkill -f` 模式可能杀掉启动它的 shell，
  包括自己）。

### 3. 录制流程
- 用可用的浏览器控制（V2 映射：仓库声明的 Playwright 依赖、隔离 headless；不使用用户浏览器除非
  明确要求——用了就如实陈述且不宣称 fresh client state）；浏览器控制不可用时用仓库声明的 Playwright
  依赖做隔离 headless，不另装 driver，不启动用户浏览器，并在 provenance 陈述 fallback。
- 录前确认：精确 origin、built vs dev、transport、fixture/mock 模式。**只记录观察到的 setup 支持
  的声明**。生产默认打开 headless 无法驱动的原生 OS 表面时，用应用正常配置选择官方浏览器可操作的
  生产后端，provenance 陈述 override——fixture/mock/test-only hook 不是可接受替代。
- 选 3–6 个讲清一个故事的语义状态（typed → running → settled → detail）。偏好语义状态变化，省略
  无帮助的加载抖动。
- 全程同一 viewport 与 crop；帧名字典序：`00-initial.png` / `01-typed.png` / …。
- 帧存仓库 gitignored 目录下（V2：`.playwright-mcp/` 或等价）的帧子目录：先 `mkdir -p
  .playwright-mcp/gif-frames-<label>`，写进不存在的目录在捕获时 ENOENT 失败。
- 截图前等**具体 UI 条件**：唯一 label、已启用控件、document title 变化、完成的响应。locator 必须
  恰好解析一个元素；Playwright accessible-name 用 `exact: true`（descendant 文本或 prompt echo
  会造成假匹配）。**不用固定延时当状态到达证明**。
- 完成谓词匹配**精确文本元素**（trimmed text 全等预期回复），不用 `body.textContent.includes(...)`
  子串——prompt 自己的 echo 也满足子串。
- 涉及工具调用/拒绝/恢复的声明：加 detail/trajectory 帧展示工具身份、状态或稳定错误码与下游结果
  （chat-only 结果证明不了工具路径为什么这样）。
- 瞬态（spinner / running row）：用慢前台操作驱动（如 `sleep 15`）+ **同一个浏览器脚本调用内**轮询
  具体 DOM 标记（`data-*`）并截图——跨工具调用轮询的状态会因回合 settle 丢失。设计 prompt 使所需
  状态真实发生：要模型前台等待慢命令，给 settle 哨兵（"reply with the single word done"）锚定完成
  谓词。
- 不捕获 secrets、个人数据、无关 tab、瞬态通知；所需状态可见后即停掉不必要长的真实 API 运行。
- 用浏览器自己的截图 API；返回字节时直接保存，编码器按图像内容检测（不依赖扩展名）。

### 4. 编码
- 依赖：`python3` + `ffmpeg` + `ffprobe`；缺任一媒体二进制 → **报告依赖**，未经授权不安装软件。
- 帧时长：一条时长适用所有帧，否则逐帧给逗号分隔的正数（最终稳定态最长）。编码器拒绝 <2 帧、尺寸
  或时长不匹配、非法限制、意外覆盖、意外时长、超 `--max-bytes` 的输出。
- 大产物先降 `--max-width`，再降 `--colors`/`--fps`；保留可读文本且最终态停留足够久。`--force` 只在
  精确确认输出路径后使用。

### 5. 验证产物
1. 读编码器 JSON summary：输出路径、源与编码帧数、尺寸、时长、字节数。
2. **看编码后的 GIF 本身**，不只源帧：转场可读、最后状态停留够久、无敏感内容。查看器只渲首帧 →
  用 ffmpeg 从编码产物解码代表帧检查（源截图证明不了编码顺序/palette/末帧停留）。
3. `git status --short` 确认帧与产物只落在 ignored 路径。
4. 返回绝对 GIF 路径，陈述 transport（real API / fixture / other）。任务不含"附到 PR"时到此为止。

### 6. 发布到资产分支（仅任务包含"附到 PR"时）
- **绝不把 GIF 提交到 PR 自己的分支或任何并入长命分支的分支**（二进制媒体会永久膨胀每个未来 clone
  的仓库历史）。GIF 只上专用 orphan assets 分支——无父 commit、只有 media；一个 assets 分支服务
  整个 PR 系列，命名 `<series>-assets`；先 `git ls-remote --heads origin '*assets*'` 列出既有分支。
- 任一路径推送前：验证 assets 分支只含 media + 暂存的 GIF 校验和与已验证的本地 artifact 一致。
- 既有资产分支：shallow single-branch scratch clone（`git clone --branch <assets-branch>
  --single-branch --depth 1 <repo-url> <scratch>`，V2：scratch 放 D 盘），cp GIF，add/commit/
  push——发布**碰不到工作树**。新系列：fresh shallow clone + `git switch --orphan <assets-branch>`
  再同样 add/commit/push。
- 推送后用认证 GitHub API 或 raw 请求确认远端路径、字节数、校验和、`200`、`image/gif` content
  type。**匿名 404 不证伪私有仓库资产**——认证验证（证明的是 repository-member review path，
  不是公开可访问性）。
- 编辑 PR body **前**重读 live head，与 GIF 旁记录的 commit 对比；移动了 → 停并重录。编辑后重读
  live head 必须仍在该 commit。用 GitHub Markdown API 渲染 body 确认预期 `<img>` 存在。
- 嵌入用 raw blob URL（`?raw=true` 必需；plain blob URL 渲染 GitHub 文件页而非图片）：
  `![<alt text>](https://github.com/<owner>/<repo>/blob/<assets-branch>/<name>.gif?raw=true)`
- **永不删除/重写资产分支、永不 force-push**（merged PR body 永久引用其 URL）——只 append 新 commit。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `pnpm run build && pnpm run build:web` 构建命令、`DSH_HOME` / `DSH_AGENTS_HOME`
环境变量与 root `.env` 具体配置路径、`browser-control` skill（V2 无此运行时——映射为仓库声明的
Playwright 依赖 + 隔离 headless）、`scripts/encode_gif.py` 具体脚本与 `GIF_SKILL_DIR` 导出约定
（V2 无此脚本；编码原则——逐帧时长/末帧最长/限宽优先/force 纪律——保留，具体实现用项目既有
ffmpeg/python 流程）、`../../notes/implemented/process/2026-08-08-browser-gif-evidence-chain.md`
（deepseek-harness 的决策注记——V2 的"why"由本 pattern + 决策记录承载）、`.playwright-mcp/` 具体
目录路径（V2 用等价 gitignored 目录）、`pkill -f` 具体停服命令（原则 = 精确匹配停服，避免宽泛
模式杀到自己）在 V2 无对应物；**原样整体不适合独立装配**（其为 deepseek-harness 仓库定制的
record-browser-gif 全套，依赖该仓库的 browser-control MCP、编码脚本与 evidence-chain 注记）。
若未来真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/record-browser-gif/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `verify-before-trust` = 验证原则（"永远给 Agent 可运行的检查——测试/构建/截图对比"）：本 pattern
  提供**产生截图/GIF 证据**的具体纪律（何时截、截什么、如何证明状态到达、如何验证编码产物）——互补。
- `closure_verify` = 端到端对账（扮演链路上下家 + 数据层不变式断言，验证正确性）；本 pattern =
  产出面向人的演示 artifact 并保持其真实性（证明的是"这个树在这个条件下确实表现出 X"）——互补不重复。
- `pre_push_evidence_gate`（D-027）= 推送前证据选择与核对（outgoing 范围确认/最小充分证据/远端
  核对）；本 pattern = GUI PR 证据的**生产侧**（录制演示 GIF 本身 + 资产分支发布纪律）——互补：
  一个管"推前该带什么证据、怎么核对"，一个管"演示证据怎么真实地做出来、怎么安全发布"。
- `git_safety_net`（backend）= 本地文件安全网纪律；本 pattern 的资产分支发布纪律（scratch clone、
  只 append 不 force）是其 PR 发布场景的延伸——互补。
- `cot_leakage_trim`（D-030）"录制的夹具与快照"排除项与本 pattern 的录制产物语义衔接：录制保留
  原声音（本 pattern 的 provenance 要求即"如实陈述录了什么条件"）——互补。

## 检查清单（录制浏览器演示 GIF 时自测）
- [ ] 录制与发布分离了吗（录制不碰远端；发布只在任务包含"附到 PR"时执行）？
- [ ] 按 PR 分阶段了吗（干净 worktree + 记录精确 commit + 从该树构建 + 全新状态根/浏览器隔离
      上下文）？
- [ ] 一个 storyboard 只来自一次隔离运行吗（失败丢弃重跑，绝不拼接两次运行的帧）？
- [ ] 真实条件未被替换吗（真实 server/API 不用 fixture/mock/合成事件/test hook；不可用 → 报告
      限制而非替换）？
- [ ] 帧是 3–6 个语义状态、单一 viewport/crop、字典序命名、落在 gitignored 目录吗？
- [ ] 每个状态等了具体 UI 条件（唯一 locator/exact:true/文档标题变化/响应完成），没用固定延时
      当证明吗？
- [ ] 完成谓词是精确文本匹配（非子串）吗（prompt echo 不造成假阳性）？
- [ ] 瞬态（spinner 等）用同一浏览器调用内轮询 + 截图捕获了吗（没有跨调用丢失状态）？
- [ ] 未捕获 secrets/个人数据/无关 tab/瞬态通知；未读取或暴露凭证值吗？
- [ ] 编码验证做了吗（JSON summary + 看编码后 GIF 本身 + 必要时 ffmpeg 解码代表帧 + git status
      确认只在 ignored 路径）？
- [ ] 发布只走专用 assets 分支吗（不碰 PR 分支/长命分支；scratch clone；校验和一致；只 append
      不 force-push）？
- [ ] 发布验证做了吗（认证 API/raw 确认 200/image/gif/校验和；PR body 编辑前后 live head 都在
      记录 commit；Markdown API 渲染确认 <img>）？
- [ ] 汇报包含 provenance 吗（commit SHA / tree 与 origin / mode flags 与浏览器状态例外 / 是否
      真实模型轮 / transport）？
