---
layout: default
title: 2024-07-12
permalink: /2024-07-12/
---

# 2024-07-12

## AI for Software Development

### InverseCoder: Unleashing the Power of Instruction-Tuned Code LLMs with Inverse-Instruct

**Relevance:** This paper tackles the challenge of improving instruction-tuned code LLMs by generating high-quality training data directly from code snippets (Inverse-Instruct). From an HCI perspective, enhancing the instruction-following capability of code generation tools like Copilot is paramount for developer productivity and trust. By enabling the model to better align natural language descriptions with formal code, this research directly improves the usability and effectiveness of AI tools used daily by software engineers.

💡 **[Summary](2407.05700/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.05700)**

### On Leakage of Code Generation Evaluation Datasets

**Relevance:** Reliable evaluation is foundational for developing trustworthy AI assistance tools. This work identifies critical contamination issues (direct leakage, synthetic data, overfitting) within code generation evaluation datasets. For the HCI community, these findings emphasize the necessity of rigorous, uncontaminated benchmarks to accurately measure the true generalization capability of AI coding assistants, ensuring that developers can rely on these tools in real-world, novel scenarios rather than relying on models that merely memorize test cases.

💡 **[Summary](2407.07565/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.07565)**

## AI Agents

### Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence

**Relevance:** This paper introduces the Internet of Agents (IoA) framework, addressing the fundamental challenge of integrating diverse, capable, third-party agents into scalable multi-agent systems. This framework is crucial for future HCI scenarios where users interact with complex agent ecosystems. IoA’s focus on flexible integration protocols and dynamic conversation flow control directly enables sophisticated human-agent teaming, allowing agents to coordinate dynamically to solve user-defined goals.

💡 **[Summary](2407.07061/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.07061)**

### This&That: Language-Gesture Controlled Video Generation for Robot Planning

**Relevance:** This work is highly relevant to HCI and embodied agents as it focuses on intuitive human-robot communication for task planning. By using language and gestures to condition video generation (which acts as the robot’s plan), the authors tackle the challenge of unambiguous instruction in complex environments. This research demonstrates a clear methodology for designing interfaces where human input directly and controllably guides an agent's reasoning and subsequent physical actions.

💡 **[Summary](2407.05530/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.05530)**

### Flash-VStream: Memory-Based Real-Time Understanding for Long Video Streams

**Relevance:** Effective autonomous agents require continuous, real-time perception and long-term memory to operate in dynamic environments. Flash-VStream addresses this by proposing a memory-based VLM architecture that handles extremely long video streams with low latency. This is essential for agents interacting with continuous user activity or environments, enabling real-time response to asynchronous queries and simulating the 'working memory' capability needed for seamless, responsive human-agent interaction.

💡 **[Summary](2406.08085/)** 📄 **[Full paper](https://arxiv.org/pdf/2406.08085)**

## LLM Evaluation Methods

### Evaluating Language Model Context Windows: A "Working Memory" Test and Inference-time Correction

**Relevance:** This paper presents SWiM, an evaluation framework that tests the robustness of long-context LLMs, confirming the critical 'lost-in-the-middle' effect which undermines user trust. Crucially, it proposes 'medoid voting,' a simple, training-free inference-time correction. This approach directly benefits HCI by offering a practical mitigation strategy to improve the reliability and perceived competence of LLMs when users input large amounts of contextual information.

💡 **[Summary](2407.03651/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.03651)**

### MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for Text-to-Image Generation?

**Relevance:** This work addresses the evaluation of multimodal reward models (judges) essential for aligning generative AI (T2I) with human preferences regarding safety, quality, and bias. MJ-Bench provides a rigorous benchmark for assessing the reliability of these automated judges. This is vital for HCI research focused on alignment and ethical evaluation, ensuring that models are trained using feedback mechanisms that accurately reflect nuanced human values and desired user outcomes.

💡 **[Summary](2407.04842/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.04842)**

### Multi-Object Hallucination in Vision-Language Models

**Relevance:** This paper systematically investigates multi-object hallucination, a significant failure mode impacting model reliability and user trust. By introducing the ROPE evaluation protocol, the authors provide a method to quantify how LVLMs misperceive complex scenes. Understanding and measuring these robustness failures is a critical step for HCI researchers aiming to design safer multimodal interfaces and developing techniques to alert users when a model is operating under high uncertainty.

💡 **[Summary](2407.06192/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.06192)**

## Reinforcement Learning

### BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark

**Relevance:** BiGym introduces a new benchmark and environment crucial for advancing Reinforcement Learning (RL) and imitation learning in complex, real-world robotic tasks. The inclusion of human-collected demonstrations for 40 diverse bi-manual tasks directly connects RL research with HCI, focusing on how agents can effectively learn complex policies from human guidance (demo-driven RL). This infrastructure facilitates the design of RL systems capable of safe and effective human-agent collaboration.

💡 **[Summary](2407.07788/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.07788)**

### This&That: Language-Gesture Controlled Video Generation for Robot Planning

**Relevance:** This paper integrates human instruction (language and gesture) into robotic planning, leveraging behavioral cloning (a form of imitation learning/RL). The work explores how explicit human communication can serve as effective supervision for policy learning, directly addressing the HCI challenge of providing intuitive guidance to complex agents. Video generation acts as a verifiable intermediate representation, potentially aiding interpretability and policy refinement.

💡 **[Summary](2407.05530/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.05530)**

## Explainable AI

### How do you know that? Teaching Generative Language Models to Reference Answers to Biomedical Questions

**Relevance:** This paper addresses XAI by enhancing the transparency and reliability of LLM outputs in sensitive domains (biomedicine). By implementing a Retrieval-Augmented Generation (RAG) system that explicitly references generated statements back to verifiable sources (PubMed abstracts), it tackles the critical HCI concern of user trust. This mechanism provides users with the necessary context and provenance to verify answers, moving beyond opaque generation to accountable factuality.

💡 **[Summary](2407.05015/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.05015)**

### Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps

**Relevance:** Lookback Lens is a novel XAI technique that uses attention mechanisms—an intrinsic model component—to detect and mitigate contextual hallucinations. By calculating the ratio of attention on context versus generated tokens, it provides a measurable, interpretable signal of where the model is drawing information. This interpretability allows for classifier-guided decoding, offering a transparent way to improve reliability and directly inform users about the confidence/source of specific outputs.

💡 **[Summary](2407.07071/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.07071)**

### Understanding Visual Feature Reliance through the Lens of Complexity

**Relevance:** This paper provides fundamental insights into model interpretability by quantifying the complexity of learned features using V-information. Understanding whether a model relies on 'simple' (shortcut) or 'complex' features is crucial for diagnosing shortcut learning and ensuring robust decision-making. These findings enable HCI researchers to better understand and visualize *what* a model sees and relies on, fostering the development of more trustworthy and transparent AI systems.

💡 **[Summary](2407.06076/)** 📄 **[Full paper](https://arxiv.org/pdf/2407.06076)**

