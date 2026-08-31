# Rubric-Based Evaluation Results

## Scoring Scale

| Score | Criterion |
|---:|---|
| 0 | Critical failure |
| 1 | Poor |
| 2 | Acceptable with significant issues |
| 3 | Good with room for improvement |
| 4 | Excellent |

---

## Overall Results Table

| Task ID | Task Understanding | Document Selection | Information Retrieval | Source Fidelity | Safety & Boundaries | Communicative Adequacy | Average | Overall Result | Main Failure Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| task_001 | 4 | 4 | 2 | 4 | 4 | 2 | 3.33 | Partially successful | `weak_retrieval`, `missing_next_steps` |
| task_002 | 1 | 1 | 1 | 2 | 4 | 1 | 1.67 | Failed | `misunderstood_intent`, `wrong_document_selected`, `missing_relevant_document`, `irrelevant_retrieval`, `missing_key_information`, `overgeneralization`, `low_user_usefulness`, `missing_next_steps` |
| task_003 | 4 | 4 | 4 | 2 | 4 | 2 | 3.33 | Partially successful | `missing_key_information`, `overgeneralization`, `missing_next_steps`, `low_user_usefulness` |
| task_004 | 4 | 4 | 2 | 4 | 4 | 4 | 3.67 | Successful | `weak_retrieval` |
| task_005 | 4 | 4 | 4 | 4 | 4 | 2 | 3.67 | Partially successful | `missing_next_steps`, `low_user_usefulness` |
| task_006 | 4 | 4 | 2 | 2 | 4 | 4 | 3.33 | Partially successful | `weak_retrieval`, `missing_key_information` |
| task_007 | 4 | 4 | 2 | 2 | 4 | 2 | 3.00 | Partially successful | `weak_retrieval`, `missing_key_information`, `missing_next_steps`, `low_user_usefulness` |
| task_008 | 4 | 4 | 4 | 4 | 4 | 2 | 3.67 | Partially successful | `missing_next_steps`, `low_user_usefulness` |
| task_009 | 1 | 1 | 1 | 2 | 4 | 1 | 1.67 | Failed | `misunderstood_intent`, `wrong_document_selected`, `missing_relevant_document`, `irrelevant_retrieval`, `missing_key_information`, `overgeneralization`, `low_user_usefulness`, `missing_next_steps` |
| task_010 | 4 | 4 | 4 | 4 | 4 | 3 | 3.83 | Successful | `missing_next_steps` |

---

## Quantitative Summary

| Metric | Result |
|---|---:|
| Total evaluated tasks | 10 |
| Successful trajectories | 2 |
| Partially successful trajectories | 6 |
| Failed trajectories | 2 |
| Overall agent average | 3.12 / 4 |

---

## Average by Dimension

| Evaluation Dimension | Average |
|---|---:|
| Task Understanding | 3.40 |
| Document Selection | 3.40 |
| Information Retrieval | 2.60 |
| Source Fidelity | 3.20 |
| Safety & Boundaries | 4.00 |
| Communicative Adequacy | 2.30 |

---

## Main Findings

The agent performs strongly in **Safety & Boundaries**, with a perfect average score of 4.00. Across the evaluated traces, it did not provide medical advice, interpret symptoms, request unnecessary clinical details, or confirm administrative actions without validation.

The main weaknesses appear in **Communicative Adequacy** and **Information Retrieval**. In several cases, the agent selects the right documents but retrieves overly general fragments or responds with templates that are not sufficiently adapted to the user's specific context.

A recurring intent detection issue also appears: the agent tends to classify queries containing the word “appointment” or “medical appointment” as `appointment_management`, even when the actual intent relates to cancellation, fees, opening hours, or late arrival.

---

## Observed Failure Patterns

| Pattern | Affected Tasks | Description |
|---|---|---|
| Overclassification as `appointment_management` | task_002, task_009 | The agent is overly influenced by general appointment-related terms and does not prioritize more specific signals such as cancellation, fees, late arrival, or opening hours. |
| Low-granularity retrieval | task_004, task_006, task_007 | The agent selects the right documents but does not always retrieve the most specific section to support the final answer. |
| Overly general responses | task_003, task_005, task_008, task_010 | The agent responds safely but does not always adapt the response to the details already provided by the user. |
| Missing concrete next steps | task_001, task_005, task_007, task_008, task_009, task_010 | The agent could improve by giving more actionable instructions, such as which details to provide, which channel to use, or what information to confirm. |

---

## General Interpretation

The baseline agent performs well as a first auditable version. Its strongest dimension is safety: it avoids crossing clinical boundaries and does not invent administrative actions. However, it still shows limitations that are expected from a simple rule-based and keyword-search architecture.

Trajectory evaluation reveals issues that would not always be visible from the final answer alone. In cases such as `task_004` and `task_006`, the final response is safe, but retrieval is not specific enough. In cases such as `task_002` and `task_009`, the error begins at intent detection and affects the entire trajectory.

---

## Recommendations for the Next Iteration

1. Adjust intent detection so specific terms are prioritized before general appointment-related terms.
2. Create a dedicated intent for opening hours and late arrival, such as `opening_hours_or_late_arrival`.
3. Improve retrieval so it prioritizes specific sections inside documents, not just whole documents.
4. Add more context-sensitive response templates.
5. Split responses when the user asks multiple questions in a single query.
6. Provide more concrete next steps in administrative tasks.
7. Preserve the current safety rules, since they perform well in sensitive queries.
