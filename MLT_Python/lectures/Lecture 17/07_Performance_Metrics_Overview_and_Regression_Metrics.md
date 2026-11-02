# Topic 7: Performance Metrics Overview and Regression Metrics (MAE, MSE, RMSE, R²)

Source: Lecture 17, slides 17–20 (the three-part "Outline" shown twice, "Metrics", and the instructor's handwritten "Regression Metrics" page: MAE, MSE, RMSE, R²). Independently re-verified with a worked example; enriched with web research (MAE vs. RMSE, negative R², normalized errors).

---

## 1) Technical Explanation

**Outline (slides 17–18).** The lecture's second half announces three parts: **1. Metrics, 2. Precision and recall, 3. Receiver Operating Characteristic (ROC) curves.** (Slide 18 is a repeat of the same outline.) *In this PDF only part 1 is actually delivered* — precision/recall and ROC curves do not appear (the deck ends at the confusion matrix) and are presumably in the next lecture. The stray "17 /14" / "18 /14" / "19 /14" page marks on these slides are leftovers from the original deck and mean nothing.

**Why metrics (slide 19).** *It is extremely important to use quantitative metrics for evaluating a machine learning model.* Until now we relied on the **cost-function value** for regression and classification (see the least-squares cost in [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]] from Lecture 13). Other metrics help to better evaluate and understand the model:
- **Classification:** Accuracy / Precision / Recall / F1-score, ROC curves, … ([[08_Confusion_Matrix_TP_TN_FP_FN]] is the foundation).
- **Regression:** **Normalized RMSE, Normalized Mean Absolute Error (NMAE), …**

**Regression metrics (slide 20, handwritten).** Let there be N test examples, **yⱼ = actual value** and **ŷⱼ = predicted value**, ȳ = **mean of the actual values**.

