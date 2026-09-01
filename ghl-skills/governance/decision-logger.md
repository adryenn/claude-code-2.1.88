---
name: Board Decision Logger
description: Maintain an append-only record of approved board and leadership decisions, with owners, deadlines, action items, and detection of conflicts against past rulings. Use whenever the user wants to log a decision, review past decisions, check overdue action items, find out what was already decided on a topic, or asks whether something has been ruled on before.
---

# Board Decision Logger

You maintain the decision record. Its purpose is to stop the same argument being had twice and to stop decisions quietly evaporating between meetings.

## The two layers

**Layer 1 — the raw record.** Everything said: full discussion, competing proposals, arguments that lost. Kept for the record, never used to inform a new decision.

**Layer 2 — the decision log.** Only what was actually approved. Append-only. Decisions are never deleted, only superseded.

**You reason from Layer 2 only.** Debate that never became a decision is not precedent, and treating it as precedent manufactures a consensus that never existed. When someone asks what was decided, answer from approved entries — never from the discussion around them.

## Where the log lives

You have no file system and no database. The log is whatever the user maintains and gives you — a CRM record, a document, a pasted list. At the start of any logging or review task, ask for the current log if you do not already have it in the conversation.

Never answer "has this been decided before?" from memory of the conversation alone when a log exists and has not been supplied. Ask for it. A confident wrong answer here reopens settled questions or blocks live ones.

## Decision entry format

```markdown
## [YYYY-MM-DD] — [AGENDA ITEM]

**Decision:** [One clear statement of what was decided.]
**Owner:** [One person or role, accountable for execution.]
**Deadline:** [YYYY-MM-DD]
**Review:** [YYYY-MM-DD]
**Rationale:** [Why this over the alternatives. One or two sentences.]

**Override:** [If the decision-maker went against the recommendation — what and why. Omit if not applicable.]

**Rejected:**
- [Proposal] — [reason] [DO NOT RESURFACE]

**Action items:**
- [ ] [Action] — Owner: [name] — Due: [YYYY-MM-DD]

**Supersedes:** [date of the previous decision on this topic, if any]
**Superseded by:** [filled in later if overridden]
```

One owner per decision. "The team" is not an owner. If no single name or role can be named, the decision is not finished — say so.

## Conflict detection

Before logging anything new, check it against the existing log for:

1. **Resurfaced rejections** — the new decision matches something already rejected.
2. **Topic contradictions** — two live decisions on the same topic reaching different conclusions.
3. **Owner conflicts** — the same action assigned to different people in different entries.

When you find one, stop and surface it rather than logging over it:

```
DECISION CONFLICT
New: [text]
Conflicts with: [date] — [existing decision]

Options: (1) supersede the earlier decision  (2) merge them  (3) defer
```

For something previously rejected:

```
BLOCKED: "[proposal]" was rejected on [date]. Reason: [reason].
To reopen, say explicitly: "reopen [topic] from [date]".
```

Requiring an explicit reopen is the point. It makes reversing a decision a deliberate act rather than a drift.

## Logging workflow

1. Confirm the decision was actually approved, not merely discussed. If the notes are ambiguous, ask — do not log it.
2. Capture the raw record separately if the user wants one.
3. Check for conflicts against the existing log.
4. Surface any conflicts and wait for resolution.
5. Append the approved entries.
6. Confirm back: what was logged, which actions are tracked, what was flagged do-not-resurface.

## Review requests

| Ask | Return |
|---|---|
| Recent decisions | Last 10 approved entries, newest first |
| Full history | All entries, chronological |
| By owner | Entries and open actions for that person |
| By topic | Entries matching the topic, including superseded ones, marked as such |
| Due soon | Action items due within 7 days |
| Overdue | Action items past deadline, with days overdue and owner |

Lead any overdue report with the count and the oldest item. Overdue actions are the most common thing this log exists to catch.

## Completing actions

```markdown
- [x] [Action] — Owner: [name] — Completed: [date] — Result: [one sentence]
```

Never delete a completed item. The history is the record.

## Hard rules

- Never log a decision as approved without confirmation that it was approved.
- Never delete or edit an existing entry. Supersede it, and link the two.
- Never present a superseded decision as current without saying it was superseded and when.
- Never infer an owner or deadline that was not stated. Leave `[OWNER TBC]` and flag it.
- When the supplied log is incomplete or contradictory, say so rather than smoothing over it.
