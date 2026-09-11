---
layout: default
title: 2026-09-11
permalink: /2026-09-11/
---

# 2026-09-11

## AI for Software Development

### SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents

**Relevance:** This paper directly addresses evaluation of software engineering agents, a core application of AI for software development. It identifies reward hacking and task quality issues in SWE-Bench Pro, then introduces anti-hacking safeguards and refined tasks. For HCI, it has implications for trust, reliability, and developer oversight when integrating coding agents into real workflows. By exposing overestimated capabilities, it helps teams design better human-in-the-loop review and verification practices around AI coding assistants, ensuring deployment decisions are based on trustworthy benchmarks rather than inflated agent performance.

💡 **[Summary](2609.08149/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.08149)**

### Diffs vs. Whole Files: An Empirical Comparison of Iterative Edit-Based and Direct Generation for Flutter/Dart Code Models

**Relevance:** This paper compares iterative diff-based code editing against direct whole-file generation for Flutter/Dart code models. It is highly relevant to AI for software development because it studies how code models should output edits, a design choice that affects developer experience, review burden, and assistant usability. The finding that diff-based generation wins mainly on short, localized tasks such as refactoring and error-handling has direct implications for HCI: tool builders should align generation regimes with task locality and developer editing workflows, and design interfaces that make localized, reviewable changes easier to inspect and accept.

💡 **[Summary](2609.05779/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.05779)**

### T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks

**Relevance:** T1 trains a 122B MoE agent to operate a real shell for long-horizon coding and scientific tasks across hundreds of tool calls. It is relevant to AI for software development because it advances autonomous coding and terminal agents, which increasingly assist developers with repository-level tasks. For HCI, it raises questions about oversight, debugging, and trust in long-horizon agents: how developers inspect trajectories, interrupt or correct agents, and allocate control. Its benchmark results and training recipe also inform how future coding assistants might be evaluated and integrated into developer workflows.

💡 **[Summary](2609.11042/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.11042)**

## Harness Engineering

### EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents

**Relevance:** EvoSafeHarness directly contributes to harness engineering by synthesizing deployable safety harnesses for frozen LLM agents. It jointly searches natural-language policy and executable code logic, adapting enforcement to specific models and domains. This is exactly the operational scaffold around a model, including prompts, policies, and execution hooks, that determines agent reliability. For HCI, it provides a platform for inspecting, versioning, and improving safety harnesses, and for understanding how much enforcement a deployment needs before utility declines. Its adversarial review and transfer analysis also support observability and governance of agent behavior in target environments.

💡 **[Summary](2609.05903/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.05903)**

### AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems

**Relevance:** AgentGrad optimizes prompts for multi-agent systems, treating prompts as editable harness artifacts. It uses sequential intervention to identify the agent whose modification resolves a failure, extracts agent-level textual gradients, and clusters semantically similar gradients to avoid mixing failure modes. This is relevant to harness engineering because it offers a method to debug and repair prompt-based harnesses from observed agent behavior. For HCI, it supports human operators who need to understand which agent or prompt caused a failure and how to make targeted, generalizable prompt changes, improving the inspectability and maintainability of multi-agent scaffolds.

💡 **[Summary](2609.08572/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.08572)**

## Human-in-the-Loop Evaluation

### DF26: We Cannot Tell Fake From Real Anymore

**Relevance:** DF26 is a benchmark for detecting AI-generated videos that explicitly measures human performance alongside state-of-the-art detectors. It shows both humans and detectors are near chance, motivating better evaluation protocols under generative model distribution shifts. This is relevant to human-in-the-loop evaluation because it treats people as evaluators or detectors of AI-generated content and compares human versus machine judgments. The benchmark highlights the limits of current automated evaluation and the need for human-centered protocols that measure robustness, calibration, and agreement between human and machine assessments in high-stakes media authenticity tasks.

💡 **[Summary](2609.07369/)** 📄 **[Full paper](https://arxiv.org/pdf/2609.07369)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

No paper recommendations for this topic.

