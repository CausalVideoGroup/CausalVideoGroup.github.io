# Key References

## 1. From Slow Bidirectional to Fast Autoregressive Video Diffusion Models

- Link: https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html
- Type: method
- Why important: It provides the starting recipe for distilling a bidirectional video diffusion teacher into a fast autoregressive student.
- Role in this topic: Foundation of the forcing-method timeline.
- Main limitation: Teacher-conditioned training does not fully reproduce the student's inference-time history distribution.
- Discussion question: Which teacher information is fundamentally unavailable to a causal student?

## 2. Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion

- Link: https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html
- Type: method
- Why important: It trains on student rollouts and directly targets the train-test history mismatch.
- Role in this topic: Central transition from teacher-forced history to on-policy autoregressive distillation.
- Main limitation: Correcting rollout distribution does not by itself resolve teacher/student causal-architecture mismatch or long-context degradation.
- Discussion question: How much student rollout is needed before on-policy training becomes stable and informative?

## 3. Causal Forcing

- Link: https://arxiv.org/abs/2602.02214
- Type: method
- Why important: It argues that the initialization teacher must itself be autoregressive to define the correct causal flow map.
- Role in this topic: Architectural correction following Self Forcing.
- Main limitation: Adding an autoregressive teacher increases training complexity and does not automatically solve long-horizon memory cost.
- Discussion question: Can the causal target be recovered without training a separate autoregressive teacher?
