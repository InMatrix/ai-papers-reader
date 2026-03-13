---
layout: default
title: 2026-03-13
permalink: /2026-03-13/
---

# 2026-03-13

## AI for Software Development

### ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning

**Relevance:** ReflexiCoder introduces a reinforcement learning framework that internalizes the debugging and optimization process directly into an LLM's weights. By teaching the model to perform bug-aware reflection and self-correction without external oracles, it significantly enhances the 'bug detection and fixing' sub-topic. From an HCI perspective, this reduces the user's need to manually verify and iteratively prompt for fixes, streamlining the developer experience. The model's ability to autonomously debug complex algorithmic tasks represents a shift toward more reliable and independent AI coding assistants that can handle structured reasoning trajectories internally.

💡 **[Summary](2603.05863/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.05863)**

### Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications

**Relevance:** This paper presents TDAD, a methodology that applies software engineering's test-driven development (TDD) principles to the creation of AI agents. It treats prompts as compiled artifacts refined through iterative testing against behavioral specifications. This is highly relevant to AI for software development as it provides a rigorous framework for ensuring code generation and tool-use compliance. By introducing mechanisms like mutation testing and regression safety scores, TDAD offers developers measurable reliability and robustness, addressing the HCI challenge of managing silent regressions and ensuring policy compliance in production-level AI software systems.

💡 **[Summary](2603.08806/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.08806)**

## AI Agents

### Meissa: Multi-modal Medical Agentic Intelligence

**Relevance:** Meissa is a specialized medical agent that masters strategy selection and execution through unified trajectory modeling. It is highly relevant to AI Agents as it demonstrates how a lightweight model can handle multi-step interactions and tool use in a high-stakes domain. Its three-tier stratified supervision allows it to learn when to engage external tools or multi-agent collaboration based on task difficulty. This addresses core agent research goals like independent problem-solving and tool integration, while its offline capability satisfies clinical requirements for privacy and low latency, essential for real-world human-agent collaboration.

💡 **[Summary](2603.09018/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.09018)**

### RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback

**Relevance:** RetroAgent introduces an online reinforcement learning framework that enables agents to evolve by learning from past experiences stored in a memory buffer. It uses a hindsight self-reflection mechanism to generate both numerical and linguistic feedback. This is a significant advancement in AI Agent research, focusing on learning from experience and adapting strategies over time. The proposed SimUtil-UCB strategy for retrieving relevant past lessons helps the agent handle out-of-distribution scenarios. This capability for test-time adaptation and continuous improvement is a key requirement for creating autonomous systems that align with human values through experience.

💡 **[Summary](2603.08561/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.08561)**

### OpenClaw-RL: Train Any Agent Simply by Talking

**Relevance:** OpenClaw-RL proposes that all agent interactions—conversations, terminal outputs, and GUI changes—provide 'next-state signals' that can be used for online learning. This framework allows a single policy to learn from diverse environments simultaneously. It is particularly relevant to the field of AI Agents because it enables agents to improve through direct use and interaction with humans (e.g., recovering signals from user corrections). This aligns with the goal of creating agents that can interact with digital tools and learn from environmental feedback in a unified, scalable RL loop.

💡 **[Summary](2603.10165/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10165)**

## LLM Evaluation Methods

### According to Me: Long-Term Personalized Referential Memory QA

**Relevance:** This paper introduces ATM-Bench, a benchmark designed to evaluate multimodal, long-term personalized memory in AI assistants. It moves beyond standard dialogue history to include multi-source evidence like images and emails spanning years. This is a critical evaluation method from an HCI perspective, as it assesses a model's ability to maintain user context and resolve complex personal references. By testing for multi-evidence reasoning and conflicting information, ATM-Bench provides a more realistic measure of how well an LLM can serve as a personalized assistant while maintaining coherence and trust over time.

💡 **[Summary](2603.01990/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.01990)**

### Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams

**Relevance:** The OAKS benchmark evaluates LLMs on their ability to adapt to streaming, continually updating knowledge. This is essential for understanding how models handle dynamic real-world information where facts change over time. The evaluation measures state-tracking accuracy and susceptibility to distraction in a sequence of context chunks. For HCI, this benchmark is vital because it tests the model's reliability and 'up-to-dateness'—factors that directly impact user satisfaction and trust when interacting with AI systems in evolving contexts where static knowledge is insufficient.

💡 **[Summary](2603.07392/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.07392)**

