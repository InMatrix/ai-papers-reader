---
layout: default
title: 2025-10-03
permalink: /2025-10-03/
---

# 2025-10-03

## AI for Software Development

### QUASAR: Quantum Assembly Code Generation Using Tool-Augmented LLMs via Agentic RL

**Relevance:** This paper directly addresses AI for software development by focusing on automated quantum assembly code generation. It leverages LLMs and agentic reinforcement learning to design and optimize quantum circuits, a specialized and complex programming task. From an HCI perspective, tools like QUASAR aim to lower the barrier to entry for quantum computing, enabling developers to create circuits more easily and accurately. The integration of quantum simulators and a hierarchical reward mechanism improves the quality and validity of generated code, enhancing developer trust and productivity.

💡 **[Summary](2510.00967/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00967)**

### PIPer: On-Device Environment Setup via Online Reinforcement Learning

**Relevance:** PIPer tackles a persistent challenge in software engineering: automated environment setup. By combining supervised fine-tuning and Reinforcement Learning with Verifiable Rewards (RLVR), it enables LLMs to generate correct Bash scripts for configuring project environments. This directly impacts developers by reducing manual effort and setup friction, enhancing their workflow efficiency. From an HCI viewpoint, automating such tedious configuration tasks through AI assistance improves user satisfaction and allows developers to focus on core coding activities, making the development process smoother and less error-prone.

💡 **[Summary](2509.25455/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25455)**

### DeepCodeSeek: Real-Time API Retrieval for Context-Aware Code Generation

**Relevance:** DeepCodeSeek significantly advances AI assistance for software development by focusing on real-time API retrieval for context-aware code generation and auto-completion. By providing critical API context, it enhances the quality of generated code, a direct benefit for developers. The method also optimizes a compact reranker using synthetic data and RL for efficiency, ensuring low latency. For HCI, this translates to faster, more accurate code suggestions and completions, reducing cognitive load and improving the flow state for developers, especially in complex enterprise environments where API usage intent can be unclear.

💡 **[Summary](2509.25716/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25716)**

## AI Agents

### ACON: Optimizing Context Compression for Long-horizon LLM Agents

**Relevance:** ACON presents a unified framework for LLM agents operating in dynamic, real-world environments, specifically addressing the challenge of growing context length in long-horizon tasks. It optimizes context compression through natural language guideline optimization and distillation into smaller models. This has significant implications for HCI by enabling more efficient and cost-effective deployment of AI agents. By reducing memory usage and preserving performance, ACON contributes to the development of responsive and reliable agents that can handle complex, multi-step user requests without excessive computational overhead, enhancing user experience.

💡 **[Summary](2510.00615/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00615)**

### Flash-Searcher: Fast and Effective Web Agents via DAG-Based Parallel Execution

**Relevance:** Flash-Searcher introduces a novel parallel agent reasoning framework for web agents, reimagining execution from sequential chains to directed acyclic graphs (DAGs). This decomposition of tasks into subtasks with explicit dependencies enables concurrent execution and dynamic workflow optimization. For HCI, this directly translates to faster and more effective interaction with web agents, reducing user waiting times and improving task completion rates. The framework's efficiency gains enhance the usability and responsiveness of AI agents in complex online environments, making them more practical and user-friendly for intricate web-based tasks.

💡 **[Summary](2509.25301/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25301)**

### An Empirical Study of Testing Practices in Open Source AI Agent Frameworks and Agentic Applications

**Relevance:** This paper conducts the first large-scale empirical study on testing practices for FM-based AI agents, highlighting challenges due to non-determinism and non-reproducibility. It identifies testing patterns and blind spots, such as the neglect of prompt testing. From an HCI perspective, this research is crucial for building robust and dependable AI agents. Understanding current limitations in testing directly informs how developers can create agents that are more reliable, trustworthy, and less prone to unexpected behaviors, ultimately leading to better user experiences and safer human-agent interaction.

💡 **[Summary](2509.19185/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.19185)**

## LLM Evaluation Methods

### BiasFreeBench: a Benchmark for Mitigating Bias in Large Language Model Responses

**Relevance:** BiasFreeBench is a crucial contribution to LLM evaluation, introducing a unified benchmark and a response-level metric (Bias-Free Score) to assess fairness, safety, and anti-stereotypical outputs. It bridges the gap between probabilistic bias evaluations and real-world user interactions. From an HCI perspective, this directly impacts user trust and ethical AI development. By providing a consistent and comprehensive evaluation framework for bias mitigation, it helps researchers and practitioners ensure that LLMs produce equitable and safe responses, fostering more inclusive and responsible human-AI interactions.

