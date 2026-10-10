---
layout: default
title: 2026-08-21
permalink: /2026-08-21/
---

# 2026-08-21

## AI for Software Development

### SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?

**Relevance:** Introduces a repository-level benchmark of 119 scientific software engineering tasks and analyzes why coding agents fail, including failure mechanisms and the effect of scientific guidance. This directly addresses how LLM coding agents repair real software, and its failure analysis and paired ablation offer lessons for designing and debugging developer-facing coding assistants.

💡 **[Summary](2608.19799/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.19799)**

### SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation

**Relevance:** Applies LLM code generation to industrial PLC programming within an existing project, gating task completion on compilation and live-runtime execution checks. It shows that execution-based verification, rather than model self-judgment, is a more faithful test of generated code, which is useful for developer tooling that must be trusted.

💡 **[Summary](2608.18565/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.18565)**

### Repo0: Design-Driven Zero-to-All Code Generation

**Relevance:** Generates entire software repositories from natural-language requirements by maintaining an explicit, modular architecture (Dual-DAG) that guides test-driven code generation. The explicit architectural state could support developers in inspecting and steering AI-generated project structure.

💡 **[Summary](2608.19854/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.19854)**

## Harness Engineering

### SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation

**Relevance:** Presents an explicit agent harness with a governing completion rule and logged external checks (specification, compilation, live runtime behavior). It treats the harness itself as the design artifact and makes agent completion decisions auditable, closely matching harness engineering concerns.

💡 **[Summary](2608.18565/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.18565)**

## Human-in-the-Loop Evaluation

### VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio Generation

**Relevance:** Builds a human-preference dataset (VAPref-10K) with fine-grained paired comparisons and validates a reward model against human annotations via rejection sampling. It is a clear example of human preference collection used to calibrate an automated judge.

💡 **[Summary](2608.18607/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.18607)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback

**Relevance:** Recasts multi-turn user simulation as a feedback generator, where simulated follow-up questions expose defects across turns to drive agent skill revision. It directly studies how simulated users can supply trustworthy feedback signals and compares them against single-turn evaluation.

💡 **[Summary](2608.13120/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.13120)**

