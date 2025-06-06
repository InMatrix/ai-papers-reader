---
layout: default
title: 2025-06-06
permalink: /2025-06-06/
---

# 2025-06-06

## Generative AI for Assisting Software Developers

### VisCoder: Fine-Tuning LLMs for Executable Python Visualization Code Generation

**Relevance:** This paper focuses on generating executable Python code for visualization tasks using LLMs. It introduces a large-scale instruction tuning dataset (VisCode-200K) and demonstrates how fine-tuning models with runtime feedback can improve code correctness and visual semantics. This directly addresses code generation, one of the core use cases of generative AI in assisting software developers, making it a highly relevant paper.

💡 **[Summary](2506.03930/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.03930)**

### CASS: Nvidia to AMD Transpilation with Data, Models, and Benchmark

**Relevance:** This paper introduces CASS, a dataset and model suite for cross-architecture GPU code transpilation. It aims to improve code portability, specifically translating CUDA to HIP and Nvidia SASS to AMD RDNA3. This is relevant as it uses generative models for code refactoring and translation, which is a valuable tool for software developers aiming to optimize or adapt code for different platforms.

💡 **[Summary](2505.16968/)** 📄 **[Full paper](https://arxiv.org/pdf/2505.16968)**

## AI Agents

### RiOSWorld: Benchmarking the Risk of Multimodal Compter-Use Agents

**Relevance:** This paper introduces RiOSWorld, a benchmark for evaluating the safety risks of MLLM-based agents that interact with computer systems. It examines how well existing risk mitigation strategies transfer to real-world computer manipulation tasks. The agent's interaction with a digital environment to complete tasks is a key element of AI agent research, making this paper relevant.

💡 **[Summary](2506.00618/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.00618)**

### Small Language Models are the Future of Agentic AI

**Relevance:** This paper argues that small language models (SLMs) are more suitable and economical for many applications in agentic systems, where specialized tasks are performed repetitively. It discusses the potential benefits and barriers to adopting SLMs in agentic systems, and the impact this has on the AI agent industry. Therefore, this paper is highly relevant to AI agent research.

💡 **[Summary](2506.02153/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.02153)**

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games

**Relevance:** This paper presents Orak, a benchmark for training and evaluating LLM agents across diverse video games. It provides a consistent evaluation framework and a fine-tuning dataset for aligning pre-trained LLMs into gaming agents. This is highly relevant as it explores the creation of AI agents that can interact with and perform tasks within simulated environments.

💡 **[Summary](2506.03610/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.03610)**

## Prompt Engineering Techniques

### Video-Skill-CoT: Skill-based Chain-of-Thoughts for Domain-Adaptive Video Reasoning

**Relevance:** This paper introduces Video-Skill-CoT, a framework that automatically constructs and leverages skill-aware Chain-of-Thought (CoT) supervisions for domain-adaptive video reasoning. This is relevant to prompt engineering as it investigates methods for improving the reasoning capabilities of models by crafting specific prompts/CoTs tailored to different skills and domains.

💡 **[Summary](2506.03525/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.03525)**

### FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning

**Relevance:** The paper introduces FinChain, a benchmark for Chain-of-Thought (CoT) financial reasoning. It includes executable Python traces for automated data generation and ChainEval, a metric for evaluating both final answers and intermediate reasoning. This falls under prompt engineering since CoT is a prompting technique to improve reasoning abilities.

💡 **[Summary](2506.02515/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.02515)**

## Human-in-the-loop Machine Learning

### Survey of Active Learning Hyperparameters: Insights from a Large-Scale Experimental Grid

**Relevance:** This paper presents a large-scale study analyzing the impact of different hyperparameters in active learning. It aims to provide recommendations for reproducible active learning experiments, helping practitioners set up active learning effectively. Active learning is a key aspect of human-in-the-loop ML where the model actively seeks human input to improve its performance.

💡 **[Summary](2506.03817/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.03817)**

### DenseDPO: Fine-Grained Temporal Preference Optimization for Video Diffusion Models

**Relevance:** This paper explores Direct Preference Optimization (DPO) for video diffusion models, focusing on obtaining training data through human preferences. It introduces DenseDPO, a method that leverages temporal alignment to label preferences on video segments, improving motion generation. Additionally, the paper shows that VLM-generated labels can be used in place of human labels for training. Both preference elicitation and using models to generate training data fall under the human-in-the-loop paradigm.

💡 **[Summary](2506.03517/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.03517)**

## Techniques for Explaining AI Behavior

### Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis

**Relevance:** This paper tackles data contamination in LLM benchmarks by analyzing shortcut solutions learned by models. It proposes a method for identifying shortcut neurons and an evaluation method called shortcut neuron patching to suppress them, therefore offering insights into model behavior and creating more trustworthy evals. Understanding how and why models make predictions (or overestimate on contaminated datasets) aligns with goals of XAI.

💡 **[Summary](2506.04142/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.04142)**

### Follow the Flow: Fine-grained Flowchart Attribution with Neurosymbolic Agents

**Relevance:** This paper presents FlowPathAgent, a neurosymbolic agent that performs fine-grained post hoc attribution for flowchart analysis. It traces specific components grounding a flowchart referring LLM response to ensure verifiability and improve explainability. The focus on attribution and linking generated responses to specific flowchart elements is directly related to explaining AI behavior.

💡 **[Summary](2506.01344/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.01344)**

### Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning

**Relevance:** This work introduces Rex-Thinker, an object referring model that formulates object referring as an explicit CoT reasoning task. The model aims to provide interpretable reasoning that justifies its predictions and clearly links them to visual evidence. This emphasis on verifiable and trustworthy predictions aligns well with the goals of Explainable AI (XAI).

💡 **[Summary](2506.04034/)** 📄 **[Full paper](https://arxiv.org/pdf/2506.04034)**

