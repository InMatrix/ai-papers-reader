---
layout: default
title: 2025-12-12
permalink: /2025-12-12/
---

# 2025-12-12

## AI for Software Development

### DeepCode: Open Agentic Coding

**Relevance:** This paper is highly relevant as it introduces DeepCode, a fully autonomous framework designed to act as a 'code engineer' capable of high-fidelity document-to-codebase synthesis. It addresses a core challenge in generative AI for software development: overcoming context bottlenecks to transform high-level specifications (like scientific papers) into production-grade implementations. DeepCode uses principled information-flow management, including blueprint distillation, structured indexing, and closed-loop error correction. This work fundamentally advances the use of AI in complex software engineering tasks, aiming to accelerate research reproduction and discovery while reducing manual developer effort.

💡 **[Summary](2512.07921/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.07921)**

## AI Agents

### Towards a Science of Scaling Agent Systems

**Relevance:** This research directly investigates the performance and scaling principles of LLM-based agent systems, which are defined by their ability to reason, plan, and act. It systematically evaluates five canonical agent architectures (Single, Independent, Centralized, Decentralized, Hybrid) across diverse benchmarks. By deriving quantitative scaling principles based on coordination metrics like error amplification and overhead, this work provides crucial, principled design choices for practitioners. Understanding these trade-offs is fundamental for building reliable, efficient, and scalable agents that can effectively accomplish complex, user-defined goals.

💡 **[Summary](2512.08296/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.08296)**

### Reinventing Clinical Dialogue: Agentic Paradigms for LLM Enabled Healthcare Communication

**Relevance:** This survey provides a first-principles analysis of the shift towards 'agentic autonomy' in medical AI, a high-stakes domain requiring reliability and alignment. It introduces a novel taxonomy for clinical agents based on knowledge sources and agency objectives, covering strategic planning, memory management, and collaboration. The framework facilitates a systematic analysis of the intrinsic trade-offs between creativity and reliability. This is highly relevant to HCI, as it focuses on the cognitive architecture required to balance agent autonomy with safety and alignment with human values in sensitive applications.

💡 **[Summary](2512.01453/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.01453)**

### EcomBench: Towards Holistic Evaluation of Foundation Agents in E-commerce

**Relevance:** EcomBench introduces a benchmark for evaluating foundation agents in the complex, real-world e-commerce domain. This aligns with the HCI goal of assessing agent performance under genuine user demands, moving beyond artificial scenarios. It evaluates key capabilities such as multi-step reasoning, deep information retrieval, and cross-source knowledge integration. By grounding evaluation in a dynamic, practical setting, this work provides a rigorous testbed for measuring the utility and robustness of agents, which is essential for ensuring user satisfaction and trust in real-world deployments.

💡 **[Summary](2512.08868/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.08868)**

## LLM Evaluation Methods

### Same Content, Different Answers: Cross-Modal Inconsistency in MLLMs

**Relevance:** This paper introduces the REST and REST+ benchmarks to systematically evaluate cross-modal inconsistency in MLLMs. The finding that state-of-the-art models fail robustness tests—providing different answers to semantically equivalent inputs across image and text modalities—is a critical evaluation concern. This inconsistency fundamentally undermines user trust and model reliability. The research provides a mechanistic interpretation of the modality gap, offering vital insights for developing more robust models, which is crucial from an HCI perspective focused on stable and predictable AI behavior.

💡 **[Summary](2512.08923/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.08923)**

### See, Hear, and Understand: Benchmarking Audiovisual Human Speech Understanding in Multimodal Large Language Models

**Relevance:** This work introduces AV-SpeakerBench, a rigorous benchmark focused on fine-grained audiovisual reasoning about human speech. It moves beyond coarse video evaluation by adopting a speaker-centric formulation and designing fusion-grounded questions that embed cross-modal dependencies (aligning who, what, and when). This detailed evaluation method is essential for understanding the limitations of MLLMs in complex human interaction and communication scenarios, ensuring that future multimodal systems can reliably process and respond to nuanced human inputs, thereby reducing user cognitive load and improving interaction quality.

