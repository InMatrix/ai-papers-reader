---
layout: default
title: 2026-02-20
permalink: /2026-02-20/
---

# 2026-02-20

## AI for Software Development

### CADEvolve: Creating Realistic CAD via Program Evolution

**Relevance:** This paper addresses the automation of Computer-Aided Design (CAD) by evolving executable code (CadQuery scripts). From an HCI perspective, this facilitates the creation of complex, editable 3D models from simple primitives or images. By generating parametric generators rather than static meshes, it supports professional engineering workflows where design intent and editability are paramount. The use of Vision-Language Models (VLMs) to guide code edits mirrors how a human designer might iteratively refine a script, providing a bridge between high-level visual goals and low-level geometric programming.

💡 **[Summary](2602.16317/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.16317)**

### TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models

**Relevance:** TAROT focuses on improving the functional correctness and robustness of AI-generated code through Reinforcement Fine-Tuning (RFT). It introduces a curriculum-based approach that adapts to the model's inherent capabilities, using tiered test suites (basic to edge cases). This is highly relevant to HCI as it aims to reduce the 'vibe coding' uncertainty, where code looks correct but fails on edge cases. By systematically improving code reliability, it enhances the developer's trust and reduces the cognitive load required for manual debugging of AI-suggested snippets.

💡 **[Summary](2602.15449/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.15449)**

### GLM-5: from Vibe Coding to Agentic Engineering

**Relevance:** GLM-5 represents a shift from simple code completion ('vibe coding') to 'agentic engineering,' where models handle end-to-end software challenges. It utilizes asynchronous reinforcement learning to improve long-horizon interactions and complex reasoning. For HCI, this signifies a transition in the user-AI relationship: the AI moves from being a simple autocomplete tool to a collaborative agent capable of managing entire software lifecycles. This has profound implications for how developers oversee autonomous systems and the interfaces required to monitor 'agentic' engineering tasks.

💡 **[Summary](2602.15763/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.15763)**

## AI Agents

### Learning Personalized Agents from Human Feedback

**Relevance:** This paper introduces the PAHF framework, which is central to HCI as it focuses on aligning agents with the unique, evolving preferences of individual users. By using a three-step loop—clarification, preference retrieval from memory, and feedback integration—it addresses the core HCI challenge of building trust and reducing friction in human-agent interaction. The emphasis on 'continual personalization' and handling 'persona shifts' ensures that the agent remains a useful assistant as user needs change over time, moving beyond static, one-size-fits-all AI behavior.

💡 **[Summary](2602.16173/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.16173)**

### Towards a Science of AI Agent Reliability

**Relevance:** As AI agents move from benchmarks to real-world deployment, reliability becomes a critical HCI concern. This paper proposes twelve metrics across consistency, robustness, predictability, and safety to evaluate agents beyond simple accuracy. For HCI researchers, these metrics provide a vocabulary to describe why users might lose trust in an agent (e.g., due to inconsistent behavior or unpredictable failures). By identifying these operational flaws, the work helps in designing more resilient systems that align better with human expectations of dependable software.

💡 **[Summary](2602.16666/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.16666)**

### Knowing Isn't Understanding: Re-grounding Generative Proactivity with Epistemic and Behavioral Insight

**Relevance:** This research explores 'generative proactivity,' where agents act without explicit user prompts to address 'unknown unknowns.' This is a classic HCI problem: how can an agent be helpful without being intrusive or overwhelming? The paper argues for 'behavioral grounding'—principled constraints on when and how an agent should intervene. This framework is essential for designing agents that foster meaningful partnerships rather than just automating tasks, ensuring that proactive AI behaviors are epistemically sound and respect user attention and autonomy.

💡 **[Summary](2602.15259/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.15259)**

## LLM Evaluation Methods

### HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam

**Relevance:** Evaluating frontier models requires high-quality benchmarks. This paper addresses 'annotation noise' in complex evaluations by using a two-stage expert-led verification and repair workflow. From an HCI perspective, this highlights the necessity of human-in-the-loop processes to ensure that the 'ground truth' used to judge AI is actually correct. By providing a fine-grained error taxonomy and a certified version of a popular benchmark, it enables more faithful measurements of model capabilities, which is vital for researchers designing user-facing AI systems.

💡 **[Summary](2602.13964/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.13964)**

### HybridRAG-Bench: A Benchmarking Framework for Multi-Hop Inference over Hybrid Knowledge

