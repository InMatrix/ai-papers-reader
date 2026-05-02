---
layout: default
title: 2026-03-27
permalink: /2026-03-27/
---

# 2026-03-27

## AI for Software Development

### Understanding the Challenges in Iterative Generative Optimization with LLMs

**Relevance:** This paper investigates generative optimization, where LLMs iteratively improve artifacts like code and workflows based on execution feedback. From an HCI perspective, it highlights the 'hidden' design choices engineers must make—such as selecting the right learning evidence and starting artifacts—which currently make these systems brittle. Understanding these human-in-the-loop design factors is essential for creating reliable AI assistants for software development. The study provides practical guidance to improve the adoption of self-optimizing code agents, bridging the gap between automated optimization and developer-centric tool design.

💡 **[Summary](2603.23994/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.23994)**

## AI Agents

### StreamingClaw Technical Report

**Relevance:** StreamingClaw is a unified framework for streaming video understanding and embodied intelligence. It addresses key HCI and ML challenges by integrating real-time reasoning, long-term multimodal memory, and proactive interaction. By supporting a perception-decision-action closed loop, it enables agents to interact naturally with real-world environments. This research is highly relevant to HCI as it focuses on creating agents that can sustain perception and execute actions in dynamic contexts, facilitating more intuitive and responsive human-agent collaboration in both digital and physical spaces.

💡 **[Summary](2603.22120/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.22120)**

### CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents

**Relevance:** Progress in general-purpose computer-use agents (CUAs) is often limited by a lack of high-quality interaction data. CUA-Suite provides a massive corpus of human-demonstrated tasks with continuous video and kinematic cursor traces. This dataset allows researchers to study the temporal dynamics of human-computer interaction, enabling agents to learn complex desktop workflows. By providing dense annotations and a rigorous benchmark (UI-Vision), it facilitates the development of agents that better understand user intent and spatial control within professional software environments, bridging the gap between raw video perception and actionable UI control.

