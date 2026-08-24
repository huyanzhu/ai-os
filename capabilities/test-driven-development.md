---
name: test-driven-development
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill test-driven-development（obra/superpowers）；原文见 evolution/intake/test-driven-development/SKILL.md
trigger:
  - 实现新功能 / 新特性（写实现代码之前）
  - 修 bug（先用测试复现）
  - 重构（任何可能破坏现有行为的改动）
  - 行为变更 / 改已有功能 / 加边界处理
  - 写代码前想跳过测试（"就这一次" / "先手动测过" / "回头再补"）——这是本工作模式的拦截信号
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本
  trigger → 读本文件全文 → 把"Test-Driven Development"完整流程装载为当前任务工作模式：
  RED（写失败测试）→ Verify RED（亲眼看到按预期理由失败）→ GREEN（最小实现）→ Verify
  GREEN（看到通过 + 无回归）→ REFACTOR（保持绿清理）；任何生产代码都必须先有失败测试
  （Iron Law）；按最后"检查清单"自测通过后才允许标记完成
status: Assembled + Delivered（外部 Skill 接入 · 可激活）；真实 TDD 消费 Q1–Q5 UNKNOWN
  （V2 自然实现任务尚未按本工作模式完整装载执行，显式不宣称已帮助）
decision_ref: D-043
knowledge_ref:
  - domains/ai-os/patterns/testing-tdd.md（既有 TDD 知识侧 · Searchable · RED-GREEN-
    REFACTOR 核心循环 / 适用边界 / 既有外部标杆映射）
  - evolution/intake/test-driven-development/SKILL.md（原文 · 未加工整包主体）
---

# 测试驱动开发 — 完整工作模式（Test-Driven Development · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（外部 Skill 整包接入，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 既有 TDD 知识侧（RED-GREEN-REFACTOR 核心循环 / 适用边界 / 既有外部标杆映射）保留在
> `domains/ai-os/patterns/testing-tdd.md`（Searchable · experience_push 检索源）——
> 本文件与它互为同一对象的不同承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：obra/superpowers `skills/test-driven-development/SKILL.md`。接入裁决：D-043。

---

name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code.
tools: ["Read", "Grep", "Glob", "Bash"]

【V2 注】tools 映射：Read/Grep/Glob/Bash = carrier 工具层文件 I/O 与搜索；
测试运行器以项目既有 runner 为准（V2 各工作区实际使用 `python -m unittest` /
`pytest` / `node:test` / vitest 等，命令按项目 README 与既有测试约定，见各 workspaces/ 项目）。

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask your human partner):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Red-Green-Refactor

```dot
digraph tdd_cycle {
    rankdir=LR;
    red [label="RED\nWrite failing test", shape=box, style=filled, fillcolor="#ffcccc"];
    verify_red [label="Verify fails\ncorrectly", shape=diamond];
    green [label="GREEN\nMinimal code", shape=box, style=filled, fillcolor="#ccffcc"];
    verify_green [label="Verify passes\nAll green", shape=diamond];
    refactor [label="REFACTOR\nClean up", shape=box, style=filled, fillcolor="#ccccff"];
    next [label="Next", shape=ellipse];

    red -> verify_red;
    verify_red -> green [label="yes"];
    verify_red -> red [label="wrong\nfailure"];
    green -> verify_green;
    verify_green -> refactor [label="yes"];
    verify_green -> green [label="no"];
    refactor -> verify_green [label="stay\ngreen"];
    verify_green -> next;
    next -> red;
}
```

### RED - Write Failing Test

Write one minimal test showing what should happen.

<Good>
```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```
Clear name, tests real behavior, one thing
</Good>

<Bad>
```typescript
test('retry works', async () => {
  const mock = jest.fn()
    .mockRejectedValueOnce(new Error())
    .mockRejectedValueOnce(new Error())
    .mockResolvedValueOnce('success');
  await retryOperation(mock);
  expect(mock).toHaveBeenCalledTimes(3);
});
```
Vague name, tests mock not code
</Bad>

**Requirements:**
- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

### Verify RED - Watch It Fail

**MANDATORY. Never skip.**

```bash
npm test path/to/test.test.ts
```

【V2 注】`npm test path/to/test.test.ts` 是示例命令；V2 用项目既有测试运行器的等价聚焦
执行（如 `python -m unittest tests.test_x` / `pytest tests/test_x.py`，以项目为准）。

Confirm:
- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

**Test passes?** You're testing existing behavior. Fix test.

**Test errors?** Fix error, re-run until it fails correctly.

### GREEN - Minimal Code

Write simplest code to pass the test.

<Good>
```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```
Just enough to pass
</Good>

<Bad>
```typescript
async function retryOperation<T>(
  fn: () => Promise<T>,
  options?: {
    maxRetries?: number;
    backoff?: 'linear' | 'exponential';
    onRetry?: (attempt: number) => void;
  }
): Promise<T> {
  // YAGNI
}
```
Over-engineered
</Bad>

