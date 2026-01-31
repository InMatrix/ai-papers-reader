---
layout: default
title: 2024-07-05
permalink: /2024-07-05/
---

# 2024-07-05

## AI for Software Development

### Agentless: Demystifying LLM-based Software Engineering Agents

**Relevance:** This paper critically evaluates complex LLM-based software engineering agents, which often introduce opacity and high cognitive load for developers. From an HCI perspective, complex agent architectures can hinder trust and debugging. The paper demonstrates that a simpler, interpretable two-phase approach (localization and repair) achieves better performance and lower cost on the SWE-bench Lite benchmark. This finding has significant implications for HCI in AI4SD: it suggests that designing efficient, trustworthy, and less complex AI developer tools that focus on interpretability over maximal autonomy may lead to better adoption and collaboration between AI and human developers.

💡 **[Summary](2407.01489/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.01489)**

## AI Agents

### ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning

**Relevance:** This framework is crucial for HCI in embodied AI because it allows non-experts to program robots using natural language via a chat interface. The system integrates structured reasoning (like behavior trees) and supports LLM reflection based on human and environmental feedback. These features directly address the HCI challenge of agent transparency and supervision. By making the agent’s internal logic structured and enabling explicit feedback loops, the framework facilitates intuitive human control and ensures that the agent's actions are interpretable and aligned with user intent.

💡 **[Summary](2406.19741/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.19741)**

### OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents

**Relevance:** OmniJARVIS focuses on creating robust instruction-following agents in complex environments (Minecraft) by unifying vision, language, and action into a single token stream. This unified approach enables the agent to generate explicit Chain-of-Thoughts alongside its actions. For HCI, the ability to generate transparent reasoning and planning traces is essential for building trust. When agents fail or encounter novel situations, these articulated thought processes allow human supervisors to quickly diagnose issues and provide targeted guidance, fostering effective human-agent collaboration.

💡 **[Summary](2407.00114/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.00114)**

### MIRAI: Evaluating LLM Agents for Event Forecasting

**Relevance:** MIRAI introduces a novel, rigorous benchmark for evaluating LLM agents in high-stakes, long-horizon tasks like international event forecasting. The benchmark emphasizes autonomous tool use (accessing structured databases) and complex reasoning. From an HCI viewpoint, evaluating agent reliability and trustworthiness in consequential domains is paramount. MIRAI helps establish a framework to assess agent competence in integrating information and using tools, which is necessary for defining safe human-agent interfaces and ensuring that human decision-makers can rely on the agent's predictions.

💡 **[Summary](2407.01231/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.01231)**

## LLM Evaluation Methods

### MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation

**Relevance:** This paper addresses the critical issue of systematic bias in multimodal LLM (LMM) benchmarks, where visual models can achieve high scores based purely on linguistic or knowledge cues, undermining evaluation trustworthiness. MMEvalPro introduces a methodology to avoid Type-I errors, ensuring that performance gains truly reflect visual perception capabilities. For HCI, trustworthy evaluation is fundamental; if benchmarks are flawed, researchers risk designing interaction paradigms based on falsely attributed capabilities, leading to poor user experiences and reduced trust in LMMs used in real-world applications.

💡 **[Summary](2407.00468/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.00468)**

### Summary of a Haystack: A Challenge to Long-Context LLMs and RAG Systems

**Relevance:** The SummHay benchmark challenges long-context models on complex summarization and precise citation tasks, moving beyond simple 'needle-in-a-haystack' retrieval. This is highly relevant to HCI because reliability and the absence of position bias are critical for user trust in knowledge-intensive applications. By focusing on measurable metrics like Coverage and Citation, SummHay provides a robust way to evaluate whether LLMs can synthesize information accurately and traceably, which is essential for reducing the cognitive load required for users to verify the AI's complex outputs.

💡 **[Summary](2407.01370/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.01370)**

### Revealing Fine-Grained Values and Opinions in Large Language Models

**Relevance:** This research analyzes LLM biases and latent values using a large dataset generated via extensive prompt variations. The finding that demographic features and prompt phrasing significantly alter moral and political stances is crucial for ethical HCI. It underscores the fragility of current alignment methods and the potential for unintended bias leakage. HCI practitioners must leverage this understanding to design interaction systems that are robust to prompting variability, ensuring that LLMs provide fair, consistent, and ethically aligned responses across diverse user interactions.

💡 **[Summary](2406.19238/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.19238)**

## Reinforcement Learning

### Iterative Nash Policy Optimization: Aligning LLMs with General Preferences via No-Regret Learning

**Relevance:** This paper proposes INPO, a novel algorithm for Reinforcement Learning from Human Feedback (RLHF) based on game theory, moving beyond the restrictive Bradley-Terry model. Since RLHF is the primary method for aligning LLMs with human values and preferences, improvements in its underlying mechanics directly benefit HCI. INPO's ability to align models with more general preferences ensures that resulting AI behaviors are robust and better capture the complexity of human needs, leading to higher user satisfaction and greater alignment with desired interaction outcomes.

💡 **[Summary](2407.00617/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.00617)**

### Step-Controlled DPO: Leveraging Stepwise Error for Enhanced Mathematical Reasoning

**Relevance:** SCDPO enhances Direct Preference Optimization (DPO), an RL method, by providing fine-grained supervision on individual reasoning steps. This focus on process rather than just the final outcome is critical from an HCI perspective, particularly for tasks requiring high user trust (like mathematical or logical reasoning). By aligning the model based on the correctness of intermediate steps, SCDPO inherently facilitates the generation of more accurate, traceable, and potentially interpretable rationales, reducing the cognitive burden on users required to verify the model’s complex outputs.

💡 **[Summary](2407.00782/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.00782)**

### DogeRM: Equipping Reward Models with Domain Knowledge through Model Merging

**Relevance:** Reward Models (RMs) are central to RLHF alignment. This work proposes integrating specific domain knowledge into RMs via model merging. For HCI, this is essential because effective human-AI interaction in specialized fields (e.g., medicine, finance) requires AI behavior to adhere to domain-specific norms and expertise. DogeRM offers a practical, efficient technique to ensure that RL-aligned agents are not only generally safe but also contextually appropriate and highly trustworthy within the specialized environments where human users operate.

💡 **[Summary](2407.01470/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.01470)**

## Explainable AI

### Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs

**Relevance:** This paper contributes to mechanistic interpretability by studying how LLMs process multi-token concepts through 'token erasure' in early layers. Understanding these internal dynamics is foundational for building reliable user-facing XAI systems. HCI practitioners need assurances that explanations reflect genuine model reasoning, not spurious correlations. Insights from mechanistic analysis, like identifying the formation of implicit vocabulary, can guide the design of attention visualizations or feature importance methods that are grounded in the model's actual conceptual representations, making explanations more accurate and trustworthy.

💡 **[Summary](2406.20086/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.20086)**

