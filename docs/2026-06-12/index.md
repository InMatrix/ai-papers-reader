---
layout: default
title: 2026-06-12
permalink: /2026-06-12/
---

# 2026-06-12

## AI for Software Development

### Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

**Relevance:** This paper introduces a benchmark to evaluate agent harnesses (claws) on software engineering tasks under fair, reproducible settings. It addresses how the interface design—specifically the workspace contract and patch extraction adapters—impacts an agent's coding performance and API costs. From an HCI and ML perspective, this research highlights that the design of the developer-agent interface is just as critical as the underlying model's capabilities. By formalizing harness and cost accounting, it provides a structured methodology to design and evaluate more effective, budget-conscious AI assistants for real-world software development workflows.

💡 **[Summary](2606.12344/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.12344)**

### Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code

**Relevance:** This paper exposes a novel security vulnerability where Grammar-Constrained Decoding (GCD), a technique widely used to ensure syntactic correctness in code generation, can be exploited to jailbreak LLMs into producing malicious code. The authors propose CodeShield, a safety alignment approach that maintains safe behavior under grammar constraints. This research has crucial implications for AI-assisted software development and HCI, as it highlights a hidden trade-off between output reliability and security. Designing developer tools that are both syntactically robust and secure is vital for maintaining user trust in AI programming assistants.

💡 **[Summary](2606.11817/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.11817)**

## AI Agents

### Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents

**Relevance:** Evoflux addresses the challenge of deploying compact language models as tool-use agents. Since small planners often generate workflows that fail during execution or tool resolution, Evoflux introduces an inference-time evolutionary search method that treats tool use as the repair of executable workflows using execution feedback. This is highly relevant to AI Agents as it improves planning, tool discovery, and error recovery. From an HCI perspective, this approach makes agents significantly more reliable and resilient when interacting with complex digital environments, reducing the need for human intervention when tool calls fail.

💡 **[Summary](2606.12674/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.12674)**

### EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

**Relevance:** This paper introduces EvoArena, a benchmark for evaluating agents in dynamic, evolving environments, and EvoMem, a patch-based memory paradigm that records structured update histories. Since real-world agent deployment environments (like software or social systems) change constantly, agents must adapt their knowledge. EvoMem enables agents to reason about environmental evolution through memory updates. This research is highly relevant to AI Agents, as it directly addresses long-term memory and adaptability. From an HCI standpoint, robust memory tracking reduces user frustration by ensuring agents remain aligned with changing task conditions and environments.

💡 **[Summary](2606.13681/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.13681)**

### HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness

**Relevance:** HarnessBridge introduces a learnable plug-in module that acts as a bidirectional controller between an LLM agent and its environment. It parameterizes the agent-environment interface into observation and action projections, optimizing raw trajectories into decision-relevant states and actions. This directly addresses the 'harness' design in AI Agents. From an HCI and ML perspective, replacing manually engineered harnesses with learnable controllers significantly reduces token usage, shortens interaction trajectories, and improves generalization across environments. This makes agent-environment interactions more efficient, scalable, and adaptable to complex, long-horizon user tasks.

💡 **[Summary](2606.12882/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.12882)**

## LLM Evaluation Methods

### EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge

**Relevance:** This paper introduces EvoBrowseComp, an evolving, contamination-free benchmark for evaluating search agents on live-web knowledge. By using a three-agent collaborative framework to continuously synthesize fresh questions and filter parametric shortcuts, it ensures that models are evaluated on genuine retrieval and browsing competence rather than memorized facts. In LLM evaluation, this addresses the critical challenge of static test-set contamination. From an HCI perspective, it ensures that search agents are evaluated under realistic, dynamic information conditions, leading to more reliable and trustworthy systems for users seeking up-to-date real-world information.

💡 **[Summary](2606.13120/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.13120)**

### WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces

**Relevance:** WeaveBench is a long-horizon benchmark evaluating computer-use agents across hybrid interfaces (GUI, CLI, and code) based on real-world user requests. It highlights that traditional outcome-only grading significantly overestimates agent capabilities and introduces a trajectory-aware judge to detect visual fabrication and shortcuts. For LLM evaluation, this paper emphasizes the importance of multi-interface orchestration and robust, path-sensitive grading. From an HCI perspective, evaluating agents on realistic desktop environments with multi-modal interfaces ensures that they can safely and accurately perform complex, long-horizon tasks as intended by human users.

💡 **[Summary](2606.09426/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.09426)**

### Large Language Models Are Overconfident in Their Own Responses

**Relevance:** This work studies the miscalibration of conversational LLMs, identifying an 'ownership bias' where models exhibit significantly higher confidence in their own answers than in identical user-provided inputs. To mitigate this overconfidence, the authors propose a simple, training-free inference strategy that frames the model's response as user input. This paper is highly valuable for LLM evaluation and HCI, as overconfident, incorrect outputs severely damage user trust. By improving calibration and reducing overconfidence without retraining, this method directly enhances human-AI collaboration and helps users better judge when to trust model-generated information.

💡 **[Summary](2606.03437/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.03437)**

## Reinforcement Learning

### N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization

**Relevance:** N-GRPO introduces an exploration strategy for Group Relative Policy Optimization (GRPO) that utilizes Semantic Neighbor Mixing in the embedding space. By mixing anchor token embeddings with their nearest semantic neighbors, it injects diversity into the rollout phase while strictly preserving local semantic consistency. This directly advances reinforcement learning policy optimization for mathematical reasoning. From an HCI perspective, generating diverse yet semantically coherent solution paths helps conversational agents provide users with alternative, valid ways to solve complex problems, improving user learning, satisfaction, and trust during interactive problem-solving sessions.

💡 **[Summary](2606.10768/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.10768)**

### TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

**Relevance:** TRACE is a rollout budget allocation framework designed to enhance reinforcement learning with verifiable rewards (RLVR) in multi-turn agentic settings. By modeling ReAct-style turns as distinct nodes, TRACE dynamically allocates sampling budgets to prompt roots and intermediate prefixes most likely to yield mixed terminal rewards. This adaptive tree structure enriches feedback and amplifies the policy-update signal. For RL, this represents a highly efficient approach to policy optimization. For HCI, training agents with TRACE leads to more reliable multi-step planners, facilitating smoother and more successful long-horizon human-agent collaborations.

💡 **[Summary](2606.11119/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.11119)**

### DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning

**Relevance:** DyCo-RL integrates dynamic cross-modal coordination into Reinforcement Learning with Verifiable Rewards (RLVR). By measuring within-modality attention shifts using Fisher-Rao geodesic distance, it aligns a token's actual attention with its functional role (visual vs. textual) during Chain-of-Thought reasoning. This addresses a fundamental RL optimization gap by focusing on fine-grained generation coordination rather than just final outcomes. For HCI, this ensures that multimodal models dynamically coordinate visual evidence with textual context. This leads to more coherent, visually grounded reasoning, directly improving user trust and interaction quality in visual-centric AI assistants.

💡 **[Summary](2606.08035/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.08035)**

## Explainable AI

No paper recommendations for this topic.

