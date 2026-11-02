# Topic 2: Overfitting vs. Underfitting — Bias vs. Variance

Source: Lecture 17, slide 5 ("Overfitting vs underfitting", with the instructor's "Bias vs Variance" note and the Degree 1 / Degree 4 / Degree 15 polynomial figure). Enriched with web research (bias–variance trade-off, validation curves).

---

## 1) Technical Explanation

**Definitions (slide 5).**
- **Overfitting** — *fitting the training data too precisely; usually leads to poor results on new data.*
- **Underfitting** — *the model does not fit the training data well.*

**The figure.** The same noisy samples (dark blue dots) come from a smooth **true function** (green curve). Three polynomial models (blue) are fitted:

| Panel | Model | Behaviour | Bias / Variance | Slide's remedy |
|---|---|---|---|---|
| **Degree 1** | straight line | misses the curve's shape even on the training points | **High bias, low variance** → *underfitting* | **Increase # of features or complexity of the model** |
| **Degree 4** | gentle curve | follows the true function closely | **good balance** (the small top figures: "low bias, low variance") | — |
| **Degree 15** | very wiggly curve | passes through/near almost every training point but oscillates wildly between and beyond them | **Low bias, high variance** → *overfitting* | **Get more training data, or reduce # of features or complexity of the model** |

The tiny top-right figures show the same story on a different dataset: "High variance" (overfitting — squiggly curve through all points), "High bias" (underfitting — flat line), "Low bias, low variance" (**good balance** — smooth curve).

**Bias vs. variance (instructor's note, with research).**
- **Bias** = systematic error from *too-simple assumptions*. A straight line can never bend to fit a parabola, no matter how much data you give it.
- **Variance** = sensitivity to the *particular training sample*. A degree-15 curve would change drastically if a few training points changed.
- Expected test error ≈ **bias² + variance + irreducible noise**. Making a model more complex lowers bias but raises variance, so there is a **sweet spot** — the **bias–variance trade-off**.

**How to diagnose in practice (research).** Compare training and validation error:

| Symptom | Diagnosis | Fix |
|---|---|---|
| Training error **high**, validation error high (close together) | Underfitting (high bias) | More complex model, more/better features, less regularization |
| Training error **low**, validation error **much higher** | Overfitting (high variance) | More data, fewer features, simpler model, regularization, early stopping |

This is exactly why training-set accuracy is untrustworthy ([[01_Why_System_Evaluation_and_Predictive_Modeling]]): an overfit model has excellent training accuracy and poor test accuracy. Evaluation methods in the rest of this lecture exist to expose that gap.

**Link to k-NN (Lecture 16).** In k-NN, **k = 1** is the overfitting end (low bias, high variance, noise-sensitive) and a **very large k** is the underfitting end ([[03_Issues_and_Choosing_the_Value_of_K]] from Lecture 16). Choosing k by cross-validation ([[05_k_Fold_Cross_Validation]]) finds the balance.

---

## 2) Simple English Explanation

Imagine drawing a line through dots on a graph.

- **Underfitting:** you use a plain **straight ruler** even though the dots clearly curve. The line is too simple — it's wrong on the dots you already have. It makes the *same kind of mistake* every time (that's **high bias**), but it doesn't change much if you move a few dots (**low variance**).
- **Good fit:** a smooth, gentle curve that follows the dots' real pattern.
- **Overfitting:** you use a super-wiggly wire that touches **every single dot**, including the random noise. On the old dots it looks perfect, but for any new dot it swings wildly. It is too sensitive to the exact dots (**high variance**), though on average it isn't "biased" (**low bias**).

**Cures:**
- Underfitting → make the model **more powerful** (more features or a more flexible model).
- Overfitting → give it **more data**, or **simplify** it (fewer features / simpler model).

Think of studying: underfitting = you barely studied; overfitting = you memorized the exact practice questions including their typos; good fit = you understood the ideas.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho graph par kuch dots hain aur tumhe unmein se ek line/curve khinchna hai.

- **Underfitting:** dots clearly curve ban rahe hain par tumne bas ek **seedha scale** (straight line) use kiya. Model bahut simple hai — jo dots pehle se pata hain unpe bhi galat hai. Ye hamesha ek jaisi galti karta hai (**high bias**) par dots thode idhar-udhar karo to zyada farak nahi padta (**low variance**). Slide ka **Degree 1** panel.
- **Good fit:** ek smooth curve jo dots ke asli pattern ko follow kare. **Degree 4** panel.
- **Overfitting:** tumne ek bahut wiggly taar use kiya jo **har ek dot ko chhoota hai**, noise ko bhi. Purane dots par perfect lagta hai, par koi naya dot aaye to wild swing karta hai. Ye dots ke exact position par bahut sensitive hai (**high variance**) par bias kam hai (**low bias**). **Degree 15** panel.

**Ilaaj (slide ke hisaab se):**
- Underfitting → model ko **zyada powerful** banao (zyada features ya zyada complex model).
- Overfitting → **zyada training data** lo, ya model ko **simple** karo (kam features / kam complexity).

Padhai ka example: underfitting = tumne kuch padha hi nahi; overfitting = tumne practice questions typos ke saath ratt liye; good fit = tumne concepts samjhe.

**k-NN se link (Lecture 16):** k = 1 overfitting wali taraf hai, bahut bada k underfitting wali taraf. Sahi k cross-validation se milta hai.
