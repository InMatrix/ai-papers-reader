---
layout: default
title: 2026-05-08
permalink: /2026-05-08/
---

# 2026-05-08

## AI for Software Development

### SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies

**Relevance:** This paper introduces a comprehensive 68-metric framework for evaluating coding agents that autonomously generate full-stack software. It identifies a "specification bottleneck" where platforms oversimplify business requirements, a critical HCI challenge. By assessing interaction modes and production readiness, it provides insights into how AI can better support the iterative and multi-role nature of software development, moving beyond simple code-level benchmarks to evaluate AI as a virtual agency capable of understanding complex user needs and making architectural decisions.

💡 **[Summary](2605.04637/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.04637)**

### Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes

**Relevance:** This paper explores a closed-loop system where specialist agents autonomously conduct research, including generating code edits and training recipes. The focus on an "auditable trajectory" of proposals and code diffs makes it highly relevant for AI-assisted development. It demonstrates how agents can translate external feedback into program-level modifications, highlighting the potential for AI to manage complex, long-horizon software and research tasks independently while maintaining a transparent record of all code changes and experimental outcomes.

💡 **[Summary](2605.05724/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.05724)**

## AI Agents

### AI Co-Mathematician: Accelerating Mathematicians with Agentic AI

**Relevance:** This paper presents an interactive workbench for human-AI collaboration in mathematical research. It features an asynchronous, stateful workspace that manages uncertainty and refines user intent—key considerations for HCI. By mirroring human collaborative workflows and producing native mathematical artifacts, it demonstrates how agents can support exploratory and iterative cognitive tasks, providing a model for interactive AI systems that enhance human expertise in highly specialized fields through independent tool use and literature search.

💡 **[Summary](2605.06651/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.06651)**

### Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning

**Relevance:** This research addresses the challenge of agent self-evolution by training a single policy for skill selection, utilization, and distillation using a shared task-outcome objective. This unified reinforcement learning approach enables agents to maintain a persistent skill library and adapt to new challenges independently. From an HCI perspective, this is significant for developing more autonomous and self-improving systems that can efficiently learn, store, and reuse strategies across diverse digital environments based on experience.

💡 **[Summary](2605.06130/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.06130)**

### ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

**Relevance:** ARIS introduces an open-source harness for autonomous research that uses adversarial multi-agent collaboration to ensure the integrity of findings. By pairing an executor with a reviewer from a different model family, it addresses the HCI challenge of trust in long-horizon agentic workflows. Its assurance layer, which audits claims against raw evidence and manages a persistent research wiki, provides a framework for building more reliable, transparent, and self-improving autonomous systems for complex scientific discovery.

💡 **[Summary](2605.03042/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.03042)**

## LLM Evaluation Methods

### XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity

**Relevance:** This paper introduces a comprehensive benchmark for evaluating LLM safety and cultural sensitivity across 10 country-language pairs. It addresses the English-centric bias of current evaluations and introduces metrics to distinguish between principled refusal and generation failure. This is crucial for HCI as it ensures that AI systems are safe, inclusive, and culturally aware, facilitating better alignment with the diverse values and specific harms relevant to a global user base through human-in-the-loop annotation.

💡 **[Summary](2605.05662/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.05662)**

### MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills

**Relevance:** This study develops a domain-specific audit framework for medical research agent skills, focusing on scientific integrity and methodological validity. It compares system-driven audits with human expert reviews, highlighting the importance of specialized safeguards in high-stakes domains. For HCI, this work underscores the need for structured, human-in-the-loop evaluation workflows to govern the deployment of modular AI capabilities in professional contexts, ensuring that agent behaviors remain aligned with rigorous scientific and safety standards.

💡 **[Summary](2604.20441/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.20441)**

### CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing

**Relevance:** This research introduces CreativityBench to evaluate the creative problem-solving abilities of LLMs through affordance-based tool repurposing. By testing models on their ability to identify non-obvious uses for objects under physical constraints, it reveals significant gaps in current agent reasoning. This benchmark is relevant to HCI as it provides a standardized way to assess how well AI agents can understand and interact with the physical world in novel ways, beyond canonical instructions.

💡 **[Summary](2605.02910/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.02910)**

## Reinforcement Learning

### Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning

**Relevance:** This survey provides a modular taxonomy (GFCR) for rollout strategies in LLM reinforcement learning, decomposing the process into four stages. It addresses common pathologies in agent training and suggests mitigation levers for building reproducible and compute-efficient pipelines. This is relevant to HCI as it offers a systematic framework for designing the training environments and feedback loops that shape agent behavior, ensuring they are better aligned with human reasoning and task requirements.

💡 **[Summary](2605.02913/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.02913)**

### MARBLE: Multi-Aspect Reward Balance for Diffusion RL

**Relevance:** MARBLE introduces a gradient-space optimization framework for balancing multiple rewards in reinforcement learning, which is essential for aligning diffusion models with complex human preferences. By harmonizing gradients from multiple evaluation criteria without manual weighting, it allows for more precise control over various quality axes. This contributes to HCI by providing tools to better align generative models with multi-faceted human subjective judgments, ensuring that diverse aesthetic and functional requirements are optimized simultaneously.

💡 **[Summary](2605.06507/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.06507)**

### When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

**Relevance:** This paper uses RL to learn "disclosure policies" that decide when an agent should deliberate privately versus commit to public output. This research addresses the "silence tax" in interactive interfaces, directly impacting user experience by balancing response latency with reasoning accuracy. It provides an HCI-centric optimization of the communication pace between humans and AI, using reinforcement learning to recover performance while managing the cognitive load and waiting time for the user.

💡 **[Summary](2605.03314/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.03314)**

## Explainable AI

### Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation

**Relevance:** This paper introduces a visual attribution framework that provides pixel-level evidence for claims made during iterative RAG. By outputting precise bounding boxes on document screenshots, it eliminates visual semantic loss and makes the reasoning process transparent. This is a major contribution to XAI and HCI, as it allows users to quickly verify information sources in complex layouts like slides or PDFs, significantly enhancing the interpretability and trustworthiness of multi-hop reasoning systems.

💡 **[Summary](2605.01284/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.01284)**

### The Granularity Axis: A Micro-to-Macro Latent Direction for Social Roles in Language Models

**Relevance:** This research identifies a structured latent direction in LLM hidden states that corresponds to the granularity of social roles, from individuals to institutions. By showing this axis is causally manipulable through activation steering, it offers a way to interpret and control model behavior more transparently. This contributes to XAI by revealing how models internally organize social concepts and providing methods for more interpretable control over model persona and response style.

💡 **[Summary](2605.06196/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.06196)**

### A Foundation Model for Zero-Shot Logical Rule Induction

**Relevance:** This paper introduces the Neural Rule Inducer (NRI), which learns interpretable, symbolic logical rules from data in a zero-shot manner. Unlike "black-box" models, NRI focuses on inducing rules that are human-readable and generalize across different domains. This is a core goal of XAI, as providing explicit rules rather than opaque predictions allows users to understand, verify, and trust the logic behind an AI system's inductive reasoning process, facilitating easier debugging and human oversight.

💡 **[Summary](2605.04916/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.04916)**

