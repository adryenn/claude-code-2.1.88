# Company Provisioning Schema

The form that spins up a new company's agent suite. Every field here exists because at least one agent degrades without it. Fields no agent consumes have been left out deliberately — an onboarding form that asks for things nothing uses is where completion rates go to die.

## Design rule

One source of truth. The form writes company custom fields on the new sub-account; the **Company Context** agent reads them; every other agent reads Company Context. No agent gets its own private copy of the company profile, because two copies means two answers to the same question.

---

## Section 1 — Identity  *(required)*

| Field | Type | Consumed by | Notes |
|---|---|---|---|
| `legal_name` | text | Corporate Secretary, Filing Monitor, Board Minutes | Exactly as registered |
| `trading_name` | text | All outbound agents | Falls back to legal_name |
| `what_we_do` | textarea | Every agent | One or two sentences. The single highest-leverage field on the form |
| `industry` | select | CFO, CMO, Regulatory | Drives which benchmarks apply |
| `website` | url | Marketing agents | |

## Section 2 — Legal entity  *(required for the Governance department)*

| Field | Type | Consumed by |
|---|---|---|
| `entity_type` | select — LLC, C-corp, S-corp, LP, LLP, nonprofit | Corporate Secretary, Filing Monitor, CFO |
| `home_state` | select | Filing Monitor |
| `formation_date` | date | Filing Monitor — drives anniversary-month deadlines |
| `state_file_number` | text | Filing Monitor |
| `foreign_qualifications` | multi-select of states | Filing Monitor |
| `registered_agent_name` | text | Filing Monitor |
| `registered_agent_expiry` | date | Filing Monitor — lapse is a silent failure mode |
| `fiscal_year_end` | select | CFO, Filing Monitor |

Without `formation_date` and `home_state`, the Filing Monitor can compute nothing and everything lands in its verification queue. Make these hard-required.

## Section 3 — Stage and scale  *(required)*

| Field | Type | Consumed by |
|---|---|---|
| `stage` | select — pre-PMF, scaling, optimizing | Every advisor. Changes what "good" means |
| `team_size` | select — 1–10, 10–50, 50–200, 200+ | CHRO, COO, CFO |
| `business_model` | select — SaaS, services, marketplace, hardware, hybrid | CFO — decides whether SaaS benchmarks apply at all |
| `funding_status` | select — bootstrapped, pre-seed, seed, Series A, Series B+ | CFO, CEO |

`business_model` matters more than it looks. The CFO agent's default targets are venture SaaS benchmarks; applied to a services business they are actively misleading.

## Section 4 — Leadership  *(required)*

| Field | Type | Consumed by |
|---|---|---|
| `founder_name` | text | All |
| `founder_archetype` | select — product, sales, technical, operator | All advisors — calibrates what to explain vs assume |
| `board_exists` | boolean | Governance department — gates the whole department |
| `board_members` | repeatable: name, role, appointed date | Board Minutes, Decision Logger |
| `quorum_requirement` | number | Board Minutes — otherwise every set of minutes carries a placeholder |

## Section 5 — Current situation  *(required)*

| Field | Type | Consumed by |
|---|---|---|
| `priority_1` | textarea | Every advisor. The thing that actually matters right now |
| `target_12mo` | textarea | CEO, CFO, CRO |
| `biggest_risk` | textarea | CISO, CFO, Board Meeting |
| `unfair_advantage` | textarea | CEO, CMO |
| `decision_being_avoided` | textarea | Executive Mentor, Board Meeting |

That last field is the most useful question on the form and the one most likely to be skipped. Keep it optional but keep it there.

## Section 6 — Financial baseline  *(optional, internal only)*

| Field | Type | Consumed by |
|---|---|---|
| `arr_or_revenue` | currency | CFO |
| `monthly_burn` | currency | CFO |
| `cash_balance` | currency | CFO |
| `runway_months` | number | CFO — or derived from the two above |

**Mark this whole section internal-only in the field configuration.** The Company Context agent is instructed never to let these into outbound drafts, but the field-level flag is the enforcement that doesn't depend on an agent behaving.

## Section 7 — Regulatory  *(conditional — show only for regulated industries)*

| Field | Type | Consumed by |
|---|---|---|
| `regulated` | boolean | Gates the Regulated Ops department |
| `device_class` | select — I, IIa, IIb, III | Regulatory Affairs |
| `target_markets` | multi-select — US, EU, Canada, Japan, China, Australia | Regulatory Affairs |
| `qms_standard` | select — ISO 13485, ISO 9001, none | Quality Manager |

---

## Provisioning sequence

1. Form submits → create sub-account.
2. Write all fields as company-level custom fields.
3. Install the department bundles the answers switch on:
   - **Always:** Company Context, plus the core advisors matching `stage`
   - **If `board_exists`:** Governance — Board Minutes, Decision Logger, Board Meeting Facilitator, Corporate Filing Monitor
   - **If `regulated`:** Regulated Ops — Regulatory Affairs, Quality Manager, Risk Management
   - **By `business_model`:** the CFO variant carrying the right benchmark set
4. Create the recurring workflows: filing deadlines off `formation_date`, quarterly context refresh, monthly financial review.
5. Seed an empty decision log.
6. Send the founder a first-run prompt naming the three agents most relevant to `priority_1`.

## Two things to decide before building this

**Conditional sections beat a long form.** Sections 2, 6 and 7 should only appear when earlier answers make them relevant. A regulated medical-device company and a bootstrapped agency should not see the same form.

**Every optional field needs a graceful absence.** The agents already handle missing context — they flag gaps rather than inventing values. Test the provisioning path with only the required fields filled in. If any agent produces confident output from an empty profile, that is a bug in the agent, not the form.
