# Lecture 13 — CPU/GPU Comparisons (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 13 CPU and GPU.pdf` — 29 slides, read in full (a mix of text slides and picture slides: the burger analogy, the GPU timeline, architecture diagrams and the component table were read visually).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [01_The_Burger_Kitchen_Analogy_One_Chef_vs_Many_Assistants.md](01_The_Burger_Kitchen_Analogy_One_Chef_vs_Many_Assistants.md) | One head chef (CPU) vs many junior assistants (GPU), 100 burgers |
| [02_GPU_History_Timeline_and_the_NVIDIA_GPU_Family_Tree.md](02_GPU_History_Timeline_and_the_NVIDIA_GPU_Family_Tree.md) | 1980s video card → GeForce 256 → GPGPU → CUDA → Maxwell; Kepler→Blackwell family tree |
| [03_CPU_vs_GPU_Definitions_and_the_Cache_Memory_Hierarchy.md](03_CPU_vs_GPU_Definitions_and_the_Cache_Memory_Hierarchy.md) | Definitions; core vs thread; L1/L2/L3, RAM, storage; hits and misses |
| [04_Similarities_Between_CPUs_and_GPUs_Cores_Memory_and_Control_Units.md](04_Similarities_Between_CPUs_and_GPUs_Cores_Memory_and_Control_Units.md) | Shared parts (cores, memory, control unit); block diagrams; component comparison table |
| [05_Key_Differences_Graphics_Origins_Memory_and_Execution_Models.md](05_Key_Differences_Graphics_Origins_Memory_and_Execution_Models.md) | Why GPUs appeared; memory/control and execution-style contrasts |
| [06_Function_Design_Summary_and_When_to_Use_GPUs.md](06_Function_Design_Summary_and_When_to_Use_GPUs.md) | Function and design; deep learning, HPC, autonomous vehicles; summary table; resources |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **No worked numeric examples** appear, so nothing needed numeric re-verification. The component table's figures were checked for plausibility only.
- **Flag — infographic slides:** slides 2–4, 6 and 7 are stylised graphics (apparently AI-generated or marketing-style), not primary sources; small print on slide 6 was not reproduced.
- **Flag — approximate ranges:** the slide-14 table ("4–64 cores", "3,000–15,000+") is an order-of-magnitude contrast; some current server CPUs exceed 64 cores.
- **Flag — "first GPU, 1999":** the NVIDIA GeForce 256 is described as the first GPU following NVIDIA's own terminology; earlier graphics chips existed (the slide shows "video card" in the 1980s).
- **Slides 8 and 9 carry handwritten notes** ("Core vs Thread", "Multicore vs Multithreading", cache sizes, "local/global miss", hit/miss ratio); their one-line explanations here are standard background, labelled as such.
- **Slides 2, 3, 6, 7, 20 and 21 are largely picture/table slides** whose content is summarised in the topic files.
- **Slide numbers on the slides** run 2–29 (title slide unnumbered); the PDF has all 29 pages, none missing.
- **Fits the syllabus's second block** (GPU architecture, CPU/GPU comparison); the CUDA/thread-hierarchy topics it leads into are not yet in this repo.
- Web research was not needed beyond confirming widely-known historical facts (GeForce 256 in 1999, CUDA in 2007, OpenCL in 2009), which match the slide's own timeline.
