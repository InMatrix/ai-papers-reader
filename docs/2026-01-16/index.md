---
layout: default
title: 2026-01-16
permalink: /2026-01-16/
---

# 2026-01-16

## AI for Software Development

### MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences

**Relevance:** This paper addresses a key limitation of autonomous software engineering (SWE) agents by integrating 'open-world' human expertise from platforms like GitHub. By converting fragmented human experience into structured, actionable memory cards and enabling logic-driven retrieval, MemGovern improves the reliability and resolution rates of code agents in real-world bug fixing. This framework provides a critical infrastructure upgrade for developer-assisting AI, allowing them to leverage collective human knowledge for more robust code generation and maintenance.

💡 **[Summary](2601.06789/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.06789)**

### Controlled Self-Evolution for Algorithmic Code Optimization

**Relevance:** This work focuses on improving the efficiency and quality of code generation, a core task in AI for software development. It addresses limitations in existing self-evolution methods (like initialization bias) by proposing Controlled Self-Evolution (CSE) with diversified planning and feedback-guided genetic evolution. By consistently discovering solutions with superior complexity and maintaining continuous improvement, CSE provides developers with more efficient and highly optimized algorithmic code suggestions, enhancing the utility of LLMs in performance-critical software tasks.

💡 **[Summary](2601.07348/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.07348)**

### Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

**Relevance:** This paper tackles the 'usability gap' in cluster workload allocation by introducing an intent-driven scheduling paradigm based on LLMs. Instead of complex technical configurations, users can express soft affinity preferences using natural language. This application of AI directly simplifies a traditionally complex software management task, significantly improving the accessibility and usability of high-performance computing resources, which is a core benefit of AI assistance in software development environments.

💡 **[Summary](2601.09282/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.09282)**

## AI Agents

### EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines

**Relevance:** This research addresses the instability and instruction drift common in self-evolving LLM agents by imposing structure via an explicit Finite State Machine (FSM). EvoFSM enables controllable self-evolution, decoupling optimization into macroscopic flow and microscopic skill improvement. This focus on structured adaptation and control is vital for building reliable, aligned AI agents that maintain safety and predictable behavior, which are non-negotiable requirements for robust human-agent collaboration and deployment.

💡 **[Summary](2601.09465/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.09465)**

### MemoBrain: Executive Memory as an Agentic Brain for Reasoning

**Relevance:** MemoBrain proposes an executive memory model essential for sustaining coherent, goal-directed reasoning in long-horizon tool-augmented agents. By constructing a dependency-aware memory that actively manages the working context (pruning invalid steps and folding completed sub-trajectories), it provides explicit cognitive control. This architectural innovation in memory is foundational for agents to handle complex, multi-step user requests without losing context or logical continuity, thereby improving agent reliability and user experience.

💡 **[Summary](2601.08079/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.08079)**

### The Agent's First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios

**Relevance:** This paper introduces a dynamic evaluation environment that shifts agent assessment from static tests to stochastic, production-oriented scenarios. It benchmarks agents on dynamic task scheduling, active exploration under uncertainty, and continuous learning—all crucial dimensions for real-world deployment. This work provides a framework for assessing agent reliability and robustness, directly addressing HCI concerns about how agents perform and adapt in novel, unpredictable environments encountered in workflow automation.

💡 **[Summary](2601.08173/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.08173)**

## LLM Evaluation Methods

### Are LLMs Vulnerable to Preference-Undermining Attacks (PUA)? A Factorial Analysis Methodology for Diagnosing the Trade-off between Preference Alignment and Real-World Validity

**Relevance:** This paper introduces a novel factorial evaluation methodology to diagnose susceptibility to manipulative prompts (PUA). It assesses the critical trade-off between preference alignment (making the user happy) and truthfulness (real-world validity). This fine-grained diagnostic approach is highly relevant to HCI and safety evaluation, as it provides nuanced insights into LLM robustness, helping developers ensure that models remain trustworthy and truthful even under adversarial or manipulative human interaction patterns.

💡 **[Summary](2601.06596/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.06596)**

### ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios

**Relevance:** ViDoRe V3 is a comprehensive multimodal RAG benchmark designed to test systems in complex, real-world scenarios involving visual elements (tables, charts) and multi-document synthesis. Crucially, it provides high-quality annotations for retrieval relevance and accurate source grounding. This benchmark directly addresses HCI concerns regarding trust and verifiability, ensuring that LLM evaluations move beyond simple text-based tasks to assess the reliability of RAG pipelines in professional, visually rich domains.

💡 **[Summary](2601.08620/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.08620)**

### EpiCaR: Knowing What You Don't Know Matters for Better Reasoning in LLMs

**Relevance:** This work addresses model overconfidence (miscalibration), a significant barrier to user trust, by proposing Epistemically-Calibrated Reasoning (EpiCaR). By jointly optimizing reasoning performance and calibration using explicit self-evaluation signals, EpiCaR enables LLMs to reliably communicate uncertainty. This is essential for safety-critical applications, as a well-calibrated model reduces the cognitive load on the human user by signaling when its output should not be fully trusted.

💡 **[Summary](2601.06786/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.06786)**

## Reinforcement Learning

### ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking

**Relevance:** ArenaRL introduces a novel RL paradigm to address the difficulty of applying RL to open-ended agent tasks where objective ground truth is absent. By shifting from pointwise scalar scoring to intra-group relative ranking via a tournament-based evaluation, it generates stable advantage signals. This approach leverages comparative human preferences (or preference models derived from them) efficiently, demonstrating how RL can be scaled effectively by incorporating nuanced feedback reflective of real-world user satisfaction in complex, subjective tasks.

💡 **[Summary](2601.06487/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.06487)**

### SCALER:Synthetic Scalable Adaptive Learning Environment for Reasoning

**Relevance:** SCALER proposes an adaptive environment design framework for RL, specifically for enhancing reasoning capabilities. By dynamically adjusting task difficulty and curating problem sets, it sustains effective learning signals, preventing reward sparsity and overfitting. This mechanism is crucial for training complex agents and has HCI implications by ensuring that RL agents are trained robustly across a diverse skill set, leading to more generalized and trustworthy behaviors when interacting with humans.

📄 **[Full paper](https://arxiv.org/pdf/2601.04809)**

### Aligning Text, Code, and Vision: A Multi-Objective Reinforcement Learning Framework for Text-to-Visualization

**Relevance:** This paper applies RL with a novel multi-objective reward function to the Text-to-Visualization task. The reward jointly optimizes for textual accuracy, code validity, and visualization quality based on post-execution feedback. This is a direct application of RL to optimize for subjective, user-perceived qualities (visualization clarity and semantic alignment), demonstrating how RL can be guided by HCI principles to generate outputs that maximize user satisfaction and utility.

💡 **[Summary](2601.04582/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.04582)**

## Explainable AI

### sui-1: Grounded and Verifiable Long-Form Summarization

**Relevance:** sui-1 addresses the critical issue of LLM unfaithfulness by generating abstractive summaries that include inline citations, allowing users to trace every claim back to its source text. This is a powerful, user-facing XAI mechanism that enables verification and builds trust, especially in compliance-sensitive domains. The ability to ground abstractive content serves as a crucial form of transparency, shifting the burden of verification away from the user's cognitive load.

💡 **[Summary](2601.08472/)** 📄 **[Full paper](https://arxiv.org/pdf/2601.08472)**

