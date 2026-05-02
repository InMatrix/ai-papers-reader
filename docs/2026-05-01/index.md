---
layout: default
title: 2026-05-01
permalink: /2026-05-01/
---

# 2026-05-01

## AI for Software Development

### Toward Scalable Terminal Task Synthesis via Skill Graphs

**Relevance:** This paper focuses on terminal agents capable of autonomous command-line execution. It introduces SkillSynth, a framework that uses skill graphs to synthesize diverse and realistic terminal tasks. This is highly relevant to AI for software development as it provides a scalable way to train agents in shell environments, which are foundational for DevOps, system administration, and automated coding workflows. By grounding task synthesis in real-world workflow paths, it ensures that AI assistants can better handle the multi-step, complex sequences required in software engineering environments.

💡 **[Summary](2604.25727/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.25727)**

## AI Agents

### FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments

**Relevance:** FAMA addresses the reliability of autonomous agents by focusing on error accumulation in multi-turn tool-use scenarios. It identifies common failure trajectories and uses a meta-agent orchestration mechanism to inject targeted context before decision-making steps. This is a crucial advancement for AI agents, as it moves beyond simple prompting toward a structured architecture that anticipates and mitigates failures. For HCI, this framework provides insights into building more resilient and predictable interactive systems that can handle the cascading errors often found in real-world user-agent dialogues.

💡 **[Summary](2604.25135/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.25135)**

### Synthetic Computers at Scale for Long-Horizon Productivity Simulation

**Relevance:** This research introduces a methodology for creating thousands of 'synthetic computers' with realistic file systems and artifacts to simulate long-horizon productivity work. It uses agents to act as users, navigating files and coordinating with collaborators to complete complex professional objectives. This is highly relevant to HCI as it provides a foundational substrate for testing how agents interact with digital environments and user-specific contexts. It enables the scaling of agent training for diverse professional roles without requiring massive amounts of sensitive, real-world user data.

💡 **[Summary](2604.28181/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.28181)**

### AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark

**Relevance:** AutoGUI-v2 shifts the focus of agent evaluation from simple task completion to deep functionality understanding. It assesses whether agents can predict the 'digital world state' resulting from an interaction, requiring a mental model of interface dynamics. This is critical for creating agents that can navigate complex, unfamiliar GUIs. By evaluating region-level semantics and transition logic across multiple operating systems, this paper provides a robust framework for developing agents that truly comprehend the interactive affordances of software, a key goal in both AI and HCI.

💡 **[Summary](2604.24441/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.24441)**

## LLM Evaluation Methods

### Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models

**Relevance:** As the field increasingly relies on LLMs and VLMs to evaluate other models, this paper provides a critical reality check. It systematically identifies 'blind spots' in evaluator VLMs, such as their inability to detect object hallucinations or spatial reasoning errors. This research is vital for HCI and ML because it highlights the risks of automated benchmarking. It suggests that current evaluation methods may overestimate model progress, emphasizing the need for more robust, multi-modal evaluation paradigms that can reliably account for fine-grained compositional and factual errors.

💡 **[Summary](2604.21523/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.21523)**

### PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech

**Relevance:** Standard TTS evaluations often rely on intelligibility (WER) or general naturalness (MOS), which can miss subtle but critical phonological nuances. PSP introduces an interpretable, per-dimension benchmark specifically for Indic accents, measuring features like retroflex articulation and aspiration. This is a significant contribution to evaluation methodology as it moves toward 'perceptually grounded' metrics. From an HCI perspective, this allows researchers to quantify user-centric aspects of speech that affect trust and cultural resonance, providing a more granular understanding of how models perform across diverse linguistic groups.

💡 **[Summary](2604.25476/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.25476)**

### DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

**Relevance:** DV-World addresses the limitations of existing data visualization benchmarks by evaluating agents in native environments (like spreadsheets) and focusing on proactive intent alignment. It includes a user simulator that mimics ambiguous real-world requirements, forcing agents to clarify user intent. This is a major step forward for LLM evaluation as it integrates HCI principles of communication and collaboration into the assessment of agentic capability. The hybrid evaluation framework, combining numerical precision with semantic-visual rubrics, provides a more holistic view of an agent's utility in professional workflows.

