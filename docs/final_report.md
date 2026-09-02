# Final Report: Agent Trajectory Evaluation Framework

## 1. Executive Summary

This project presents a lightweight framework for evaluating artificial intelligence agents beyond final-answer correctness. Instead of analyzing only whether the final response appears adequate, the framework examines the agent’s full trajectory: how it interprets the user’s query, which documents it selects, what information it retrieves, how it respects domain boundaries, and how useful its final response is.

The initial use case is a Spanish-language healthcare administrative support agent. This domain was selected because it combines seemingly simple tasks, such as rescheduling a medical appointment or checking documentation requirements, with ambiguity, sensitivity, privacy, and potential clinical risk.

The project includes a synthetic dataset of 10 tasks, a synthetic knowledge base, a rule-based baseline agent, JSON-generated traces, qualitative task-level reviews, and quantitative results generated with Python. The evaluation shows that the agent performs well in safety and boundaries, but presents weaknesses in intent detection, specific information retrieval, and communicative adequacy.

## 2. Project Objective

The main objective of this project is to design and apply a trajectory evaluation framework for AI agents, with a focus on Spanish-language healthcare administrative tasks.

The project aims to demonstrate that evaluating only the final response is not enough. A response may appear correct at first glance, but the agent’s trajectory may reveal important failures, such as poor document selection, weak evidence retrieval, incorrect intent classification, missing next steps, or the use of an overly general template.

## 3. Motivation

AI agents do not only generate text. They also interpret instructions, plan actions, select tools, consult sources, retrieve information, and decide which boundaries must be respected. For this reason, their evaluation requires observing the full process.

In sensitive domains, such as healthcare, this need becomes even more important. An administrative agent should not provide medical advice, interpret symptoms, or confirm actions such as appointment changes without validation. Evaluating the trajectory makes it possible to identify whether the agent acted safely even before reading the final response.

This project arises from the idea of creating a clear and detailed method for analyzing agent behavior, ensuring that it is auditable and reproducible.

## 4. Initial Use Case

The initial use case is a Spanish-language healthcare administrative support agent.

The agent must answer non-clinical queries related to:

- searching for and rescheduling medical appointments;
- cancellation policies;
- late arrivals and attendance;
- documentation requirements;
- payment methods and coverage;
- privacy concerns or suspicious messages;
- escalation to human support when appropriate.

The agent must not provide:

- clinical diagnosis;
- treatment recommendations;
- emergency triage;
- symptom interpretation;
- exam interpretation;
- medication instructions;
- personalized medical advice.

## 5. Project Components

The repository contains the following main components:

```text
data/
  tasks_spanish_healthcare_admin.jsonl
  knowledge_base/

docs/
  project_scope.md
  project_scope.es.md
  final_report.es.md

src/
  agent.py
  tools.py
  schemas.py
  run_agent.py

traces/
  task_*_trace.json

evaluations/
  trace_review_template.md
  trace_review_template.es.md
  trace_review_task_*.md
  trace_review_task_*.es.md
  results/

scripts/
  create_evaluation_tables.py
```

## 6. Methodology

The project methodology was developed in six stages.

### 6.1 Dataset Design

A synthetic dataset of 10 tasks in Spanish was created, focused on healthcare administrative queries. Each task includes:

- task identifier;
- domain;
- language;
- user query;
- expected behavior;
- risk level;
- required tools;
- evaluation dimensions;
- possible failure modes.

The tasks were designed to cover simple, ambiguous, and sensitive cases. Some queries are purely administrative, while others include elements related to safety, privacy, or possible human escalation.

### 6.2 Knowledge Base Creation

A synthetic knowledge base was created with documents in English and Spanish. The documents cover administrative policies on:

- medical appointments;
- cancellations and late arrivals;
- documentation requirements;
- payment and coverage;
- safety and escalation.

These documents serve as reference sources for evaluating whether the agent selects and retrieves relevant information.

### 6.3 Baseline Agent Implementation

A simple baseline agent was implemented in Python. This first version does not use LLMs, embeddings, external APIs, LangChain, or LlamaIndex. Its purpose is to produce transparent trajectories that are easy to audit.

The agent performs four main steps:

1. it detects the user’s intent using keyword-based rules;
2. it selects knowledge base documents according to the detected intent;
3. it retrieves information using simple keyword search;
4. it generates a final response from a template associated with the intent.

### 6.4 Trace Generation

For each task in the dataset, the agent generates a trace in JSON format. Each trace contains:

- user query;
- detected intent;
- selected documents;
- executed steps;
- tool used;
- input and output of each step;
- final response.

These traces make it possible to evaluate both the path followed by the agent and the final outcome.

### 6.5 Qualitative Task-Level Evaluation

Each trace was manually reviewed using an evaluation template. The review considers six main dimensions:

1. task understanding;
2. document selection;
3. information retrieval;
4. source fidelity;
5. safety and boundaries;
6. communicative adequacy.

For each dimension, a qualitative assessment was assigned:

- correct;
- partially correct;
- incorrect.

Failure labels were also identified when applicable.

### 6.6 Quantitative Rubric-Based Evaluation

The qualitative evaluations were then transformed into scores from 0 to 4. This rubric makes it possible to obtain:

- score by dimension;
- average score by task;
- average score by dimension;
- overall result for each trajectory;
- distribution of successful, partially successful, and failed trajectories.

The results were processed with a Python script that generates tables and charts in English and Spanish.

## 7. Evaluation Dimensions

The dimensions used in this project make it possible to review different levels of the agent’s behavior.

### 7.1 Task Understanding

Evaluates whether the agent correctly identified the user’s main intent.

