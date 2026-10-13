# Key References

The deck covers 26 papers in publication order. The eight below carry the main arguments; the full list follows. All numbers are taken from the papers and are shown with their charts in the presentation.

## 1. Video models are zero-shot learners and reasoners (Veo3-ZS)

- Link: https://arxiv.org/abs/2509.20328
- Type: problem
- Why important: It made the first broad claim that a video model (Veo 3) can solve mazes, puzzles and physical tasks from only a first frame and a text instruction, and named the mechanism "chain-of-frames".
- Role in this topic: The starting point. Most later papers either build benchmarks to test this claim or argue with its mechanism.
- Main limitation: The paper itself frames its scores as a lower bound; the same team's follow-up (VIPE) raises them by changing only the input image.
- Discussion question: Is "the answer grows frame by frame" a description of the output or of the computation?

## 2. Thinking with Video: Video Generation as a Promising Multimodal Reasoning Paradigm

- Link: https://arxiv.org/abs/2511.04570
- Type: benchmark
- Why important: With Wan 2.5, turning off the API's prompt rewriter drops GSM8K accuracy from 78.4 to 0: the rewritten prompt already contains the answer.
- Role in this topic: Anchors the question of who does the reasoning. Of the 26 papers, 13 used a closed API without mentioning its built-in rewriter.
- Main limitation: Sora-2's rewriter cannot be turned off, so its text-task scores cannot be attributed to the video model.
- Discussion question: Which evaluation settings should be mandatory to report (rewriter on or off, exact prompt sent)?

## 3. Beyond the Last Frame: Process-aware Evaluation for Generative Video Reasoning (VIPER)

- Link: https://arxiv.org/abs/2512.24952
- Type: benchmark
- Why important: Re-judging the same videos on the whole process, with every frame required to obey the rules, cuts success sharply: Sora 2 goes from 47.0% to 23.3%. Across six models, outcome-only success is 2.0 to 4.3 times process success.
- Role in this topic: The clearest evidence that last-frame scoring rewards wrong paths that end in the right place.
- Main limitation: The judge is GPT-5 reading one frame per second against a rubric; VBVR-Pro later shows that VLM judges change their score on 54.6–92.8% of samples when re-run at temperature 0.
- Discussion question: When can a rule-based checker replace a VLM judge, and what is lost?

## 4. A Very Big Video Reasoning Suite (VBVR)

- Link: https://arxiv.org/abs/2602.20159
- Type: benchmark
- Why important: The first million-scale training set. LoRA fine-tuning Wan2.2 raises the VBVR-Bench score from 0.371 to about 0.685, but gains stop after about 200K samples; humans score 0.974.
- Role in this topic: Turns the field from evaluation to training, and shows that synthetic data helps but saturates.
- Main limitation: Unseen tasks stay about 0.15 below seen ones (0.610 vs 0.760). On VGI-Bench's realistic tasks the gain shrinks with distance from the training tasks: +40.5 for the same structure, +17.1 for partly similar, +6.2 for different.
- Discussion question: Is the plateau a data-diversity limit or a model limit?

## 5. Demystifying Video Reasoning

- Link: https://arxiv.org/abs/2603.16870
- Type: theory
- Why important: Decoding the predicted output at each denoising step shows several paths tried early, one chosen in the middle, and details refined late. Adding noise to all frames at one step drops the score from 0.685 to below 0.3, while noising one frame at every step only drops it to about 0.6.
- Role in this topic: Proposes "chain-of-steps" and directly argues against chain-of-frames.
- Main limitation: The analysis uses one fine-tuned model. VGI-Bench later finds that switching from a wrong to a right answer mid-denoising is rare (2 of 702 cases).
- Discussion question: If the plan is fixed early in denoising, should search and verification act on early steps instead of full videos?

## 6. CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models

- Link: https://arxiv.org/abs/2605.08735
- Type: method
- Why important: A VLM plans each step and checks the result while the video model renders it. On VBVR-Bench this raises the score from 0.671 to 0.757 with about three times the generation of a single run, above best-of-4 sampling.
- Role in this topic: Representative of methods whose gains come from combining video with language.
- Main limitation: It reports no baseline where the same language model answers directly, or writes a program that a deterministic renderer draws.
- Discussion question: How much of the gain belongs to the video model?