**Relevance:** This paper introduces a framework to distinguish between 'parametric recall' (memory) and 'genuine retrieval and reasoning' (logic). In HCI, understanding whether a model is hallucinating from its training data or correctly using provided context is crucial for user trust. HybridRAG-Bench uses recent scientific literature to create a 'contamination-aware' evaluation. This method helps HCI practitioners determine if an AI assistant is truly capable of reasoning over new, user-provided documents or if it is merely reciting potentially outdated information from its pre-training phase.

💡 **[Summary](2602.10210/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.10210)**

### Learning Situated Awareness in the Real World

**Relevance:** SAW-Bench evaluates 'situated awareness'—the ability of a model to reason from an observer-centric viewpoint (e.g., through smart glasses). This is highly relevant to egocentric HCI and augmented reality. The paper identifies a significant gap between human and model performance in spatial reasoning relative to the user's pose and motion. For HCI, this benchmark provides a way to measure how well AI can understand the user's immediate physical context, which is essential for building proactive, context-aware wearable assistants.

💡 **[Summary](2602.16682/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.16682)**

## Reinforcement Learning

### Multi-agent cooperation through in-context co-player inference

**Relevance:** This paper explores how sequence models can learn cooperative behaviors in multi-agent RL settings without hardcoded rules. By training against diverse co-players, agents develop 'in-context' best-response strategies. This is relevant to HCI as it models how AI might adapt to human 'co-players' in collaborative environments. Understanding how agents evolve to avoid exploitation and move toward mutual cooperation provides insights into designing AI that can naturally and safely collaborate with humans in shared digital or physical spaces.

📄 **[Full paper](https://arxiv.org/pdf/2602.16301)**

### STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens

**Relevance:** STAPO addresses the instability of RL fine-tuning for LLMs, specifically the issue of 'spurious tokens' that cause performance collapse. While technical, this has direct HCI implications: more stable RL training leads to more reliable and predictable model behavior. By preventing late-stage performance degradation, STAPO ensures that the reasoning capabilities of the model remain consistent. This reliability is fundamental for user satisfaction and the long-term adoption of RL-tuned agents in sensitive domains like mathematics or logic.

📄 **[Full paper](https://arxiv.org/pdf/2602.15620)**

### Learning to Configure Agentic AI Systems

**Relevance:** This work uses RL to learn a policy (ARC) that dynamically configures an agent's workflow, tools, and token budgets based on the specific query. This 'per-query' adaptation is an HCI-centric improvement over 'one size fits all' systems. It optimizes the balance between performance and cost (latency/tokens), directly impacting the user experience. By learning when to use 'expensive' reasoning versus 'cheap' direct answers, the system provides a more responsive and efficient interface for the user.

💡 **[Summary](2602.11574/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.11574)**

## Explainable AI

### Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

**Relevance:** Sparse Autoencoders (SAEs) are a leading method for 'mechanistic interpretability'—explaining the internal features of neural networks. This paper provides a critical 'sanity check,' revealing that SAEs might not be as reliable at decomposing internal mechanisms as previously thought. For HCI, this is a cautionary tale: it emphasizes that the 'explanations' provided by AI interpretability tools must themselves be rigorously validated before they are used to build user-facing transparency dashboards or safety audits.

📄 **[Full paper](https://arxiv.org/pdf/2602.14111)**

### STATe-of-Thoughts: Structured Action Templates for Tree-of-Thoughts

**Relevance:** STATe improves the explainability of 'inference-time-compute' methods like Tree-of-Thoughts. It replaces stochastic sampling with discrete, interpretable 'textual interventions' (high-level reasoning choices). This allows the system to not only produce better answers but also provide a clear, traceable path of the 'actions' taken during reasoning. In HCI, this structure can be used to generate diverse response options and provide users with an understandable rationale for how the AI arrived at a specific conclusion.

💡 **[Summary](2602.14265/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.14265)**

### Visual Persuasion: What Influences Decisions of Vision-Language Models?

**Relevance:** This paper presents a framework to infer the 'latent visual utility' of Vision-Language Models—essentially explaining what visual features (lighting, composition, background) 'persuade' a model to make a certain choice. This is a novel form of XAI that is deeply relevant to HCI and safety. By surfacing these visual vulnerabilities, researchers can understand and explain how AI agents might be manipulated by adversarial images or biased marketing, supporting more proactive auditing of image-based decision systems.

💡 **[Summary](2602.15278/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.15278)**

