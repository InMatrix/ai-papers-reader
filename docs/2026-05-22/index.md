---
layout: default
title: 2026-05-22
permalink: /2026-05-22/
---

# 2026-05-22

## AI for Software Development

### SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering

**Relevance:** This paper introduces SaaSBench, a benchmark designed to evaluate AI coding agents in complex, multi-component enterprise software environments. For HCI and ML researchers, the paper's key finding is that the primary bottleneck in automated software engineering is not writing localized code, but rather configuring and integrating heterogeneous full-stack components (databases, frameworks, APIs). This insight has significant implications for the design of developer-AI interfaces, highlighting the need for collaborative tools that help developers and AI agents co-navigate complex system-level configurations and debugging loops rather than just code completion.

💡 **[Summary](2605.17526/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.17526)**

### TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

**Relevance:** TerminalWorld provides a scalable benchmark of real-world terminal tasks derived from actual developer recordings. From an HCI perspective, the terminal is a primary interface for developers, and automating terminal workflows requires agents to handle complex, multi-step actions and tool use. By evaluating agents on authentic, in-the-wild terminal commands, this research helps identify where current AI systems fail to understand developer intent and environment states. This work benefits the co-design of command-line interfaces and AI assistants to support more robust, natural, and context-aware developer-agent interactions.

💡 **[Summary](2605.22535/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.22535)**

## AI Agents

### π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

**Relevance:** π-Bench addresses a critical challenge in human-agent interaction: proactive assistance. In real-world settings, users often provide underspecified requests, leaving their underlying preferences and constraints unstated. By benchmarking personal assistant agents on long-horizon workflows with hidden intents, this paper directly informs HCI research on how autonomous agents can dynamically elicit, infer, and adapt to user needs over multi-turn interactions. It bridges the gap between static task execution and the socially-aware, anticipatory behavior required for seamless human-agent collaboration in everyday life.

💡 **[Summary](2605.14678/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.14678)**

### CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing

**Relevance:** Cutverse introduces a benchmark for GUI agents performing complex, long-horizon tasks in professional creative software like Premiere Pro and Photoshop. For HCI researchers, this paper is highly relevant because creative workflows feature dense, multimodal user interfaces that require precise spatial grounding and domain-specific planning. By exposing the limitations of current agents in these professional environments (only 36% success), the paper highlights the need for new agent architectures that can better understand complex UI hierarchies and collaborate with human professionals in highly interactive, creative tasks.

💡 **[Summary](2605.19484/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.19484)**

### MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems

**Relevance:** MINTEval evaluates how memory-augmented agents handle multi-target interference and evolving information over long horizons. In human-agent collaboration, users frequently update, revise, or contradict previously shared information. This paper's findings—that agents struggle to recall and reason over facts that are subsequently updated—have strong implications for the design of agent memory systems. To build trustworthy assistants, researchers must develop memory architectures that can handle dynamic, conversational drift and information updates without losing track of past user contexts.

💡 **[Summary](2605.18565/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.18565)**

## LLM Evaluation Methods

### Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?

**Relevance:** This paper introduces Grounded Personality Reasoning (GPR) to evaluate whether multimodal LLMs truly understand human personality or merely rely on superficial stereotypes. By proposing a dataset (MM-OCEAN) and metrics like the Prejudice Rate, it exposes a gap where models output correct personality ratings without grounding them in behavioral evidence. This is highly relevant to HCI, as deploying biased or ungrounded models in human-facing roles can severely damage user trust and equity. The proposed evaluation framework offers a pathway to build more socially intelligent and accountable AI systems.

💡 **[Summary](2605.22109/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.22109)**

### Capturing LLM Capabilities via Evidence-Calibrated Query Clustering

**Relevance:** This paper presents ECC, an algorithm that clusters queries based on latent LLM capability demands rather than surface-level semantics. For HCI, evaluating LLMs in a way that aligns with actual user task performance is incredibly challenging. By calibrating query embeddings using real model comparisons, ECC provides a more accurate, user-centric evaluation of model capabilities. This allows system designers to better route user queries to the most capable models, ultimately reducing user latency, improving task success rates, and optimizing the overall user experience.

💡 **[Summary](2605.17110/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.17110)**

### LLMEval-Logic: A Solver-Verified Chinese Benchmark for Logical Reasoning of LLMs with Adversarial Hardening

**Relevance:** LLMEval-Logic is a solver-verified benchmark for assessing logical reasoning in LLMs, utilizing realistic scenarios and expert rubrics. Evaluating logical consistency is vital for HCI applications where users rely on AI for decision support in rule-governed domains (e.g., legal, medical, or administrative tasks). The paper reveals that even frontier models struggle with hardened logical reasoning. By providing high-quality, auditable rubrics, this work supports the development of evaluation methods that measure not just output correctness, but the logical validity of the reasoning process, which is essential for user trust.

💡 **[Summary](2605.19597/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.19597)**

## Reinforcement Learning

### Learning from Language Feedback via Variational Policy Distillation

**Relevance:** VPD addresses the challenge of sparse rewards in RL by leveraging rich language feedback to guide agent learning. In HCI, providing numerical rewards is often unintuitive for human users, whereas natural language feedback is a highly expressive and comfortable way for humans to correct and guide AI. By formalizing language-feedback learning as a variational EM problem that co-evolves a teacher and student policy, this work provides a robust technical foundation for building interactive RL systems that can continuously learn from natural, conversational human guidance.

💡 **[Summary](2605.15113/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.15113)**

### From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

**Relevance:** This paper introduces SCRL, a curriculum RL framework that decomposes complex reasoning tasks into verifiable subproblems. In human-agent collaboration, complex tasks often overwhelm both the user's cognitive load and the agent's planning capabilities. By showing how RL agents can learn more effectively through subproblem-level normalization and curriculum learning, this work offers insights into how human-AI interfaces can dynamically scaffold complex problem-solving processes, breaking them down into mutually understandable sub-steps to facilitate cooperative decision-making.

💡 **[Summary](2605.22074/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.22074)**

### Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

**Relevance:** Spreadsheet-RL leverages RL to train LLM agents on realistic spreadsheet tasks within a sandbox environment (Spreadsheet Gym). Spreadsheets are one of the most ubiquitous data interfaces used by humans. By formulating the interaction as a multi-turn RL problem, this research bridges the gap between raw LLM capabilities and structured software interaction. The paper’s environment design and routing rules provide a blueprint for how RL can be used to train agents that intuitively collaborate with humans on complex, multi-step data-centric workflows in everyday office applications.

💡 **[Summary](2605.22642/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.22642)**

## Explainable AI

No paper recommendations for this topic.