## 7. VGI-Bench: Probing Visual Intelligence in Video Generation Models

- Link: https://arxiv.org/abs/2608.19583
- Type: benchmark
- Why important: Realistic photographs as inputs, and strict success that requires both completion and no rule violations. The best model, Seedance 2.0, is fully correct on 14.0% of tasks; humans reach 97.1%.
- Role in this topic: Recalibrates the field: strict zero-shot scores have stayed between about 5% and 25% for a year (VR-Bench 5.6%, VIPER 23.3%, VGI-Bench 14%).
- Main limitation: A VLM still scores completion and rule checks from the whole video.
- Discussion question: Which task families show progress, and which show none?

## 8. Scaling Video Generation for Reasoning: At What Cost? (Rubik-Scaling)

- Link: https://arxiv.org/abs/2609.36599
- Type: theory
- Why important: A controlled study of a 2×2×2 cube turned through nine moves with only three faces visible, training video DiTs from 20M to 1B parameters from scratch. Training loss falls smoothly while reasoning accuracy jumps late. After 1.5M videos, the 1B model has lower MSE than the 70M model, yet its frame accuracy is 3.67% versus 41.00%.
- Role in this topic: Separates looking right from tracking the right hidden state. A 2.8M-parameter model that predicts the state symbolically solves the task, and feeding the state back to the video model raises accuracy from 31.1% to 67.3%.
- Main limitation: One synthetic task with a fixed camera.
- Discussion question: Do loss and FVD tell us anything about whether the hidden state is correct?

## Full paper list

1. Veo3-ZS — https://arxiv.org/abs/2509.20328
2. VChain: Chain-of-Visual-Thought for Reasoning in Video Generation — https://arxiv.org/abs/2510.05094
3. Are Video Models Ready as Zero-Shot Reasoners? (MME-CoF) — https://arxiv.org/abs/2510.26802
4. Thinking with Video — https://arxiv.org/abs/2511.04570
5. TiViBench: Benchmarking Think-in-Video Reasoning for Video Generative Models — https://arxiv.org/abs/2511.13704
6. Can World Simulators Reason? Gen-ViRe — https://arxiv.org/abs/2511.13853
7. Reasoning via Video (VR-Bench) — https://arxiv.org/abs/2511.15065
8. V-ReasonBench — https://arxiv.org/abs/2511.16668
9. RULER-Bench — https://arxiv.org/abs/2512.02622
10. Video Models Start to Solve Chess, Maze, Sudoku, Mental Rotation, and Raven's Matrices (VMEvalKit) — https://arxiv.org/abs/2512.05969
11. MMGR: Multi-Modal Generative Reasoning Benchmark and Evaluation — https://arxiv.org/abs/2512.14691
12. Beyond the Last Frame (VIPER) — https://arxiv.org/abs/2512.24952
13. A Very Big Video Reasoning Suite (VBVR) — https://arxiv.org/abs/2602.20159
14. Demystifying Video Reasoning — https://arxiv.org/abs/2603.16870
15. MME-CoF-Pro — https://arxiv.org/abs/2603.20194
16. Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (ChEaP) — https://arxiv.org/abs/2603.30043
17. How Far Are Video Models from True Multimodal Reasoning? (CLVG-Bench) — https://arxiv.org/abs/2604.19193
18. CollabVR — https://arxiv.org/abs/2605.08735
19. VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization (VLM-as-Teacher) — https://arxiv.org/abs/2606.02564
20. OpenCoF: Learning to Reason Through Video Generation — https://arxiv.org/abs/2607.08763
21. Hierarchical Denoising For Multi-Step Visual Reasoning (HDR) — https://arxiv.org/abs/2607.15278
22. Visual prompt engineering for video models (VIPE) — https://arxiv.org/abs/2607.25537
23. VGI-Bench — https://arxiv.org/abs/2608.19583
24. VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning — https://arxiv.org/abs/2608.26105
25. Training Object Permanence in World Models (WROP) — https://arxiv.org/abs/2609.28654
26. Scaling Video Generation for Reasoning: At What Cost? (Rubik-Scaling) — https://arxiv.org/abs/2609.36599
