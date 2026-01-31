---
layout: default
title: 2025-12-26
permalink: /2025-12-26/
---

# 2025-12-26

## AI for Software Development

### SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

**Relevance:** Directly addresses the gap between current AI coding agents and real-world software engineering. By introducing SWE-EVO, a benchmark focusing on long-horizon, multi-file software evolution, the paper highlights that agents struggle with sustained planning and coordinated changes. This is critical for HCI, as it defines the limitations of current developer tools and sets a new standard for evaluating agent usability and reliability in complex, real-world development workflows.

📄 **[Full paper](https://arxiv.org/pdf/2512.18470)**

### SecureCode v2.0: A Production-Grade Dataset for Training Security-Aware Code Generation Models

**Relevance:** This work is highly relevant to HCI because it tackles the critical issue of security and trust in AI-generated code. By providing a production-grade dataset grounded in real CVEs and including comprehensive operational security guidance, it enables the training of security-aware models. This directly impacts the safety and reliability of AI assistants used by developers, ensuring that these tools are trustworthy and minimize the introduction of vulnerabilities into production systems.

💡 **[Summary](2512.18542/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.18542)**

### C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling

**Relevance:** C2LLM advances the fundamental capability of code retrieval, which is the backbone for many AI software development tools like code completion and documentation generation. The method uses an adaptive pooling module to generate superior code embeddings, improving the efficiency and accuracy of retrieval tasks. Better code embeddings lead to more relevant and context-aware suggestions from AI assistants, directly enhancing the developer experience and productivity.

💡 **[Summary](2512.21332/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.21332)**

## AI Agents

### MemEvolve: Meta-Evolution of Agent Memory Systems

**Relevance:** This paper introduces a meta-evolutionary framework that allows AI agents to jointly refine their memory architecture alongside their experiential knowledge. From an HCI perspective, this is crucial for designing adaptive agents that can learn continuously and tailor their learning strategies to diverse tasks. Evolving the memory system itself addresses the staticity limitation of previous agents, leading to more robust, generalizable, and ultimately more dependable human-agent collaborations.

💡 **[Summary](2512.18746/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.18746)**

### INTELLECT-3: Technical Report

**Relevance:** INTELLECT-3 is relevant for AI agents because it details the large-scale RL infrastructure and methodology (prime-rl) used to train state-of-the-art Mixture-of-Experts models optimized for agentic tasks. The infrastructure specifically supports multi-turn interactions and tool use, which are defining characteristics of sophisticated agents. This work provides the architectural foundation and training recipe necessary to build highly capable and efficient agents for complex user goals.

💡 **[Summary](2512.16144/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.16144)**

### Active Intelligence in Video Avatars via Closed-loop World Modeling

**Relevance:** This paper is highly relevant as it addresses the transition of video avatars from passive animation to active, goal-oriented agents. The ORCA framework, using a closed-loop Observe-Think-Act-Reflect (OTAR) cycle and an Internal World Model, enables autonomous planning and robust state tracking. This design ensures that avatars maintain behavioral coherence and pursue long-term goals adaptively, crucial for developing believable and useful interactive agents.

💡 **[Summary](2512.20615/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.20615)**

## LLM Evaluation Methods

### LLM Swiss Round: Aggregating Multi-Benchmark Performance via Competitive Swiss-System Dynamics

**Relevance:** This paper introduces a novel, competitive ranking system for LLMs that moves beyond fragmented metrics. The Competitive Swiss-System Dynamics framework aggregates performance dynamically and includes Failure Sensitivity Analysis. This provides a risk-informed and nuanced ranking, which is highly valuable for HCI researchers and practitioners selecting LLMs, as it captures a model's robustness and competitive fitness across diverse user needs and tasks.

💡 **[Summary](2512.21010/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.21010)**

### Beyond Memorization: A Multi-Modal Ordinal Regression Benchmark to Expose Popularity Bias in Vision-Language Models

**Relevance:** This work directly addresses the critical HCI concern of trust and bias in VLMs. By introducing a benchmark to expose popularity bias—where models rely on memorization rather than generalizable understanding—it highlights a major flaw in reasoning capabilities. The use of quantitative ordinal regression and popularity-aware metrics provides a systematic way to evaluate fairness and generalization, guiding the development of more reliable and trustworthy multimodal systems.

💡 **[Summary](2512.21337/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.21337)**

### Multi-LLM Thematic Analysis with Dual Reliability Metrics: Combining Cohen's Kappa and Semantic Similarity for Qualitative Research Validation

**Relevance:** This paper is relevant for validating the use of LLMs in qualitative research, a cornerstone of HCI methods. It proposes a robust validation framework using dual reliability metrics (Cohen's Kappa and semantic similarity) across multi-run ensembles. This approach establishes transparent methodological foundations for reliable AI-assisted qualitative analysis, helping researchers trust and integrate LLMs into complex data coding workflows.

💡 **[Summary](2512.20352/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.20352)**

## Reinforcement Learning

### Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies

**Relevance:** This paper offers deep interpretability into the RL process by decomposing the LLM policy into internal layer contributions. The proposed BuPO paradigm optimizes these internal policies directly. This is crucial for HCI as understanding *how* an agent learns and reasons at a foundational level allows researchers to better diagnose failures, guide learning effectively, and design systems where the user can interpret and trust the agent's internal decision-making structure.

💡 **[Summary](2512.19673/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.19673)**

### Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents

**Relevance:** This work applies RL to enhance temporal reasoning and memory selection in conversational agents, a key challenge for usable LLM systems. By employing a multi-level reward function that explicitly optimizes for temporal consistency and evidence grounding, the framework learns robust policies against noise in long histories. This focus on structured, time-aware decision-making directly benefits the reliability and coherence of agents, improving user experience in multi-session interactions.

💡 **[Summary](2512.20092/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.20092)**

### Reinforcement Learning for Self-Improving Agent with Skill Library

**Relevance:** SAGE proposes an RL framework to systematically integrate learned skills into policy optimization, focusing on continuous improvement and adaptation. The use of a Skill-integrated Reward provides a dense signal that complements outcome rewards, leading to greater efficiency and accuracy. For HCI, this demonstrates how RL can facilitate the design of agents that are adaptable, learnable, and can transparently manage their increasing capabilities (skill library).

💡 **[Summary](2512.17102/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.17102)**

## Explainable AI

### Brain-Grounded Axes for Reading and Steering LLM States

**Relevance:** This paper offers a novel method for XAI by grounding interpretability axes in human neurophysiology (MEG). By mapping LLM hidden states to these brain-derived axes, researchers gain interpretable and controllable handles for steering model behavior (e.g., lexical frequency). This external grounding provides a robust, human-centric coordinate system for LLM transparency, moving beyond purely textual explanations to enhance trust and cognitive understanding.

💡 **[Summary](2512.19399/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.19399)**

### FaithLens: Detecting and Explaining Faithfulness Hallucination

**Relevance:** FaithLens directly addresses the need for trustworthy AI by focusing on faithfulness hallucination detection and explanation generation. It fine-tunes a model using rule-based RL to optimize both prediction correctness and explanation quality. This cost-efficient approach provides users with immediate, high-quality explanations for potentially unreliable outputs, which is fundamental for maintaining user trust and enabling effective human verification in critical applications like RAG and summarization.

💡 **[Summary](2512.20182/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.20182)**

### Reasoning Palette: Modulating Reasoning via Latent Contextualization for Controllable Exploration for (V)LMs

**Relevance:** This framework introduces a stochastic latent variable to modulate LLM internal planning, enabling controllable and interpretable exploration of reasoning strategies. The latent context is decoded into prefixes that guide the model's internal trajectory, allowing developers to shape the style and structure of the response. This is a powerful XAI tool, providing insight into the model's high-level strategy and offering users fine-grained control over the reasoning process.

💡 **[Summary](2512.17206/)** 📄 **[Full paper](https://arxiv.org/pdf/2512.17206)**

