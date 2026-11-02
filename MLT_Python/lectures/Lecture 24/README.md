# Lecture 24 — Support Vector Machines (ES514: Machine Learning Techniques)

Source PDF: `Lecture_Support Vector Machine.pdf` (22 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_SVM_History_Vapnik_and_Bell_Labs.md](01_SVM_History_Vapnik_and_Bell_Labs.md) | Slides 1–2: Vapnik & Chervonenkis, Boser–Guyon–Vapnik (COLT-92, AT&T Bell Labs), NIPS, Cortes–Vapnik 1995 soft margin; full timeline |
| [02_What_Is_an_SVM_Hyperplane_w_x_plus_b.md](02_What_Is_an_SVM_Hyperplane_w_x_plus_b.md) | Slides 3–4: supervised SVM, hyperplane w·x + b = 0, cats-vs-dogs 3·Weight + 2·Height − 50 = 0 worked with numbers, distance (w·x+b)/‖w‖ |
| [03_Support_Vectors_Margin_Hard_and_Soft_Margin.md](03_Support_Vectors_Margin_Hard_and_Soft_Margin.md) | Slides 5–8: definitions, "maximize the margin" sketches, canonical form, margin = 2/‖w‖, hard-margin QP, worked 8-point example (x₁ = 2, margin 2, α values) |
| [04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin.md](04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin.md) | Slides 9–11: positive/negative/maximum-margin hyperplanes, good vs bad margin, hard vs soft margin, hinge loss; outlier demo (C = 10⁶ → margin 0.5 vs C = 1 → margin 2) |
| [05_Gamma_and_Regularization_C.md](05_Gamma_and_Regularization_C.md) | Slides 12–14: RBF γ (reach of influence) and C (violation penalty), naming caution, our moons experiment tables |
| [06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick.md](06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick.md) | Slides 15–19: linear vs non-linear, 2-D → 3-D map z = x² + y², kernel trick (verified 121 = 121), linear/poly/RBF formulas, circles experiment (63% → 100%) |
| [07_Advantages_Disadvantages_and_Applications.md](07_Advantages_Disadvantages_and_Applications.md) | Slides 20–22: advantages, disadvantage, applications, each checked/qualified with our runs (scaling 92.3% → 97.9%, timing, digits 99.1%) |
| [08_SVM_in_scikit_learn_Code_Scaling_and_Multiclass.md](08_SVM_in_scikit_learn_Code_Scaling_and_Multiclass.md) | Research enrichment: SVC code, pipeline + GridSearchCV on breast cancer, one-vs-one multiclass (45 SVMs for 10 digits), parameters, comparison with k-NN/trees |

Every one of the 22 slides is accounted for:
- Slide 1 is the title slide.
- Slides 4, 6 and 7 are the instructor's hand-drawn sketches.
- Slides 9–11 share the same title.
- Slides 13–19 are screenshots of animations or figures.

No recap slide, so there is no `00_` file. Three styles per file: Technical, Simple English, Hinglish. Text-only notes; the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **Back to supervised learning** after Lecture 23's clustering. SVM generalises the perceptron of Lecture 4: same w·x + b form, but the separating line is chosen to have the **maximum margin**, and kernels make it non-linear, which solves Lecture 4's linear-separability problem.
- **The slides contain no numeric worked example**, so we built and verified our own:
  - **Cats/dogs hyperplane** (slide 3), with ‖w‖ = √13 ≈ 3.606:
    - (10, 15) scores +10, a cat, at distance 2.77.
    - (5, 10) scores −15, a dog, at distance 4.16.
    - (8, 13) lies on the boundary.
  - **8-point hard-margin example:**
    - Solved by hand: x₁ = 2, w = (1, 0), b = −2, margin 2, support vectors (1, 0), (3, ±1).
    - scikit-learn agrees: dual α·y = −0.5, 0.25, 0.25, and w = Σαᵢyᵢxᵢ checks out.
  - **Outlier/soft-margin demo:** with C = 10⁶ the boundary moves to x₁ = 2.75 and the margin shrinks to 0.5. With C = 1 the boundary stays at x₁ = 2 with margin 2, and the outlier gets slack 1.5.
  - **Kernel trick:** (a·c)² = 121 = φ(a)·φ(c) for a = (1, 2), c = (3, 4). RBF value e⁻⁴ = 0.0183 for ‖x − z‖² = 8 and γ = 0.5.
  - **Experiments** (scikit-learn 1.9.1):
    - **Moons:** γ sweep gives test 76.7 → 93.3 → 88.9% (over-fitting at γ = 100). C sweep gives 45.6% at C = 0.01, then 91–92%.
    - **Circles:** linear 63.3% vs explicit z feature, poly or RBF 100%.
    - **Breast cancer:** raw 92.3%, scaled 97.9%, linear 98.6%.
    - **Digits:** 99.1%.
    - **Timing:** doubling n costs about 3.5× training time.
- **Flags / corrections:**
  1. **Slide 14** labels the wiggly boundary "High Regularization (C)". It means a **high C value**. In standard terms large C is *weak* regularization, because C is the inverse of regularization strength. The pictures are right; the wording is ambiguous.
  2. **Slide 19** says the transformation "is called kernel". Strictly, z = x² + y² is a *feature map* φ. The kernel is K(u, v) = φ(u)·φ(v), computed without building φ (the kernel trick).
  3. **Slide 20:** "memory-efficient" holds for the trained model (only support vectors are stored). Kernel-SVM *training* can need O(n²) memory and be slow on large n.
  4. **Slide 2 history:** the original maximum-margin idea is from the 1960s ("generalized portrait", Vapnik & Lerner / Vapnik & Chervonenkis, 1963–64). The handwritten "1982" matches Vapnik's book *Estimation of Dependences Based on Empirical Data*. The kernel trick is from 1992 (COLT) and the soft margin from Cortes & Vapnik (1995). Secondary sources disagree by a year on some of these dates.
  5. **Slide 5:** "margin = distance from hyperplane to nearest point" is the half-width d = 1/‖w‖. Many texts call the full gap 2/‖w‖ the margin. Both are noted.
  6. **Slide 3's** cats/dogs equation is illustrative (no units or data), and which side is +1 is a convention.
  7. Typos on the slides: "sector vectors" (support vectors, slide 10); "Sentimental Analysis" (sentiment analysis); "Hand Written Detection" (handwriting recognition).
- **Handwriting transcribed:**
  - Slide 2: "kernels 2D → 3D", "AT&T Bell Laboratories", "(1982)", "1992", "(Neural Info. Processing System)", "→ linear & non-linear classification".
  - Slide 3: "Hyperplanes / feature space", "wx + b = 0", "3*Weight + 2*Height − (50) = 0".
  - Slide 4: "Hyperplane (Decision boundary)".
  - Slides 6–7: "Class 1", "Class 2", "Margin", "Hyperplane", "d", "* Maximize the Margin", "support vectors".
  - Slide 12: "controls the trade-off between the model simplicity / training accuracy & overfitting".
  - Slide 13: "(non-linear kernels)".
  - Slide 16: "kernel transformation".
  - Slide 18: one blue point circled, which stays on the wrong side after the transformation.
- **Research enrichment:** SVM history (web search), scikit-learn's definitions of γ and C (web search, the official "RBF SVM parameters" page), dual form and kernel trick, Mercer's condition, hinge loss, multiclass strategies, applications (general knowledge).
- **Off-topic content:** none. The Alice/Cinderella pictures on slide 9 are decoration.
