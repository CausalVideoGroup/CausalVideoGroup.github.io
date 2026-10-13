# Video Reasoning — Idea Map

Four questions organize the 26 papers. Representative papers are placed where their main evidence lands.

```mermaid
graph TD
    T[Video reasoning: first frame + instruction, draw the solution] --> Q1[Who does the reasoning?]
    T --> Q2[What counts as correct?]
    T --> Q3[Where does reasoning happen?]
    T --> Q4[Can it be taught?]
    Q1 --> A1[Prompt rewriters: Thinking with Video, TiViBench]
    Q1 --> A2[VLM planning: VChain, CollabVR]
    Q1 --> A3[VLM rewards: VLM-as-Teacher]
    Q2 --> B1[Outcome vs process: VR-Bench, VIPER, MME-CoF-Pro]
    Q2 --> B2[Judge reliability: VBVR-Pro]
    Q2 --> B3[Stricter tasks: CLVG-Bench, VGI-Bench, HDR, WROP]
    Q3 --> C1[Chain-of-frames: Veo3-ZS]
    Q3 --> C2[Chain-of-steps: Demystifying, ChEaP]
    Q3 --> C3[Rare self-correction: VGI-Bench]
    Q4 --> D1[Synthetic training data: VBVR, VBVR-Pro, OpenCoF]
    Q4 --> D2[Realistic inputs help: VIPE]
    Q4 --> D3[Fidelity before state: Rubik-Scaling]
```

Timeline used in the deck:

- 2025-09 to 2025-11: zero-shot claims, then the first cracks (papers 1–8).
- 2025-12: same month, opposite conclusions (papers 9–12).
- 2026-02 to 2026-04: training data and mechanism studies (papers 13–17).
- 2026-05 to 2026-07: methods that try to make models reason (papers 18–22).
- 2026-08 to 2026-09: recalibration with stricter benchmarks and controlled studies (papers 23–26).
