# Topic 4: Summaries of the Confusion Matrix — The Full Table of Rates

Source: Lecture 18, slide 10 ("Summaries of the confusion matrix": "Different metrics can be computed from the confusion matrix, depending on the class of interest" — the large colour-coded table taken from the Wikipedia "Precision and recall" page). Every formula applied to the man/woman exercise and verified.

---

## 1) Technical Explanation

The slide shows one big table: the 2×2 confusion matrix (columns **True condition: positive / negative**, rows **Predicted condition: positive / negative**) surrounded by every ratio you can compute from it. The key message: *which metric you quote depends on the class of interest.* (The "57 /14" at the bottom is a stray page label.)

**The four cells, with their alternate names on the slide.**
- **True positive** — also called **Power**
- **False positive** — **Type I error**
- **False negative** — **Type II error**
- **True negative**

**Rates read along the columns (conditioned on the TRUE condition) — "of all really positive / really negative…"**

| Name (aliases on slide) | Formula | Meaning |
|---|---|---|
| **True positive rate (TPR)** = **Recall** = **Sensitivity** = probability of detection | Σ TP / Σ condition positive = TP/(TP + FN) | Fraction of real positives found |
| **False negative rate (FNR)** = **Miss rate** | FN/(TP + FN) = 1 − TPR | Fraction of real positives missed |
| **False positive rate (FPR)** = **Fall-out** = probability of false alarm | FP/(FP + TN) = 1 − TNR | Fraction of real negatives wrongly flagged |
| **True negative rate (TNR)** = **Specificity (SPC)** = **Selectivity** | TN/(FP + TN) | Fraction of real negatives correctly cleared |

**Rates read along the rows (conditioned on the PREDICTION) — "of all predicted positive / negative…"**

| Name | Formula | Meaning |
|---|---|---|
| **Positive predictive value (PPV)** = **Precision** | Σ TP / Σ predicted condition positive = TP/(TP + FP) | When it says positive, how often right? |
| **False discovery rate (FDR)** | FP/(TP + FP) = 1 − PPV | When it says positive, how often wrong? |
| **False omission rate (FOR)** | FN/(FN + TN) = 1 − NPV | When it says negative, how often wrong? |
| **Negative predictive value (NPV)** | TN/(FN + TN) | When it says negative, how often right? |

**Whole-population summaries.**

| Name | Formula |
|---|---|
| **Prevalence** | Σ condition positive / Σ total population = (TP + FN)/N |
| **Accuracy (ACC)** | (Σ TP + Σ TN)/Σ total population |
| **F₁ score** | 1 / ( (1/recall + 1/precision) / 2 ) = 2PR/(P + R) — the harmonic mean ([[01_Classification_Metrics_Accuracy_Precision_Recall_F1]]) |

**Ratios that combine the rates.**

| Name | Formula | Meaning |
|---|---|---|
| **Positive likelihood ratio (LR+)** | TPR / FPR | How much more likely a positive prediction is for a real positive than for a real negative; > 1 is useful, bigger is better |
| **Negative likelihood ratio (LR−)** | FNR / TNR | How much *less* likely a negative prediction is for a real positive; < 1 is useful, smaller is better |
| **Diagnostic odds ratio (DOR)** | LR+ / LR− | Single number of overall discriminating power (1 = useless) |

**Every formula on the man/woman exercise** ([[03_Worked_Exercise_Man_vs_Woman_Photo_Classification]]: TP = 4, TN = 3, FP = 2, FN = 1, N = 10, woman = positive):

| Metric | Calculation | Value |
|---|---|---|
| Prevalence | (4 + 1)/10 | 0.50 |
| Accuracy | (4 + 3)/10 | 0.70 |
| TPR / Recall / Sensitivity | 4/5 | 0.80 |
| FNR (miss rate) | 1/5 | 0.20 |
| TNR / Specificity | 3/5 | 0.60 |
| FPR (fall-out) | 2/5 | 0.40 |
| PPV / Precision | 4/6 | 0.667 |
| FDR | 2/6 | 0.333 |
| NPV | 3/4 | 0.75 |
| FOR | 1/4 | 0.25 |
| F₁ | 2·4/(8 + 2 + 1) | 0.727 |
| LR+ | 0.80 / 0.40 | 2.0 |
| LR− | 0.20 / 0.60 | 0.333 |
| DOR | 2.0 / 0.333 | 6.0 |

