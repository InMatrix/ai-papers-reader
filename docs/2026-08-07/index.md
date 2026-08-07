---
layout: default
title: 2026-08-07
permalink: /2026-08-07/
---

# 2026-08-07

## AI for Software Development

### Self-Evolving Coding Agents

**Relevance:** This survey directly targets AI for software development by reviewing coding agents that inspect repositories, invoke tools, execute tests, debug failures, and generate patches. It proposes an object-centered taxonomy for self-evolving coding agents and examines how executable feedback, repository context, and coding trajectories let software engineering serve as a natural domain for agent self-improvement. The paper is relevant because it synthesizes methods for making generative coding assistants adaptive, updating memory, skills, tools, and models from prior interactions, which is central to using AI for code generation, bug fixing, refactoring, and maintenance.

💡 **[Summary](2608.03392/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.03392)**

## AI Agents

### OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents

**Relevance:** OneDayAgent addresses core AI-agent challenges in long-horizon, cross-environment, multimodal tasks. It turns open-ended everyday requests into a managed execution process that decomposes tasks into bounded subtasks, maintains execution memory under context pressure, and verifies or repairs final deliverables. The paper demonstrates a single harness managing goal drift, state loss, and context overflow across five backend LLMs. This is highly relevant to AI agents because it focuses on the harness-level infrastructure needed for autonomous agents to work reliably over many steps and heterogeneous tools.

💡 **[Summary](2608.05013/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.05013)**

### GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks

**Relevance:** GDPevo is an evolution-native benchmark for agent self-evolution, a key capability in AI-agent research. It uses rule hybridization to decompose enterprise workflows into atomic business rules and recombines them in held-out tasks so test-time gains can be attributed to prior experience. The benchmark covers CRM, ERP, finance, healthcare, legal, and data-centric workflows, and shows that self-evolution improves held-out accuracy, though current agents remain far below oracle performance. This is relevant because it provides a methodology for measuring whether agents can learn from experience and adapt to new tasks, central to AI-agent research.

💡 **[Summary](2608.03764/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.03764)**

### FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory

**Relevance:** FocusMem targets latent memory in GUI agents, separating content, readout, and trust in a compact memory interface. It enables episodic memory to retain reusable experience, working memory to track task progress, a state-conditioned readout to expose decision-specific views, and a trust gate to suppress irrelevant memory. These are exactly the memory mechanisms AI agents need to function across tasks and long interactions. The paper demonstrates consistent gains across five GUI-agent benchmarks and analyzes how semantic and functional supervision and trust gating contribute to robust agent behavior, making it highly relevant to AI-agent memory and tool-use research.

💡 **[Summary](2608.04530/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.04530)**

## LLM Evaluation Methods

### OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

**Relevance:** OSReward is a benchmark for evaluating VLM-based judges of computer-use agent trajectories. It systematically tests whether vision-language models can reliably verify whether a CUA trajectory fulfilled a task instruction, using realistic trajectories and ground-truth verdicts from multi-stage human annotation. The paper reveals that even state-of-the-art VLM judges have systematic leniency bias and that affordable open models lag far behind. This is directly relevant to LLM evaluation methods because it examines the reliability and cost trade-offs of using LLMs and VLMs as evaluators, a central concern for scalable human-in-the-loop and automated evaluation.

💡 **[Summary](2607.28609/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.28609)**

### What AI Red-Team Evaluations Can and Cannot Prove

**Relevance:** This paper provides a formal, calculable framework for understanding the evidential ceiling of red-team evaluations of AI models. It derives closed-form bounds for how much a benchmark result can move belief under a fixed testing budget and distinguishes regimes where clean benchmarks are strong evidence from regimes where feasible passive benchmarks cannot certify safety. It also applies the bound to adaptive and automated red-teaming. This is highly relevant to LLM evaluation methods because it clarifies what safety and capability evaluations can and cannot demonstrate, helping the community design benchmarks with appropriate evidentiary standards.

💡 **[Summary](2607.21735/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.21735)**

### SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in Multimodal Large Language Models

**Relevance:** SIGNPOST-Bench is a controlled counterfactual benchmark for evaluating how multimodal LLMs resolve conflicting text and visual evidence. It creates image quintuplets with original, blank, similar, random, and adversarial variants and injects localized scene-text interventions to measure changes in localization performance. The paper finds large shifts in predictions under conflicting text and shows that clean-input performance does not fully predict robustness. This is relevant to LLM evaluation methods because it offers a rigorous protocol for robustness testing and for assessing how models arbitrate between multiple evidence sources, a critical evaluation dimension.

💡 **[Summary](2608.04244/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.04244)**

## Reinforcement Learning

### AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

**Relevance:** AgentOPSD is a critic-free, recursive method for turn-level credit assignment in agentic reinforcement learning. It aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space, converting sparse outcome rewards into dense turn-level credit signals. This directly addresses a central RL challenge: credit assignment in long-horizon, multi-turn tasks. It is compatible with standard policy optimization and outperforms GRPO and self-distillation baselines across ALFWorld, WebShop, and Search-QA, making it highly relevant to improving policy optimization for RL agents.

💡 **[Summary](2608.05987/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.05987)**

### EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning

**Relevance:** EnvACE introduces world rehearsal for agentic reinforcement learning: instead of interacting with external environments during training, the policy alternates between generating tool calls and playing the role of the environment to produce responses. This lets the model internalize action-response dynamics in its parameters, producing an agent world model that directly supports decision making. The method is jointly optimized end-to-end with task-success rewards and outperforms environment-scaling baselines across tool-use benchmarks. This is relevant to RL because it rethinks the interaction loop and environment design, enabling scalable policy learning beyond external environment constraints.

💡 **[Summary](2608.06197/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.06197)**

### Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from Adaptive Teacher Guidance

**Relevance:** This paper addresses a known failure of GRPO in reinforcement learning with verifiable rewards: when all responses in a group receive identical rewards, gradients vanish. It proposes RSTG, which applies on-policy distillation selectively to negative zero-variance prompts and targets only high-entropy or high-divergence tokens, while also injecting SFT on correct teacher trajectories. This is directly relevant to RL methods for LLMs because it combines policy optimization with dense teacher guidance to recover learning signals that RL alone misses, improving math and code reasoning over naive GRPO plus OPD baselines.

💡 **[Summary](2608.00782/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.00782)**

## Explainable AI

### Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval

**Relevance:** This paper builds an interpretable deep network for MEG-to-audio retrieval by redesigning the front end and decoder so that weights map to cortical sources. The spatial attention operates on spherical harmonics over the 3D MEG helmet geometry, and branch filters are matched to neuronal sources in space and time. By mapping weights to source space and performing paired MEG occlusion, the authors identify which stimulus features drive retrieval, such as silence, intensity, vowels, and onsets. This exemplifies explainable AI: connecting model representations to neuroscientifically meaningful quantities and revealing what the model uses for prediction.

💡 **[Summary](2608.01481/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.01481)**

