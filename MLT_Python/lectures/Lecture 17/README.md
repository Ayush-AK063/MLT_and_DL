# Lecture 17 — Performance Metrics & Model Evaluation (ES514: Machine Learning Techniques)

Source PDF: `Lecture 17 Performance Metrics.pdf` (21 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Why_System_Evaluation_and_Predictive_Modeling.md](01_Why_System_Evaluation_and_Predictive_Modeling.md) | Why evaluate, predictive modeling examples (classification vs. regression), why training-set performance is misleading |
| [02_Overfitting_vs_Underfitting_Bias_and_Variance.md](02_Overfitting_vs_Underfitting_Bias_and_Variance.md) | Overfitting vs. underfitting, the Degree 1 / 4 / 15 figure, high bias vs. high variance and their fixes, link to k in k-NN |
| [03_Train_Test_Split_Large_Data_and_Validation_Set.md](03_Train_Test_Split_Large_Data_and_Validation_Set.md) | Train/test split (2/3–1/3), the 3-step evaluation diagrams, and why tuning needs a separate validation set |
| [04_Holdout_Stratified_Sampling_and_the_Small_Data_Problem.md](04_Holdout_Stratified_Sampling_and_the_Small_Data_Problem.md) | Holdout, stratified sampling, why one split is unreliable on small data |
| [05_k_Fold_Cross_Validation.md](05_k_Fold_Cross_Validation.md) | k-fold CV, stratified ten-fold, repeated CV, a worked averaging example, why ten (Kohavi 1995) |
| [06_The_Bootstrap_and_Out_of_Bag_Validation.md](06_The_Bootstrap_and_Out_of_Bag_Validation.md) | Sampling with replacement, out-of-bag testing, the verified 63.2 % / 36.8 % result, .632 bootstrap |
| [07_Performance_Metrics_Overview_and_Regression_Metrics.md](07_Performance_Metrics_Overview_and_Regression_Metrics.md) | Metric outline, MAE / MSE / RMSE / R² with a verified worked example, MAE vs. RMSE, negative R², normalized errors |
| [08_Confusion_Matrix_TP_TN_FP_FN.md](08_Confusion_Matrix_TP_TN_FP_FN.md) | Confusion matrix, Type I/II errors, worked 100-patient example, why accuracy can mislead |

Every slide across the 21-slide deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images (the site adds recreated SVG diagrams separately).

## Notes on this lecture

- **A new kind of lecture:** not a new algorithm, but *how to judge any algorithm* (Lectures 13–16's models). No verbatim recap slides, so no `00_` file.
- **Deck is incomplete / ends early (flagged):** slides 17–18 announce an outline — *1. Metrics, 2. Precision and recall, 3. ROC curves* — but this PDF only delivers the **Metrics** part (regression metrics + confusion matrix). Precision, recall, F1 and ROC curves are **not in this PDF**; they are presumably in the next lecture. Slide 18 duplicates slide 17, and the "17 /14, 18 /14, 19 /14" marks are leftover page labels. Slide 20 (handwritten regression metrics) has no slide title/number. If a later PDF covers precision/recall/ROC, link back to [[08_Confusion_Matrix_TP_TN_FP_FN]].
- **Formula correction (flagged):** the handwritten RMSE on slide 20 omits the 1/N inside the square root; RMSE = √MSE. Documented with a numeric check in [[07_Performance_Metrics_Overview_and_Regression_Metrics]].
- **Verified:** regression-metric worked example (MAE 0.875, MSE 1.3125, RMSE 1.1456, R² 0.644, NRMSE_range 0.229); bootstrap out-of-bag probability (1 − 1/n)ⁿ = 0.328 / 0.349 / 0.366 / 0.368 for n = 5 / 10 / 100 / 1000 → e⁻¹; CV example average (0.82); stratified-split counts; confusion-matrix accuracy (0.85) and the 99 % accuracy-on-imbalanced-data trap. All of these worked examples are our own illustrations — the slides give formulas and diagrams but no numbers.
- **Slide-5 diagram detail:** the top-right mini figures (High variance / High bias / Low bias, low variance) are consistent with the Degree-1/4/15 panels, so bias/variance labels are used together.
- **Research enrichment** for: why training error is optimistic, bias–variance trade-off and diagnosing it from train vs. validation error, Kohavi's 1995 study (stratified 10-fold CV), leave-one-out, the .632 bootstrap, MAE vs. RMSE robustness, negative R², normalized RMSE/MAE options, Type I/II errors.
- **Connection to Lecture 16:** choosing k in k-NN is exactly a validation/cross-validation task; k = 1 is the overfitting extreme ([[02_Overfitting_vs_Underfitting_Bias_and_Variance]]).
- **No off-topic content** found.