💡 **[Summary](2604.25914/)** 📄 **[Full paper](https://arxiv.org/pdf/2604.25914)**

## Reinforcement Learning

### Step-Audio-R1.5 Technical Report

**Relevance:** This paper identifies the 'verifiable reward trap' in reinforcement learning, where models optimized solely for discrete, verifiable text labels lose their acoustic nuance and conversational feel. It proposes a shift from Reinforcement Learning with Verified Rewards (RLVR) to Reinforcement Learning from Human Feedback (RLHF) for audio reasoning. This is highly relevant to RL and HCI as it emphasizes that 'correctness' in human-agent interaction is not just about the final answer, but also about prosodic naturalness and emotional continuity, advocating for reward functions that better reflect human sensory experience.

📄 **[Full paper](https://arxiv.org/pdf/2604.25719)**

### V-GRPO: Online Reinforcement Learning for Denoising Generative Models Is Easier than You Think

**Relevance:** V-GRPO introduces an efficient method for aligning denoising generative models (like those used for image generation) with human preferences using online RL. By integrating ELBO-based surrogates with the Group Relative Policy Optimization (GRPO) algorithm, it overcomes the stability issues that previously hindered RL in visual generation. This research is significant for the RL community as it provides a scalable path for post-training alignment. For HCI, this enables the development of generative tools that are more responsive to specific user preferences and aesthetic constraints through iterative feedback loops.

📄 **[Full paper](https://arxiv.org/pdf/2604.23380)**

### Large Language Models Explore by Latent Distilling

**Relevance:** Exploration is a core challenge in RL, and this paper applies the concept to LLM decoding. It proposes Exploratory Sampling (ESamp), which uses a lightweight distiller to identify novel semantic patterns during generation based on prediction error. By biasing decoding toward less-explored latent states, it encourages semantic rather than just lexical diversity. This benefits RL research by providing a new mechanism for exploration in large state spaces and benefits HCI by improving the 'Pass@k' efficiency in reasoning tasks and breaking the trade-off between diversity and coherence in creative writing.

📄 **[Full paper](https://arxiv.org/pdf/2604.24927)**

## Explainable AI

### FASH-iCNN: Making Editorial Fashion Identity Inspectable Through Multimodal CNN Probing

**Relevance:** This paper applies XAI techniques to the cultural domain of fashion. It introduces FASH-iCNN, a system that identifies which fashion houses, eras, and color traditions are encoded in an AI's prediction. By probing visual channels, the researchers can explain which features (like texture vs. color) drive the model's classification. This is a unique application of interpretability that makes the 'aesthetic logic' of AI systems transparent. It allows users to see the cultural influences behind a prediction, addressing important HCI concerns regarding bias, transparency, and the 'black-box' nature of creative AI.

📄 **[Full paper](https://arxiv.org/pdf/2604.26186)**

### IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance

**Relevance:** IndustryAssetEQA addresses the lack of trust in AI assistants for safety-critical industrial settings. It combines episodic telemetry with knowledge graphs to provide explanations grounded in physical data with verifiable provenance. Critically, it supports counterfactual reasoning (e.g., 'What if this valve failed?'), a key component of XAI. By reducing expert-rated overclaims by 93%, it demonstrates how neurosymbolic approaches can make AI decision-making more transparent and reliable for human operators, directly benefiting the HCI goal of fostering appropriate trust in complex human-AI collaborative environments.

📄 **[Full paper](https://arxiv.org/pdf/2604.23446)**

### Towards Understanding the Robustness of Sparse Autoencoders

**Relevance:** Sparse Autoencoders (SAEs) are a leading tool for LLM interpretability. This paper explores their role in model robustness, showing that integrating SAEs into a model's residual stream can significantly reduce the success rate of optimization-based jailbreak attacks. It suggests a 'representational bottleneck hypothesis,' where sparse projections reshape the optimization geometry. This is relevant to XAI as it links interpretability (understanding internal representations) with security. For HCI, this provides a path toward building models that are not only more explainable but also more resilient to adversarial manipulation by end-users.

📄 **[Full paper](https://arxiv.org/pdf/2604.18756)**

