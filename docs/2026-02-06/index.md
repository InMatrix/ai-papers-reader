---
layout: default
title: 2026-02-06
permalink: /2026-02-06/
---

# 2026-02-06

## AI for Software Development

### Learning to Repair Lean Proofs from Compiler Feedback

**Relevance:** This research studies proof repair as a supervised learning problem, addressing the 'Bug detection and fixing' element of AI for SWE. It introduces APRIL, a dataset pairing erroneous proofs with compiler diagnostics and aligned repairs. From an HCI perspective, the ability of the system to predict both a corrected proof and a natural-language diagnosis grounded in compiler feedback is critical. This transparency significantly lowers the cognitive burden on the developer when interpreting and trusting automated fixes, accelerating the debugging loop and improving the usability of theorem-proving and coding assistants.

💡 **[Summary](2602.02990/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.02990)**

### BatCoder: Self-Supervised Bidirectional Code-Documentation Learning via Back-Translation

**Relevance:** BatCoder optimizes both code generation and documentation production using a self-supervised reinforcement learning framework. This directly addresses two core SWE topics: 'Code completion and generation' and 'Documentation generation.' By allowing models to be trained efficiently using only code, it scales the creation of high-quality software artifacts. High-fidelity, automatically generated documentation is essential for maintainability and developer onboarding (HCI), ensuring that the output of AI coding tools is not only functional but also well-explained and usable.

💡 **[Summary](2602.02554/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.02554)**

### MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering

**Relevance:** MEnvAgent introduces a framework for automated, scalable construction of verifiable execution environments for software engineering (SWE) tasks across diverse languages. This infrastructure is foundational for creating robust AI systems capable of complex tasks like code refactoring and bug fixing. Crucially, the focus on *verifiable* datasets ensures that the AI-generated code solutions are functionally correct and safe before deployment. This addresses major HCI concerns regarding the reliability and trustworthiness of autonomous SWE agents in production settings.

💡 **[Summary](2601.22859/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.22859)**

## AI Agents

### AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent

**Relevance:** AgentArk proposes distilling the superior reasoning and self-correction performance of high-cost multi-agent systems into a single, computationally efficient LLM agent. This directly relates to developing agents that can 'Use reasoning to make decisions' and 'Learn from experience.' By shifting the computational burden from inference to training, AgentArk ensures that advanced agent capabilities are efficient enough for practical deployment, improving the responsiveness and reducing the operational cost of autonomous systems that interact with human users (HCI).

💡 **[Summary](2602.03955/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.03955)**

### D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use

**Relevance:** D-CORE focuses on training reasoning models to improve sub-task decomposition and complex tool use, addressing the identified problem of 'Lazy Reasoning.' This is essential for agents that need to 'Break complex tasks into manageable steps' and 'Interact with digital tools.' From an HCI standpoint, better task decomposition leads to agent trajectories that are more reliable and inherently easier for human users to interpret and verify, fostering greater trust in the agent's planning and execution capabilities.

💡 **[Summary](2602.02160/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.02160)**

### Vibe AIGC: A New Paradigm for Content Generation via Agentic Orchestration

**Relevance:** Vibe AIGC introduces a paradigm shift towards agentic orchestration for content generation, focusing on bridging the 'Intent-Execution Gap' between high-level human goals (the 'Vibe') and machine output. This is directly relevant to creating agents that 'Maintain safety and alignment with human values.' The framework transforms the user into a 'Commander' who guides a hierarchical multi-agent workflow, significantly improving creative control and usability (HCI) compared to traditional, stochastic single-shot generative models.

💡 **[Summary](2602.04575/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04575)**

## LLM Evaluation Methods

### HalluHard: A Hard Multi-Turn Hallucination Benchmark

**Relevance:** HalluHard is a challenging multi-turn benchmark designed to test LLMs' factual grounding and reliability in high-stakes domains (legal, medical, coding). This directly addresses the need for rigorous 'Benchmarking' and 'Robustness testing.' From an HCI perspective, ungrounded factual claims (hallucinations) are a primary barrier to user trust and model usability in critical applications. This benchmark provides the necessary tooling to measure and mitigate these core failure modes, driving progress toward reliable AI systems.

💡 **[Summary](2602.01031/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.01031)**

### Trust The Typical

