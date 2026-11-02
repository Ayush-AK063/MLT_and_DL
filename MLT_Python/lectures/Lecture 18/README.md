# Lecture 18 — Classification Metrics (ES514: Machine Learning Techniques)

Source PDF: `Lecture 18 Classification Metrics.pdf` (10 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_Confusion_Matrix_and_the_Sick_People_Intuition.md](00_Recap_Confusion_Matrix_and_the_Sick_People_Intuition.md) | Recap of Lecture 17's confusion matrix (slide 1 is verbatim) + the instructor's plain-words reading of TP/FP/FN/TN (slide 2) |
| [01_Classification_Metrics_Accuracy_Precision_Recall_F1.md](01_Classification_Metrics_Accuracy_Precision_Recall_F1.md) | Accuracy, precision, recall (sensitivity), F1 with formulas, the harmonic-mean reason, precision–recall tug-of-war, verified check |
| [02_Precision_and_Recall_Document_Retrieval_Venn_Diagram.md](02_Precision_and_Recall_Document_Retrieval_Venn_Diagram.md) | The Relevant/Retrieved Venn diagram, mapping to TP/FP/FN/TN, worked retrieval example, Cranfield-experiments origin |
| [03_Worked_Exercise_Man_vs_Woman_Photo_Classification.md](03_Worked_Exercise_Man_vs_Woman_Photo_Classification.md) | The 10-photo exercise fully solved: TP 4, TN 3, FP 2, FN 1; accuracy 0.70, precision 0.667, recall = sensitivity 0.80, specificity 0.60, F1 0.727; class-swap check |
| [04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates.md](04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates.md) | Slide 10's full table (TPR, FNR, FPR, TNR, PPV, FDR, FOR, NPV, prevalence, LR+, LR−, DOR, F1) with every value computed for the exercise |
| [05_Choosing_the_Right_Metric_Imbalance_Trade_offs_and_Extensions.md](05_Choosing_the_Right_Metric_Imbalance_Trade_offs_and_Extensions.md) | Research-enriched: when to use which metric, F-beta, balanced accuracy, MCC, thresholds, macro/micro averaging |

Every slide across the 10-slide deck is accounted for (slides 7, 8, 9 are progressive builds of the same exercise-step slide). Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images (the site adds recreated SVG diagrams separately).

## Notes on this lecture

- **Continuation of Lecture 17.** Slide 1 repeats Lecture 17's confusion-matrix slide verbatim, and the right half of slide 3 ("Regression Metrics") repeats Lecture 17's handwritten regression page — both are linked back rather than re-explained ([[08_Confusion_Matrix_TP_TN_FP_FN]] and [[07_Performance_Metrics_Overview_and_Regression_Metrics]] from Lecture 17). The handwritten RMSE there still lacks its 1/N, as flagged in Lecture 17.
- **Lecture 17's promised outline is now delivered:** *Precision and recall* ✓. **ROC curves are still not covered** in this PDF — expect them in the next lecture. (Noted in [[05_Choosing_the_Right_Metric_Imbalance_Trade_offs_and_Extensions]].)
- **Exercise independently re-verified from the 10-row table:** TP = 4 (rows 3, 6, 7, 10), TN = 3 (2, 4, 8), FP = 2 (1, 9), FN = 1 (5) — matches the slide's counts and the handwritten 4/2/1/3 matrix. The slide only gives formulas for part (b); the final numbers (accuracy 0.70, precision 0.667, recall 0.80, specificity 0.60, F1 0.727) are worked out in these notes. Also checked the complement identities (TPR + FNR = 1, etc.) and recomputed everything with the roles of man/woman swapped.
- **Sensitivity = recall** (same formula TP/(TP + FN)); the exercise lists both only to show the medical vs. retrieval names for the same quantity.
- **Slide 10** is a Wikipedia table (source URL printed on the slide); "57 /14" is a leftover page label. Slide 4 uses the retrieval vocabulary, so the TP/FP/FN/TN mapping is spelled out explicitly.
- **Research enrichment** for: Cranfield experiments & van Rijsbergen's F-measure, why F1 uses the harmonic mean, F-beta, balanced accuracy, MCC, precision–recall threshold trade-off, sensitivity/specificity vs. precision/recall conventions.
- **No off-topic content** found.
