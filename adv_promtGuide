# Quick Guide on Prompt Engineering

## Understanding Output Configuration and Model Interfaces

Before diving into prompting strategies, it's important to understand the relationship between prompt design and the context in which a language model is accessed. The format and structure of the output are highly dependent on two factors: the output configuration and the method of access.

### Output Configuration

Output configuration governs the expected format of a model’s response. This can include:

* **Temperature**: Controls randomness. Lower values lead to more deterministic output.
* **Top-p / nucleus sampling**: Adjusts diversity by limiting the probability mass.
* **Max tokens**: Determines the length of the response.
* **Stop sequences**: Signals to the model where to end the output.

Correctly setting these parameters is important for structured outputs like JSON, markdown, tables, or function arguments. In production environments, especially in API-driven pipelines, poorly defined output configurations can result in unusable or malformed results.

### Method of Access: Prompting via Web Interfaces vs. APIs

#### 1. Prompting via Web Interfaces (e.g., Perplexity, Manus)

Web interfaces like **Perplexity AI** or **Manus** offer interactive experiences where the model is often guided by frontend logic. These systems:

* Use behind-the-scenes prompt tuning (system prompts).
* May auto-correct grammar or style.
* Can rely on RAG (retrieval-augmented generation) and plugins.
* Return results tailored for readability, not structured parsing.

**Limitation**: You have minimal control over inference parameters, and responses are often not programmatically structured.

#### 2. Prompting via APIs (e.g., OpenAI, Anthropic)

Prompting through APIs offers direct access to LLM inference engines. You can:

* Set precise generation parameters (e.g., temperature, stop tokens).
* Programmatically enforce response formats (e.g., JSON, YAML).
* Use function calling or tool use (e.g., OpenAI's `tool_choice`, Anthropic’s `system_prompt`).

**Advantage**: This level of control is crucial for applications like data extraction, report generation, or interacting with other systems programmatically.

**Example - OpenAI API Prompt:**

```json
{
  "model": "gpt-4",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant that returns JSON."},
    {"role": "user", "content": "Return the sentiment and main topic of this review: 'The product was okay, but shipping was late.'"}
  ],
  "temperature": 0,
  "max_tokens": 100
}
```

**Expected Output:**

```json
{
  "sentiment": "neutral",
  "topic": "shipping"
}
```

---

## Prompt Engineering Techniques

### Step-back Prompting

Step-back prompting encourages a model to reassess and reflect on its previous assumptions or outputs. It involves prompting the model to explicitly reconsider its reasoning, thus reducing errors caused by initial assumptions.

* **Quick take**: This approach helps models avoid confirmation biases or premature conclusions by forcing reevaluation.
* **Use-case**: Debugging complex reasoning or refining strategic decisions.
* **Example**:

  ```
  Prompt: "The algorithm underperforms. Step back and reexamine underlying assumptions and methodology."
  ```

### Chain of Thought (CoT)

Chain of Thought prompting involves structuring prompts to guide a model through a logical reasoning path, breaking complex tasks into simpler sequential steps.

* **Quick take**:  This method emulates human cognitive processes, enhancing the accuracy of reasoning tasks.
* **Use-case**: Mathematical problem-solving, diagnostics.
* **Example**:

  ```
  Prompt: "Solve and explain step-by-step: Integrate sin(x)^2 dx."
  ```

### Self-consistency

Self-consistency prompting requests multiple solutions or explanations from the model and identifies consistent themes or consensus.

* **Quick take**: Enhances reliability by reducing outliers in generated solutions.
* **Use-case**: Research, exploratory analysis.
* **Example**:

  ```
  Prompt: "Provide three different explanations of entropy and summarize their common points."
  ```

### Tree of Thoughts (ToT)

ToT prompting allows exploring multiple hypotheses or reasoning pathways simultaneously before choosing the optimal solution based on evaluative criteria.

* **Quick take**: Useful for complex decision-making, simulating exploratory thinking processes.
* **Use-case**: Strategic planning, hypothesis generation.
* **Example**:

  ```
  Prompt: "Identify three feasible renewable energy strategies, evaluate their strengths and weaknesses, then recommend the best approach."
  ```

### ReAct (Reason & Act)

ReAct integrates both reasoning and action-oriented prompts, allowing models to not only reason but take or suggest direct actionable steps.
The core structure of ReAct prompting is cyclic in thought:
1. Thought - The model reasons (arguably) about the current task and what needs to be done
2. Action - The model takes a specific action (search, calling a tool) 
3. Observation - The model processes the resulta of that action
4. Thought - The model reflects on the observation and plans the next step

This cycle continues until the task is complete. These interations are anagolous to human problem-solving by breaking complex problems or tasks into manageable steps.
* **Quick take**: It's particularly valuable for complex tasks that require multi-step problem-solving and decision-making.
* **Use-case**: Debugging, adaptive systems.
* **Example**:

  ```
  Prompt: "Identify the cause of this software bug and list clear steps for remediation."
  ```

### Automatic Prompt Engineering

Systematically optimizes prompts.

* **Quick take**:
* **Use-case**: High-volume Q\&A, content generation.
* **Example**:

  ```
  Prompt: "Generate five prompts to clearly define artificial intelligence for a general audience."
  ```

## JSON in Prompt Engineering
JSON prompt engineering involves structuring prompts in a way that guides the model to return outputs in valid JSON format. This is critical in machine-to-machine interactions, software automation, and modern AI-driven applications that require predictable and readable output.

When LLMs are integrated into applications, especially through APIs, the ability to return structured data is non-negotiable. Prompting a model to return a well-formed JSON object allows downstream processes (like UI rendering, database inserts, or automated pipelines) to consume outputs directly without additional parsing or correction. This ensures reliability, reduces post-processing, and increases security in automated flows.

### JSON Repair
JSON repair involves detecting and correcting syntactical errors in JSON data to ensure proper parsing and functionality.

* **Quick take**: Essential for complex data interchange, ensuring automated systems correctly interpret data structures.
* **Incorrect Config:**

```json
{
  "user": "Alice",
  "age": 30,
  "interests": ["AI", "ML",,]
}
```

* **Corrected Config:**

```json
{
  "user": "Alice",
  "age": 30,
  "interests": ["AI", "ML"]
}
```

### JSON Schemas
JSON schemas define the structure and constraints of JSON data to validate conformity.

* **Quick take**: Facilitates data integrity, consistency, and validation, particularly critical in API interactions and data-driven applications.
**Example:**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "username": { "type": "string" },
    "age": { "type": "integer" },
    "skills": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["username", "age"]
}
```

## What is JSON-LD (JSON for Linked Data)?
JSON-LD is a lightweight Linked Data format that provides a structured, context-aware way to encode information about resources and their relationships.

* **Quick take**: JSON-LD leverages context to specify data semantics, enhancing interoperability and clarity in data exchanges across different systems.
### Example JSON-LD:

```json
{
  "@context": {
    "name": "http://schema.org/name",
    "homepage": {"@id": "http://schema.org/url", "@type": "@id"},
    "image": {"@id": "http://schema.org/image", "@type": "@id"}
  },
  "name": "Alice Doe",
  "homepage": "https://example.com/alice",
  "image": "https://example.com/alice.jpg"
}
```

* **Use-case**:  Semantic web applications, SEO optimization, knowledge graphs, improved data interoperability.

## Wrap-up

This quick guide provides insights into advanced prompt engineering, output strategies, and the structured use of JSON and JSON-LD.

> V 2.10.0