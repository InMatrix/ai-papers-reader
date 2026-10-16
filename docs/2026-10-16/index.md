---
layout: default
title: 2026-10-16
permalink: /2026-10-16/
---

# 2026-10-16

## AI for Software Development

### MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering

**Relevance:** Trains an agentic model to autonomously carry out long-horizon machine learning engineering: writing and running code, organizing experiments, and adapting based on execution feedback. This is a direct instance of AI assisting or automating software and ML development workflows. Its interaction harness for model-directed experimentation and its evaluation on MLE-Bench make it relevant to the software-engineering use case, though the focus is on post-training rather than developer-facing tools.

💡 **[Summary](2610.22344/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.22344)**

### FDE-Gym: The Last Mile of AI Delivery

**Relevance:** Benchmarks agents on end-to-end delivery tasks in which they must modify live customer systems and produce working software solutions. It covers requirement clarification, debugging-like operation of production-like systems, and verification of outcomes. This extends AI-for-software-development beyond isolated coding tasks to real engineering delivery, and it highlights where current agents fail to uncover unstated constraints.

📄 **[Full paper](https://arxiv.org/pdf/2610.22350)**

## Harness Engineering

### Self-Evolving Agent Harness

**Relevance:** Directly addresses harness engineering by formalizing how prompts, memory, workflows, tools, and code in an agent's scaffold are revised across runs while model weights stay fixed. It distinguishes update targets and proposal/admission mechanisms, and it discusses governance, independent validation, and runtime privileges. These are central concerns for human oversight and for who may change harness components.

💡 **[Summary](2610.18813/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.18813)**

### CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness

**Relevance:** Presents a harness made of editable artifacts (tools, skills, and execution code) that is co-evolved from execution feedback while model weights are frozen. This matches the topic's focus on editable harness artifacts and on improving the harness from observed behavior. The paper is primarily a method, so its human-in-the-loop and observability aspects are less developed.

💡 **[Summary](2610.21910/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.21910)**

## Human-in-the-Loop Evaluation

### RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment

**Relevance:** Compares model performance against a study with 20 undergraduate participants on the same interactive tasks. It analyzes differences between human and model progress at matched states, including image-space versus pose-space judgments. The human baseline and the behavioral analysis make it a measurement of human-machine agreement in an interactive evaluation.

📄 **[Full paper](https://arxiv.org/pdf/2610.17665)**

## Human-AI Collaboration

No paper recommendations for this topic.

## Simulated Users

### Cowork-Gym: Synthesizing Interactive Work Environments at Scale

**Relevance:** Introduces a stateful user simulator that responds to the agent through dialogue and direct edits to the shared workspace, reproducing realistic cowork dynamics. The simulator is used to train and evaluate agents, which is the central use case of simulated users. The paper does not validate the simulator against real human behavior, which is a gap for this topic.

💡 **[Summary](2610.17670/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.17670)**

### FDE-Gym: The Last Mile of AI Delivery

**Relevance:** Uses scripted stakeholders that respond to agent messages, trial runs, and waiting time in simulated customer environments. These stand-ins model customers who reveal unstated constraints only through interaction, and the penalties for stakeholder interactions make the simulated user part of the evaluation. It is a benchmark-oriented use of simulated people rather than a fidelity study.

📄 **[Full paper](https://arxiv.org/pdf/2610.22350)**

