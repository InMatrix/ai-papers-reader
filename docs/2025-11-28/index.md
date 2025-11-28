---
layout: default
title: 2025-11-28
permalink: /2025-11-28/
---

# 2025-11-28

## AI for Software Development

### HunyuanOCR Technical Report

**Relevance:** HunyuanOCR is a lightweight (1B parameters) Vision-Language Model dedicated to end-to-end OCR tasks, including text spotting, parsing, and information extraction from documents. This is highly relevant for software development tasks involving processing legacy code documentation, extracting data from diagrams, or automating structured data intake. By adopting an efficient, end-to-end architecture and leveraging RL for performance gains, it provides a superior, lightweight tool that simplifies deployment and reduces error propagation in developer pipelines.

💡 **[Summary](2511.19575/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19575)**

## AI Agents

### Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

**Relevance:** Agent0-VL introduces a self-evolving agent with two synergistic roles: a Solver and a Verifier. The Verifier uses tool-integrated reasoning to provide fine-grained, evidence-grounded self-rewards, enabling the agent to refine its reasoning continually. This design greatly benefits HCI by increasing agent reliability and trustworthiness; the ability to self-verify and self-repair complex reasoning steps means the agent can offer more transparent and robust performance in tool-use and complex visual tasks.

💡 **[Summary](2511.19900/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19900)**

### Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution

**Relevance:** This work addresses task scheduling for embodied agents by introducing ORS3D, a task requiring agents to leverage Operations Research knowledge to minimize total completion time via parallel task execution. The proposed model, GRANT, generates efficient schedules and grounded actions. This directly impacts human-agent collaboration and utility by ensuring agents operate efficiently and logically in shared 3D environments, fulfilling complex instructions faster and more intuitively for the user.

💡 **[Summary](2511.19430/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19430)**

### Latent Collaboration in Multi-Agent Systems

**Relevance:** LatentMAS enables collaboration among LLM agents directly within a continuous latent space, bypassing slow, token-heavy text-based communication. This results in significantly faster inference (4x speedup) and reduced token usage while improving reasoning quality. For HCI, this efficiency is paramount for building highly responsive, real-time multi-agent systems where synchronous collaboration and immediate feedback are essential for an effective user experience.

💡 **[Summary](2511.20639/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.20639)**

## LLM Evaluation Methods

### Position: The Complexity of Perfect AI Alignment -- Formalizing the RLHF Trilemma

**Relevance:** This paper formalizes the inherent tension in RLHF alignment as the Trilemma: balancing representativeness, tractability, and robustness. From an HCI perspective, this is a fundamental evaluation paper, as it proves that achieving perfect alignment across diverse human values at scale is computationally intractable. This framework is essential for researchers designing alignment strategies, forcing them to explicitly acknowledge and navigate trade-offs concerning fairness, bias, and robustness in user-facing systems.

💡 **[Summary](2511.19504/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19504)**

### Cognitive Foundations for Reasoning and Their Manifestation in LLMs

**Relevance:** This work synthesizes a taxonomy of 28 cognitive elements from human cognitive science to provide a fine-grained evaluation framework for LLM reasoning traces. By comparing model traces against human think-aloud data, it offers a principled, human-centric methodology to diagnose reasoning failures. This approach moves beyond simple accuracy metrics, providing critical insights into how models reason, which is vital for designing robust, reliable, and interpretable AI systems.

💡 **[Summary](2511.16660/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.16660)**

### Multimodal Evaluation of Russian-language Architectures

**Relevance:** The introduction of Mera Multi, an open multimodal evaluation framework for Russian-spoken architectures, directly addresses critical HCI concerns regarding inclusivity and cultural bias. By constructing 18 new tasks with attention to Russian cultural and linguistic specificity, the paper provides a methodology for creating culturally sensitive benchmarks in typologically diverse languages, ensuring that LLM evaluation accounts for global representativeness and fairness.

💡 **[Summary](2511.15552/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.15552)**

## Reinforcement Learning

### Soft Adaptive Policy Optimization

**Relevance:** SAPO improves the stability and performance of RL training for LLMs (e.g., in RLHF) by using a smooth, temperature-controlled gate instead of rigid clipping. Since RL is the primary mechanism for aligning LLMs to human preferences and values, improving RL stability is crucial. SAPO provides a more reliable and sample-efficient path to training aligned models, which directly translates to more consistent and trustworthy behavior in user interactions.

💡 **[Summary](2511.20347/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.20347)**

### Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs

**Relevance:** This work introduces VISTA-Gym, a scalable environment designed specifically for training VLMs using RL to master tool selection, invocation, and coordination. VISTA-Gym provides verifiable feedback signals essential for effective RL training. This infrastructure is critical for developing sophisticated agents capable of practical human-agent collaboration, allowing researchers to efficiently train robust policies that can reason and act effectively using external tools as guided by human instructions.

💡 **[Summary](2511.19773/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.19773)**

### Diverse Video Generation with Determinantal Point Process-Guided Policy Optimization

**Relevance:** DPP-GRPO uses reinforcement learning to explicitly optimize for diversity in text-to-video (T2V) generation outputs, addressing the problem of low-diversity samples. By imposing diminishing returns on redundant samples via DPP, the RL policy maximizes the range of plausible outcomes. From an HCI perspective, maximizing output diversity is vital for creative applications, ensuring users have sufficient choice and control over the generative process.

💡 **[Summary](2511.20647/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.20647)**

## Explainable AI

### I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

**Relevance:** I-GLIDE is a framework for Remaining Useful Life (RUL) prediction that provides 'interpretable, mechanism-specific diagnostics' by isolating sensor subsets to model specific degradation mechanisms. It also quantifies uncertainty in these health indicators. This level of transparency is vital for XAI in high-stakes operational systems (e.g., aerospace, manufacturing), allowing human operators to understand the 'why' behind a prediction and fostering trust in automated prognostics.

💡 **[Summary](2511.21208/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.21208)**

### Cognitive Foundations for Reasoning and Their Manifestation in LLMs

**Relevance:** This research analyzes LLM reasoning traces against a taxonomy of human cognitive primitives. By identifying which cognitive elements (e.g., meta-cognitive controls, diverse representations) are correlated with human success but under-utilized by models, the framework enables diagnosis of reasoning failures. This detailed diagnosis provides powerful insights into model behavior, serving as a deep form of XAI that can guide the development of models that reason in human-like, and thus more understandable, ways.

💡 **[Summary](2511.16660/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.16660)**

