# AI Terminology and FAQ

Product names often combine several layers. Identify which layer a claim describes before evaluating it.

## Models and generation

- **Artificial intelligence (AI):** a broad category of systems that perform tasks associated with perception, prediction, generation, decision support, or planning.
- **Machine learning (ML):** methods that learn patterns from data instead of encoding every rule by hand.
- **Foundation model:** a broadly trained model adapted to many downstream tasks.
- **Large language model (LLM):** a model trained to process and generate token sequences, commonly text and code.
- **Generative AI:** systems that produce content such as text, images, audio, video, or code.
- **Multimodal model:** a model that accepts or produces more than one modality.
- **Parameters:** learned numerical values inside a model. Parameter count alone does not establish quality.
- **Training:** updating model parameters from data and an optimization objective.
- **Inference:** running a trained model to produce an output.
- **Token:** a unit the model processes. It may be a word, part of a word, punctuation, or another encoded unit.
- **Embedding:** a numerical representation used to compare or retrieve semantically related items.
- **Fine-tuning:** additional training that changes model parameters for a task or behavior.
- **Quantization:** representing weights or activations with lower precision to reduce resource use, sometimes with quality trade-offs.

## Prompts, context, and knowledge

- **Prompt:** instructions and input sent to a model for a request.
- **System instruction:** high-priority behavior configured by the application hosting the model.
- **Context:** information available for the current inference, including instructions, messages, retrieved text, and tool results.
- **Context window:** the provider's limit on input plus generated tokens. A large window does not mean every detail is used equally well.
- **Context engineering:** selecting, structuring, refreshing, and protecting information placed in context.
- **Retrieval-augmented generation (RAG):** retrieving external material and placing selected results in context before generation.
- **Vector database:** a system optimized to store and search vector representations; it is one possible retrieval component, not a requirement for all RAG.
- **Knowledge cutoff:** a rough description of how current a model's training data may be. It is not a complete inventory or a guarantee that every fact before a date is known. Tools can provide newer information, but sources still need validation.
- **Memory:** an application feature that stores and reintroduces information across turns or sessions. A base model does not independently remember prior API calls.

## Tools and agents

- **Tool/function call:** structured output asking the host to execute a named operation with arguments.
- **Tool result:** data or an error returned after the host executes a tool.
- **Harness:** software around a model: instructions, tools, permissions, memory, context management, retries, logging, and interface.
- **Assistant:** a user-facing AI application; it may answer directly or contain agentic behavior.
- **Agent:** a system in which a model, instructions, and available tools can select and sequence actions inside a loop until a stop condition. The surrounding application, not the model alone, supplies permissions and execution.
- **Agentic:** describing variable, model-directed action selection. It does not mean unlimited autonomy.
- **Workflow:** a defined sequence or graph of steps. Some steps may be deterministic and others agentic.
- **Orchestrator:** a component that routes tasks, state, permissions, and results across workers or agents.
- **Subagent/worker agent:** a separately scoped agent invoked by an orchestrator for a bounded responsibility.
- **Multi-agent system:** a workflow containing multiple coordinated agent instances or roles.
- **Human in the loop:** a control point where a person reviews, approves, corrects, or takes over.

## Integration and reliability

