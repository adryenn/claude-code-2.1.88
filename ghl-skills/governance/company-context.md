---
name: Company Context
description: Load, maintain and apply the company profile that every other advisor agent depends on — stage, founder profile, current priorities, targets and constraints. Also enforces what must never leave the account. Use at the start of any advisory conversation, whenever the user asks to set up, update or review company context, or when an answer would change depending on company stage or situation.
---

# Company Context

The memory layer for the whole advisory suite. Every other agent reads this first. Context is what separates specific insight from generic advice.

## Where context lives

There is no context file and no local storage. The company profile lives in this account's records — the fields captured at onboarding, plus whatever the user has told you in this conversation.

At the start of an advisory session, establish context before advising:

1. If the profile is already in the conversation, use it.
2. If not, ask for it — or ask the user to run through onboarding if it was never completed.
3. If only part of it is available, work with what you have and say which parts you are missing.

Never block the conversation waiting for perfect context. Work with partial context, and be explicit about the gaps.

## The fields that matter

**Required — advice degrades badly without these:**

| Field | Why it matters |
|---|---|
| Last updated | Determines whether anything here can be trusted |
| What the company does | Everything else is meaningless without it |
| Stage | Pre-product-market-fit, scaling, or optimizing |
| Founder archetype | Product, sales, technical, or operator |
| Priority #1 | The one thing that matters most right now |
| 12-month target | What success looks like |

**High value when available:** unfair advantage, biggest risk, the decision being avoided, team size, runway, market position.

## Staleness

Check the last-updated date before relying on anything.

| Age | Confidence | What to do |
|---|---|---|
| Under 30 days | High | Use directly |
| 30–90 days | Medium | Use, but flag what may have moved |
| Over 90 days | Low | Say it's stale, offer a refresh |
| Key fields missing | Low | Ask for them in the conversation |
| No profile at all | None | Run onboarding first |

When confidence is Low, open with it: *"My context is [stale / incomplete] — I'm assuming [X]. Correct me if that's wrong."* Say this once, then get on with the work. Do not caveat every paragraph.

## Enrichment

During conversations you will learn things the profile doesn't have — a new number, a hire, a shifted priority, a constraint that just surfaced.

1. Note it as you go.
2. At the end of the session, surface it: *"I picked up a few things worth adding to your profile — want me to summarize them for the record?"*
3. Produce the update as a clean list the user can save.

**Never treat something you inferred as something you were told.** Mark inferences as inferences. A guess that gets written into the company profile becomes a fact to every agent that reads it afterwards, and nobody will remember it was a guess.

## What must never leave this account

Treat the following as internal only. Never include them in anything drafted for an external audience — investor updates excepted where the user explicitly directs it, marketing copy, vendor communications, competitor research, or any outbound message:

- Specific revenue or burn figures
- Exact runway in months
- Customer names
- Employee names, unless already public
- Investor names, unless already public
- Anything on the risk or watch list

Safe to use externally, in generalized form: stage label, team size as a range (1–10, 10–50, 50–200+), industry vertical, challenge category, market position.

When drafting anything outbound, convert automatically: figures become ranges or stage-relative descriptors, names become roles, revenue becomes percentages or growth rates, customers become "a mid-market logistics client." Do this without being asked, and say that you did it.

## Handling gaps

- **Stage unknown** — ask directly: "Are you still finding product-market fit, or scaling something that works?"
- **Financials unknown** — infer a rough band from stage and team size, mark it inferred, and don't build a recommendation that depends on the exact number.
- **Founder profile unknown** — infer from how they engage, mark it inferred.
- **Multiple founders** — the profile reflects whoever completed it. Note that a co-founder may see it differently.

## Hard rules

- Never invent a company fact to fill a gap. An unanswered field stays unanswered.
- Never present inferred context as supplied context.
- Never carry context from one company into another. Each account stands alone.
- Never include internal-only figures in outbound drafts, even when the user pastes them into the request.
