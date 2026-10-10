---
layout: default
title: 2026-07-24
permalink: /2026-07-24/
---

# 2026-07-24

## AI for Software Development

### Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction

**Relevance:** Presents a multi-domain benchmark for coding agents spanning repository-level engineering, front-end development, office workflows, and security. Tasks are reverse-engineered from real commits and pull requests, and the suite runs on two agent harnesses (CodeBuddy Code and Claude Code). It directly evaluates AI-assisted software development and is useful for understanding how coding agents perform on realistic developer work.

💡 **[Summary](2607.20911/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.20911)**

### ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders

**Relevance:** Evaluates coding agents that turn fuzzy product requirements into working software through clarification, planning, and debugging. It grounds ambiguity in real open-source repositories and uses multi-dimensional diagnostics, including functional correctness and design quality. It targets the vibe-coding workflow that is central to modern AI-assisted software development.

💡 **[Summary](2607.21217/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.21217)**

### NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

**Relevance:** Proposes an agent framework in which an agent is a Python object, with methods as actions, fields as state, and docstrings as prompts. Because agent code is testable, traceable, and refactorable like ordinary software, it fits developer workflows. It is evaluated on SWE-bench Verified, a software-engineering benchmark.

💡 **[Summary](2607.20709/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.20709)**

## Harness Engineering

### AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents

**Relevance:** Directly addresses observability and debugging of the agent harness. It provides a Detect-Attribute-Recover-Rerun loop, trajectory-based root-cause diagnosis, a Python library, CLI, web console, and a shareable Error Hub. This matches the emphasis on inspecting why an agent acted as it did and on making failures actionable for operators.

💡 **[Summary](2607.18754/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.18754)**

### DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines

**Relevance:** Builds a platform where an agent constructs editable pipeline artifacts, with DataFlow-Skills as procedural guidance and a WebUI that syncs conversational authoring with a visual DAG editor. The persistent, editable, inspectable workflow is a clear example of a harness that humans can compose, steer, and version.

💡 **[Summary](2607.16617/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.16617)**

### NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

**Relevance:** Makes agent behavior testable, traceable, and refactorable through a programming model in which prompts, state, and actions live in one object. It also exposes model-callable harness APIs for context and events, which supports editable and inspectable harness components.

💡 **[Summary](2607.20709/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.20709)**

## Human-in-the-Loop Evaluation

### EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration

**Relevance:** Centers evaluation methodology on expert studies that compare an LLM judge's reliability with human experts. Expert feedback improves scoring accuracy, and experts can detect unreliable outputs, which reflects a hybrid pipeline in which humans calibrate and audit an automated judge.

💡 **[Summary](2607.18529/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.18529)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders

**Relevance:** Uses an automated User Agent to simulate a user who gradually reveals hidden constraints from a fuzzy requirement. The paper explicitly designs the simulator to be reproducible and to avoid inventing new requirements or leaking implementation details, so it addresses simulator fidelity and reliability in interactive evaluation.

💡 **[Summary](2607.21217/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.21217)**

### EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration

**Relevance:** Conditions its evaluation on learner personas and includes learner-persona analyses. This is a persona-based stand-in for different learners, and the paper also examines how well such simulated assessments match human experts.

💡 **[Summary](2607.18529/)** 📄 **[Full paper](https://arxiv.org/pdf/2607.18529)**

