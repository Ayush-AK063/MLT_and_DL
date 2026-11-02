# Topic 5: Choosing the Right Metric — Imbalance, Trade-offs, and Extensions (F-beta, Balanced Accuracy, MCC)

Source: Lecture 18, slides 3, 5 and 10 (the instructor's "depending on the class of interest" point and the exercise's A, P, R, S, F1 list). **This topic is enrichment from web research** — the slides state the metrics but not when to prefer which. Research covered: precision–recall trade-off, F-beta, balanced accuracy, Matthews correlation coefficient (MCC), medical vs. retrieval conventions.

---

## 1) Technical Explanation

**Which metric when?**

| Situation | Metric to emphasize | Why |
|---|---|---|
| Classes roughly balanced, errors equally costly | **Accuracy** | Simple and fine ([[01_Classification_Metrics_Accuracy_Precision_Recall_F1]]) |
| **Missing a positive is very costly** (cancer screening, fraud, safety defects) | **Recall / sensitivity** (also FNR) | A FN is the dangerous error |
| **False alarms are costly** (spam filter deleting real mail, legal flagging) | **Precision** | A FP is the dangerous error |
| Need balance of the two, positives are rare | **F1** | Harmonic mean punishes a weak side |
| Negatives matter too (medical devices) | **Specificity**, NPV | Retrieval ignores TN; diagnosis can't |
| Strongly imbalanced classes | Precision/recall/F1 or **balanced accuracy** or **MCC** — *not plain accuracy* | See below |

**1. The imbalance trap again.** In [[08_Confusion_Matrix_TP_TN_FP_FN]] (Lecture 17) a do-nothing model scored 99 % accuracy with 0 recall. Accuracy is dominated by the majority class.

**2. F-beta (research).** F₁ weights precision and recall equally. The generalization is
**F_β = (1 + β²)·P·R / (β²·P + R)**.
β = 2 weights recall ≈ 4× more than precision (use when misses are worse than false alarms); β = 0.5 weights precision ≈ 4× more. β = 1 gives F1. (Originates with C. J. van Rijsbergen's 1979 effectiveness measure.) *Check:* for P = 0.667, R = 0.8 (man/woman exercise): F₂ = 5(0.667)(0.8)/(4(0.667) + 0.8) = 2.667/3.467 = **0.769**, above F1 = 0.727 because recall (0.8) is the better number and F₂ rewards it.

**3. Balanced accuracy (research).** = (sensitivity + specificity)/2 — the average per-class recall. For the exercise: (0.80 + 0.60)/2 = **0.70** (coincidentally equal to accuracy because both classes have 5 samples). For the "all healthy" model on 990 healthy/10 sick it is (0 + 1)/2 = **0.50** — correctly revealing a useless classifier, where plain accuracy said 0.99.

**4. Matthews correlation coefficient (research).** MCC = (TP·TN − FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN)); ranges from −1 (always wrong) through 0 (no better than chance) to +1 (perfect), and uses **all four** cells. Exercise: (4·3 − 2·1)/√(6·5·5·4) = 10/√600 = **0.408** — a modest correlation, more sobering than 0.70 accuracy. F-scores ignore TN; MCC does not.

**5. The precision–recall trade-off and thresholds (research).** For a classifier that outputs a score or probability ([[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15), changing the decision threshold moves you along a trade-off: threshold ↓ → more predicted positives → recall ↑, precision usually ↓; threshold ↑ → the reverse. Sweeping the threshold and plotting the resulting rates gives the **ROC curve** (TPR vs. FPR — both defined in [[04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates]]), which Lecture 17's outline announced as part 3 but which has **still not appeared** in the Lecture 17 or 18 slides.

**6. Averaging over many classes (research, beyond the slides).** For more than two classes compute the metrics per class (one-vs-rest) and combine by **macro** average (simple mean, treats classes equally) or **micro** average (pool all TP/FP/FN, dominated by big classes).

**7. Estimating these metrics honestly.** Compute them on **test/validation data or via cross-validation**, never on training data ([[05_k_Fold_Cross_Validation]] from Lecture 17).

**Quick decision guide.** Ask: *What is the positive class? What does a FP cost? What does a FN cost? Are classes balanced?* Then pick the metric(s) accordingly and report more than one.

---

## 2) Simple English Explanation

There's no single "best" score — it depends on **what mistakes hurt most**.

- **Balanced groups, all mistakes equal?** Plain **accuracy** is fine.
- **Missing a positive is terrible** (like a deadly disease)? Watch **recall** — you want to catch every sick person, even if you raise a few false alarms.
- **False alarms are terrible** (like a spam filter hiding your job offer)? Watch **precision**.
- **Want one balanced number?** Use **F1**. If you want to lean toward catching more, use **F2**; toward fewer false alarms, **F0.5**.
- **Very uneven groups** (99 healthy, 1 sick)? Don't trust accuracy! A lazy model that always says "healthy" gets 99 %. Better: **balanced accuracy** (average of how well you do on each group — that lazy model scores only 50 %) or **MCC** (one fair score from −1 to +1 using all four counts).

Our 10-photo example: accuracy 0.70, but MCC is only 0.41 — a more honest picture of a modest model.

**The tug-of-war:** most models give a *score*, and you choose a cut-off. A low cut-off flags more things (catch more positives, more false alarms); a high cut-off flags fewer. Plotting this over all cut-offs gives the **ROC curve** (coming later).

Always judge on **fresh test data**, not data the model has already seen.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Koi ek "best" score nahi hota — ye isper depend karta hai ki **kaun si galti zyada mehengi padti hai.**

- **Groups balanced hain aur har galti barabar?** Seedhi **accuracy** theek hai.
- **Positive ko miss karna bahut bura hai** (jaise jaanleva bimaari)? **Recall** dekho — saare bimaar pakadne hain, chahe thode false alarm aa jaayein.
- **False alarm bahut bura hai** (jaise spam filter ne tumhara job offer mail chhupa diya)? **Precision** dekho.
- **Ek balanced number chahiye?** **F1** lo. Zyada pakadne ki taraf jhukna ho to **F2**, kam false alarm ki taraf jhukna ho to **F0.5**. (Formula: F_β = (1 + β²)·P·R / (β²·P + R). Humare exercise ka F2 ≈ 0.77.)
- **Groups bahut uneven hain** (99 healthy, 1 sick)? Accuracy par bharosa mat karo! Aalsi model jo hamesha "healthy" bole wo 99% accuracy le leta hai. Behtar: **balanced accuracy** (har group par performance ka average — wo aalsi model sirf 50% paata hai) ya **MCC** (−1 se +1 tak ek fair score jo chaaron counts use karta hai).

Humare 10-photo example mein accuracy 0.70 hai, par MCC sirf **0.41** — ye model ki zyada honest tasveer hai.

**Tug-of-war:** zyada tar models ek *score* dete hain aur tum cut-off (threshold) chunte ho. Kam cut-off = zyada cheezein positive flag hoti hain (zyada pakde, par false alarm bhi zyada); zyada cut-off = kam flag. Saare cut-offs par ye plot karne se **ROC curve** banta hai (ye Lecture 17 ke outline mein promise hua tha par abhi tak slides mein aaya nahi).

Aur hamesha score **naye test data** par nikaalo, us data par nahi jo model ne pehle dekha hai.
