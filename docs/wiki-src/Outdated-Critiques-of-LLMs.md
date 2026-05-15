## A little noise cancellation in the AI arena would be helpful. 

### A lot is being claimed by sudden AI experts on LinkedIn, X, and any hill from which sudden experts yell. These claims cause confusion and for me (and other professional consultants) odd expectations or pessimism from clients. 
### A quick example is with my fraud prevention engagements where model ability gets conflated or outright confused with model architecture. 

In this context an AI architectural challenge (system design problem), you deploy an LLM to flag potentially fraudulent transactions in near-real time across multiple payment rails. The challenge is not whether the model can detect fraud patterns, but how it is embedded in the system:

* Coordinating real-time streaming data, historical context, and user behavior graphs

* Ensuring the model’s judgment is advisory, with deterministic policy engines enforcing final allow/deny decisions

* Maintaining auditability, replay, and rollback when the model’s reasoning changes
 
This would be an architectural problem: orchestration, control boundaries, trust placement, and failure containment.

To address an ability issue (compute / correctness problem), the model must correctly calculate risk scores, thresholds, and statistical correlations. If the LLM miscalculates a probability, fails at arithmetic, or produces inconsistent outputs under load, that is an ability problem—addressed by more compute, better training, or deterministic calculators.

**The Distinction**

Architecture: *Where and how should AI be allowed to influence outcomes safely?*

Ability: *Can the model compute the right answer reliably?*

Most real-world AI failures in 2024–2025 stem from system architecture, integration, data, governance, and workflow misalignment, rather than from deficiencies in the underlying foundation models themselves.

**A field note:** Most client and prospects are failing to implement correctly or correctly use the output. 

### Top LLM/AI Critiques as of Jan 2026

There are many persistent critiques of large language models (LLMs) that reflect their 2020–2022-era limitations rather than their current operational reality. While these critiques were once correct, they no longer describe how modern AI systems are designed or deployed. This may be a consequence of early certifications and outdated LLM/prompt engineering curricula.

You have to filter out two loud but equally misleading narratives: the overnight “AI evangelist” who insists models are basically magic, and the LinkedIn/X “skeptic influencer” who insists nothing has improved since the “next-word prediction” memes went viral. The truth is more interesting: the field has shifted from arguing about whether models “reason” to engineering systems that reliably separate probabilistic generation from deterministic checking, execution, and enforcement—because that is where real-world correctness is won or lost.

Common claims I see circulate repeatedly on LinkedIn and X: “LLMs can’t do math,” “they’re just autocomplete trained on Reddit,” “hallucinations make them unusable,” and “image models can’t even count fingers.” These claims often conflate two different things: (1) what a base model can do in isolation, and (2) what modern AI systems do in production with tools, verifiers, and evaluation harnesses.

On “trained on human knowledge vs. computational logic,” the critique is mildly correct about how LLMs learn (statistical learning from large corpora) but wrong in the implied conclusion that they lack computational rigor. Current practice emphasizes inference-time methods, best-of-N sampling, rejection sampling with verifiers, self-consistency, and search over solution paths to increase reliability without pretending the raw model is deterministic. This is a research-visible trend, oppose to marketing.

On “LLMs are terrible at math,” the practical update is architectural: strong systems treat the LLM as the planner/translator and push calculation and proof obligations into deterministic backends (symbolic solvers, code execution, formal systems) with verification signals. The direction of research literature is explicit about formal methods and verifiable rewards as the path to durable gains in mathematical reliability. 

That said, it is also now well documented that “LLM-as-its-own-verifier” can fail; naïve self-correction can degrade outcomes, which is why serious stacks use structured verifiers, multiple checks, or domain-grounded validators rather than vibes-based “double check your work.”

On “image models can’t count fingers,” this critique became a meme because it was visible and frequent in early diffusion outputs. The update is not that generative vision is “solved,” but that research and systems have moved toward hybrid diffusion/transformer designs and stronger spatial/structural constraints (including synthetic data where appropriate). The broader image-generation literature reflects this steady march: better architectures, better supervision, and better evaluation reducing classic artifact patterns even if edge cases persist.

The top hype, "hallucinations", is bothersome semantically, but even if I gave in to the misuse of the word the overnight gurus still haven't learned the science behind their own claim. LLM hallucinations dominate headlines, but research shows they are amplified—often created—by misuse of architecture

Studies on Retrieval‑Augmented Generation (RAG) reveal that hallucinations often arise from poor retrieval quality, stale embeddings, missing citation enforcement, or lack of confidence gating, even when models themselves perform well. Microsoft’s 2025 enterprise guidance explicitly frames hallucination control as a system‑level responsibility involving data curation, retrieval design, reranking, prompting constraints, and monitoring—not simply “better models”. 
ANd, there's this complicated solution to hallucination prevention called semantic-entropy and confabulation detection. I send you to the experts on this: [Detecting Hallucinations in LLMs...](https://www.nature.com/articles/s41586-024-07421-0.pdf)

In consumer or viral incidents (e.g., incorrect legal citations, health advice errors), failures may appear model‑centric. However, post‑analysis typically reveals users lack of disclaimers, no output validation, and poor domain gating (and escalation paths). While these may be deployment and architectural lapses, they are frequently mislabeled as “bad models” in public discourse. 

The competence of models has advanced faster than the institutional and general consumer ability to design, constrain, and operationalize AI systems.

