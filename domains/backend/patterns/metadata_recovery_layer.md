---
rule_id: metadata_recovery_layer
title: Pattern metadata survives encoding corruption — keywords, rule_id, and related_rules preserve navigability even when body text is lost
trigger:
  - pattern file contains unreadable Chinese text
  - encoding corruption detected in pattern files
  - mojibake in bootstrap pattern read
  - garbled text in knowledge artifacts
  - Select-String matches garbled bytes
condition: Encoding corruption in pattern files (GBK stored as UTF-8, BOM contamination, or double-encoding)
action:
  do:
    - When reading a pattern file that has corrupted body text, extract usable information from metadata fields: keywords, rule_id, trigger, related_rules, aliases
    - Use related_rules to find clean copies of linked patterns — routing through corrupt artifacts is still possible
    - Inject "Pattern Alert" using only the English/ASCII fragments that survived
    - Do not discard the pattern just because the body is unreadable — the metadata alone may be sufficient for decision routing
    - Record the pollution in telemetry so false positive rates can be traced
  dont:
    - Do not treat garbled patterns as empty — metadata may still be valid
    - Do not use garbled Chinese text for semantic reasoning — only English/ASCII metadata
    - Do not re-encode or attempt to repair the file in-flight during task execution
keywords:
  - garbled
  - mojibake
  - encoding
  - corruption
  - recovery
  - metadata
  - disaster
  - navigation
  - routing
  - false positive
  - precision
  - retrieval
  - sanitization
  - pollution
  - injection
epistemology_tag: PATTERN
confidence: HIGH
related_rules:
  - environment_first.md (the garbled artifact this was proven against)
  - escalation_workflow.md (also garbled, metadata survived)
  - protected_artifact_write.md (prevention, not recovery)
  - write_java_no_bom.md (BOM-specific recovery)
---

# Metadata as Machine-Recoverable Layer

## Observation

On 2026-06-30, two success patterns (environment_first.md, escalation_workflow.md)
were read during Bootstrap Step 7A with garbled Chinese body text. The encoding
corruption destroyed Chinese semantics but left English metadata intact.

Despite the corruption, the Agent:
1. Correctly identified the patterns as relevant (keyword match on clean English keywords)
2. Extracted the 3-level decision model from cross-referencing related_rules
3. Made correct escalation decisions using only the English metadata fragments

Pollution path:
`
Garbled file -> Context -> Pattern Search (false positives) -> Pattern Injection (sanitized) -> Decision (clean)
`

## Root Cause

Encoding corruption (GBK bytes interpreted as UTF-8, or vice versa) can destroy
Chinese body text while preserving ASCII metadata. This creates a situation where
the file is partially usable but looks completely broken.

## Lesson

Pattern metadata (keywords, rule_id, trigger, related_rules, aliases) functions as
a **machine-recoverable layer** — a second path to the same knowledge. When body
text is lost, the metadata routing chain can still guide the Agent to the correct
decision.

## Pattern Injection as Sanitization Layer

Bootstrap Step 7A "Pattern Alert" injection serves a dual purpose:
1. Deliver pattern content to the Agent
2. Filter corrupt/unusable knowledge before it reaches Decision

This was not originally designed — it emerged from the architecture.

## Verification

- Check: can all patterns be navigated using only metadata fields?
- Check: are related_rules chains reciprocal?
- Telemetry: add False Positive counter to the funnel
  (Matched -> False Positive -> Injected -> Referenced -> Validated)
