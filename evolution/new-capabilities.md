# V2 第一代新能力（来自 Usage → Evolution，非 V1 复活）

> 这些不是 94 V1 Capability 的复活，而是真实项目使用中长出来的新能力。

---

## NC-001 Observation Extraction（会话日志 → 结构化观察）

**来源**：摩擦 #1（成本/时间/重工未记录）→ 调研外部 Skill（llm-cost-profiler 等）→ 决定性 UNKNOWN（instrumentation 测不到 agent 运行时内 token）→ **发现会话日志本身就有 token_count / 调用序列 / 推理 / 时间戳** → 泛化为"所有观察数据都能从会话日志提取"。

**是什么**：只读提取器——输入 session JSONL，输出结构化观察（能力使用 Trace / 成本 token / 时间 / 推理片段 Why）。

**为什么是 V2 第一代新能力**：

```text
V1 telemetry 死了：需要 agent 自己写事件（instrumentation 失败）
Observation Extraction：会话日志由载体自然产生，提取器只读、零额外步骤、零记忆依赖
```

**定位**：演化线辅助能力——把 Work Instance 的原始痕迹变成 Evolution 可消化的证据（双线循环的接缝）。

**最小 realization**：`D:\AI-os\tools\observe_extract.py`（输入 session JSONL → 输出 能力使用/token/时间/推理片段 摘要）。

**纪律**：只做提取器，不做成观察系统（不建仪表盘/不自动监控）。

**待验证**：跨 session 格式稳定性；Reasoning 片段提取质量；能否直接回填 Phase Review 的 Cost/Time。

---

*第一条；后续 Usage→Evolution 长出的新能力继续登记。*
