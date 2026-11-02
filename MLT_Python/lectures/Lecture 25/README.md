# Lecture 25 — SVM Numericals: Finding the Optimal Hyperplane by Hand (ES514: Machine Learning Techniques)

Source PDF: `Lecture_SVM_Numericals.pdf` (14 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Exercise_1_Problem_and_the_Six_Step_Method.md](01_Exercise_1_Problem_and_the_Six_Step_Method.md) | Slides 1–2: the 11-point question (labels not stated, so we infer left = −1, right = +1), the six-step augmented-vector recipe, why "add a 1" absorbs b |
| [02_Exercise_1_Full_Solution_Alphas_and_Hyperplane_x1_equals_3.md](02_Exercise_1_Full_Solution_Alphas_and_Hyperplane_x1_equals_3.md) | Slides 3–6: S₁ = (2, 0, 1), S₂ = (4, 0, 1); 5α₁ + 9α₂ = −1, 9α₁ + 17α₂ = 1 → α₁ = −6.5, α₂ = 3.5; w̃ = (1, 0, −3) → x₁ = 3; orientation rule; margin 2; every point checked |
| [03_Exercise_2_Three_Support_Vectors_Hyperplane_x1_equals_2.md](03_Exercise_2_Three_Support_Vectors_Hyperplane_x1_equals_2.md) | Slide 7: three support vectors; full Gram matrix and equations (not on the slide); α = −3.5, 0.75, 0.75; w̃ = (1, 0, −2) → x₁ = 2 |
| [04_scikit_learn_SVM_Documentation_and_Code_for_Both_Exercises.md](04_scikit_learn_SVM_Documentation_and_Code_for_Both_Exercises.md) | Slide 8: scikit-learn User Guide 1.4 (definition, advantages, disadvantages); code reproducing both exercises |
| [05_Iris_Setosa_vs_Versicolor_Choosing_the_Best_Line.md](05_Iris_Setosa_vs_Versicolor_Choosing_the_Best_Line.md) | Slides 9–14: petal/sepal, candidate lines, black vs orange, support vectors and margin; our real-Iris solution (w = (0.824, 1.294), b = −3.788, margin 1.304) derived by hand |
| [06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method.md](06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method.md) | Research: what the augmented shortcut computes, why it is right for Exercises 1–2, counter-examples, the exact dual method and the two-SV closed form, exam advice |

Every one of the 14 slides is accounted for. Slide 2 repeats the question without the steps. Slides 4–5 are full-page handwriting. Slides 9–14 are an animation-style figure sequence. No recap slide; this lecture applies Lecture 24 directly. Three styles per file: Technical, Simple English, Hinglish. Text-only notes; the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **Continuation of Lecture 24.** Lecture 25 turns the maximum-margin idea into hand calculation. Exercise 2's dataset is the same 8-point example we had already solved in Lecture 24, Topic 3, using a different method, and the answer agrees.
- **Verification:**
  - **Exercise 1:**
    - Dot products 5, 9 and 17. α₁ = −6.5, α₂ = 3.5 (elimination and Cramer's rule).
    - w̃ = (1, 0, −3), so the hyperplane is x₁ = 3 with margin 2.
    - All 11 points satisfy yᵢ(w·xᵢ + b) ≥ 1.
    - scikit-learn gives w = (1, 0), b = −3, support vectors (2, 0) and (4, 0) ✔.
  - **Exercise 2:**
    - Gram matrix [[2, 4, 4], [4, 11, 9], [4, 9, 11]]. α = −3.5, 0.75, 0.75.
    - w̃ = (1, 0, −2), so the hyperplane is x₁ = 2 with margin 2.
    - scikit-learn agrees ✔.
  - **Iris** (our run on the real data; the slides only show a schematic):
    - Setosa vs versicolor on petal width and length.
    - w = (0.824, 1.294), b = −3.788. Support vectors (0.4, 1.9) and (1.1, 3.0). Margin √1.70 = 1.304. 100% accuracy.
    - Reproduced by hand with the perpendicular-bisector formula.
- **Flags / corrections:**
  1. **Exercise 1 never states the class labels.** The solution implicitly takes the left cluster (x₁ ≤ 2) as −1 and the right cluster (x₁ ≥ 4) as +1. State this in answers.
  2. **"b + 3 = 0" (slide 5) and "b + 2 = 0" (slide 7)** should read **x₁ − 3 = 0** and **x₁ − 2 = 0**. The values b = −3 and b = −2 themselves are correct.
  3. **The augmented-vector shortcut's α values are not the SVM's Lagrange multipliers.** Those are ≥ 0: 0.5, 0.5 in Exercise 1 and 0.5, 0.25, 0.25 in Exercise 2. The shortcut minimises ‖w‖² + b² on the chosen support vectors instead of ‖w‖² alone.
     - It gives the correct hyperplane for both exercises: in Exercise 2 the equations fully determine (w, b), and in Exercise 1 both support vectors lie on x₂ = 0.
     - It is **not reliable in general.** For the points (0, 1)/(2, 1) it gives a tilted line with margin 1.789 instead of x₁ = 1 with margin 2. On the real Iris support vectors it gives margin 0.856 instead of 1.304.
     - Topic 6 gives the exact dual method and a two-support-vector closed form.
  4. **Slide 3 handwriting** labels both support vectors "S₂". The left one, (2, 0), is S₁.
  5. **Slides 10–14 are schematic.**
     - The real Iris data has no versicolor flower near the setosa cluster.
     - In an exact SVM all support vectors are equidistant (1/‖w‖) from the hyperplane, unlike the varying dashed lengths drawn on slide 14.
  6. **"Convert 2D to 3D" (slide 1, step 3)** is bias augmentation (adding a constant 1). It is not the kernel lift of Lecture 24.
- **Handwriting transcribed:**
  - Slide 1: "SVs (x, y) → 3D", "3D → (…, 1) → Bias", "α₁, α₂ = ?", "→ Σ wᵢ αᵢ"; ticks on steps 1–3.
  - Slide 3: circled (2, 0) and (4, 0); S₁ = (2, 0, 1), S₂ = (4, 0, 1); "2D to 3D".
  - Slide 4: equations ① to ④, "w.r.t. S₁ / S₂", α₁ = −6.5, α₂ = 3.5, "Obtain Hyperplane → w̃ = Σ αᵢ Sᵢ".
  - Slide 5: the w̃ arithmetic, "for orientation of line", "Vertical line", "for bias", "(i) Horizontal (0, 1), (ii) Vertical (1, 0), (iii) Diagonal (1, 1)", "b = −3", "b + 3 = 0 plus side".
  - Slide 7: support vectors S₁ (−), S₂ (+), S₃ (+), α values, w̃ = (1, 0, −2), "Vertical", "b = −2", "b + 2 = 0".
  - Slide 13: "SV" arrows.
- **Research enrichment:** scikit-learn documentation (rest of the slide-8 page), SVM dual formulation (Lecture 24 sources), Fisher's Iris data via scikit-learn, and our own analysis of the shortcut.
- **Off-topic content:** none.
