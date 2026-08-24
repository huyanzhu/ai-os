---
rule_id: EXP-AER-001
title: Update standards must verify old workflow completion conditions still exist
category: Architecture Evolution Risk
trigger:
  - Standard version upgrade
  - Workflow definition modification
  - Acceptance criteria added/removed
condition: Change directly modifies or replaces existing workflow acceptance criteria
action:
  do:
    - Get acceptance criteria lists before and after change
    - Compare each old condition for existence or explicit replacement
    - Execute Skill-005 Definition Preservation Check
    - If BROKEN: Block deployment, redesign required
    - If PARTIAL: Mark risk, deploy after human confirmation
  dont:
    - Directly replace acceptance criteria without tracing old conditions
    - Assume "new version is better" ignoring old version's intentional design
keywords:
  - experience
  - aer
  - contract
  - task
  - state

knowledge_position: Cluster
knowledge_cluster: FC-006 Definition Drift
epistemology_tag: PATTERN
confidence: HIGH
---

# EXP-AER-001 — Architecture Evolution Risk

## Problem

When task-helper instance was created, Main Instance only performed "registration"
(Identity file + Registry Entry) but lacked the intermediate steps from
registration to ready state.

Result: Registration complete != Instance ready. Session directory, WORKING_STATE.md,
and startup entry were not automatically generated.

## Root Cause

AIS-003 defined "what an instance is", AIS-004 defined "what happens after task
completion", but no standard defined "what steps are needed from registration to
readiness when creating a new Task instance".

This is a Definition Drift: the old workflow's implicit completion conditions
(instance directory exists, can be started) were not explicitly inherited by the
new standard.

## Lesson

When upgrading standards, verify that old workflow completion conditions still
exist or are explicitly replaced. Otherwise Definition Drift occurs: old conditions
disappear, new conditions don't cover them, behavior silently changes.

## Verification

Execute Skill-005 Level 3 Workflow Audit — Definition Preservation Check.

## Related

- AIS-003 v1.2 — Task Instance Initialization Standard
- AIS-006 v1.1 — Workflow Drift / Definition Preservation Check
- Skill-005 v1.1 — Level 3 Workflow Audit
- EXP-AER-002 — Concrete instance of this pattern
