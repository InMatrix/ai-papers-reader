---
layout: default
title: 2026-03-20
permalink: /2026-03-20/
---

# 2026-03-20

## AI for Software Development

### AI Scientist via Synthetic Task Scaling

**Relevance:** This paper presents a pipeline for automatically generating machine learning challenges, including dataset proposal and code generation. From an HCI perspective, this research facilitates the development of AI agents capable of performing complex software engineering and research tasks. By automating the creation of high-quality synthetic tasks grounded in real-world data, the authors provide a framework for training models that can generate effective code and debug issues autonomously. This directly impacts the 'Code completion and generation' and 'Bug detection and fixing' sub-topics, offering a principled way to evolve AI-driven development tools that learn from experience.

💡 **[Summary](2603.17216/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.17216)**

### Efficient Reasoning with Balanced Thinking

**Relevance:** Efficient reasoning is critical for software development tools where latency and accuracy are paramount. ReBalance addresses the issues of overthinking and underthinking in Large Reasoning Models (LRMs) by using confidence as a dynamic indicator to prune redundant steps or promote exploration. This is highly relevant to AI-assisted coding, where models often generate overly verbose or insufficient logic. By optimizing reasoning trajectories across coding tasks and general question answering, this framework enhances the usability of LLMs in development environments, reducing cognitive load for developers who must review and verify AI-generated code snippets.

💡 **[Summary](2603.12372/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.12372)**

## AI Agents

### MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild

**Relevance:** MetaClaw introduces a continual meta-learning framework for LLM agents that allows them to evolve behavioral skills and optimize policies without disruptive downtime. This research is pivotal for HCI as it addresses the need for AI systems to adapt to shifting user needs and task distributions in real-time. By distilling knowledge from failure trajectories into reusable skills, MetaClaw creates agents that are more resilient and aligned with human values over long-term deployment. The system's ability to perform opportunistic optimization during user-inactive windows exemplifies a sophisticated approach to building autonomous, self-improving digital collaborators.

💡 **[Summary](2603.17187/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.17187)**

### AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents

**Relevance:** Memory is a fundamental component of effective AI agents. AdaMem proposes a multi-layered memory architecture (working, episodic, persona, and graph) that allows dialogue agents to maintain temporal and causal coherence over long interactions. From an HCI standpoint, this framework significantly improves user-centric understanding by moving beyond simple semantic similarity to include stable user traits and relation-aware connections. This enables agents to provide more personalized assistance and handle multi-step reasoning tasks more effectively, directly addressing the challenge of maintaining context and trust in human-agent partnerships during long-horizon digital interactions.

💡 **[Summary](2603.16496/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.16496)**

### Fanar-Sadiq: A Multi-Agent Architecture for Grounded Islamic QA

**Relevance:** Fanar-Sadiq demonstrates a specialized multi-agent architecture designed to handle diverse and complex queries in a sensitive domain. By using intent-aware routing and specialized modules for retrieval, citation verification, and deterministic calculations, it exemplifies how agents can use reasoning and tools to maintain high accuracy and alignment with specific cultural or legal values. This paper is a prime example of designing agents that can break complex, rule-constrained tasks into manageable steps while providing transparent 'verification traces,' which is essential for user trust and the practical deployment of AI in specialized social contexts.

💡 **[Summary](2603.08501/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.08501)**

## LLM Evaluation Methods

### Alignment Makes Language Models Normative, Not Descriptive

**Relevance:** This paper provides a critical HCI-focused evaluation of post-training alignment. It reveals a fundamental trade-off: while alignment improves a model's adherence to normative human preferences, it significantly degrades its ability to descriptively model and predict actual human behavior in complex, multi-round strategic interactions. By comparing 120 model pairs across 10,000 human decisions, the authors show that aligned models often fail to capture the descriptive dynamics of human reciprocity and adaptation. This research is essential for evaluating LLMs as proxies for human behavior and understanding how alignment affects user satisfaction and the realism of social simulations.

💡 **[Summary](2603.17218/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.17218)**

### BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs

**Relevance:** As LLMs increasingly use persistent memory to store user data, evaluating how they apply these preferences across different social and institutional contexts becomes vital. BenchPreS introduces metrics like Misapplication Rate to assess whether models inappropriately enforce personal preferences in settings governed by broader norms. This evaluation method is deeply rooted in HCI, as it considers how model behavior aligns with complex social expectations and institutional rules. The finding that frontier models struggle with context-sensitive preference application highlights a critical area for improving trust and the social intelligence of personalized AI systems.

💡 **[Summary](2603.16557/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.16557)**

### FINER: MLLMs Hallucinate under Fine-grained Negative Queries

