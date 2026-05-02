---
layout: default
title: 2026-04-03
permalink: /2026-04-03/
---

# 2026-04-03

## AI for Software Development

### Embarrassingly Simple Self-Distillation Improves Code Generation

**Relevance:** This paper introduces Simple Self-Distillation (SSD) to improve LLM performance on code generation without external verifiers or teachers. By fine-tuning models on their own high-temperature samples, it addresses the precision-exploration conflict in code decoding. From an HCI perspective, this approach lowers the barrier for developers to customize and improve local coding assistants autonomously. It demonstrates how model refinement can lead to significant gains in complex problem-solving, directly benefiting AI-assisted software development tools by enhancing their underlying generation capabilities without requiring expensive human-annotated datasets or complex reinforcement learning pipelines.

💡 **[Summary](2604.01193/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.01193)**

### Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification

**Relevance:** This paper addresses the evaluation of coding agents for end-to-end website development, spanning from static UI-to-code generation to full-stack development. It introduces a hierarchical benchmark and a workflow-based agent verification paradigm that uses a GUI agent verifier and a VLM-based judge. This is highly relevant to HCI as it focuses on the visual and interactive aspects of software development, ensuring that AI-generated code aligns with intended visual prototypes. It provides a structured way to measure how well AI agents can assist in real-world web engineering workflows while maintaining visual and functional fidelity.

💡 **[Summary](2603.26648/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.26648)**

### S0 Tuning: Zero-Overhead Adaptation of Hybrid Recurrent-Attention Models

**Relevance:** This paper presents S0 tuning, a parameter-efficient method that excels at adapting hybrid models for code generation with minimal overhead. By optimizing only the initial state matrix, it outperforms LoRA on benchmarks like HumanEval. This has significant implications for developer tools where low-latency inference and fast task-switching are crucial. It suggests an efficient way to provide specialized, high-performance coding assistance in resource-constrained environments. For HCI, this enables more responsive and personalized development environments that can quickly adapt to specific coding styles or proprietary APIs without the need for model reloads or heavy computation.

