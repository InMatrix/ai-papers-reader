---
layout: default
title: 2026-10-09
permalink: /2026-10-09/
---

# 2026-10-09

## AI for Software Development

### TestPrism: Rethinking Test Evaluation Beyond a Single Reference

**Relevance:** Directly addresses LLM coding agents that generate tests, a core software-development task. It shows that single-reference evaluation overstates test quality and introduces a stricter metric (Joint Success Function) that checks tests against both valid and invalid implementations. It also proposes TestHelix, which pairs test synthesis with repair and peer cross-validation. This is relevant to AI-assisted testing and debugging workflows where developers need trustworthy generated tests.

💡 **[Summary](2610.12289/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.12289)**

## Harness Engineering

### Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution

**Relevance:** Focuses on optimizing the operational scaffold of deployed AI systems (prompts, skills, harnesses, code) rather than model weights. It evaluates harness optimization on TerminalBench 2.1 and compares against harness-improvement methods such as AHE and Meta-Harness. Its refinement loop over rejected candidates is relevant to making harness iteration more efficient, although it is largely automated and does not center on human steering.

💡 **[Summary](2609.35855/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.35855)**

### Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict

**Relevance:** Analyzes agent behavior at the trajectory level (Identify, Solve, Escalate), which supports the observability goal of making agent decisions visible. It concludes that epistemic humility emerges from the interaction of the backbone model, agent harness, and evaluation environment, which motivates harness-level inspection and repair. The paper gives concrete diagnostic dimensions for auditing agent behavior.

💡 **[Summary](2610.12360/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.12360)**

## Human-in-the-Loop Evaluation

### TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows

**Relevance:** Proposes an MLLM-driven evaluation pipeline and explicitly validates it by correlation with human judgments of world consistency. It shows that conventional metrics can miss failures humans notice, which makes it a useful case for hybrid pipelines where automated judges are calibrated against people. Its taxonomy of violation types could also support expert annotation protocols.

💡 **[Summary](2610.02959/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.02959)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### Do LLMs Understand Sequential Structure? A Controlled Study of Inference and Generation

**Relevance:** Examines whether LLMs can serve as behavioral simulators of interactive agents, using controlled two-player Rock-Paper-Scissors and n-gram continuation tasks. It shows that apparent behavioral fidelity can mask incorrect generative mechanisms, which is a direct caution about using LLM stand-ins for users. The distinction between distribution matching and rule following is useful for assessing simulator validity.

💡 **[Summary](2610.04977/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.04977)**

