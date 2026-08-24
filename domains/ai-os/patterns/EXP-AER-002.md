---
rule_id: EXP-AER-002
title: Task Runtime Consumption Failure — Contract/Plan created but not consumed by instance
category: Architecture Evolution Risk
trigger:
  - Task Contract exists in tasks/contracts/ but not read by instance
  - Execution Plan exists in tasks/plans/ but not read by instance
  - Task completed without executing Skill-003 wrap-up
condition: Contract/Plan generated but Runtime did not consume

action:
  do:
    - Task instance startup MUST auto-scan for Contract
    - Task instance startup MUST auto-scan for Plan
    - No Contract -> Forbidden to infer task goal autonomously
    - No Plan -> Request Main to generate
  dont:
    - Do not auto-infer task goal without Contract
    - Do not skip Plan loading
keywords:
  - experience
  - aer
  - context
  - loss
  - recovery

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# EXP-AER-002 — Task Runtime Consumption Failure

## Problem

Real task validation (task-helper-20260613) exposed:

1. Task Contract existed (TC-20260613-001-daily-helper.md) but Task instance
   did not auto-read it after startup
   → Task inferred task goals autonomously

2. Execution Plan not generated (Skill-004 not triggered)
   → Task tried 4 approaches before finding correct method

3. Skill-003 wrap-up not executed
   → TASK_INBOX empty, WORKING_STATE not updated, Main unaware of completion

## Root Cause

Workflow Definition Incomplete:
- AIS-003 defined instance identity, but not that Runtime must load Contract/Plan
- AIS-004 defined handoff, but not that completion should prompt wrap-up
- AGENTS.md existed but startup directory did not point to correct location

## Lesson

Task instance startup:
- MUST auto-scan for Contract (Owner = self)
- MUST auto-scan for Plan (Task ID matches Contract)
- No Contract → Forbidden to infer task goal autonomously
- No Plan → Request Main to generate

Task completion:
- MUST auto-prompt wrap-up
- MUST NOT auto-execute Skill-003 (requires user confirmation)

## Verification

Execute Skill-005 Level 4 Runtime Audit (Audit 4.1~4.5).

## Fix

- AIS-003 v1.3 — Runtime Initialization Standard (Contract_Loaded, Plan_Loaded)
- AIS-004 v1.1 — Completion Suggestion (prompt on completion)
- Skill-005 v1.2 — Level 4 Runtime Audit

## Related

- OBS-TR-001 (Contract not consumed)
- OBS-TR-002 (Plan not consumed)
- OBS-TR-003 (Skill-003 not triggered)
- OBS-TR-004 (Zombie Task detection missing)
- EXP-AER-001 — Architecture pattern behind this failure
