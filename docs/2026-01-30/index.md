---
layout: default
title: 2026-01-30
permalink: /2026-01-30/
---

# 2026-01-30

## AI for Software Development

### How AI Impacts Skill Formation

**Relevance:** This paper directly investigates the critical HCI issue of how AI assistance (e.g., Copilot) affects skill acquisition in novice developers. It finds that passive delegation impairs conceptual understanding and debugging abilities. The findings are essential for designing AI tools that act as effective collaborators and mentors rather than competence shortcuts, identifying specific interaction patterns that preserve learning. This guides the design of AI assistants to support long-term human expertise in software development workflows.

💡 **[Summary](2601.20245/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.20245)**

### CooperBench: Why Coding Agents Cannot be Your Teammates Yet

**Relevance:** This work addresses the critical HCI/CSCW challenge of integrating AI agents into collaborative software development teams. By introducing a benchmark for collaborative coding tasks, it reveals that state-of-the-art agents suffer a 30% drop in success rate when coordinating compared to working individually. This highlights the urgent need for HCI research to develop social intelligence, effective communication protocols, and shared understanding mechanisms for AI agents to function as reliable teammates.

💡 **[Summary](2601.13295/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.13295)**

### SERA: Soft-Verified Efficient Repository Agents

**Relevance:** SERA focuses on creating cost-efficient, specialized coding agents for private codebases. From an HCI perspective, the ability to rapidly and cheaply specialize agents to proprietary environments (repository specialization) is a key factor for industrial adoption and developer trust. This efficiency (26x cheaper than RL) makes the continuous integration of highly relevant, domain-specific AI assistance seamlessly into enterprise development workflows practical.

💡 **[Summary](2601.20789/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.20789)**

## AI Agents

### OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution

**Relevance:** This paper describes a general-purpose agent capable of autonomous task execution across highly complex digital environments (mobile and desktop GUIs). This research fundamentally impacts HCI by defining a new paradigm for user interaction—delegating complex, multi-step tasks entirely to an autonomous entity. The use of RL for spatial grounding and sequential planning is crucial for developing reliable, trustworthy human-agent interaction in digital environments, revolutionizing human productivity.

💡 **[Summary](2601.20380/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.20380)**

### AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security

**Relevance:** AgentDoG addresses the crucial safety and trust issues arising from autonomous agents that use tools and interact with environments. By providing a Diagnostic Guardrail framework, it offers fine-grained, contextual monitoring and root cause diagnosis of unsafe actions. This introduces transparency and provenance (a core XAI/HCI principle) into agent behavior, which is necessary for effective human oversight and aligning agents with safety and security requirements.

💡 **[Summary](2601.18491/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.18491)**

### Yunjue Agent Tech Report: A Fully Reproducible, Zero-Start In-Situ Self-Evolving Agent System for Open-Ended Tasks

**Relevance:** This agent system focuses on the 'In-Situ Self-Evolving' paradigm, allowing the agent to continuously synthesize and optimize its toolset based on real-time execution feedback in open-ended environments. This self-evolution capability is highly relevant to HCI for designing robust agents that remain useful and adaptable over long periods without constant human retraining or explicit supervision, addressing the challenge of continuous capability expansion.

💡 **[Summary](2601.18226/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.18226)**

## LLM Evaluation Methods

### MortalMATH: Evaluating the Conflict Between Reasoning Objectives and Emergency Contexts

**Relevance:** MortalMATH introduces a benchmark designed to evaluate a profound failure mode: the conflict between specialized LLM reasoning and immediate human safety in emergency contexts. From an HCI perspective, evaluation must prioritize human alignment and safety over pure task accuracy. This highlights the urgent need for evaluation methods that test 'survival instincts' and context sensitivity, ensuring models do not develop 'tunnel vision' in high-stakes scenarios.

💡 **[Summary](2601.18790/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.18790)**

### Benchmarks Saturate When The Model Gets Smarter Than The Judge

