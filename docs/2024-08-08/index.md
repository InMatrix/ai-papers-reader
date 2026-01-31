---
layout: default
title: 2024-08-08
permalink: /2024-08-08/
---

# 2024-08-08

## AI for Software Development

### CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases

**Relevance:** This system integrates LLM agents with graph database interfaces to enable precise, structure-aware context retrieval and navigation across entire code repositories. This addresses a major limitation of current LLM coding tools (like GitHub Copilot) when dealing with repository-scale tasks. The research is critical for next-generation developer tools, as it provides the necessary ML architecture for advanced tasks like complex bug fixing and refactoring. The HCI implication is significant: enabling agents to reason accurately about complex code structures enhances the utility and trustworthiness of AI assistants in professional software engineering workflows, reducing developer cognitive load.

💡 **[Summary](2408.03910/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03910)**

### Synthesizing Text-to-SQL Data from Weak and Strong LLMs

**Relevance:** This work focuses on enhancing LLMs specifically for text-to-SQL generation, a specialized form of code generation essential in data analysis and backend development. By using a synthetic data approach combining outputs from powerful and weaker models, the authors create SENSE, which achieves state-of-the-art results on benchmarks like SPIDER. Increasing the reliability and accuracy of domain-specific code generation is a direct benefit to HCI, as it reduces the need for human verification and correction of generated code, making LLM-based tools more usable and dependable for data professionals and software developers.

💡 **[Summary](2408.03256/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03256)**

## AI Agents

### Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks

**Relevance:** Optimus-1 directly tackles the challenge of building general-purpose agents capable of completing long-horizon tasks in open worlds by introducing a Hybrid Multimodal Memory module (Knowledge Graph and Experience Pool). This module supports a Knowledge-guided Planner and an Experience-Driven Reflector. This research is central to agent development, focusing on memory, planning, and reflection—all critical for building reliable, autonomous systems. The HCI implications involve designing interfaces around agent planning and memory, ensuring the agent can be effectively monitored and guided by human users over extended, complex interactions.

💡 **[Summary](2408.03615/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03615)**

### Operationalizing Contextual Integrity in Privacy-Conscious Assistants

**Relevance:** This paper addresses a fundamental challenge for advanced AI agents: maintaining user privacy when accessing sensitive information (like emails and documents) to perform tasks. By operationalizing the Contextual Integrity (CI) framework, the authors design strategies to steer LLM agents' information-sharing behaviors. This is crucial for the safety and alignment aspect of AI agents. From an HCI perspective, ensuring agent behavior adheres to human privacy expectations is paramount for building trust and enabling the widespread, ethical adoption of autonomous, personalized assistants.

💡 **[Summary](2408.02373/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.02373)**

### CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases

**Relevance:** This paper presents a concrete example of an LLM agent architecture designed for complex digital environments (code repositories). The agent uses graph database tools and query language reasoning to perform precise context retrieval and code navigation. This demonstrates advanced tool use and planning capabilities necessary for autonomous agents to succeed in professional settings. This ML advancement is crucial for developing agents that can collaborate effectively with human developers by reliably understanding and manipulating large, complex codebases.

💡 **[Summary](2408.03910/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03910)**

## LLM Evaluation Methods

### StructEval: Deepen and Broaden Large Language Model Assessment via Structured Evaluation

**Relevance:** StructEval proposes a novel evaluation framework that moves beyond single-item assessments to structure evaluation across multiple cognitive levels and critical concepts. This aims to provide a more comprehensive, robust, and consistent understanding of LLM capabilities, resisting issues like data contamination. This research is highly relevant to HCI because reliable and trustworthy evaluation protocols are necessary to ensure that models deployed to users genuinely possess the required capabilities, thereby building user trust and providing consistent performance guarantees necessary for effective interaction design.

💡 **[Summary](2408.03281/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03281)**

### MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models