📄 **[Full paper](https://arxiv.org/pdf/2604.01168)**

## AI Agents

### GPA: Learning GUI Process Automation from Demonstrations

**Relevance:** GPA introduces a system for learning GUI process automation from a single human demonstration, addressing the fragility of traditional RPA. It uses Sequential Monte Carlo-based localization and readiness calibration to handle rescaling and detection uncertainty. From an HCI perspective, it enables users to automate repetitive digital tasks easily and reliably. By focusing on robustness and local execution for privacy, it bridges the gap between autonomous agent capabilities and the practical requirements of enterprise workflows. This approach allows users to orchestrate complex GUI tasks through reasoning while the agent handles the technical execution.

📄 **[Full paper](https://arxiv.org/pdf/2604.01676)**

### When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation

**Relevance:** This research directly tackles a core HCI challenge: human-agent collaboration in dynamic environments. It introduces InterruptBench to evaluate how agents handle user interruptions—such as goal revisions or retractions—during long-horizon web navigation. Most agent research assumes static goals, but real-world interaction involves evolving user intents. By analyzing how agents adapt to mid-task changes, this paper provides critical insights into building more flexible, user-aware assistants. It highlights current limitations in recovery efficiency and adaptation, guiding the design of agents that can effectively realign with human needs during complex, stateful executions.

📄 **[Full paper](https://arxiv.org/pdf/2604.00892)**

### HippoCamp: Benchmarking Contextual Agents on Personal Computers

**Relevance:** HippoCamp presents a benchmark for agents operating in user-centric environments, specifically focusing on multimodal file management on personal computers. It models individual user profiles and massive personal file systems to evaluate context-aware reasoning and search. This is deeply relevant to HCI as it shifts agent evaluation from generic tasks to personalized, high-stakes user data. The identification of multimodal perception and evidence grounding as primary bottlenecks highlights the need for better interface designs and retrieval mechanisms in personal AI assistants, providing a foundation for developing next-generation agents that truly understand a user's digital context.

💡 **[Summary](2604.01221/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.01221)**

## LLM Evaluation Methods

### Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy

**Relevance:** This study explores behavioral consistency in LLM agents, finding that while higher consistency often aligns with accuracy, it can also amplify 'consistent wrong interpretations.' This is a vital contribution to evaluation, moving beyond simple success rates to analyze reliability and failure modes. From an HCI standpoint, understanding when a model is consistently wrong is crucial for building user trust and designing effective error-correction interfaces. It emphasizes that for production deployment, interpretation accuracy is more important than mere execution stability, suggesting that evaluation should prioritize identifying systematic biases over simple variance.

💡 **[Summary](2603.25764/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.25764)**

### Brevity Constraints Reverse Performance Hierarchies in Language Models

**Relevance:** This paper reveals a counterintuitive phenomenon where larger models underperform smaller ones due to scale-dependent verbosity. By applying brevity constraints, the researchers show that large models possess superior latent capabilities masked by universal prompting. This has major implications for LLM evaluation; it suggests that standard protocols are often biased against larger models. For HCI, this implies that the way we prompt or constrain model outputs can fundamentally change perceived utility. It advocates for scale-aware prompt engineering as a core part of evaluation to accurately measure and maximize model performance in user-facing applications.

📄 **[Full paper](https://arxiv.org/pdf/2604.00025)**

### MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome

**Relevance:** MiroEval shifts evaluation from final outputs to the research process of deep research agents. It assesses how systems search, reason, and refine investigations across text and multimodal tasks. This process-centric approach is highly valuable for HCI, as it provides a diagnostic tool to understand the 'how' behind AI-generated reports. By grounding tasks in real user needs and using task-specific rubrics, it offers a more nuanced and human-aligned way to evaluate the effectiveness of complex AI-driven knowledge work. It reveals that process quality is a reliable predictor of outcomes and identifies hidden system weaknesses.

💡 **[Summary](2603.28407/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.28407)**

## Reinforcement Learning

### SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization

**Relevance:** This paper introduces an in-context RL framework for 'skill internalization,' allowing agents to acquire and internalize procedural knowledge into their parameters via a training-time curriculum. This reduces runtime token overhead and retrieval noise. In the context of HCI, this method enables the creation of more capable and efficient agents that don't require massive context windows to perform complex tasks. It explores how agents can learn from interaction history to become more autonomous, directly impacting the design of fluid human-agent collaboration systems by creating models that truly 'know' how to use tools rather than just following instructions.

💡 **[Summary](2604.02268/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.02268)**

### All Roads Lead to Rome: Incentivizing Divergent Thinking in Vision-Language Models

**Relevance:** This research investigates Group Relative Policy Optimization (GRPO) and its tendency toward 'diversity collapse' in Vision-Language Models. It proposes Multi-Group Policy Optimization (MUPO) to incentivize divergent thinking across multiple solutions. This is relevant to RL as it addresses the exploration-exploitation balance in reasoning tasks. From an HCI perspective, encouraging diverse reasoning strategies can lead to more robust and creative AI assistants that offer multiple perspectives to a user, rather than converging prematurely on a single path. It demonstrates how RL can be tuned to maintain a broader spectrum of intelligent behaviors.

📄 **[Full paper](https://arxiv.org/pdf/2604.00479)**

### MemRerank: Preference Memory for Personalized Product Reranking

**Relevance:** This paper uses RL to train a memory extractor that distills user purchase history into concise, query-independent signals for personalized product reranking. By using downstream performance as the RL reward, it optimizes for user utility. This is a clear application of RL to improve personalization in agentic systems. For HCI, it demonstrates how RL can be used to manage user context and preferences efficiently, creating more personalized and less noisy interactions in e-commerce applications. The framework measures memory quality and utility, providing a practical building block for personalization in next-generation digital assistants.

💡 **[Summary](2603.29247/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.29247)**

## Explainable AI

### AgentWatcher: A Rule-based Prompt Injection Monitor

**Relevance:** AgentWatcher addresses the opacity of prompt injection detection by using a rule-based monitor. It attributes LLM outputs to specific context segments and uses a monitor LLM to reason over explicit rules. This makes detection decisions explainable, transparent, and easy to reason about for both developers and users. This is a classic XAI contribution applied to agent security, providing clear justifications for why an action was flagged. By making the reasoning process explicit, it increases system trust and allows for better auditing of autonomous agent behaviors in security-sensitive environments.

📄 **[Full paper](https://arxiv.org/pdf/2604.01194)**

### AI Generalisation Gap In Comorbid Sleep Disorder Staging

**Relevance:** This paper uses Grad-CAM and attention visualizations to explain why deep learning models fail to generalize in clinical sleep staging for stroke patients. By showing that models focus on 'physiologically uninformative regions' in patient data, it provides a clear diagnostic for clinical experts. This is a strong example of XAI being used for clinical validation, highlighting the importance of subject-aware models. It demonstrates how interpretability methods can bridge the gap between black-box AI performance and the requirements of medical professionals, ensuring that models are grounded in domain-specific expertise before deployment.

📄 **[Full paper](https://arxiv.org/pdf/2603.23582)**

### The Model Says Walk: How Surface Heuristics Override Implicit Constraints in LLM Reasoning

**Relevance:** This paper provides a mechanistic analysis of why LLMs fail when surface heuristics conflict with unstated feasibility constraints. It uses token-level attribution and causal-behavioral analysis to 'diagnose, measure, and treat' these reasoning vulnerabilities. This work is essential for XAI as it characterizes systematic biases in model reasoning using a 'Heuristic Override Benchmark.' For HCI, it provides tools to understand model limitations, enabling the design of better prompts and interfaces that help users navigate and correct these inherent model failures. It highlights how goal-decomposition can recover performance by forcing explicit reasoning.

💡 **[Summary](2603.29025/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.29025)**

