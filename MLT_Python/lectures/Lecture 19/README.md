# Lecture 19 — ROC Curves and AUC (ES514: Machine Learning Techniques)

Source PDF: `Lecture 19 ROC and AUC.pdf` (15 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_TPR_FPR_and_the_Blood_Test_Threshold_Idea.md](00_Recap_TPR_FPR_and_the_Blood_Test_Threshold_Idea.md) | Outline recap, the blood-test dataset with threshold 45, TPR/FPR recap and the instructor's "P ← P / N ← P" reading trick |
| [01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying.md](01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying.md) | ROC definition, ranking by score, one confusion matrix per threshold, the Observations list ((0,0), (1,1), diagonal…), radar origin, how to build the curve |
| [02_ROC_Shapes_AUC_and_Comparing_Models.md](02_ROC_Shapes_AUC_and_Comparing_Models.md) | Ideal / random / typical shapes, AUC meaning (incl. the ranking-probability interpretation), trapezoid area formula, comparing multiple curves, the "AUC near 0" correction |
| [03_PR_Curves_vs_ROC_Curves.md](03_PR_Curves_vs_ROC_Curves.md) | PR vs. ROC, when each is appropriate, a worked imbalanced-data example (FPR 4 % but precision 17 %) |
| [04_Worked_Example_1_Building_a_ROC_Curve_and_AUC.md](04_Worked_Example_1_Building_a_ROC_Curve_and_AUC.md) | Example 1: threshold-by-threshold TPR/FPR table, the ROC points, convex hull, **AUC = 0.76** (computed here) |
| [05_Worked_Example_2_Trapezoid_Rule_AUC_0_64.md](05_Worked_Example_2_Trapezoid_Rule_AUC_0_64.md) | Example 2: the table, trapezoid-rule area, **AUC = 0.64** (verified), pair-counting check |
| [06_Choosing_a_Threshold_Youden_J_and_Practical_ROC_Notes.md](06_Choosing_a_Threshold_Youden_J_and_Practical_ROC_Notes.md) | Research-enriched: Youden's J, cost-based thresholds, convex hull, multi-class AUC, pitfalls |

Every slide across the 15-slide deck is accounted for (slides 12–13 and 14–15 are two-slide sets for Examples 1 and 2). Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images (the site adds recreated SVG diagrams separately).

## Notes on this lecture

- **Completes Lecture 17's promised outline:** Metrics (L17) → Precision/recall (L18) → **ROC curves (L19)**. The first slide is that same outline again; "68 /14", "76 /14" etc. are leftover page labels from the source deck.
- **Both worked examples re-verified from scratch:** every TP / FP / TPR / FPR entry in both tables matches the slides. **Example 2's AUC = 0.64** (the instructor's circled answer) is reproduced by the trapezoid rule and by pair-counting (16/25). **Example 1's AUC = 0.76** is not stated on the slide (the area is only shaded); we computed it by trapezoid and by pair-counting (19/25). The instructor's handwritten points for Example 1 — (0,0.2), (0,0.4), (0.2,0.4), (0.2,0.6), (0.2,0.8), (0.4,0.8), (0.6,0.8), (0.8,0.8), (0.8,1.0), (1,1) — all match.
- **Slide 11 imprecision (flagged):** "Low AUC (close to 0): the model struggles to differentiate" is not quite right — AUC near 0 means the model is *inverted* (rank-reversed), and flipping it gives AUC near 1; the least-informative value is 0.5. See [[02_ROC_Shapes_AUC_and_Comparing_Models]].
- **Slide 9 is schematic (flagged):** it is "adapted from [1]" and the five confusion matrices (counts of 100 positives / 100 negatives) do not map one-to-one onto the 9 listed instances (e.g. the 0.70 matrix shows 6 TP while the 9 rows would give 5). Described as an illustration of the idea. See [[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]].
- **Slide 2 (blood test)** is an infographic-style slide showing only steps 1–2 (data + threshold 45); the data is perfectly separable, so its ROC curve would have AUC = 1 (our observation).
- **Slide 3's FPR handwriting** is read as FP/(TN + FP), consistent with the printed formula on the slide.
- **Research enrichment** for: ROC's origin in WWII radar signal detection, AUC as the Wilcoxon–Mann–Whitney probability, AUC < 0.5 meaning, PR plots for imbalanced data (Saito & Rehmsmeier 2015), Youden's J, ROC convex hull, one-vs-rest AUC.
- **No off-topic content** found.
