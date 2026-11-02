# Lecture 15 — Logistic Regression (ES514: Machine Learning Techniques)

Source PDF: `Lecture 15 Logistic Regression.pdf` (26 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Linear_Regression_vs_Classification_and_Types.md](01_Linear_Regression_vs_Classification_and_Types.md) | The continuous-vs-categorical distinction between regression and classification, why "logistic regression" is actually a classification technique despite its name, and Binary vs. Multiclass classification types |
| [02_Why_a_Straight_Line_Fails_for_Classification_Worked_Example.md](02_Why_a_Straight_Line_Fails_for_Classification_Worked_Example.md) | The age/have_insurance dataset (traced to its real public source — codebasics' `insurance_data.csv`), the scatter plot, and a concrete demonstration of why a straight-line best-fit breaks down for 0/1 data |
| [03_The_Sigmoid_Function_and_Decision_Boundary.md](03_The_Sigmoid_Function_and_Decision_Boundary.md) | The sigmoid formula, why it's mathematically guaranteed to stay between 0 and 1, the 0.5 Yes/No threshold, the log-odds/logit connection (research-enriched, not on the slide), and the research-enriched history of the logistic curve (Verhulst, 1838) |
| [04_Multiclass_Classification_and_Handwritten_Digit_Recognition.md](04_Multiclass_Classification_and_Handwritten_Digit_Recognition.md) | The binary-vs-multiclass recap, the handwritten-digit-recognition example, research-enriched MNIST dataset history (Yann LeCun), and how logistic regression itself extends from 2 classes to 10 (One-vs-Rest / Softmax — not explained on the slide) |
| [05_Worked_Example_Logistic_Regression_Exam_Pass_Probability.md](05_Worked_Example_Logistic_Regression_Exam_Pass_Probability.md) | The full pass/fail worked example using a given log-odds equation — both the forward direction (hours → probability, 88%) and the reverse direction (target probability → required hours, 33.47), independently re-verified numerically |

Every slide across the 26-slide deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

## Notes on this lecture

- **No verbatim recap this time.** Unlike Lecture 14, this lecture doesn't repeat earlier slides word-for-word — slide 1 briefly restates the y=mx+c vocabulary as a springboard into the new material, so no `00_` recap file was needed; all content is genuinely new or meaningfully extends [[04_Types_of_Regression_Models_Overview]] from Lecture 13 (which introduced logistic regression in one line — this lecture builds the full mechanism).
- **Both worked numeric examples independently verified:**
  - The exam pass/fail log-odds example: recomputed Q1 (88% probability at 33 hours) and Q2 (33.47 hours needed for >95% probability) from scratch — both matched the slide's handwritten answers essentially exactly.
- **Traced the age/have_insurance dataset to its real source**: the well-known "codebasics" logistic regression tutorial's `insurance_data.csv` (same as the multiple-regression dataset traced in Lecture 13). The slide's 15-row table is the first 15 rows of that public 27-row file; the extra ~85-year-old data point shown in later scatter plots isn't part of the original file and looks like an instructor-added synthetic stress-test point — flagged explicitly in [[02_Why_a_Straight_Line_Fails_for_Classification_Worked_Example]].
- **Research enrichment done for:** the history of the sigmoid/logistic curve (Verhulst, 1838, population growth — long before machine learning existed), the log-odds/logit mathematical connection to sigmoid (not derived on the slide), the MNIST dataset's origin (Yann LeCun, 1990s), and how binary logistic regression extends to multiclass problems via One-vs-Rest or Softmax (neither mechanism is explained on the slide, which only shows the 10-class digit example conceptually).
- **No anomalies flagged** — every slide is on-topic for an introduction to logistic regression (the regression-vs-classification distinction, why a straight line fails for 0/1 data, the sigmoid function, a multiclass preview, and a full worked log-odds example).