Don't add features, refactor other code, or "improve" beyond the test.

### Verify GREEN - Watch It Pass

**MANDATORY.**

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix code, not test.

**Other tests fail?** Fix now.

### REFACTOR - Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers

Keep tests green. Don't add behavior.

### Repeat

Next failing test for next feature.

## Good Tests

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | One thing. "and" in name? Split it. | `test('validates email and domain and whitespace')` |
| **Clear** | Name describes behavior | `test('test1')` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |

When writing or changing any test, read [writing-good-tests.md](writing-good-tests.md) for the
rules that keep tests honest:
- Name the production change that would make the test fail — before writing it
- Assert on real behavior, never on mock behavior
- Keep test-only code in test utilities, out of production classes
- Understand a dependency's side effects before mocking it

【V2 注】`writing-good-tests.md` 是 superpowers 生态的配套文件，本 intake 只收录了
`SKILL.md`（唯一输入），该配套文件不在 V2 内——**不虚构其内容**；其四条原则的等价知识侧
见 `domains/ai-os/patterns/testing-tdd.md`（RED-GREEN-REFACTOR / 适用边界）与既有
`debug_protocol` pattern 的 Prove-It 规则（修 bug 先测复现）。若未来真实项目引入该配套
文件，按原文装载。

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests written after pass immediately — which proves nothing. They may test the wrong thing, test the implementation instead of the behavior, or miss the edge case you forgot. You never watched it fail, so you never proved it can catch the bug. Test-first forces that failure. |
| "Tests after achieve same goals (spirit not ritual)" | Tests-after answer "what does this do?"; tests-first answer "what should this do?" Tests written after are biased by the code you already wrote — you verify the cases you remembered, not the ones you'd have discovered. Coverage without proof the tests work. |
| "Already manually tested" | Manual testing is ad-hoc: no record of what you covered, no way to re-run it when the code changes, easy to forget cases under pressure. "Worked when I tried it" ≠ comprehensive. Automated tests run the same way every time. |
| "Deleting X hours is wasteful" | Sunk cost fallacy — that time is already spent either way. The real choice: rewrite with TDD (high confidence) vs. keep it and bolt tests on after (low confidence, likely bugs). Keeping code you can't trust is the waste. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD IS the pragmatic path: catches bugs before commit, prevents regressions, lets you refactor without fear. "Pragmatic" shortcuts mean debugging in production — slower, not faster. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for existing code. |

## Red Flags - STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "It's about spirit not ritual"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**

## Example: Bug Fix

**Bug:** Empty email accepted

**RED**
```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

**Verify RED**
```bash
$ npm test
FAIL: expected 'Email required', got undefined
```

**GREEN**
```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

**Verify GREEN**
```bash
$ npm test
PASS
```

**REFACTOR**
Extract validation for multiple fields if needed.

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typos)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write wished-for API. Write assertion first. Ask your human partner. |
| Test too complicated | Design too complicated. Simplify interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify design. |

## Debugging Integration

Bug found? Write failing test reproducing it. Follow TDD cycle. Test proves fix and prevents regression.

Never fix bugs without a test.

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without your human partner's permission.

## 检查清单（装载执行后自测）

- [ ] 写了失败测试并**亲眼看过它失败**（不是报错、不是通过），且失败原因 = 功能缺失而非笔误？
- [ ] 只在看到失败后写了最小实现（Iron Law：没有失败测试就没有生产代码）？
- [ ] 看到测试通过 + 其他测试仍通过 + 输出干净（无错误/警告）？
- [ ] 测试测真实行为、每测一件事、命名描述行为（"and" 在名字里就拆开）？
- [ ] 重构只发生在 GREEN 之后且保持全绿？
- [ ] 修 bug 先写复现测试（Prove-It），绝不无测试修 bug？
- [ ] 没有落入任何合理化（"太简单不用测" / "回头补" / "手动测过" / "保留参考" / "就这一次"）？
- [ ] 例外（一次性原型 / 生成代码 / 配置文件）已问 human partner，没有自行裁决？

---

## Reference（知识侧 · 多关系）

- **既有知识侧（Searchable）**：`domains/ai-os/patterns/testing-tdd.md` —— RED-GREEN-
  REFACTOR 核心循环、适用边界（配置/文档/静态内容不用）、既有外部标杆映射
  （addyosmani / mattpocock / superpowers 系）。需要知识检索命中或边界论证时回读本 pattern。
- **原文（Source preservation）**：`evolution/intake/test-driven-development/SKILL.md` ——
  未加工整包主体；未来真实项目需要原文逐字语义时直接装载。
- **互补关系**：`debug_protocol`（domains pattern）= 修复侧科学调试（复现 → 单假说 →
  证据报告），其 Prove-It 规则与本单位"修 bug 先写复现测试"同向；`testing-tdd` pattern =
  知识侧核心循环；本单位 = 完整可装载工作模式（Iron Law / Verify RED-GREEN / 合理化拦截 /
  Red Flags / 检查清单）。三者互补不重复。
