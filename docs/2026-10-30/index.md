---
layout: default
title: 2026-10-30
permalink: /2026-10-30/
---

# 2026-10-30

## AI for Software Development

### Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models

**Relevance:** Builds a benchmark of 273 coding tasks drawn from real user coding sessions, where agents must turn multimodal requests (image, audio, video, documents) into working application revisions. It targets the gap between partial requirement satisfaction and complete task success, and grades results with acceptance criteria, browser evidence, and a verifier. This directly addresses how well coding assistants support real developers' edits and repository-level changes, which is central to AI-assisted software development.

💡 **[Summary](2610.35138/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.35138)**

### VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team

**Relevance:** Presents an end-to-end pipeline in which LLM agents generate complete 2D game projects from natural-language prompts. It coordinates code, scenes, assets, physics, and configurations, and uses an adversarial review loop where implementation and review are separated. The framework also distills accepted projects into reusable modules, which is a practical instance of AI-assisted development workflows and code reuse.

💡 **[Summary](2610.33106/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.33106)**

### Scaling Lean Theorem Proving for Real-World Code Verification

**Relevance:** Applies automated proving to verification of real implementations by translating Rust programs into Lean and generating specifications with proofs or refutations. It targets implementation-level obligations such as fixed-width arithmetic and mutation, which are the kinds of correctness issues developers face when writing code. This connects formal verification to practical code quality assurance and bug finding.

💡 **[Summary](2610.38174/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.38174)**

## Harness Engineering

### Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents

**Relevance:** Shows that the interface layer between an agent and its tools (MCP versus CLI) changes behavior, failure pathways, and recovery even when capabilities are matched. It proposes a Decoupled Action Realization and Targeted Repair method that fixes interface-specific issues while preserving semantic commitments. This treats the tool-facing harness as an editable, inspectable artifact that teams can diagnose and improve, which is central to harness engineering.

💡 **[Summary](2610.34298/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.34298)**

## Human-in-the-Loop Evaluation

No paper recommendations for this topic.

## Human-AI Collaboration

### RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents

**Relevance:** Evaluates CLI agents not only on task completion but also on collaboration quality during execution. A paired comparison introduces progressive information, corrections, constraint revisions, and authorization decisions from a user. It highlights gaps in steerability, trust calibration, and safety-boundary management, which are core concerns for human-agent teaming and oversight.

💡 **[Summary](2610.22507/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.22507)**

## Simulated Users

### PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas

**Relevance:** Uses a persona agent with 44 profiles to stand in for users, rewriting task instructions in each user's own words and answering the agent's clarifying questions over multiple turns. Comparing persona-driven runs with the original requests shows a 36% drop in completion and lower satisfaction. It directly studies how simulated users change agent evaluation outcomes.

💡 **[Summary](2610.22990/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.22990)**

### RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents

**Relevance:** Uses a scripted user that delivers progressive information, corrections, and authorization decisions during CLI execution. This simulated user is a controlled stand-in for real collaborators in an interactive evaluation, enabling reproducible measurement of collaboration quality.

💡 **[Summary](2610.22507/)** 📄 **[Full paper](https://arxiv.org/pdf/2610.22507)**

