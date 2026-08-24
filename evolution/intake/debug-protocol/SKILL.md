---
name: debug-protocol
description: Diagnose bugs, failing tests, crashes, regressions, flaky behavior, and performance failures when the cause is unknown. Use for stack traces, wrong output, intermittent failures, environment mismatches, or repeated unsuccessful fixes. Do not use when the root cause is already established and the task is to implement the known fix; hand that work to tdd-loop.
---

# Debug Protocol

Turn each debugging step into evidence that confirms or rejects one explanation.

## Select the Mode

- **Diagnosis only:** Reproduce, identify the supported root cause, and report evidence. Do not modify production code or implement a fix.
- **Diagnose and fix:** Complete diagnosis first, then hand the confirmed behavior to `tdd-loop` for the regression test and implementation.

## Protocol

1. Reproduce with the smallest safe deterministic test, script, trace, or command. Do not experiment against production or private data without explicit authority.
2. Read the complete first error and capture exact inputs, outputs, versions, configuration, environment, timestamps, and correlation identifiers that matter.
3. Reduce flaky cases with repeated runs, a fixed seed, controlled clocks, resource limits, or an isolated environment. Consider races, timeouts, retries, partial failure, and environment parity.
4. State one falsifiable hypothesis: "X happens because Y."
5. Run the cheapest experiment that can disprove it. Change one variable and inspect actual values rather than inferred values.
6. Keep instrumentation temporary, scoped, and free of secrets. Remove it and confirm repository state before handoff.
7. For regressions, use binary search or `git bisect` only in a clean disposable worktree or after explicit approval. Record the starting state and always run `git bisect reset` before leaving it.
8. Trace the invalid state to its source. Distinguish the root cause from the location where the failure surfaced.
9. After three rejected hypotheses, stop editing, rebuild the system model from evidence, summarize attempts, and request missing human or environmental input when necessary.

## Evidence Report

Report the reproduction, supported cause, rejected hypotheses, affected scope, confidence, and the next safe boundary. Do not round a plausible theory into a confirmed diagnosis.
