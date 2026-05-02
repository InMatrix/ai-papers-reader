---
layout: default
title: 2026-02-13
permalink: /2026-02-13/
---

# 2026-02-13

## AI for Software Development

### GameDevBench: Evaluating Agentic Capabilities Through Game Development

**Relevance:** This paper introduces a benchmark for evaluating AI agents in the complex, multimodal domain of game development. Unlike traditional coding benchmarks that focus on isolated functions, GameDevBench requires agents to navigate large codebases while manipulating visual assets like shaders and animations. From an HCI perspective, this is significant because it mirrors the interdisciplinary nature of real-world software engineering. The study reveals that multimodal complexity significantly impacts agent success, and it proposes feedback mechanisms that allow agents to 'see' their output, highlighting the importance of visual feedback loops in AI-assisted creative workflows.

💡 **[Summary](2602.11103/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.11103)**

### FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

**Relevance:** FeatureBench shifts the focus of AI evaluation from simple bug fixing to end-to-end feature development. It utilizes a scalable, test-driven method to derive tasks from real-world repositories, ensuring that agents are tested on their ability to manage dependencies and multi-commit changes. For HCI researchers, this paper highlights the gap between current AI capabilities and the needs of professional developers. By providing a framework for verifiable, executable environments, it enables the study of how AI can act as a long-term collaborator in software projects rather than just a code completion tool.

💡 **[Summary](2602.10975/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10975)**

### GoodVibe: Security-by-Vibe for LLM-Based Code Generation

**Relevance:** This paper addresses 'vibe coding'—a fast-paced, informal development style where security is often overlooked. It proposes a framework called GoodVibe that uses neuron-level optimization to improve the security of generated code by default. This is highly relevant to HCI as it explores how to bake safety into the developer experience without introducing friction or cognitive load. By identifying security-critical neurons and performing selective fine-tuning, the authors demonstrate a scalable way to secure AI-assisted programming environments, ensuring that speed and convenience do not come at the cost of software integrity.

💡 **[Summary](2602.10778/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10778)**

## AI Agents

### SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes

**Relevance:** SceneSmith employs a hierarchical agentic framework involving a designer, critic, and orchestrator to generate complex, physically accurate 3D environments from natural language. This research is vital for HCI as it demonstrates how multi-agent systems can handle high-dimensional design tasks that would be overwhelming for a single model. The framework's ability to produce stable, simulation-ready scenes with dense clutter and articulated objects provides a powerful tool for researchers training robots or designing virtual reality environments, showcasing the potential for agents to serve as sophisticated co-creators in spatial design.

💡 **[Summary](2602.09153/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.09153)**

### Towards Autonomous Mathematics Research

**Relevance:** This work introduces Aletheia, an agent capable of navigating mathematical literature and constructing long-horizon proofs at a professional research level. It presents significant milestones in human-AI collaboration, including papers co-authored by AI and humans. From an HCI standpoint, this paper is a landmark study in how agents can transition from solving competition-level problems to engaging in professional-grade research. The proposed 'levels of autonomy' for AI-assisted results provide a framework for HCI researchers to categorize and study the evolving dynamics of human-AI partnership in highly specialized intellectual fields.

💡 **[Summary](2602.10177/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10177)**

### AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management

**Relevance:** AgentSys addresses the security risk of indirect prompt injection by introducing a hierarchical memory management system inspired by operating system process isolation. By spawning worker agents in isolated contexts and strictly validating data return values, it prevents malicious instructions from persisting in the main agent's memory. This is a critical contribution to HCI, as user trust in autonomous agents is contingent on robust security. The framework demonstrates that architectural changes in how agents manage information can significantly enhance safety while maintaining or even improving utility in complex, tool-using workflows.

💡 **[Summary](2602.07398/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.07398)**

## LLM Evaluation Methods

### LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation

**Relevance:** LiveMedBench addresses the problem of data contamination in medical LLM evaluation by harvesting real-world clinical cases weekly. It introduces an automated rubric-based evaluation that aligns more closely with expert physician judgment than standard metrics. For HCI, this paper is important because it emphasizes the need for evaluation methods that capture 'clinical correctness' and 'patient-specific constraints' rather than just lexical similarity. It highlights that the biggest bottleneck for AI in high-stakes domains is contextual application, suggesting that HCI methods should focus on how models interpret specific human circumstances.