**Relevance:** T3 introduces a framework for LLM safety that operationalizes safety as an out-of-distribution detection problem, learning the distribution of acceptable prompts. This is highly relevant to 'Ethical and bias evaluation' and 'Robustness testing.' T3 significantly reduces false positive rates compared to traditional safety guardrails, leading to fewer 'over-refusal' instances. This stability and reduced friction directly enhances user satisfaction and trust, making the safety mechanism less intrusive during normal interaction (HCI implication).

💡 **[Summary](2602.04581/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04581)**

### From Data to Behavior: Predicting Unintended Model Behaviors Before Training

**Relevance:** This paper proposes Data2Behavior, a task and method for predicting unintended model biases and safety risks by analyzing training data representations *before* the costly fine-tuning process. This proactive approach is essential for 'Ethical and bias evaluation.' By identifying latent statistical signals that lead to harmful behaviors early on, researchers can ensure fairness and inclusivity, mitigating societal risks and upholding user trust before a model is ever deployed to the public.

💡 **[Summary](2602.04735/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04735)**

## Reinforcement Learning

### SAFE: Stable Alignment Finetuning with Entropy-Aware Predictive Control for RLHF

**Relevance:** SAFE is a novel RLHF algorithm that addresses stability issues (reward oscillations, policy divergence) commonly found in PPO. It employs a multi-layer stabilization framework combining entropy-gated KL regulation and PID-controlled adaptive thresholds, fitting the 'Policy optimization' topic. For HCI, stable alignment ensures that the LLM policy reliably converges to the desired 'human preferences,' making the final deployed model's behavior more predictable, safer, and better aligned with user intent over long-horizon optimization.

💡 **[Summary](2602.04651/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04651)**

### VLS: Steering Pretrained Robot Policies via Vision-Language Models

**Relevance:** VLS introduces a training-free framework for inference-time adaptation of frozen robot policies, steering them based on vision-language inputs. This directly relates to how humans can 'effectively guide agent learning' and interpret agent behaviors. By allowing human language instructions to dynamically control and adapt robot actions in out-of-distribution scenarios, VLS facilitates intuitive human-agent collaboration and improves the robustness and controllability of robotic systems.

💡 **[Summary](2602.03973/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.03973)**

### WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning

**Relevance:** This paper leverages multi-agent reinforcement learning (MARL) to optimize a lead-agent-subagent framework for broad information seeking (width scaling). This is a significant contribution to 'Multi-agent RL.' For HCI, this organizational capability allows the system to parallelize complex tasks and synthesize information efficiently, leading to faster and more comprehensive results for users. This showcases how MARL can be used to design environments that facilitate scalable and high-utility human-agent collaboration.

💡 **[Summary](2602.04634/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04634)**

## Explainable AI

### "I May Not Have Articulated Myself Clearly": Diagnosing Dynamic Instability in LLM Reasoning at Inference Time

**Relevance:** This work introduces a training-free method to diagnose reasoning failures mid-generation using inference-time signals (JSD, entropy), identifying when the model 'loses the thread.' This provides a crucial diagnostic lens for XAI, offering transparency into the model's internal decision process. Understanding whether instability is 'corrective' or 'destructive' helps researchers and users interpret *how* a failure occurred, which is essential for building trust and designing effective human-in-the-loop validation mechanisms.

💡 **[Summary](2602.02863/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.02863)**

### Beyond Unimodal Shortcuts: MLLMs as Cross-Modal Reasoners for Grounded Named Entity Recognition

**Relevance:** This research addresses modality bias in MLLMs by enforcing Modality-aware Consistency Reasoning (MCR). This focuses on making the model's decision-making process more transparent and interpretable by ensuring rigorous cross-modal verification, rather than relying on unimodal shortcuts. By transforming abstract constraints into verifiable reasoning chains, MCR provides a mechanism to assure users (HCI) that the model's output is based on comprehensive, aligned evidence, enhancing reliability and trust in multimodal systems.

💡 **[Summary](2602.04486/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.04486)**

### Semantic Routing: Exploring Multi-Layer LLM Feature Weighting for Diffusion Transformers

**Relevance:** This paper explores systematically organizing multi-layer LLM hidden states to condition generative models, focusing on depth-wise feature weighting. This research provides insights into *what* semantic information the model utilizes *when* during the generation process. By studying this internal mechanism, it serves as a foundation for future 'Attention visualization' and feature importance techniques, crucial for making the complex black-box behavior of generative AI systems more transparent and interpretable to human users.

💡 **[Summary](2602.03510/)** 📄 **[Full paper](https://arxiv.org/pdf/2602.03510)**

