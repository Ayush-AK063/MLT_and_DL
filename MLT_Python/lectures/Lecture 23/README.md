# Lecture 23 — Clustering and the k-Means Algorithm (ES514: Machine Learning Techniques)

Source PDF: `Lecture_Clustering with K Means.pdf` (32 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_What_Is_Clustering_Unsupervised_Grouping.md](01_What_Is_Clustering_Unsupervised_Grouping.md) | Slides 1–2, 7: clustering as unsupervised grouping, similarity/distance measures, intra- vs inter-cluster similarity, the "Structure/Pattern" C1–C2 scatter |
| [02_Taxonomy_of_Clustering_Techniques.md](02_Taxonomy_of_Clustering_Techniques.md) | Slides 3–4: the five-family tree (partitioning, hierarchical, density, graph, model-based) with every named algorithm, plus the Han–Kamber characteristics table (incl. grid-based) |
| [03_K_Means_Definition_Objective_and_History.md](03_K_Means_Definition_Objective_and_History.md) | Slides 5, 8: definition, SSE objective, why the mean, "k is a free parameter", history (Steinhaus → Lloyd → Forgy → MacQueen → Hartigan–Wong) |
| [04_K_Means_Algorithm_Steps.md](04_K_Means_Algorithm_Steps.md) | Slide 6: Algorithm 16.1 step by step, convergence criteria, proof that SSE never increases, ties/empty clusters/scaling |
| [05_K_Means_Visual_Walkthrough_k_Equals_2.md](05_K_Means_Visual_Walkthrough_k_Equals_2.md) | Slides 9–16: the 16-point animation (random stars → assign → move → re-assign … → 8/8 split), perpendicular-bisector boundary |
| [06_Choosing_k_SSE_and_the_Elbow_Method.md](06_Choosing_k_SSE_and_the_Elbow_Method.md) | Slides 17–25: k = 2/4/6 splits, SSE = SSE₁+…+SSE_k, the elbow plot (k = 4); our verification runs (blobs elbow at 4; 8-point data elbow at 3) |
| [07_Silhouette_Coefficient_and_Gap_Statistic.md](07_Silhouette_Coefficient_and_Gap_Statistic.md) | Slide 25 (handwritten): silhouette s(i) = (b−a)/max(a,b) with hand-worked A8/A2 values, gap statistic with our run; comparison table |
| [08_Worked_Example_Eight_Points_Manhattan_Distance.md](08_Worked_Example_Eight_Points_Manhattan_Distance.md) | Slides 26–32: the 8-point, k = 3, Manhattan-distance exam problem — both iterations in full; answer (3, 9.5), (6.5, 5.25), (1.5, 3.5); our iterations 3–4 to convergence |
| [09_K_Means_Limitations_k_means_plus_plus_and_scikit_learn.md](09_K_Means_Limitations_k_means_plus_plus_and_scikit_learn.md) | Research enrichment: strengths/limitations, initialisation experiment, k-means++, two-moons vs DBSCAN, scikit-learn code, k-NN vs k-Means |

Every one of the 32 slides is accounted for. Slide 1 is the title slide. Slides 7–16 and 18–25 are screenshots of an animation with handwritten notes and no printed slide numbers. The printed numbers on the other slides jump (6, 7, 8, 10, 12, then 33–39), which suggests the deck is an excerpt of a longer source deck. No content is missing within the topic sequence. No recap slide, so there is no `00_` file. Three styles per file: Technical, Simple English, Hinglish. Text-only notes; the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **New unit: unsupervised learning.** Lectures 9–22 were all supervised (labels known). Clustering has no labels. It ties back to Lecture 3 (ML paradigms), Lecture 8 (discretisation by clustering) and Lecture 16 (distance metrics; k-NN's k ≠ k-Means' k).
- **Verification of the worked example (slides 26–32):**
  - Every distance in both iteration tables, every assignment, and all centre calculations were recomputed in Python. **All printed values are correct.**
  - The answer after iteration 2 is **C1(3, 9.5), C2(6.5, 5.25), C3(1.5, 3.5)** ✔.
  - We continued the run: iteration 3 moves A4 to C1, giving centres (3.67, 9), (7, 4.33), (1.5, 3.5). Iteration 4 changes nothing, so the run has converged.
  - SSE after each update: 37 → 23.25 → 14.33. 14.33 is the global optimum for k = 3.
  - Euclidean distance gives identical assignments at every step.
