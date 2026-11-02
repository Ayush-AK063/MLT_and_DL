# Lecture 12 — EWMA and RMSProp Optimizers (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 12 EWMA and RMSProp Optimizers.pdf` — Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Read in full (all 12 pages supplied — see the slide-numbering gaps noted below; this PDF itself is not a contiguous slide deck).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Momentum_Optimizer_Visuals.md](00_Recap_Momentum_Optimizer_Visuals.md) | Recap: the Momentum diagrams from Lecture 11, linked back |
| [01_Momentum_Update_Rule_BGD_vs_MBGD_Paths.md](01_Momentum_Update_Rule_BGD_vs_MBGD_Paths.md) | BGD's smooth path vs. MBGD's noisy path, side by side; ADAMW/ADAM/RMS-PROP grouped |
| [02_What_Is_an_Exponentially_Weighted_Moving_Average.md](02_What_Is_an_Exponentially_Weighted_Moving_Average.md) | EWMA introduced generically, with a classic noisy-data-smoothing illustration |
| [03_Deriving_the_EWMA_Recurrence.md](03_Deriving_the_EWMA_Recurrence.md) | The full $V_1$–$V_4$ unrolled derivation, verified — and a $V_0$ initialization discrepancy resolved |
| [04_General_EWMA_Formula_and_Effect_of_Beta.md](04_General_EWMA_Formula_and_Effect_of_Beta.md) | The closed-form EWMA formula, and why $\beta^t\to0$ as $t$ grows |
| [05_Comparing_Different_Beta_Values_Worked_Example.md](05_Comparing_Different_Beta_Values_Worked_Example.md) | β=0.6 vs. 0.9 vs. 0.95, visually compared (and a flagged slide-number gap) |
| [06_Momentum_Applied_to_Gradient_Descent_Updates.md](06_Momentum_Applied_to_Gradient_Descent_Updates.md) | The full $V_{dW}$/$V_{dB}$ Momentum update rule, reconciled against Lecture 0's formula |
| [07_RMSprop_Root_Mean_Square_Propagation.md](07_RMSprop_Root_Mean_Square_Propagation.md) | RMSprop derived from EWMA-of-squared-gradients, plus the overshooting/epsilon explanation |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- **Recap handled per convention**: slides 1–4 repeat Lecture 11's Momentum diagrams (and its already-flagged unrelated car-shopping checklist anomaly) verbatim — [[00_Recap_Momentum_Optimizer_Visuals]] links back rather than re-explaining or re-flagging.
- **This PDF is not a contiguous slide deck — flagged, not silently absorbed**: the printed slide-corner numbers jump from 23 to 28 (four slides, 24–27, missing) and then from 28 to 30 (one more slide, 29, missing). Both gaps are called out explicitly in [[05_Comparing_Different_Beta_Values_Worked_Example]] and [[06_Momentum_Applied_to_Gradient_Descent_Updates]] respectively — nothing was reconstructed or guessed for the missing slides.
- **A discrepancy in the source slide's own math, resolved**: slide 22 (numbered) states $V_0=\theta$ in its initial annotation, but its own worked-out expansion is only consistent with $V_0=0$. [[03_Deriving_the_EWMA_Recurrence]] independently re-derives $V_1$ through $V_4$ from $V_0=0$ and confirms this matches the slide's own red-annotated working exactly — the "$V_0=\theta$" note is treated as an early, superseded draft.
- **A real gap in coverage, flagged via web research**: this lecture's EWMA derivation never mentions **bias correction** — the standard fix for the fact that initializing at $V_0=0$ makes the earliest few smoothed values a severe underestimate. [[03_Deriving_the_EWMA_Recurrence]] notes this explicitly and ties it to the bias-correction step already covered for Adam in Lecture 0's [[09_Adam]].
- **A formula reconciled, not just accepted at face value**: this lecture's Momentum update rule ($V_{dW}=\beta V_{dW,\text{prev}}+(1-\beta)dW$, then $W=W-\alpha V_{dW}$) looks different from Lecture 0's ($v_t=\gamma v_{t-1}+\eta\nabla_\theta J(\theta)$) because the learning rate is factored in at a different point — [[06_Momentum_Applied_to_Gradient_Descent_Updates]] explains why these are the same underlying idea, not two competing formulas.
- **A concrete numeric scenario, verified**: the "Problem of Overshooting" explanation on the RMSprop slide (small/zero $S_{dB}$ plus a large $dB$ causing a huge update) is worked through explicitly in [[07_RMSprop_Root_Mean_Square_Propagation]] to show exactly why $\epsilon=10^{-8}$ exists in the formula.
- **Lecture ends mid-topic**: this deck covers RMSprop's core update rule but stops before combining it with Momentum into Adam (already covered from a different angle in Lecture 0's [[09_Adam]]) — a natural candidate for whatever the next lecture in this course turns out to be.
- **Diagrams added**: a generic noisy-scatter-with-EWMA-line illustration (slide 21), and a three-way β=0.6/0.9/0.95 smoothness comparison (slide 28) — both recreated as inline SVGs in `site/diagrams.js`.
