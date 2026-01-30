---
layout: default
title: 2026-01-02
permalink: /2026-01-02/
---

# 2026-01-02

## AI for Software Development

### KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta

**Relevance:** KernelEvolve is an agentic framework designed for automated kernel generation and optimization across heterogeneous hardware. This falls squarely under AI for Software Development, focusing on automating complex, performance-critical coding tasks (code generation/refactoring). From an HCI perspective, this tool drastically changes the workflow of specialized engineers, reducing development time from weeks to hours, necessitating studies on trust, control, and the interaction design of such highly automated coding agents.

💡 **[Summary](2512.23236/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.23236)**

### GraphLocator: Graph-guided Causal Reasoning for Issue Localization

**Relevance:** GraphLocator addresses the challenging software engineering task of issue localization, which is crucial for automated bug detection and fixing. By mitigating the semantic gap between natural language issue descriptions and source code, it directly improves the utility of AI in software development workflows. HCI research could focus on how developers interact with the resulting "causal issue graph" (CIG) to understand complex dependencies and verify the AI's causal reasoning before implementing fixes, enhancing transparency and trust in automated debugging tools.

💡 **[Summary](2512.22469/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.22469)**

### Shape of Thought: When Distribution Matters More than Correctness in Reasoning Tasks

**Relevance:** This paper explores how the internal reasoning process (Chain-of-Thought traces) influences performance in tasks including code generation (MBPP). The finding that the distribution of reasoning steps matters more than final correctness suggests that future AI coding tools should prioritize generating high-quality, readable intermediate steps. for HCI, this implies that the interpretability of the AI's *process* (the "shape of thought") is vital for user adoption and debugging, reinforcing the need for research into how developers consume and trust intermediate AI reasoning during code synthesis.

💡 **[Summary](2512.22255/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.22255)**

## AI Agents

### AI Meets Brain: Memory Systems from Cognitive Neuroscience to Autonomous Agents

**Relevance:** This paper directly tackles a foundational component of sophisticated AI Agents: memory systems. By synthesizing insights from cognitive neuroscience and applying them to LLM-driven agents, it provides a crucial roadmap for building more human-aligned and robust agents. HCI implications are vast, focusing on how humans can understand, inspect, and manage agents whose behavior is governed by complex, bio-inspired memory architectures, particularly concerning trust, security, and long-term interaction coherence.

💡 **[Summary](2512.23343/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.23343)**

### Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem

**Relevance:** This work introduces ROME, an open-source agent model, and the Agentic Learning Ecosystem (ALE) specifically designed for "agentic crafting" in real-world environments. This accelerates the development of complex, autonomous agents. HCI research is critical here to design effective interfaces for monitoring, intervening, and controlling agents operating in sandbox environments (ROCK) and managing long-horizon tasks, especially given the novel Interaction-based Policy Alignment (IPA) used for stable training.

💡 **[Summary](2512.24873/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.24873)**

### Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models

**Relevance:** Youtu-LLM demonstrates that strong intrinsic agentic capabilities (reasoning, planning, tool-use) can be cultivated in lightweight LLMs (sub-2B). This has significant implications for deploying advanced AI agents on edge devices or in resource-constrained environments. From an HCI perspective, enabling complex agent functionality locally opens up new interaction possibilities, requiring studies on how users perceive the reliability and responsiveness of lightweight, on-device agents compared to cloud-based counterparts.

💡 **[Summary](2512.24618/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.24618)**

## LLM Evaluation Methods

### Introducing TrGLUE and SentiTurca: A Comprehensive Benchmark for Turkish General Language Understanding and Sentiment Analysis

**Relevance:** TrGLUE and SentiTurca address a critical gap in LLM evaluation by providing comprehensive, linguistically natural benchmarks for Turkish NLU. This directly supports the LLM Evaluation Methods topic by establishing standardized assessment tools in a non-English domain. Furthermore, the semi-automated dataset creation pipeline (combining LLM annotation, cross-model checks, and human validation) is itself a novel method for scaling human-in-the-loop evaluation efforts, ensuring robustness and minimizing bias often found in translated datasets.

💡 **[Summary](2512.22100/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.22100)**

### Video-BrowseComp: Benchmarking Agentic Video Research on Open Web

