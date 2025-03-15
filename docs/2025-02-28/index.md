---
layout: default
title: 2025-02-28
permalink: /2025-02-28/
---

# 2025-02-28

## Generative AI for Assisting Software Developers

### SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution

**Relevance:** This paper directly addresses how LLMs can be used to assist in software engineering tasks by leveraging reinforcement learning on open-source software evolution data.  The approach allows LLMs to recover developer reasoning processes and solutions from code snapshots, changes, and events like issues and pull requests.  The results indicate improved performance on real-world GitHub issues and even generalized reasoning skills, showing promise for applying LLMs to code-related tasks.

💡 **[Summary](2502.18449/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.18449)**

### MutaGReP: Execution-Free Repository-Grounded Plan Search for Code-Use

**Relevance:** MutaGReP introduces a novel approach for providing LLMs with relevant context from large code repositories to complete coding tasks.  Instead of using the entire repository or relying on the LLM to navigate it, MutaGReP searches for plans that decompose a user request into natural language steps grounded in the codebase. This involves neural tree search and a symbol retriever. This allows smaller models to rival GPT-4o's performance with significantly less of the code repository added into the LLM's context, supporting the concept of using LLMs to navigate existing code to solve development tasks.

💡 **[Summary](2502.15872/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.15872)**

### CritiQ: Mining Data Quality Criteria from Human Preferences

**Relevance:** This paper introduces CritiQ, a method for automatically mining data quality criteria from human preferences to improve the training data used for language models. This is relevant because higher quality training data can result in models that are more reliable code generators. By improving the LLM training data, CritiQ indirectly assists software developers by leading to improved tooling.

💡 **[Summary](2502.19279/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.19279)**

## AI Agents

### Towards an AI co-scientist

**Relevance:** This paper describes the development of an AI co-scientist, a multi-agent system built on Gemini 2.0, designed to generate novel scientific hypotheses and proposals. It utilizes a generate, debate, and evolve approach inspired by the scientific method.  The system's architecture and automated evaluations demonstrate its potential to augment scientific discovery in biomedical areas, showcasing its capabilities as an independent agent. This is relevant because it can apply to the software domain, where AI agents can contribute to software development and research.

💡 **[Summary](2502.18864/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.18864)**

### Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents

**Relevance:** Curie is an AI agent framework designed to embed rigor into the scientific experimentation process. It uses an intra-agent rigor module to enhance reliability, an inter-agent rigor module to maintain methodical control, and an experiment knowledge module to enhance interpretability.  The design for rigorous experimentation with well-defined steps and the benchmark provide a strong foundation that can inform the design of AI agents in other domains, including software development.

💡 **[Summary](2502.16069/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.16069)**

### VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model

**Relevance:** This paper presents an environment-free reinforcement learning framework for training GUI agents using a Value Environment Model (VEM).  VEM predicts state-action values directly from offline data, focusing on semantic reasoning. This approach avoids costly interactions and distribution shift issues. The work shows how to train GUI agents without relying on an environment. This framework has potential implications for creating more robust and efficient AI agents that can interact with software interfaces.

💡 **[Summary](2502.18906/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.18906)**

## Prompt Engineering Techniques

### Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?

**Relevance:** This paper introduces DeltaBench to analyze the effectiveness and efficiency of long Chain-of-Thought (CoT) reasoning in LLMs and measure the critique abilities of existing LLMs on these CoTs. This is relevant because understanding how to elicit, analyze, and improve chain-of-thought prompting can lead to more reliable and accurate responses from LLMs, which is crucial for AI assistants.

💡 **[Summary](2502.19361/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.19361)**

### Prompt-to-Leaderboard

**Relevance:** This paper introduces Prompt-to-Leaderboard (P2L), a method for creating leaderboards specific to a prompt. This approach enables unsupervised task-specific evaluation, optimal routing of queries to models, personalization, and automated evaluation of model strengths and weaknesses. This can be used to engineer prompts to achieve the best model performance.

💡 **[Summary](2502.14855/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.14855)**

## Human-in-the-loop Machine Learning

### Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems

**Relevance:** This paper proposes agentic reward modeling, a reward system that combines reward models with verifiable correctness signals. The work combines human preference rewards with verifiable signals like factuality and instruction following to provide more reliable rewards. It shows how including human feedback allows LLMs to incorporate human intuition and real-world knowledge to solve certain problems.

💡 **[Summary](2502.19328/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.19328)**

### CritiQ: Mining Data Quality Criteria from Human Preferences

**Relevance:** CritiQ is a data selection method that automatically mines data quality criteria from human preferences. This method employs a manager agent to evolve quality criteria and worker agents to make pairwise judgments. CritiQ can be used to filter training data for LLMs in a way that aligns with human preferences, leading to more reliable and useful outputs.

💡 **[Summary](2502.19279/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.19279)**

## Techniques for Explaining AI Behavior

### LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models

**Relevance:** This paper introduces LaTIM, a token-level decomposition method for Mamba models that enables fine-grained interpretability. Understanding how Mamba selectively processes sequences across layers can reveal the model's reasoning behind its decisions, allowing developers to better understand and trust its outputs. This is relevant to XAI because LaTIM offers insights into the inner workings of SSMs, which is a step towards more transparent AI.

💡 **[Summary](2502.15612/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.15612)**

### Rank1: Test-Time Compute for Reranking in Information Retrieval

**Relevance:** The Rank1 model uses a reasoning language model for distillation to improve the performance of a smaller model, and importantly, has explainable reasoning chains that can be given to users or RAG-based systems. Rank1 shows how test-time compute allows for a fundamentally new type of explainable and performant reranker model for search, relevant to XAI due to its transparency and user-understandable reasoning.

💡 **[Summary](2502.18418/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.18418)**

