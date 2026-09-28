# Video Editing Frontiers — References

## Key reading

## 1. FlowEdit (ICCV 2025)

- Link: [FlowEdit (ICCV 2025)](https://arxiv.org/pdf/2412.08629)
- Role: Inference-time transport
- Why important: Editing follows a difference between target and source velocity fields.
- Main limitation: The original work addresses images; a video adaptation changes the backbone and must verify temporal behavior.
- Discussion question: How does source preservation interact with changes in motion?

## 2. DynaEdit

- Link: [DynaEdit](https://arxiv.org/pdf/2603.17989)
- Role: Dynamic rewriting
- Why important: Its source-query and guidance design motivates a separate discussion of preserving appearance while changing dynamics.
- Main limitation: Sampling controls do not by themselves establish correct object contact or event replacement.
- Discussion question: Which failures come from the control signal, and which come from the backbone?

## 3. Bernini

- Link: [Bernini](https://arxiv.org/pdf/2605.22344)
- Role: Semantic planning and rendering
- Why important: A semantic planner and a renderer expose different roles for edit intent and visual detail.
- Main limitation: The deck follows the existing v1 method audit; it does not claim a completed v2 difference audit.
- Discussion question: Which planner supervision improves action semantics without unwanted source changes?

## 4. World in World

- Link: [World in World](https://arxiv.org/pdf/2609.11548)
- Role: Source-grounded world-model editing
- Why important: Source observations and correspondence-based evidence support controlled re-observation and editing.
- Main limitation: Camera-rendering evidence should not be treated as proof of arbitrary physical interaction editing.
- Discussion question: How should hidden state and contact uncertainty enter the editing interface?

## 5. MMLVE-Agent

- Link: [MMLVE-Agent](https://arxiv.org/pdf/2608.26809)
- Role: Editing agents
- Why important: Shot assignment, global visual references, and feedback separate orchestration from pixel generation.
- Main limitation: External editor capability, service failures, and retry costs influence the end-to-end result.
- Discussion question: Does planning improve success over a fixed workflow at the same call budget?

## 6. CoVEBench

- Link: [CoVEBench](https://arxiv.org/pdf/2606.08415)
- Role: Compositional evaluation
- Why important: Fine-grained checks help separate individual instruction requirements.
- Main limitation: A compositional instruction is different from a sequence of requests with history and selective undo.
- Discussion question: Which event and session annotations reveal failures hidden by aggregate quality?

## Paper and model index

- [World in World](https://arxiv.org/pdf/2609.11548)
- [NeoVerse](https://arxiv.org/pdf/2601.00393)
- [ActionSplice](https://arxiv.org/pdf/2609.08230)
- [PhysEditWorld](https://arxiv.org/pdf/2606.26694)
- [GaussianDWM++](https://arxiv.org/pdf/2608.16234)
- [Twin Rollouts](https://arxiv.org/pdf/2608.08982)
- [Game2World](https://arxiv.org/pdf/2608.24680)
- [CRONOS](https://arxiv.org/pdf/2605.23699)
- [What-If World](https://arxiv.org/pdf/2605.27589)
- [Qwen-Video-Edit](https://arxiv.org/pdf/2608.14790)
- [GRNEdit](https://arxiv.org/pdf/2608.16328)
- [MSEditor](https://arxiv.org/pdf/2608.17559)
- [MMLVE-Agent](https://arxiv.org/pdf/2608.26809)
- [EditVid](https://arxiv.org/pdf/2609.04190)
- [SVEET](https://arxiv.org/pdf/2609.24788)
- [VideoX-Qwen](https://arxiv.org/pdf/2609.26015)
- [Vidu S2](https://arxiv.org/pdf/2609.11638)
- [JAVEdit](https://arxiv.org/pdf/2606.03168)
- [MDN-Control](https://arxiv.org/pdf/2609.16475)
- [CoinVE](https://arxiv.org/pdf/2608.17566)
- [AnyV2V](https://arxiv.org/pdf/2403.14468)
- [DreamMotion](https://arxiv.org/pdf/2403.12002)
- [FastVideoEdit](https://arxiv.org/pdf/2403.06269)
- [COVE](https://arxiv.org/pdf/2406.08850)
- [VideoDirector](https://arxiv.org/pdf/2411.17592)
- [V2Edit](https://arxiv.org/pdf/2503.10634)
- [DFVEdit](https://arxiv.org/pdf/2506.20967)
- [VINO](https://arxiv.org/pdf/2506.12520)
- [FlowAnchor](https://arxiv.org/pdf/2604.22586)
- [EquiEdit](https://arxiv.org/pdf/2607.05056)
- [EffiVED](https://arxiv.org/pdf/2403.11568)
- [EVE](https://arxiv.org/pdf/2403.09334)
- [Movie Gen](https://arxiv.org/pdf/2410.13720)
- [VACE](https://arxiv.org/pdf/2503.07598)
- [UNIC](https://arxiv.org/pdf/2506.04216)
- [OmniV2V](https://arxiv.org/pdf/2506.01801)
- [EditVerse](https://arxiv.org/pdf/2509.20360)
- [Unpaired Clips](https://arxiv.org/pdf/2510.14648)
- [Scaling / Editto](https://arxiv.org/pdf/2510.15742)
- [UniVideo](https://arxiv.org/pdf/2510.08377)
- [EasyV2V](https://arxiv.org/pdf/2512.16920)
- [SAMA](https://arxiv.org/pdf/2603.19228)
- [Omni-Video 2](https://arxiv.org/pdf/2602.08820)
- [Kiwi-Edit](https://arxiv.org/pdf/2603.02175)
- [ViFeEdit](https://arxiv.org/pdf/2603.15478)
- [OmniWeaving](https://arxiv.org/pdf/2603.24458)
- [Mamoda2.5](https://arxiv.org/pdf/2605.02641)
- [Lance](https://arxiv.org/pdf/2605.18678)
- [Bernini](https://arxiv.org/pdf/2605.22344)
- [RVEDiT](https://arxiv.org/pdf/2605.24674)
- [LoomVideo](https://arxiv.org/pdf/2606.06042)
- [TIDE](https://arxiv.org/pdf/2606.08260)
- [I2VEdit](https://arxiv.org/pdf/2405.16537)
- [VIVID](https://arxiv.org/pdf/2411.15260)
- [VideoPainter](https://arxiv.org/pdf/2503.05639)
- [VideoGrain](https://arxiv.org/pdf/2502.17258)
- [Shape-for-Motion](https://arxiv.org/pdf/2506.22432)
- [PropFly](https://arxiv.org/pdf/2602.20583)
- [NOVA](https://arxiv.org/pdf/2603.02802)
- [MiVE](https://arxiv.org/pdf/2605.14664)
- [GIVE](https://arxiv.org/pdf/2606.24225)
- [ReBind](https://arxiv.org/pdf/2607.14681)
- [Streaming Video Diffusion](https://arxiv.org/pdf/2405.19726)
- [Memory-V2V](https://arxiv.org/pdf/2601.16296)
- [MLV-Edit](https://arxiv.org/pdf/2602.02123)
- [LIVEditor-14B](https://arxiv.org/pdf/2605.04569)
- [StreamEdit](https://arxiv.org/pdf/2605.21466)
- [LiveEdit](https://arxiv.org/pdf/2606.26740)
- [FateZero](https://arxiv.org/pdf/2303.09535)
- [Text2Video-Zero](https://arxiv.org/pdf/2303.13439)
- [TokenFlow](https://arxiv.org/pdf/2307.10373)
- [RAVE](https://arxiv.org/pdf/2312.04524)
- [ReCo](https://arxiv.org/pdf/2512.17650)
- [EditBoard](https://arxiv.org/pdf/2409.09668)
- [Señorita-2M](https://arxiv.org/pdf/2502.06734)
- [InsViE-1M](https://arxiv.org/pdf/2503.20287)
- [FiVE](https://arxiv.org/pdf/2503.13684)
- [CoVEBench](https://arxiv.org/pdf/2606.08415)
- [VEFX-Bench](https://arxiv.org/pdf/2604.16272)
- [Goku](https://arxiv.org/pdf/2606.30599)
- [Aurora](https://arxiv.org/pdf/2605.18748)
- [DynaEdit](https://arxiv.org/pdf/2603.17989)
- [MotionV2V](https://arxiv.org/pdf/2511.20640)
- [VOID](https://arxiv.org/pdf/2604.02296)
- [JoyAI-Video-Edit](https://arxiv.org/pdf/2608.03974)
- [FlowEdit (ICCV 2025)](https://arxiv.org/pdf/2412.08629)
- [WorldMirror](https://arxiv.org/pdf/2510.10726)
- [Wan](https://arxiv.org/pdf/2503.20314)
- [Wan2.2](https://github.com/Wan-Video/Wan2.2)
- [SD3](https://arxiv.org/pdf/2403.03206)
- [FLUX](https://github.com/black-forest-labs/flux)
- [FLUX.2 Klein](https://bfl.ai/models/flux-2-klein)
- [SigLIP](https://arxiv.org/pdf/2303.15343)
- [Gemma](https://arxiv.org/pdf/2503.19786)
- [LTX-2.3](https://ltx.io/blog/ltx-2-3-release)
- [SAM2](https://arxiv.org/pdf/2408.00714)
- [SAM3](https://arxiv.org/pdf/2511.16719)
- [VGGT](https://arxiv.org/pdf/2503.11651)
- [LingBot-World](https://arxiv.org/pdf/2601.20540)
- [Self Forcing](https://arxiv.org/pdf/2506.08009)
- [LongLive](https://arxiv.org/pdf/2509.22622)
- [Qwen-Image-Edit](https://arxiv.org/pdf/2508.02324)
- [Qwen2.5-VL](https://arxiv.org/pdf/2502.13923)
- [Qwen3-VL](https://arxiv.org/pdf/2511.21631)
- [Qwen3.5-4B](https://qwen.ai/blog?id=qwen3.5)
- [T5](https://arxiv.org/pdf/1910.10683)
- [CLIP](https://arxiv.org/pdf/2103.00020)
- [DINO](https://arxiv.org/pdf/2104.14294)
- [IVEBench](https://arxiv.org/pdf/2510.11647)
- [TAPNext](https://arxiv.org/pdf/2504.05579)
- [CogVideoX](https://arxiv.org/pdf/2408.06072)
- [ControlNet](https://arxiv.org/pdf/2302.05543)
- [LingBot-World-2](https://arxiv.org/pdf/2607.07534)
- [ReCamMaster](https://arxiv.org/pdf/2503.11647)
- [LucyEdit](https://d2drjpuinn46lb.cloudfront.net/Lucy_Edit__High_Fidelity_Text_Guided_Video_Editing.pdf)
- [HappyHorse 1.0](https://www.alibabacloud.com/help/en/model-studio/happyhorse-1-0-video-edit)
- [DDIM](https://arxiv.org/pdf/2010.02502)
- [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)

## Example and asset notes

- [Examples and evaluation protocols](evidence.html)
- [Figure, formula, and video sources](sources.html)