📄 **[Full paper](https://arxiv.org/pdf/2512.02231)**

### LYNX: Learning Dynamic Exits for Confidence-Controlled Reasoning

**Relevance:** LYNX introduces an online early-exit mechanism that uses a model's hidden states to make confidence-controlled stopping decisions during Chain-of-Thought (CoT) reasoning. While primarily focused on efficiency, this method provides explicit, user-tunable confidence guarantees for when a model stops reasoning. Providing this control and transparency over the 'overthinking' process directly impacts user trust and helps manage cognitive load by reducing unnecessary output length, linking efficiency improvements to crucial HCI concerns regarding model reliability and interpretability.

💡 **[Summary](2512.05325/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.05325)**

## Reinforcement Learning

### TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion Models

**Relevance:** This paper introduces TreeGRPO, a novel RL framework that significantly improves training efficiency for generative models by restructuring the denoising process as a search tree. By strategically branching and reusing common prefixes, TreeGRPO achieves superior sample efficiency and enables fine-grained credit assignment. These methodological advances in policy optimization (a variant of GRPO) are critical for scaling RL to complex, high-dimensional tasks, facilitating faster iteration cycles when aligning agents with human preferences or feedback, which is key for effective human guidance in RL systems.

💡 **[Summary](2512.08153/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.08153)**

### MIND-V: Hierarchical Video Generation for Long-Horizon Robotic Manipulation with RL-based Physical Alignment

**Relevance:** MIND-V is a hierarchical framework that uses Reinforcement Learning (GRPO post-training) guided by a Physical Foresight Coherence (PFC) reward to ensure synthesized long-horizon robotic manipulation videos are physically plausible. This application of RL focuses on learning complex, temporally coherent behaviors and aligning them with physical laws. This research is relevant to RL environment design and human-agent collaboration, as physical plausibility and long-horizon coherence are essential for designing embodied agents that humans can intuitively guide, interpret, and trust in real-world scenarios.

💡 **[Summary](2512.06628/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.06628)**

### HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models

**Relevance:** This work addresses temporal coherence in Vision-Language-Action (VLA) models, which are often trained using RL or imitation learning for robotics. It leverages motion to enable bidirectional temporal reasoning (hindsight and foresight), facilitating a 'think-while-acting' paradigm crucial for long-horizon manipulation. This focus on internal planning and temporal context directly relates to the HCI challenge of interpreting agent behaviors and guiding agent learning. By improving the agent's ability to maintain coherence, it makes the agent's decision-making more predictable and understandable to human collaborators.

💡 **[Summary](2512.09928/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.09928)**

## Explainable AI

### Pay Less Attention to Function Words for Free Robustness of Vision-Language Models

**Relevance:** This research analyzes and manipulates attention mechanisms in VLMs to improve robustness against adversarial attacks. By proposing Function-word De-Attention (FDA), the authors reveal the vulnerability caused by function words and mitigate it. This constitutes a form of attention visualization and analysis, which is a key XAI technique. By making the model's focus more transparent and demonstrating how feature importance (or lack thereof) affects output, the method enhances interpretability and model reliability, critical for user trust.

💡 **[Summary](2512.07222/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.07222)**

### UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving

**Relevance:** The UniUGP framework for autonomous driving is designed to synergize reasoning and planning by producing 'interpretable chain-of-thought reasoning' alongside physically consistent trajectories. Chain-of-Thought (CoT) is one of the most effective methods in XAI for LLMs, offering step-by-step transparency into the model's reasoning process. In a high-stakes application like autonomous driving, providing this detailed, interpretable rationale is essential for building safety, accountability, and user trust in the AI's complex decision-making.

💡 **[Summary](2512.09864/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.09864)**

