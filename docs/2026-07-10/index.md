---
layout: default
title: 2026-07-10
permalink: /2026-07-10/
---

# 2026-07-10

## AI for Software Development

### Teaching LLMs a Low-Resource Language: Enhancing Code Completion in Pharo

**Relevance:** This paper addresses a significant gap in AI-assisted software development: support for low-resource programming languages. By developing an end-to-end pipeline for Pharo (a Smalltalk-inspired language), the authors show how to bring advanced code completion to niche developer communities. From an HCI perspective, this is highly valuable because it democratizes AI coding assistants, which are typically biased towards mainstream languages. The focus on creating models small enough for real-time, in-IDE support directly impacts user experience, reducing cognitive friction and latency during the software development workflow.

📄 **[Full paper](https://arxiv.org/pdf/2607.04939)**

### SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review

**Relevance:** While typical AI coding tools focus on one-shot code generation, this paper addresses the collaborative and iterative nature of software engineering by introducing an agentic code review framework (SWE-Review). This is highly relevant to HCI because software development is inherently collaborative; developers do not just accept raw code but review, discuss, and revise it. By closing the loop with automated, structured feedback, the tool mimics human-to-human code review workflows. This iterative interaction model lowers the barrier to trust for AI-generated code and improves downstream software quality through collaborative refinement.

💡 **[Summary](2607.06065/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.06065)**

## AI Agents

### Automating the Design of Embodied Agent Architectures

**Relevance:** This paper introduces AgentCanvas, a visual, graph-based runtime that models embodied agents as editable node-and-wire programs with episode-level logs. This has profound implications for HCI and Agent design, as it transitions agent creation from opaque, code-heavy implementations to inspectable, visual representations. By automating architecture search (AAS) and exposing execution traces, it helps human designers understand where information is stored and how decisions are made. This visual-symbolic layout bridges the gap between machine optimization and human-centric design, allowing researchers to easily debug and configure agent behaviors.

📄 **[Full paper](https://arxiv.org/pdf/2606.30111)**

### CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration

**Relevance:** CanvasAgent represents a shift from passive perception agents to active, manipulation-centered visual creation agents. It orchestrates heterogeneous visual tools (segmentation, editing, compositing) through multi-turn interactions. For HCI, this is a prime example of an agent collaborating with users on complex creative tasks. By inspecting intermediate results and adapting its strategy based on the evolving visual state, CanvasAgent acts as a co-creator. Understanding how users guide such multi-tool orchestration and how the agent communicates its intermediate visual hypotheses is crucial for designing intuitive, agent-assisted creative interfaces.

📄 **[Full paper](https://arxiv.org/pdf/2607.05465)**

## LLM Evaluation Methods

### AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

**Relevance:** Traditional agent benchmarks rely on binary pass/fail outcomes, ignoring the user-experience journey. AgentLens addresses this by evaluating the entire interaction trajectory—how agents follow instructions, use tools, recover from errors, and communicate. This shift from outcome-only to process-oriented evaluation is deeply rooted in HCI principles. By pairing formal verification with LLM-generated trajectory reviews and side-by-side comparisons, AgentLens provides human-readable explanations. This helps developers diagnose agent behavior, catch regressions, and ensure that agent actions align with user expectations, directly fostering trust and system transparency.

📄 **[Full paper](https://arxiv.org/pdf/2607.06624)**

### VIBE: Voice-Induced open-ended Bias Evaluation for Large Audio-Language Models via Real-World Speech

**Relevance:** As audio-language models become integrated into daily applications, evaluating their biases under realistic, open-ended scenarios is critical for safe human-AI interaction. VIBE moves away from rigid multiple-choice benchmarks toward natural, voice-induced interactions using real-world speech. This is highly relevant to HCI evaluation methods as it measures how subtle vocal cues (gender, accent) trigger conversational biases in open recommendations. By assessing how stereotypes manifest organically, VIBE provides a more ecological and user-centric approach to evaluating fairness, safety, and inclusivity in voice-based AI systems.

💡 **[Summary](2604.17248/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.17248)**

## Reinforcement Learning

### Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

**Relevance:** This paper introduces Single-rollout Asynchronous Optimization (SAO) to address training stability and off-policy challenges in agentic RL. For HCI, the stability of RL training is critical when agents are deployed in real-world, interactive environments where they must adapt to changing user preferences or evolving tasks. By replacing group-wise sampling with single-rollout sampling, SAO improves generalization and training efficiency. This is highly beneficial for designing interactive learning systems where human feedback or environment dynamics change dynamically, allowing the underlying agent to adapt stably without catastrophic policy degradation.

📄 **[Full paper](https://arxiv.org/pdf/2607.07508)**

### Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

**Relevance:** This paper uncovers a surprising structural phenomenon in RL post-training: the benefits of RL adaptation are highly concentrated in a small subset of (or even a single) middle transformer layers. From an HCI and system design perspective, this has massive implications. If RL adaptation can be localized to a single layer, it drastically reduces the computational overhead required to personalize or fine-tune models based on human feedback (RLHF). This enables highly efficient, lightweight, and potentially local adaptation of LLMs to individual users, lowering the barrier to real-time, interactive personalization.

💡 **[Summary](2607.01232/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.01232)**

## Explainable AI

### Attending to Multimodal Generation One Token at a Time

**Relevance:** This paper addresses a key interpretability gap in multimodal LLMs by tracking attention shifts across image, text, and instruction tokens dynamically (One Token at a Time). For XAI and HCI, understanding when a model leverages specific modalities is critical for explaining multimodal decisions. The authors use attention-blocking interventions to demonstrate how attention disruptions cause models to fall back on language priors or leak information. The proposed test-time intervention to boost attention at key moments not only improves performance but provides a clear mechanism to explain and steer model focus, enhancing user trust.

📄 **[Full paper](https://arxiv.org/pdf/2607.03738)**

### RuleChef: Grounding LLM Task Knowledge in Human-Editable Rules

**Relevance:** RuleChef addresses a core goal of XAI: replacing complex, opaque model inferences with deterministic, inspectable, and human-editable rules. Instead of using LLMs at runtime, RuleChef uses them at training time to synthesize and iteratively patch rules based on human feedback. This is highly aligned with HCI principles of human-in-the-loop design and agency. By outputting explicit, readable rule systems, it allows domain experts to easily audit, modify, and verify the system's logic, ensuring safety, predictability, and complete transparency in high-stakes text processing tasks.

📄 **[Full paper](https://arxiv.org/pdf/2607.01293)**

### Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

**Relevance:** SciReasoner focuses on making structural reasoning in scientific domains (biology, chemistry, materials science) transparent and explainable. It discretizes complex coordinates and topologies into addressable tokens, generating explicit, fragment-level disconnection and verification traces. In expert evaluations, its reasoning traces were highly preferred, demonstrating that scientific AI can move beyond black-box predictions to provide inspectable evidence. This is a crucial advancement for XAI in professional domains, where human scientists must understand and trust the physical constraints and logical steps behind an AI's prediction before acting on it.

💡 **[Summary](2607.07708/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.07708)**

