# Odipie Wiki Cleanup Plan

## Audit summary

The public `chef` branch and local checkout were synchronized before this review. The repository mirror had seven substantive Markdown pages, one empty bias page at the repository root, and a one-line footer. The live GitHub wiki had eight newer pages, including the full bias table, a long context-engineering guide, an unsupported benchmark comparison, and an unfinished persistence outline. The main issues were:

- no sidebar or explicit reading order;
- duplicate orchestration content;
- an inaccurate MCP overview that defined the words “model,” “context,” and “protocol” rather than the Model Context Protocol;
- links to pages that did not exist;
- inconsistent filenames, titles, tone, and heading depth;
- no beginner glossary or FAQ;
- no clear distinction between a model, assistant, agent, workflow, and multi-agent system;
- no WebMCP, orchestration, or graph-workflow guidance;
- unsupported performance and market claims presented as general facts;
- an empty AI bias page and an adversarial misconceptions page.

## Live-to-canonical migration

| Live page | Cleanup destination |
|---|---|
| Home | **Home**; inaccurate MCP material moves to the agent-systems page. |
| Advanced Prompt Engineering | Split between **Prompt and Context Guide** and **Automatic Prompt Engineering**. |
| AI Bias Recognition & Mitigation | Preserved and expanded as **AI Bias Recognition & Mitigation**, including all 18 table categories. |
| Context: Talking to Models and Agents | Condensed into **Prompt and Context Guide**, terminology, and agent operating controls. |
| Odipie vs Other Lazy Loading Solutions | Accurate concepts move to **Getting Started**; unreferenced benchmark numbers and universal recommendations are removed. |
| OdiPie: Engineering Persistence (Under Construction) | Replaced by the completed eight-page navigation and the source-of-truth plan. |
| Outdated Critiques of LLMs | Reframed neutrally as **AI Claims and Misconceptions**. |
| Workflow Orchestration | Rebuilt as **Agents, MCP, and Orchestration**. |

## Canonical eight-page structure

1. **Home** — scope, audience, reading paths, and project orientation.
2. **Getting Started** — install, smoke checks, optional extras, Docker, and troubleshooting.
3. **AI Terminology and FAQ** — plain-language glossary and common beginner questions.
4. **Prompt and Context Guide** — reusable task template and context-engineering practices.
5. **Automatic Prompt Engineering** — evaluation-driven prompt optimization.
6. **Agents, MCP, and Orchestration** — agents, orchestrated agents, MCP, WebMCP, and graph engineering.
7. **AI Claims and Misconceptions** — balanced corrections to common hype and dismissal.
8. **AI Bias Recognition and Mitigation** — sources of bias, evaluation, controls, and limits.

`_Sidebar.md` supplies the reading order and `_Footer.md` supplies compact navigation.

## Editorial rules

- Define a term before using its acronym.
- Separate model capability from system behavior and deployment guarantees.
- Label emerging specifications as drafts when applicable.
- Prefer reproducible local measurements over universal performance claims.
- Treat tools and retrieved content as untrusted inputs.
- Avoid anthropomorphism and claims that an agent is inherently autonomous, correct, or secure.
- Cite primary specifications or first-party technical guidance for time-sensitive claims.
- Keep Odipie product instructions separate from general AI education.

## Publication checklist

- [ ] Confirm eight canonical content pages plus navigation files.
- [ ] Check internal links and repository links.
- [ ] Check headings, code fences, spelling, and trailing whitespace.
- [ ] Fact-check MCP, WebMCP, orchestration, graph engineering, and safety claims.
- [ ] Verify package and Docker commands against the current repository.
- [ ] Commit and push the source files to `origin/chef`.
- [ ] Publish the same canonical pages to the GitHub wiki remote.
