# Lecture 9 — Classification and Prediction (ES514: Machine Learning Techniques)

Source PDF: `Lecture 9 Classification and Prediction.pdf` (16 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Classification_and_Prediction_Overview.md](00_Classification_and_Prediction_Overview.md) | What classification vs. prediction (regression) means; named classifier/prediction algorithm families; real-world applications |
| [01_Classification_Two_Step_Process.md](01_Classification_Two_Step_Process.md) | Model Construction (training set) vs. Model Usage (accuracy estimation, independent test set, overfitting) |
| [02_Training_Validation_and_Test_Sets.md](02_Training_Validation_and_Test_Sets.md) | The three-way data split — training, validation, testing — their distinct roles, and why all three must stay separate |
| [03_Bias_and_Variance.md](03_Bias_and_Variance.md) | Bias (underfitting) vs. Variance (overfitting), the house-price underfitting/appropriate-fitting/overfitting curve example, and the full bias-variance error decomposition |
| [04_Addressing_Overfitting_and_Underfitting.md](04_Addressing_Overfitting_and_Underfitting.md) | Concrete remedies for both problems — model complexity, data quality/quantity, early stopping, Ridge/Lasso regularization, Dropout |
| [05_General_Approach_for_Building_Classification_Model.md](05_General_Approach_for_Building_Classification_Model.md) | The Induction (train → model) / Deduction (model → predictions) diagram, using the generic Attrib1/2/3 training/test set example |
| [06_Decision_Tree_Classification_and_Induction.md](06_Decision_Tree_Classification_and_Induction.md) | Decision tree structure and induction, the classic `buys_computer` worked example, and trees as a "disjunction of conjunctions" |

Every slide across the 16-slide deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

## Notes on this lecture

- **No recap slide** at the start of this deck — Lecture 9 opens a genuinely new unit (Classification and Prediction), so there is no `00_` recap file this time; numbering simply starts at the first topic.
- **Enriched with web research** for: the bias-variance error decomposition (Bias² + Variance + Irreducible Error), the history and mechanics of the ID3 decision-tree-induction algorithm (Ross Quinlan, 1986) and its successor C4.5, Ridge (L2) vs. Lasso (L1) regularization, and Dropout (Srivastava et al., 2014) — none of these were spelled out in detail on the slides themselves, only named or shown as diagrams.
- **Verified correction**: slide 16's disjunction-of-conjunctions formula, as extracted from the source PDF's text layer, reads `age = >=30` for the first clause. This contradicts the tree diagram on the same slide, whose leftmost branch is clearly labelled `age <= 30`. This has been treated as a PDF text-extraction artifact (a "≤" glyph misrendering) rather than a real change to the logic, and the corrected form (`age <= 30 AND student = yes`) is used throughout [[06_Decision_Tree_Classification_and_Induction]]. Flagging here in case a future lecture's recap references this slide differently.
- The `buys_computer` decision tree example (slides 14–16) and the generic Training-Set/Test-Set Induction/Deduction diagram (slide 13) are both well-known, classic illustrations from the standard data mining textbook tradition (Han & Kamber's *Data Mining: Concepts and Techniques*, and Tan/Steinbach/Kumar's *Introduction to Data Mining*, respectively) — flagged for context, not as an anomaly.
- **Not yet added to the site** (`site/content.js`) per instruction — run `build_site.py` only after this lecture is reviewed and approved.
