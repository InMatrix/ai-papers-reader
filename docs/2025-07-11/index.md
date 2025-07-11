---
layout: default
title: 2025-07-11
permalink: /2025-07-11/
---

# 2025-07-11

## AI for Software Development

### Rethinking Verification for LLM Code Generation: From Generation to Testing

**Relevance:** This paper directly addresses the use of Large Language Models (LLMs) in code generation, a core AI for Software Development task. It highlights the limitations of current evaluation benchmarks, which often miss subtle faults, inflating performance. From an HCI perspective, this means developers might implicitly trust incomplete AI-generated code. The paper proposes methods for generating more thorough test cases and a human-LLM collaborative approach (SAGA) to enhance test quality and coverage, aiming for a more reliable foundation for LLM-based code generation and improving the trustworthiness and utility of AI tools for software developers.

💡 **[Summary](2507.06920/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.06920)**

### Coding Triangle: How Does Large Language Model Understand Code?

**Relevance:** This research provides a systematic framework, 'Code Triangle,' to evaluate LLMs' programming competence across dimensions like editorial analysis, code implementation, and test case generation—all vital for AI in software development. It uncovers that while LLMs can form self-consistent solutions, they often lack the diversity and robustness of human programmers, largely due to training data biases. For HCI, understanding these limitations is crucial for designing effective developer tools. The paper suggests leveraging human-generated data and model mixtures to improve LLM performance and robustness, directly influencing how AI assists developers and how users can interactively enhance AI-generated code.

💡 **[Summary](2507.06138/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.06138)**

### AutoTriton: Automatic Triton Programming with Reinforcement Learning in LLMs

**Relevance:** AutoTriton introduces the first model dedicated to Triton programming, powered by reinforcement learning (RL), to automate kernel development for deep learning. This is a direct application of AI for software development, specifically in optimizing low-level computational units for hardware. The manual tuning of parameters for optimal performance creates significant barriers for developers; AutoTriton aims to alleviate this by using LLMs for code generation and optimization. From an HCI viewpoint, this work promises to simplify complex, expert-level programming tasks, making high-performance kernel development more accessible and efficient for engineers, reducing cognitive load and empirical tuning effort.

💡 **[Summary](2507.05687/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05687)**

## AI Agents

### MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Relevance:** MIRIX directly addresses a critical limitation of AI agents: their memory capabilities. By introducing a modular, multi-agent memory system with distinct memory types (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault), it enables LLM-based agents to personalize, abstract, and reliably recall user-specific information, including multimodal experiences. From an HCI perspective, improved memory means agents can maintain context, understand user preferences over time, and provide more consistent and helpful interactions. This significantly enhances the usability and effectiveness of AI agents in complex, long-term user-defined goals, making them more adaptable and reliable human collaborators.

💡 **[Summary](2507.07957/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.07957)**

### How to Train Your LLM Web Agent: A Statistical Diagnosis

**Relevance:** This paper investigates the training of LLM-based web agents, which are designed to autonomously interact with graphical user interfaces (GUIs) to complete tasks. It addresses the challenges of multi-step web interactions and the high computational costs of training. The research identifies effective hyperparameters for a two-stage training pipeline (SFT + on-policy RL) to improve agent performance and efficiency. For HCI, this work is crucial as it directly impacts the reliability and usability of web agents. Better trained agents mean more successful task completion, reduced user frustration, and the potential for agents to handle more complex, human-like digital interactions.

💡 **[Summary](2507.04103/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.04103)**

### GTA1: GUI Test-time Scaling Agent

**Relevance:** GTA1 introduces a GUI agent designed for autonomous operation across platforms by interacting with visual elements, addressing challenges in task planning ambiguity and accurate action grounding in complex interfaces. It employs a test-time scaling method with a judge model for optimal action selection and uses reinforcement learning for improved visual grounding. From an HCI perspective, GTA1 enhances the agent's ability to 'understand' and interact with digital environments, making it more robust for automating user tasks. This leads to more reliable human-agent collaboration on software interfaces, improving user productivity and reducing the need for direct manual intervention.

💡 **[Summary](2507.05791/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05791)**

## LLM Evaluation Methods

### RabakBench: Scaling Human Annotations to Construct Localized Multilingual Safety Benchmarks for Low-Resource Languages

**Relevance:** RabakBench is a novel multilingual safety benchmark localized to Singapore's linguistic context, addressing the poor performance of LLMs and safety classifiers in low-resource languages. It uses a scalable pipeline involving adversarial example generation, semi-automated multi-label annotation, and high-fidelity translation. From an HCI perspective, this work is critical for evaluating the ethical and bias aspects of LLMs, ensuring fairness and inclusivity for diverse user populations. By revealing performance degradation in context-specific settings, RabakBench provides a reproducible framework for building localized safety datasets, which is essential for ensuring LLM alignment with varied user needs and cultural norms.

