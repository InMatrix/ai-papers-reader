---
layout: default
title: 2026-08-28
permalink: /2026-08-28/
---

# 2026-08-28

## AI for Software Development

### SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?

**Relevance:** This paper directly targets AI-assisted software development by introducing a benchmark for long-horizon, whole-repository code migration. It goes beyond pass/fail behavioral tests and audits whether coding agents actually perform the migration, addressing a key weakness in current code-generation evaluation. The benchmark covers four types of technical debt and uses agentic verification, making it highly relevant to research on AI tools for refactoring, maintenance, and large-scale code changes. It also has HCI implications: developers need trustworthy tools that perform genuine migrations rather than superficial test-passing workarounds.

💡 **[Summary](2608.23564/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.23564)**

### Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation

**Relevance:** This paper addresses UI-to-code generation, a direct application of generative AI to software development. It identifies a key failure mode, visual repair coupling, where local code edits cause regressions in previously faithful UI regions. RubSE uses typed rubrics and prioritized repair targets to guide self-evolution, improving stability across multiple VLMs. This is relevant to AI-assisted front-end development and to HCI because it targets the fidelity of visual interfaces and the iterative design/development loop between human designers and automated code generators.

💡 **[Summary](2608.24138/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.24138)**

### The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents

**Relevance:** Although centered on LLM agents, this paper is highly relevant to AI-assisted software development because coding agents are a primary use case. It studies what happens when a long-running coding trajectory is handed off between a cheaper, lower-capability model and a stronger, higher-cost model, showing a cost-quality penalty. The findings inform tool design for mixed-model developer workflows and interactive debugging, helping practitioners decide when to escalate or downshift models during real coding sessions. These handoff decisions are increasingly part of human-agent collaboration in IDEs.

💡 **[Summary](2608.24358/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.24358)**

## AI Agents

### PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents

**Relevance:** PILOT directly addresses the core AI-agent challenge of long-horizon autonomy. It introduces a supervisor-worker harness that enables live steering and self-evolution during execution, rather than only after a run finishes. The paper demonstrates substantial gains on Terminal-Bench and reduced token costs, showing how agent harnesses can learn from emerging experience. This is important for HCI because live steering gives humans/supervisors a practical mechanism to redirect agents in real time and build trust in autonomous systems.

💡 **[Summary](2608.26530/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.26530)**

### JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution

**Relevance:** This paper targets the agent harness—memory, planning, tool orchestration—and treats it as a trainable, transferable component. JIT-Agent synthesizes task-adaptive harnesses on the fly for off-the-shelf agentic LLMs, showing that harness design can be automated and evolve over time. This is directly relevant to AI-agent research because it expands the design space beyond model weights and offers a scalable route to improving agent behavior. It also has HCI implications: adaptively configured harnesses can better match tasks and user workflows.

💡 **[Summary](2608.25593/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.25593)**

### WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

**Relevance:** WikiSkill demonstrates how AI agents can progressively adapt by turning raw execution experience into a persistent wiki of accumulated knowledge and reusable skills. This directly addresses the agent topic's emphasis on learning from experience and maintaining memory. The framework separates experience, knowledge, and executable skills, enabling skill evolution that transfers across models. From an HCI perspective, persistent knowledge bases can make agent behavior more inspectable and support user-facing skill customization and debugging.

💡 **[Summary](2608.27454/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.27454)**

## LLM Evaluation Methods

### Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios

**Relevance:** This is a comprehensive evaluation benchmark for instruction following in MLLMs, a key element of LLM evaluation from an HCI perspective. It introduces a taxonomy of instruction types and constraint categories, including visual/audio-grounded constraints, and reveals that current models struggle with many-constraint and conditional instructions. The benchmark provides a reusable method for evaluating user-facing interactive systems, directly connecting model capability assessment to the kinds of natural-language requests people make in real video-understanding tasks.

💡 **[Summary](2608.25529/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.25529)**

### GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding

**Relevance:** GUI-Primitives is a diagnostic benchmark for evaluating vision-language models' spatial reasoning in graphical user interfaces, an area central to HCI. It uses contrastive instruction pairs to isolate whether models can bind relational language to interface elements. The results separate candidate localization from relation understanding and quantify failure modes, giving evaluation researchers a fine-grained methodology for assessing GUI agents. Human annotation validates the benchmark, aligning with human-in-the-loop evaluation and providing insights for improving accessible and reliable UI automation.

💡 **[Summary](2608.21832/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.21832)**

### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments

**Relevance:** This paper evaluates LLM-based Android GUI agents under realistic runtime anomalies, such as unexpected pop-ups and action misuse. It proposes a taxonomy of anomaly types and a benchmark that injects dynamic perturbations while preserving task solvability. The findings reveal universal vulnerability, with even strong models degrading significantly. This is directly relevant to LLM evaluation methods, especially robustness testing and human-AI interaction, because agents must remain reliable and recover gracefully in dynamic user-facing environments.

💡 **[Summary](2608.24099/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.24099)**

## Reinforcement Learning

### WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration and Exploitation

**Relevance:** WarpSAC is a core RL contribution that investigates how data regime changes the effectiveness of standard stabilizers in off-policy RL. It systematically studies exploration-exploitation trade-offs across massively parallel environments and proposes regime-aware algorithms that adapt stabilizers to data availability. The paper reports large gains on CPU/GPU simulated benchmarks and sim-to-real transfer, making it highly relevant to policy optimization and scalable RL. Its analysis of when to use parameter normalization or clipped double-Q is also useful for designing RL training pipelines.

💡 **[Summary](2608.24479/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.24479)**

### TTPO: Test-Time Policy Optimization

**Relevance:** TTPO presents a novel RL objective for test-time training of LLM reasoners without ground-truth labels. It combines on-policy self-distillation and grouped RL with an asymmetric treatment of agreeing/disagreeing rollouts, addressing pseudo-label noise. This is directly relevant to reinforcement learning research on policy optimization, reward design, and self-supervision. It also demonstrates how RL can be applied at test time to adapt models, which has implications for interactive systems where models need to improve from user interactions.

💡 **[Summary](2608.27448/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.27448)**

### Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

**Relevance:** This paper provides a systematic RL-focused analysis of Evolution Strategies as a post-training paradigm for LLM reasoning. It explains why ES can outperform GRPO in terms of reasoning coverage and Pass@K, relates diversity to verifier-projected Jensen-Shannon divergence, and reveals sparse parameter-update patterns. The work advances RL optimization knowledge by comparing gradient-free evolutionary approaches with policy-gradient methods, and it offers practical guidance on population sizing and hybrid GRPO-ES training. This is valuable for RL researchers seeking scalable, memory-efficient alternatives.

💡 **[Summary](2608.27351/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.27351)**

## Explainable AI

### A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans

**Relevance:** This paper is a strong XAI example because it replaces opaque end-to-end spatial reasoning in medical imaging with explicit stages: language parsing, anatomical localization, and deterministic geometric verification. The modular design yields auditable intermediate representations and interpretable rules, allowing clinicians and developers to inspect exactly how a spatial relation is verified. It outperforms direct VLM prompting while maintaining transparency. This directly supports explainable AI in high-stakes HCI contexts, where users need to trust and verify model reasoning.

💡 **[Summary](2608.21140/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.21140)**

