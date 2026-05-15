---
layout: default
title: 2026-05-15
permalink: /2026-05-15/
---

# 2026-05-15

## AI for Software Development

### Orchard: An Open-Source Agentic Modeling Framework

**Relevance:** This paper introduces Orchard-SWE, a specialized agentic modeling recipe designed for coding tasks. It addresses the lack of scalable open-source infrastructure for software engineering agents by distilling trajectories from proprietary models and applying credit-assignment supervised fine-tuning. From an HCI perspective, Orchard enables more accessible development of autonomous coding assistants that can solve complex repository-level issues. By providing lightweight sandbox lifecycle management, it allows researchers to build and evaluate tools that assist developers in multi-turn interactions, reducing the cognitive load of manual code refactoring and bug fixing.

💡 **[Summary](2605.15040/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.15040)**

### An Empirical Study of Automating Agent Evaluation

**Relevance:** While focused on evaluation, this study specifically examines the ability of frontier coding assistants to generate complex software artifacts, such as evaluation pipelines. It reveals a gap between general coding ability and domain-specific software engineering, showing that simple prompting leads to over-engineered and brittle solutions. The introduction of EvalAgent, which uses procedural instructions and reusable code templates, demonstrates how AI can be better structured to assist in the software development lifecycle, particularly for the specialized task of building robust testing and metric-generation infrastructure.

💡 **[Summary](2605.11378/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.11378)**

## AI Agents

### PREPING: Building Agent Memory without Tasks

**Relevance:** PREPING addresses the 'cold-start' problem in agent deployment by allowing agents to build procedural memory through self-generated synthetic practice before encountering real tasks. This is a significant advancement for AI agents, as it reduces the reliance on curated demonstrations. From an HCI standpoint, this reduces the user's burden of providing initial training data or guidance. The framework ensures that agents arrive in new digital environments with pre-established skills, making them more autonomous and reducing the deployment time and cost for the end user.

💡 **[Summary](2605.13880/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.13880)**

### EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

**Relevance:** EvolveMem introduces a self-evolving memory architecture where the agent autonomously optimizes its own retrieval configurations and strategies. This move from fixed to adaptive infrastructure allows agents to better handle long-term, multi-session interactions. In HCI, this is crucial for building personalized agents that grow more effective over time. By diagnosing its own failures and proposing architectural adjustments, the agent minimizes the need for manual tuning by human developers, leading to a more seamless and intelligent user experience in long-horizon tasks.

💡 **[Summary](2605.13941/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.13941)**

### Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

**Relevance:** This survey provides a comprehensive roadmap for multi-agent systems, focusing on how specialized agents can coordinate and self-evolve. It identifies the 'LIFE' progression (Foundation, Integration, Fault Attribution, Evolution) as a framework for building collective intelligence. For HCI researchers, this paper highlights the causal dependencies in agent collaboration and the risks of error propagation. Understanding these dynamics is essential for designing multi-agent interfaces where humans can effectively monitor, diagnose, and collaborate with groups of autonomous software entities.

💡 **[Summary](2605.14892/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.14892)**

## LLM Evaluation Methods

### MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

**Relevance:** MemEye addresses a critical gap in multimodal agent evaluation: the preservation of fine-grained visual evidence. Many current benchmarks allow agents to 'cheat' using text-based traces. MemEye forces agents to reason over pixel-level details and visual state changes over time. From an HCI perspective, this is vital for ensuring that visual assistants (e.g., for navigation or accessibility) truly understand the visual environment rather than relying on superficial textual summaries, thereby improving user trust and system reliability in visually-intensive tasks.

💡 **[Summary](2605.15128/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.15128)**

### FutureSim: Replaying World Events to Evaluate Adaptive Agents

**Relevance:** FutureSim proposes a novel evaluation method by replaying real-world events in chronological order to test how agents adapt to new information. This shifts evaluation from static benchmarks to dynamic, open-ended simulations. This is highly relevant to HCI because real-world AI deployment happens in non-stationary environments. By measuring Brier skill scores and adaptation over long horizons, FutureSim provides a more realistic assessment of how agents will perform when assisting users with volatile, real-world information, such as news or financial events.

💡 **[Summary](2605.15188/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.15188)**

### RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation

**Relevance:** RealICU challenges the standard evaluation practice of imitating historical clinician actions, which may be suboptimal. Instead, it uses hindsight-annotated 'gold' labels from expert reviews of full patient trajectories. This is a landmark for evaluation in high-stakes HCI domains. It exposes critical failure modes like 'anchoring bias' in AI, where models stick to early, potentially wrong interpretations. This benchmark provides the rigorous, clinically-grounded testing necessary to develop AI decision-support systems that humans can safely rely on in intensive care settings.

💡 **[Summary](2605.13542/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.13542)**

## Reinforcement Learning

### Self-Distilled Agentic Reinforcement Learning

**Relevance:** SDAR addresses the difficulty of applying RL to multi-turn agents where trajectory-level rewards are too coarse. By introducing token-level guidance through self-distillation, it provides a denser supervision signal. This is relevant to HCI because multi-turn interactions are the bedrock of human-agent collaboration. SDAR's ability to improve performance across diverse environments like search and web shopping suggests it can help create more responsive and accurate agents that learn more effectively from complex, interactive user feedback than standard RL methods.

💡 **[Summary](2605.15155/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.15155)**

### Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization

**Relevance:** This paper proposes an RL framework that teaches agents when to explore and when to execute, based on uncertainty. This is a fundamental challenge in the exploration-exploitation trade-off. From an HCI perspective, an agent that knows when it lacks information and needs to 'explore' (e.g., by asking a user a question or searching) is far more useful than one that blindly executes. This RL approach scales the agent's ability to gather environmental feedback, leading to more efficient task completion and reduced user frustration.

💡 **[Summary](2605.08978/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.08978)**

### PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation

**Relevance:** PhyMotion uses a physics simulator to provide structured rewards for RL-based video generation, focusing on kinematic plausibility and balance. In the context of HCI, this is essential for generating realistic human movements in virtual environments or simulations. By grounding the RL reward in physical laws rather than just 2D perceptual metrics, the model produces motion that is more convincing and less likely to exhibit 'uncanny valley' effects, which is critical for user immersion and the training of vision systems.

💡 **[Summary](2605.14269/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.14269)**

## Explainable AI

### Nexus : An Agentic Framework for Time Series Forecasting

**Relevance:** Nexus bridges the gap between numerical forecasting and contextual reasoning. Crucially for XAI, it produces high-quality reasoning traces that explicitly detail the fundamental drivers behind its forecasts (e.g., identifying specific news events affecting a stock). For human users, especially in high-stakes financial or real estate domains, this 'explanation' of a prediction is often more valuable than the number itself. It allows human experts to audit the AI's logic, fostering trust and better-informed human-in-the-loop decision-making.

💡 **[Summary](2605.14389/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.14389)**

### From Pixels to Concepts: Do Segmentation Models Understand What They Segment?

**Relevance:** This paper introduces the CAFE benchmark, which uses counterfactual attribute manipulation to determine if segmentation models are truly grounding concepts or just finding visual shortcuts. This is a classic XAI methodology applied to computer vision. By modifying attributes like material or context while keeping the mask the same, it reveals whether a model's decision-making is based on superficial mimicry. This is essential for HCI applications like autonomous driving or medical imaging, where it is critical to know if the AI 'understands' the object it is identifying.

💡 **[Summary](2605.09591/)** 📄 **[Full paper](https://arxiv.org/pdf/2605.09591)**

