# Lecture 16 — K Nearest Neighbor (k-NN) Classification (ES514: Machine Learning Techniques)

Source PDF: `Lecture KNN Classification-1.pdf` (20 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Nearest_Neighbor_Idea_and_Basic_Rule.md](01_Nearest_Neighbor_Idea_and_Basic_Rule.md) | The "duck test" idea, the majority-vote rule, why k is chosen odd, the 1-/2-/3-nearest-neighbor figure, and the research-enriched origin (Fix & Hodges 1951, Cover & Hart 1967) |
| [02_k_NN_as_Instance_Based_Lazy_Learning.md](02_k_NN_as_Instance_Based_Lazy_Learning.md) | Instance-based / memory-based / lazy learning vs. eager learners, the "similar things are close" assumption (decision-region figure), classification (plurality vote) vs. regression (average) |
| [03_Issues_and_Choosing_the_Value_of_K.md](03_Issues_and_Choosing_the_Value_of_K.md) | The five issues list, too-small vs. too-large k, the K = √N rule of thumb (and its even-k problem), cross-validation |
| [04_Distance_Metrics.md](04_Distance_Metrics.md) | All 12 distance functions on slide 7 (Minkowski, Euclidean, Manhattan, Chebyshev, Canberra, Quadratic, Mahalanobis, Correlation, Chi-square, Kendall) with a verified mini-example |
| [05_The_k_NN_Algorithm_Step_by_Step.md](05_The_k_NN_Algorithm_Step_by_Step.md) | The 5-step algorithm, pseudocode, tie-breaking, cost, and the odd/even contradiction on slide 11 |
| [06_Worked_Example_Predicting_Movie_Genre.md](06_Worked_Example_Predicting_Movie_Genre.md) | "Barbie" (7.4, 114) vs. four movies — distances 46/56/54/41, k = 1 and 3 → Comedy; plus the hidden feature-scale problem and a min–max scaled re-check |
| [07_Worked_Example_Paper_Tissue_Classification.md](07_Worked_Example_Paper_Tissue_Classification.md) | Paper-tissue (3, 7) with K = 3, squared distances 16/25/9/13, ranking, majority vote → Good |
| [08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons.md](08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons.md) | Research-enriched: feature scaling, speed (KD/ball trees), curse of dimensionality, weighted k-NN, pros & cons |

Every slide across the 20-slide deck is accounted for (slide 12 is only a "Numerical Example" section divider). Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference (the site adds two recreated SVG diagrams separately).

## Notes on this lecture

- **New algorithm family.** After Lecture 15's model-based logistic regression, this lecture introduces a *lazy, instance-based* classifier. No recap slides from earlier lectures, so no `00_` file.
- **Contradiction in the slides (flagged):** slide 3 says k should be **odd** to avoid ties; slide 11's footnote says k *must be even*. Odd is correct for two classes (and slide 4's 2-NN panel is itself a tie). Also, slide 6's own example (N = 100 → √N = 10) gives an even k; practice is to round to the nearest odd number. Details in [[05_The_k_NN_Algorithm_Step_by_Step]] and [[03_Issues_and_Choosing_the_Value_of_K]].
- **Numeric examples independently verified:**
  - Movie example: exact distances 46.004 / 56.013 / 54.0004 / 41.008 — match the instructor's rounded 46/56/54/41; k = 1 and k = 3 both → Comedy.
  - Paper-tissue example: squared distances 16/25/9/13, ranks 3/4/1/2, 3-NN = Good, Good, Bad → Good — all match.
- **Hidden problem in the movie example:** duration (gaps of 41–56) swamps rating (gaps of 0.2–1.2), so the result depends almost entirely on duration. Re-checked after min–max scaling: ranking unchanged, answer still Comedy — but the lesson (always scale features) is explained in [[06_Worked_Example_Predicting_Movie_Genre]] and [[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]].
- **Slide 7 details:** the figure spells "Canberra" as "Camberra", and its Correlation row as written is the correlation coefficient itself (a similarity); as a distance one uses 1 − r. Noted in [[04_Distance_Metrics]].
- **Research enrichment** for: history (Fix & Hodges, Cover & Hart 2× Bayes-error bound), eager vs. lazy learning, k-NN regression, Minkowski special cases and Mahalanobis, cross-validation for k, KD-/ball trees, curse of dimensionality, weighted k-NN.
- **No off-topic content** found — every slide belongs to k-NN classification.
