---
layout: default
title: 2025-11-14
permalink: /2025-11-14/
---

# 2025-11-14

## AI for Software Development

### Agentic Refactoring: An Empirical Study of AI Coding Agents

**Relevance:** This paper is highly relevant as it empirically studies the practical application of AI agents in a core software engineering task: refactoring. From an HCI perspective, it offers critical insights into how agents impact code quality (maintainability, readability) and contrasts agentic behavior with human refactoring patterns. The findings guide the design of future AI developer tools that effectively complement human expertise, focusing on improving the internal quality aspects of code.

💡 **[Summary](2511.04824/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.04824)**

### Walking the Tightrope of LLMs for Software Development: A Practitioners' Perspective

**Relevance:** This is a crucial HCI contribution, using grounded theory based on practitioner interviews to analyze the socio-technical impact of LLMs on software development. It moves beyond technical metrics to identify human-centric trade-offs, such as maintaining developer flow, improving mental models, versus potential damage to professional reputation. The work provides essential guidance for software team leaders and IT managers on how to responsibly adopt and integrate AI coding assistants into the human workflow.

💡 **[Summary](2511.06428/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.06428)**

### SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads?

**Relevance:** The paper introduces a much-needed benchmark for evaluating LLMs on repository-level performance optimization, a task requiring complex code reasoning and bottleneck localization. This addresses the challenge of moving AI assistance beyond simple code generation to high-level software engineering tasks like efficiency improvement. The findings highlight current agent struggles in maintaining correctness and reasoning across functions, providing clear targets for future research in robust AI coding tools.

💡 **[Summary](2511.06090/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.06090)**

## AI Agents

### Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds

**Relevance:** This paper is key for generalist agent research, proposing an open recipe for building agents capable of complex, long-horizon tasks in 3D open worlds. Its focus on a 'human-like interaction paradigm' that unifies perception, reasoning, and action (raw pixels to precise keyboard-mouse actions) is directly relevant to HCI, aiming for agents that can operate intuitively and generalize across distinct, open-ended digital environments.

💡 **[Summary](2511.08892/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.08892)**

### Adapting Web Agents with Synthetic Supervision

**Relevance:** This research tackles the fundamental agent challenge of generalization and robustness in dynamic environments (websites). By proposing SynthAgent, which refines synthetic training data to eliminate hallucinations and noise, it directly benefits the reliability and deployability of web automation agents. Improving synthetic data quality is crucial for ensuring that agents can consistently meet user-defined goals without requiring extensive, costly human demonstrations.

💡 **[Summary](2511.06101/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.06101)**

### FLEX: Continuous Agent Evolution via Forward Learning from Experience

**Relevance:** FLEX addresses the critical challenge of continuous learning in autonomous agents, enabling them to 'continuously evolve through accumulated experience' via continual reflection on successes and failures. This gradient-free approach to lifelong learning is vital for creating agents that grow and adapt over long periods of deployment, mirroring human learning and improving their long-term utility and collaboration potential.

💡 **[Summary](2511.06449/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.06449)**

## LLM Evaluation Methods

### Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

**Relevance:** This paper proposes 'intelligence per watt' (IPW) as a critical metric for assessing the capability and efficiency of local LLM inference, balancing accuracy and power consumption. This directly impacts the practical viability and accessibility of on-device LLMs, making it highly relevant to HCI concerns regarding latency, battery life, and democratizing advanced AI access on power-constrained personal devices, thus guiding the transition from cloud to local inference.

💡 **[Summary](2511.07885/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.07885)**

### MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs

**Relevance:** This contribution fills a major evaluation gap by introducing the first comprehensive benchmark for Multi-Video Understanding (MVU), requiring MLLMs to synthesize information across multiple visual streams. This moves evaluation beyond simplified single-instance tasks to complex, real-world scenarios (e.g., autonomous systems, sports analytics), aligning evaluation methods with genuine user needs and the high-order reasoning required in modern applications.

💡 **[Summary](2511.07250/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.07250)**

## Reinforcement Learning

### WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

**Relevance:** This work applies RL to Vision-Language-Action (VLA) models for robotic manipulation, focusing on self-correction and learning without interacting with the real environment. WMPO addresses the high sample complexity inherent to robotics RL by leveraging pixel-based world models. This approach facilitates emergent behaviors like self-correction, which is essential for developing robust and reliable human-robot collaboration systems.

💡 **[Summary](2511.09515/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.09515)**

### RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments

**Relevance:** RLVE addresses the 'Novel agent environment design' aspect of RL by introducing RLVE-Gym, a large suite of verifiable environments where problem difficulty dynamically adapts to the policy model's capabilities. This mechanism ensures that the learning signal remains challenging and relevant as the policy improves, facilitating scalable RL and enhancing the model's generalizable reasoning capabilities, a key requirement for complex agents.

💡 **[Summary](2511.07317/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.07317)**

### The Path Not Taken: RLVR Provably Learns Off the Principals

**Relevance:** This paper provides a fundamental, mechanistic understanding of Reinforcement Learning with Verifiable Rewards (RLVR) training dynamics. By revealing that RLVR learns 'off principal directions' in weight space, it offers crucial theoretical insight into why RL alignment works differently than SFT. This knowledge is essential for designing geometry-aware, RL-native learning algorithms and interpreting the behavioral effects of RL on language models.

💡 **[Summary](2511.08567/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.08567)**

## Explainable AI

### Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads

**Relevance:** This paper advances model introspection by proposing lightweight Uncertainty Heads (UHeads) that use internal LLM states to estimate the confidence of individual reasoning steps. This technique provides local, step-level transparency and verification, improving the interpretability and trustworthiness of complex LLM reasoning chains without relying on computationally expensive external Process Reward Models (PRMs).

💡 **[Summary](2511.06209/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.06209)**

### Reinforcement Learning Improves Traversal of Hierarchical Knowledge in LLMs

**Relevance:** This study uses internal activation analysis to explain the mechanism behind RL alignment on knowledge tasks. It shows that RL primarily enhances procedural skills (navigating knowledge hierarchies) rather than altering factual representations. This insight contributes significantly to white-box transparency, helping researchers understand exactly how RL modifies LLM behavior and procedural knowledge retrieval, which is vital for building reliable knowledge-based agents.

💡 **[Summary](2511.05933/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.05933)**