💡 **[Summary](2510.00232/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00232)**

### Rethinking Reward Models for Multi-Domain Test-Time Scaling

**Relevance:** This paper critically evaluates different reward models (Process Reward Models vs. Outcome Reward Models) for assessing the reliability of LLMs during test-time scaling across various domains. It challenges conventional wisdom by showing that generative ORMs are often more robust. From an HCI perspective, understanding which evaluation methods reliably reflect model quality is paramount. This research helps refine how we evaluate LLM performance in user-facing applications, influencing model selection and deployment strategies to ensure consistent and high-quality user experiences, especially in diverse and complex reasoning tasks where reliability is key.

💡 **[Summary](2510.00492/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00492)**

### Making, not Taking, the Best of N

**Relevance:** This work introduces Fusion-of-N (FusioN), a collaborative method for obtaining high-quality LLM generations by synthesizing informative elements from multiple samples, rather than simply selecting the 'best.' This approach inherently involves evaluating and combining diverse outputs. From an HCI perspective, this directly impacts how users perceive the quality and utility of LLM-generated content. By improving the robustness and versatility of outputs across multiple languages and tasks, FusioN enhances user satisfaction and trust in LLMs, demonstrating a shift towards integrating diverse strengths for superior results rather than relying on a single 'best' answer.

💡 **[Summary](2510.00931/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00931)**

## Reinforcement Learning

### DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search

**Relevance:** DeepSearch addresses a critical bottleneck in RL with Verifiable Rewards (RLVR) for LLMs: insufficient exploration leading to training plateaus. By integrating Monte Carlo Tree Search (MCTS) directly into the RLVR training loop, it enables systematic exploration and fine-grained credit assignment. From an HCI perspective, this advancement can lead to LLMs with superior reasoning skills, particularly in complex tasks like mathematical reasoning. More robust and efficient learning processes in RL directly contribute to developing AI systems that can reliably solve challenging problems, enhancing their utility and trustworthiness in human-AI collaboration.

💡 **[Summary](2509.25454/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25454)**

### Nudging the Boundaries of LLM Reasoning

**Relevance:** NuRL proposes a novel 'nudging' method to overcome a key limitation of current RL algorithms for LLMs: their inability to learn from 'unsolvable' problems. By using self-generated abstract hints, NuRL introduces training signals for previously inaccessible samples, effectively pushing the upper bound of LLM reasoning. From an HCI viewpoint, this research is significant because it enables LLMs to develop more advanced and adaptable reasoning capabilities. It promises to deliver AI systems that can learn from a broader range of challenges, potentially leading to more flexible and intelligent assistants that require less human intervention to improve.

💡 **[Summary](2509.25666/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25666)**

### VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators

**Relevance:** VLA-RFT introduces a reinforcement fine-tuning framework for Vision-Language-Action (VLA) models, crucial for embodied decision-making. By leveraging a data-driven world model as a controllable simulator, it provides efficient, action-aligned learning signals, drastically reducing real-world sample requirements. This is highly relevant to HCI for developing robust and generalizable embodied AI agents. By enhancing VLA models' generalization and robustness under distribution shifts, VLA-RFT contributes to creating more reliable and safer human-robot interaction scenarios, allowing agents to perform complex tasks in diverse environments with greater autonomy and fewer errors.

💡 **[Summary](2510.00406/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00406)**

## Explainable AI

### Hyperdimensional Probe: Decoding LLM Representations via Vector Symbolic Architectures

**Relevance:** Hyperdimensional Probe introduces a novel paradigm to decode information from LLM vector space into interpretable concepts using Vector Symbolic Architectures. This directly addresses the opacity of LLM internal representations, moving beyond output vocabulary or unclear feature names. From an HCI perspective, this is a significant step towards making LLM decision-making more transparent and trustworthy for users and developers. By enabling the extraction of more informative and structured features, it helps identify LLM failures and build greater confidence in AI systems, improving overall human understanding and control over complex models.

💡 **[Summary](2509.25045/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.25045)**

### Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls

**Relevance:** This paper employs reverse-engineering techniques, including logit attributions and linear probes, to uncover why Transformers struggle with multi-digit multiplication. It reveals how models encode (or fail to encode) long-range dependencies and implement operations. This detailed analysis is a prime example of XAI, focusing on understanding model failures at a fundamental level. From an HCI perspective, explaining such core limitations is crucial for managing user expectations and designing more reliable AI systems. Understanding *why* an AI fails informs better model development and helps users discern appropriate tasks for AI assistance.

💡 **[Summary](2510.00184/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.00184)**