**Relevance:** Video-BrowseComp is a novel benchmark designed to evaluate the complex, proactive reasoning required of AI agents when conducting open-ended research involving video evidence. This evaluation goes beyond standard accuracy metrics, assessing the agent's ability to navigate, cross-reference, and temporally ground information. This directly relates to HCI concerns about system trustworthiness and usability, as models fail when textual proxies collapse, highlighting the need for evaluation methods that focus on robust visual grounding essential for reliable human-agent collaboration.

💡 **[Summary](2512.23044/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.23044)**

### Valori: A Deterministic Memory Substrate for AI Systems

**Relevance:** Valori introduces a deterministic memory substrate crucial for trustworthy AI systems by eliminating non-determinism caused by floating-point operations. This is highly relevant to LLM Evaluation Methods, particularly robustness testing and audit trails, which are necessary for deployment in regulated sectors. From an HCI perspective, guaranteeing bit-identical replayability across platforms is foundational for user trust and verifying model behavior post-hoc, ensuring that observed failures or successes are reproducible and attributable.

💡 **[Summary](2512.22280/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.22280)**

## Reinforcement Learning

### Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation

**Relevance:** Robo-Dopamine addresses the core RL challenge of designing effective reward functions for complex robotic manipulation. It introduces a General Reward Model and a Policy-Invariant Reward Shaping method, leading to highly efficient policy learning (near-zero to 95% success in 1 hour). This is highly relevant to HCI in RL, as efficient learning minimizes the data and time cost for human supervisors/operators who provide initial demonstrations or feedback, thereby facilitating intuitive and rapid human guidance of agent learning in real-world physical tasks.

💡 **[Summary](2512.23703/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.23703)**

### PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation

**Relevance:** PhyGDPO applies Reinforcement Learning (specifically preference optimization) to guide generative models toward physical consistency, a challenging aspect of T2V generation. It uses a Physics-Guided Rewarding scheme derived from a Vision-Language Model. This demonstrates RL's role in aligning complex generative outputs with automated, objective constraints (physics). HCI considerations arise in how preference optimization, usually driven by human feedback, is transferred to automated constraints, and how this affects user control and predictability in content creation.

📄 **[Full paper](https://arxiv.org/pdf/2512.24551)**

### Evaluating Parameter Efficient Methods for RLVR

**Relevance:** This paper provides a systematic evaluation of Parameter-Efficient Fine-Tuning (PEFT) methods within Reinforcement Learning with Verifiable Rewards (RLVR). This research is crucial for scaling RL methods efficiently. From an HCI perspective, RLVR relies on verifiable feedback, often provided by human-designed systems or human verification steps. Optimizing the underlying training efficiency ensures that human feedback cycles are utilized maximally, potentially leading to faster adaptation and more stable agents, improving the feasibility of human-in-the-loop RL systems.

💡 **[Summary](2512.23165/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.23165)**

## Explainable AI

### Fantastic Reasoning Behaviors and Where to Find Them: Unsupervised Discovery of the Reasoning Process

**Relevance:** This paper introduces RISE, an unsupervised framework for discovering and controlling internal "reasoning behaviors" in LLMs using Sparse Auto-Encoders. This is a cutting-edge XAI method that provides fine-grained interpretability by identifying vectors corresponding to behaviors like reflection and confidence. This has profound HCI implications, enabling developers to controllably steer inference trajectories and providing users with explanations based on the model's high-level cognitive steps, enhancing trust and debugging capabilities far beyond simple input feature importance.

📄 **[Full paper](https://arxiv.org/pdf/2512.23988)**

### GateBreaker: Gate-Guided Attacks on Mixture-of-Expert LLMs

**Relevance:** While presenting an attack framework, GateBreaker contributes significantly to XAI by localizing and analyzing safety mechanisms within Mixture-of-Expert (MoE) LLMs. The finding that safety alignment concentrates in a small, identifiable subset of neurons provides crucial insight into MoE model functioning. This interpretability is vital for HCI, allowing developers to design targeted defense and monitoring systems. Understanding these "safety experts" provides a basis for creating more accurate and targeted explanations for why a model refused or accepted a harmful query.

💡 **[Summary](2512.21008/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.21008)**