- **Our own experiments** (scikit-learn 1.9.1; none of these numbers are on the slides):
  - **Elbow, 4 blobs:** SSE 19780 → 9211 → 1919 → 362 → 328 …, elbow at k = 4.
  - **Elbow, 8 points:** SSE 100.75 → 51.47 → 14.33 → 8.67 …, elbow at k = 3.
  - **Silhouette:** best at k = 3 (0.571) for the 8 points and k = 4 (0.834) for the blobs.
  - **Gap statistic:** picks k = 4 on the blobs.
  - **Random initialisation:** reaches the optimum in 80.5% of 200 single starts, versus 99% with k-means++.
  - **Two moons:** k-Means ARI 0.24 vs DBSCAN ARI 1.00.
- **Flags / corrections:**
  1. **Slide 5** credits k-Means to "J. Hartigan and M. A. Wong [1979]". The method is older: Steinhaus 1956, Lloyd 1957 (published 1982), Forgy 1965, and MacQueen 1967, who coined the name. Hartigan & Wong published an efficient *variant* (Algorithm AS 136), which is R's default. Algorithm 16.1 on slide 6 is Lloyd's procedure.
  2. **Slide 3** lists STING, CLIQUE and WaveCluster under *density-based*. In Han–Kamber–Pei (the source of slide 4's table) they are the standard *grid-based* examples (CLIQUE being grid + density). Slide 3 also has no grid-based branch, even though slide 4 does.
  3. **Slide 3's years** are milestone dates. Fuzzy c-means is usually credited to Dunn (1973) and Bezdek (1981), not 1999.
  4. **Slide 26 handwriting:** the instructor's scratch row gives A1→A7 = 8. The correct value is |1−2| + |2−10| = **9**, which the printed table shows. It has no effect on the result.
  5. **Slides 22–23 notation:** SSE is written Σ_{i=0}^{n} dist(x_i − c)². Read it as Σ_{i=1}^{n} dist(x_i, c)².
  6. **Slide 24's elbow plot** is illustrative. SSE reaches exactly 0 only when every point is its own cluster (k = n).
  7. **Slides 9–10** start the centroids at random *locations*, while Algorithm 16.1 picks random *data objects*. Both are valid initialisations.
  8. **Slides 26–32** assign with Manhattan distance but update with the mean. This is the standard textbook convention. The median would be the exact L1 minimiser (k-medians).
  9. Typos on the slides: "Chamelon" (CHAMELEON); "We re-compute the new cluster clusters" (should be "cluster centres").
- **Handwriting transcribed:**
  - Slide 3: "Distance based", "Hierarchical Decomposition", "Dense regions of objects (Neighborhood)".
  - Slide 5: n objects h1, h2, h3 → C1, C2, C3, "Distance", "k no. of clusters", "Moving stops".
  - Slide 6: "k = 2, 3, 4", "C1, C2, C3", "Centroid".
  - Slide 7: "Structure / Pattern", f1 (X), f2 (Y).
  - Slide 8: "kmeans → Clusters, K? free parameter".
  - Slide 16: "K? optimal clusters".
  - Slides 18, 21, 24: "Elbow method", "Sum of Squared Error", "k = 4", "Clusters".
  - Slide 23: "SSE", "k = 3, 4, 6".
  - Slide 25: "① Silhouette Coefficient method ② Gap statistic".
  - Slides 26–29: the worked arithmetic.
- **Research enrichment:** k-Means history, Hartigan–Wong, k-means++ (SODA 2007, O(log k) guarantee), silhouette (Rousseeuw 1987), gap statistic (Tibshirani–Walther–Hastie 2001), Han–Kamber–Pei taxonomy, DBSCAN, scikit-learn API.
- **Off-topic content:** none.
