# Topic 8: The Confusion Matrix — TP, TN, FP, FN

Source: Lecture 17, slide 21 ("Confusion Matrix", with the instructor's red annotations: TP/TN/FP/FN, "True labels", "predicted", D = disease, ND = no disease). Enriched with a worked example and web-researched context (Type I / Type II errors, accuracy pitfall on imbalanced data).

---

## 1) Technical Explanation

**Definition (slide 21).** *A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data* ([[03_Train_Test_Split_Large_Data_and_Validation_Set]]).

**The four outcomes (the slide uses a disease-test story).**

| Term | Meaning (slide) |
|---|---|
| **True Positive (TP)** | We predicted **positive** (they have the disease), and they **do** have the disease. |
| **True Negative (TN)** | We predicted **negative**, and they **don't** have the disease. |
| **False Positive (FP)** | We predicted **positive**, but they **don't** actually have the disease. Also known as a **"Type I error."** |
| **False Negative (FN)** | We predicted **negative**, but they **actually do** have the disease. Also known as a **"Type II error."** |

**The table layout (slide).** Columns = **Actual** (the instructor writes "True labels": **D** = disease/positive, **ND** = no disease/negative). Rows = **Predicted** (**D** / **ND**):

|  | **Actual: Positive (D)** | **Actual: Negative (ND)** |
|---|---|---|
| **Predicted: Positive (D)** | **TP** | **FP** |
| **Predicted: Negative (ND)** | **FN** | **TN** |

The correct decisions (TP and TN) lie on the **main diagonal** (circled on the slide); errors (FP, FN) are off-diagonal. ⚠️ Layout conventions differ between books and libraries — some put *Actual* on the rows. Always read the labels, not the position.

**Memory trick (research).** Read each name as *(was the prediction right?) + (what did we predict?)*: "True Positive" = right, predicted positive; "False Negative" = wrong, predicted negative.

**Which error is worse depends on the task.** In disease screening a **FN** (missing a sick patient) is usually more dangerous than a **FP** (an extra test); for a spam filter a **FP** (real mail marked spam) is often worse than a FN.

**Worked example (illustrative, verified).** A screening test on 100 patients gives TP = 40, FP = 10, FN = 5, TN = 45 (so 45 actually sick = 40 + 5; 55 healthy = 10 + 45).

|  | Actual D | Actual ND |
|---|---|---|
| Predicted D | 40 | 10 |
| Predicted ND | 5 | 45 |

- Correct = TP + TN = 85 → **accuracy** = (TP + TN)/(TP + TN + FP + FN) = 85/100 = **0.85**.
- Errors: 10 false alarms (Type I) and 5 misses (Type II).

**Why "accuracy, with caution" (slide 4).** Accuracy alone can mislead when classes are imbalanced: if only 10 of 1,000 patients are sick, a useless model that says "healthy" for everyone has TP = 0, FP = 0, FN = 10, TN = 990 → accuracy = 990/1000 = **99 %**, yet it finds **none** of the sick patients. The confusion matrix reveals this; this is why further metrics — **precision, recall, F1-score and ROC curves**, announced in the outline ([[07_Performance_Metrics_Overview_and_Regression_Metrics]]) but not covered in this PDF — are all built from TP, FP, FN, TN.

**Connection.** Every classifier from earlier lectures — [[05_Worked_Example_Logistic_Regression_Exam_Pass_Probability]] from Lecture 15 (after the 0.5 threshold) and k-NN from Lecture 16 — can be evaluated with a confusion matrix on its test set; with cross-validation ([[05_k_Fold_Cross_Validation]]) you can sum or average the matrices across folds.

---

## 2) Simple English Explanation

A **confusion matrix** is a small 2×2 scoreboard showing **how a yes/no predictor got things right and wrong.** Think of a medical test for a disease.

- **True Positive (TP):** test says "sick" and the person **is** sick. ✅
- **True Negative (TN):** test says "healthy" and the person **is** healthy. ✅
- **False Positive (FP):** test says "sick" but the person is **healthy** — a *false alarm* (also called Type I error). ❌
- **False Negative (FN):** test says "healthy" but the person is **sick** — a *miss* (Type II error). ❌

Draw it as a table: columns = the **truth**, rows = the **prediction**. Good answers sit on the diagonal (TP and TN); mistakes are in the other two boxes.

Example with 100 people: 40 correctly flagged sick, 45 correctly cleared, 10 false alarms, 5 missed. Correct = 40 + 45 = 85 → **accuracy 85 %.**

**Warning:** accuracy can hide problems. If 99 % of people are healthy, a lazy test that says "healthy" to everyone is 99 % accurate — but misses **every** sick person. The scoreboard shows this at once (0 TP). That is why people also use precision, recall and other scores built from these four numbers.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Confusion matrix** ek chhota 2×2 scoreboard hai jo dikhata hai ki ek yes/no predictor ne **kahan sahi aur kahan galat** kiya. Ek bimaari ke medical test ka example lo (slide mein bhi yahi hai).

- **True Positive (TP):** test ne bola "bimaar hai" aur banda **sach mein bimaar** hai. ✅
- **True Negative (TN):** test ne bola "theek hai" aur banda **sach mein theek** hai. ✅
- **False Positive (FP):** test ne bola "bimaar hai" par banda **theek** hai — **false alarm** (ise **Type I error** kehte hain). ❌
- **False Negative (FN):** test ne bola "theek hai" par banda **bimaar** hai — **chhoot gaya / miss** (**Type II error**). ❌

Table aise banta hai: **columns = asli sach (True labels: D = disease, ND = no disease)** aur **rows = prediction**. Sahi jawab diagonal par (TP aur TN) aate hain, galtiyan baaki do boxes mein.

Example (100 log): 40 bimaar sahi pakde (TP), 45 theek logon ko sahi clear kiya (TN), 10 false alarm (FP), 5 bimaar chhoot gaye (FN). Sahi = 40 + 45 = 85 → **accuracy = 85%**.

⚠️ **Dhyaan:** accuracy kabhi-kabhi dhokha deti hai. Agar 99% log theek hain aur ek aalsi test sabko "theek" bol deta hai, to wo 99% accurate hai — par **ek bhi bimaar nahi pakadta** (TP = 0). Confusion matrix ye turant dikha deta hai. Isiliye slide 4 mein likha tha ki accuracy "with caution" use karo, aur isiliye precision, recall, F1 aur ROC jaise scores bhi hote hain (jo in chaaron numbers se hi bante hain).

Yaad rakhne ka trick: pehla shabd (True/False) batata hai ki prediction **sahi thi ya galat**, doosra shabd (Positive/Negative) batata hai ki model ne **kya predict kiya**.
