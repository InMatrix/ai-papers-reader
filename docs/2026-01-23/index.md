---
layout: default
title: 2026-01-23
permalink: /2026-01-23/
---

# 2026-01-23

## AI for Software Development

### The Responsibility Vacuum: Organizational Failure in Scaled Agent Systems

**Relevance:** This paper directly addresses the structural failure mode arising from integrating agent-generated code into continuous integration/continuous deployment (CI/CD) pipelines. It defines the 'responsibility vacuum,' where human authority to approve code decisions lacks the epistemic capacity to understand the AI's basis. This is a critical HCI problem concerning trust, verification, and organizational design when scaling generative AI tools for software development, demanding solutions that redesign decision boundaries rather than just adding automation.

💡 **[Summary](2601.15059/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.15059)**

### DSAEval: Evaluating Data Science Agents on a Wide Range of Real-World Data Science Problems

**Relevance:** Data Science Agents automate complex tasks ranging from data analysis to deep learning, requiring sophisticated code generation and execution. This benchmark introduces multi-dimensional evaluation focusing on reasoning, code quality, and results in execution-grounded environments. For AI in software development, this evaluation methodology is vital for assessing the reliability and correctness of generated code artifacts in real-world, open-ended data science workflows.

💡 **[Summary](2601.13591/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.13591)**

### Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics

**Relevance:** This work proposes using a general coding agent (LLM) as a formal math reasoner capable of interacting with the Lean theorem prover. Formal mathematics requires generating highly precise, verifiable, and code-like proofs. This application demonstrates advanced AI assistance for high-assurance technical reasoning and code generation, which is highly relevant to developing reliable AI tools for complex and safety-critical software engineering tasks.

💡 **[Summary](2601.14027/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14027)**

## AI Agents

### Agentic Reasoning for Large Language Models

**Relevance:** As a comprehensive survey, this paper provides a structured roadmap for the field of AI agents, organizing agentic reasoning into foundational, self-evolving, and collective multi-agent categories. It synthesizes the core ML techniques (planning, tool use, RL) required for autonomous systems. This overview is essential for HCI researchers seeking to understand the current capabilities and limitations of agents to design effective human-agent collaboration interfaces.

💡 **[Summary](2601.12538/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.12538)**

### FinVault: Benchmarking Financial Agent Safety in Execution-Grounded Environments

**Relevance:** This paper addresses the critical safety and security risks introduced by LLM-powered financial agents that can execute plans and manipulate mutable state. It introduces an execution-grounded benchmark, highlighting that standard safety evaluations fail to capture real operational risks. This emphasizes the vital need for HCI principles—such as control, transparency, and robust safety interfaces—when deploying autonomous agents in high-stakes, regulated environments.

💡 **[Summary](2601.07853/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.07853)**

### XR: Cross-Modal Agents for Composed Image Retrieval

**Relevance:** This work introduces a training-free multi-agent framework that reframes complex retrieval tasks as a coordinated reasoning process. It orchestrates specialized agents (imagination, similarity, and question agents) to iteratively refine results based on multimodal constraints. This illustrates a cutting-edge approach to structuring complex agent behavior, relevant for designing future interfaces where users interact with coordinated AI teams rather than monolithic models.

💡 **[Summary](2601.14245/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14245)**

## LLM Evaluation Methods

### MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents

**Relevance:** This benchmark evaluates complex multimodal agents on citation-grounded report generation. Crucially, it proposes FLAE, TRACE, and MOSAIC—a unified, interpretable evaluation pipeline that produces fine-grained signals for error diagnosis (e.g., citation alignment and text-visual integrity). These methods move beyond single-score metrics, providing the necessary transparency for human evaluators to diagnose failures and ensure the trustworthiness of agent outputs.

💡 **[Summary](2601.12346/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.12346)**

### LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals

**Relevance:** This framework addresses the challenge of rigorously evaluating the faithfulness of concept-based explanations (a key XAI method) by using Structured Causal Models to generate structural counterfactuals. By providing a causality-based benchmark and new metrics, it ensures that explanations are reliable and accurately reflect model behavior, which is fundamental for user trust and effective human decision-making in high-stakes applications.

💡 **[Summary](2601.10700/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.10700)**

## Reinforcement Learning

### FARE: Fast-Slow Agentic Robotic Exploration

**Relevance:** This work integrates LLM global reasoning (slow thinking) with an RL policy for local control (fast thinking) in robotic exploration. This hierarchical architecture is highly relevant to HCI because it decouples semantic planning from execution. This decoupling facilitates human guidance and intervention at the high-level planning stage, making the agent's behavior more predictable and interpretable for human collaborators in complex environments.

💡 **[Summary](2601.14681/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14681)**

### InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning

**Relevance:** Standard RL suffers from poor credit assignment, penalizing correct intermediate steps in failed LLM reasoning traces. Intervention Training (InT) addresses this by having the model propose targeted, single-step corrections. This mechanism not only improves RL efficiency but also introduces a form of localized interpretability, allowing researchers and users to pinpoint exactly where the agent's reasoning failed and how it could be corrected.

💡 **[Summary](2601.14209/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14209)**

### Behavior Knowledge Merge in Reinforced Agentic Models

**Relevance:** This paper focuses on integrating knowledge from multiple RL-trained agents, which is challenging due to the sparse nature of RL task vectors. The proposed Reinforced Agent Merging (RAM) framework enables the creation of a single generalist model by selectively preserving task-specific behaviors. This scalability is critical for developing versatile RL agents that can handle diverse, user-defined tasks without requiring complex, task-specific interfaces.

💡 **[Summary](2601.13572/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.13572)**

## Explainable AI

### Show me the evidence: Evaluating the role of evidence and natural language explanations in AI-supported fact-checking

**Relevance:** This is a direct HCI study demonstrating how non-expert users evaluate AI predictions under varying explanation types. It finds that users consistently rely on inspectable evidence to validate AI claims, even when natural language explanations are provided. This is crucial for XAI design, confirming that transparency must move beyond mere linguistic summarization to provide verifiable grounding for building user trust and supporting informed decision-making.

💡 **[Summary](2601.11387/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.11387)**

### Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models

**Relevance:** This survey provides a framework for operationalizing Mechanistic Interpretability (MI), shifting XAI from an observational science to an actionable methodology. It structures MI around 'Locate, Steer, and Improve,' detailing intervention protocols to optimize LLMs for alignment, capability, and efficiency. This approach allows HCI practitioners to collaborate with ML engineers to directly integrate interpretability insights into model design and refinement.

💡 **[Summary](2601.14004/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14004)**

### Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning

**Relevance:** Render-of-Thought (RoT) reifies the latent reasoning chain by rendering textual CoT steps into images. This makes the rationale visually explicit and traceable, enhancing transparency and analyzability for the user or developer. Furthermore, by achieving significant token compression and inference acceleration, RoT demonstrates a powerful technique for making transparent reasoning practical in real-time, high-throughput applications.

💡 **[Summary](2601.14750/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.14750)**

