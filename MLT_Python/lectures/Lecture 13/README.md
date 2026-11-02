# Lecture 13 — Regression Basics (ES514: Machine Learning Techniques)

Source PDF: `Lecture 13 Regression_Basics.pdf` (24 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_What_Is_Regression_Relationships_and_Variables.md](01_What_Is_Regression_Relationships_and_Variables.md) | Cause-and-effect vs. functional relationships, the Y = f(X) definition, dependent/independent variable naming, the slide's paired examples, controllable vs. uncontrollable explanatory variables, and research-enriched history of the word "regression" (Francis Galton, 1886) |
| [02_Simple_Linear_Regression_Worked_Example_Home_Prices.md](02_Simple_Linear_Regression_Worked_Example_Home_Prices.md) | The 5-point area/price dataset, scatter plot and "best fit" line intuition, the Δ error and minimizing Σ(Δᵢ)², slope/intercept (y=mx+b), and an independently verified prediction for 3300 sqft (matches the slide's "628715" almost exactly) and 5000 sqft |
| [03_Multiple_Linear_Regression_Worked_Example_Home_Prices.md](03_Multiple_Linear_Regression_Worked_Example_Home_Prices.md) | The extended area/bedrooms/age/price dataset (with a genuine missing value), the multiple-regression equation with per-feature coefficients, "features" terminology, and a from-scratch fit showing why this 5-row version is numerically unstable — cross-checked against the real 6-row source dataset (a well-known ML tutorial) for sensible reference coefficients/predictions |
| [04_Types_of_Regression_Models_Overview.md](04_Types_of_Regression_Models_Overview.md) | All 5 types named on the slide — Simple/Multiple/Polynomial/Logistic/Ridge & Lasso — each fully explained via web research where the slide gave only a one-liner: overfitting risk in polynomial regression, the sigmoid/log-odds mechanism behind logistic regression, and the L1 vs. L2 (Lasso vs. Ridge) regularization distinction |
| [05_Least_Squares_Method_and_Worked_Example_Exam_Grades.md](05_Least_Squares_Method_and_Worked_Example_Exam_Grades.md) | The formal Least Squares formulas (b and a), the full 12-student midterm→final-exam worked derivation, research-enriched history (the Gauss–Legendre priority dispute over inventing the method), and an independent numeric re-verification of every step |

Every slide across the 24-slide deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

## Notes on this lecture

- **No recap slide** — this lecture opens directly with new material (Regression), so there is no `00_` recap file.
- **Two worked numeric examples, both independently verified by recomputing from scratch:**
  - The home-price simple linear regression: the slide's handwritten prediction of "628715" for a 3300 sqft house was confirmed to be a genuine least-squares fit of the given 5-point data (recomputed value: 628,715.75).
  - The exam-grade Least Squares worked example: recomputed the full 12-row table (means, sums, slope b=0.5816, intercept a=32.02, final prediction y=82.04 for midterm=86) and every number matched the slide to within ordinary rounding.
- **Multiple regression example flagged as under-determined.** Slide 12's area/bedrooms/age/price dataset (which has a genuine missing bedroom value) is only 5 rows for a 4-parameter model — fitting it directly gives an unstable, counter-intuitive (negative bedroom coefficient) result. Traced this dataset to a well-known public ML tutorial (codebasics) that uses the same table plus one extra 6th row; fitting the full 6-row version gives a sensible, correctly-signed model. This is noted explicitly in [[03_Multiple_Linear_Regression_Worked_Example_Home_Prices]] as a genuine "too few data points for too many features" teaching moment, not an error in the notes.
- **Letter-convention swap flagged:** slides 4–17 use `y = mx + b` (m=slope, b=intercept), while slides 21–24 switch to `y = a + bx` (a=intercept, b=slope) for the formal Least Squares derivation — same underlying line, different letters for slope vs. intercept. Called out explicitly in [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]] so it isn't mistaken for a contradiction.
- **Research enrichment done for:** the origin of the word "regression" (Galton, 1886 — [[01_What_Is_Regression_Relationships_and_Variables]]), history of the Least Squares method (Gauss vs. Legendre priority dispute — [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]]), and the three regression types the slides only name without explaining (Polynomial Regression's overfitting risk, Logistic Regression's sigmoid/log-odds mechanism, Ridge/Lasso's L2/L1 regularization — all in [[04_Types_of_Regression_Models_Overview]]).
- **No anomalies flagged** — every slide in this deck is on-topic for the course (an introduction to regression, building up from the definition through simple/multiple linear regression to a taxonomy of regression types and the formal least-squares derivation).