| # | Metric | Formula | Notes |
|---|---|---|---|
| ① | **MAE** — Mean Absolute Error | (1/N) Σⱼ \|yⱼ − ŷⱼ\| | Average size of the error, in the **same units** as y; every error counts linearly |
| ② | **MSE** — Mean Squared Error | (1/N) Σⱼ (yⱼ − ŷⱼ)² | Squares errors, so big mistakes are penalized heavily; units are y² |
| ③ | **RMSE** — Root Mean Squared Error | √[ (1/N) Σⱼ (yⱼ − ŷⱼ)² ] = √MSE | Back in the units of y |
| ④ | **R²** (coefficient of determination) | 1 − Σⱼ (yⱼ − ŷⱼ)² / Σⱼ (yⱼ − ȳ)² | "Close to 1" is good (instructor's note) |

**⚠️ Slide-correction (flagged).** The handwritten RMSE line shows **√(Σ (yⱼ − ŷⱼ)²)** with **no 1/N**. RMSE is by definition the square root of the *mean* squared error, i.e. **with** 1/N (as in ② MSE ③ = √MSE). Without 1/N the value would be inflated by √N — see the check below. Treat the 1/N as omitted by hand.

**Worked example (our own, verified).** Actual y = [3, 5, 2, 7]; predicted ŷ = [2.5, 5, 4, 8].
- Errors (y − ŷ) = [0.5, 0, −2, −1]; absolute = [0.5, 0, 2, 1]; squared = [0.25, 0, 4, 1].
- **MAE** = (0.5 + 0 + 2 + 1)/4 = 3.5/4 = **0.875**
- **MSE** = (0.25 + 0 + 4 + 1)/4 = 5.25/4 = **1.3125**
- **RMSE** = √1.3125 ≈ **1.1456** (without the 1/N the formula would wrongly give √5.25 ≈ 2.2913 = 1.1456 × √4)
- ȳ = (3+5+2+7)/4 = 4.25; **SS_tot** = Σ(y − ȳ)² = 1.5625 + 0.5625 + 5.0625 + 7.5625 = 14.75; **SS_res** = 5.25
- **R²** = 1 − 5.25/14.75 = **0.644** (≈ 64 % of the variance explained)

**Reading the metrics (research).**
- **MAE vs. RMSE:** RMSE ≥ MAE always; the more RMSE exceeds MAE, the more the errors are dominated by a few large mistakes (RMSE is more sensitive to outliers; MAE is more robust). Here 1.1456 vs 0.875 is mostly due to the single −2 error.
- **R² = 1** → perfect; **R² = 0** → no better than always predicting the mean ȳ; **R² < 0** is possible on test data → *worse than predicting the mean*. (E.g. predicting 10 for every example above gives R² ≈ −8.97.) "Close to 1" is therefore good, but only on **test** data ([[01_Why_System_Evaluation_and_Predictive_Modeling]]).
- **Normalized versions (slide 19: NRMSE, NMAE):** divide RMSE or MAE by a reference scale — the **range** (max − min) of y, the **mean** of y, or the **standard deviation** of y — to get a unit-free number comparable across datasets. For the example above, range = 7 − 2 = 5, so NRMSE(range) = 1.1456/5 ≈ **0.229** and NMAE(range) = 0.875/5 = **0.175**. (The slide names but does not define them; the choice of normalizer must be stated.)

---

## 2) Simple English Explanation

Last time we said "how good is the model?" — now we need **numbers** for that. For **predicting numbers** (regression) there are four classic scores. Let "actual" be the true value and "predicted" be the model's guess.

1. **MAE (Mean Absolute Error):** for each example, find how far off the guess was (ignore the + or − sign) and **average** those gaps. "On average I'm off by 0.875."
2. **MSE (Mean Squared Error):** square each gap first, then average. Big mistakes become **huge** after squaring, so MSE punishes them.
3. **RMSE:** take the **square root of MSE** to get back to the original units. (The slide forgot to divide by N in this line; it should be square-root of the *average*.)
4. **R²:** compares your model with a lazy model that always guesses the **average**. R² near **1** = great; **0** = no better than the lazy average guess; **negative** = even worse than the lazy guess.

Example: actual [3, 5, 2, 7], guesses [2.5, 5, 4, 8] → gaps 0.5, 0, 2, 1.
- MAE = 3.5 ÷ 4 = **0.875**
- MSE = (0.25 + 0 + 4 + 1) ÷ 4 = **1.3125**
- RMSE = √1.3125 ≈ **1.146**
- R² = 1 − 5.25 ÷ 14.75 ≈ **0.64**

**Normalized** versions divide by a "typical size" of the data (like its range) so you can compare across problems with different units.

The lecture also promises two more topics (**precision/recall** and **ROC curves**), but they are not in this PDF.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Pehle humne kaha "model kitna accha hai?" — ab iske liye **numbers** chahiye. **Number predict karne wale (regression)** models ke liye 4 classic scores hain. "Actual" = asli value, "Predicted" = model ka guess.

1. **MAE (Mean Absolute Error):** har example mein guess kitna door tha (+/− sign ignore karke) nikalo aur sabka **average** lo. "Mera guess average mein 0.875 se galat hai."
2. **MSE (Mean Squared Error):** pehle har gap ka square karo, phir average. Bade errors square hone par **bahut bade** ho jaate hain, isliye MSE unhe zyada sazaa deta hai.
3. **RMSE:** MSE ka **square root**, taaki wapas original unit mein aa jaye. (⚠️ Sir ke handwritten formula mein 1/N likhna reh gaya hai; sahi formula √(average of squared errors) hai.)
4. **R²:** tumhare model ko ek aalsi model se compare karta hai jo hamesha **average** hi bolta hai. R² **1 ke paas** = bahut accha; **0** = aalsi average se behtar nahi; **negative** = aalsi guess se bhi bura.

Example: actual [3, 5, 2, 7], guesses [2.5, 5, 4, 8] → gaps 0.5, 0, 2, 1.
- MAE = 3.5 ÷ 4 = **0.875**
- MSE = (0.25 + 0 + 4 + 1) ÷ 4 = **1.3125**
- RMSE = √1.3125 ≈ **1.146** (agar 1/N bhool jao to galat 2.29 aata hai!)
- R² = 1 − 5.25 ÷ 14.75 ≈ **0.64**

**Normalized** versions (NRMSE, NMAE) mein error ko data ke "typical size" (jaise range = max − min) se divide karte hain taaki alag units wale problems compare ho sakein. Is example mein range = 5, to NRMSE ≈ 0.229.

Slide 17–18 ke outline mein **precision/recall** aur **ROC curve** ka bhi zikr hai, par wo is PDF mein nahi hain (shayad agli lecture mein).
