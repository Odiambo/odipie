<html>
<body>
<!--StartFragment--><html><head></head><body><h1>Odipie Wiki</h1>
<p>Welcome to the official odipie Wiki, your guide to building scalable, modular, and production-ready AI systems with Python and large language models (LLMs). This documentation is designed for developers, researchers, and engineers who want to harness the power of generative AI through a structured, maintainable, and extensible architecture.</p>
<p>Odipie combines modern development best practices with the flexibility of Python and the intelligence of LLMs, enabling the rapid prototyping and deployment of intelligent systems. Whether you're orchestrating model prompts, integrating external tools, or preparing containers for production, this guide walks you through each layer of the stack: from environment setup and code quality to model interaction patterns and deployment strategies.</p>
<p>Research and training pipelines are easily maintained in Jupyter Notebooks. This is a good tool for folks new to the building side of AI.  

<p>Explore how odipie implements the Model–Context–Protocol (MCP) pattern to separate responsibilities, reduce coupling, and empower developers to scale AI capabilities with confidence.</p>
<h2>1. Model–Context–Protocol (MCP) Overview</h2>
<p>odipie adopts the <strong>Model–Context–Protocol (MCP)</strong> architectural pattern to ensure clean separation of concerns, maximize reusability, and support modular scaling in LLM-powered systems.</p>
<ul>
<li>
<p><strong>Model</strong>: The "Model" represents a large language model or AI agent, such as OpenAI's GPT or a local transformer-based model. In odipie, these models are accessed via structured, well-encapsulated Python modules that abstract away the backend engine. This allows easy model replacement or extension without changing the surrounding logic.</p>
</li>
<li>
<p><strong>Context</strong>: This includes any runtime information needed to process a request: user inputs, environmental variables, prompt templates, runtime arguments, and session metadata. Context encapsulation ensures that each model call receives exactly what it needs—no more, no less. It also makes it easier to test and reproduce behaviors.</p>
</li>
<li>
<p><strong>Protocol</strong>: Protocols define the rules of engagement between context and model. This includes validation steps, response parsing, retry logic, fallbacks, logging, and any pre/post-processing behavior. Protocols also govern how tools (e.g., search, math, file I/O) are integrated and triggered, turning odipie into a controlled, observable orchestration layer.</p>
</li>
</ul>
<p>By formalizing these components, odipie provides a blueprint for responsible, testable, and extensible AI development. Developers can iterate on prompts and model logic without breaking interface contracts. Meanwhile, protocols help enforce safety, manage dependencies, and enable LLM chaining or decision trees across use cases like document analysis, structured Q&amp;A, or data transformation pipelines.</p>
<p>The MCP pattern allows odipie to support:</p>
<ul>
<li>
<p>Pluggable models (LLMs or otherwise)</p>
</li>
<li>
<p>Runtime-configurable workflows</p>
</li>
<li>
<p>Integration with external tools (search, APIs, databases)</p>
</li>
<li>
<p>Streamlined monitoring and error handling</p>
</li>
</ul>
<p>In essence, odipie uses MCP to turn generative AI into something composable and production-friendly without giving up on flexibility or developer ergonomics.</p>
<hr>
<h2>2. Python Environment Setup &amp; Poetry Workflow</h2>
<ol>
<li>
<p><strong>Install Poetry</strong> if needed:</p>
<pre><code class="language-bash">curl -sSL https://install.python-poetry.org | python3 -
</code></pre>
</li>
<li>
<p><strong>Install dependencies</strong> and activate:</p>
<pre><code class="language-bash">poetry install
poetry shell
</code></pre>
<p>This creates isolated virtual environments and clean dependency management via <code inline="">pyproject.toml</code>.</p>
</li>
<li>
<p><strong>Running tasks</strong>:</p>
<ul>
<li>
<p><code inline="">poetry run python -m odipie</code> launch core module</p>
</li>
<li>
<p><code inline="">poetry run pytest</code> run tests</p>
</li>
</ul>
</li>
</ol>
<p>Poetry ensures consistent environments, easy dependency pinning, and simpler CI/CD integration.</p>
<hr>
<h2>3. Docker Environment Preparation</h2>
<p>Offer both local dev and production-ready images:</p>
<pre><code class="language-dockerfile">FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
 &amp;&amp; poetry config virtualenvs.create false \
 &amp;&amp; poetry install --no-dev
