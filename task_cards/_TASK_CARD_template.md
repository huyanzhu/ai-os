# TASK_CARD

> Working Memory — disposable after task close. Not permanent knowledge.
> If information belongs elsewhere, store only the reference here.

---

## Header

```
Task ID:     TASK-YYYYMMDD-001
Type:        Course Project | Bug Fix | Architecture | Refactor | Research | Pattern Review | Maintenance | Experiment
Priority:    Critical | High | Medium | Low
Owner:       <role or instance>
Manager:     <coordinating instance>
Reviewer:    <review instance>
Created:     YYYY-MM-DD HH:mm
Last Updated: YYYY-MM-DD HH:mm
Updated By:  System | Worker | Manager | Review | Human
```

---

## Goal

One sentence. What is the single deliverable this task exists to produce?

---

## Current Status

```
State:         Created | Planning | Executing | Blocked | Waiting_Human | Reviewing | Completed | Archived
Resume Policy: auto | manual
Current Step:  What is happening right now?
Next Action:   What is the next concrete action?
Resume Point:  Where to pick up if interrupted?
Estimated Finish: YYYY-MM-DD / TBD
```

---

## Outcome

```
Unknown | Success | Partial | Abandoned | Cancelled
```

Brief summary of what happened, what was delivered, and any notable deviations.

---

## Confidence

```
High | Medium | Low
Reason: Why this confidence level?
```

---

## Open Questions

Questions that need answers before the task can progress. If Blocked, describe exactly what blocks progress.

---

## Blocked On

```
Human | Decision | External | API | Tool | Dependency
Reason: Why is this blocked?
```

---

## Decision Snapshot

Key decisions made during this task. Reference ADs by ID when applicable.

---

## Knowledge Used

```
Patterns:   PAT-xxx / PAT-xxx
Documents:  TOOL_RUNTIME / ARCHITECTURE_DECISIONS / ...
```

---

## Deliverables

```
Files Created / Modified:

Patterns Created:

Registry Updates:
```

---

## Event Log (max 20 entries)

| Time | State | Reason | Changed By |
|------|-------|--------|:----------:|
| HH:mm | Created | Task registered | System |

---

## Notes

Capture observations during the task. Review before close — anything worth a pattern?

---

## Close Checklist

- [ ] Deliverables completed
- [ ] Pattern extracted (if any)
- [ ] Telemetry written
- [ ] Task Card cleaned (open questions resolved, blocked cleared, temp notes removed)
- [ ] Task Card archived

---

> Rule: If information belongs elsewhere, store only the reference here.
> Task Card is Working Memory, not permanent knowledge.

---

## Constraints

**Size Budget:** Task Card is optimized for active work. Core information (Goal, Status, Next Action, Blocked, Confidence) should remain scannable in one screenful. Historical detail belongs in Telemetry or archived artifacts — not in the active Task Card.

**One Active:** Each Worker may have only one active Executing Task Card at a time unless explicitly coordinated by the Manager.

**Freeze:** No new fields before 20 real tasks. Changes allowed only if: a field is consistently unused, a missing field blocks work, or multi-instance collaboration exposes a structural gap.