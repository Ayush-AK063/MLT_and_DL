# Lecture 11 — Types of Gradient Descent and Momentum Based Gradient Descent (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 11 Gradient Descent Types and Momentum Based MBGD.pdf` — Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Read in full (all 18 slides).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Gradient_Descent_Definition_and_Types.md](00_Recap_Gradient_Descent_Definition_and_Types.md) | Recap: the GD definition and the 3 types, linked back to Lecture 10 |
| [01_Function_Requirements_for_Gradient_Descent.md](01_Function_Requirements_for_Gradient_Descent.md) | Differentiable + convex — and a flagged inconsistency with a later slide |
| [02_SGD_BGD_and_MBGD_Compared_in_Detail.md](02_SGD_BGD_and_MBGD_Compared_in_Detail.md) | Detailed pros/cons and use cases for each of the three GD types |
| [03_Gradient_Descent_Pseudocode_and_Memory_Motivation.md](03_Gradient_Descent_Pseudocode_and_Memory_Motivation.md) | The generic update rule, and a verified memory-size calculation motivating mini-batching |
| [04_MiniBatching_a_Large_Dataset_Worked_Example.md](04_MiniBatching_a_Large_Dataset_Worked_Example.md) | Splitting 100,000 examples into 100 mini-batches of 1000, verified |
| [05_Choosing_Batch_Size_and_the_Momentum_EWMA_Preview.md](05_Choosing_Batch_Size_and_the_Momentum_EWMA_Preview.md) | The m<2000/m≥2000 rule of thumb, and the EWMA formula behind Momentum |
| [06_Advantages_and_Disadvantages_of_Gradient_Descent.md](06_Advantages_and_Disadvantages_of_Gradient_Descent.md) | 4 advantages and 5 disadvantages, cross-referenced throughout this repo |
| [07_Momentum_Based_MiniBatch_Gradient_Descent.md](07_Momentum_Based_MiniBatch_Gradient_Descent.md) | Momentum as EWMA-smoothing applied to noisy mini-batch gradients, tied to Lecture 0's fuller treatment |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- **Recap handled per convention**: slides 2 and 4 repeat Lecture 10's Gradient Descent definition and its three types verbatim — [[00_Recap_Gradient_Descent_Definition_and_Types]] links back rather than re-deriving.
- **A genuine internal inconsistency in the source material, flagged rather than silently resolved**: slide 3 states gradient descent "has to be" applied to a convex function, but slide 12 later in the *same* lecture explicitly says it "can also be used for non-convex optimization problems." [[01_Function_Requirements_for_Gradient_Descent]] flags this directly and explains the resolution (convexity is required for the clean convergence *guarantee*, not for the algorithm to run at all) — this is called out in both [[01_Function_Requirements_for_Gradient_Descent]] and [[06_Advantages_and_Disadvantages_of_Gradient_Descent]].
- **A worked, verified memory calculation**: the handwritten byte-size numbers on slide 8 (100,000 images, 1000×1000 pixels, 10¹¹ bytes, 100GB) were independently recomputed in [[03_Gradient_Descent_Pseudocode_and_Memory_Motivation]] and confirmed exact — a concrete illustration of why mini-batching is a memory necessity, not just a speed optimization.
- **An off-topic anomaly flagged, not silently absorbed**: one slide in the Momentum section (slide 18) has an unrelated handwritten car-shopping checklist scribbled in the corner (budget, comfort, mileage, resale value) — clearly the instructor's own personal note that ended up on the slide, with no connection to the lecture content. Noted explicitly in [[07_Momentum_Based_MiniBatch_Gradient_Descent]] rather than silently ignored or misread as course material.
- **Heavy cross-referencing throughout**: this lecture revisits and deepens material from Lecture 0 (Momentum, the three GD types, learning rate, local minima/saddle points, batch normalization, early stopping) and Lecture 10 (the GD definition, the cyclist analogy) — each handled with a link back rather than full re-derivation where the content is identical, and full new explanation where it goes deeper (the detailed SGD/BGD/MBGD trade-offs, the memory-sizing example, and the advantages/disadvantages lists are all new to this lecture).
- **Web research added**: the standard EWMA framing of Momentum (with β≈0.9 as the typical default) in [[05_Choosing_Batch_Size_and_the_Momentum_EWMA_Preview]], confirming and extending the slide's own handwritten formula.
- **A reference list exists on slide 14** (external sources on gradient descent, learning rate, and normal equations) but wasn't turned into its own topic file, since it's a citation list rather than course content to explain in three styles.
- **Diagrams added**: the mini-batch zigzag descent down a bowl-shaped cost surface (slide 10), and the noisy-vs-momentum-smoothed contour comparison (slide 18) — both recreated as inline SVGs in `site/diagrams.js`.
