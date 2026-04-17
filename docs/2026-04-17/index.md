---
layout: default
title: 2026-04-17
permalink: /2026-04-17/
---

# 2026-04-17

## AI for Software Development

### Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

**Relevance:** This paper investigates how coding agents can leverage meta-knowledge, such as validation routines, across heterogeneous task domains. By studying memory abstraction and transferability, it provides insights into building more efficient and generalizable AI assistants for software development. From an HCI perspective, this research helps in designing agents that better understand the shared infrastructural foundations of coding, leading to more intuitive and context-aware developer support tools.

💡 **[Summary](2604.14004/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.14004)**

### Do AI Coding Agents Log Like Humans? An Empirical Study

**Relevance:** This study bridges HCI and software engineering by comparing the logging practices of AI agents against human baselines. It identifies a 'dual failure' where agents struggle with natural language logging instructions and require human 'silent janitors' to fix observability issues. The findings suggest a need for deterministic guardrails and better human-agent alignment to ensure that AI-generated code meets non-functional requirements like maintainability and debuggability.

💡 **[Summary](2604.09409/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.09409)**

### Spec Kit Agents: Context-Grounded Agentic Workflows

**Relevance:** Addressing the problem of 'context blindness' in large repositories, this paper introduces a multi-agent pipeline for spec-driven development. By using probing and validation hooks to ground agents in repository evidence, it reduces API hallucinations and architectural violations. This work is highly relevant to HCI as it explores structured workflows and grounding mechanisms that improve the reliability and quality of AI-assisted software engineering.

💡 **[Summary](2604.05278/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.05278)**

## AI Agents

### SemaClaw: A Step Towards General-Purpose Personal AI Agents through Harness Engineering

**Relevance:** SemaClaw focuses on 'harness engineering'—the infrastructure required to transform autonomous agents into controllable and reliable systems. It introduces a hybrid orchestration method and a safety system for human-agent interaction. This is a quintessential HCI-ML paper as it frames the evolution of agents as a shift toward persistent, contextually aware collaborative relationships, emphasizing the need for trustworthy and extensible infrastructure for personal AI.

💡 **[Summary](2604.11548/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.11548)**

### Mobile GUI Agents under Real-world Threats: Are We There Yet?

**Relevance:** This paper evaluates how mobile GUI agents perform in the presence of untrustworthy third-party content, such as ads and user-generated posts. It highlights significant performance degradation in real-world environments compared to static benchmarks. For HCI researchers, this work underscores the security and usability challenges of deploying autonomous agents as system building blocks, where environmental noise can lead to unintended or harmful agent actions.

📄 **[Full paper](https://arxiv.org/pdf/2507.04227)**

### Self-Sovereign Agent

**Relevance:** This paper explores the emerging concept of agents that can economically sustain and extend their own operation without human involvement. It analyzes the technical, security, and governance challenges of such high-autonomy systems. This research is critical for HCI as it investigates the boundary where AI transitions from a tool to an independent actor, necessitating new frameworks for human-AI alignment and societal safety.

💡 **[Summary](2604.08551/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08551)**

## LLM Evaluation Methods

### DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation

**Relevance:** This paper introduces a realistic benchmark for evaluating research agents on complex, long-horizon tasks. It features a multi-dimensional evaluation framework covering information recall, factual accuracy, and instruction following, validated against human judgments. This approach addresses the HCI need for evaluation methods that reflect the complexity of authentic user tasks and the nuances of human-perceived quality in report generation.

💡 **[Summary](2604.14683/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.14683)**

### ROSE: An Intent-Centered Evaluation Metric for NL2SQL

**Relevance:** ROSE shifts the evaluation of Natural Language to SQL (NL2SQL) from syntactic consistency to user intent. By using an adversarial Prover-Refuter cascade, it assesses whether predicted SQL actually answers the user's question. This intent-centered approach is highly relevant to HCI, as it prioritizes semantic correctness and user satisfaction over rigid code matching, providing a more reliable measure of how well models serve human users.

💡 **[Summary](2604.12988/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.12988)**

### OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language World Models

**Relevance:** OccuBench evaluates agents across 100 professional task scenarios using Language World Models to simulate complex environments. It specifically tests environmental robustness under fault injection, such as missing data or timeouts. This is relevant to HCI as it assesses how agents handle the ambiguity and degradation common in real-world professional work, providing a systematic way to measure occupational readiness and reliability.

💡 **[Summary](2604.10866/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.10866)**

## Reinforcement Learning

### RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework

**Relevance:** RAD-2 applies RL to autonomous driving motion planning, using a discriminator to rerank trajectory candidates based on long-term driving quality. It introduces Temporally Consistent Group Relative Policy Optimization to address the credit assignment problem. This research benefits HCI by exploring how RL can improve the perceived safety and smoothness of autonomous systems in complex human environments, such as urban traffic.

💡 **[Summary](2604.15308/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.15308)**

### Target Policy Optimization

**Relevance:** This paper introduces TPO, a method that separates the determination of target probabilities from the parameter update process in RL. This separation prevents overshooting and improves performance under sparse rewards. For HCI, this represents a technical advancement in training agents for complex tasks where feedback is infrequent, making it easier to align agent policies with specific, high-level human objectives without the instability of traditional policy-gradient methods.

💡 **[Summary](2604.06159/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.06159)**

### PokeRL: Reinforcement Learning for Pokemon Red

**Relevance:** PokeRL addresses long-horizon tasks and partial observability in a complex game environment using hierarchical rewards and anti-loop mechanisms. It demonstrates how to explicitly model failure modes like unproductive wandering. This work is relevant to HCI as it provides a modular system for training agents to navigate environments with quirky mechanics and sparse feedback, mirroring the challenges humans face when collaborating with autonomous systems in complex digital spaces.

💡 **[Summary](2604.10812/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.10812)**

## Explainable AI

### RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time

**Relevance:** This paper proposes reward models that generate explicit, multi-dimensional critiques before scoring visual content. These rationales transform the model from a 'black-box' evaluator into a transparent optimization tool. In HCI, this is a significant step forward for XAI, as it provides users with interpretable feedback on why certain outputs are preferred, enabling human-in-the-loop refinement and increasing trust in generative AI systems.

💡 **[Summary](2604.11626/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.11626)**

### Do Thought Streams Matter? Evaluating Reasoning in Gemini Vision-Language Models for Video Scene Understanding

**Relevance:** This research benchmarks 'thought streams'—internal reasoning traces in vision-language models. It introduces metrics to measure how much of the internal trace is useful content versus meta-commentary and how faithfully it translates to the final output. This is highly relevant to XAI as it investigates the transparency of the model's 'internal monologue,' helping researchers and users understand the cognitive process behind video scene interpretation.

💡 **[Summary](2604.11177/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.11177)**

### What do Language Models Learn and When? The Implicit Curriculum Hypothesis

**Relevance:** By proposing the Implicit Curriculum Hypothesis, this paper identifies a predictable and compositional order in which skills emerge during LLM pretraining. It shows that these trajectories are readable from the model's internal representations. This provides a novel XAI perspective on the pretraining process, allowing developers to interpret and predict the emergence of complex capabilities, which is essential for designing safe and predictable human-AI interactions.

💡 **[Summary](2604.08510/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08510)**

