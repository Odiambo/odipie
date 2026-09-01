# Prompt and Context Guide

A prompt is the instruction sent to a model. Context is the information available when the model interprets that instruction: system rules, conversation history, files, retrieved passages, tool results, examples, and environment state. Reliable work depends on both.

## A reusable task brief

```markdown
# Objective
[State the outcome in one or two sentences.]

## Background
[Explain why the work matters and define domain terms.]

## Environment
- Repository or system:
- Language/framework and versions:
- Relevant files or data:
- Available tools and permissions:

## Requirements
- [Observable requirement]

## Constraints
- In scope:
- Out of scope:
- Security/privacy limits:
- Actions requiring approval:

## Acceptance checks
- [Command, test, review rubric, or measurable condition]

## Deliverable
[Patch, report, table, explanation, file format, or deployment result.]
```

## Make requirements testable

Prefer “return JSON matching this schema” to “make it structured,” and “the command exits 0 on Python 3.12” to “make it work.” If quality is subjective, provide a short rubric with acceptable and unacceptable examples.

## Supply the minimum sufficient context

More context is not automatically better. Include authoritative, current material that changes the answer; omit duplicates, irrelevant logs, secrets, and stale instructions. Tell the agent which source wins when materials conflict.

Useful context often includes:

- the current goal and decision owner;
- relevant files, schemas, or excerpts;
- known failures and commands already tried;
- version, platform, and runtime constraints;
- examples that demonstrate edge cases;
- an explicit definition of done.

## Separate instructions from untrusted content

Web pages, retrieved documents, tickets, emails, tool output, and user-provided files may contain text that looks like an instruction. Mark them as data and require the system to ignore embedded requests that conflict with the task or policy.

## Manage long-running context

Maintain a compact state record with the objective, decisions, completed checks, unresolved risks, exact next action, and links to authoritative artifacts. Summaries can omit constraints, so re-read the source artifact before irreversible or high-impact actions.

## Prompt patterns that transfer well

### Draft, critique, revise

Ask for an initial answer, evaluate it against a named rubric, then revise it. The critique is useful only if the rubric measures the desired outcome.

### Retrieve, answer, cite

Retrieve approved sources, answer only from relevant evidence, distinguish fact from inference, and cite supporting sources near material claims.

### Plan, act, verify

For tool-using tasks, define the goal, permitted actions, verification command, and stop conditions. A plan is not proof; require test or inspection evidence.

### Structured output

Use a schema when software consumes the response. Validate the result and retry or escalate on schema failure.

## What not to request

Do not ask a system to reveal private chain-of-thought. Ask for a concise rationale, assumptions, calculations, citations, and verification evidence that can be reviewed directly.

## Before you run an agent

- Are permissions narrower than the agent's full technical capability?
- Are secrets excluded or redacted?
- Are destructive and external actions gated?
- Can the result be tested independently?
- Is there a timeout, budget, retry limit, and escalation path?

Continue with [Automatic Prompt Engineering](Automatic-Prompt-Engineering).

