# Topic 0: Recap — TPR, FPR, and the Blood-Test Threshold Idea

Source: Lecture 19, slides 1–3 (the repeated "Outline", the blood-value dataset with "Choose a classification threshold", and "Recap: Confusion matrix" with the instructor's TPR/FPR notes). Recap note — the confusion matrix itself is already covered in Lecture 17 and 18. The blood-test numbers are re-verified here.

---

## 1) Technical Explanation

**Slide 1 — outline.** The same three-part outline as Lecture 17: *1. Metrics, 2. Precision and recall, 3. Receiver Operating Characteristic (ROC) curves.* Lectures 17 and 18 delivered parts 1 and 2; **this lecture finally delivers part 3, ROC curves** (the stray "68 /14" is a leftover page label). Earlier material: [[08_Confusion_Matrix_TP_TN_FP_FN]] from Lecture 17 and [[01_Classification_Metrics_Accuracy_Precision_Recall_F1]] from Lecture 18.

**Slide 2 — a motivating example (blood test for cancer).** Data from 10 people, one blood value each, with the true status:

| Person | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Blood value | 70 | 62 | 58 | 52 | 48 | 40 | 35 | 30 | 25 | 20 |
| Actual status | Cancer | Cancer | Cancer | Cancer | Cancer | Healthy | Healthy | Healthy | Healthy | Healthy |

**Step 2 — choose a classification threshold:** *if blood value ≥ 45 → predict Cancer; if blood value < 45 → predict Healthy.* A dashed red line at **Threshold = 45** separates the two groups in the scatter plot. (The slide's arrow suggests further steps, but only these two are shown in this PDF.)

With threshold 45 **every prediction is right:** all five cancer values (70, 62, 58, 52, 48) are ≥ 45 → TP = 5; all five healthy values (40, 35, 30, 25, 20) are < 45 → TN = 5; FP = FN = 0 → TPR = 5/5 = **1**, FPR = 0/5 = **0**.

*Why it matters:* this model's score (the blood value) can be cut at **any** threshold, and each threshold gives a different confusion matrix and different TPR/FPR. Moving the threshold — the idea the whole lecture is built on ([[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]]). Our check: here the two groups don't overlap at all (lowest cancer 48 > highest healthy 40), so *any* threshold between 40 and 48 gives the perfect (FPR = 0, TPR = 1) point, and the ROC curve would be the ideal one with **AUC = 1** ([[02_ROC_Shapes_AUC_and_Comparing_Models]]).

**Slide 3 — recap of the confusion matrix with two new rates.**
- The confusion matrix (*easily generalizes to multi-class*).
- *Machine-learning methods usually minimize FP + FN* (the total number of errors).
- **TPR (True Positive Rate) = TP / (TP + FN) = Recall** (instructor writes this on the slide as "True Positive Rate (Recall) = TP/(TP+FN)").
- **FPR (False Positive Rate) = FP / (TN + FP)** — the instructor writes it out as FP over (TN + FP), i.e. **FPR = FP/(TN + FP) = 1 − Specificity** ([[04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates]] from Lecture 18).

**Instructor's reading trick (red notes on slide 3):** *"True positive: P ← P"* and *"False positive: N ← P"*, with arrows labelling **Actual class** (left letter) and **Predicted class** (right letter). So in "True positive" the actual class is P and the predicted class is P; in "False positive" the actual class is **N** but the model predicted **P**.

**Worked check (Lecture 18's man/woman exercise: TP 4, FP 2, FN 1, TN 3).** TPR = 4/5 = 0.80; FPR = 2/(3 + 2) = 0.40 — one point **(FPR, TPR) = (0.40, 0.80)** that ROC analysis will treat as one dot on a curve.

---

## 2) Simple English Explanation

**The blood-test story.** Ten people give a blood sample. A higher blood value tends to mean cancer. The doctor picks a **cut-off (threshold)** of 45: *at or above 45 → "cancer", below 45 → "healthy"*. In this tiny example the cancer patients all have 48–70 and the healthy people all have 20–40, so the cut-off at 45 gets **everyone right**: 5 cancer patients correctly flagged, 5 healthy people correctly cleared. Good — but the doctor could have used 30, or 60 as the cut-off instead, and results would change. This lecture is about studying **all possible cut-offs at once**.

**Two rates to remember:**
- **TPR (True Positive Rate)** = of the really-sick people, what fraction did we catch? (= recall.)
- **FPR (False Positive Rate)** = of the really-healthy people, what fraction did we wrongly call sick? (= false-alarm rate.)

**Teacher's trick for the names:** the *first* word (True/False) says whether we were right, the *second* word (Positive) says what we predicted. "False positive" = the person is actually **N**egative but we said **P**ositive.

Remember: the lecture's outline promised ROC curves in Lecture 17; here they finally arrive.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Blood-test ki kahani.** 10 logon ka blood test hua. Blood value jitni zyada, cancer ke chance utne zyada. Doctor ne **cut-off (threshold) 45** rakha: *45 ya usse zyada → "cancer", 45 se kam → "healthy"*. Is chhote example mein cancer wale sabki value 48–70 hai aur healthy logon ki 20–40, isliye 45 ka cut-off **sabko sahi** pakadta hai: 5 cancer patients sahi flag hue (TP = 5) aur 5 healthy sahi clear hue (TN = 5). Par doctor 30 ya 60 ka cut-off bhi rakh sakta tha aur results badal jaate. Is lecture ka maqsad **saare possible cut-offs ko ek saath** dekhna hai.

**Do rates yaad rakho:**
- **TPR (True Positive Rate)** = jo sach mein bimaar hain, unme se kitno ko pakda? (= **recall**) = TP / (TP + FN)
- **FPR (False Positive Rate)** = jo sach mein theek hain, unme se kitno ko galti se bimaar bola? (false-alarm rate) = FP / (TN + FP) = 1 − specificity

**Sir ka trick (slide 3 ke lal notes):** "True positive: P ← P" yaani actual class P aur predicted class bhi P. "False positive: N ← P" yaani **actual N** hai par model ne **P** bol diya. Left letter = Actual class, right letter = Predicted class.

Example: Lecture 18 ke man/woman exercise mein TPR = 4/5 = 0.80 aur FPR = 2/5 = 0.40, yaani graph par ek point (0.40, 0.80). Ek point ek threshold ka hota hai — saare thresholds ke points jodne par **ROC curve** banta hai.

Lecture 17 ke outline mein ROC curves ka promise tha — wo ab is lecture mein aa gaya.
