# Key References

Multi-Agent Problems in World Models · Yuxin Wang · 2026-10-26

Literature checked through 2026-10-23. The collection contains seven core readings, five supporting comparisons, two brief latent-action backgrounds, and one distributed-generation perspective. “Read” below means the relevant original problem, method, evaluation, and limitation passages, not a claim that every appendix was read or that results were reproduced. Evidence summaries describe the authors' reported experiments.

The six-part organization is a synthesis for this discussion. It does not imply that the papers form an implemented pipeline. Dates refer to the initial public version where established; a later formal venue is stated separately. Titles and canonical identifiers distinguish papers from similarly named systems.

## 1. Factored Latent Action World Models — FLAM

- **Source and date:** [arXiv:2602.16229](https://arxiv.org/abs/2602.16229), February 2026; [ICML 2026 proceedings](https://proceedings.mlr.press/v306/wang26gs.html). Method discussed: [v2](https://arxiv.org/html/2602.16229v2).
- **Type and role:** Core method; Part 1, multi-agent action learning.
- **Actual problem:** A single scene-level latent action mixes changes from several entities. Can different factors receive separate action channels that support selective manipulation?
- **Mechanism:** Factorize frame features into slots, infer a continuous latent action for each slot from a transition, and predict future features before recombining them. The inverse and forward models can access all current slots, preserving interaction context.
- **Evidence:** Selected-entity manipulation in MultiGrid, prediction in Procgen and nuPlan, and analyses of factor allocation.
- **Boundary:** Correlated entities may share a factor. Some predictive demonstrations infer latent actions from observed future frames; they do not establish autonomous decisions by every entity.
- **Why important / discussion question:** A direct entry into separate action channels. When do the learned factors align with the agents one wants to control?
- **Read:** v2 Sections 2–5 and the relevant control, factorization, and architecture passages of Appendix C.

## 2. ActionParty: Multi-Subject Action Binding in Generative Video Games

- **Source and date:** [arXiv:2604.02330](https://arxiv.org/abs/2604.02330), April 2026; method discussed: [v2](https://arxiv.org/html/2604.02330v2).
- **Type and role:** Core method; Part 2, control binding.
- **Actual problem:** Each player's action is already supplied, but a video generator may apply it to the wrong character or lose the action-to-subject association during interaction.
- **Mechanism:** Subject-state tokens connect actions and coordinates to persistent subject representations. Spatial conditioning helps route controls to the correct regions; the model predicts subject coordinates together with video.
- **Evidence:** Multi-subject control in MeltingPot, including subject-count and long-horizon checks.
- **Boundary:** Training uses action and coordinate supervision. This is not discovery of separate actions from unlabelled video; controllability also does not determine an uncontrolled character's policy.
- **Why important / discussion question:** Isolates the difference between representing an action and binding it to the right actor. How should identity binding be evaluated during occlusion or close interaction?
- **Read:** Sections 1 and 3.1–3.3, coordinate-supervision details, and the relevant subject-count and long-horizon results.

## 3. COMBAT: Conditional World Models for Behavioral Agent Training

- **Source and date:** [arXiv:2603.00825](https://arxiv.org/abs/2603.00825), 2026; method discussed: [v1](https://arxiv.org/html/2603.00825v1).
- **Type and role:** Core method; Part 3, implicit other-agent behavior.
- **Actual problem:** In a two-player fighting game, only Player 1's actions condition the prediction. The model must still generate what the opponent does next.
- **Mechanism:** Condition future video on visual history and Player 1's actions. Opponent behavior is generated within the predicted video, with RGB and RGB-plus-pose variants.
- **Evidence:** Tekken 3 experiments include damage trajectories, action frequencies, and human judgments of responsiveness, beyond image-quality checks.
- **Boundary:** The setting is fixed one-versus-one interaction. Behavioral plausibility is not proof of identifying arbitrary opponent policies or training a transferable standalone policy; policy learning inside the model is discussed as future work.
- **Why important / discussion question:** Shows that leaving an agent's actions unspecified changes the prediction task. Which behavioral tests separate meaningful responses from visually plausible continuation?
- **Read:** Section 3 architecture and conditioning, Section 4 behavioral evaluation, and Section 6 limitations and future work.

## 4. WorldMind: Decoupled Game World Model for State-Aware NPC Behavior

- **Source and date:** [arXiv:2608.21439](https://arxiv.org/abs/2608.21439), August 2026; method discussed: [v1](https://arxiv.org/html/2608.21439v1).
- **Type and role:** Core system; Part 3, explicit state and decision interfaces.
- **Actual problem:** An NPC's next action should depend on the evolving scene and game mechanics, rather than emerge only as an implicit visual continuation.
- **Mechanism:** Estimate compact state from frames and skill history; use that state and skill mechanisms to choose NPC actions; convert decisions to temporally aligned controls for video generation and feed the generated observation back.
- **Evidence:** State-estimation, mechanism-intervention, and closed-loop comparisons in the paper.
- **Boundary:** Training uses engine-state supervision for geometry; skill history and mechanics provide additional information. Not all state is recovered from pixels. Component transfer should not be presented as demonstrated generalization of the entire closed-loop system.
- **Why important / discussion question:** Complements COMBAT by making the behavioral interface inspectable. Which state variables are necessary for useful decisions?
- **Read:** Section 3 interfaces and the relevant Section 4 experiments.

## 5. COMBO: Compositional World Models for Embodied Multi-Agent Cooperation

- **Source and date:** [arXiv:2404.10775](https://arxiv.org/abs/2404.10775), April 2024; [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7d03c6bf9f07acb4038eea96c63db52d-Abstract-Conference.html). Method discussed: [v3](https://arxiv.org/html/2404.10775v3).
- **Type and role:** Core system; Part 4, cooperative planning.
- **Actual problem:** An agent with partial observations must anticipate partners and compare the consequences of its own actions before choosing how to cooperate.
- **Mechanism:** Build and complete a top-down visual estimate from RGBD history; propose own actions and infer partner actions; compose action-conditioned diffusion predictions; evaluate imagined outcomes with tree search; execute the selected own action.
- **Evidence:** Cooperative tasks in TDW-Game, TDW-Cook, and 2D-FetchQ, with component comparisons.
- **Boundary:** The agent does not directly command all partners. Composition occurs within diffusion prediction, not by overlaying separately generated videos, and joint-action conditioning appears in training. Planning can exploit prediction artifacts.
- **Why important / discussion question:** Connects video prediction to decisions. Which prediction failures actually change cooperative success?
- **Read:** Sections 4–5, Section 6.1, and relevant task definitions in Appendix D.

## 6. Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction — ME-World

- **Source and date:** [arXiv:2610.12299](https://arxiv.org/abs/2610.12299), October 2026; method discussed: [v1](https://arxiv.org/html/2610.12299v1).
- **Type and role:** Core method; Part 5, shared worlds and persistence.
- **Actual problem:** Different participants see the same interaction from different positions. Their generated videos must agree on bodies, objects, and the effects of actions.
- **Mechanism:** Jointly generate multiple egocentric streams with one diffusion transformer; project all agents' action conditions into each target view; use geometry-aligned history and reference memory.
- **Evidence:** Synthetic and real two-person interactions, with evaluations of interaction, identity, environment, and state updates.
- **Boundary:** Experiments mainly involve two agents and supplied pose controls. A general formulation for N agents does not establish arbitrary population sizes. Consistent views alone do not prove physically correct dynamics.
- **Why important / discussion question:** Provides a concrete shared-world interface. How should agreement on an event be distinguished from superficial visual similarity?
- **Read:** Sections 3.1–3.4, 4.1–4.3, and limitations.

## 7. Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

- **Source and date:** [arXiv:2605.28816](https://arxiv.org/abs/2605.28816), May 2026; method discussed: [v1](https://arxiv.org/html/2605.28816v1).
- **Type and role:** Core method; Part 6, agent-count generalization.
- **Actual problem:** A model trained with few players should distinguish and coordinate more players at inference without depending on a fixed semantic meaning for each identity slot.
- **Mechanism:** Use distinguishable, symmetrically related identity encodings from a preset pool, randomly assign active identities during training, and organize cross-agent information through shared hub tokens.
- **Evidence:** The paper reports two-player training followed by four-player inference, with identity-encoding comparisons and computational scaling analyses.
- **Boundary:** The identity pool is finite. A scaling curve at a larger population is not, by itself, evidence of generation quality at that population. More-agent inference does not establish arbitrary online entry and exit.
- **Why important / discussion question:** Frames population size as a representation and information-routing problem. What transfers when the number and interaction pattern of agents change?
- **Read:** Sections 3.2–3.3, relevant Section 4 results, and limitations.


## 8. PlaySlot: Learning Inverse Latent Dynamics for Controllable Object-Centric Video Prediction and Planning

- **Source and date:** [arXiv:2502.07600](https://arxiv.org/abs/2502.07600), February 2025; [ICML 2025 proceedings](https://proceedings.mlr.press/v267/villar-corrales25a.html). Relevant version: [v2](https://arxiv.org/html/2502.07600v2).
- **Role:** Supporting comparison in Part 1.
- **Problem and mechanism:** Infer controllable object changes from transitions using frozen SAVi slots. Latent actions combine a discrete prototype with continuous variation. The method includes a scene-level variant and a per-slot variant.
- **Evidence and boundary:** GridShapes tests several moving objects; robot examples largely use a single-action setting. Multiple moving shapes should not be described as multiple autonomous robots.
- **Read:** Sections 3.1–3.5 and 4.1–4.4, with relevant Appendix A/B.2 passages.
- **Comparison question:** What does object-level decomposition add when compared with one global transition code?

## 9. Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling — LPWM

- **Source and date:** [arXiv:2603.04553](https://arxiv.org/abs/2603.04553), March 2026; [ICLR 2026 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cf7ba4b2d14e0f6a0e8247af77745094-Abstract-Conference.html). Relevant version: [v1](https://arxiv.org/html/2603.04553v1).
- **Role:** Supporting comparison in Part 1.
- **Problem and mechanism:** Represent distinct stochastic motions locally through latent particles, per-particle action posteriors, and state-conditioned priors from which future motion can be sampled.
- **Evidence and boundary:** Video prediction and control examples include games and robot-object interaction. A particle is not necessarily a whole object, agent, or independent control command; control demonstrations are mainly single-robot settings.
- **Read:** Sections 1–2, 4, 5.1–5.2, and 6.
- **Comparison question:** How do local uncertainty and agent-specific control differ?

## 10. Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models

- **Source and date:** [arXiv:2605.18601](https://arxiv.org/abs/2605.18601), 2026; relevant version: [v2](https://arxiv.org/html/2605.18601v2).
- **Role:** Supporting comparison in Part 2.
- **Problem and mechanism:** Express heterogeneous character actions through per-entity structured language slots, with temporally localized text conditioning for video generation.
- **Evidence and boundary:** Multi-character game examples and cross-entity action reuse. Labels come from game animation/state information, not unsupervised action discovery. Long-term game logic uses additional event tracking and transition mechanisms.
- **Read:** Section 3.1 and action-interface results; Appendix A6 on labels and A16 on long-term logic.
- **Comparison question:** Which aspects of an action meaning transfer across bodies, and which remain tied to game mechanics?

## 11. OverSeer: Multi-Agent World Models Beyond What Agents See

- **Source and date:** [arXiv:2610.28554](https://arxiv.org/abs/2610.28554), October 2026; relevant version: [v1](https://arxiv.org/html/2610.28554v1).
- **Role:** Supporting comparison in Part 5.
- **Problem and mechanism:** Moving local cameras may lose common state. Jointly generate egocentric streams and fixed auxiliary views, using compressed changes relative to an anchor.
- **Evidence and boundary:** Revisit and regrouping cases in Minecraft and Doom, plus multi-camera examples. Auxiliary streams are generated at inference, not reads of ground-truth hidden state; coverage and scale remain limitations.
- **Read:** Sections 3.1–3.2, relevant Section 4 evaluation, and Appendix E.
- **Comparison question:** What can a generated auxiliary view preserve, and how can its own drift be detected?

## 12. Multics: Generative Multi-Player World Model with Hierarchical Communication

- **Source and date:** [arXiv:2610.17201](https://arxiv.org/abs/2610.17201), October 2026; relevant version: [v1](https://arxiv.org/html/2610.17201v1).
- **Role:** Supporting comparison in Part 6.
- **Problem and mechanism:** With several concurrent interactions, unrestricted global information exchange can mix unrelated events. Player-group-global communication and dynamic grouping organize relevant interactions.
- **Evidence and boundary:** Multiplayer control and interference checks in OpenCS2 and EgoTeam. Communication improvements do not establish persistent shared state over arbitrary durations.
- **Read:** Method overview, relevant Section 3.2–3.3 mechanisms, Sections 4.2–4.4, and Appendix D.
- **Comparison question:** Which interactions should share a local group, and when does information need global access?

## 13. Latent Actions from Factorized Transition Effects under Agent Ambiguity — OTF-LAM

- **Source and date:** [arXiv:2606.30544](https://arxiv.org/abs/2606.30544), June 2026; relevant version: [v2](https://arxiv.org/html/2606.30544v2).
- **Role:** Brief latent-action background in Part 1.
- **Problem and mechanism:** Reduce entanglement between observed transitions, appearance, and embodiment. Learn shared local transition primitives and aggregate them with state and position into one compact continuous latent action.
- **Evidence and boundary:** Appearance and morphology transfer, plus action decoding/control. Decomposing local effects does not produce separate actions for several agents; the final representation remains aggregated.
- **Read:** v2 problem, method, experiments, conclusion, and relevant Appendix B.1–B.3 passages.
- **Comparison question:** What is gained by decomposing effects even when the final action representation is global?

## 14. GDLAM: Group-Disentangled Latent Action Model for Highly Disentangled Embodied Pretraining

- **Source and date:** [arXiv:2609.26118](https://arxiv.org/abs/2609.26118), 2026; [original text](https://arxiv.org/html/2609.26118). Only the year is stated because the recorded first-release metadata is inconsistent.
- **Role:** Brief latent-action background in Part 1.
- **Problem and mechanism:** Separate mixed visual changes into latent groups through multiple stochastic bottlenecks and spatial routing, with sparsity and separation objectives.
- **Evidence and boundary:** Group interventions and swaps, robot-action representations, and downstream transfer. The learned groups need not correspond to agents or identified causal sources; separate multi-agent control is not established.
- **Read:** Grouping/routing method, experiment settings, and relevant limitation and metric passages.
- **Comparison question:** Which evidence would distinguish useful grouping from true agent-aligned actions?

## 15. WorldCast: Distributed Multiplayer World Models

- **Source and date:** [arXiv:2610.12412](https://arxiv.org/abs/2610.12412), October 2026; relevant version: [v1](https://arxiv.org/html/2610.12412v1).
- **Role:** Brief distributed-generation perspective within Part 5.
- **Problem and mechanism:** Let separate clients generate local views while exchanging the player state and generated scene memory needed for a common environment.
- **Evidence and boundary:** Multiplayer Counter-Strike 2 generation and long-horizon checks. Training uses position and map geometry; state estimates can drift. Block-synchronous evaluation does not demonstrate tolerance to arbitrary delays, missing packets, or disconnections.
- **Read:** Relevant system and evaluation passages in Section 5 and Appendix F.
- **Comparison question:** What shared information is sufficient for local generators to agree on the same event?

## Reading connections

The additional readings broaden mechanisms within the six questions; they do not add separate presentation chapters. Compare assumptions before comparing outcomes: unlabelled transitions versus supplied controls, implicit behavior versus explicit decisions, candidate futures versus synchronized views, and tested population sizes versus unrestricted dynamic populations.

[English summary and open questions](summary.html) · [Chinese presentation](presentation.html) · [Discussion overview](./)
