---
layout: default
title: 2025-05-16
permalink: /2025-05-16/
---

# 2025-05-16

## Generative AI for Assisting Software Developers

### SweRank: Software Issue Localization with Code Ranking

**Relevance:** This paper presents SweRank, a retrieve-and-rerank framework for software issue localization, identifying relevant code locations for natural language issue descriptions. This directly assists developers by speeding up bug fixing and feature implementation. The creation of the SweLoc dataset further contributes to the community, enabling the training of more effective models for this task. The outperformance of SweRank compared to agent-based systems using closed-source LLMs highlights its efficiency and practicality for integration into developer workflows.

💡 **[Summary](2505.07849/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07849)**

### Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation

**Relevance:** This work introduces WebApp1K, a benchmark where LLMs generate code directly from test cases. This aligns perfectly with the 'code generation' aspect of assisting developers. LLMs that perform well on this benchmark have a better capacity for TDD and are more helpful to programmers. Because the work explores instruction following in code context, it has implications for helping developers follow specifications and constraints in practice. The insights into long prompt handling are also practically relevant for real-world development tasks.

💡 **[Summary](2505.09027/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.09027)**

### TRAIL: Trace Reasoning and Agentic Issue Localization

**Relevance:** This paper addresses the need for evaluating agentic workflows, particularly in software engineering. The TRAIL dataset, consisting of annotated traces from agentic systems, can be used to train models to identify errors in code generation and debugging processes. This has direct implications for improving the reliability and effectiveness of AI agents designed to assist software developers in tasks such as bug fixing and code review, by identifying and categorizing errors present in traces of agent actions.

💡 **[Summary](2505.08638/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.08638)**

## AI Agents

### LLAMAPIE: Proactive In-Ear Conversation Assistants

**Relevance:** LLAMAPIE introduces a real-time proactive AI assistant delivered via hearable devices. It aims to enhance human conversations without interrupting them, which is achieved through predicting user needs and leveraging user knowledge for context-aware assistance. The system is implemented on Apple Silicon M2 hardware and user studies show preference for the proactive assistant, highlighting the potential for AI agents to enhance live, real-world interactions. This is directly relevant to AI agents that can perceive, reason, plan and take action.

💡 **[Summary](2505.04066/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.04066)**

### Reinforced Internal-External Knowledge Synergistic Reasoning for Efficient Adaptive Search Agent

**Relevance:** This paper presents IKEA, an agent designed to strategically use internal and external knowledge. It addresses the challenge of over-reliance on retrieval in RAG systems by enabling the agent to determine when external search is necessary. The IKEA agent has a knowledge-boundary-aware reward function and training dataset to learn when to retrieve information. Results show that it reduces retrieval frequency and improves generalization. This is relevant to AI Agents as it addresses the crucial aspect of efficient and adaptive resource utilization, a core function of an AI agent.

💡 **[Summary](2505.07596/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07596)**

### Measuring General Intelligence with Generated Games

**Relevance:** This paper introduces gg-bench, a set of procedurally generated game environments used to evaluate general reasoning in AI models. The benchmark uses an LLM to generate game descriptions and code, then tests language models by having them play the games. This is relevant because it tests the AI's ability to perceive an environment (game rules), reason about tasks (how to win), plan actions, and execute them (make moves), which are all defining characteristics of AI agents.

💡 **[Summary](2505.07215/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07215)**

## Prompt Engineering Techniques

### A Multi-Dimensional Constraint Framework for Evaluating and Improving Instruction Following in Large Language Models

**Relevance:** This paper introduces a framework with constraint patterns, categories, and difficulty levels to evaluate LLMs' ability to follow instructions. The paper demonstrates the utility by using the framework to generate data for RL, and it shows how it enhances LLM's constraint recognition and adherence. The work has a direct link to prompt engineering by creating an improved evaluation benchmark which would inform the creation of better prompts, specifically for constrained situations.

💡 **[Summary](2505.07591/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07591)**

### Visually Interpretable Subtask Reasoning for Visual Question Answering

**Relevance:** This paper introduces VISTAR, a framework that fine-tunes MLLMs to produce structured Subtask-of-Thought rationales (step-by-step reasoning sequences). This is directly relevant to chain-of-thought prompting, as it aims to improve reasoning accuracy and interpretability by guiding the model to explicitly break down complex questions into smaller, manageable steps. By training the model to generate textual and visual explanations, VISTAR enhances the transparency and effectiveness of its reasoning process.

💡 **[Summary](2505.08084/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.08084)**

## Human-in-the-loop Machine Learning

### ViMRHP: A Vietnamese Benchmark Dataset for Multimodal Review Helpfulness Prediction via Human-AI Collaborative Annotation

**Relevance:** This paper describes the creation of ViMRHP, a large-scale dataset for predicting the helpfulness of Vietnamese reviews, using human annotators assisted by AI. This showcases a human-in-the-loop approach to data labeling, improving efficiency and reducing costs. It involves human-verified and AI-generated annotations, which exemplifies the collaborative process of human experts and AI models.

💡 **[Summary](2505.07416/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07416)**

### DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation

**Relevance:** This paper explores using LLM outputs as feedback for optimizing reranking in RAG systems. The reranker is modeled as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality. This means that a person isn't directly evaluating the response. Rather, the agent is deriving a 'reward' signal from the LLM itself to improve. While it is not 'direct' human-in-the-loop, it uses LLM outputs to guide improvement, which is aligned with using human feedback.

💡 **[Summary](2505.07233/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.07233)**

## Techniques for Explaining AI Behavior

### Visually Interpretable Subtask Reasoning for Visual Question Answering

**Relevance:** This paper introduces VISTAR, a subtask-driven training framework to enhance both interpretability and reasoning in multimodal models. It produces textual and visual explanations within MLLMs. By generating step-by-step reasoning sequences, VISTAR aims to make the AI's decision-making more transparent and understandable. This is aligned with explainable AI (XAI) as it directly provides insights into the model's thought process.

💡 **[Summary](2505.08084/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.08084)**

### Document Attribution: Examining Citation Relationships using Large Language Models

**Relevance:** This work explores the concept of 'attribution,' tracing generated LLM outputs back to their source documents. The research proposes techniques to assess the reliability of these citations to ensure trustworthiness and interpretability. The work explores the role of the attention mechanism in enhancing the attribution process, which improves the explanation of why certain documents are being cited.

💡 **[Summary](2505.06324/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.06324)**

