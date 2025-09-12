---
layout: default
title: 2025-09-12
permalink: /2025-09-12/
---

# 2025-09-12

## AI for Software Development

### EnvX: Agentize Everything with Agentic AI

**Relevance:** This paper introduces EnvX, a framework that transforms GitHub repositories into intelligent, autonomous AI agents capable of natural language interaction and inter-agent collaboration. This directly supports AI for software development by automating not just code generation, but the entire process of understanding, initializing dependencies, and operationalizing repository functionality, enabling developers to efficiently reuse software components and overcome manual, error-prone integration barriers.

💡 **[Summary](2509.08088/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08088)**

## AI Agents

### AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

**Relevance:** This paper introduces AgentGym-RL, a novel framework for training LLM agents to make multi-turn intelligent decisions in complex, real-world tasks using reinforcement learning. It focuses on agents acquiring knowledge and skills through exploration and interaction, without relying on supervised fine-tuning. The framework's modular architecture, support for diverse environments, and focus on exploration-exploitation balance directly align with core aspects of AI agent research, emphasizing autonomous problem-solving and adaptation.

💡 **[Summary](2509.08755/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08755)**

### EnvX: Agentize Everything with Agentic AI

**Relevance:** EnvX enables the creation of intelligent, autonomous agents from GitHub repositories. These agents perceive environments (repository structure, APIs), reason about tasks, plan actions, and execute them by integrating tools and collaborating. The framework's emphasis on natural language interaction, inter-agent collaboration, and automating complex tasks like dependency initialization and operationalization directly addresses the core goals of AI agent research, using LLMs as a 'brain' for system understanding and execution.

💡 **[Summary](2509.08088/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08088)**

### SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents

**Relevance:** This work focuses on developing autonomous single-agent models for 'Deep Research' tasks, which require extensive search and reasoning over many sources with minimal external guidance. The paper emphasizes agents that dynamically determine their next action based on context, without manual directives, and proposes a reinforcement learning recipe for enhancing agentic skills while preserving reasoning ability. This directly contributes to the field of AI agents, particularly in creating self-sufficient, reasoning-oriented systems with tool-use capabilities.

💡 **[Summary](2509.06283/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.06283)**

## LLM Evaluation Methods

### HumanAgencyBench: Scalable Evaluation of Human Agency Support in AI Assistants

**Relevance:** This paper introduces HumanAgencyBench (HAB), a benchmark integrating philosophical and scientific theories of human agency with AI-assisted evaluation methods. HAB measures an AI assistant's tendency to Ask Clarifying Questions, Avoid Value Manipulation, Correct Misinformation, Defer Important Decisions, Encourage Learning, and Maintain Social Boundaries. From an HCI perspective, this is highly relevant as it focuses on critical aspects of user satisfaction, trust, safety, and alignment with human values, addressing how LLMs impact human control and decision-making.

💡 **[Summary](2509.08494/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08494)**

### SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge

**Relevance:** This paper introduces SimpleQA Verified, a rigorous 1,000-prompt benchmark for evaluating LLM short-form factuality. It addresses limitations of existing benchmarks by employing a multi-stage filtering process (de-duplication, topic balancing, source reconciliation) to produce a more reliable and challenging evaluation set, alongside improvements in the autorater prompt. This directly contributes to LLM evaluation by providing a higher-fidelity tool to track progress in parametric model factuality, measure hallucination rates, and enhance user trust in information retrieved from LLMs.

💡 **[Summary](2509.07968/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.07968)**

### Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet

**Relevance:** This work evaluates the effectiveness of increasing test-time computation in reasoning models for knowledge-intensive tasks, focusing on factual accuracy and hallucination rates. It highlights that extended reasoning does not consistently improve accuracy and can even increase hallucinations, suggesting that current methods may induce confirmation bias. From an HCI perspective, this research is crucial for understanding LLM robustness, reliability, and the potential for cognitive load or misinformation when users interact with 'thinking' models, informing safer deployment and interaction design for complex information retrieval.

💡 **[Summary](2509.06861/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.06861)**

## Reinforcement Learning

### A Survey of Reinforcement Learning for Large Reasoning Models

**Relevance:** This paper provides a comprehensive survey of recent advances in Reinforcement Learning (RL) for reasoning with Large Language Models (LLMs), identifying RL as a foundational methodology for transforming LLMs into Large Reasoning Models (LRMs). It covers foundational components, core problems, training resources, and downstream applications. This survey is highly relevant to the RL topic as it maps the current landscape, challenges, and future opportunities in applying RL to enhance complex logical tasks, including policy optimization and multi-agent RL implications for reasoning systems.

💡 **[Summary](2509.08827/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08827)**

### AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

**Relevance:** This paper introduces AgentGym-RL, a unified, interactive reinforcement learning (RL) framework for training LLM agents for multi-turn decision-making in diverse, realistic environments. It features a modular architecture and supports mainstream RL algorithms, along with a training approach (ScalingInter-RL) for exploration-exploitation balance and stable RL optimization. This is highly relevant as it directly addresses policy optimization, exploration-exploitation, and novel agent environment design within the context of LLM-powered agents, providing a practical framework for complex behavior learning.

💡 **[Summary](2509.08755/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.08755)**

### Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning

**Relevance:** This paper analyzes how Reinforcement Learning (RL) enhances complex reasoning abilities in LLMs, uncovering an emergent hierarchical reasoning with a two-phase dynamic: initial procedural correctness followed by strategic planning. It proposes HIerarchy-Aware Credit Assignment (HICRA) to concentrate optimization on high-impact planning tokens. This is highly relevant as it delves into policy optimization mechanisms, how RL shapes agent learning, and proposes an algorithm to improve the efficiency of learning complex behaviors, contributing to the understanding of emergent capabilities.

💡 **[Summary](2509.03646/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.03646)**

## Explainable AI

### From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers

**Relevance:** This paper systematically investigates how and when hallucinations arise in pre-trained transformer models by analyzing concept representations captured by sparse autoencoders. It identifies that growing input uncertainty leads to the activation of input-insensitive semantic features, causing hallucinated output. This work is highly relevant to XAI as it provides mechanistic insight into a critical failure mode of AI, enhancing transparency by explaining the internal processing that leads to unreliable behaviors, which is crucial for building trust and aligning AI models with human values.

💡 **[Summary](2509.06938/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.06938)**

### Mechanistic interpretability for steering vision-language-action models

**Relevance:** This paper introduces the first framework for interpreting and steering Vision-Language-Action (VLA) models via their internal representations. It projects feedforward activations onto token embedding basis, identifying 'sparse semantic directions' (e.g., speed, direction) causally linked to action selection. This allows for real-time behavioral control without fine-tuning or reward signals. This work is highly relevant to XAI as it directly addresses transparency and interpretability by making AI decision-making processes more understandable and steerable, establishing a new paradigm for transparent and controllable embodied agents.

💡 **[Summary](2509.00328/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.00328)**

### Focusing by Contrastive Attention: Enhancing VLMs' Visual Reasoning

**Relevance:** This paper investigates attention patterns in Vision-Language Models (VLMs), discovering correlations between visual complexity, attention entropy, and reasoning performance. It proposes Contrastive Attention Refinement for Visual Enhancement (CARVE), a training-free method that extracts task-relevant visual signals through attention contrasting at the pixel level. This work is highly relevant to XAI as it provides insights into 'attention visualization' by explaining what parts of the input the model focuses on, offering a method to enhance transparency and interpretability of VLM visual reasoning without modifying the model architecture.

💡 **[Summary](2509.06461/)** 📄 **[Full paper](https://arxiv.org/pdf/2509.06461)**

