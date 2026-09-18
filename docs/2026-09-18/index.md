---
layout: default
title: 2026-09-18
permalink: /2026-09-18/
---

# 2026-09-18

## AI for Software Development

### An Empirical Study of Harness Design for Coding Agents

**Relevance:** This paper directly investigates how different harness components—planning, action space, and context management—affect autonomous coding agents on software engineering benchmarks like SWE-Bench Verified and Terminal-Bench. It provides component-level comparisons and trajectory-level analysis, offering actionable insights for designing AI assistants that help developers with long-horizon coding tasks. Its focus on coding agent performance and harness design makes it highly relevant to AI for software development, especially for understanding how to configure agents for code generation, debugging, and repository-level tasks.

💡 **[Summary](2609.20804/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.20804)**

### ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks

**Relevance:** This paper introduces a benchmark for coding agents that must infer desired behavior by interacting with fully functional reference applications, then implement features in incomplete web apps. It evaluates frontier coding agents on reconstruction tasks, with controlled difficulty. This directly addresses AI for software development, particularly code generation from interactive examples and web development tasks. The benchmark and diagnostic insights can guide future training and evaluation of AI coding assistants in realistic software engineering settings.

💡 **[Summary](2609.18805/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.18805)**

### SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

**Relevance:** This work scales auto-research loops for coding agents to improve token efficiency and harness design. It targets long-horizon software engineering tasks where agents reason, use tools, and receive feedback. By optimizing action execution, context compaction, observation handling, and delegated reading, SoL-Pi reduces token traffic and cost while maintaining performance on EdgeBench. It is relevant to AI for software development because it studies how to make coding agents more efficient and production-ready for unattended software engineering workflows.

💡 **[Summary](2609.20519/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.20519)**

## Harness Engineering

### An Empirical Study of Harness Design for Coding Agents

**Relevance:** This paper is a direct empirical study of harness design for coding agents. It varies planning, action space, and context management across 176 matched settings and four models, measuring effects on SWE-Bench and Terminal-Bench. The trajectory-level analysis explains how each component shapes agent behavior. This provides a modular framework for evaluating and designing harness components, making it highly relevant to harness engineering, especially for understanding how context management and tool interfaces affect agent reliability and cost.

💡 **[Summary](2609.20804/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.20804)**

### SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

**Relevance:** SoL-Pi operates at the harness layer, scaling auto-research loops to discover reusable improvements for coding agents. Four mechanisms span action execution, context compaction, observation handling, and delegated reading. It reduces token traffic and API cost while maintaining performance. This is a clear harness-engineering contribution: it designs and iterates the operational scaffold around a foundation model to make agent systems more efficient and reliable in production-like environments.

💡 **[Summary](2609.20519/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.20519)**

### Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents

**Relevance:** This paper introduces EvoSkill-GUI, a training-free framework where skills are structured multi-file packages containing retrieval metadata, executable plans, failure-recovery rules, and failure cases. It uses a reflect-revise-reuse loop with an isolated critic to edit skill files from execution feedback. This is harness engineering because it treats skills as editable artifacts that improve through deployment, making agent behavior more observable and adaptable without retraining.

📄 **[Full paper](https://arxiv.org/pdf/2609.17653)**

## Human-in-the-Loop Evaluation

### VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering

**Relevance:** This paper introduces a Telugu spoken factoid QA benchmark with human-verified reference answers. It validates automatic evaluation against human judgments, finding that Gemini-as-a-judge best approximates human ratings but is non-uniformly strict. The study is a human-in-the-loop evaluation contribution: it uses human verification to calibrate and critique automatic judges, then benchmarks models across modalities and domains. It shows how human judgments are essential for reliable evaluation in low-resource, spoken-language settings.

💡 **[Summary](2609.19879/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.19879)**

### RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation

**Relevance:** This benchmark evaluates models on restoring obfuscated platform messages and then investigating associated websites. It pairs synthetic restoration inputs with human-labeled local web environments, and human labels determine task correctness. A fixed multimodal evidence judge assesses report faithfulness. By centering human-labeled ground truth for a complex web investigation task, it contributes a human-in-the-loop evaluation methodology for high-stakes content moderation and risk assessment.

💡 **[Summary](2609.16900/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.16900)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

No paper recommendations for this topic.

