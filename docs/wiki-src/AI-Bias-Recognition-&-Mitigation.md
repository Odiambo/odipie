# AI Bias Recognition & Mitigation

Bias is a systematic difference in data, model behavior, or system outcomes. Not every difference is unfair, and an equal aggregate score does not establish fairness. The relevant question depends on the use case, affected people, applicable law, and harm being measured.

## AI bias table

This table preserves the wiki's original diagnostic catalog while clarifying that mitigations are starting points, not guarantees.

| Bias type | Description | Example | Mitigation steps |
|---|---|---|---|
| **Sampling bias** | Training data does not represent the target population. | A facial-recognition dataset contains mostly light-skinned people. | Define the target population, use representative or stratified sampling, and test coverage and performance by relevant group. |
| **Selection bias** | Inclusion or exclusion rules systematically distort the dataset. | A hiring model is trained only on people who were previously hired. | Review selection criteria, include rejected or missing cases where lawful and appropriate, diversify sources, and audit outcomes. |
| **Historical bias** | Data reflects inequities or patterns from past decisions. | Historical hiring data teaches a screening model to favor men for engineering roles. | Document historical skews, reconsider labels and objectives, evaluate affected groups, and add policy constraints before deployment. |
| **Labeling bias** | Human annotations encode subjective or inconsistent judgments. | Toxicity labels vary across cultures or dialects. | Use clear guidance, multiple trained annotators, adjudication, inter-rater analysis, and subgroup review. |
| **Representation bias** | Groups or conditions are missing, scarce, or inaccurately portrayed. | A vision model performs worse on darker-skinned women because the dataset contains too few relevant examples. | Expand coverage across relevant people, contexts, devices, and edge cases; report remaining limits. |
| **Measurement bias** | A feature, label, or proxy does not measure the intended concept consistently. | Healthcare spending is used as a proxy for medical need despite unequal access to care. | Revisit the construct, validate proxies, compare measurement error by group, and use closer outcome measures. |
| **Confirmation bias** | Collection or interpretation favors an existing belief. | An investigator collects only evidence supporting a fraud hypothesis. | Predefine competing hypotheses, seek disconfirming evidence, use independent review, and run adversarial tests. |
| **Survivorship bias** | Failed, rejected, or otherwise missing cases are excluded. | A study of startup strategy analyzes only successful companies. | Identify the missing population and include negative outcomes and censored or rejected cases where possible. |
| **Automation bias** | People over-trust automated recommendations. | A clinician accepts an AI suggestion without checking contrary evidence. | Calibrate the interface, train users, expose uncertainty and evidence, monitor overrides, and require qualified review. |
| **Reporting bias** | Some events are more likely to be observed or reported. | A moderation model is trained only on posts users reported. | Estimate under-reporting, supplement reports with representative sampling, and compare reporting rates across groups. |
| **Aggregation bias** | One model or rule is applied to populations with materially different relationships. | A medical model is applied across populations despite different baseline risks or care pathways. | Test heterogeneity and subgroup calibration; use different models or policies only when evidence and governance support it. |
| **Evaluation bias** | Benchmarks do not reflect real users or deployment conditions. | A skin-cancer model looks accurate on a test set dominated by light-skin images but degrades in other clinics. | Build deployment-representative tests, report subgroup results and uncertainty, and validate prospectively. |
| **Temporal bias** | Data or behavior becomes outdated as conditions change. | A fraud model is trained only on pre-pandemic behavior. | Monitor drift, refresh data and tests, revalidate after change, and maintain rollback procedures. |
| **Popularity bias** | Frequently observed items dominate ranking or recommendation. | A recommender repeatedly promotes already popular products. | Measure catalog exposure, add exploration or diversity constraints, and evaluate long-tail outcomes. |
| **Proxy bias** | A seemingly neutral variable acts as a stand-in for a protected or sensitive attribute. | ZIP code correlates with race because of residential segregation. | Examine feature provenance and correlations, test counterfactual and subgroup behavior, restrict unjustified proxies, and review applicable law. |
| **Feedback-loop bias** | System decisions influence the future data used to train or evaluate the system. | Predictive policing sends more patrols to an area, creating more recorded incidents there. | Track interventions, use causal analysis where feasible, preserve independent samples, and audit downstream effects. |
| **Data-poisoning bias** | An actor intentionally manipulates data to shift model behavior. | Coordinated fake reviews alter recommendations. | Authenticate sources, track provenance, validate data, detect anomalies, limit write access, and maintain incident response. |
| **Deployment bias** | A system is used differently from its designed and evaluated purpose. | A decision-support score becomes the de facto decision without the intended human review. | Define use boundaries, train operators, enforce approval paths, monitor actual use, and stop unsupported deployments. |

These categories can overlap. For example, a selection process may create representation bias and then become a feedback loop after deployment.

## A practical review process

### 1. Define the decision and harm

Document who is affected, what the system recommends or changes, the cost of false positives and negatives, and which decisions require human authority.

### 2. Map data provenance

Record source, collection period, missingness, label creation, transformations, access basis, and known representation gaps. Synthetic data can supplement testing but does not automatically represent real populations.

### 3. Choose relevant slices

Evaluate groups that are legally, ethically, or operationally relevant. Include intersections where sample size permits. Do not infer sensitive attributes casually or publish slices that create re-identification risk.

### 4. Measure more than one outcome

Depending on the task, inspect false-positive and false-negative rates, calibration, error severity, ranking or allocation, abstention and escalation, retrieval coverage, and usability. Fairness metrics can conflict; selecting one is a policy decision tied to the deployment.

### 5. Test the whole system

Evaluate the model with its real instructions, retrieval, tools, thresholds, interface, and human review process. A model-card result does not establish the behavior of a different deployed system.

### 6. Apply layered controls

- Improve collection and labeling procedures.
- Revise objectives, prompts, retrieval, or thresholds.
- Add deterministic constraints and qualified review.
- Provide notice, explanation, appeal, and correction where appropriate.
- Restrict or stop uses whose risk cannot be acceptably controlled.

### 7. Monitor and respond

Track performance and complaints after deployment, define alert thresholds, investigate drift, preserve audit evidence, and maintain rollback and incident-response procedures.

## Generative and agentic-system considerations

Test paraphrases, dialects, languages, names, and role descriptions. For tool-using systems, examine whether different groups receive different retrieval coverage, tool selection, escalation, or approval outcomes.

Do not let the same model both make a high-impact decision and serve as its only fairness reviewer. Use independent data, deterministic analysis where possible, domain experts, affected-user input, and accountable human governance.

## Reporting template

```markdown
Use case and decision:
Affected population:
Deployment date and version:
Data sources and limitations:
Metrics and subgroup slices:
Known failure modes:
Human review and appeal path:
Monitoring thresholds:
Owner and next review date:
```

## Limits of mitigation

No checklist makes an AI system neutral. Technical metrics cannot decide which harms society should accept, and a fluent explanation is not evidence that a decision was fair. Some uses require domain-specific regulation, independent audit, or a decision not to deploy.

Return to [AI Terminology and FAQ](AI-Terminology-and-FAQ) or review [AI Claims and Misconceptions](AI-Claims-and-Misconceptions).

