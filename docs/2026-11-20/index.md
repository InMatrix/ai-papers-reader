---
layout: default
title: 2026-11-20
permalink: /2026-11-20/
---

# 2026-11-20

## AI for Software Development

### Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search

**Relevance:** Directly studies code search for coding agents, a core software-development task. It builds Repo-Premium, a realistic repository-level benchmark spanning six programming languages and real pull requests. It shows that a fair lexical baseline can match dense retrievers when queries are expanded with LLM-written identifiers, and derives practical guidelines such as fusing dense retrieval with BM25. These findings matter for how developers and agents locate code in real repositories.

💡 **[Summary](2611.20455/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.20455)**

### CompoundingKernel: Self-Improving from Zero to First

**Relevance:** An agent system that writes GPU kernels through search, which is a concrete form of AI-driven code generation and optimization. It uses an archive of correct kernels, an LLM controller that picks parents and designs, and external correctness checks. The paper's finding that the rate of reliable measurements, rather than the number of agents, limits scaling is a useful lesson for designing code-generation and verification pipelines.

💡 **[Summary](2611.19230/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.19230)**

## Harness Engineering

### Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments

**Relevance:** Builds a benchmark that embeds rules in work environments and measures how the agent's persistence scaffold leads to violations. It finds that violations often occur after the rule is displayed and that agents often write the rule down first. This gives observability-relevant evidence about how agent trajectories reveal decisions, supporting the governance and monitoring side of harness engineering.

💡 **[Summary](2611.17460/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.17460)**

## Human-in-the-Loop Evaluation

### AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators

**Relevance:** Provides a statistical test for deciding whether LLM annotators can replace human annotators when items are labeled by different annotator subsets. It mixes human and LLM annotations in bootstrap panels and compares inter-annotator agreement. This is a human-grounded evaluation methodology for auditing automated judges, and it addresses when human involvement can be safely reduced.

💡 **[Summary](2611.26073/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.26073)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests

**Relevance:** Evaluates a model fine-tuned on human browsing data that simulates 1,000 shoppers per arm to predict A/B test outcomes. Its predictions are checked against recorded live results, which directly measures simulator fidelity against real user behavior. It is a strong example of using simulated users for UX evaluation.

💡 **[Summary](2611.25200/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.25200)**

### S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive Experiments

**Relevance:** Benchmarks decision models on human-response prediction across established cognitive tasks and checks whether their choices look human-like under changing task demands. This directly assesses how faithfully these models stand in for human decision-makers. It also reveals failures that aggregate scores hide, which is important for judging when simulated users are valid.

💡 **[Summary](2611.00911/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.00911)**

### PlayCraft: Designing Engaging Games from Agent Play Experience

**Relevance:** Uses vision-based player agents with memory and learning-progression targets as stand-ins for learners to measure learning gain and slope in games. The simulated players drive design revisions, making this a use of persona-like agents for interaction design. Its fidelity to real human players is not validated, which limits how far the results transfer.

💡 **[Summary](2611.26624/)** 📄 **[Full paper](https://arxiv.org/pdf/2611.26624)**