**Relevance:** This paper introduces MMIU, the most extensive benchmark of its kind, designed specifically to evaluate the crucial capability of Large Vision-Language Models (LVLMs) to process and understand multiple images simultaneously. Multi-image comprehension is fundamental for sophisticated multimodal user interactions (e.g., spatial, temporal, causal reasoning). The evaluation identifies significant performance gaps even in state-of-the-art proprietary models, providing valuable insights that directly guide future ML development toward reliable and nuanced multimodal HCI systems.

💡 **[Summary](2408.02718/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.02718)**

### Self-Taught Evaluators

**Relevance:** This work addresses the high cost and staleness of human preference data used for training reward models (evaluators). It proposes an iterative self-improvement scheme to train evaluators using only synthetic data (LLM-as-a-Judge). The resulting evaluators are highly competitive with human-labeled reward models. While reducing human-in-the-loop data collection, this ML advancement is critical for defining the metrics that ensure models are aligned with human values and preferences, directly impacting the quality, safety, and trustworthiness of the final user experience.

💡 **[Summary](2408.02666/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.02666)**

## Reinforcement Learning

### Achieving Human Level Competitive Robot Table Tennis

**Relevance:** This paper presents an RL agent that achieves amateur human-level performance in competitive table tennis, a physically demanding, dynamic, real-world task. The work uses a hierarchical policy and techniques for zero-shot sim-to-real transfer, demonstrating successful application of RL in complex physical settings. This research is highly relevant to Human-Robot Interaction (HRI), as it pushes the boundaries of real-time, precise physical collaboration and requires the robot to interpret and adapt to the behaviors of unseen human opponents, paving the way for intuitive physical human-agent collaboration.

💡 **[Summary](2408.03906/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03906)**

### GPUDrive: Data-driven, multi-agent driving simulation at 1 million FPS

**Relevance:** GPUDrive introduces a GPU-accelerated, multi-agent simulator capable of generating over a million steps of experience per second. This infrastructure is designed to overcome the critical data bottleneck preventing the application of large-scale multi-agent RL algorithms to complex real-world problems like autonomous driving. The ability to quickly train highly effective and general-purpose multi-agent systems is foundational for deploying safe and collaborative agents that interact with humans in shared, complex environments, a crucial challenge in HCI and HRI research.

💡 **[Summary](2408.01584/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.01584)**

### Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks

**Relevance:** Optimus-1, while primarily an AI agent paper, showcases advanced RL concepts applied to long-horizon environmental interaction (e.g., Minecraft). The agent's ability to plan, reflect, and learn from multimodal experience is crucial for developing sophisticated RL policies. From an HCI perspective, this research demonstrates how to imbue RL agents with mechanisms (memory, planning) that facilitate better alignment with complex user intent and enable intuitive human guidance, leading to more manageable and reliable human-agent collaboration over extended tasks.

💡 **[Summary](2408.03615/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.03615)**

## Explainable AI

### Measuring Progress in Dictionary Learning for Language Model Interpretability with Board Game Models

**Relevance:** This work directly contributes to XAI for LLMs by focusing on training Sparse Autoencoders (SAEs) to disentangle interpretable features in model representations. The novelty lies in using LMs trained on board games (chess/Othello), where ground-truth interpretable features are known, allowing for robust, supervised metrics to evaluate interpretability techniques. This foundational ML research is essential for achieving transparency by attempting to map internal model states to human-understandable concepts, a necessary step for building user trust and designing effective, actionable explanations in HCI applications.

💡 **[Summary](2408.00113/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.00113)**

### Smoothed Energy Guidance: Guiding Diffusion Models with Reduced Energy Curvature of Attention

**Relevance:** This paper proposes Smoothed Energy Guidance (SEG), a novel approach that uses the energy-based perspective of the self-attention mechanism to enhance image generation quality. By manipulating the energy landscape of attention, the method provides insight into how the model focuses and makes decisions during the generative process. Although focused on performance, understanding and visualizing how fundamental model mechanisms (like attention energy) guide generation contributes to XAI. This knowledge can be leveraged to provide users with more controllable and interpretable inputs for creative AI applications.

💡 **[Summary](2408.00760/)** 📄 **[Full paper](https://arxiv.org/pdf/2408.00760)**

