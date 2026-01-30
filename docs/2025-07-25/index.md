---
layout: default
title: 2025-07-25
permalink: /2025-07-25/
---

# 2025-07-25

## AI for Software Development

### Re:Form -- Reducing Human Priors in Scalable Formal Software Verification with RL in LLMs: A Preliminary Study on Dafny

**Relevance:** This paper explores using Reinforcement Learning (RL) to enhance LLMs in generating formally verified software (Dafny). This advances the core AI4SD goal of reliable code generation. The HCI implication lies in the necessity for robust interfaces that allow developers to interact with and trust mathematically provable code. While reducing human priors in training is efficient, the resulting system requires sophisticated XAI/HCI methods to ensure the developer can understand and maintain the complex formal reasoning produced by the RL-trained LLM.

💡 **[Summary](2507.16331/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.16331)**

## AI Agents

### ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

**Relevance:** ThinkAct introduces a dual-system framework for Vision-Language-Action (VLA) agents that generates explicit reasoning plans compressed into a visual latent. This separation of high-level reasoning and low-level action is highly relevant to HCI for embodied agents. It offers a potential 'handle' for human users, allowing HCI researchers to design interfaces that monitor the agent's internal visual plan, enabling human intervention, self-correction, and interpretation of agent failures during complex, long-horizon tasks.

💡 **[Summary](2507.16815/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.16815)**

### STITCH: Simultaneous Thinking and Talking with Chunked Reasoning for Spoken Language Models

**Relevance:** STITCH addresses a core HCI challenge in conversational AI: latency caused by internal reasoning. By interleaving unspoken reasoning chunks with spoken response chunks, it achieves 'simultaneous thinking and talking.' This dramatically improves the responsiveness and perceived intelligence of the Spoken Language Model. HCI researchers can further leverage this chunked architecture to selectively expose reasoning steps to the user (e.g., via a visual interface) to enhance transparency and trust without incurring interaction delays.

💡 **[Summary](2507.15375/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.15375)**

### SPAR: Scholar Paper Retrieval with LLM-based Agents for Enhanced Academic Search

**Relevance:** SPAR presents a multi-agent framework for complex academic search, utilizing query decomposition and evolution. This paper demonstrates the deployment of LLM agents for sophisticated, real-world information retrieval tasks. The HCI challenge here is designing effective human-agent collaboration interfaces that allow users to manage the multi-agent workflow, inspect the agents' query decomposition process, and trust the aggregated results from multiple, specialized agents.

💡 **[Summary](2507.15245/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.15245)**

## LLM Evaluation Methods

### RAVine: Reality-Aligned Evaluation for Agentic Search

**Relevance:** RAVine proposes a crucial shift in LLM evaluation by focusing on the 'iterative process' and 'tool interaction efficiency' inherent to AI agents, rather than just the final answer. This aligns perfectly with HCI evaluation needs, which emphasize assessing the quality of the interaction and the system's utility in real-world, complex scenarios. By using 'reality-aligned' multi-point queries, RAVine helps ensure that evaluation metrics reflect actual user intent and agent performance bottlenecks.

💡 **[Summary](2507.16725/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.16725)**

### Inverse Scaling in Test-Time Compute

**Relevance:** This paper reveals that increasing reasoning length (test-time compute) can paradoxically deteriorate performance, identifying failure modes like distraction and overfitting. This finding is critical for HCI, as inconsistent or deteriorating behavior under scaling directly undermines user trust and increases cognitive load. Evaluation methods must explicitly test for this 'inverse scaling' to ensure that models intended for complex reasoning provide reliable and trustworthy interactive experiences.

💡 **[Summary](2507.14417/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.14417)**

### PrefPalette: Personalized Preference Modeling with Latent Attributes

**Relevance:** PrefPalette enhances evaluation by decomposing human preferences into interpretable attribute dimensions (e.g., formality, sarcasm) tailored to specific social communities. This moves beyond aggregate metrics, providing transparent insights into *why* a model output is preferred or disliked. This is invaluable for HCI evaluation, enabling the development of personalized AI systems that are explicitly aligned with diverse user values and providing the foundation for more trustworthy and customizable interactions.

💡 **[Summary](2507.13541/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.13541)**

## Reinforcement Learning

### A Simple "Try Again" Can Elicit Multi-Turn LLM Reasoning

**Relevance:** This work introduces Unary Feedback as Observation (UFO) into RL training, demonstrating that minimal, natural human feedback (like 'Try Again') can significantly improve multi-turn reasoning. This is highly relevant to Human-in-the-Loop RL and HCI. UFO provides a scalable, low-effort method for humans to guide and correct LLM behavior in interactive, conversational settings, effectively bridging the gap between formal RL reward signals and intuitive human-AI communication.

💡 **[Summary](2507.14295/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.14295)**

### The Invisible Leash: Why RLVR May Not Escape Its Origin

**Relevance:** This paper investigates the theoretical limits of Reinforcement Learning with Verifiable Rewards (RLVR), concluding that it often acts as a conservative reweighting mechanism constrained by the base model's initial support. For HCI, this finding is crucial: it warns that RL may not lead to truly novel reasoning, but rather reinforces known solutions. Future human-agent collaboration systems must integrate explicit exploration mechanisms, possibly guided by human input, to overcome this 'invisible leash' and facilitate genuine discovery.

📄 **[Full paper](https://arxiv.org/pdf/2507.14843)**

### Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training

**Relevance:** This paper uses a Reinforcement Learning Agent to learn optimal heuristics for mixing data domains during continual pre-training. This meta-learning approach has significant implications for system stability and reliability, which are core HCI concerns. By automating data management, the RL agent ensures balanced performance across source and target domains, preventing catastrophic forgetting and improving the long-term, consistent utility of the LLM for the end-user.

💡 **[Summary](2507.15640/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.15640)**

## Explainable AI

### Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning

**Relevance:** CAFT leverages interpretability tools (concept directions in latent space) to proactively steer an LLM away from undesired generalizations during fine-tuning. This represents a shift from passive XAI (explaining past behavior) to active, preventative control, which is essential for aligned and trustworthy AI. By using latent space explanations to enforce behavioral constraints without modifying training data, CAFT offers a powerful method for controlling complex model behavior in a human-interpretable manner.

💡 **[Summary](2507.16795/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.16795)**

### Does More Inference-Time Compute Really Help Robustness?

**Relevance:** This research reveals a critical trade-off: making intermediate reasoning steps accessible (a form of XAI) can reduce model robustness, exhibiting an inverse scaling law under adversarial conditions. This finding is vital for XAI design, forcing practitioners to weigh the benefits of transparency for user trust against potential security risks. It highlights the need for HCI-informed XAI that provides sufficient transparency for utility without revealing exploitable internal mechanics.

💡 **[Summary](2507.15974/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.15974)**

### RefCritic: Training Long Chain-of-Thought Critic Models with Refinement Feedback

**Relevance:** RefCritic trains LLM critic modules using RL to generate high-quality, 'actionable feedback' based on refinement accuracy. This moves XAI from simple descriptive explanations to prescriptive guidance. The focus on generating critiques that effectively guide model refinement means the explanations are intrinsically useful and interpretable, providing a robust mechanism for users or downstream systems to understand *how* to correct the AI's reasoning chain, thus enhancing trust and collaboration.

💡 **[Summary](2507.15024/)** 📄 **[Full paper](https://arxiv.org/pdf/2507.15024)**

