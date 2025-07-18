---
layout: default
title: 2025-07-18
permalink: /2025-07-18/
---

# 2025-07-18

## AI for Software Development

### GitChameleon: Evaluating AI Code Generation Against Python Library Version Incompatibilities

**Relevance:** This paper introduces GitChameleon, a benchmark to evaluate AI code generation, specifically focusing on the critical challenge of Python library version incompatibilities. From an HCI perspective, the ability of AI code assistants to generate functionally accurate code that is compatible with specific library versions is paramount for developer productivity and trust. This research helps identify current limitations and guides the development of more adaptable and dependable AI code generation methods, directly impacting the usability and reliability of AI tools in real-world software development workflows.

💡 **[Summary](2507.12367/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.12367)**

### SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?

**Relevance:** SWE-Perf is the first benchmark designed to evaluate LLMs on code performance optimization tasks within authentic repository contexts. This research directly addresses a high-value and complex aspect of software development. For HCI, this is crucial because developers need AI tools that can effectively enhance the performance of existing, large codebases, not just generate simple snippets. Highlighting a substantial capability gap, SWE-Perf provides insights for developing AI systems that can truly assist software engineers with complex, impactful tasks, improving their efficiency and the quality of production-level systems.

💡 **[Summary](2507.12415/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.12415)**

### OpenCodeReasoning-II: A Simple Test Time Scaling Approach via Self-Critique

**Relevance:** This paper presents OpenCodeReasoning-II, a large-scale dataset and a two-stage fine-tuning strategy for LLMs focused on code generation and critique. The integration of a critique mechanism is highly relevant for HCI in software development. AI tools that can not only generate code but also self-critique and potentially improve their outputs reduce the burden on human developers for debugging and review, leading to more efficient and trustworthy AI-assisted coding. This research advances the capabilities of such intelligent code assistants.

💡 **[Summary](2507.09075/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.09075)**

## AI Agents

### AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs

**Relevance:** AgentsNet proposes a new benchmark to measure the ability of multi-agent LLM systems to self-organize, coordinate, and collaboratively reason given a network topology. From an HCI perspective, as AI systems become more autonomous and composed of multiple interacting agents, understanding and designing for their collective behavior and communication is critical for human oversight, collaboration, and interaction. This research directly addresses the challenges of managing and collaborating with complex AI agent societies, informing future human-agent teaming strategies and user interface designs for such systems.

💡 **[Summary](2507.08616/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.08616)**

### EmbRACE-3K: Embodied Reasoning and Action in Complex Environments

**Relevance:** EmbRACE-3K introduces a dataset and benchmark for evaluating vision-language models in embodied settings, requiring online interaction, active scene understanding, and long-horizon planning. This is highly relevant to AI Agents, particularly embodied agents (e.g., robots, virtual avatars). From an HCI perspective, understanding how well agents can reason and act in complex, dynamic environments is crucial for designing intuitive control interfaces, effective feedback mechanisms, and for fostering human trust in autonomous systems that share our physical or virtual spaces.

💡 **[Summary](2507.10548/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.10548)**

### Orchestrator-Agent Trust: A Modular Agentic AI Visual Classification System with Trust-Aware Orchestration and RAG-Based Reasoning

**Relevance:** This paper introduces a modular agentic AI system for visual classification that integrates multimodal agents with a non-visual reasoning orchestrator and RAG, focusing on 'trust-aware orchestration.' From an HCI perspective, fostering human trust in multi-agent AI systems is paramount, especially in zero-shot or critical domains. By enabling trust calibration, leveraging RAG to ground predictions, and providing iterative re-evaluation, this framework contributes to more interpretable and reliable multi-agent AI, allowing users to better understand, and thus trust, the system's decisions and mitigate overconfidence.

💡 **[Summary](2507.10571/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.10571)**

## LLM Evaluation Methods

### REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once

**Relevance:** REST is a novel stress-testing framework that evaluates large reasoning models (LRMs) by concurrently exposing them to multiple problems. This goes beyond traditional single-question benchmarks. From an HCI perspective, this evaluation is vital because real-world user interactions often involve complex, multi-faceted queries that impose 'multi-context pressure' and 'dynamic cognitive load' on the AI. REST's ability to reveal performance degradation and differences among models under such stress directly informs how reliably users can expect these systems to perform in practical, demanding scenarios, enhancing our understanding of their robustness.