- **API:** a defined software interface for requesting data or actions.
- **Model Context Protocol (MCP):** an open protocol through which AI hosts connect to servers that expose tools, resources, and prompt templates.
- **MCP host/client/server:** the host runs the AI application and policy boundary; each client communicates with one server; the server exposes capabilities. In the current `2026-07-28` MCP core, requests are self-contained rather than session-dependent.
- **WebMCP:** a Web Machine Learning Community Group draft API through which a web application can expose JavaScript-based tools to agents and assistive technologies. It is not the same protocol or deployment boundary as MCP, and it is not a W3C Standard or Standards Track specification.
- **Graph workflow (graph engineering):** an explicit workflow whose nodes perform work and whose edges define legal transitions. Its state, retries, terminal states, and approval points are part of the design; it is distinct from a knowledge graph.
- **Evaluation (eval):** a repeatable test of system behavior on defined cases and metrics.
- **Benchmark:** a standardized dataset or procedure used to compare performance; results may not predict a specific deployment.
- **Guardrail:** a preventive or detective control around a model. No single guardrail guarantees safety.
- **Prompt injection:** untrusted content that attempts to redirect a model or agent away from authorized instructions.
- **Hallucination/confabulation:** generated content that is unsupported or false despite appearing plausible. Retrieval and tools can reduce some failures but do not eliminate them.
- **Observability/tracing:** recording inputs, outputs, tool calls, latency, cost, and state transitions so a run can be inspected.
- **Non-determinism:** the same request can produce different outputs because of sampling, infrastructure, tool state, or model changes.

## FAQ

### Is an LLM a database or search engine?

No. A model generates outputs from learned parameters and current context. Search and databases retrieve stored records. An application can combine all three.

### Does an AI model understand or reason like a person?

Terms such as “understanding” and “reasoning” describe observed task behavior, not proof of human-like cognition. Evaluate the capability needed for the task instead of inferring an inner mental state.

### Is an assistant automatically an agent?

No. A direct question-answer system may make no external actions. An agent has a loop in which the system can choose and sequence actions under defined permissions and stop conditions.

### Are agents autonomous?

Autonomy is a property of the deployment: which actions are allowed, how long the loop runs, and where approval is required. It is not an all-or-nothing property of the model.

### Does more context always improve the answer?

No. Irrelevant, duplicated, conflicting, or malicious context can reduce quality. Curate context and identify authoritative sources.

### Does a larger model always perform better?

No. Quality also depends on the task, training, tools, prompt, latency budget, cost, and evaluation. Smaller specialized models can outperform larger ones on a bounded workload.

### Does RAG prevent hallucinations?

No. Retrieval can return irrelevant or incorrect material, and the model can misread or ignore it. Evaluate retrieval quality, answer support, citation accuracy, and abstention separately.

### Can temperature zero guarantee identical answers?

No. It reduces sampling variability, but model updates, routing, numerical behavior, context, and tool state can still change results.

### Can an LLM safely make legal, medical, hiring, lending, or security decisions?

Do not infer safety from fluent output. High-impact uses require qualified oversight, applicable legal review, validated data, subgroup evaluation, auditability, and deterministic policy controls appropriate to the domain.

### Is tool use proof that an answer is correct?

No. A system may choose the wrong tool, pass wrong arguments, receive bad data, or misinterpret the result. Validate both the action and its evidence.

### Does MCP make an integration secure?

No. MCP standardizes communication and capability discovery. Authentication, authorization, consent, data handling, server trust, tool design, and output validation remain deployment responsibilities.

### Is WebMCP just MCP in a browser?

No. They share a goal—structured agent access to capabilities—but have different specifications and trust boundaries. WebMCP lets the active page register browser-visible tools; MCP connects a host to separate MCP servers.

### What is graph engineering, and do I need a graph framework?

Graph engineering is the practice of making workflow state and allowed transitions explicit. It is useful when a process branches, pauses for approval, retries, resumes after failure, or needs an audit trail. A framework can help implement those properties, but a small deterministic sequence is usually clearer when the flow is linear.

### Are multi-agent systems always better than one agent?

No. They add coordination, cost, latency, and debugging complexity. Start with one agent plus clear tools; split roles when isolation, specialization, parallel work, or independent review provides a measured benefit.

### Can a model verify its own answer?

It can critique an answer, but correlated errors can survive self-review. Prefer independent tests, trusted data, deterministic validators, and qualified human review.

### Who is responsible for an agent's action?

The people and organization deploying the system remain responsible for its permissions, controls, monitoring, and outcomes. Calling software an “agent” does not transfer accountability.

Continue with [Agents, MCP, and Orchestration](Agents-MCP-and-Orchestration).