💡 **[Summary](2602.10367/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10367)**

### GENIUS: Generative Fluid Intelligence Evaluation Suite

**Relevance:** The GENIUS suite is designed to evaluate 'Generative Fluid Intelligence'—the ability of models to reason through novel constraints and patterns on the fly, rather than relying on memorized knowledge. This is highly relevant to HCI because it tests how well AI can adapt to the immediate, idiosyncratic context of a user's request. The finding that failures often stem from context comprehension rather than generative limits suggests that HCI improvements in how models process and attend to user-provided context could significantly enhance the perceived intelligence and utility of multimodal AI systems.

💡 **[Summary](2602.11144/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.11144)**

### Benchmarking Large Language Models for Knowledge Graph Validation

**Relevance:** This paper introduces FactCheck, a benchmark for evaluating LLMs on their ability to validate facts within Knowledge Graphs using internal knowledge, RAG, and multi-model consensus. From an HCI perspective, the inclusion of an interactive exploration platform for analyzing verification decisions is key. It allows researchers to study how humans interpret AI-generated evidence and where trust breaks down. The study's finding that multi-model consensus and RAG do not always improve reliability underscores the complexity of building trustworthy AI assistants for knowledge-intensive tasks, necessitating better human-in-the-loop validation interfaces.

📄 **[Full paper](https://arxiv.org/pdf/2602.10748)**

## Reinforcement Learning

### Blockwise Advantage Estimation for Multi-Objective RL with Verifiable Rewards

**Relevance:** This paper proposes a method to assign specific rewards to individual segments of a generated text, reducing 'objective interference' where unrelated signals get mixed. In the context of HCI, this allows for much finer control over AI behavior during training. For example, a model could be rewarded for 'mathematical correctness' in one block and 'explanation clarity' in another. This modular approach to RL training facilitates the development of models that better align with complex, multi-faceted human preferences without requiring the manual design of intricate scalar reward functions.

💡 **[Summary](2602.10231/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10231)**

### Spend Search Where It Pays: Value-Guided Structured Sampling and Optimization for Generative Recommendation

**Relevance:** V-STAR addresses the mismatch between probability and reward in generative recommendation systems. By using value-guided decoding and sibling-relative advantages in RL, it encourages the exploration of high-reward items that might be overlooked by standard search. This is relevant to HCI because recommendation is fundamentally a user-experience task; by improving the diversity and quality of the 'tail' of recommendations, V-STAR enhances user discovery and satisfaction. It demonstrates how RL can be tuned to better capture long-term value for the user rather than just short-term token probability.

💡 **[Summary](2602.10699/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10699)**

### Online Causal Kalman Filtering for Stable and Effective Policy Optimization

**Relevance:** This paper introduces the KPO framework, which uses Kalman filtering to smooth the noise in token-level importance sampling during RL training for LLMs. While technical, its implications for HCI are significant: by stabilizing the training process, it allows for more reliable and effective policy updates when fine-tuning models on human feedback. This leads to models that are more stable and performant in reasoning tasks. The use of traditional control theory (Kalman filters) to improve modern LLM training offers a principled way to build more predictable and better-aligned AI systems.

💡 **[Summary](2602.10609/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10609)**

## Explainable AI

### From Features to Actions: Explainability in Traditional and Agentic AI Systems

**Relevance:** This paper is a direct and vital contribution to XAI, specifically addressing the shift from static model predictions to agentic AI trajectories. It demonstrates that traditional attribution methods (like feature importance) fail to diagnose failures in multi-step agent behaviors. Instead, it proposes 'trace-grounded rubric evaluation' to localize breakdowns. This is a crucial HCI insight: as AI becomes more agentic, human users need explanations that describe the 'story' of the agent's actions and state-tracking rather than just a heatmap of the input features. This moves XAI toward more actionable, diagnostic transparency.

💡 **[Summary](2602.06841/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.06841)**

