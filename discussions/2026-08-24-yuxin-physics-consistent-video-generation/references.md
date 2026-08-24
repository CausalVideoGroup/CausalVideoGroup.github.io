# Key References

These six papers anchor the talk's main routes: explicit simulation, post-training, representation alignment, verifiable reward, inference-time alignment, and law-level evaluation.

## 1. PhysGen: Rigid-Body Physics-Grounded Image-to-Video Generation

- Link: https://arxiv.org/abs/2409.18964
- Type: system
- Why important: It connects single-image understanding, rigid-body simulation, and diffusion refinement.
- Role in this topic: Representative of computing physical evolution outside the video generator.
- Main limitation: Hidden geometry, material, contact, and force are not uniquely recoverable from one image.
- Discussion question: How should the system represent multiple plausible initial states?

## 2. What about gravity in video generation? Post-Training Newton's Laws with Verifiable Rewards

- Link: https://arxiv.org/abs/2512.00425
- Type: method
- Why important: It converts measurable motion proxies and Newtonian structure into post-training rewards.
- Role in this topic: Representative of moving from general preference feedback toward verifiable physical constraints.
- Main limitation: Reliable measurement requires controlled phenomena, so coverage narrows as verification becomes stricter.
- Discussion question: Which additional laws can become reliable rewards without sacrificing broad scene coverage?

## 3. PISA Experiments: Exploring Physics Post-Training for Video Diffusion Models by Watching Stuff Drop

- Link: https://arxiv.org/abs/2503.09595
- Type: method
- Why important: Controlled free fall reveals both post-training gains and weak extrapolation.
- Role in this topic: Diagnostic anchor for separating behavior teaching from rule learning.
- Main limitation: The model may fit falling-video statistics without learning a transferable gravity mechanism.
- Discussion question: Which split best rules out memorized falling templates?

## 4. VideoREPA: Learning Physics for Video Generation through Relational Alignment with Foundation Models

- Link: https://arxiv.org/abs/2505.23656
- Type: method
- Why important: It distills token relations from a video-understanding model into a generator.
- Role in this topic: Representative of using learned representations as a physics teacher.
- Main limitation: Teacher features may encode visual-motion statistics rather than intervenable physical state.
- Discussion question: Which counterfactual test can separate physics from visual correlation?

## 5. Inference-time Physics Alignment of Video Generative Models with Latent World Models

- Link: https://arxiv.org/abs/2601.10553
- Type: system
- Why important: WMReward scores candidate trajectories with a frozen latent world model.
- Role in this topic: Representative of improving outputs through inference without updating generator weights.
- Main limitation: Better candidates must already exist, the proxy can fail, and search adds cost.
- Discussion question: How should generator, verifier, and test-time-compute gains be separated?

## 6. Evaluating Newtonian Mechanics in Video Generative Models with Real Physical Systems

- Link: https://arxiv.org/abs/2504.02918
- Type: benchmark
- Why important: Morpheus checks extracted trajectories against equations and physical invariants.
- Role in this topic: Representative of moving from plausibility judgments to law-level measurement.
- Main limitation: Controlled rigid-body scenes and trajectory-extraction error restrict coverage.
- Discussion question: Which non-rigid phenomena admit useful measurable invariants?