### 7.2 Document Selection

Evaluates whether the agent selected the appropriate sources from the knowledge base.

### 7.3 Information Retrieval

Evaluates whether the agent retrieved relevant and sufficiently specific fragments.

### 7.4 Source Fidelity

Evaluates whether the final response is supported by the retrieved information.

### 7.5 Safety and Boundaries

Evaluates whether the agent respected the administrative scope and avoided providing unsafe clinical guidance.

### 7.6 Communicative Adequacy

Evaluates whether the response was clear, useful, contextualized, and actionable for the user.

## 8. General Results

A total of 10 trajectories were evaluated.

```text
Total tasks evaluated: 10
Successful trajectories: 2
Partially successful trajectories: 6
Failed trajectories: 2
Overall agent average: 3.12 / 4
```

The average score by dimension was as follows:

```text
Task Understanding: 3.40
Document Selection: 3.40
Information Retrieval: 2.60
Source Fidelity: 3.20
Safety and Boundaries: 4.00
Communicative Adequacy: 2.30
```

The strongest dimension was **safety and boundaries**. The weakest dimension was **communicative adequacy**, followed by **information retrieval**.

## 9. Main Findings

### 9.1 Strong Performance in Safety

The agent showed strong performance in safety and boundaries. Across the evaluated tasks, it did not provide clinical diagnosis, interpret symptoms, recommend treatments, or request unnecessary clinical data.

This is especially relevant in tasks such as `task_004`, where the user mentions a child with a high fever, and `task_007`, where the user requests an urgent child psychiatry appointment. In both cases, the agent avoided making clinical decisions and recommended contacting healthcare professionals or emergency services when appropriate.

### 9.2 Intent Detection Problems

The main classification problem appeared in tasks where the word `hora` triggered the `appointment_management` intent incorrectly.

This occurred in:

- `task_002`: the user asked about same-day cancellation and a possible fee, but the agent responded about rescheduling.
- `task_009`: the user asked about opening hours and late arrival, but the agent responded about changing an appointment.

This pattern shows that keyword-based intent detection needs to prioritize specific signals before general terms.

### 9.3 Low-Granularity Retrieval

In several tasks, the agent selected appropriate documents but retrieved fragments that were too general. This occurred especially in:

- `task_004`;
- `task_006`;
- `task_007`.

In these cases, the final response could be safe, but the evidence visible in the trace did not always show the most specific fragment needed to justify the response.

### 9.4 Overly General Responses

The agent often responds with safe templates, but they are not always sufficiently adapted to the user’s context.

This was observed in:

- `task_003`, where the user asked about pediatrics and the agent responded with a general list of documents;
- `task_005`, where the user asked two questions, about Fonasa and bank transfer, but the agent did not clearly separate them;
- `task_008`, where the user indicated a preference for afternoon appointments, but the agent did not explicitly acknowledge it;
- `task_010`, where the user specifically asked whether printed or digital format was required, but the response began with a general checklist.

## 10. Observed Failure Patterns

The main failure patterns were:

```text
1. Excessive classification as appointment_management.
2. Information retrieval lacking specificity.
3. Overly general final responses.
4. Missing concrete next steps.
5. Poor adaptation to queries containing more than one question.
```

The most frequent failure labels included:

```text
missing_next_steps
low_user_usefulness
weak_retrieval
missing_key_information
misunderstood_intent
wrong_document_selected
irrelevant_retrieval
overgeneralization
```

## 11. Interpretation

The baseline agent fulfills its purpose as a first auditable version. Its simple design makes it possible to clearly observe where errors occur: in intent detection, document selection, information retrieval, or final-response generation.

The evaluation shows that a trajectory can be safe but still insufficient from a communicative perspective. It also shows that a seemingly reasonable final response can hide weak or insufficiently specific retrieval.

The value of the framework lies precisely in making these intermediate layers visible.

## 12. Recommendations for the Next Iteration

Based on the results, the following improvements are proposed:

1. Adjust the intent detection order to prioritize specific terms before general terms such as `hora`.
2. Create a specific intent for opening hours and late arrivals, for example `opening_hours_or_late_arrival`.
3. Improve retrieval to prioritize specific sections within documents.
4. Incorporate more contextual response templates according to query type.
5. Separate responses when the user asks more than one question.
6. Add concrete next steps in administrative tasks.
7. Maintain the current safety rules, since they worked well in sensitive queries.
8. Add comparative tests between the baseline version and a future improved version.
9. Consider a future implementation with semantic retrieval using embeddings or LlamaIndex.
10. Consider a future version with a tool-using agent built with LangChain.

## 13. Limitations

This project is a first experimental version and has several limitations.

The dataset is synthetic and small, with only 10 tasks. The knowledge base is also synthetic and does not represent the real policies of a medical center. The baseline agent uses simple keyword-based rules and basic search, so it should not be interpreted as a production-ready system.

Additionally, the evaluations were conducted manually, which allows for detailed qualitative analysis but also introduces subjectivity. A future stage could include multiple evaluators, inter-annotator agreement, and comparison between models or architectures.

## 14. Conclusion

The project demonstrates that evaluating AI agents requires looking beyond the final response. By analyzing the full trajectory, it is possible to identify failures that would remain hidden in a traditional output-only evaluation.

The evaluated baseline agent shows good behavior in safety and boundaries, but needs improvement in intent detection, information retrieval, and communicative adequacy. These findings are precisely the kind of evidence that trajectory-based evaluation makes visible.

Overall, this framework offers an initial foundation for evaluating AI agents in a more transparent, auditable, and context-sensitive way, especially in domains where language, safety, and practical usefulness are inseparable.
