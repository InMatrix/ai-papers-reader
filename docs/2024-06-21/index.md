---
layout: default
title: 2024-06-21
permalink: /2024-06-21/
---

# 2024-06-21

## AI for Software Development

### REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark

**Relevance:** This paper introduces RepoExec, a new benchmark focused on evaluating CodeLLMs' ability to generate executable and functionally correct code at the repository level. This is highly relevant to AI for Software Development as it moves evaluation beyond single-file snippets to complex, real-world development scenarios, emphasizing functional correctness and integration, which are critical for practical developer assistance tools like Copilot.

💡 **[Summary](2406.11927/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11927)**

### DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence

**Relevance:** DeepSeek-Coder-V2 is an open-source Mixture-of-Experts (MoE) model specifically aimed at code intelligence. Its continued pre-training significantly enhances coding, mathematical reasoning, and supports an extended context length (128K) and hundreds of programming languages. This directly contributes to the development of powerful, efficient AI tools for software developers, rivaling closed-source models in generating and understanding complex codebases.

💡 **[Summary](2406.11931/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11931)**

### Long Code Arena: a Set of Benchmarks for Long-Context Code Models

**Relevance:** This work addresses a key limitation in current code models: handling long, project-wide context. Long Code Arena provides six benchmarks covering tasks like library-based code generation, CI build repair, and project-level code completion. These tasks are essential for AI systems that assist professional developers with complex, multi-file software engineering challenges, directly improving the utility of AI in development workflows.

💡 **[Summary](2406.11612/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11612)**

## AI Agents

### DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning

**Relevance:** DigiRL focuses on training autonomous agents capable of device control through graphical user interfaces (GUIs) in 'in-the-wild' environments. This directly addresses core AI Agent research—creating systems that perceive environments, reason, and execute actions using tools (the GUI). The use of autonomous RL tackles real-world stochasticity, moving agents closer to reliable, independent operation.

💡 **[Summary](2406.11896/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11896)**

### $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**Relevance:** This paper introduces a benchmark to evaluate language agents on their ability to interact dynamically with human users and adhere to domain-specific policy guidelines. This is crucial for deployable AI agents, as it tests reliability, consistency, and alignment with human rules—key HCI aspects necessary for agents operating in real-world, interactive settings using API tools.

💡 **[Summary](2406.12045/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.12045)**

### AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology

**Relevance:** AgileCoder proposes a multi-agent system where different agents assume specific roles (e.g., Product Manager, Developer, Tester) to collaboratively develop software. This research exemplifies the complex planning, reasoning, and collaboration aspects of AI agents, structuring their interaction based on established human methodologies (Agile) to achieve large, complex goals.

💡 **[Summary](2406.11912/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11912)**

## LLM Evaluation Methods

### From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline

**Relevance:** This work introduces BenchBuilder, a pipeline to filter high-quality, challenging prompts from live crowdsourced data (Chatbot Arena) to create reliable offline benchmarks (Arena-Hard). This methodology improves evaluation by ensuring benchmarks align strongly with real-world user preferences and better differentiate model capabilities, enhancing the validity and utility of LLM assessment.

💡 **[Summary](2406.11939/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11939)**

### MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding

**Relevance:** MMBench-Video is a quantitative benchmark designed to rigorously evaluate Large Vision-Language Models (LVLMs) in holistic video understanding. It focuses on temporal comprehension and uses human-annotated questions and automated GPT-4 assessment. This addresses limitations in traditional benchmarks by testing complex reasoning skills in long-form, multi-modal contexts, pushing the boundary of LVLM evaluation.

💡 **[Summary](2406.14515/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.14515)**

### Hierarchical Prompting Taxonomy: A Universal Evaluation Framework for Large Language Models

**Relevance:** The Hierarchical Prompting Taxonomy (HPT) introduces a universal framework using five hierarchical prompting strategies to assign a score (HP-Score) that measures task complexity and LLM capability. This novel methodology provides a nuanced and standardized way to compare models and tasks, offering a clearer perspective on LLM strengths and weaknesses across varying cognitive demands.

💡 **[Summary](2406.12644/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.12644)**

## Reinforcement Learning

### DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning

**Relevance:** This paper presents DigiRL, an autonomous RL approach for training device control agents. It utilizes offline and offline-to-online RL stages, emphasizing the design of a scalable learning environment (Android) and policy optimization techniques tailored for real-world stochasticity. This is a direct application and advancement of RL principles for creating highly capable digital agents.

💡 **[Summary](2406.11896/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.11896)**

### Iterative Length-Regularized Direct Preference Optimization: A Case Study on Improving 7B Language Models to GPT-4 Level

**Relevance:** This work applies Direct Preference Optimization (DPO), a critical component of RLHF, iteratively. Crucially, it introduces length regularization to penalize verbosity, addressing a common usability issue (poor output quality/cognitive load) that arises from standard RL alignment. This demonstrates how RL alignment methods are adapted based on explicit human/HCI preferences.

📄 **[Full paper](https://arxiv.org/pdf/2406.11817)**

### BPO: Supercharging Online Preference Learning by Adhering to the Proximity of Behavior LLM

**Relevance:** BPO (Behavior LLM Proximal Optimization) focuses on advancing Direct Alignment from Preferences (DAP), a family of methods closely related to RLHF, by optimizing performance using online training samples. It emphasizes maintaining a trust region near the behavior model, improving the efficiency and effectiveness of preference learning for aligning LLMs to human desiderata.

📄 **[Full paper](https://arxiv.org/pdf/2406.12168)**

## Explainable AI

### Probabilistic Conceptual Explainers: Trustworthy Conceptual Explanations for Vision Foundation Models

**Relevance:** This paper introduces PACE, a variational Bayesian framework for generating trustworthy post-hoc conceptual explanations for Vision Transformers (ViTs). It establishes five desiderata for explanations (e.g., faithfulness, stability, parsimony), directly addressing the need for transparency and interpretability in complex vision models, a core concern of XAI research for building user trust.

📄 **[Full paper](https://arxiv.org/pdf/2406.12649)**

### Whiteboard-of-Thought: Thinking Step-by-Step Across Modalities

**Relevance:** Whiteboard-of-Thought is a prompting method that enables multimodal LLMs to externalize their visual and spatial reasoning steps by 'drawing' intermediate thoughts as images. This process makes the model's internal decision-making transparent and verifiable, offering a powerful form of intrinsic explainability and interpretability for multimodal reasoning tasks.

📄 **[Full paper](https://arxiv.org/pdf/2406.14562)**

### Estimating Knowledge in Large Language Models Without Generating a Single Token

**Relevance:** This work proposes KEEN, a probe that estimates model knowledge about an entity solely from internal computation. While not a traditional XAI technique, it provides intrinsic interpretability by revealing what the model 'knows' parametrically. This transparency helps users and developers identify knowledge gaps and guide retrieval augmentation, enhancing trust and debugging capabilities.

📄 **[Full paper](https://arxiv.org/pdf/2406.12673)**
