# Lecture 14 — Multiple Linear Regression (ES514: Machine Learning Techniques)

Source PDF: `Lecture 14 Multiple Linear Regression.pdf` (15 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_Note_Slides_1_to_3.md](00_Recap_Note_Slides_1_to_3.md) | Short recap note — slides 1–3 are a verbatim repeat of Lecture 13's simple linear regression best-fit-line and Least Squares Method content; links back rather than re-explaining |
| [01_Multiple_Linear_Regression_Definition_and_General_Form.md](01_Multiple_Linear_Regression_Definition_and_General_Form.md) | Simple vs. multiple regression contrast, the general form y=a₀+a₁x₁+...+aₙxₙ+ε, predictor/dependent-variable/coefficient terminology, and the new error-term (ε) concept |
| [02_Worked_Exercise_Setup_Plant_Dry_Weight_Dataset.md](02_Worked_Exercise_Setup_Plant_Dry_Weight_Dataset.md) | The new 7-row plant-dry-weight/soil-organic-matter/soil-nitrogen dataset, the two-part task (find the equation, then predict for x1=5, x2=4), and the β₀/β₁/β₂ notation (a third naming convention for the same coefficients) |
| [03_Matrix_Approach_Normal_Equation_Worked_Solution.md](03_Matrix_Approach_Normal_Equation_Worked_Solution.md) | The full matrix method: building X and Y, the normal equation β=(XᵀX)⁻¹XᵀY (research-enriched with its derivation), the complete worked computation (XᵀX, its inverse, β), and the final prediction — every step independently re-verified numerically, plus a research-enriched note on why real ML tools use gradient descent instead of direct matrix inversion at scale |

Every slide across the 15-slide deck is accounted for. Each topic file (0–3) explains its content in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

## Notes on this lecture

- **Opens with a straight recap.** Slides 1–3 are a verbatim, word-for-word repeat of Lecture 13's simple-linear-regression best-fit-line slide and the Least Squares Method / exam-grade worked example — so `00_` is a short pointer file rather than a full re-explanation, per the established recap convention.
- **Genuinely new content starts at slide 4**: Multiple Linear Regression, first as a general formula (with three different letter-conventions used for the same coefficients across this lecture and Lecture 13 — m/b, a₀…aₙ, and now β₀/β₁/β₂ — flagged explicitly in [[02_Worked_Exercise_Setup_Plant_Dry_Weight_Dataset]] so it isn't mistaken for three different concepts), then solved end-to-end via the matrix / normal-equation method.
- **Full worked matrix example independently verified.** Recomputed the entire plant-dry-weight regression from scratch: XᵀX, (XᵀX)⁻¹, and β = (XᵀX)⁻¹XᵀY all matched the slide's handwritten values (β₀=51.5697, β₁≈1.49, β₂≈6.72), and the final prediction for x1=5, x2=4 matched the slide's stated answer of 85.8 exactly when using the slide's own rounded coefficients (85.95 using full precision — same answer, just rounding). See [[03_Matrix_Approach_Normal_Equation_Worked_Solution]] for the full step-by-step verification.
- **This dataset is well-conditioned**, unlike Lecture 13's 5-row home-price multiple-regression example (which had too few data points for its 4 unknowns and produced an unstable, counter-intuitive fit) — this one has 7 data points for 3 unknowns and produces small, sensible residuals, confirmed during verification.
- **Research enrichment done for:** the derivation of the normal equation β=(XᵀX)⁻¹XᵀY from the least-squares minimization (not shown on the slide), and a practical note on why direct matrix inversion doesn't scale to large datasets/feature counts (motivating gradient descent and connecting back to why Ridge regression, from [[04_Types_of_Regression_Models_Overview]] in Lecture 13, also happens to fix the "XᵀX not invertible" problem caused by correlated features) — both in [[03_Matrix_Approach_Normal_Equation_Worked_Solution]].
- **No anomalies flagged** — every slide is on-topic (multiple linear regression, building from the general formula through a fully worked matrix-algebra solution), aside from the expected recap-of-Lecture-13 opening.