### Do What I Say: A Spoken Prompt Dataset for Instruction-Following

**Relevance:** DOWIS provides a multilingual dataset of human-recorded spoken prompts to evaluate Speech Large Language Models (SLLMs). This addresses a gap in evaluation methods that typically rely on text, which fails to capture the nuances of real-world speech interaction. By benchmarking models across different styles and tasks using actual audio, it offers a more ecologically valid assessment of SLLM performance. This is highly relevant to HCI for designing inclusive systems that respond accurately to vocal instructions, helping researchers identify where models fail in cross-lingual or low-resource speech settings.

💡 **[Summary](2603.09881/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.09881)**

## Reinforcement Learning

### In-Context Reinforcement Learning for Tool Use in Large Language Models

**Relevance:** This paper introduces ICRL, an RL-only framework that leverages few-shot prompting to teach LLMs how to use external tools. It bypasses the need for expensive supervised fine-tuning (SFT) by using in-context examples during the RL rollout. This research is relevant to RL policy optimization and exploration, as it demonstrates how models can learn complex tool-calling behaviors through interaction and feedback. From an HCI perspective, this provides a data-efficient way to adapt agents to new tools and environments, facilitating more intuitive and capable human-agent collaboration without massive labeled datasets.

💡 **[Summary](2603.08068/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.08068)**

### CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR

**Relevance:** CLIPO addresses the issue of 'hallucination' and inconsistent reasoning in RL with verifiable rewards. By incorporating a contrastive learning mechanism, it forces the model to capture invariant structures across correct reasoning paths rather than just memorizing paths to the final answer. This is a significant contribution to RL policy optimization, ensuring that the 'brain' of the agent learns robust strategies. In an HCI context, this leads to more reliable and interpretable AI behavior, as the model's intermediate reasoning steps become more consistent and less prone to generating nonsensical but outcome-correct artifacts.

💡 **[Summary](2603.10101/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10101)**

### V_{0.5}: Generalist Value Model as a Prior for Sparse RL Rollouts

**Relevance:** V_{0.5} proposes a method to improve RL policy gradients by fusing pre-trained generalist value models with empirical data from sparse rollouts. It uses real-time statistical testing and dynamic budget allocation to balance estimator variance against model bias. This is highly relevant to RL research in environments with sparse rewards, where constructing a stable advantage baseline is difficult. For HCI, this means more efficient training of AI agents for complex reasoning tasks (like math), allowing for faster convergence and more stable learning of optimal behaviors in challenging, multi-step environments.

💡 **[Summary](2603.10848/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10848)**

## Explainable AI

### Causal Concept Graphs in LLM Latent Space for Stepwise Reasoning

**Relevance:** This paper introduces Causal Concept Graphs (CCG), which map interpretable latent features and their causal dependencies during multi-step reasoning. This goes beyond standard XAI techniques like feature visualization by showing how concepts interact to produce a decision. By using differentiable structure learning, it provides a transparent view of the model's internal 'logic' graph. This is highly relevant to HCI for building trust and allowing users to debug or intervene in the model's reasoning process, as it offers a human-readable explanation of the causal flow within the high-dimensional latent space.

💡 **[Summary](2603.10377/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10377)**

### Are Audio-Language Models Listening? Audio-Specialist Heads for Adaptive Audio Steering

**Relevance:** This work uses mechanistic interpretability to identify 'audio-specialist' attention heads in multimodal models. These heads provide a 'listening' signal that indicates when the model is grounding its output in audio rather than just text. By localizing these heads, the researchers can apply an inference-time intervention to amplify audio engagement. This is a valuable XAI contribution because it helps explain and mitigate 'text dominance' in multimodal models. For HCI, this allows for better control over how models utilize different sensory inputs, ensuring that predictions are transparently grounded in the relevant non-textual data.

💡 **[Summary](2603.06854/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.06854)**

### Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models

**Relevance:** CSRO reframes multi-agent policy discovery by prompting LLMs to generate policies as human-readable code instead of 'black-box' neural networks. This makes the resulting policies inherently interpretable, debuggable, and transparent. It is a novel approach to XAI that leverages the structured nature of code to explain complex agent strategies. From an HCI perspective, this allows human designers to audit and understand the logic of multi-agent systems, shifting the focus from opaque parameter optimization to synthesizing explainable algorithmic behavior that can be easily verified and aligned with human intentions.

💡 **[Summary](2603.10098/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10098)**

