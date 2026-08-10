# Key References

These four papers anchor the talk: general video quality, 3D consistency, revisit consistency, and dynamic out-of-sight consistency. The selection emphasizes narrative value rather than claiming that every paper is the absolute first under every possible definition.

## 1. VBench — Visible Video Quality (2023-11)

https://arxiv.org/abs/2311.17982

VBench established a 16-dimension framework for automatic short-video evaluation and validated each dimension against human preferences. It became the metric lineage reused by many autoregressive and long-video papers.

## 2. WorldScore — 3D Consistency (2025-04)

https://arxiv.org/abs/2504.00983

WorldScore is the 3D benchmark anchor in this narrative. It presents itself as the first unified world-generation benchmark, specifies next-scene generation with camera trajectories, and evaluates geometric stability through DROID-SLAM depth and reprojection errors over co-visible pixels.

## 3. MIND — Revisit Consistency (2026-02)

https://arxiv.org/abs/2602.08025

MIND is the first open-domain, closed-loop revisit benchmark. It uses return trajectories to test long-term memory consistency while covering first- and third-person views, diverse scenes, and generalization across action spaces.

## 4. STEVO-Bench — Dynamic Out-of-Sight Consistency (2026-03)

https://arxiv.org/abs/2603.13215

STEVO-Bench controls observation through occlusion, lights-off instructions, and camera look-away, then checks whether hidden dynamics continue, remain physically plausible, and reappear coherently. It makes decoupling state evolution from observation the benchmark's central question.
