---
layout: default
title: 2026-03-06
permalink: /2026-03-06/
---

# 2026-03-06

## AI for Software Development

### SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration

**Relevance:** SWE-CI introduces a repository-level benchmark that shifts the evaluation of code generation from static, one-shot fixes to long-term maintainability within Continuous Integration loops. This is highly relevant to HCI and AI for Software Development because it mirrors the iterative nature of real-world programming, where developers must manage evolving requirements and complex dependencies. By assessing an agent's ability to sustain code quality over hundreds of days and dozens of commits, the paper addresses the human-centric need for AI tools that integrate seamlessly into professional workflows. This approach encourages the development of agents that prioritize long-term software health over short-term functional patches.

💡 **[Summary](2603.03823/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.03823)**

### BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?

**Relevance:** BeyondSWE broadens the evaluation scope for code agents by introducing challenges such as cross-repository reasoning, dependency-driven migration, and full-repository generation. These tasks represent the complex, high-level problems professional developers face daily, which are often overlooked by narrower benchmarks. From an HCI perspective, this work highlights the 'capability gap' between current AI agents and human developer workflows, particularly in how agents use external knowledge. By providing a more realistic and challenging benchmark, BeyondSWE pushes the field toward creating coding assistants that can handle the nuanced, multi-repo context required for genuine software engineering collaboration.

💡 **[Summary](2603.03194/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.03194)**

### ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution

**Relevance:** ParEVO focuses on synthesizing high-performance parallel algorithms for irregular data structures, a task notoriously difficult for human programmers due to steep learning curves and unpredictable data dependencies. This paper is relevant because it uses an 'Evolutionary Coding Agent' to iteratively repair code based on feedback from compilers and performance profilers. This 'agentic evolution' mimics the human debugging process but at a scale and speed that significantly outperforms human baselines. For AI in software development, this demonstrates how specialized agents can assist experts in optimizing performance-critical code, reducing the cognitive load and error rate associated with concurrent programming.

💡 **[Summary](2603.02510/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.02510)**

## AI Agents

### InfoPO: Information-Driven Policy Optimization for User-Centric Agents

**Relevance:** InfoPO addresses the challenge of underspecified user requests by framing agent interaction as active uncertainty reduction. It introduces an information-gain reward that identifies which interaction turns most effectively change the agent's action distribution, allowing for more targeted learning. From an HCI perspective, this is critical for designing agents that can effectively collaborate with humans by asking the right clarifying questions at the right time. By optimizing for information importance while maintaining task-oriented goals, InfoPO provides a scalable mechanism for enhancing user-agent communication. This work benefits the field by creating more intuitive assistants that reduce user frustration in ambiguous scenarios.

💡 **[Summary](2603.00656/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.00656)**

### Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

**Relevance:** The MOSAIC framework focuses on the safety of agentic models that perform multi-step planning and tool execution. Unlike standard chat models, agents can cause irreversible harm by accessing sensitive data or executing incorrect commands. MOSAIC aligns agents for safe tool use by making safety reasoning and refusal first-class actions within a 'plan, check, act' loop. This is a vital contribution to AI Agent research and HCI, as it ensures that autonomous systems remain aligned with human values and safety constraints during long-horizon tasks. This approach builds user trust by making the agent's safety boundaries explicit and learnable.