**Checks:** TPR + FNR = 1 ✓; TNR + FPR = 1 ✓; PPV + FDR = 1 ✓; NPV + FOR = 1 ✓. So only a few of these are independent — you can always derive the "missing" one from its complement.

**Same table, two vocabularies.** Information retrieval says *precision, recall*; medicine and statistics say *PPV, sensitivity, specificity*; ML mixes both. The summary table ties all names together ([[02_Precision_and_Recall_Document_Retrieval_Venn_Diagram]]).

---

## 2) Simple English Explanation

Once you have the four counts (TP, FP, FN, TN), you can make **many** different scores. This slide is a giant cheat-sheet of them. There is a simple way to think about it:

**Look down each column (the real truth):**
- **Recall / sensitivity (TPR):** of the really-positive ones, how many did we find?
- **Miss rate (FNR):** of the really-positive ones, how many did we miss? (= 1 − recall)
- **Specificity (TNR):** of the really-negative ones, how many did we correctly clear?
- **Fall-out (FPR):** of the really-negative ones, how many did we wrongly flag? (= 1 − specificity)

**Look along each row (what the model said):**
- **Precision (PPV):** when it says "positive," how often is it right?
- **False discovery rate:** when it says "positive," how often is it wrong?
- **NPV:** when it says "negative," how often is it right?
- **False omission rate:** when it says "negative," how often is it wrong?

**Overall:** *prevalence* (how common the positives are), *accuracy* (overall correctness), *F1* (balance of precision and recall), and three "ratio" scores (LR+, LR−, DOR) that boil the quality down to one number each.

Using our 10-photo example: recall 0.8, specificity 0.6, precision 0.67, NPV 0.75, accuracy 0.7. Notice the pairs add to 1 (recall + miss rate = 1, and so on).

The slide's main hint: **choose the score that matches the question you care about** — which depends on which class matters.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Jab tumhare paas 4 counts (TP, FP, FN, TN) aa jaate hain, to unse **bahut saare scores** ban sakte hain. Ye slide unka ek bada cheat-sheet hai. Isse samajhne ka aasaan tareeka:

**Column ke neeche dekho (asli sach ke hisaab se):**
- **Recall / sensitivity (TPR):** jo sach mein positive hain, unme se kitne pakde?
- **Miss rate (FNR):** jo sach mein positive hain, unme se kitne chhoot gaye? (= 1 − recall)
- **Specificity (TNR):** jo sach mein negative hain, unme se kitno ko sahi clear kiya?
- **Fall-out (FPR):** jo sach mein negative hain, unme se kitno ko galti se positive bol diya? (= 1 − specificity)

**Row ke saath dekho (model ne kya bola uske hisaab se):**
- **Precision (PPV):** jab model "positive" bole, to kitni baar sahi?
- **False discovery rate:** jab "positive" bole, kitni baar galat?
- **NPV:** jab "negative" bole, kitni baar sahi?
- **False omission rate:** jab "negative" bole, kitni baar galat?

**Overall:** *prevalence* (positives kitne common hain), *accuracy* (kul sahi), *F1* (precision-recall ka balance), aur teen ratio scores (LR+, LR−, DOR).

Humare 10-photo example mein: recall 0.8, specificity 0.6, precision 0.67, NPV 0.75, accuracy 0.7, FPR 0.4, FNR 0.2. Dhyaan do — jodi wale numbers 1 banate hain (recall + miss rate = 1, specificity + fall-out = 1, precision + FDR = 1).

Slide ka main message: **wahi score chuno jo tumhare sawaal se match kare** — aur wo is par depend karta hai ki **class of interest** kaun si hai. (Isi table ke naam alag-alag fields mein alag use hote hain: retrieval mein precision/recall, medicine mein sensitivity/specificity/PPV.)
