---
layout: default
title: 2026-04-10
permalink: /2026-04-10/
---

# 2026-04-10

## AI for Software Development

### SEVerA: Verified Synthesis of Self-Evolving Agents

**Relevance:** SEVerA addresses the critical need for reliability in AI-driven software development by introducing a verified synthesis framework for self-evolving agents. It combines formal specifications with generative models to ensure that synthesized agent programs, which are often used for tasks like autonomous program repair, satisfy safety and correctness constraints. For HCI, this provides a mechanism for "guarded" autonomy, allowing developers to trust AI agents to execute code without violating hard logical constraints. This integration of formal methods with LLMs represents a significant step toward robust, deployable AI software assistants that maintain high performance while guaranteeing behavioral compliance.

💡 **[Summary](2603.25111/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.25111)**

### Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

**Relevance:** Squeez addresses the efficiency bottleneck in coding agents by introducing task-conditioned tool-output pruning. In software development, agents often process massive logs, repository files, or API responses where only a tiny fraction of the data is relevant to the next coding step. Squeez uses a fine-tuned model to return only the essential evidence blocks, significantly reducing token usage while maintaining high recall. This is highly relevant to HCI as it reduces the cognitive load on both the agent and the human overseer, enabling faster iterations and more focused interactions during complex, multi-step software engineering tasks.

💡 **[Summary](2604.04979/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.04979)**

## AI Agents

### Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

**Relevance:** This paper provides a foundational systems-level framework for AI agents, arguing that progress depends on "externalizing" cognitive burdens into memory, skills, and protocols. This perspective is deeply relevant to HCI, as it treats agent infrastructure as a set of "cognitive artifacts" that help models solve tasks more reliably. By organizing the agent's runtime around these external modules, researchers can design more transparent and manageable systems. The review offers a roadmap for building sophisticated agents that go beyond simple prompting, focusing on how structured harnesses can coordinate complex human-agent interactions and maintain state over time.

💡 **[Summary](2604.08224/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08224)**

### Qualixar OS: A Universal Operating System for AI Agent Orchestration

**Relevance:** Qualixar OS represents a major leap in agent orchestration by providing a universal application-layer operating system for multi-agent systems. It supports heterogeneous frameworks and provides visual tools like a production dashboard and workflow builder. For HCI, this is significant because it shifts agent development from low-level coding to high-level orchestration and monitoring. The inclusion of features like content attribution and consensus-based judging addresses key human-centric concerns regarding trust, accountability, and the management of complex, multi-agent collaborative environments, making it a robust platform for studying how humans interact with large-scale agent ecosystems.

