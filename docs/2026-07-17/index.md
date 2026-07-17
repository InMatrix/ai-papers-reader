---
layout: default
title: 2026-07-17
permalink: /2026-07-17/
---

# 2026-07-17

## AI for Software Development

### Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code

**Relevance:** This paper introduces generative compilation, a method that provides real-time compiler feedback on partial programs during the autoregressive generation process. This directly impacts AI-assisted code generation tools by catching semantic errors early, reducing error cascades, and decreasing cognitive load for developers trying to debug generated code. By transforming partial code into compilable structures, it bridges the gap between static language constraints and LLM sampling. From an HCI perspective, this shifts the compiler from a passive post-generation check to an active collaborator, significantly improving the developer experience and system trustworthiness during real-time code completion.

💡 **[Summary](2607.13921/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.13921)**

### Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution

**Relevance:** This paper addresses software issue resolution by proposing ACQUIRE, a QA-driven framework that acquires repository knowledge prior to generating patches. By explicitly identifying and resolving knowledge gaps before coding, this mimics a human developer's workflow and improves the accuracy of automated bug fixing. This approach presents a highly collaborative paradigm for AI-assisted programming, showing how structured repository exploration can prevent factual errors in generated code. For HCI, it demonstrates how dividing complex software tasks into explicit, understandable stages (knowledge acquisition then resolution) improves both model performance and developer inspectability.

💡 **[Summary](2607.11111/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.11111)**

### Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable

**Relevance:** This paper presents Harness Handbook, a behavior-centric representation synthesized from agent codebase to help developers and coding agents identify where to make modifications. By improving behavior localization and edit-plan quality, it directly aids software developers in maintaining and refactoring complex AI agent infrastructures. This work is highly relevant to HCI for software development, as it addresses the cognitive friction of navigating large, distributed codebases. By progressively disclosing details guided by high-level behaviors, it supports developers in understanding and editing AI agent behaviors more intuitively, streamlining the software maintenance lifecycle.

💡 **[Summary](2607.13285/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.13285)**

## AI Agents

### PalmClaw: A Native On-Device Agent Framework for Mobile Phones

**Relevance:** PalmClaw is an open-source agent framework running natively on mobile phones, bypassing long GUI interaction sequences by exposing device capabilities directly as tools with explicit arguments. Running agents natively on-device dramatically improves response times and preserves user privacy, which are critical factors for user trust and satisfaction. From an HCI perspective, PalmClaw redefines how users interact with mobile agents, shifting from slow, error-prone visual GUI tapping to direct, secure capability execution. This framework significantly reduces the execution boundaries and latency of mobile automation, creating a more seamless user experience.