**Relevance:** Evaluating the robustness of Multimodal LLMs (MLLMs) is crucial for their safe interaction with the physical world. The FINER benchmark addresses a gap in existing evaluations by focusing on fine-grained hallucinations where models fail to distinguish between present and absent elements in complex images. This work is relevant to HCI because it quantifies the reliability of models in high-detail tasks (e.g., multi-object or multi-attribute relations). By proposing 'FINER-Tuning' via Direct Preference Optimization, the authors show how evaluation-driven insights can directly improve model performance and reduce the cognitive load users face when verifying AI-generated visual descriptions.

💡 **[Summary](2603.17662/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.17662)**

## Reinforcement Learning

### Efficient Exploration at Scale

**Relevance:** This research focuses on improving the data efficiency of Reinforcement Learning from Human Feedback (RLHF), a core technique for aligning LLMs with human values. By introducing information-directed exploration and epistemic neural networks to model reward uncertainty, the authors achieve a 10x to 1,000x gain in data efficiency. This is highly significant for HCI, as it reduces the burden on human evaluators and allows for more rapid, iterative refinement of models based on human choice data. The algorithm's ability to match high-performance benchmarks with fewer labels makes RL-based alignment more accessible and scalable for diverse human-centric applications.

💡 **[Summary](2603.17378/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.17378)**

### ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning

**Relevance:** ARISE utilizes hierarchical reinforcement learning to co-evolve reasoning capabilities and a library of reusable skills. By employing a 'Skills Manager' and a 'Worker' policy, the framework enables agents to summarize successful solution traces and retrieve relevant strategies for future tasks. This approach to RL is particularly relevant for complex problem-solving domains like mathematics. From an HCI perspective, it illustrates how agents can learn to organize their own 'experience' and strategies, leading to more robust and interpretable problem-solving behaviors that can better generalize to out-of-distribution tasks compared to standard RL algorithms.

💡 **[Summary](2603.16060/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.16060)**

### From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

**Relevance:** DICE-RL demonstrates how reinforcement learning can be used as a 'distribution contraction' operator to refine pretrained generative robot policies. By amplifying high-success behaviors from online feedback, the framework enables the mastery of complex manipulation skills from high-dimensional inputs. This is relevant to the design of novel agent-environment interactions, showing how RL can bridge the gap between broad behavioral priors and high-performing, task-specific expertise. The focus on sample efficiency and stability in real-world robotic platforms is critical for creating agents that can safely and effectively interact with and learn from their physical environments.

💡 **[Summary](2603.10263/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.10263)**

## Explainable AI

### I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning

**Relevance:** This paper introduces Latent Posterior Factors (LPF), a framework that bridges unstructured data processing with structured probabilistic reasoning. By transforming VAE latent posteriors into soft likelihood factors for Sum-Product Networks, it enables calibrated uncertainty estimates in high-stakes decision-making. This is a core XAI contribution, as it allows models to quantify 'what they don't know' across contradictory evidence sources. The ability to provide exact epistemic-aleatoric uncertainty decomposition offers users a clear understanding of why a model is uncertain, enhancing trust and interpretability in domains like medical diagnosis or financial assessment.

💡 **[Summary](2603.15670/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.15670)**

### Video-CoE: Reinforcing Video Event Prediction via Chain of Events

**Relevance:** Video event prediction often suffers from a lack of logical transparency regarding future states. Video-CoE addresses this by constructing 'temporal event chains' that implicitly enforce logical reasoning within Multimodal LLMs. This Chain-of-Events paradigm makes the model's temporal modeling more interpretable by incentivizing it to focus on specific visual content and logical connections. For HCI, this means users can better understand the rationale behind an AI's prediction of future events, as the model is trained to follow a structured reasoning path rather than relying on superficial visual cues or 'black-box' predictions.

💡 **[Summary](2603.14935/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.14935)**

### HistoAtlas: A Pan-Cancer Morphology Atlas Linking Histomics to Molecular Programs and Clinical Outcomes

**Relevance:** HistoAtlas exemplifies XAI in the medical domain by extracting 38 interpretable histomic features from pathology slides. Unlike opaque deep learning models, this atlas links morphological features to survival and gene expression through covariate-adjusted, statistically calibrated associations. Every result is 'spatially traceable' to tissue compartments and individual cells, allowing clinicians to visually verify the AI's findings. By providing an interactive web atlas and interpretable biomarkers, HistoAtlas demonstrates how AI can augment human expertise in cancer research and diagnosis while maintaining high levels of transparency and biological grounding.

💡 **[Summary](2603.16587/)** 📄 **[Full paper](https://arxiv.org/pdf/2603.16587)**

