---
layout: default
title: 2024-07-19
permalink: /2024-07-19/
---

# 2024-07-19

## AI for Software Development

### Scaling Granite Code Models to 128K Context

**Relevance:** This paper advances code generation and completion by significantly extending the context length of LLMs tailored for code. From an HCI perspective, increasing the effective context window to 128K tokens means developers can work on vast codebases without losing continuity, dramatically reducing the cognitive load associated with manually searching, tracking, and integrating distant code segments. The demonstrated ability to maintain performance on standard benchmarks while achieving significant gains on long-context tasks implies a more robust and highly usable tool for real-world programming, thereby enhancing developer productivity and flow state.

💡 **[Summary](2407.13739/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.13739)**

### CodeV: Empowering LLMs for Verilog Generation through Multi-Level Summarization

**Relevance:** CodeV addresses the challenge of generating specialized code, specifically Hardware Description Languages (HDLs) like Verilog. This is highly relevant to HCI as it focuses on enabling domain experts (hardware engineers) to leverage LLMs effectively, bridging the gap between natural language instructions and highly specialized, complex syntax. The model's training approach, which uses multi-level summarization to generate natural language descriptions from high-quality existing code, highlights an effective paradigm for training AI tools based on expert-generated artifacts, improving the quality of generated code.

💡 **[Summary](2407.10424/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.10424)**

### AUITestAgent: Automatic Requirements Oriented GUI Function Testing

**Relevance:** This work directly impacts the software development lifecycle by introducing an agent that automates GUI testing based on natural language requirements. From an HCI viewpoint, this ensures that the functional correctness of the Graphical User Interface aligns with human-written specifications. By automatically extracting interaction commands and verification oracles from natural language, AUITestAgent drastically reduces the manual effort required from testing engineers, allowing them to focus on higher-level quality assurance and user experience issues rather than repetitive functional checks.

💡 **[Summary](2407.09018/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.09018)**

## AI Agents

### Sibyl: Simple yet Effective Agent Framework for Complex Real-world Reasoning

**Relevance:** Sibyl proposes a novel agent framework drawing inspiration from cognitive theories (Global Workspace Theory and Society of Mind) to enhance complex, long-term reasoning capabilities. This is highly relevant to HCI because it aims to shift LLM agents toward System-2 thinking, making them more reliable and deliberate partners for human users in complex, high-stakes tasks. The multi-agent debate mechanism for self-refinement ensures the final answers are more comprehensive and aligned with human expectations for thorough decision-making.

💡 **[Summary](2407.10718/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.10718)**

### ThinkGrasp: A Vision-Language System for Strategic Part Grasping in Clutter

**Relevance:** ThinkGrasp describes a system that uses advanced vision-language reasoning (via GPT-4o) to plan and execute strategic, multi-step actions in cluttered physical environments. This work is a crucial step for embodied HCI and human-agent collaboration. The agent interprets goal-oriented language to proactively remove obstructing objects before grasping the target, demonstrating sophisticated tool use and planning that moves beyond simple command execution toward robust, real-world problem-solving capabilities required for effective human-robot interaction.

💡 **[Summary](2407.11298/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.11298)**

### Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?

**Relevance:** This paper introduces a benchmark designed to rigorously evaluate multimodal agents on complex, professional data science and engineering workflows involving code generation and GUI operations. This is essential for HCI/ML research as it provides a realistic measure of agent competence in high-stakes environments. The findings highlight crucial usability bottlenecks, particularly agents' underperformance in tasks requiring fine-grained, knowledge-intensive GUI actions, paving the way for targeted research to improve the practical deployment and human adoption of autonomous agents.

💡 **[Summary](2407.10956/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.10956)**

## LLM Evaluation Methods

### Benchmark Agreement Testing Done Right: A Guide for LLM Benchmark Evaluation

**Relevance:** This paper focuses on standardizing Benchmark Agreement Testing (BAT) to assess the validity and robustness of LLM benchmarks themselves. From an HCI perspective, if the evaluation metrics are flawed or inconsistent, researchers cannot reliably determine if models are truly improving or aligning with complex user needs. By proposing best practices and releasing a toolkit, this work ensures that the foundational measurements guiding LLM development are trustworthy, thereby fostering confidence in the performance metrics used across the research community.

💡 **[Summary](2407.13696/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.13696)**

### LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models

**Relevance:** This work addresses the 'evaluation trilemma' (coverage, cost, contamination) specific to Large Multimodal Models (LMMs). Since LMMs interact with humans through complex modalities, comprehensive and transparent evaluation is critical for ensuring safety and functionality. By introducing standardized benchmarks and a 'LITE' toolkit, the paper helps navigate the trade-offs in LMM evaluation, ensuring that the models developed are reliably assessed for usability, trust, and alignment across diverse human interaction scenarios.

💡 **[Summary](2407.12772/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.12772)**

### Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation

**Relevance:** This paper focuses on developing high-performing LLM-as-a-Judge models (autoraters) to improve automatic evaluation. This directly addresses the high cost and scalability limitations of human-in-the-loop evaluation, a cornerstone of HCI-informed LLM assessment. By achieving performance competitive with proprietary models and demonstrating reduced bias, FLAMe enables rapid, cost-effective evaluation of user satisfaction, coherence, and ethical alignment across a massive scale of generated responses.

💡 **[Summary](2407.10817/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.10817)**

## Reinforcement Learning

### Understanding Reference Policies in Direct Preference Optimization

**Relevance:** Direct Preference Optimization (DPO) is a critical method derived from RLHF used to align LLMs with human preferences, making this research highly relevant to HCI. The paper investigates the role and optimal configuration of the reference policy, which dictates how strongly the model resists deviating from its base behavior. Understanding this sensitivity is crucial for designing effective alignment procedures that ensure models are safe, helpful, and responsive to subtle human feedback signals without causing unintended behavioral drift.

💡 **[Summary](2407.13709/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.13709)**

### Grasping Diverse Objects with Simulated Humanoids

**Relevance:** This paper applies Reinforcement Learning to teach simulated humanoid agents complex motor skills, specifically grasping and carrying diverse objects along specified trajectories. This is foundational research for intuitive human-agent collaboration in physical environments. By leveraging a human-like motion representation and simple rewards, the method scales to complex tasks and diverse objects, suggesting a path toward designing RL environments and policies that facilitate learning complex, interpretable, and collaborative behaviors for future physical AI assistants.

💡 **[Summary](2407.11385/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.11385)**

## Explainable AI

### A Comparative Study on Automatic Coding of Medical Letters with Explainability

**Relevance:** This study focuses on implementing visual explainability in a high-stakes clinical application (automatic medical coding). This directly addresses the critical HCI concern of trust and transparency in AI deployed in sensitive domains. Providing clinicians with light-weighted, local explanations facilitates the auditability of AI decisions and improves user understanding of the prediction process, which is essential for safe integration and effective human reliance on machine learning systems in healthcare settings.

💡 **[Summary](2407.13638/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.13638)**

### Uncertainty is Fragile: Manipulating Uncertainty in Large Language Models

**Relevance:** Uncertainty estimation is a core XAI mechanism intended to communicate model reliability and confidence to the user, thereby building trust. This paper reveals that this signal can be manipulated via adversarial attacks (backdoors). This vulnerability has significant HCI implications, as users rely on uncertainty cues to assess when to verify or override an AI output. The work underscores the crucial need for developing robust and trustworthy XAI mechanisms that cannot be easily compromised.

💡 **[Summary](2407.11282/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.11282)**