**Relevance:** This work critiques the reliability of current LLM evaluation systems, showing that judge errors (even in automated judges like Omni-Judge) often mask genuine differences between models' abilities. This is essential for HCI researchers relying on quantitative benchmarks, emphasizing the critical need for robust, human-audited evaluation methodologies to ensure meaningful progress and accurate understanding of model capabilities and limitations.

💡 **[Summary](2601.19532/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.19532)**

### Persona Prompting as a Lens on LLM Social Reasoning

**Relevance:** This evaluation method assesses the impact of persona prompting on LLM rationale quality and bias in socially sensitive tasks. It uses human alignment metrics to measure agreement with human annotations. The finding that performance gains may trade off with explanation fidelity (rationale quality) is a critical insight for HCI/XAI, urging evaluation to focus not just on task completion but on the interpretability and ethical implications of the underlying model reasoning.

💡 **[Summary](2601.20757/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.20757)**

## Reinforcement Learning

### Reinforcement Learning via Self-Distillation

**Relevance:** This paper introduces SDPO, which leverages rich textual feedback (such as runtime errors in code or judge evaluations) from verifiable environments to overcome the severe credit-assignment bottleneck of scalar rewards. This is highly relevant to HCI as it mimics how humans learn from detailed corrective feedback, suggesting pathways for designing more intuitive and informative human-in-the-loop guidance mechanisms for RL agents, improving sample efficiency and final accuracy.

💡 **[Summary](2601.20802/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.20802)**

### Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning

**Relevance:** Spark improves RL efficiency for long-horizon agent tasks by selectively exploring critical decision states via dynamic branching. For HCI, this strategic exploration is vital for designing effective human supervision mechanisms. By prioritizing sampling quality at key decision points, the agent's behavior becomes more interpretable, allowing humans to guide or intervene efficiently without observing wasted computation on trivial steps.

📄 **[Full paper](https://arxiv.org/pdf/2601.20209)**

### TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment

**Relevance:** This paper proposes a closed-loop RL framework involving three co-improving roles (attacker, defender, evaluator) for LLM safety alignment. This approach formalizes an iterative, adversarial process that mirrors complex human review and safety testing. It provides an efficient and scalable paradigm for continuous safety alignment, directly benefiting HCI by improving user trust and mitigating the generation of harmful content in human-facing LLM applications.

📄 **[Full paper](https://arxiv.org/pdf/2601.18290)**

## Explainable AI

### VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

**Relevance:** VERGE is a neurosymbolic XAI framework that verifies LLM outputs using SMT solvers. Crucially, it uses logical error localization via Minimal Correction Subsets (MCS) to pinpoint the exact claims needing revision. This transforms a binary failure signal into actionable, precise feedback. This highly valuable form of transparent and verifiable explanation is essential for building human trust and enabling effective human debugging in high-stakes reasoning domains.

📄 **[Full paper](https://arxiv.org/pdf/2601.20055)**

### Linear representations in language models can change dramatically over a conversation

**Relevance:** This research reveals that internal linear representations corresponding to high-level concepts (like factuality) evolve significantly within a conversation. This finding challenges the fundamental assumption of static interpretability methods (like fixed probes or feature visualization) used in XAI. It implies that XAI tools must become dynamic and context-sensitive to accurately reflect how conversational LLMs make decisions, maintaining user understanding and trust in evolving contexts.

📄 **[Full paper](https://arxiv.org/pdf/2601.20834)**

### Persona Prompting as a Lens on LLM Social Reasoning

**Relevance:** This study directly evaluates the quality and human alignment of LLM-generated rationales (explanations) in sensitive social contexts. It reveals a critical XAI trade-off: techniques used to align output (persona prompting) can degrade the quality and human agreement of the accompanying explanations. This highlights the fragility of current XAI methods and emphasizes the need for HCI to ensure that explanations remain faithful and interpretable, especially when models are steered for specific behaviors.

📄 **[Full paper](https://arxiv.org/pdf/2601.20757)**

