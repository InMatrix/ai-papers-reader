---
layout: default
title: 2026-08-14
permalink: /2026-08-14/
---

# 2026-08-14

## AI for Software Development

### Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review

**Relevance:** Directly relevant to AI for software development: this paper reports a fully instrumented case study in which an AI coding agent dismantles a core architectural invariant across 189 files in a 717k-line TypeScript codebase, with no human review of generated code and no pre-existing test oracle. The specification-first protocol—formal specification, refinement cycles, atomic implementation, compile/test feedback, and verification audits—shows generative AI performing large-scale refactoring and defect correction. For HCI, it reframes the human role from line-by-line code review to specification auditing and convergence-based oversight, an important model for trustworthy human-AI collaboration in software maintenance.

💡 **[Summary](2608.12440/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.12440)**

### Persistent Recursive Worlds Enable Autonomous Software Evolution

**Relevance:** Relevant to AI for software development because it introduces EvoX Genesis, a persistent recursive world model in which finite-lived coding agents evolve a software project over timescales exceeding any single agent. Agents propose local changes, recursive delegation moves work across repository paths, and only accepted consequences advance persistent version history. The system built a Rust C compiler and reimplemented large Fortran modules with speedups. From an HCI perspective, this shifts continuity from an agent session to the project itself, supporting human oversight through versioned state and accepted outcomes rather than requiring continuous agent memory or management.

💡 **[Summary](2608.10450/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.10450)**

## AI Agents

### DarwinX: Evolving Agent Harnesses Through Natural Selection

**Relevance:** Relevant to AI agents because it treats an agent's capability as a function of its harness—prompts, tools, skills, and control flow—and evolves that harness through natural selection over a population. DarwinX uses a preserve-and-extend contract to prevent regression, archives alternative lineages for recombination, and relies on benchmark verifiers as fitness signals without gold solutions or hand-picked winners. This directly addresses agent self-improvement, adaptation, and tool use. From an HCI perspective, the verifier-driven, audit-clean evaluation supports transparent accountability and helps humans understand which agent improvements are general versus task-specific.

💡 **[Summary](2608.07545/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.07545)**

### Agent Safety Should Be a Runtime Contract

**Relevance:** Relevant to AI agents because it argues that agent safety should be enforced as a runtime contract by the harness rather than only instilled during training. It proposes preventive mechanisms such as sandboxes, permission gates, output filters, and trajectory monitors, plus evidential mechanisms that gate task completion on verified proof like test runs, logs, diffs, and citation grounding. This speaks to safety, alignment, and reliable tool use in autonomous agents. For HCI, the emphasis on transparent trajectories and checkable evidence is crucial for user trust, accountability, and appropriate oversight in real-world deployments.

💡 **[Summary](2608.11274/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.11274)**

### OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution

**Relevance:** Relevant to AI agents because it offers an open-ended arena for scalable agent red teaming through environment evolution, addressing safety in long-horizon, stateful tasks. OpenART provides over 10,000 validated scenarios across 50 domains, requiring many tool calls and enabling evaluation across many agent-model configurations. The proposed Evolutionary Markov Hypergraph Attack coordinates authorized environment changes to expose safety failures, with higher attack success as complexity grows. From an HCI perspective, this kind of robustness evaluation helps designers anticipate failure modes, design safer agent environments, and understand how runtime implementation affects safety beyond model choice.

💡 **[Summary](2608.00677/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.00677)**

## LLM Evaluation Methods

### Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity

**Relevance:** Relevant to LLM evaluation because it examines how instruction tuning changes models' verbalized confidence, rationale diversity, and calibration. The paper evaluates matched base and instruction-tuned models on QA benchmarks, showing that instruction tuning consistently alters answer confidence with limited accuracy change and decreased likelihood-based calibration, while cross-rationale diversity decreases. These findings identify confidence and lexical diversity as distinct evaluation signals beyond accuracy. From an HCI perspective, overconfidence and inconsistent rationales directly affect user trust and perceived reliability, making such calibration-aware evaluation essential for human-facing LLM systems.

💡 **[Summary](2608.13430/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.13430)**

### How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review

**Relevance:** Relevant to LLM evaluation because it studies reward hacking in AI-based peer review: how rhetorical choices influence LLM reviewers' judgments even when reported scientific content is preserved. Using a controlled corpus of 4,200 manuscripts derived from 120 ICLR submissions, two rewriters manipulate six rhetorical dimensions and five LLM reviewers score them under standard and strict protocols. The findings reveal structured rhetorical sensitivity and interaction with reviewer scores. For HCI, this demonstrates the need for evaluation protocols robust to content-preserving variation and highlights risks of using LLMs in high-stakes human-in-the-loop assessment.