COPY . .
CMD ["odipie"]
</code></pre>
<ul>
<li>
<p>Bases image on a slim Python release.</p>
</li>
<li>
<p>Uses Poetry to install pinned dependencies.</p>
</li>
<li>
<p>Copies code and executes the primary CLI/script entrypoint.</p>
</li>
</ul>
<p>Optionally, add a <code inline="">docker-compose.yml</code> for local services and tools integration.</p>
<hr>
<h2>4. Code Hygiene &amp; Python Best Practices</h2>
<ul>
<li>
<p><strong>Formatting</strong>: Use tools like <code inline="">black</code>, <code inline="">isort</code>, and <code inline="">flake8</code> (can be integrated via <code inline="">poetry add -D ...</code>).</p>
</li>
<li>
<p><strong>Typing</strong>: All public functions should include type hints for clarity.</p>
</li>
<li>
<p><strong>Structure</strong>: Organize modules by domain—e.g., <code inline="">models/</code>, <code inline="">contexts/</code>, <code inline="">protocols/</code>.</p>
</li>
<li>
<p><strong>Tests</strong>: Keep tests in a <code inline="">tests/</code> folder, following the structure of your code.</p>
</li>
<li>
<p><strong>Docs</strong>: Use doctrings in Google or NumPy style; generate docs with Sphinx or MkDocs as needed.</p>
</li>
<li>
<p><strong>Lazy loading and other CI and edge ergonomics</strong>:
[Odiapie in Comparison](https://github.com/odiambo/odipie)
</li>
</ul>

<h2>5. LLM Capabilities and Tool Integration</h2>
<p>Use of LLMs alongside tools:</p>
<ul>
<li>
<p><strong>Structured prompts</strong>: Prompt templates encapsulate context and required schema.</p>
</li>
<li>
<p><strong>Tool usage</strong>: Call external services (e.g. search, calculators) via code hooks mediated through LLMs.</p>
</li>
<li>
<p><strong>Validation loops</strong>: After NLP output, parse and validate results before proceeding.</p>
</li>
</ul>
<p>This structured approach helps ensure predictable, schema-compliant outputs by tight coupling task framing with model input.
There is a lot of talk about 'hallucinations' and not much talk, outside of academics, about what is really going on with the models and what the user's behavior is during the full interaction.</p>
<p>One thing is for sure, good output comes from proper scoping, context use [Context engineering is a marketing phrase. It goes without saying that adding context to a question or research inquiry will return a better result than utter nonsense ending with a question mark.] and the use of templates help reduce output errors.</p>
<p>Good model development, tool integration, RAG, and long-term memory reduce model drift and help with downstream validation success. We get into deep architecture later.</p>
<h3>Upcoming projects and template pipelines:</h3>
<ul> 
   <li>Tool schema and contract development</li>
   <li>Add multi-turn protocols for task requiring retries or planning</li>
   <li>Integrate MCP monitoring, validation logs, and encryption</li>
   <li>Adversarial stress testing</li>
</ul>

<hr>
<h2>6. Advantages of MCP &amp; LLMs + Python Pipeline</h2>

Advantage | Description
-- | --
Modular design | Each MCP component is testable and swappable, ideal for specialization.
Dynamic behavior | Protocols can enforce retries, fallback, and chain call logic.
Observability | Easily log context and prompts for traceability or auditing.
Tool orchestration | Seamlessly bridge LLMs with Python utilities and 3rd-party APIs.
Evolving automation | As models improve, only model layer changes—context & protocol stay stable.


<p>Using Python as the “common” language allows complex interactions, LLMs as brain, Python as hands, to automate workflows, make decisions, and generate outputs dynamically and simplified.</p>
<hr>
<h2>✅ Quick Start</h2>
<pre><code class="language-bash">git clone https://github.com/Odiambo/odipie.git
cd odipie
poetry install &amp;&amp; poetry shell
poetry run python -m odipie --help
</code></pre>
<p>Or build the Docker image:</p>
<pre><code class="language-bash">docker build -t odipie:latest .
docker run --rm odipie:latest --help
</code></pre>
<hr>
<h2>Project Outlooks</h2>
<ul>
<li>
<p><strong>Model swapping</strong>: Plug in different LLMs (local or cloud) with minimal changes.</p>
</li>
<li>
<p><strong>Tool library</strong>: Add more connectors—web search, database calls, file I/O.</p>
</li>
<li>
<p><strong>UI integration</strong>: Expose MCPs via REST or CLI for wider adoption.</p>
</li>
<li>
<p><strong>Metrics</strong>: Include usage tracking and performance metrics for protocol paths.</p>
</li>
</ul>
<hr>
<p>Overall, odipie emphasizes human-centered code structure, clean environment management, and intelligent orchestration of LLMs and tools. It’s a powerful springboard for scalable, tool-driven AI workflows with Python at the core.</p></body></html><!--EndFragment-->
</body>
</html>