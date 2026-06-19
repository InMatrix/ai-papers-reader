---
layout: default
title: 2026-06-19
permalink: /2026-06-19/
---

# 2026-06-19

## AI for Software Development

### JAMER: Project-Level Code Framework Dataset and Benchmark on Professional Game Engines

**Relevance:** JAMER introduces JamSet and JamBench, focusing on professional game development in the Godot engine. This is highly relevant to HCI because it evaluates code agents' ability to maintain architectural integrity and behavioral alignment (not just syntactic correctness) in highly interactive software environments. HCI researchers can use this benchmark to study the cognitive friction developers experience when collaborating with agents on complex, multi-file codebases, and to design better developer interfaces that bridge the capability cliff identified in larger projects.

📄 **[Full paper](https://arxiv.org/pdf/2606.19830)**

### FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines

**Relevance:** FAPO optimizes multi-step LLM pipelines by editing prompts and modifying chain structure within a codebase. From an HCI perspective, this shift toward autonomous pipeline optimization directly impacts how developers debug and refine AI-infused applications. Instead of manually engineering prompts—a high-cognitive-load trial-and-error process—developers can use FAPO as an automated co-designer. This has strong implications for the design of interactive debugging tools, where the AI suggests structural code and prompt changes, and the human developer acts as a high-level supervisor validating the proposed optimizations.

📄 **[Full paper](https://arxiv.org/pdf/2606.19605)**

### A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets

**Relevance:** This paper introduces a benchmark for next-action prediction in spreadsheets, directly addressing the lack of auto-completion features in end-user programming environments. This is a core HCI topic, as spreadsheets are the most ubiquitous form of programming. The benchmark's online evaluation framework mimics real human-AI collaboration (proposing, accepting/rejecting, and updating actions). HCI researchers can leverage this work to design more intuitive, less intrusive predictive interfaces for non-programmers, studying how the frequency of triggers and the rate of false positives affect user trust and cognitive load during data tasks.

📄 **[Full paper](https://arxiv.org/pdf/2606.13802)**

## AI Agents

### iOSWorld: A Benchmark for Personally Intelligent Phone Agents

**Relevance:** iOSWorld introduces an interactive native iOS simulator benchmark centered on persistent user identity and personalized tasks across multiple apps. This is deeply relevant to HCI, as it moves agent evaluation from isolated, impersonal sandboxes to realistic human-centric scenarios involving personal data (transactions, messages, relationships). Designing phone agents that respect user privacy, understand context, and minimize user disruption requires sophisticated human-agent interaction paradigms. This benchmark enables HCI researchers to evaluate how agents navigate complex user interfaces and personal histories, providing a foundation for designing socially and personally aware mobile assistants.

📄 **[Full paper](https://arxiv.org/pdf/2606.09764)**

### CEO-Bench: Can Agents Play the Long Game?

**Relevance:** CEO-Bench evaluates LLM agents on long-horizon, uncertain, and noisy business simulation tasks over a 500-day period. This benchmark directly tests agents' strategic planning and adaptive decision-making. For HCI, this represents a shift toward evaluating agents as collaborative partners in high-stakes, long-term human endeavors rather than executors of short, isolated tasks. Understanding where agents fail in these complex environments helps HCI researchers design better collaborative interfaces, decision-support visualizations, and intervention mechanisms that allow human operators to guide and correct agents over extended, multi-day workflows.

📄 **[Full paper](https://arxiv.org/pdf/2606.18543)**

### MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents

**Relevance:** Similar to iOSWorld, MyPCBench evaluates computer-use agents acting as personal desktop assistants across simulated real-world web applications seeded with a specific persona. This is highly relevant to HCI because it addresses the gap between impersonal agent evaluation and actual deployment in a user's digital life. The benchmark highlights that agent failures cluster on long trajectories and multi-app tasks where personalization is key. This work highlights the critical need for HCI methods to design interfaces that help users safely delegate, monitor, and correct personalized agent actions across diverse desktop applications.

📄 **[Full paper](https://arxiv.org/pdf/2606.16748)**

## LLM Evaluation Methods

### Re-Centering Humans in LLM Personalization

**Relevance:** This paper directly addresses a major gap in HCI and LLM evaluation: the over-reliance on synthetic data rather than real human feedback for evaluating personalization. By collecting human conversations and multi-stage judgments, the study reveals that models struggle to extract attributes that real users find relevant and often generate personalized responses that humans rate no better than generic ones. This represents a crucial contribution to HCI, emphasizing the limits of automated reward models and the necessity of human-centered evaluation protocols to design personalized systems that truly align with user preferences and trust.

📄 **[Full paper](https://arxiv.org/pdf/2606.06614)**

### Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents

**Relevance:** Leaderboards often fail to predict how LLM agents perform in actual deployments. This paper proposes evaluating agents using predictive validity—the correlation between in-sample and out-of-sample ranks—to capture deployment-relevant dimensions that standard benchmarks collapse. This is highly valuable for HCI, as deploying agents in real-world human environments requires robust, stable, and generalizable performance. By establishing evaluation criteria that better reflect out-of-distribution deployment stability, this work helps HCI researchers and practitioners build more reliable, trustworthy, and predictable agentic systems for human-computer collaboration.

📄 **[Full paper](https://arxiv.org/pdf/2606.19704)**

### Beyond Alignment: Value Diversity as a Collective Property in Multicultural Agent Systems

**Relevance:** While traditional evaluation focuses on how well a single agent aligns with a specific target culture, this paper introduces value diversity as a system-level evaluation axis for multi-agent societies. It reveals that social interaction often erodes cultural diversity, driving agents toward consensus and homogenizing collective decision-making. This has profound implications for HCI and computer-supported cooperative work (CSCW). When humans interact with multi-agent systems, maintaining cultural plurality is vital for fair and representative outcomes. This evaluation framework helps HCI researchers design agent interactions that preserve diverse perspectives in collaborative systems.

📄 **[Full paper](https://arxiv.org/pdf/2606.05985)**

## Reinforcement Learning

### Understanding the Behaviors of Environment-aware Information Retrieval

**Relevance:** This paper studies how LLMs learn to adapt their query formulation strategies for different retrievers using reinforcement learning, finding that incorporating retriever-specific human guidance enhances performance. This is highly relevant to HCI and information retrieval (IR). By showing that optimal query styles vary significantly, the research highlights the difficulty users face when manually querying different systems. Applying these RL insights can help HCI researchers design intelligent search interfaces that automatically translate user intent into retriever-optimized queries, reducing the cognitive load on users and facilitating more intuitive human-AI search collaboration.

📄 **[Full paper](https://arxiv.org/pdf/2606.16817)**

### From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning

**Relevance:** This work proposes an LLM-as-Environment-Engineer framework where an LLM policy analyzes failure trajectories and automatically redesigns the next training environment configuration. In HCI, designing effective training environments (or curricula) for AI agents often requires substantial human expert labor. Automating this process via LLMs allows for more adaptive and personalized agent training. HCI researchers can benefit from this framework to design co-creative systems where human designers and LLM environment engineers collaboratively build, test, and refine interactive environments, game levels, or simulation tasks.

📄 **[Full paper](https://arxiv.org/pdf/2606.17682)**

### Learning User Simulators with Turing Rewards

**Relevance:** Turing-RL uses a reinforcement learning approach to train user simulator models based on a discriminative Turing reward (indistinguishability from real human responses). User simulators are extremely valuable in HCI for prototyping interfaces, evaluating personalization systems, and training conversational agents without exhausting human testers. By optimizing for conversational indistinguishability rather than exact response matching, this RL method produces highly realistic user simulators. This enables HCI researchers to conduct scalable, automated user studies and usability testing of interactive systems before deploying them to real users.

💡 **[Summary](2606.19336/)** 📄 **[Full paper](https://arxiv.org/pdf/2606.19336)**

## Explainable AI

### Thinking with Visual Grounding

**Relevance:** This paper introduces visually grounded thinking, where vision-language models interleave natural-language reasoning with explicit point or box groundings of visual evidence. This is a significant advancement for Explainable AI (XAI) and HCI. Traditional VLM reasoning traces are purely textual, leaving visual evidence implicit and hard for users to verify. By physically pointing to or bounding the image regions that justify each step of reasoning, the model provides highly interpretable, visual explanations of its thoughts. This directly enhances user trust, reduces cognitive load, and enables more effective human-in-the-loop verification of multimodal AI decisions.

📄 **[Full paper](https://arxiv.org/pdf/2606.16122)**

### Bag of Dims: Training-Free Mechanistic Interpretability via Dimension-Level Sign Patterns

**Relevance:** Bag of Dims presents a training-free mechanistic interpretability framework showing that the standard basis of transformer hidden states acts as independent binary registers encoding semantic concepts. This provides a remarkably simple and scalable way to extract human-readable features without expensive optimization. For XAI and HCI, this enables the development of real-time, lightweight explanation interfaces that can show users exactly which semantic concepts are active in a model's hidden states during a live forward pass. It also facilitates interactive steering, allowing users to directly inspect and manipulate model concepts.

📄 **[Full paper](https://arxiv.org/pdf/2606.12629)**

### SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior

**Relevance:** This paper investigates the limits of Sparse Autoencoders (SAEs) for model steering and safety interventions, showing that suppressing unsafe SAE features does not guarantee behavioral compliance because the model can recover the behavior through unexplained residuals. This has critical implications for XAI and AI safety. In HCI, designers rely on explanations and steering controls to build trust and ensure safety. This research warns that feature-level explanations and interventions can create a false sense of security. It highlights the need for more comprehensive, behavior-level evaluation tools in interactive steering interfaces.

📄 **[Full paper](https://arxiv.org/pdf/2606.18322)**

