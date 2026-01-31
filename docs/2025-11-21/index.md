---
layout: default
title: 2025-11-21
permalink: /2025-11-21/
---

# 2025-11-21

## AI for Software Development

### LLM-Powered Fully Automated Chaos Engineering: Towards Enabling Anyone to Build Resilient Software Systems at Low Cost

**Relevance:** This paper is highly relevant as it automates the entire Chaos Engineering (CE) cycle, which involves complex software engineering tasks such as requirement definition, code generation, testing, and debugging, using LLM agents. From an HCI perspective, ChaosEater significantly lowers the barrier to entry for building resilient systems, enabling non-experts to leverage sophisticated AI for critical infrastructure tasks. The automation of planning and post-experiment analysis, previously manual and labor-intensive, represents a major shift in how developers interact with resilience testing tools, moving towards fully autonomous AI assistance in the software lifecycle.

💡 **[Summary](2511.07865/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.07865)**

### Agent READMEs: An Empirical Study of Context Files for Agentic Coding

**Relevance:** This empirical study directly addresses the Human-Computer Interaction aspect of AI for Software Development by examining how developers instruct and provide context to agentic coding tools. The findings reveal a critical HCI gap: while developers provide functional context (e.g., build commands), they rarely specify non-functional requirements like security or performance. This highlights the need for better tooling and interaction design that guides developers to establish necessary guardrails, ensuring that AI-generated code is not just functional but also safe and robust, thus improving the reliability and trustworthiness of AI assistance.

💡 **[Summary](2511.12884/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.12884)**

### LoCoBench-Agent: An Interactive Benchmark for LLM Agents in Long-Context Software Engineering

**Relevance:** This paper introduces an interactive benchmark specifically designed for evaluating LLM agents in realistic, long-context software engineering tasks. It moves beyond single-turn evaluations to assess crucial HCI-relevant dimensions like multi-turn conversation, tool usage efficiency, and error recovery. This framework is vital for advancing usable AI in software development, as it provides metrics that measure how effectively agents handle complex, multi-step, and adaptive reasoning—qualities essential for reliable and collaborative AI assistants in real-world professional environments.

💡 **[Summary](2511.13998/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.13998)**

## AI Agents

### MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling

**Relevance:** MiroThinker explores 'interactive scaling' as a third dimension of agent performance improvement, where the agent is trained via reinforcement learning to handle deeper and more frequent agent-environment interactions. This is highly relevant to HCI as it focuses on designing agents that actively leverage environmental feedback and external tool calls to refine complex, multi-turn reasoning trajectories. This research provides a roadmap for building more capable and robust agents that can sustain complex collaboration with humans in research or problem-solving workflows.

💡 **[Summary](2511.11793/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.11793)**

### FreeAskWorld: An Interactive and Closed-Loop Simulator for Human-Centric Embodied AI

**Relevance:** This paper introduces a simulation framework designed for human-centric embodied AI, integrating LLMs for high-level planning and interaction grounded in theories of social cognition. It extends tasks like Vision-and-Language Navigation (VLN) into interaction-enriched settings where agents actively seek and interpret navigational guidance. This work is fundamental for HCI research in embodied agents, emphasizing interaction itself as a crucial information modality necessary for creating agents capable of naturalistic and socially aware collaboration with human users.

💡 **[Summary](2511.13524/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.13524)**

### WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance

**Relevance:** WebCoach addresses a major challenge in agent design: the lack of long-term robustness and learning across sessions. It introduces a model-agnostic framework that provides agents with persistent cross-session memory and a 'Coach' for injecting task-specific advice retrieved from past experiences. This self-evolving capability is key for HCI, ensuring agents become more reliable over time without retraining, improving user trust, and reducing the cognitive load required by humans to correct repetitive agent errors.

💡 **[Summary](2511.12997/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.12997)**

## LLM Evaluation Methods

### TopoPerception: A Shortcut-Free Evaluation of Global Visual Perception in Large Vision-Language Models

**Relevance:** This paper introduces TopoPerception, a novel benchmark leveraging topological properties for shortcut-free evaluation of Large Vision-Language Models (LVLMs). This evaluation method is crucial for robustness testing, as it exposes fundamental deficits in global visual perception that are often masked by local shortcuts in conventional benchmarks. Identifying such profound limitations, where models perform no better than random chance, is essential for guiding the development of reliable models and ensuring user trust in LVLMs deployed in high-stakes visual reasoning applications.

