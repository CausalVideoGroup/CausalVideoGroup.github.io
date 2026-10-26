# Idea Map

Multi-Agent Problems in World Models · 2026-10-26

This map organizes research questions, not an implemented sequence of systems. The terms agent, passive object, learned slot or particle, and camera viewpoint refer to different things.

## 1. Learn separate actions from video

**Given:** visual transitions without per-agent action labels.

**Need:** latent representations that separate changes associated with different entities.

**Core:** FLAM.

**Supporting comparisons:** PlaySlot uses object slots and action prototypes plus continuous variation; LPWM models local stochastic transitions through particles.

**Brief background:** OTF-LAM factorizes local effects and then aggregates a single action representation; GDLAM learns latent groups. Neither establishes that every group is an active agent.

**Boundary:** Decomposition does not guarantee a one-to-one correspondence with agents or true physical commands.

**Next question:** If actions are already supplied, how are they applied to the correct subjects?

## 2. Bind controls to the correct subjects

**Given:** each subject's action or instruction.

**Need:** video in which the correct subject executes that action.

**Core:** ActionParty.

**Supporting comparison:** Incantation uses per-entity language action slots and explores action-semantic reuse across entities.

**Boundary:** These methods use action supervision. Learning separate latent actions and binding known controls are different tasks.

**Next question:** If only some actions are supplied, where do the other characters' actions come from?

## 3. Generate other agents' behavior

**Given:** observation history and externally supplied actions for only part of the scene.

**Need:** behavior for agents whose actions were not specified.

**Core sequence:** COMBAT, then WorldMind.

**Contrast:** COMBAT generates opponent behavior within conditional video prediction. WorldMind explicitly connects compact state estimation, NPC decisions, action conditioning, and video generation.

**Boundary:** An implicit continuation is not an already trained transferable policy. Explicit decisions require suitable state and skill interfaces; the two methods are not a controlled performance ranking.

**Next question:** How can predictions of behavior and consequences help an agent choose its own cooperative action?

## 4. Use imagined futures for cooperative planning

**Given:** partial observations, candidate own actions, and inferred partner actions.

**Need:** a choice among the acting agent's candidate actions.

**Core:** COMBO.

**Mechanism:** Estimate the visual world, generate joint-action consequences, evaluate and search, then execute the selected own action.

**Boundary:** The planner need not control all partners. Different action candidates are different possible futures and can legitimately disagree.

**Next question:** For one chosen world evolution, how can several participants' videos agree on shared facts?

## 5. Maintain one world across views and time

**Given:** multiple local views, action conditions, and history.

**Need:** compatible identities, object states, and event outcomes across viewpoints and revisits.

**Core:** ME-World, with joint generation, shared action conditioning, and shared geometry-aligned memory.

**Supporting comparison:** OverSeer generates fixed auxiliary views as a persistent common reference.

**Brief distributed perspective:** WorldCast coordinates local client generation through shared player state and scene memory.

**Boundary:** A camera is not another agent. Generated auxiliary views are not omniscient observations. Agreement does not by itself demonstrate physical correctness.

**Next question:** Do these identity and information structures still work with more agents?

## 6. Generalize to more agents

**Given:** training scenes with fewer agents than a target inference setting.

**Need:** distinguishable identities and relevant cross-agent information at the larger population.

**Core:** Gamma-World, with a preset identity pool and shared hub communication.

**Supporting comparison:** Multics uses player-group-global communication and dynamic grouping for concurrent interactions.

**Boundary:** Tested population generalization is not unlimited scale, arbitrary online entry and exit, or guaranteed long-term state persistence.

## Cross-cutting comparison axes

- What is supplied: unlabelled video, actions, identity, geometry, skill rules, or history?
- What is inferred: latent actions, binding, behavior, candidate outcomes, shared state, or relations?
- What is the output for: reconstruction, control, decision-making, synchronized views, or population transfer?
- What is evaluated: targeted control, behavioral response, cooperative success, shared events, persistence, or agent-count transfer?
- What remains conditional: training supervision, action format, world coverage, identity capacity, and tested environments?

The six open discussion questions and a clearly labelled diagnostic example appear in the [English summary](summary.html). All fifteen papers are linked and analyzed in [References](references.html).
