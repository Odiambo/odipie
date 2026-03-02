

# Workflow Orchestration

![workflow-orchestration](https://img.shields.io/badge/workflow--orchestration-4A90E2?style=flat-square) ![task-management](https://img.shields.io/badge/task--management-50C878?style=flat-square) ![ai-agents](https://img.shields.io/badge/ai--agents-9B59B6?style=flat-square) ![planning](https://img.shields.io/badge/planning-F39C12?style=flat-square) ![subagents](https://img.shields.io/badge/subagents-E74C3C?style=flat-square) ![self-improvement](https://img.shields.io/badge/self--improvement-1ABC9C?style=flat-square) ![debugging](https://img.shields.io/badge/debugging-E67E22?style=flat-square) ![linting](https://img.shields.io/badge/linting-3498DB?style=flat-square) ![verification](https://img.shields.io/badge/verification-27AE60?style=flat-square) ![software-engineering](https://img.shields.io/badge/software--engineering-8E44AD?style=flat-square) ![developer-productivity](https://img.shields.io/badge/developer--productivity-16A085?style=flat-square) ![prompt-engineering](https://img.shields.io/badge/prompt--engineering-D35400?style=flat-square)

## 1. Plan Mode Default
- Enter plan mode for any non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, stop and re-plan immediately; do not keep pushing.
- Use plan mode for verification steps, not just building.
- Write detailed specs upfront to reduce ambiguity.

## 2. Swarm & Subagent Continuity
- **Subagent**: a single delegated helper focused on one clearly scoped task.
- **Swarm**: a coordinated group of agents or subagents working in parallel toward a shared goal.
- Use subagents to keep the main context window clean by delegating focused work.
- Use swarms for broad exploration or multi-path problem solving when parallelization is helpful.
- Offload research, exploration, and parallel analysis to subagents or swarms as appropriate.
- For complex problems, spin up a swarm of subagents to increase throughput.
- Keep one task per subagent for focused execution; coordinate shared context at the swarm level.

## 3. MCP Tool Delegation
- **Discovery First**: Always search for available MCP tools using `tool_search_regex` before attempting direct calls to deferred/MCP tools.
- **Specialized Knowledge**: Prefer MCP tools for domain-specific tasks (documentation lookups, API interactions, database queries, language-specific analysis).
- **Tool Selection**: Choose the most specific MCP tool for the task (e.g., use Pylance MCP for Python analysis rather than generic grep).
- **Batch Operations**: When using multiple MCP tools, parallelize independent calls to reduce latency.
- **Error Recovery**: If an MCP tool fails, log the error, attempt a fallback strategy (built-in tools or alternative MCP), and never silently ignore failures.
- **Context Awareness**: Before delegating to MCP tools, ensure you have enough context about what data/format they return to use results effectively.
- **Documentation Preference**: For Microsoft/Azure/framework-specific questions, use documentation MCP servers (e.g., `shrpoint_docs_search`) before generic web searches.

## 4. Self-Improvement Loop
- After any correction from the user, update `tasks/lessons.md` with the pattern.
- Write rules for yourself that prevent the same mistake.
- Ruthlessly iterate on these lessons until the mistake rate drops.
- Review lessons at session start for the relevant project.

## 5. Task Verification 
- Never mark a task complete without proving it works.
- Diff behavior between `main` and your changes when relevant.
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, and demonstrate correctness.

## 6. Solutions Improvement
- For non-trivial changes, pause and ask: "Is there a more elegant way?"
- If a fix feels hacky, apply: "Knowing everything I know now, implement the elegant solution."
- Skip this for simple, obvious fixes; do not over-engineer.
- Challenge your own work before presenting it.

## 7. Auto Debugging/Linting
- When given a bug report, fix it without hand-holding.
- Point to logs, errors, or failing tests, then resolve them.
- Require zero context switching from the user.
- Fix failing CI tests without being told how.

## Task Management
1. **Requirements & Planning**: Write a plan to `tasks/todo.md` with checkable items.
2. **Verify Plan**: Check in before starting implementation.
3. **Track Progress**: Mark items complete as you go.
4. **Explain Changes**: Provide a high-level summary at each step.
5. **Document Results**: Add a review section to `tasks/todo.md`.
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections.

## Core Principles
- **Simplicity**: Make every change as simple as possible; impact minimal code.
- **Root Cause First**: Find root causes. Avoid temporary fixes. Follow senior developer standards.
- **Solution Efficiency**: Touch only what is necessary and avoid introducing bugs.
