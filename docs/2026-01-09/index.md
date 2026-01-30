---
layout: default
title: 2026-01-09
permalink: /2026-01-09/
---

# 2026-01-09

## AI for Software Development

### Agentic Rubrics as Contextual Verifiers for SWE Agents

**Relevance:** This paper addresses a critical challenge in AI for SWE: efficient and interpretable verification. By using an agent to create context-grounded rubrics (checklists) for patch evaluation, it provides a scalable verification signal without relying solely on slow code execution. From an HCI perspective, these structured rubrics offer highly transparent, human-readable criteria for why a generated patch succeeded or failed, enhancing developer trust and facilitating effective human oversight of AI coding assistants. This verification method acts as an essential feedback loop for both human developers and RL-based SWE agents.

💡 **[Summary](2601.04171/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.04171)**

### MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics

**Relevance:** This work applies LLMs to a highly specialized scientific programming domain (Molecular Dynamics, LAMMPS scripts). It tackles the challenge of LLM code generation in scarce data environments by introducing a domain-specific data construction pipeline and a closed-loop RL method that uses simulation outcomes as reward signals. The resulting multi-agent system integrates code generation, execution, evaluation, and self-correction, fundamentally transforming how domain scientists interact with complex simulation software. The goal is to make specialized programming tasks accessible and time-efficient, significantly improving user productivity in AI for Science.

💡 **[Summary](2601.02075/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.02075)**

### SciEvalKit: An Open-source Evaluation Toolkit for Scientific General Intelligence

**Relevance:** SciEvalKit is an evaluation toolkit for scientific AI, explicitly including "Scientific Code Generation" as a core competency. While primarily an ML tool, evaluation toolkits are vital for HCI, as they define the standards for reliability, trustworthiness, and applicability of AI systems used by scientists and engineers. By providing a flexible, transparent, and reproducible infrastructure based on expert-grade, real-world tasks, it ensures that AI code generation models are benchmarked against authentic challenges, directly impacting the quality and dependability of AI assistance in scientific software development.

💡 **[Summary](2512.22334/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.22334)**

## AI Agents

### Evolving Programmatic Skill Networks

**Relevance:** This framework focuses on creating robust, adaptive embodied AI agents that learn executable symbolic programs (skills) and organize them into a compositional network. For HCI, this is critical because it moves agents beyond monolithic policies toward interpretable, modular behaviors. The mechanisms REFLECT (structured fault localization) and canonical structural refactoring are forms of self-explanation and refinement, allowing future human collaborators to better understand, debug, and potentially guide the agent's learned skill library in complex, open-ended environments.

💡 **[Summary](2601.03509/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03509)**

### Atlas: Orchestrating Heterogeneous Models and Tools for Multi-Domain Complex Reasoning

**Relevance:** Atlas addresses the core agent challenge of complex reasoning by dynamically orchestrating heterogeneous LLMs and external tools. This is key for robust agents intended for real-world use. From an HCI perspective, the framework focuses on adaptive alignment (routing) and synergistic invocation, aiming to provide superior performance that users can rely on across diverse domains. Although the routing is automated via RL, the underlying goal is to create a more capable and trustworthy tool-using interface, minimizing user friction caused by poor tool selection or reasoning failure in multi-step tasks.

💡 **[Summary](2601.03872/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03872)**

### MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

**Relevance:** MAGMA introduces a multi-graph memory architecture for LLM agents, decoupling temporal, causal, and entity information. This design has profound implications for HCI by addressing the limitations of monolithic memory stores that hinder interpretability. By formulating retrieval as policy-guided traversal over relational views, MAGMA explicitly enables "transparent reasoning paths." This transparency is crucial for user trust and debugging, allowing humans to audit the evidence the agent used to reach a decision, addressing the notorious "black box" problem in long-context, memory-augmented agents.

💡 **[Summary](2601.03236/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03236)**

## LLM Evaluation Methods

### Pearmut: Human Evaluation of Translation Made Trivial

**Relevance:** This paper introduces a lightweight platform designed to make human evaluation of NLP tasks (like translation) trivial and routine, rather than complex and occasional. From an HCI standpoint, this tool directly lowers the operational and engineering overhead required for high-quality human-in-the-loop evaluation. By supporting standard protocols (MQM, DA) and features like attention checks, Pearmut makes reliable human judgment a practical component of the ML development lifecycle, ensuring models are aligned with user needs for relevance, coherence, and usability.

💡 **[Summary](2601.02933/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.02933)**

### Benchmark^2: Systematic Evaluation of LLM Benchmarks

