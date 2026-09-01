# Agents, MCP, and Orchestration

An agent is a software system, not just a model. Its harness supplies instructions, tools, state, permissions, an execution loop, and stop conditions. The application executes actions and remains accountable for the permissions it grants.

## The basic agent loop

```text
goal + current state
        |
        v
model selects next action
        |
        +--> answer or stop
        |
        +--> request tool --> host checks permission --> tool executes
                                                   |
                                                   v
                                           result updates state
                                                   |
                                                   +----> repeat
```

The host executes actions; the model proposes structured calls. Reliable systems record the proposed action, authorization decision, result, and resulting state.

## Start with the least complex design

Use a direct model call when one response is enough. Use a deterministic workflow when steps are known. Use one tool-enabled agent when the route varies. Introduce multiple agents only when measured benefits justify the coordination cost.

## Orchestrated agents

An orchestrator decomposes or routes work, provides bounded context, tracks state, and combines results. Common patterns include:

- **Manager and workers:** one agent delegates bounded tasks and reviews outputs.
- **Handoffs:** the active agent transfers control to a specialist with explicit state.
- **Parallel fan-out/fan-in:** independent workers run concurrently and a reducer reconciles results.
- **Generator and reviewer:** one component creates an artifact and an independent component checks it against a rubric.
- **Deterministic router:** code selects the agent or workflow from validated fields.

Define ownership when agents disagree. “Let the agents debate until they agree” is not a reliable termination or correctness rule.

Two widely used orchestration styles are model-directed routing and code-directed routing. In the first, a manager may select a specialist or hand off the active conversation. In the second, code uses validated structured output to choose the next step. The styles can be combined, but consequential routing and writes should retain deterministic validation and approval controls.

## Graph engineering

Graph engineering models a workflow as explicit state, nodes, and edges:

- **State** is the durable record passed through a run.
- **Nodes** perform model calls, tools, validation, approval, or deterministic computation.
- **Edges** define allowed transitions, including branches, retries, and termination.

```text
intake --> classify --> retrieve --> draft --> validate
              |                         |         |
              |                         |         +--> approved --> finish
              |                         +------------> revise --+
              +--> human review ----------------------> finish
```

The phrase is used here for workflow/control-flow graphs, not knowledge graphs or neural-network computation graphs. Every cycle needs a retry budget, every terminal state needs a definition, and state changes should be traceable. A graph framework can help with persistence and resumption, but a diagram alone does not provide reliability.

## Model Context Protocol (MCP)

MCP is an open, JSON-RPC-based protocol for connecting AI applications to external capabilities. Its client-host-server architecture separates:

- **Host:** the AI application and primary policy/consent boundary.
- **Client:** a host-managed protocol component that communicates with one MCP server.
- **Server:** a local or remote service exposing capabilities.

Servers can expose **tools** (operations), **resources** (contextual data), and **prompts** (reusable templates). In the current `2026-07-28` specification, the protocol core is stateless: each request is self-contained and carries its protocol version and capabilities, while applications can still maintain state outside the protocol. Clients may use server discovery before other requests. Older MCP versions used a connection lifecycle and initialization handshake, so implementations must agree on the version they support. MCP standardizes communication and discovery; it does not make a server, its instructions, or its results trustworthy.

Official references:

- [MCP specification](https://modelcontextprotocol.io/specification/latest)
- [MCP architecture](https://modelcontextprotocol.io/specification/latest/architecture)
- [MCP 2026-07-28 release notes](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

## Where MCP belongs

```text
user
  |
agent host: model + policy + loop + audit
  |
MCP client connections
  |
MCP servers: source control, tickets, databases, browsers, internal APIs
```

The agent generally calls a named tool presented by the host. It does not need to know whether that capability came from MCP, a built-in function, or another adapter.

## WebMCP

WebMCP is an emerging Web Machine Learning Community Group API that enables a web application to expose JavaScript-based tools to agents and assistive technologies. It gives a page a structured action surface alongside—not as a replacement for—accessible user interfaces and other browser interaction methods.

WebMCP is a Draft Community Group Report. It is not a W3C Standard and is not on the W3C Standards Track; implementations and API details may change.

| Question | MCP | WebMCP |
|---|---|---|
| Capability provider | Separate local or remote MCP server | Active web application/page |
| Primary consumer | MCP host through a client connection | Browser-integrated AI agent |
| Typical boundary | Service or process integration | In-page browser interaction |
| Maturity | Versioned open protocol | Emerging Community Group draft |

Official reference: [WebMCP draft specification](https://webmachinelearning.github.io/webmcp/).

## References for orchestration and graph workflows

- [OpenAI Agents SDK: agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) distinguishes manager-as-tool, handoff, code-directed, and parallel patterns.
- [LangGraph concepts](https://langchain-ai.github.io/langgraph/concepts/low_level/) describes graph state, nodes, edges, and execution concepts. It is a framework reference, not a requirement to adopt that framework.

## Security and operating controls

- Connect only reviewed servers and web origins.
- Treat tool descriptions, resources, page text, and results as untrusted input.
- Use least-privilege credentials and narrow tool schemas.
- Separate read operations from writes and irreversible actions.
- Require confirmation at the moment of consequential action.
- Validate arguments and outputs outside the model.
- Limit turns, retries, time, tokens, and spend.
- Log provenance, calls, approvals, failures, and state transitions.
- Test prompt injection, confused-deputy, data-exfiltration, and cross-tenant scenarios.

## Production readiness checklist

- Does each agent have a bounded responsibility?
- Can deterministic code replace a model decision?
- Is every tool necessary, authenticated, and authorized?
- Are loops bounded and resumable?
- Are graph states and terminal conditions explicit?
- Are independent evaluations and rollback procedures in place?
- Is a person accountable for high-impact decisions?

See [AI Terminology and FAQ](AI-Terminology-and-FAQ) and [AI Bias Recognition & Mitigation](AI-Bias-Recognition-&-Mitigation).
