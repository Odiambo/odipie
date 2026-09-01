# Automatic Prompt Engineering

Automatic prompt engineering uses a repeatable search-and-evaluation loop to propose prompt variants, measure them on representative cases, and select a version under explicit constraints. It is an optimization process, not proof that a prompt will be correct in every deployment.

## When it is useful

- The task repeats often enough to justify an evaluation set.
- Success can be scored by code, a rubric, reviewers, or a combination.
- Failures can be grouped into meaningful categories.
- The model, tool configuration, and prompt version can be recorded.

For one-off or poorly specified work, improve the task definition before automating prompt search.

## The evaluation loop

1. **Define the task contract.** Specify inputs, outputs, constraints, and failure conditions.
2. **Build a representative evaluation set.** Include ordinary, edge, adversarial, and high-impact subgroup cases where relevant.
3. **Record a baseline.** Freeze the model, system instructions, tools, settings, and initial prompt.
4. **Generate controlled variants.** Change one strategy at a time when possible.
5. **Score outputs.** Prefer deterministic checks; supplement them with calibrated review.
6. **Inspect regressions.** Aggregate scores can hide severe failures.
7. **Validate on held-out cases.** Do not select and report on the same examples.
8. **Version and monitor.** Model, data, tool, and policy changes can invalidate the result.

## A minimal experiment record

```yaml
experiment: support-summary-v3
model: provider/model-version
prompt_version: 3
dataset_version: 2026-08-31
tools: [knowledge_search]
primary_metric: grounded_answer_rate
guardrails:
  unsupported_claim_rate: "<= 0.02"
  p95_latency_ms: "<= 2500"
reviewer_notes: "Inspect all safety-critical failures"
```

## Choosing metrics

- task correctness or exact-match checks;
- schema validity;
- groundedness and citation support;
- refusal precision and recall;
- latency and cost;
- human-rated clarity or usefulness;
- subgroup and worst-case performance.

Avoid arbitrary targets unless the scale, reviewers, examples, and acceptance threshold are defined.

## Evaluation methods

### Deterministic checks

Use parsers, unit tests, calculators, type checkers, policy engines, and exact constraints whenever the property can be computed.

### Human review

Use domain experts for nuanced correctness, risk, and usability. Blind the prompt variant when practical and measure reviewer agreement.

### Model-based judging

A model judge can scale review but may favor verbosity, style similarity, or its own prior answer. Calibrate it against humans, randomize answer order, use a concrete rubric, and audit disagreement cases.

## Common failure modes

- **Overfitting:** the prompt memorizes evaluation patterns.
- **Metric gaming:** the score improves while the real outcome worsens.
- **Data leakage:** held-out answers enter the prompt context.
- **Uncontrolled changes:** model or tool updates are attributed to the prompt.
- **Average-only reporting:** a strong mean hides catastrophic edge cases.
- **Prompt injection:** untrusted content changes evaluator or candidate behavior.

## Deployment checklist

- Keep the baseline and a rollback path.
- Store prompt and evaluation-set versions with each run.
- Re-run critical cases after model, retrieval, tool, or policy changes.
- Require human approval for high-impact decisions.
- Publish results as conditional measurements, not universal claims.

See [AI Bias Recognition & Mitigation](AI-Bias-Recognition-&-Mitigation) and [Agents, MCP, and Orchestration](Agents-MCP-and-Orchestration).
