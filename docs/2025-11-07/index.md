---
layout: default
title: 2025-11-07
permalink: /2025-11-07/
---

# 2025-11-07

## AI for Software Development

### CodeClash: Benchmarking Goal-Orientated Software Engineering

**Relevance:** This paper introduces a benchmark that evaluates LLMs on high-level, goal-oriented software engineering tasks, moving beyond isolated coding challenges. The benchmark assesses strategic reasoning, iterative code development, and long-term codebase maintenance against competitive objectives. This directly addresses the need to evaluate AI systems on complex, open-ended objectives, which is critical for developing autonomous developer agents capable of tackling real-world human programming workflows.

💡 **[Summary](2511.00839/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.00839)**

## AI Agents

### The Collaboration Gap

**Relevance:** This study addresses the crucial challenge of effective collaboration among heterogeneous AI agents, revealing a significant 'collaboration gap' where agents performing well solo degrade substantially when paired. The findings motivate developing collaboration-aware training strategies and interaction designs for multi-agent systems, which is essential for scaling AI solutions and ensuring reliable human-agent teaming.

💡 **[Summary](2511.02687/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.02687)**

### ToolScope: An Agentic Framework for Vision-Guided and Long-Horizon Tool Use

**Relevance:** ToolScope is an agentic framework designed for long-horizon tasks that unifies global planning with local multimodal perception. It explicitly integrates external tools (Search, Code, Perceive) via an Agentic Executor to augment MLLMs. This directly addresses core research challenges in building autonomous agents capable of sustained, complex operation and effective resource utilization.

💡 **[Summary](2510.27363/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.27363)**

### GUI-AIMA: Aligning Intrinsic Multimodal Attention with a Context Anchor for GUI Grounding

**Relevance:** GUI grounding is a prerequisite for computer-use agents to interact with digital environments. GUI-AIMA proposes an efficient, coordinate-free framework that aligns MLLMs' intrinsic attention with grounding signals, enabling precise action prediction from natural language instructions. This is a foundational step for creating reliable and data-efficient agents capable of automating human digital tasks.

💡 **[Summary](2511.00810/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.00810)**

## LLM Evaluation Methods

### LiveTradeBench: Seeking Real-World Alpha with Large Language Models

**Relevance:** LiveTradeBench introduces a novel dynamic evaluation environment (live trading) that tests LLM agents on sequential decision-making under real-time uncertainty. This benchmark exposes a crucial gap between static evaluation scores and practical competence, highlighting the need for HCI-relevant evaluations that assess consistency, reliability, and trust in dynamic, high-stakes deployment scenarios.

💡 **[Summary](2511.03628/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.03628)**

### RiddleBench: A New Generative Reasoning Benchmark for LLMs

**Relevance:** RiddleBench evaluates flexible, multifaceted reasoning, a key component of human intelligence, using challenging puzzles. It serves as a diagnostic tool that reveals fundamental weaknesses in LLMs, such as hallucination cascades and self-confirmation bias. Identifying and quantifying these failure modes is essential for improving model robustness and aligning models with human expectations and safety requirements.

💡 **[Summary](2510.24932/)** 📄 **[Full paper](https://arxiv.org/pdf/2510.24932)**

### LTD-Bench: Evaluating Large Language Models by Letting Them Draw

**Relevance:** This benchmark transforms abstract numerical scores into observable visual outputs by requiring LLMs to generate drawings. This approach makes spatial reasoning limitations immediately apparent and intuitively understandable, bridging the gap between statistical performance and human assessment, thereby offering a powerful, accessible diagnostic method that aids in trust and transparency.

💡 **[Summary](2511.02347/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.02347)**

## Reinforcement Learning

### OpenSIR: Open-Ended Self-Improving Reasoner

**Relevance:** OpenSIR is a self-play framework where an LLM learns to generate and solve novel problems without external supervision or verifiable rewards, leading to open-ended mathematical discovery. This RL approach fundamentally addresses the dependency on annotated datasets, enabling agents to autonomously improve reasoning skills, which is a significant step toward general-purpose, self-improving agents.

💡 **[Summary](2511.00602/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.00602)**

### Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR

**Relevance:** The research modifies the Reinforcement Learning with Verifiable Rewards (RLVR) pipeline to retain moderately easy problems as implicit length regularizers. This achieves 'emergent brevity for free,' reducing LLM verbosity and inference cost without sacrificing accuracy, directly impacting the usability and cognitive load associated with interacting with RL-optimized models.

💡 **[Summary](2511.01937/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.01937)**

## Explainable AI

### Multi-Step Knowledge Interaction Analysis via Rank-2 Subspace Disentanglement

**Relevance:** This work introduces a novel rank-2 projection subspace to accurately disentangle the contributions of Context Knowledge (CK) and Parametric Knowledge (PK) during the generation of multi-step explanations (NLEs). This analytical framework is crucial for understanding the grounding of LLM decisions, allowing researchers to assess why explanations are generated and whether they are faithful to the source context.

💡 **[Summary](2511.01706/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.01706)**

### When Visualizing is the First Step to Reasoning: MIRA, a Benchmark for Visual Chain-of-Thought

**Relevance:** MIRA requires models to generate intermediate visual images (sketches, diagrams) to guide reasoning, mimicking human 'drawing to think.' This Visual Chain-of-Thought (V-CoT) provides explicit, visual explanations, making the model's complex reasoning process transparent and inspectable, which is a direct mechanism for achieving better interpretability in XAI.

💡 **[Summary](2511.02779/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.02779)**

### VCode: a Multimodal Coding Benchmark with SVG as Symbolic Visual Representation

**Relevance:** VCode utilizes SVG code as an inherently interpretable and executable symbolic representation of visual understanding. Since code provides a clear, compositional sequence of operations, it offers a transparent trace of the model's decision-making process, serving as a powerful form of counterfactual explanation for multimodal tasks.

💡 **[Summary](2511.02778/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.02778)**

