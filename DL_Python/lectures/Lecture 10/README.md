# Lecture 10 — Gradient Descent (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 10 Gradient Descent.pdf` — Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Read in full (all 28 slides).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Data_Model_Parameters_and_FFNN_Exercise.md](00_Recap_Data_Model_Parameters_and_FFNN_Exercise.md) | Recap: Lecture 9's Data/Model/Parameters framing and its solved FFNN exercise, linked back |
| [01_Evaluation_Metrics_Overview.md](01_Evaluation_Metrics_Overview.md) | Accuracy, Precision, Recall, F1, ROC/AUC (classification); MAE, MSE, RMSE, R² (regression) |
| [02_Simple_Linear_Regression_Intuition_Home_Price_Example.md](02_Simple_Linear_Regression_Intuition_Home_Price_Example.md) | The home-price scatter-plot example, best-fit line, residuals |
| [03_Simple_Linear_Regression_Worked_Example_Verified.md](03_Simple_Linear_Regression_Worked_Example_Verified.md) | The actual least-squares $m$, $b$ computed by hand and checked against the slide's $628,715 prediction |
| [04_Multiple_Linear_Regression_and_Features.md](04_Multiple_Linear_Regression_and_Features.md) | Extending to multiple features (area, bedrooms, age), coefficients, a flagged missing-data anomaly |
| [05_Loss_Function_and_the_Meaning_of_Gradient_Descent.md](05_Loss_Function_and_the_Meaning_of_Gradient_Descent.md) | What "gradient" and "descent" literally mean, and the cyclist/local-minimum analogy |
| [06_Types_of_Gradient_Descent_Revisited.md](06_Types_of_Gradient_Descent_Revisited.md) | Batch/Stochastic/Mini-batch, linked back to Lecture 0's fuller treatment |
| [07_Worked_Derivation_Gradient_Descent_for_Linear_Regression.md](07_Worked_Derivation_Gradient_Descent_for_Linear_Regression.md) | Full derivation of $dJ/dm$ for $\hat{y}=mx$, verified against the slide's own numbers |
| [08_Exercise_Two_Variable_Gradient_Descent_Solved.md](08_Exercise_Two_Variable_Gradient_Descent_Solved.md) | The slide's unsolved two-variable exercise, fully solved: partial derivatives, analytical minimum, and iterative convergence |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- **Recap handled per convention**: slides 2–3 repeat Lecture 9's Data/Model/Parameters framing and its worked FFNN exercise verbatim — [[00_Recap_Data_Model_Parameters_and_FFNN_Exercise]] links back rather than re-deriving.
- **A slide's numeric claim, verified**: slide 8 states a predicted price of $628,715 for a 3300 sq ft home but never shows the regression coefficients that produced it. [[03_Simple_Linear_Regression_Worked_Example_Verified]] independently fits the least-squares line by hand ($m\approx135.79$, $b\approx180{,}615$) and confirms this exact prediction — and also answers the slide's other, never-answered question (price at 5000 sq ft ≈ $859,555).
- **Two unsolved "Exercise" slides, both worked through**: slide 16 (repeated from Lecture 9, already solved there) and, new to this lecture, slide 28's two-variable cost function $J(m,b)=(m+b-5)^2+(2m-b-1)^2$ — [[08_Exercise_Two_Variable_Gradient_Descent_Solved]] derives both partial derivatives, solves for the exact minimum $(m,b)=(2,3)$, and demonstrates the iterative gradient-descent update converging toward it.
- **An anomaly flagged, not silently worked around**: the multiple-regression dataset (slide 13) has a missing `bedrooms` value for one row, with no explanation or handling shown in the slides — noted in [[04_Multiple_Linear_Regression_and_Features]] rather than guessed at, and that topic's own posed exercise (predict prices for two new homes) is left genuinely unsolved for the same reason, unlike the single-feature case which *was* fully solved.
- **Heavy cross-referencing to earlier lectures**: this lecture revisits several ideas already covered in depth elsewhere in this repo — the three types of gradient descent (Lecture 0), the general gradient descent update rule (Lecture 0), and the Data/Model/Parameters framing (Lecture 9) — each handled with a short recap-and-link rather than full re-derivation, per the usual convention.
- **Web research added**: the ROC/AUC definition and the R² formula/interpretation caveats in [[01_Evaluation_Metrics_Overview]] (the slide names these metrics but gives formulas for only some of them).
- **Diagrams added**: the home-price scatter plot with best-fit line and labeled residuals (slides 7/10), and the cyclist-on-a-landscape analogy for local vs. global minima (slide 21, sourced from GeeksforGeeks) — both recreated as inline SVGs in `site/diagrams.js`.
