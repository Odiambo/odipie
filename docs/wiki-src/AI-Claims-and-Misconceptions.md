# AI Claims and Misconceptions

Public AI discussion often evaluates the wrong layer. Separate the base model, its harness, connected data and tools, the workflow, and the organization operating it.

## A five-layer diagnostic

1. **Model:** What can the selected model do under controlled evaluation?
2. **Context and data:** Was relevant, authoritative information available?
3. **Tools and harness:** Were actions, permissions, validation, and retries designed correctly?
4. **Workflow:** Were routing, approval, escalation, and failure states appropriate?
5. **Operations and governance:** Were monitoring, ownership, policy, and incident response adequate?

This separation prevents both model hype and model scapegoating.

## “LLMs are just autocomplete”

Next-token prediction is central to how many language models are trained and generate text. The word “just” does not tell you which tasks the resulting system can perform reliably. Capability must be measured, while fabricated claims, brittle planning, and context sensitivity remain operationally important.

## “LLMs cannot do math”

Models can solve many mathematical tasks, but fluent generation is not a deterministic calculator or proof checker. For important calculations, use code, a calculator, symbolic solver, or formal verifier and validate the inputs and interpretation.

## “RAG eliminates hallucinations”

Retrieval-augmented generation can ground an answer, but creates several failure points: query construction, retrieval, ranking, source quality, context selection, generation, and citation. Measure each stage and allow abstention when support is insufficient.

## “Hallucination is only a deployment problem”

Unsupported generation can originate in model behavior and can be amplified by poor data, prompting, retrieval, or workflow design. Architecture can reduce exposure and catch failures; it cannot convert a probabilistic model into a guaranteed source of truth.

## “Agents are autonomous employees”

An agent is software operating within permissions, tools, budgets, and stop conditions selected by its deployer. Human job titles are metaphors, not specifications. State exactly what the system may read, change, send, purchase, or delete and who approves those actions.

## “More agents produce a better result”

Multiple agents can provide specialization, isolation, parallelism, or independent review. They also create more model calls, handoffs, coordination failures, latency, and cost. Compare the design against a single agent and a deterministic workflow on the same evaluation set.

## “Tool use makes the answer factual”

A tool call adds evidence or an action path, not automatic correctness. The agent can choose the wrong tool, send invalid arguments, use an untrusted source, or summarize the result incorrectly. Preserve provenance and verify material claims or actions.

## “A benchmark score proves production readiness”

Benchmarks measure performance under a particular dataset and procedure. Production readiness also depends on distribution shift, latency, cost, privacy, security, subgroup behavior, error severity, monitoring, and recovery.

## “AI bias is only in training data”

Bias can enter through problem framing, labels, sampling, model objectives, prompt/context selection, retrieval, tool data, thresholds, user interaction, and feedback loops. Mitigation is a lifecycle practice.

## “Safety filters make an agent secure”

Content filters address some inputs and outputs. Agent security also requires authentication, authorization, least privilege, sandboxing, provenance, approval gates, rate and spend limits, validation, and incident response.

## A better way to make an AI claim

State the system, version, task, dataset, tools, settings, metric, baseline, limitations, and evaluation date. Prefer:

> On evaluation set v3, the configured system answered 87% of supported questions with valid citations, compared with 74% for the recorded baseline. It was not evaluated for medical advice.

Avoid:

> The model is 87% accurate and does not hallucinate.

For operational controls, continue with [Agents, MCP, and Orchestration](Agents-MCP-and-Orchestration).

