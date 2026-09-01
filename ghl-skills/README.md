# GoHighLevel Agent Skills

Single-file agent skills for GoHighLevel, organised by department. Each department is
intended to ship as a unit — the agents assume the others exist.

## Format requirements

GoHighLevel imports one Markdown file per skill. A file must have:

- Exactly one YAML frontmatter block, first thing in the file, with `name` and `description`
- No byte-order mark before the opening `---`
- LF line endings
- Under 50 KB
- No references to sibling files, scripts, or directories — GHL has no filesystem and no
  runtime, so a skill must be wholly self-contained

`description` is the only thing an agent reads when deciding whether to invoke a skill, so
it carries the trigger vocabulary, not just a summary.

Validate before importing:

```sh
python3 ghl-skills/validate.py
```

`README.md`, `_TEMPLATE.md` and `PROVISIONING-SCHEMA.md` are documentation, not skills. The
validator skips them.

## Departments

### `governance/` — Governance & Board Ops

| Skill | Role |
|---|---|
| `company-context.md` | The spine. Provisioning form output lands here; every other agent reads it |
| `chief-of-staff.md` | Front door — scores decision complexity, routes, escalates |
| `board-meeting.md` | Multi-perspective deliberation with adversarial critique |
| `decision-logger.md` | Append-only decision record, conflict detection |
| `board-minutes.md` | Formal legal record — quorum, resolutions, recusals |
| `board-deck-builder.md` | Board pack structure, variance explanation, the asks slide |
| `corporate-filing-monitor.md` | State filing calendar and verification queue |
| `cfo-advisor.md` | Financial strategy; owns the board pack's financial section |

### `regulated-ops/` — Regulated Operations

| Skill | Role |
|---|---|
| `regulatory-affairs-head.md` | FDA 510(k)/De Novo/PMA, EU MDR, multi-market access |

Planned: quality manager (ISO 13485), risk management (ISO 14971), MDR specialist.

### `general/`

| Skill | Role |
|---|---|
| `internal-comms.md` | 3P updates, newsletters, FAQs, general internal comms |

## Provenance

Several skills are rewrites of material from a purchased third-party bundle
(SynthOperator "Ultimate Claude Skills Bundle v1"). **Confirm that bundle's licence terms
before distributing or reselling anything derived from it.** Internal use and resale are
different postures.

Skills written from scratch, with no third-party provenance:

- `board-minutes.md`
- `corporate-filing-monitor.md`
- `PROVISIONING-SCHEMA.md`

## Design constraints that shaped these

GHL skills are prompt-only: no API calls, no scripts, no file storage, no ability to
invoke another agent. Three consequences run through every file here.

**Nothing may be invented.** These agents run unattended after provisioning, so no human
reviews the first output. Every skill defaults to flagging a gap rather than filling it —
the filing monitor treats unverified as its default state; the regulatory skill marks fees
and review clocks for verification; the decision logger refuses to infer an owner. An agent
that sounds confident about a company it knows nothing about is the failure mode that
matters here.

**Orchestrators degrade.** `board-meeting` and `chief-of-staff` were originally designed to
dispatch to other agents with enforced isolation between them. GHL cannot do that. Both were
rewritten as single agents applying perspectives in sequence, with the loss stated inside the
skill. For real multi-agent isolation, run these under Claude Code agent teams instead
(`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`).

**The CRM is the persistence layer.** Where the originals read and wrote local files, these
work from what the user supplies in conversation or what is stored on the account record.
