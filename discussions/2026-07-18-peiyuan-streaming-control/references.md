# Key References

## 1. StreamingT2V: Consistent, Dynamic, and Extendable Long Video Generation from Text

- Link: https://arxiv.org/abs/2403.14773
- Type: method
- Why important: It directly addresses autoregressive long-video generation and separates short-term transition conditioning from long-term appearance preservation.
- Role in this topic: Streaming baseline and memory design reference.
- Main limitation: Continuity and appearance preservation do not by themselves establish persistent causal state.
- Discussion question: What additional state must be carried forward after an intervention?

## 2. MotionCtrl: A Unified and Flexible Motion Controller for Video Generation

- Link: https://arxiv.org/abs/2312.03641
- Type: method
- Why important: It explicitly distinguishes camera motion from object motion and conditions on poses and trajectories.
- Role in this topic: Control representation and motion-disentanglement reference.
- Main limitation: Successful trajectory following in a generated clip does not guarantee long-horizon persistence after the control ends.
- Discussion question: Can camera/object separation remain stable during chunk-wise generation?

## 3. DragNUWA: Fine-grained Control in Video Generation by Integrating Text, Image, and Trajectory

- Link: https://arxiv.org/abs/2308.08089
- Type: method
- Why important: It combines text, image, and trajectory information for open-domain fine-grained control.
- Role in this topic: Multi-condition trajectory-control reference.
- Main limitation: A trajectory describes a desired path but not necessarily the physical or causal mechanism producing it.
- Discussion question: When should a controller specify a path, and when should it specify an intervention or event?