💡 **[Summary](2608.08975/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.08975)**

### Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives

**Relevance:** Relevant to LLM evaluation because it introduces NCP-Bench, a benchmark for long-horizon consistency in interactive narratives. It defines Narrative Commitment Preservation and evaluates LLM narrators across 100 movie-derived environments under adversarial user interventions. Results show that high linguistic quality does not guarantee commitment preservation, with low survival rates and high fact conflict rates even for strong models. This moves LLM evaluation beyond static benchmarks to interactive, multi-turn settings. From an HCI perspective, narrative consistency is critical for user trust and experience in AI-driven games and interactive storytelling.

💡 **[Summary](2608.08160/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.08160)**

## Reinforcement Learning

### SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models

**Relevance:** Relevant to reinforcement learning because it proposes a natural-language-driven RL framework, SKILLER, which treats a small-model agent system as the environment and uses a strong model as actor and critic to generate executor-specific skills. All RL signals are propagated in natural language, enabling automatic skill extraction that improves task execution across benchmarks. This is a novel application of RL to policy and behavior-space design. From an HCI perspective, it makes agent skill customization more accessible and affordable, allowing smaller models to be deployed on consumer hardware while preserving quality—an important step for practical human-AI collaboration.

💡 **[Summary](2608.10538/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.10538)**

### Parameter Exploration for RLVR via Variational Learning

**Relevance:** Relevant to reinforcement learning because it investigates parameter-space exploration for RLVR, an underexplored complement to action-space exploration. The authors introduce Perturbed Parameter Policy Optimization (3PO), which samples policies from a posterior to generate diverse rollouts and groups them differently for reward estimation. Experiments on math and code tasks show improved performance over GRPO at similar FLOPs, with fewer zero-advantage groups and malformed rollouts. This advances policy optimization and exploration-exploitation balance. For HCI, understanding exploration dynamics helps design training environments where human feedback and reward signals can guide robust learning.

💡 **[Summary](2608.09805/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.09805)**

### Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

**Relevance:** Relevant to reinforcement learning because it introduces CaRL, a Capability-aligned Reinforcement Learning method that trains LLMs to abort futile reasoning. It uses reward shaping to incentivize refusal over specious reasoning and hindsight refusal augmentation to turn failed rollouts into refusal supervision. This is a direct example of policy optimization and reward design, aligning model behavior with capability boundaries. From an HCI perspective, teaching models when to abstain is essential for trust and safety, preventing plausible but incorrect derivations from misleading users in interactive AI systems.

💡 **[Summary](2607.29211/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.29211)**

## Explainable AI

### Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence

**Relevance:** Relevant to explainable AI because it builds an agentic system for autonomous mechanistic discovery of AI intelligence. Mechanist integrates an interpretability-focused knowledge graph, a large multidisciplinary database, and a library of causal intervention and validation methods. It generates and tests mechanism hypotheses, revealing cross-modal safety transfer, a mechanism theory of belief, and practical model-steering interventions. This moves XAI from static feature attribution to active causal understanding. From an HCI perspective, mechanistic explanations can support scientists and practitioners in understanding capabilities and risks, enabling informed oversight and control of complex models.

💡 **[Summary](2608.12036/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.12036)**

### Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus

**Relevance:** Relevant to explainable AI because it provides a mechanistic account of massive activations in hybrid linear attention LLMs. The paper identifies two architecture-aligned morphologies—pre-attention spikes and inter-spike plateaus—and explains their lifecycle through a write-sink-cancel process. By analyzing outlier activations across architectures, scales, and data domains, it contributes to understanding how internal representations are organized. This kind of interpretability knowledge can inform debugging and monitoring. For HCI, it helps researchers and developers anticipate model behavior and design transparent systems that surface relevant internal states to users or auditors.

💡 **[Summary](2608.12149/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.12149)**

### The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images

**Relevance:** Relevant to explainable AI because it causally audits visual tool-use in multimodal LLMs. It formulates tool-use as a causal graph and introduces interventions at policy, trajectory, and step levels, including Visual Evidence Gain, to determine whether returned observations causally affect answers. The findings reveal failure modes where visual tool-use is not causally effective despite aggregate gains. This is a strong example of explanation via causal intervention rather than post-hoc saliency. From an HCI perspective, it helps users understand when visual tool-use is reliable, preventing over-trust in apparently capable but non-causal model behaviors.

💡 **[Summary](2608.06270/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.06270)**

