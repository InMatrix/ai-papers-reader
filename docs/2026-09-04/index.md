---
layout: default
title: 2026-09-04
permalink: /2026-09-04/
---

# 2026-09-04

## AI for Software Development

### RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests

**Relevance:** RealSWE targets the gap between curated SWE-bench tasks and genuine developer requests to coding agents. It builds a taxonomy of information composition and linguistic style from real prompts and creates task variants that differ only in these human factors. The finding that realistic inputs reduce resolution rates and can change model rankings, while adding desired behavior and motivation significantly improves outcomes, gives actionable HCI guidance for how users should phrase requests to AI coding assistants. It is therefore relevant both as a benchmark for AI-assisted software development and as an empirical study of human-AI communication in software tasks.

💡 **[Summary](2608.27831/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.27831)**

## Harness Engineering

### Using Grounded Theory for Agent Behavior Analysis at Scale

**Relevance:** Agent trajectory inspection is central to observability in harness engineering. This paper adapts grounded theory, an auditable qualitative method, to automatically code thousands of agent trajectories and produce behavioral taxonomies and failure modes without relying on pre-built classifiers. The saturation criterion and auditable trail help researchers and developers decide when trajectory analysis is sufficient, and the resulting codebooks improve downstream failure prediction. This demonstrates how a human-centered qualitative method can support debugging and evaluation of agent systems at scale.

💡 **[Summary](2608.30391/)** 📄 **[Full paper](https://arxiv.org/pdf/2608.30391)**

## Human-in-the-Loop Evaluation

### Last Translation Benchmark

**Relevance:** This benchmark places human judgment at the center of evaluation: domain experts and peer review author examples that break leading translation models and handcraft verification rules that expose concrete failure cases. It directly addresses the unreliability of automatic metrics and the reproducibility limitations of conventional human evaluation. The live, continuously contributed dataset also establishes a sustained human-supported evaluation process for tracking progress over time. This is a strong example of human-in-the-loop evaluation methodology for generative systems where standard metrics are nearing saturation.

💡 **[Summary](2609.04173/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.04173)**

### WorldReward: Reward Modeling for Camera-Conditioned World Models

**Relevance:** WorldReward is primarily a reward model, but its evaluation methodology is deeply human-in-the-loop. The authors construct preference data using structured VLM judgments, refine them through tool-based agent auditing and targeted human review, and introduce WorldReward-Bench, a human-annotated benchmark that measures agreement between reward-model preferences and human preferences on action consistency, appearance, and motion quality. This is a hybrid evaluation pipeline in which automated judges are calibrated against human judgment, and it explicitly quantifies agreement gaps between machine and human evaluation.

💡 **[Summary](2609.03952/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.03952)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Systems

**Relevance:** This paper studies the generation and use of synthetic conversational supervision as a stand-in for scarce in-domain human dialogue data. The authors create synthetic CRS conversations from non-conversational signals such as item reviews, metadata, and user-item interactions, and compare selection strategies and domain signals for building this synthetic data. They show that synthetic data can outperform zero-shot prompting and even scarce real dialogues in low-resource settings, while complementing real data when available. These findings are directly relevant to designing, validating, and using simulated user interactions for conversational AI.

💡 **[Summary](2504.15476/)** 📄 **[Full paper](https://arxiv.org/pdf/2504.15476)**