📄 **[Full paper](https://arxiv.org/pdf/2603.24440)**

### STEM Agent: A Self-Adapting, Tool-Enabled, Extensible Architecture for Multi-Protocol AI Agent Systems

**Relevance:** STEM Agent introduces a modular architecture inspired by biological pluripotency, where an undifferentiated core specializes into protocol handlers and tool bindings. This is highly relevant to HCI as it includes a 'Caller Profiler' that learns user preferences across twenty behavioral dimensions and a skill acquisition system where interaction patterns crystallize into reusable skills. By unifying multiple interaction protocols and focusing on long-term memory consolidation, the framework provides a foundation for more personalized and extensible agentic systems that adapt to individual user workflows and diverse digital environments.

💡 **[Summary](2603.22359/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.22359)**

## LLM Evaluation Methods

### Qworld: Question-Specific Evaluation Criteria for LLMs

**Relevance:** Evaluating LLMs on open-ended questions is difficult because quality is highly context-dependent. Qworld introduces a method to generate question-specific evaluation criteria using a recursive expansion tree, covering scenarios and perspectives that static rubrics miss. This approach aligns with HCI goals of nuanced evaluation, as it reveals capability differences in dimensions like equity, error handling, and interdisciplinary reasoning. By moving toward adaptive, question-level criteria, Qworld provides a more robust framework for assessing how well models meet diverse user needs and handle complex, real-world reasoning tasks effectively.

💡 **[Summary](2603.23522/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.23522)**

### T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search

**Relevance:** T-MAP proposes a trajectory-aware evolutionary search method to red-team LLM agents, specifically focusing on vulnerabilities that emerge during multi-step tool execution. Unlike traditional text-based red-teaming, this method evaluates the safety of agent actions within tool-use ecosystems like the Model Context Protocol. From an HCI perspective, this is crucial for building trust and safety in autonomous systems. By automatically discovering adversarial prompts that bypass guardrails through actual tool interactions, T-MAP helps researchers identify and mitigate underexplored risks in the interaction loops between agents and digital environments.

💡 **[Summary](2603.22341/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.22341)**

### GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents

**Relevance:** GameplayQA provides a framework for evaluating agentic perception and reasoning through first-person video understanding in 3D environments. It uses densely annotated multiplayer gameplay to test if models can attribute actions to correct entities and reason about concurrent behaviors. This benchmark is vital for HCI as it identifies where models hallucinate in decision-dense scenarios. By highlighting failures in temporal grounding and agent-role attribution, GameplayQA guides the development of more reliable virtual agents that can better understand and interact with humans and other agents in complex virtual worlds.

💡 **[Summary](2603.24329/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.24329)**

## Reinforcement Learning

### EVA: Efficient Reinforcement Learning for End-to-End Video Agent

**Relevance:** EVA introduces an efficient RL framework for video agents, utilizing a pipeline that includes Kahneman-Tversky Optimization (KTO) and Generalized Reward Policy Optimization (GRPO). The agent learns to 'plan-before-perception,' autonomously deciding what and when to watch to solve queries. This is relevant to HCI as it explores how agents can be trained to reason adaptively rather than passively. The use of RL to bridge supervised imitation and autonomous planning offers insights into creating agents that can efficiently navigate long-context visual environments while maintaining high performance on video understanding tasks.

💡 **[Summary](2603.22918/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.22918)**

### When Models Judge Themselves: Unsupervised Self-Evolution for Multimodal Reasoning

**Relevance:** This paper proposes an unsupervised self-evolution framework that uses Group Relative Policy Optimization (GRPO) to improve multimodal reasoning. By using the actor's self-consistency as a training prior and incorporating a bounded judge-based modulation, the model learns to reweight reasoning trajectories without human-annotated answers. This is a significant advancement in RL, as it provides a scalable path for models to improve their reasoning capabilities autonomously. From an HCI standpoint, this self-evolution reduces the need for costly human labeling while potentially improving the consistency and reliability of AI-generated reasoning.

💡 **[Summary](2603.21289/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.21289)**

### Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs

**Relevance:** This study performs a systematic empirical analysis of Reinforcement Learning with Verifiable Rewards (RLVR). It identifies that RL fine-tuning induces highly sparse, targeted changes at the token level that are responsible for significant reasoning gains. By using cross-sampling interventions, the authors isolate the specific decisions that drive performance. This research benefits both RL and HCI by providing a granular understanding of how RL fine-tuning actually modifies model behavior, offering a 'targeted refinement' lens that can help designers create more predictable and controllable RL-based training processes for reasoning tasks.

💡 **[Summary](2603.22446/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.22446)**

## Explainable AI

### Reasoning or Rhetoric? An Empirical Analysis of Moral Reasoning Explanations in Large Language Models

**Relevance:** This paper critiques the transparency of LLM reasoning by investigating whether their moral explanations reflect genuine developmental logic or merely 'moral ventriloquism' produced by alignment training. It identifies 'moral decoupling'—systematic inconsistencies between stated justifications and actual action choices—which serves as a critical diagnostic for logical incoherence. For HCI, this work is vital for building trust and interpretability, as it warns against relying on sophisticated rhetoric and provides methods to detect when a model's stated reasoning does not align with its underlying decision-making processes in sensitive moral domains.

💡 **[Summary](2603.21854/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.21854)**

### Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?

**Relevance:** This research explores why self-distillation can harm the reasoning performance of LLMs despite shortening reasoning traces. The authors trace this degradation to the suppression of 'epistemic verbalization'—the model's expression of uncertainty. From an XAI perspective, this highlights that transparently exposing uncertainty is crucial for robust reasoning, especially in out-of-distribution scenarios. The findings suggest that optimizing for concise 'correct' traces at the expense of uncertainty markers can make models less interpretable and more brittle, emphasizing the need for evaluation metrics that value the model's internal reasoning health over mere output length.

💡 **[Summary](2603.24472/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.24472)**

