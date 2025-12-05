---
layout: default
title: 2025-12-05
permalink: /2025-12-05/
---

# 2025-12-05

## AI for Software Development

No paper recommendations for this topic.

## AI Agents

### Deep Research: A Systematic Survey

**Relevance:** This survey provides a comprehensive overview of Deep Research systems, which are LLM-powered agents designed to act as research assistants capable of completing complex, open-ended tasks requiring multi-source verification. It formalizes a three-stage roadmap and details the key components of agent architecture, including query planning, memory management, information acquisition, and optimization techniques like agentic reinforcement learning. This work is foundational for understanding the current landscape and future directions of autonomous AI Agents.

💡 **[Summary](2512.02038/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.02038)**

### ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

**Relevance:** ToolOrchestra focuses on training small orchestrator models using RL with outcome, efficiency, and user-preference rewards to coordinate multiple intelligent models and tools. This approach directly addresses the core AI Agent challenge of efficient planning and tool management for solving difficult, long-horizon tasks (like Humanity's Last Exam). It demonstrates that a lightweight orchestration model can be more effective and 2.5x more efficient than relying solely on monolithic frontier models, paving the way for scalable agent systems.

💡 **[Summary](2511.21689/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.21689)**

### SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds

**Relevance:** SimWorld introduces a crucial piece of infrastructure for advancing AI Agents: an open-ended simulator built on Unreal Engine 5. Existing simulators often lack the realistic physical and social dynamics required for agents to 'survive and thrive in the real world.' SimWorld provides a rich interface for LLM/VLM agents, enabling massive-scale training, reasoning, and evaluation across diverse embodied scenarios involving strategic cooperation and competition, essential for developing robust real-world agent intelligence.

💡 **[Summary](2512.01078/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.01078)**

## LLM Evaluation Methods

### InnoGym: Benchmarking the Innovation Potential of AI Agents

**Relevance:** InnoGym is the first benchmark designed to systematically evaluate the *innovation potential* of AI agents, moving beyond simple task correctness. It introduces complementary metrics—performance gain and novelty—to capture methodological differences in solutions to real-world engineering and scientific problems. This is highly relevant to HCI, as evaluating novelty and creativity is crucial for assessing AI systems intended for collaboration in research, directly impacting user perception of AI capability and utility.

💡 **[Summary](2512.01822/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.01822)**

### AlignBench: Benchmarking Fine-Grained Image-Text Alignment with Synthetic Image-Caption Pairs

**Relevance:** This paper introduces AlignBench to rigorously assess fine-grained image-text alignment in VLMs. By using synthetically generated, annotated data, the benchmark reveals critical limitations in current models, showing they are 'nearly blind' to fine details and exhibit self-preference favoring their own outputs. These findings are essential for understanding model fragility and bias, informing HCI design related to user trust and the cognitive load required to verify VLM outputs.

💡 **[Summary](2511.20515/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.20515)**

### ViDiC: Video Difference Captioning

**Relevance:** ViDiC introduces a new task and dataset (ViDiC-1K) focused on evaluating MLLMs' comparative perception and difference reasoning between video pairs. It proposes a reliable dual-checklist evaluation framework based on the LLM-as-a-Judge protocol. This advancement addresses the need for robust evaluation of temporal and compositional changes, a complex reasoning task that directly impacts the usability and reliability of MLLMs in dynamic environments and applications like video editing or surveillance.

💡 **[Summary](2512.03405/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.03405)**

## Reinforcement Learning

### GoRL: An Algorithm-Agnostic Framework for Online Reinforcement Learning with Generative Policies

**Relevance:** GoRL addresses a core challenge in online RL: the trade-off between optimization stability and policy expressiveness. It proposes decoupling the optimization of a tractable latent policy from the synthesis of actions via a conditional generative decoder (e.g., diffusion or flow matching). This two-timescale update allows RL agents to model complex, multimodal action distributions stably, significantly advancing the methodology for applying RL to continuous-control tasks and complex behaviors.

💡 **[Summary](2512.02581/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.02581)**

### SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment

**Relevance:** This work introduces stable rank, an intrinsic, annotation-free quality signal derived from the effective dimensionality of a model's hidden states, as a reward for LLM alignment using Reinforcement Learning (SR-GRPO). This approach offers a scalable alternative to costly, subjective human annotations or vulnerable reward models, representing a significant methodological advance in using RL for aligning LLMs with desired behaviors based on internal model geometry rather than external supervision.

💡 **[Summary](2512.02807/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.02807)**

### PretrainZero: Reinforcement Active Pretraining

**Relevance:** PretrainZero proposes extending Reinforcement Learning (RL) from its typical use in domain-specific post-training (fine-tuning) to general pretraining on corpus data. It features active learning where a unified reasoning policy identifies informative content and reasons to predict it using RL, without relying on verifiable labels or supervised fine-tuning. This framework significantly breaks the 'verification data-wall,' leveraging RL to enhance the general reasoning capabilities of base models during the foundational pretraining stage.

💡 **[Summary](2512.03442/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.03442)**

## Explainable AI

### The Curious Case of Analogies: Investigating Analogical Reasoning in Large Language Models

**Relevance:** This paper uses interpretability tools, including analyzing representation propagation and surgically patching hidden states, to understand how LLMs encode and apply high-level relational concepts during analogical reasoning. By revealing that failures often stem from degraded structural alignment or missing relational information in mid-upper layers, this work provides crucial, granular explanations for complex cognitive failures, enabling researchers to improve model transparency and build trust in LLMs' reasoning abilities (XAI).

💡 **[Summary](2511.20344/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.20344)**

### C^2DLM: Causal Concept-Guided Diffusion Large Language Models

**Relevance:** C^2DLM addresses the lack of reasoning transparency in Diffusion Language Models (DLMs) by explicitly guiding the attention mechanism using a concept-level causal graph. By integrating causal knowledge, the model focuses its attention on genuine causal relationships between concepts, making the resulting reasoning process more structured and interpretable. This approach embeds a form of transparency directly into the model architecture, moving beyond post-hoc explanations toward inherently interpretable decision-making.

💡 **[Summary](2511.22146/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.22146)**

### CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization

**Relevance:** This paper tackles a critical XAI issue in agent systems: high accuracy masking unfaithful reasoning (e.g., ignoring tool outputs). CodeV introduces a faithfulness evaluation protocol and uses RL to enforce that the agent's intermediate tool-use steps are necessary and evidence-consistent. By focusing on verifiable process transparency and encouraging faithful behavior, this work is crucial for ensuring that complex agentic decisions are interpretable and trustworthy, essential for human users relying on AI agents.

💡 **[Summary](2511.19661/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19661)**

