# Key References

这四篇作为演讲主线锚点，分别代表通用视频质量、3D consistency、revisit consistency 与动态 out-of-sight consistency。这里强调叙事代表性，不主张每篇都是所有口径下的绝对最早工作。

## 1. VBench — visible video quality（2023-11）

https://arxiv.org/abs/2311.17982

奠定 16 个维度的短视频自动评测框架，并用逐维人工偏好数据验证 human alignment。它是后续大量 AR 与长视频论文的 metric lineage。

## 2. WorldScore — 3D consistency（2025-04）

https://arxiv.org/abs/2504.00983

这条叙事中的 3D benchmark 锚点。WorldScore 自称首个统一的 world-generation benchmark，用相机轨迹定义 next-scene generation，并以 DROID-SLAM 深度和共视像素重投影误差测几何稳定性。

## 3. MIND — revisit consistency（2026-02）

https://arxiv.org/abs/2602.08025

首个 open-domain、closed-loop revisited benchmark。它用闭环回访测试长期记忆一致性，同时覆盖第一／第三人称、不同场景与动作空间泛化。

## 4. STEVO-Bench — dynamic out-of-sight consistency（2026-03）

https://arxiv.org/abs/2603.13215

通过遮挡、关灯和 camera look-away 控制观察，再检查不可见期间的动态演化是否继续、是否物理合理、重新出现后是否连贯。它把状态演化与观察解耦明确变成 benchmark 的核心问题。