**Relevance:** This work proposes a systematic framework for evaluating the quality of LLM benchmarks themselves, focusing on metrics like ranking consistency and discriminability. This is a meta-HCI contribution: if the tools used to measure model progress (benchmarks) are flawed, human evaluators and developers will receive misleading signals about model capabilities, leading to misaligned development. Benchmark^2 ensures that the foundation of ML evaluation is robust, promoting trustworthy and meaningful assessment of LLMs' performance and capabilities relative to user expectations.

💡 **[Summary](2601.03986/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03986)**

### RedBench: A Universal Dataset for Comprehensive Red Teaming of Large Language Models

**Relevance:** RedBench provides a universal dataset and standardized taxonomy for comprehensive red teaming, focusing on adversarial robustness and safety vulnerabilities across 22 risk categories. Robustness and safety are foundational for trustworthy AI deployment, a core tenet of HCI. By standardizing the evaluation of vulnerabilities, RedBench facilitates systematic vulnerability assessment, helping developers mitigate biases and prevent harmful outputs, thereby ensuring LLMs are secure, safe, and reliable for real-world interaction and deployment in safety-critical applications.

💡 **[Summary](2601.03699/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03699)**

## Reinforcement Learning

### E-GRPO: High Entropy Steps Drive Effective Reinforcement Learning for Flow Models

**Relevance:** E-GRPO (Entropy-aware Group Relative Policy Optimization) introduces an RL innovation focused on enhancing exploration efficiency by strategically increasing the entropy of SDE sampling steps. In the context of Human-in-the-Loop RL (HRL) and human preference alignment, efficient exploration is crucial. This method reduces the number of ambiguous rollouts and accelerates convergence, consequently reducing the required amount of human feedback. Lowering the cognitive load and maximizing the utility of human supervision is a direct benefit derived from this RL methodological improvement, facilitating better human-AI alignment.

💡 **[Summary](2601.00423/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.00423)**

### ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing

**Relevance:** This framework applies RL to improve reasoning-centric image editing, a complex generative task requiring precise instruction following. The key HCI relevance lies in the reward system design: it decouples reasoning from synthesis and uses a binary checklist for rewards. This yields more precise, interpretable, and lower-variance rewards than traditional VLM scores, making the RL objective clearer and more stable. This clarity is essential for aligning the model's behavior with complex human instructions, resulting in instruction-faithful and semantically grounded edits that meet user expectations.

💡 **[Summary](2601.03467/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03467)**

### ROI-Reasoning: Rational Optimization for Inference via Pre-Computation Meta-Cognition

**Relevance:** ROI-Reasoning uses Reinforcement Learning to teach LLMs "meta-cognition"—the ability to predict task difficulty and rationally allocate computational budgets (tokens). The Rationality-Aware Reinforcement Learning stage optimizes sequential decision-making under hard constraints. From an HCI perspective, this research aims to move LLMs toward reliable behavior under resource limitations. By optimizing resource allocation, the model can ensure that complex tasks receive sufficient computation, reducing reasoning failures and improving output quality, which significantly enhances the perceived reliability and usability of LLM services for the end-user.

💡 **[Summary](2601.03822/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03822)**

## Explainable AI

### Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy

**Relevance:** This paper delves into mechanistic interpretability, analyzing how LLMs perform large-scale counting tasks via a System-2 strategy. By identifying the specific latent components (attention heads, representations) responsible for computing and aggregating counts, it provides deep, causal insight into the model's internal reasoning process. This level of transparency is vital for building user trust and for developing reliable AI systems, as it allows researchers to diagnose and fix systematic limitations (like counting errors) based on understanding the underlying mechanism rather than surface-level behavior.

💡 **[Summary](2601.02989/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.02989)**

### X-MuTeST: A Multilingual Benchmark for Explainable Hate Speech Detection and A Novel LLM-consulted Explanation Framework

**Relevance:** X-MuTeST addresses the critical need for explainability in hate speech detection, especially for under-resourced languages. It introduces an explanation-guided training framework that leverages human-annotated rationales (token-level explanations) and an LLM-consulted method to refine model attention. By providing human-interpretable rationales alongside predictions, this work significantly enhances user trust, improves accountability, and helps human moderators understand *why* a piece of content was flagged, fostering better human-AI collaboration in content moderation tasks.

💡 **[Summary](2601.03194/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03194)**

### MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

**Relevance:** MAGMA introduces a multi-graph memory architecture for LLM agents that explicitly represents memory across semantic, temporal, causal, and entity graphs. This design is highly relevant to XAI because it enables "transparent reasoning paths." Unlike black-box memory retrieval systems, MAGMA allows for fine-grained control and structured context construction, making the agent's decision-making process auditable. This architectural transparency is crucial for human users who need to trust and interpret the complex, long-horizon actions taken by intelligent autonomous agents.

💡 **[Summary](2601.03236/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.03236)**

