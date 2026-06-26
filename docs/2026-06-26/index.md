---
layout: default
title: 2026-06-26
permalink: /2026-06-26/
---

# 2026-06-26

## AI for Software Development

### Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence

**Relevance:** This survey explores how models connect visual perception to executable programs for tasks like generating, editing, and refining code from visual artifacts like screenshots and charts. From an HCI perspective, it shifts the focus of AI for software development from simple text-based code completion to visually grounded, interactive programming environments. The paper's proposed verification-centered directions, such as multi-state verification across execution trajectories, have profound implications for designing more robust, user-centered debugging and development tools that align with actual human developer workflows and visual intents.

📄 **[Full paper](https://arxiv.org/pdf/2606.15932)**

### Autodata: An agentic data scientist to create high quality synthetic data

**Relevance:** This paper introduces Autodata, which enables AI agents to act as data scientists to create high-quality training and evaluation data. It demonstrates how to train these agents to perform complex data science tasks, aligning directly with AI for software development by automating data engineering workflows. For HCI, this highlights a shift where developers collaborate with agentic data scientists, changing how software and machine learning pipelines are constructed. The study's focus on computer science and reasoning tasks shows how generative AI can assist in the broader software development lifecycle.

📄 **[Full paper](https://arxiv.org/pdf/2606.25996)**

### ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation

**Relevance:** ReNIO improves LLM reasoning and code generation by training models on their own incorrect outputs, utilizing student-to-teacher probability ratios to identify pivotal errors. In the context of AI for software development, this method enhances the model's ability to self-correct and generate more robust code. From an HCI standpoint, understanding how models learn from "negative" or erroneous trajectories can help in designing better interactive debugging tools. By training models to recognize their own logical missteps, AI assistants can provide more explainable code refactoring and bug-fixing suggestions to human developers.

📄 **[Full paper](https://arxiv.org/pdf/2606.23104)**

## AI Agents

### Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents

**Relevance:** This paper diagnoses a critical vulnerability in long-horizon LLM agents: they do not carry plans forward as persistent state and instead suffer from "plan eviction" due to naive context management. This research is highly relevant to HCI because context management directly impacts the reliability and predictability of agents interacting with users over long-term tasks. By introducing a probe-gated re-surfacing framework to protect plans, the authors offer a concrete system-level design pattern that prevents agents from losing track of user-defined goals, thereby improving user trust and reducing the cognitive overhead of human-agent collaboration.

📄 **[Full paper](https://arxiv.org/pdf/2606.22953)**

### PrivacyAlign: Contextual Privacy Alignment for LLM Agents

**Relevance:** PrivacyAlign addresses the critical challenge of aligning LLM agents with human privacy norms during tool use and decision-making. By introducing a dataset grounded in human annotations and using annotation-conditioned reward modeling, the paper places human judgment at the center of agent training. For HCI, this is a vital contribution to agent safety and trust, as it ensures agents make contextually appropriate decisions about what information to share. It demonstrates how HCI methods (collecting human expectations and social norms) can directly guide the reinforcement learning process to build socially aligned, trustworthy autonomous agents.

📄 **[Full paper](https://arxiv.org/pdf/2606.21710)**

### When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

**Relevance:** This paper investigates "over-privileged tool selection," where LLM agents escalate to high-privilege tools unnecessarily, posing significant safety and security risks. The authors introduce a privilege-aware defense that trains agents to prefer the least-privileged tool sufficient for a task. From an HCI perspective, this research is crucial for building user trust and safety in agentic systems. By establishing predictable, least-privilege tool execution boundaries, the system minimizes security risks during autonomous operations, ensuring that the agent's actions remain strictly aligned with safety-conscious human values and organizational policies.

📄 **[Full paper](https://arxiv.org/pdf/2606.20023)**

## LLM Evaluation Methods

### MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

**Relevance:** MEMPROBE shifts the evaluation of agent memory from downstream task success to auditing the memory artifact itself by reconstructing the agent's understanding of the user. This is highly relevant to HCI, as long-term personalization is key to user satisfaction. Traditional evaluations treat memory as a black box, but MEMPROBE evaluates how well an agent retains an accurate, evolving model of the user. This benchmark provides HCI researchers with a rigorous tool to measure user-state recovery, directly addressing how agent memory systems can be designed to foster deeper, more faithful long-term human-agent relationships.

📄 **[Full paper](https://arxiv.org/pdf/2606.24595)**

### CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression

**Relevance:** CAVEWOMAN evaluates LLMs under input and output compression (e.g., "caveman" style prompts), measuring task accuracy, API costs, and semantic divergence. This study has direct implications for HCI and user experience design, as users often compress their prompts to save time or tokens, which the paper reveals actually increases net costs and collapses accuracy. By demonstrating how linguistic compression impacts model outputs and costs, this work helps HCI researchers understand the trade-offs in user-facing prompt interfaces, guiding the design of systems that balance user efficiency with optimal model performance and predictability.

📄 **[Full paper](https://arxiv.org/pdf/2606.24083)**

### Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do

**Relevance:** This paper evaluates multimodal Chain-of-Thought (CoT) across 12 tasks, identifying a "Look Light, Think Heavy" pattern where models struggle with deep visual introspection despite strong verbal reflection. This evaluation is highly relevant to HCI as it pinpoints the specific cognitive limitations of current multimodal models. Understanding where CoT fails (e.g., in visual grounding and counting) allows HCI designers to mitigate these limitations by designing interfaces that scaffold the model's visual perception or manage user expectations regarding the model's visual reasoning capabilities, thereby reducing user frustration and improving task collaboration.

📄 **[Full paper](https://arxiv.org/pdf/2606.22565)**

## Reinforcement Learning

### COrigami: An AI Pipeline for Co-Designing Flat-Foldable Visually Recognisable Origami

**Relevance:** COrigami presents an end-to-end pipeline that assists in computational origami design, using reinforcement learning driven by an autonomous aesthetic evaluation loop. This paper perfectly illustrates how RL can be applied to human-AI co-creativity and collaborative design. From an HCI perspective, it shows how RL agents can optimize for subjective human values (like visual aesthetics) alongside rigid geometric constraints. The system acts as a collaborative assistant, generating starting points for human artists, demonstrating a powerful paradigm where RL is utilized to enhance, rather than replace, human creative expression and interaction.

📄 **[Full paper](https://arxiv.org/pdf/2606.26299)**

### Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

**Relevance:** This paper addresses the instability and catastrophic collapse of LLMs during tool-use reinforcement learning. By analyzing how probability spikes in control tokens disrupt execution, and proposing interleaved SFT and RL supervision, it stabilizes multi-step tool-use training. For HCI, this is highly valuable because reliable tool execution is fundamental to a seamless user-agent experience. By resolving these RL-induced failures, this research ensures that agents can interact with digital tools predictably and robustly, minimizing frustrating execution errors and reducing the cognitive friction experienced by users when delegating complex workflows to AI.

📄 **[Full paper](https://arxiv.org/pdf/2606.26027)**

### OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

**Relevance:** OPID proposes extracting hierarchical skill supervision directly from completed on-policy trajectories to guide reinforcement learning. This framework addresses the challenge of sparse rewards by providing dense, token-level supervision based on trajectory hindsight. From an HCI perspective, this research is highly relevant to how agents learn from experience and adapt their strategies over multi-turn interactions. By structuring hindsight as global workflows or local decision knowledge, OPID improves the agent's sample efficiency and robustness, making the learning process more interpretable and aligned with structured human workflows.

📄 **[Full paper](https://arxiv.org/pdf/2606.26790)**

## Explainable AI

### Forecasting Future Behavior as a Learning Task

**Relevance:** This paper proposes "Behavior Forecasters" to predict how an LLM will behave on new inputs or how changes in the input will alter its answers, bypassing traditional, unfaithful explanation methods. This is highly relevant to Explainable AI and HCI, as user trust is built on being able to anticipate an AI's behavior. By framing explanation as a behavior-forecasting task, the authors provide a practical, low-cost way to give users reliable expectations about model reliability (e.g., likelihood to repeat an answer). This directly supports the HCI goal of helping users build accurate mental models of complex AI systems.

📄 **[Full paper](https://arxiv.org/pdf/2606.11445)**

### GridVQA-X: A Framework for Evaluating Multimodal Explainability Methods

**Relevance:** GridVQA-X is a diagnostic framework designed to evaluate whether Multimodal Explainable AI (MxAI) methods faithfully capture cross-modal reasoning or merely exploit shallow shortcuts. The paper reveals that current explainability methods struggle to distinguish between genuine spatial reasoning and shortcuts. This is critical for HCI because false explanations mislead users, creating a misplaced sense of trust. By exposing these fidelity gaps, this work helps HCI and XAI researchers develop more honest, transparent explanation interfaces that accurately reflect the inner workings of vision-language models, preventing user deception.

📄 **[Full paper](https://arxiv.org/pdf/2606.14740)**

### What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics

**Relevance:** This paper analyzes token-level predictive entropy trajectories across the intermediate layers of LLMs to detect jailbreak attempts. It reveals that harmful intent is structured within mid-network representations rather than at the final output head. This work contributes to Explainable AI by visualizing and interpreting the internal uncertainty dynamics of LLMs. From an HCI and safety perspective, localizing where and how adversarial intent is encoded allows developers to build more transparent safety dashboards and real-time intervention interfaces, helping human moderators understand why a model flagged or refused a prompt.

📄 **[Full paper](https://arxiv.org/pdf/2606.25182)**

