# Topic 1: Classification Metrics — Accuracy, Precision, Recall (Sensitivity), F1-Score

Source: Lecture 18, slide 3 (the instructor's handwritten page: left half "Classification Metrics" ①–④, right half "Regression Metrics"). Enriched with web research (harmonic mean, F-beta, precision–recall trade-off).

---

## 1) Technical Explanation

Slide 3 is a two-column page. The **right column** ("Regression Metrics": MAE, MSE, RMSE, R²) is a verbatim repeat of Lecture 17, slide 20 — see [[07_Performance_Metrics_Overview_and_Regression_Metrics]] from Lecture 17 (including the note that the handwritten RMSE is missing its 1/N). The **left column** is new: four classification metrics, all computed from the confusion matrix ([[00_Recap_Confusion_Matrix_and_the_Sick_People_Intuition]]).

| # | Metric | Formula (slide) | In words |
|---|---|---|---|
| ① | **Accuracy** | (No. of correct predictions) / (Total no. of predictions) = **(TP + TN) / (TP + FP + TN + FN)** (the longer form appears on slide 6) | Fraction of all predictions that were right |
| ② | **Precision (P)** | **TP / (TP + FP)** | Of everything the model *called positive*, how much really was positive? |
| ③ | **Recall (R)** — "Sensitivity measure" | **TP / (TP + FN)**; the instructor marks its range **(0, 1)** | Of everything that *really is positive*, how much did the model find? |
| ④ | **F1-score** | **Harmonic mean of Precision & Recall = 2 × (P × R)/(P + R)** | A single number that is high only when *both* P and R are high |

**What each denominator is.**
- Precision's denominator **TP + FP = all predicted positive** (the first *row* of the matrix).
- Recall's denominator **TP + FN = all actually positive** (the first *column*).
- Accuracy's denominator = everything.

**Why the harmonic mean (research).** The F1-score uses the **harmonic**, not arithmetic, mean because the harmonic mean is dragged toward the *smaller* of the two numbers. Example: P = 1.0 and R = 0.1 → arithmetic mean = 0.55 (sounds okay), harmonic mean = 2 × 0.1 / 1.1 = **0.182** (honestly reflects a model that misses 90 % of positives). A model with P = 1, R = 0 gets F1 = 0, not 0.5. An equivalent form (verified): **F1 = 2TP / (2TP + FP + FN)**.

**Precision vs. recall — they pull against each other (research).** Most classifiers output a score and apply a threshold ([[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15, the 0.5 cut-off). *Lowering* the threshold flags more cases → recall rises, precision usually falls (more false alarms). *Raising* it does the reverse. F1 summarizes the balance; the **F-beta** family (F₂ weights recall more, F₀.₅ weights precision more) tilts it when one error type is costlier — see [[05_Choosing_the_Right_Metric_Imbalance_Trade_offs_and_Extensions]].

**Worked check (using Lecture 17's 100-patient example, TP = 40, FP = 10, FN = 5, TN = 45).**
- Accuracy = 85/100 = 0.85
- Precision = 40/50 = **0.80**
- Recall = 40/45 = **0.889**
- F1 = 2(0.80)(0.889)/(0.80 + 0.889) = **0.842** (= 2·40/(80 + 10 + 5) = 80/95 ✓)

**The accuracy trap revisited.** In the "say everyone is healthy" example (TP = 0, FP = 0, FN = 10, TN = 990) accuracy is 99 % but recall = 0/10 = **0** and F1 = 0 — which is exactly what these new metrics are for.

---

## 2) Simple English Explanation

After the 2×2 scoreboard, here are four scores built from it. Think of a doctor's test for a disease.

1. **Accuracy** — "Out of everyone tested, how many did the test get right?" (correct ÷ total).
2. **Precision** — "When the test **says 'sick'**, how often is it right?" = TP ÷ (TP + FP). High precision means few false alarms.
3. **Recall** (also called **sensitivity**) — "Out of everyone who **really is sick**, how many did the test catch?" = TP ÷ (TP + FN). High recall means few misses. It's always between 0 and 1.
4. **F1-score** — one number mixing precision and recall: 2 × (P × R) ÷ (P + R). It uses a special "harmonic" average which punishes you if **either** score is poor. (Precision 1.0 but recall 0.1 gives only 0.18, not 0.55.)

Example (100 patients: TP 40, FP 10, FN 5, TN 45): accuracy 0.85, precision 40 ÷ 50 = 0.80, recall 40 ÷ 45 = 0.89, F1 = 0.84.

There's a tug-of-war: if you make the test "more eager" to say sick, you catch more sick people (recall ↑) but raise more false alarms (precision ↓).

(The right side of the slide, regression scores, was already covered last lecture.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

2×2 scoreboard ke baad ab chaar scores aate hain (doctor ke disease-test ka example socho):

1. **Accuracy** — "Jitne logon ko test kiya, unme se kitno ka test ne sahi answer diya?" = sahi ÷ total.
2. **Precision** — "Jab test **'bimaar' bolta hai**, to kitni baar sahi hota hai?" = TP ÷ (TP + FP). Precision zyada = false alarm kam.
3. **Recall** (isse **sensitivity** bhi kehte hain) — "Jo log **sach mein bimaar** hain, unme se test ne kitno ko pakda?" = TP ÷ (TP + FN). Recall zyada = miss kam. Iski value hamesha 0 se 1 ke beech hoti hai (sir ne (0,1) likha hai).
4. **F1-score** — precision aur recall ko mila kar ek number: 2 × (P × R) ÷ (P + R). Ye **harmonic mean** hai, jo tab hi bada hota hai jab **dono** achhe hon. (Precision 1.0 par recall 0.1 ho to F1 sirf 0.18 aata hai, 0.55 nahi.)

Example (100 patients: TP 40, FP 10, FN 5, TN 45): accuracy 0.85, precision 40 ÷ 50 = **0.80**, recall 40 ÷ 45 = **0.89**, F1 = **0.84**.

Ek tug-of-war hota hai: agar test ko zyada "jaldi bimaar bolne wala" bana do, to zyada bimaar pakde jaate hain (recall ↑) par false alarm bhi badhte hain (precision ↓).

Slide ke daayein taraf ke regression metrics (MAE, MSE, RMSE, R²) pichli lecture (17) mein ho chuke hain.