💡 **[Summary](2507.05980/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05980)**

### ModelCitizens: Representing Community Voices in Online Safety

**Relevance:** This paper highlights the subjectivity of toxic language detection and the limitations of current models trained on annotations that collapse diverse perspectives. ModelCitizens introduces a dataset with annotations across diverse identity groups and augments posts with LLM-generated conversational scenarios to capture context. From an HCI standpoint, this work is crucial for developing inclusive content moderation systems that respect varied community norms and lived experiences. It directly addresses the ethical and bias evaluation of AI by emphasizing community-informed annotation, thereby improving user satisfaction and trust in online platforms by ensuring fairness and mitigating the negative impacts of AI-driven moderation.

💡 **[Summary](2507.05455/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05455)**

### LOOM-Scope: a comprehensive and efficient LOng-cOntext Model evaluation framework

**Relevance:** LOOM-Scope proposes a comprehensive and efficient framework for evaluating the long-context performance of large language models (LLMs). It addresses the inconsistencies in existing benchmarks and the high computational cost of evaluation by standardizing settings and supporting efficient inference acceleration methods. From an HCI perspective, understanding LLMs' long-context capabilities is vital for designing interactive applications requiring sustained dialogue or complex document analysis. By providing a reliable and efficient evaluation framework, LOOM-Scope helps researchers and developers assess model performance against user needs, understand limitations, and ensure that LLMs can effectively handle the cognitive load and complexity of real-world human interactions.

💡 **[Summary](2507.04723/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.04723)**

## Reinforcement Learning

### Perception-Aware Policy Optimization for Multimodal Reasoning

**Relevance:** This paper introduces Perception-Aware Policy Optimization (PAPO), an extension of Reinforcement Learning with Verifiable Rewards (RLVR), specifically designed for multimodal reasoning tasks. It identifies and addresses the bottleneck of visual input perception in current RLVR applications for LLMs. By integrating an Implicit Perception Loss, PAPO encourages models to learn perception while reasoning, entirely from internal supervision. From an HCI perspective, this research is significant because it aims to make multimodal AI systems more robust and less prone to perception errors, leading to more reliable and trustworthy interactions when humans engage with AI that processes both text and visuals.

💡 **[Summary](2507.06448/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.06448)**

### RLVER: Reinforcement Learning with Verifiable Emotion Rewards for Empathetic Agents

**Relevance:** RLVER is a pioneering reinforcement learning framework that leverages verifiable emotion rewards from simulated users to enhance the emotional intelligence (EQ) of Large Language Models (LLMs). This innovative approach guides LLM learning using deterministic emotion scores during dialogue rollouts. From an HCI standpoint, this work is profoundly impactful as it directly addresses the development of emotionally intelligent AI agents. By improving empathy, RLVER can lead to more natural, supportive, and trustworthy human-AI interactions, enhancing user satisfaction and reducing cognitive and emotional load, especially in applications requiring nuanced social understanding and responsiveness.

💡 **[Summary](2507.03112/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.03112)**

### High-Resolution Visual Reasoning via Multi-Turn Grounding-Based Reinforcement Learning

**Relevance:** This paper introduces Multi-turn Grounding-based Policy Optimization (MGPO), an end-to-end reinforcement learning (RL) framework for Large Multi-modal Models (LMMs) to perform high-resolution visual reasoning. It enables LMMs to iteratively focus on relevant visual regions through automatic cropping, based on model-predicted grounding coordinates. Crucially, this approach teaches LMMs robust grounding abilities during RL training without costly explicit grounding annotations. From an HCI perspective, MGPO enhances the interpretability and efficiency of multimodal AI by allowing models to 'focus' on specific visual details relevant to a query, making their reasoning more transparent and reliable for human users.

💡 **[Summary](2507.05920/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.05920)**

## Explainable AI

### Towards Solving More Challenging IMO Problems via Decoupled Reasoning and Proving

**Relevance:** This paper proposes a novel framework that decouples high-level reasoning from low-level proof generation for automated theorem proving. By utilizing distinct specialized models—a Reasoner for strategic subgoal lemmas and a Prover for verification—it liberates the model's full reasoning potential. From an Explainable AI (XAI) perspective, this modular design inherently enhances transparency. Separating the complex reasoning process into distinct, more manageable stages makes the AI's decision-making flow more interpretable. Users can better trace the logical steps taken by the AI, which is crucial for trust and understanding, especially in high-stakes domains like formal mathematics.

💡 **[Summary](2507.06804/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.06804)**