💡 **[Summary](2507.10541/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.10541)**

### Planted in Pretraining, Swayed by Finetuning: A Case Study on the Origins of Cognitive Biases in LLMs

**Relevance:** This paper investigates the origins of cognitive biases in LLMs, disentangling the influence of pretraining, finetuning, and training stochasticity. From an HCI perspective, understanding and mitigating cognitive biases in LLMs is critical for ensuring fairness, trustworthiness, and ethical AI. Biases can lead to irrational or discriminatory outputs, eroding user trust and confidence. This research provides crucial insights into where these biases are 'planted,' enabling more principled strategies for their evaluation and mitigation, which is essential for developing AI systems that are safe and equitable for human interaction.

💡 **[Summary](2507.07186/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.07186)**

### Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination

**Relevance:** This paper exposes that many current evaluations of RL-enhanced LLM reasoning suffer from data contamination in popular benchmarks, leading to unreliable results. From an HCI perspective, the validity and trustworthiness of LLM evaluation results are paramount for setting accurate user expectations and ensuring the safe deployment of AI systems. If benchmarks are contaminated, researchers and users cannot reliably assess an AI's true capabilities or limitations. This work highlights the need for rigorous, 'leakage-free' datasets to establish trustworthy conclusions about AI reasoning and performance.

💡 **[Summary](2507.10532/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.10532)**

## Reinforcement Learning

### RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning

**Relevance:** RLEP introduces a two-phase reinforcement learning framework that uses experience replay to optimize LLM reasoning. This method aims to stabilize training, prevent policy drift, and improve convergence and performance by replaying high-quality examples. From an HCI perspective, enhancing LLM reasoning through RL can lead to more capable and reliable AI agents. Agents that can learn efficiently from verified trajectories become more robust and predictable, facilitating more effective human guidance and collaboration, and ultimately making human-agent interactions smoother and more productive.

💡 **[Summary](2507.07451/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.07451)**

### A Practical Two-Stage Recipe for Mathematical LLMs: Maximizing Accuracy with SFT and Efficiency with Reinforcement Learning

**Relevance:** This paper proposes a practical two-stage recipe that integrates Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to enhance mathematical reasoning in LLMs, focusing on both accuracy and efficiency. For HCI, efficient mathematical reasoning is critical for AI tools assisting in STEM fields. An efficient model not only performs better but also reduces latency and computational costs, improving user experience and accessibility for complex problem-solving. This research offers a blueprint for developing high-performing and practically deployable AI mathematical reasoners for human-AI collaborative discovery.

💡 **[Summary](2507.08267/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.08267)**

### Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning

**Relevance:** Open Vision Reasoner explores transferring linguistic cognitive behaviors to Multimodal LLMs (MLLMs) using massive linguistic cold-start fine-tuning followed by extensive multimodal reinforcement learning. This is highly relevant to RL as it applies the paradigm to visual reasoning. From an HCI perspective, enhanced visual reasoning capabilities in MLLMs are crucial for developing more intuitive and capable embodied AI and human-robot interaction. Agents that can 'reason' visually based on human-like cognitive patterns will be more easily understood by users, leading to more natural and effective human-AI collaboration in visual environments.

💡 **[Summary](2507.05255/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05255)**

## Explainable AI

### Orchestrator-Agent Trust: A Modular Agentic AI Visual Classification System with Trust-Aware Orchestration and RAG-Based Reasoning

**Relevance:** While primarily an AI Agents paper, this work's explicit focus on 'trust-aware orchestration' and enabling 'interpretable multi-agent AI' directly aligns with Explainable AI. From an HCI perspective, ensuring human trust in complex, multi-agent AI systems is paramount. By leveraging confidence calibration, RAG-grounded predictions, and iterative re-evaluation to address agent overconfidence, this system provides mechanisms for users to better understand the AI's decision-making process, calibrate their trust, and even correct system behavior. This enhances transparency and accountability, core goals of XAI for user-centric AI.

💡 **[Summary](2507.10571/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.10571)**