📄 **[Full paper](https://arxiv.org/pdf/2511.11831)**

### MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs

**Relevance:** MVI-Bench is the first comprehensive benchmark designed specifically to evaluate LVLM robustness against misleading visual inputs, addressing a critical gap in trustworthy AI development. It introduces a hierarchical taxonomy of misleading inputs (Concept, Attribute, Relationship) and the MVI-Sensitivity metric for granular assessment. This focus on robustness directly relates to HCI concerns around model reliability and safety, providing necessary tools to identify vulnerabilities and guide the creation of more dependable models that maintain user trust under adversarial visual conditions.

💡 **[Summary](2511.14159/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.14159)**

### Aligning Generative Music AI with Human Preferences: Methods and Challenges

**Relevance:** This paper advocates for the systematic use of preference alignment techniques to bridge the gap between computational optimization and subjective human musical appreciation. It discusses methods like MusicRL and preference optimization, which fundamentally rely on large-scale human-in-the-loop evaluation to capture nuanced preferences (e.g., temporal coherence and subjective quality). This work directly addresses the HCI goal of evaluation methods that prioritize user satisfaction and alignment with human values over mere computational fidelity, particularly in creative generative AI applications.

💡 **[Summary](2511.15038/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.15038)**

## Reinforcement Learning

### NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards

**Relevance:** This paper applies Direct Preference Optimization (DPO) to Vision-Language-Action (VLA) models, utilizing novel reward models that combine an action-conditioned world model (WM) with a deviation-from-ground-truth heuristic. This reward-guided post-training is crucial for improving agent reliability and generalization in embodied tasks. From an HCI perspective, defining preference rewards based on verifiable outcomes (like goal progress and deviation) is key to designing training environments where human guidance, even implicitly via collected preferences, leads to dependable and predictable agent behavior.

💡 **[Summary](2511.14659/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.14659)**

### Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning

**Relevance:** This foundational work systematically clarifies RL methodologies for LLM Agents by extending the Markov Decision Process (MDP) framework to define key agent components. It introduces Agent-R1, a modular framework for RL-based LLM Agents. This is highly relevant to advancing RL application in agents, which is the mechanism underpinning sophisticated agent behavior. Understanding and formalizing this framework is essential for future HCI research focused on how humans can effectively guide the learning process or interpret the complex policies developed by RL-trained agents.

💡 **[Summary](2511.14460/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.14460)**

### SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization

**Relevance:** SafeGRPO introduces a self-rewarded safety alignment framework that integrates rule-governed reward construction into Group Relative Policy Optimization (GRPO). This technique tackles compositional safety risks in MLLMs by enforcing structured, step-guided safety reasoning. For HCI, this is vital for maintaining safety and alignment with human values. By making the reasoning process interpretable and verifiable through rule-governed rewards, SafeGRPO addresses the need for designing RL systems that are transparent and trustworthy when deployed in sensitive, multimodal environments.

💡 **[Summary](2511.12982/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.12982)**

## Explainable AI

### Error-Driven Scene Editing for 3D Grounding in Large Language Models

**Relevance:** This paper proposes DEER-3D, an error-driven framework that uses 3D scene editing to generate precise visual counterfactuals, mitigating grounding biases in 3D-LLMs. By diagnosing predicate-level errors (e.g., attribute or spatial relation failures) and applying minimal edits to produce counterfactual supervision, the framework provides inherent explanations. This aligns directly with XAI goals, specifically counterfactual explanations, by showing users/developers exactly how small changes in the input (the 3D scene) would affect the model’s grounding output, helping to understand decision boundaries.

💡 **[Summary](2511.14086/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.14086)**

### REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding

**Relevance:** REVISOR introduces a framework for tool-augmented multimodal reflection, enabling MLLMs to construct introspective reasoning processes across textual and visual modalities. Crucially, the Dual Attribution Decoupled Reward (DADR) mechanism enforces causal alignment between the model's reasoning and the selected video evidence. This explicit alignment acts as a built-in explanation mechanism, promoting transparency by showing which visual segments informed the model's final decision, thereby advancing interpretability in complex, long-form video understanding tasks.

💡 **[Summary](2511.13026/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.13026)**

### SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization

**Relevance:** While also relevant to RL and Agents, SafeGRPO provides strong XAI implications. It enforces 'step-guided safety thinking' and uses rule-governed reward construction to achieve verifiable optimization. This structured reasoning trace acts as an explanation, offering transparency into how the MLLM processes and adheres to safety constraints during decision-making. This approach is superior to opaque safety filters, providing interpretable assurance that the model is aligned with human safety values through a transparent, rule-based reasoning process.

💡 **[Summary](2511.12982/)** 📄 **[Full paper](https://arxiv.org/pdf/2511.12982)**

