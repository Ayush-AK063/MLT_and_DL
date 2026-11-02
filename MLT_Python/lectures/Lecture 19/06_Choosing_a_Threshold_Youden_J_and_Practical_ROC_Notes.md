# Topic 6: Choosing a Threshold and Practical ROC Notes (Youden's J, Convex Hull, Multi-class, Pitfalls)

Source: Lecture 19, slides 4–6, 10, 13 (threshold idea, "Different classifiers can be compared", convex hull). **Enrichment topic from web research** — the slides show ROC curves but do not say how to pick the operating threshold or how ROC extends beyond two classes. Research covered: Youden's J, ROC convex hull, one-vs-rest AUC, AUC limitations.

---

## 1) Technical Explanation

**1. A ROC curve shows all thresholds — but you must deploy one.** Each point on the curve is a threshold ([[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]]). Common ways to pick it:

| Rule | Idea |
|---|---|
| **Youden's J** | Maximize **J = TPR − FPR = sensitivity + specificity − 1**: the point farthest above the diagonal |
| **Closest to (0, 1)** | Minimize distance to the "Perfection" corner: √(FPR² + (1 − TPR)²) |
| **Cost-based** | Choose the point where cost(FN)·(miss rate) + cost(FP)·(false-alarm rate) is lowest; if misses are expensive, accept a higher FPR for a higher TPR (move up-right) |
| **Constraint-based** | e.g. "FPR must be ≤ 0.05" or "recall ≥ 0.9" — take the best point satisfying it |

*Worked (Example 1 from [[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]], verified):* J at the ten thresholds = 0.2 (≥0.90), 0.4 (≥0.80), 0.2 (≥0.70), 0.4 (≥0.60), **0.6 (≥0.55)**, 0.4, 0.2, 0.0, 0.2, 0.0 → the best cut-off is **0.55** (TPR 0.8, FPR 0.2). For Example 2 ([[05_Worked_Example_2_Trapezoid_Rule_AUC_0_64]]) J at the ten thresholds = 0.2, 0.0, 0.2, **0.4** (≥ 0.66: TPR 0.6, FPR 0.2), 0.2, **0.4** (≥ 0.55: TPR 0.8, FPR 0.4), 0.2, 0.0, −0.2, 0.0 → best J is only **0.4** (a weaker model has a smaller best J than Example 1's 0.6).

**2. ROC convex hull (slide 13).** The solid outer line on the slide. Any point on a straight segment between two ROC points can be achieved by **randomly choosing between the two classifiers/thresholds** with suitable probabilities. So points *below* the hull are never optimal under any class/cost distribution; the hull is the set of potentially optimal operating points (research).

**3. Comparing classifiers (slide 6, 10).** If curve A lies above curve B everywhere → A dominates. If they cross, compare in the region of interest (e.g. low FPR) or use **partial AUC**; AUC alone averages over regions you may not care about.

**4. More than two classes (slide 3: confusion matrix "easily generalizes to multi-class").** ROC is defined for binary problems. For K classes: **one-vs-rest** — treat each class as positive vs. all others, draw K curves, and average the AUCs (**macro** = simple mean; **micro** = pooled counts).

**5. Pitfalls (research).**
- **Imbalanced data:** ROC/AUC can look good when precision is poor → use PR curve ([[03_PR_Curves_vs_ROC_Curves]]).
- **AUC ignores calibration:** two models with the same ranking have the same AUC even if one's probabilities are nonsense.
- **AUC is not accuracy:** it does not tell you performance at a particular threshold.
- **AUC < 0.5** ⇒ inverted predictions (flip them) — not "can't separate" ([[02_ROC_Shapes_AUC_and_Comparing_Models]]).
- **Tied scores** create diagonal segments; use the trapezoid rule.
- Estimate AUC on **test or cross-validated** predictions, never training data ([[05_k_Fold_Cross_Validation]] from Lecture 17).

**6. Connection to earlier lectures.** The threshold is exactly the 0.5 cut-off of logistic regression ([[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15), which can be moved; for k-NN ([[05_The_k_NN_Algorithm_Step_by_Step]] from Lecture 16) the "score" can be the fraction of the k neighbors that vote positive.

---

## 2) Simple English Explanation

The ROC curve shows **every possible cut-off** at once, but in real life you must pick **one**. Options:

- **Best balance (Youden's J):** pick the cut-off where (catch rate − false-alarm rate) is largest — the point **farthest above the diagonal**. In Example 1 that's cut-off 0.55 (catch 80 %, false alarms 20 %).
- **Closest to the perfect corner:** pick the dot nearest the top-left.
- **Based on cost:** if missing a sick person is much worse than a false alarm, accept more false alarms to catch more (move up and right on the curve).
- **Based on a rule:** e.g. "false alarms must stay under 5 %".

**Other useful facts:**
- **Convex hull:** by randomly switching between two cut-offs you can get any point on the straight line between them, so dots below the outer line are never the best choice.
- **Comparing two models:** if one curve is above the other everywhere, it's simply better. If they cross, think about which region matters to you.
- **More than two groups:** do "one group versus everyone else" for each group and average.
- **Be careful:** with very rare positives the ROC looks too rosy (use PR curve); AUC doesn't tell you whether the probabilities themselves are accurate; always compute it on **test data**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

ROC curve **saare possible cut-offs** ek saath dikhata hai, par asli zindagi mein tumhe **ek hi** chunna padta hai. Tareeke:

- **Best balance (Youden's J):** wo cut-off jahan (catch rate − false-alarm rate) sabse bada ho — yaani point jo **diagonal se sabse upar** ho. Example 1 mein ye cut-off **0.55** hai (catch 80%, false alarm 20%, J = 0.6).
- **Perfect corner ke sabse paas:** top-left ke sabse nazdeek wala dot.
- **Cost ke hisaab se:** agar bimaar ko miss karna false alarm se bahut bura hai, to zyada false alarm accept karke zyada pakdo (curve par upar-daayein jao).
- **Rule ke hisaab se:** jaise "false alarm 5% se kam hi rahe."

**Aur kaam ki baatein:**
- **Convex hull (slide 13):** do cut-offs ke beech randomly switch karke tum unke beech ki seedhi line ka koi bhi point pa sakte ho, isliye outer line ke neeche wale dots kabhi best nahi hote.
- **Do models compare karna:** agar ek curve har jagah doosre se upar hai to wo seedha behtar. Agar curves cross karein, to dekho tumhe kaun sa region zyada zaroori hai.
- **2 se zyada classes:** har class ke liye "wo class vs baaki sab" karke curve banao aur AUCs ka average lo.
- **Savdhaani:** bahut rare positives mein ROC zyada accha dikhta hai (tab PR curve use karo); AUC ye nahi batata ki probabilities khud sahi hain ya nahi; aur hamesha **test data** par nikaalo.
- **AUC < 0.5** matlab predictions ulte hain — flip karo, model "bekaar" nahi hai.

Connection: logistic regression ka 0.5 cut-off (Lecture 15) bhi ek threshold hai jise badla ja sakta hai — ROC se pata chalta hai badalne par kya hoga.
