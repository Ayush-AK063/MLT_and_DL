# Topic 3: Worked Exercise — Predicting Man vs. Woman from a Photograph

Source: Lecture 18, slides 5–9 (the exercise statement, "Woman as Positive class (P), Man as Negative class (N)", the 10-row Expected/Predicted table, Step 1 count of TP/TN/FP/FN, the confusion matrix, and the instructor's A, P, R, S / F1 notes). Independently re-verified; the slide leaves parts (b) as formulas only, so full answers are worked out here.

---

## 1) Technical Explanation

**Exercise (slide 5).** *Consider a two-class classification problem of predicting whether a photograph contains a man or a woman. Suppose we have a test dataset of 10 records with expected outcomes and a set of predictions from our classification algorithm.* (a) Compute the **confusion matrix**. (b) Compute the **accuracy, precision, recall, sensitivity and specificity**.

**Class convention (slide 6).** **Woman = Positive class (P); Man = Negative class (N).** (The choice is arbitrary but must be fixed first — see the swap check below.)

**Data and Step 1 (slides 5, 8).** Each row is labelled by comparing *Expected* with *Predicted*:

| Row | Expected | Predicted | Type |
|---|---|---|---|
| 1 | man (N) | woman (P) | **FP** |
| 2 | man (N) | man (N) | **TN** |
| 3 | woman (P) | woman (P) | **TP** |
| 4 | man (N) | man (N) | **TN** |
| 5 | woman (P) | man (N) | **FN** |
| 6 | woman (P) | woman (P) | **TP** |
| 7 | woman (P) | woman (P) | **TP** |
| 8 | man (N) | man (N) | **TN** |
| 9 | man (N) | woman (P) | **FP** |
| 10 | woman (P) | woman (P) | **TP** |

**Counts (slide 9, re-verified):** **TP = 4** (rows 3, 6, 7, 10), **TN = 3** (rows 2, 4, 8), **FP = 2** (rows 1, 9), **FN = 1** (row 5). Total 10 ✓. Actual women = 5 (TP + FN), actual men = 5 (TN + FP).

**(a) Confusion matrix** (the instructor's handwritten 4 / 2 / 1 / 3 grid, rows = predicted, columns = actual):

|  | Actual: woman (P) | Actual: man (N) |
|---|---|---|
| **Predicted: woman (P)** | TP = **4** | FP = **2** |
| **Predicted: man (N)** | FN = **1** | TN = **3** |

**(b) Metrics** (formulas from [[01_Classification_Metrics_Accuracy_Precision_Recall_F1]]; the instructor's margin notes: "Accuracy, Precision, Recall, F1" and, on slide 5, "Specificity = TN/(TN + FP)" and "Sensitivity = TP/(TP + FN) — true positive rate", "True negative rate"):

| Metric | Formula | Calculation | Result |
|---|---|---|---|
| **Accuracy** | (TP + TN)/(TP + FP + TN + FN) | (4 + 3)/10 | **0.70** (70 %) |
| **Precision** | TP/(TP + FP) | 4/(4 + 2) | **0.667** |
| **Recall** | TP/(TP + FN) | 4/(4 + 1) | **0.80** |
| **Sensitivity** (TPR) | TP/(TP + FN) | 4/5 | **0.80** — *identical to recall* |
| **Specificity** (TNR) | TN/(TN + FP) | 3/(3 + 2) | **0.60** |
| **F1-score** | 2PR/(P + R) | 2(0.667)(0.8)/(1.467) | **0.727** (= 2·4/(8 + 2 + 1) = 8/11 ✓) |

**Observations.**
- Sensitivity and recall are **the same quantity** under two names (medicine vs. information retrieval). The exercise asks for both only to make this point.
- The model is better at finding women (recall 0.80) than at correctly rejecting men (specificity 0.60): of 5 men it falsely called 2 "woman".
- Accuracy 0.70 alone hides this asymmetry — and the other 4 numbers differ a lot.

**Swap check — the class of interest matters.** If instead *man* is the positive class, TP/TN and FP/FN swap roles: TP = 3, TN = 4, FP = 1, FN = 2 → accuracy 0.70 (unchanged), precision = 3/4 = **0.75**, recall = 3/5 = **0.60**, specificity = 4/5 = **0.80**, F1 = 6/9 = **0.667**. Accuracy is symmetric, but precision, recall, specificity and F1 are **not** — always state which class is "positive" ([[04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates]]: "depending on the class of interest").

**Other quantities for this exercise (from the summary table, verified).** FPR = 2/5 = 0.40, FNR = 1/5 = 0.20, NPV = 3/4 = 0.75, FDR = 2/6 = 0.333, balanced accuracy = (0.8 + 0.6)/2 = 0.70.

---

## 2) Simple English Explanation

**The task:** a program looks at 10 photos and says "woman" or "man." We know the real answers. We call "woman" the **positive** class and "man" the **negative** class.

**Step 1 – mark every photo:**
- Said woman and it **was** a woman → **TP** (photos 3, 6, 7, 10) = **4**
- Said man and it **was** a man → **TN** (photos 2, 4, 8) = **3**
- Said woman but it was a **man** → **FP** (photos 1, 9) = **2**
- Said man but it was a **woman** → **FN** (photo 5) = **1**

**Confusion matrix:** top row (said woman): 4 correct, 2 wrong; bottom row (said man): 1 wrong, 3 correct.

**Scores:**
- **Accuracy** = 7 correct out of 10 = **0.70**
- **Precision** = of the 6 times it said "woman," 4 were right = 4 ÷ 6 = **0.67**
- **Recall / Sensitivity** = of the 5 real women, it found 4 = 4 ÷ 5 = **0.80** (these two names mean the same thing)
- **Specificity** = of the 5 real men, it correctly called 3 "man" = 3 ÷ 5 = **0.60**
- **F1** = mix of precision and recall = **0.73**

**Notice:** if we had picked "man" as the positive class, the scores change (precision 0.75, recall 0.60, …) though accuracy stays 0.70. So always say which class is "positive."

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Task:** ek program 10 photos dekhta hai aur bolta hai "woman" ya "man". Asli answers humein pata hain. "Woman" ko **positive** class aur "man" ko **negative** class maanenge.

**Step 1 – har photo ko mark karo:**
- Bola woman aur **thi woman** → **TP** (photo 3, 6, 7, 10) = **4**
- Bola man aur **tha man** → **TN** (photo 2, 4, 8) = **3**
- Bola woman par **tha man** → **FP** (photo 1, 9) = **2**
- Bola man par **thi woman** → **FN** (photo 5) = **1**

**Confusion matrix** (sir ne 4, 2, 1, 3 likha hai): upar wali row (bola woman): 4 sahi, 2 galat; neeche wali row (bola man): 1 galat, 3 sahi.

**Scores:**
- **Accuracy** = 10 mein se 7 sahi = **0.70**
- **Precision** = jab 6 baar "woman" bola, unme se 4 sahi = 4 ÷ 6 = **0.67**
- **Recall / Sensitivity** = 5 asli women mein se 4 pakdi = 4 ÷ 5 = **0.80** (ye dono naam ek hi cheez ke hain; sir ne slide par "true positive rate" likha hai)
- **Specificity** = 5 asli men mein se 3 ko sahi "man" bola = 3 ÷ 5 = **0.60** (ise "true negative rate" bhi kehte hain)
- **F1** = precision aur recall ka harmonic mean = **0.73**

**Dhyaan do:** model women ko pakadne mein (0.80) men ko reject karne (0.60) se behtar hai — sirf accuracy 0.70 ye farak chhupa deti hai.

**Swap check:** agar "man" ko positive class bana dete, to TP = 3, TN = 4, FP = 1, FN = 2 hota. Accuracy wahi 0.70 rehti, par precision 0.75, recall 0.60, specificity 0.80, F1 0.67 ho jaate. Isliye hamesha bolo ki **positive class kaun si hai.**