📄 **[Full paper](https://arxiv.org/pdf/2604.06392)**

### SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

**Relevance:** SkillClaw introduces a framework for collective skill evolution in multi-user agent ecosystems. Instead of treating agent skills as static, it aggregates trajectories and experiences across different users to refine and extend the agent’s capabilities autonomously. This is a quintessential HCI-AI problem: how to leverage distributed human interactions to improve system performance over time. By allowing improvements discovered in one user’s context to propagate system-wide without additional effort, SkillClaw enables a form of collaborative learning that reduces individual user burden while continuously enhancing the agent's utility and adaptability in complex, real-world scenarios.

💡 **[Summary](2604.08377/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08377)**

## LLM Evaluation Methods

### KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation

**Relevance:** KnowU-Bench is a user-centric benchmark that evaluates mobile agents on their ability to infer preferences and provide proactive assistance. Unlike traditional app-centric benchmarks, it focuses on interactive dynamics, such as seeking consent and eliciting missing information through dialogue in a live GUI environment. This is highly relevant to HCI research on trust and autonomy, as it measures whether agents can navigate the "proactive decision chain" without being intrusive. By testing agents using a user simulator grounded in structured profiles, it provides a realistic assessment of an agent's ability to act as a personalized digital assistant.

💡 **[Summary](2604.08455/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08455)**

### Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization

**Relevance:** This paper addresses the challenge of "pluralistic alignment" by evaluating how well reward models capture individual user preferences. In HCI, personalization is key to user satisfaction, yet most benchmarks focus on general response quality. Personalized RewardBench uses human-aligned rubrics to ensure that preference distinctions are tailored to individuals. This provides a robust proxy for evaluating how agents will perform in downstream personalized applications. It highlights the gap in current models' ability to handle subjective values, pushing the field toward evaluation methods that respect diverse human perspectives and specific user needs in interactive settings.

💡 **[Summary](2604.07343/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.07343)**

### Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces

**Relevance:** OmniBehavior introduces a benchmark for user simulation based entirely on real-world, long-horizon data. It identifies a critical "Utopian bias" in current LLMs, where they tend to simulate a "positive average person" rather than capturing individual differences and long-tail behaviors. This has profound implications for HCI, as user simulators are often used to test interfaces and predict user needs. By exposing the structural biases in how LLMs model human behavior, this research guides the development of more high-fidelity, representative simulations that are essential for designing inclusive, effective, and realistic human-centered systems.

💡 **[Summary](2604.08362/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.08362)**

## Reinforcement Learning

### OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks

**Relevance:** OpenVLThinkerV2 introduces Gaussian GRPO, a novel RL objective designed to handle the extreme variance in rewards across diverse visual tasks. From an HCI perspective, this is important because it stabilizes the training of multimodal models that must balance fine-grained perception with multi-step reasoning. The paper also explores "response length shaping" to elicit reasoning chains, which can improve the interpretability of the model’s decision-making process for human users. This work demonstrates how RL can be tuned to create more robust and "thoughtful" agents capable of handling complex, real-world visual environments with improved stability.

📄 **[Full paper](https://arxiv.org/pdf/2604.08539)**

### Learning to Hint for Reinforcement Learning

**Relevance:** This paper explores "Hint Learning" (HiLL), where a hinter policy is trained to provide adaptive guidance to a reasoner during reinforcement learning. This mirrors human pedagogical strategies and is highly relevant to HCI research on human-agent collaboration and "human-in-the-loop" RL. By generating hints that are transferable to "no-hint" scenarios, the framework demonstrates how structured intervention can facilitate agent learning. This approach offers insights into how systems can be designed to accept and benefit from human-provided cues, making the learning process more efficient, interactive, and aligned with how humans naturally teach.

💡 **[Summary](2604.00698/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.00698)**

### RAGEN-2: Reasoning Collapse in Agentic RL

**Relevance:** RAGEN-2 identifies "template collapse" in agentic RL, where models adopt input-agnostic reasoning patterns despite appearing diverse via entropy metrics. The paper proposes using Mutual Information as a diagnostic tool to ensure that an agent's reasoning is actually responsive to different inputs. For HCI, this is a critical safety and usability concern: an agent that appears to be "thinking" but isn't actually processing the specific user context is untrustworthy. RAGEN-2 provides the metrics and filtering strategies needed to ensure that RL-trained agents remain grounded and context-aware during multi-turn interactions in complex environments.

💡 **[Summary](2604.06268/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.06268)**

## Explainable AI

### Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning

**Relevance:** This paper introduces a process-driven generation paradigm that decomposes image synthesis into an interleaved reasoning trajectory of planning, drafting, and reflection. This "chain-of-thought" for images makes the generative process explicit and interpretable, allowing users to see why a model made certain visual choices. By grounding each step in evolving visual states and providing textual reflections, the model offers a level of transparency that is often missing in "black-box" diffusion models. This is a significant contribution to XAI, enabling better human oversight, auditability, and steerability in creative AI tools.

💡 **[Summary](2604.04746/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.04746)**

### The Depth Ceiling: On the Limits of Large Language Models in Discovering Latent Planning

**Relevance:** This research investigates the limits of "latent planning" in LLMs—the ability to reason internally without explicit chain-of-thought. It finds that models have a strict "ceiling" on how many planning steps they can execute latently. This discovery reinforces the importance of XAI and CoT monitoring; if complex reasoning cannot be done latently, it must be externalized to be successful. This provides a theoretical justification for requiring agents to provide step-by-step explanations for complex tasks, ensuring that their internal processes remain visible, auditable, and understandable to human users in high-stakes scenarios.

📄 **[Full paper](https://arxiv.org/pdf/2604.06427)**

