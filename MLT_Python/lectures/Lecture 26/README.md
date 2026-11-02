# Lecture 26 — Introduction to Deep Learning: Representation Learning (ES514: Machine Learning Techniques)

Source PDF: `Lecture_Introduction to Deep learning.pdf` (23 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_Note_Slides_1_to_4_Traditional_Programming_and_AI_Hierarchy.md](00_Recap_Note_Slides_1_to_4_Traditional_Programming_and_AI_Hierarchy.md) | Slides 1–4: title slide; Traditional programming vs ML and AI ⊃ ML ⊃ DL repeat Lecture 2, so this is a short recap that links back |
| [01_The_Issue_of_Representation_Search_Roman_Numerals_and_Unary_Primality.md](01_The_Issue_of_Representation_Search_Roman_Numerals_and_Unary_Primality.md) | Slide 5: why representation matters; sorted vs unsorted search (10⁶ vs 20 comparisons); 210 ÷ 6 vs CCX ÷ VI; unary primality (input size, pseudo-polynomial, the regex trick) |
| [02_Choice_of_Representation_Cartesian_vs_Polar_Coordinates.md](02_Choice_of_Representation_Cartesian_vs_Polar_Coordinates.md) | Slide 6: same data in (x, y) vs (r, θ); conversion formulas; our logistic-regression run: 53.75% vs 100% |
| [03_Learning_Representations_and_Why_Hand_Designed_Features_Are_Hard.md](03_Learning_Representations_and_Why_Hand_Designed_Features_Are_Hard.md) | Slides 7–9: traditional pattern recognition vs end-to-end learning; dependence on features and domain knowledge; the "identify a car" wheel example |
| [04_Representation_Learning_and_Factors_of_Variation.md](04_Representation_Learning_and_Factors_of_Variation.md) | Slides 10–11: benefits of learned representations, transfer learning, the autoencoder; factors of variation (speech, image) and disentangling |
| [05_Deep_Learning_Building_Complex_Concepts_from_Simple_Ones.md](05_Deep_Learning_Building_Complex_Concepts_from_Simple_Ones.md) | Slides 12 and 18: pixels → edges → corners/contours → object parts → identity; low/mid/high-level features → trainable classifier (Zeiler & Fergus) |
| [06_Computational_Graphs_and_the_Depth_of_a_Model.md](06_Computational_Graphs_and_the_Depth_of_a_Model.md) | Slides 13–15: σ(w₁x₁ + w₂x₂) as a graph; worked value σ(−1) = 0.2689; depth 3 vs depth 1; parallel vs sequential computation; link to back-propagation |
| [07_Machine_Learning_and_AI_Venn_Diagram_and_the_Cyc_Project.md](07_Machine_Learning_and_AI_Venn_Diagram_and_the_Cyc_Project.md) | Slides 16–17: AI ⊃ ML ⊃ representation learning ⊃ DL with examples; Cyc (MCC, July 1984, Lenat), knowledge bases and the "Fred shaving" failure |
| [08_Conventional_Machine_Learning_Pipeline_SIFT_and_HOG.md](08_Conventional_Machine_Learning_Pipeline_SIFT_and_HOG.md) | Slide 19: sensing → preprocessing → feature extraction → selection → inference; SIFT (128-D) and HOG (3,780-D) explained with a gradient example |
| [09_Deep_Learning_Model_and_the_Four_AI_Flowcharts.md](09_Deep_Learning_Model_and_the_Four_AI_Flowcharts.md) | Slides 20–23: MLP as a composition of simple functions; our XOR network (OR + AND hidden layer); rule-based vs classic ML vs representation learning vs deep learning flowcharts |

All 23 slides are covered. Slide 18 is explained together with slide 12 (Topic 5) because both show the simple → complex feature hierarchy. Each file has three styles: Technical, Simple English, Hinglish. The notes are text-only; the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **Course code on the slides.** Every slide's footer says "**ES532: Deep Learning**", with page numbers 34–55. The slides come from a larger Deep Learning deck. The user confirmed this lecture belongs to the MLT course as Lecture 26. It is the bridge from classical ML (Lectures 1–25) to deep learning.
- **Recap.** Slides 2–4 repeat Lecture 2 (slides 19–20 and 30), so Topic 0 links back instead of repeating them.
- **Main source.** Most figures come from Goodfellow, Bengio & Courville, *Deep Learning* (MIT Press, 2016), chapter 1: Figs 1.1 (Cartesian/polar), 1.2 (layers of a face/car/animal network), 1.3 (computational graphs), 1.4 (Venn diagram) and 1.5 (flowcharts). Slide 18 is from LeCun & Ranzato's ICML 2013 tutorial; slide 19 is credited to LeCun, Bengio & Hinton (*Nature*, 2015).
- **Verification** (the slides have no numeric examples, so all numbers are ours):
  - Binary search on 10⁶ items: ⌈log₂(10⁶ + 1)⌉ = 20 comparisons. 210 ÷ 6 = 35 (CCX ÷ VI = XXXV).
  - The unary regex `^1?$|^(11+?)\1+$` fails to match exactly the primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 for n = 1…29.
  - Ring dataset (400 points): logistic regression 53.75% on (x, y), 100% on (r, θ), boundary r ≈ 1.52.
  - Computational graph: w = (2, −1), x = (1, 3) → z = −1, σ = 0.2689; gradient ∂ŷ/∂w₁ = 0.1966.
  - HOG window 64 × 128: 105 blocks × 36 = 3,780 features. SIFT: 4 × 4 × 8 = 128.
  - XOR MLP (OR + AND hidden units): correct on all 4 inputs.
- **Flags:**
  1. **Slides 21–23 differ from the book's Fig. 1.5** in three ways: the Classic ML row says "Hand designed program" (book: "Hand-designed features"); representation learning and deep learning are merged under one "Deep Learning" label (the book keeps them as separate rows); and the "Abstract feature" box is not shaded (in the book it is, because it is learned). Details in Topic 9.
  2. **Slide 15's note** ("shallow architecture can do computation in parallel but not sequential") is compressed. Topic 6 explains it using the book's view of depth as the number of sequential steps.
  3. **Slide 16** is a re-styled redraw of the book's Fig. 1.4. Its content matches the original.
- **Cyc facts checked** against Wikipedia and MIT Technology Review: started July 1984 at MCC (Austin, Texas), led by Douglas Lenat (died 31 Aug 2023), spun off as Cycorp in 1994–95 (sources differ on the year), OpenCyc released 2002.