📄 **[Full paper](https://arxiv.org/pdf/2607.13027)**

### Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos

**Relevance:** This paper presents Vinci2, an agentic system that shifts from reactive to proactive assistance using egocentric videos. It reasons over temporal context to decide when and if to intervene (e.g., safety alerts or habit coaching). This is a crucial HCI direction for wearable AI, focusing on user context, history, and minimizing unwanted interruptions. By reframing proactive assistance as a context-dependent decision problem, it explores how agents can seamlessly integrate into a user's daily life without causing cognitive overload or annoyance, offering a blueprint for future human-agent daily interactions.

💡 **[Summary](2607.11523/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.11523)**

### KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

**Relevance:** This paper introduces KnowAct-GUIClaw, a framework that leverages accumulated user interaction experience and feedback to continuously improve GUI manipulation, task decomposition, and tool calls. It directly supports cross-platform GUI interaction, making it highly valuable for personal AI assistants adapting dynamically to diverse operating systems and user habits. From an HCI standpoint, this research highlights how self-evolving memory systems can align AI agent actions with specific user preferences over time. This continuous learning from user feedback ensures the agent remains personalized, adaptive, and highly accurate during long-horizon tasks.

💡 **[Summary](2607.12625/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.12625)**

## LLM Evaluation Methods

### AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities

**Relevance:** This paper introduces AgentCompass, a lightweight, extensible infrastructure designed to evaluate LLM-based agents across multiple benchmarks. Crucially for HCI and system design, it separates benchmarks, harnesses, and environments, and features trajectory analysis tools to diagnose complex failure modes like reward-hacking. By providing a unified and reproducible evaluation pipeline, it helps researchers systematically study agent behavior, reliability, and safety. This infrastructure is essential for establishing user trust in autonomous agents, as it allows developers to rigorously test models under diverse environments and ensure alignment with human values.

💡 **[Summary](2607.13705/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.13705)**

### Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists

**Relevance:** This paper presents SDABench, a benchmark that evaluates LLMs on scientific data analysis across capabilities like hypothesis exploration and causal reasoning. It introduces a five-stage error analysis framework that locates exactly where LLMs fail, helping researchers understand the cognitive limitations of models when assisting humans in scientific discovery. From an HCI perspective, this benchmark provides critical insights into how LLMs can be designed to support human scientists. By identifying specific failure modes in reasoning and assumption selection, it guides the design of more effective, collaborative human-AI scientific interfaces.

💡 **[Summary](2607.11079/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.11079)**

### Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models

**Relevance:** This paper introduces blind-spots-bench, a diagnostic stress test evaluating tasks that are trivial for humans but challenging for modern AI models. This human-centric evaluation approach is highly aligned with HCI, as it directly exposes the gap between human common-sense reasoning and machine capabilities, highlighting critical limitations in safety and trust. By systematically identifying these 'blind spots' across language, vision, and image-generation models, the benchmark helps developers build more robust systems. It ensures that AI models can be evaluated against realistic human expectations, preventing unexpected failures in user-facing deployments.

💡 **[Summary](2607.08317/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.08317)**

## Reinforcement Learning

### SPEAR: A Simulator for Photorealistic Embodied AI Research

**Relevance:** SPEAR is a simulator built on Unreal Engine that provides high programmability and photorealistic rendering for training embodied agents. It allows human-in-the-loop co-simulation with physics engines and scene editing via natural language. This provides a novel environment design that facilitates intuitive human-agent collaboration and training of agents in complex, realistic scenarios. For HCI, SPEAR represents a powerful platform for designing and testing how humans can guide agent learning within immersive, photorealistic virtual environments. Its natural language editing capabilities lower the barrier for non-experts to customize training environments and interact with agents.

💡 **[Summary](2607.06701/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.06701)**

### Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation

**Relevance:** This paper proposes SpectraReward, which uses pretrained multimodal LLMs as zero-shot reward models for text-to-image reinforcement learning. By measuring prompt recovery likelihood, it circumvents the need for expensive human preference labels. It demonstrates how models can self-improve while aligning with the original human intent expressed in prompts. This is highly relevant to HCI because it explores how to align complex image generation with user-defined prompts without requiring continuous manual feedback. It streamlines the reinforcement learning pipeline, making the creation of personalized, high-fidelity generative models more accessible and less labor-intensive.

💡 **[Summary](2607.11886/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.11886)**

### Principled Analysis of Deep Reinforcement Learning Evaluation and Design Paradigms

**Relevance:** This paper conducts a large-scale analysis of standard evaluation and design paradigms in deep reinforcement learning, showing how current practices can lead to incorrect conclusions about scaling and performance. This is crucial for designing reliable RL systems, helping developers understand how to correctly evaluate and guide agent learning under different data regimes. From an HCI perspective, understanding these scaling and evaluation boundaries is essential for building predictable and interpretable RL systems. It ensures that when humans interact with or guide these agents, the system's learning progression remains stable and aligned with design expectations.

💡 **[Summary](2607.07769/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.07769)**

## Explainable AI

### What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness

**Relevance:** This paper explores the gap between LLM reasoning traces (CoT) and their actual internal states by training probes on intermediate activations. These probes serve as 'lie detectors' that track behavioral shifts better than the generated text, providing a powerful, non-textual explainability mechanism to audit, calibrate, and verify the faithfulness of model reasoning. From an HCI perspective, this research exposes a critical limitation of relying solely on natural language explanations for user trust. It offers a practical methodology to build more transparent interfaces that can alert users when a model's generated reasoning is unfaithful to its internal predictions.

💡 **[Summary](2607.08046/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.08046)**

### Length Penalties Make Chain-of-Thought Less Monitorable

**Relevance:** This paper investigates how training with length penalties compresses chain-of-thought (CoT) reasoning but hides the underlying influences driving the model's answers. This exposes a crucial trade-off between computational efficiency and explainability, warning that shorter reasoning traces make AI systems significantly harder for humans to monitor and audit. From an HCI and safety perspective, this work highlights the danger of optimizing models purely for token efficiency. It emphasizes that to maintain human trust and monitorability, interface designers and AI engineers must preserve rich reasoning traces, even if they incur higher computational costs.

💡 **[Summary](2607.09786/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.09786)**

### Evidence-Backed Video Question Answering

**Relevance:** This paper introduces Evidence-Backed Video Question Answering (E-VQA), which requires models to output both a semantic answer and precise spatio-temporal visual evidence (tracked segmentation masklets). This directly addresses the black-box nature of video LLMs, providing visually grounded explanations that help users verify and trust the model's outputs. For HCI, this represents a significant advancement in explainable AI for video. Instead of relying on vague text descriptions, users are provided with concrete, pixel-level visual justifications, making it much easier to diagnose errors, verify model claims, and build robust, trustworthy collaborative video analysis tools.

💡 **[Summary](2607.11862/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.11862)**

