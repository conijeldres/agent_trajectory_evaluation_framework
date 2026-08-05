# agent_trajectory_evaluation_framework
A lightweight framework to evaluate AI agents beyond final-answer correctness.


This project focuses on the full trajectory of an AI agent: how it understands a task, plans its actions, selects and uses tools, retrieves information, remains faithful to sources, respects safety boundaries, communicates with the user, and produces a useful final response.

## Current Implementation

The current version implements a simple rule-based baseline agent in Python.

It does not use LangChain, LlamaIndex, external LLM APIs, embeddings, or live healthcare systems. This is intentional: the first goal is to create transparent and auditable trajectories that can be evaluated before introducing more complex agent architectures.

Future versions may include a LlamaIndex-based retrieval layer or a LangChain tool-using agent for comparison.

## Initial Use Case

The first use case is a Spanish-language healthcare administrative support agent.

The agent handles non-clinical tasks such as appointment rescheduling, cancellation policies, documentation requirements, and escalation to human support when needed.

This domain was selected because it combines real-world ambiguity, user anxiety, procedural information, privacy concerns, and the need for clear, safe, and context-sensitive communication.

## Core Idea

Final-answer evaluation is not enough for AI agents.

A final response can appear correct while the agent may have selected the wrong tool, retrieved weak evidence, ignored ambiguity, violated a safety boundary, or followed an inefficient path.

This project proposes evaluating the full agent trajectory, not just the final answer.

## Evaluation Dimensions

1. Task Understanding
2. Planning Quality
3. Tool Selection
4. Tool Execution
5. Information Retrieval Quality
6. Source Fidelity
7. Safety & Boundaries
8. Communicative Adequacy
9. Efficiency
10. User Usefulness

## Language

This repository is documented in English and Spanish.

- [Spanish README](README.es.md)
- [Project Scope](docs/project_scope.md)
- [Alcance del proyecto](docs/project_scope.es.md)

## Status

Work in progress.
