# Key References

## 1. HoloCine: Holistic Generation of Cinematic Multi-Shot Long Videos

- Link: https://arxiv.org/abs/2510.20822
- Type: method
- Why important: It extends joint multi-shot generation toward minute-scale narratives with sparse inter-shot self-attention.
- Role in this topic: Representative of the holistic-joint route and its scaling strategy.
- Main limitation: The full storyboard is planned before generation, and sparse summaries may omit fine-grained distant state.
- Discussion question: Which cross-shot facts require dense token interaction rather than summary communication?

## 2. OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory

- Link: https://arxiv.org/abs/2512.07802
- Type: method
- Why important: It retrieves relevant frames from the full history and compresses them into a compact context for the current shot.
- Role in this topic: Clear example of caption-guided visual memory in shot-level autoregressive generation.
- Main limitation: Retrieval quality depends on the current caption and may discard state whose relevance becomes clear only later.
- Discussion question: How should memory preserve latent causal state that is not explicitly named in the next-shot caption?

## 3. ShotStream

- Link: https://arxiv.org/abs/2603.25746
- Type: method
- Why important: It connects a bidirectional next-shot teacher to a causal student designed for real-time multi-shot output.
- Role in this topic: Representative bridge from shot-conditioned diffusion to causal streaming and few-step inference.
- Main limitation: Causal rollout cannot use future shots to repair past output and may accumulate appearance or motion drift.
- Discussion question: Which teacher signals survive causal distillation when the student leaves the teacher's history distribution?

## 4. VideoMemory

- Link: https://arxiv.org/abs/2601.03655
- Type: system
- Why important: It externalizes character, prop, and background state into a dynamic memory bank used throughout shot-by-shot generation.
- Role in this topic: Representative of explicit semantic state management outside a single video context window.
- Main limitation: A memory bank can preserve references without diagnosing whether the generated shot actually obeyed them.
- Discussion question: What verification signal should decide whether a generated frame is safe to write back into memory?

## 5. GroundShot

- Link: https://arxiv.org/abs/2606.20799
- Type: system
- Why important: It joins shot scheduling, entity grounding, reference verification, and memory updates into a visual-feedback loop.
- Role in this topic: Representative of the shift from open-loop planning to online directing.
- Main limitation: Additional planning and verification stages increase latency and can compound errors from imperfect evaluators.
- Discussion question: When should a director agent reorder shots, regenerate a shot, or repair the memory instead?

## 6. MSVBench

- Link: https://arxiv.org/abs/2602.23969
- Type: benchmark
- Why important: It evaluates multi-shot video systems with hierarchical scripts and references across a broad method set.
- Role in this topic: Evidence that multi-shot evaluation is becoming a distinct problem rather than an extension of generic video quality.
- Main limitation: One benchmark cannot simultaneously isolate cinematic language, delayed entity recurrence, online control, and audio-visual consistency.
- Discussion question: What controlled interventions are needed to identify the source of a cross-shot failure?