📄 **[Full paper](https://arxiv.org/pdf/2603.03205)**

### AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation

**Relevance:** AgentConductor introduces an orchestrator agent that dynamically generates interaction topologies for multi-agent systems based on task difficulty. By optimizing the communication graph and reducing redundant interactions, it achieves state-of-the-art accuracy in complex code generation while significantly lowering token costs. This research is relevant to the field of AI Agents as it explores how autonomous systems can self-organize and collaborate more effectively. From an HCI perspective, understanding and optimizing these internal 'agent workflows' is essential for building scalable systems that can solve high-level problems without human intervention, while maintaining efficiency and clarity in their reasoning processes.

💡 **[Summary](2602.17100/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.17100)**

## LLM Evaluation Methods

### QEDBENCH: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs

**Relevance:** QEDBENCH investigates the 'Alignment Gap' in using LLMs as automated judges for university-level mathematical proofs. The study reveals that frontier models often exhibit significant positive bias and struggle with reasoning in discrete domains, leading to score inflation. This is highly relevant to LLM Evaluation Methods and HCI because it highlights the risks of relying on AI-as-a-judge protocols without expert human oversight. By providing a large-scale dual-rubric benchmark, it enables researchers to measure and mitigate these biases. This work underscores the importance of human-in-the-loop evaluation to ensure that automated metrics remain trustworthy and aligned with expert human standards.

💡 **[Summary](2602.20629/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.20629)**

### RIVER: A Real-Time Interaction Benchmark for Video LLMs

**Relevance:** RIVER Bench addresses the gap in evaluating real-time interactivity for multimodal LLMs. Unlike traditional offline benchmarks, RIVER evaluates models on memory, perception, and proactive anticipation during continuous video streams. This is a crucial advancement for LLM evaluation because it shifts the focus toward how models perform in live, interactive dialogues—a key requirement for AI companions and real-world assistants. From an HCI perspective, this benchmark provides a framework for measuring user-centric metrics like response latency and interaction quality, helping researchers build models that feel more responsive and naturally aligned with human conversational dynamics.

💡 **[Summary](2603.03985/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.03985)**

### Humans and LLMs Diverge on Probabilistic Inferences

**Relevance:** This research identifies a fundamental divergence between human reasoning and LLM behavior in non-deterministic, probabilistic settings. By introducing the ProbCOPA dataset, the authors show that while LLMs excel at logic, they fail to replicate the graded and varied distribution of human probabilistic judgments. From an HCI perspective, this is crucial for understanding user trust and the 'uncanny valley' of AI reasoning. If models cannot reason about likelihood in a human-like way, their collaborative utility in open-ended decision-making is limited. This work highlights the need for evaluation methods that go beyond binary correctness to capture human-aligned reasoning patterns.

💡 **[Summary](2602.23546/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.23546)**

## Reinforcement Learning

### Heterogeneous Agent Collaborative Reinforcement Learning

**Relevance:** HACRL introduces a new reinforcement learning paradigm where heterogeneous agents share rollouts during training to mutually improve while remaining independent during inference. This addresses the inefficiencies of isolated on-policy optimization and facilitates cross-agent knowledge transfer. From an HCI and multi-agent RL perspective, this research is significant because it explores how diverse agents with different capabilities can collaborate and learn from one another. By providing mechanisms to mitigate capability discrepancies and distribution shifts, HACRL enables the creation of more robust and efficient multi-agent systems. This collaborative learning approach can be applied to design environments where humans and multiple AI agents interact and learn synergistically.

💡 **[Summary](2603.02604/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.02604)**

### Specificity-aware reinforcement learning for fine-grained open-world classification

**Relevance:** SpeciaRL uses reinforcement learning to steer multimodal models toward predictions that are both correct and specific in open-world settings. It introduces a dynamic, verifier-based reward signal that promotes specificity without compromising accuracy. This is highly relevant to RL and HCI because users often require precise, fine-grained information rather than generic labels. By using RL to align model outputs with the level of detail humans expect, SpeciaRL improves the utility and interpretability of AI predictions. This framework demonstrates how reward design can be used to balance competing objectives like correctness and specificity, which is essential for effective human-AI communication.

💡 **[Summary](2603.03197/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.03197)**

### Next Embedding Prediction Makes World Models Stronger

**Relevance:** NE-Dreamer advances model-based reinforcement learning (MBRL) by using a temporal transformer to predict next-step encoder embeddings. This approach enables agents to learn coherent state representations without the need for expensive reconstruction losses, particularly in partially observable environments. For RL research, this establishes a scalable framework for learning world models in complex domains. From an HCI perspective, stronger world models allow agents to better anticipate the consequences of their actions and reason about temporal dependencies. This leads to more capable and predictable agents that can assist humans in tasks involving memory, spatial reasoning, and long-term planning.

💡 **[Summary](2603.02765/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.02765)**

## Explainable AI

### Transformers converge to invariant algorithmic cores

**Relevance:** This paper explores the internal workings of transformers, demonstrating that they converge to shared 'algorithmic cores'—compact subspaces necessary for task performance—regardless of their specific weight configurations. This is a major contribution to Explainable AI (XAI) as it moves the focus from implementation-specific details to the 'computational essence' of the models. For HCI, identifying these low-dimensional invariants offers a way to provide more consistent and meaningful explanations to users. By understanding the stable internal structures that drive AI behavior, designers can create better interfaces for transparency, helping users understand why a model generalizes or memorizes information across different scales.

💡 **[Summary](2602.22600/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.22600)**

### Spilled Energy in Large Language Models

**Relevance:** This work reinterprets LLM classifiers as Energy-Based Models (EBMs) to track 'energy spills' during decoding. The authors show that these spills correlate with factual errors and hallucinations, providing a training-free metric for hallucination detection. This is highly relevant to XAI because it offers a principled way to monitor model reliability in real-time without requiring auxiliary probe classifiers. For HCI, this provides a mechanism to alert users when a model is likely to be hallucinating, enhancing transparency and trust. It allows for the development of interfaces that can visually signal the 'energy' or uncertainty of generated text to the user.

💡 **[Summary](2602.18671/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.18671)**

### AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models

**Relevance:** AgilePruner provides a thorough empirical analysis of attention-based and diversity-based pruning methods in vision-language models. By using metrics like feature diversity (erank) and attention entropy, the paper reveals how different pruning strategies affect model performance and hallucination frequency. This is relevant to XAI because it helps researchers understand the 'visual token processing mechanisms' that drive model decisions. From an HCI perspective, understanding these trade-offs allows for the design of more efficient models that maintain high performance on complex images while providing insights into why a model might fail or hallucinate, leading to more interpretable visual AI systems.

📄 **[Full paper](https://arxiv.org/pdf/2603.01236)**

