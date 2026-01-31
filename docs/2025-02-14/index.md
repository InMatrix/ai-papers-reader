---
layout: default
title: 2025-02-14
permalink: /2025-02-14/
---

# 2025-02-14

## AI for Software Development

### Teaching Language Models to Critique via Reinforcement Learning

**Relevance:** This paper uses Reinforcement Learning (RL) to train LLMs to act as critics, generating actionable feedback for code refinement. From an HCI perspective, this directly improves the quality and usability of AI assistance in software development. High-quality, targeted critiques mitigate compounding errors and reduce the cognitive load on developers, fostering better human-AI collaboration in debugging and refinement tasks. The resulting system acts as an enhanced AI assistant that provides not just a solution, but effective guidance on how to improve it, which is crucial for developer trust and learning.

💡 **[Summary](2502.03492/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.03492)**

### CodeI/O: Condensing Reasoning Patterns via Code Input-Output Prediction

**Relevance:** CodeI/O enhances LLM reasoning by training them to produce structured Chain-of-Thought (CoT) rationales derived from code logic. For developers using AI assistants for tasks like code completion or bug fixing, clear and logically structured reasoning is essential for verification and trust. By improving the quality and procedural rigor of the AI's internal reasoning, this method directly enhances the interpretability and trustworthiness of the output, making the AI assistant more effective in collaborative software development workflows.

💡 **[Summary](2502.07316/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.07316)**

## AI Agents

### WorldGUI: Dynamic Testing for Comprehensive Desktop GUI Automation

**Relevance:** This paper addresses the challenge of building robust AI agents capable of operating in complex, dynamic desktop environments (GUIs). This is paramount for HCI, as agents must reliably navigate unstructured digital spaces designed for human interaction. The proposed critique mechanism and dynamic testing benchmark (WorldGUI) are necessary steps toward creating controllable and reliable agents that humans can trust to execute complex, multi-step goals across various software applications, simulating real-world user scenarios.

💡 **[Summary](2502.08047/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.08047)**

### Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training

**Relevance:** Hephaestus focuses on foundational capabilities for LLM agents, specifically API function calling, reasoning, and planning, through specialized continual pre-training. These skills are essential for effective human-agent collaboration. Robust foundational skills ensure the agent can reliably understand complex user goals, select appropriate tools, and adapt to environmental feedback, leading to more predictable, efficient, and useful interactions when deployed in user-facing roles.

💡 **[Summary](2502.06589/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.06589)**

### Skill Expansion and Composition in Parameter Space

**Relevance:** This work introduces a framework (PSEC) for autonomous agents to iteratively learn new skills and compose them efficiently using LoRA modules. This addresses a major challenge in agent design: continuous learning and adaptation to new tasks defined by human users. HCI researchers can leverage this paradigm to design interfaces that allow users to teach new 'skill primitives' or prompt the composition of existing skills to solve novel, complex, and multi-objective tasks, thereby improving agent flexibility and longevity in dynamic settings.

💡 **[Summary](2502.05932/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.05932)**

## LLM Evaluation Methods

### Expect the Unexpected: FailSafe Long Context QA for Finance

**Relevance:** This paper introduces FailSafeQA, a benchmark designed to test LLM robustness and compliance against simulated 'human-interface interactions' like query and context failures in high-stakes finance. This evaluation directly addresses trustworthiness and reliability concerns critical to HCI. By emphasizing the balance between robust answering and the ability to refrain from hallucinating (compliance), the benchmark pushes models toward safer, more reliable behavior when handling complex, ambiguous, or degraded inputs from real users.

💡 **[Summary](2502.06329/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.06329)**

### Forget What You Know about LLMs Evaluations - LLMs are Like a Chameleon

**Relevance:** The Chameleon Benchmark Overfit Detector (C-BOD) is a meta-evaluation framework that systematically perturbs prompts to detect model overfitting to superficial dataset cues. This method forces evaluation to move beyond idealized leaderboard scores to prioritize robustness and generalization. From an HCI perspective, robustness to minor input variations is essential for a reliable and predictable user experience, ensuring the model performs consistently and predictably outside of narrow, academic testing environments.

💡 **[Summary](2502.07445/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.07445)**

### Auditing Prompt Caching in Language Model APIs

**Relevance:** This paper develops statistical audits to detect prompt caching in commercial LLM APIs, revealing potential side-channel timing attacks that leak user prompt data. This evaluation is critical from an HCI/Ethics standpoint, as it addresses transparency, privacy, and accountability in deployed systems. Users must have confidence that their inputs are handled securely and confidentially. This work provides a framework for auditing black-box commercial models for non-compliance with expected privacy standards, impacting user trust significantly.

💡 **[Summary](2502.07776/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.07776)**

## Reinforcement Learning

### Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models

**Relevance:** This work uses Reinforcement Learning (RL) to dynamically optimize Conformal Prediction (CP) thresholds for uncertainty quantification (UQ). This is a vital application of RL for improving trustworthy AI. By enabling models to selectively abstain when uncertainty is high, the system provides reliable statistical coverage guarantees, which is crucial for safety-critical HCI applications where human oversight must be automatically triggered during high-risk or low-confidence decisions.

💡 **[Summary](2502.06884/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.06884)**

### DPO-Shift: Shifting the Distribution of Direct Preference Optimization

**Relevance:** DPO-Shift addresses the likelihood displacement issue in Direct Preference Optimization (DPO), a core technique in Reinforcement Learning from Human Feedback (RLHF) used for model alignment. Improving the stability and efficiency of DPO is fundamental for training LLMs that reliably adhere to complex human preferences and ethical values. This foundational RL work directly impacts the quality and trustworthiness of human-aligned agents and LLMs used in user-facing applications.

💡 **[Summary](2502.07599/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.07599)**

### Competitive Programming with Large Reasoning Models

**Relevance:** This paper demonstrates that scaling general-purpose Reinforcement Learning (RL) significantly boosts performance on complex human-level reasoning tasks, outperforming specialized, hand-crafted domain strategies. This finding has implications for designing RL environments and policies for human-agent collaboration. It suggests that focusing on robust, generalizable RL scaling, rather than narrow domain engineering, is the path toward creating agents capable of intuitive interaction and high performance across diverse user requests.

💡 **[Summary](2502.06807/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.06807)**

## Explainable AI

### Sparse Autoencoders for Scientifically Rigorous Interpretation of Vision Models

**Relevance:** This work uses Sparse Autoencoders (SAEs) to discover human-interpretable visual features and enables controlled interventions to test causal hypotheses about model behavior. This advances XAI from passive visualization (e.g., attention maps) towards scientific rigor and causal understanding. Providing causally validated explanations is essential for building user trust and ensuring that explanations are actionable and relevant for human decision-making and model debugging.

💡 **[Summary](2502.06755/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.06755)**

### LLM Pretraining with Continuous Concepts

**Relevance:** The proposed Continuous Concept Mixing (CoCoMix) framework enhances LLM interpretability and steerability by allowing direct inspection and modification of continuous concepts during the model's internal reasoning process. This offers a high degree of transparency in the 'black box.' For HCI, this provides a transparent mechanism and potential interface for users or developers to guide the AI's internal logic, making the model's behavior more predictable and controllable than traditional post-hoc XAI methods.

💡 **[Summary](2502.08524/)** 📄 **[Full paper](https://arxiv.org/pdf/2502.08524)**

