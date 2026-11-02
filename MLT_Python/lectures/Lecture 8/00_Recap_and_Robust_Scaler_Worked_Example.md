# Topic 0: Recap & the Interquartile/Robust Scaler (Worked Example)

Source: Lecture 8, slides 1–4 (RECAP, Interquartile/Robust normalization ×3).

---

## 1) Technical Explanation

**Recap (slide 1)**: Lecture 7's content is summarized — Data Integration (schema integration/feature matching, data value conflicts, redundant features/correlation analysis) and Data Transformation's four major techniques (Normalization/Scaling, Aggregation, Generalization, Feature construction).

**The 7th scaling method — completing Lecture 7's list**: Lecture 7 named "InterQuartile Scaler / Robust Scaler" as a seventh normalization method but didn't work through it. This lecture completes it.

**Formula**: `X' = (X − Q2) / (Q3 − Q1)`

Where `Q2` is the **median** (second quartile), and `Q1`/`Q3` are the first and third quartiles — the same **IQR (Interquartile Range = Q3 − Q1)** concept from the Boxplot/Outlier Analysis topic in Lecture 6.

**Why this method exists — the stated rationale**: *"The mean, maximum and minimum values of the columns... All these values are sensitive to outliers. If there are too many outliers in the data, they will influence the mean and the max value or the min value. Thus, even if we scale this data using the above methods [Min-Max, Mean Normalization, Z-score, etc.], we cannot guarantee a balanced data with a normal distribution."* Since the **median and quartiles are far more robust to extreme values** than the mean/min/max, this scaler produces more reliable results specifically when a dataset has significant outliers — directly addressing the same outlier-robustness concern first raised for imputation in Lecture 6 ([[09_Missing_Values_Imputation_Methods]] from Lecture 6, where median was preferred over mean for outlier-heavy data).

**Worked example**: same running dataset from Lecture 7, `X = [2, 47, 90, 18, 5]`.
- Sorted: `2, 5, 18, 47, 90`
- Using the standard **linear-interpolation percentile method** (the default method used by tools like NumPy/pandas): `Q1 = 5` (25th percentile), `Q2 = 18` (50th percentile, the median), `Q3 = 47` (75th percentile).
- `IQR = Q3 − Q1 = 47 − 5 = 42`
- `X'= (X − 18) / 42`
  - `X=2`: `(2−18)/42 = −16/42 = −0.38095238`
  - `X=47`: `(47−18)/42 = 29/42 = 0.69047619`
  - `X=90`: `(90−18)/42 = 72/42 = 1.71428571`
  - `X=18`: `(18−18)/42 = 0`
  - `X=5`: `(5−18)/42 = −13/42 = −0.30952381`

Result: `X' = [−0.38095238, 0.69047619, 1.71428571, 0, −0.30952381]` — exactly matching the lecture's stated output, confirming Q1/Q2/Q3 were computed via the linear-interpolation method (not a simpler "split the sorted list in half" approach, which would have given different Q1/Q3 values).

---

## 2) Simple English Explanation

This lecture picks up exactly where Lecture 7 left off — completing the last of the seven scaling methods that was only named but not worked through: the **Interquartile (Robust) Scaler**.

**Why do we need yet another scaling method?** Because the earlier methods (Min-Max, Mean Normalization, Z-score) all rely on the mean, minimum, or maximum of your data — and all three of those get thrown off badly if your dataset has outliers (extreme values). Remember the earlier example of weights `67, 78, 900, −56, 389, −1`? The mean got dragged way off by those bad values. The Robust Scaler avoids this problem by using the **median and quartiles** instead — these are much more resistant to a few extreme values messing things up.

**The formula**: take a value, subtract the **median** (Q2), then divide by the **IQR** (the gap between the 75th percentile and the 25th percentile).

**Worked example**: using `2, 47, 90, 18, 5` again — sorted, that's `2, 5, 18, 47, 90`. The median (Q2) is `18`. The 25th percentile (Q1) is `5`, and the 75th percentile (Q3) is `47`, so the IQR is `47 − 5 = 42`.
- `2` → `(2−18)/42 = −0.381`
- `47` → `(47−18)/42 = 0.690`
- `90` → `(90−18)/42 = 1.714`
- `18` → `0` (since it *is* the median)
- `5` → `(5−18)/42 = −0.310`

This is especially useful whenever your data has a few weird outlier values, since — unlike the mean-based methods — it won't get skewed by them.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture bilkul wahi se shuru hoti hai jaha Lecture 7 chhoda gaya tha — 7 scaling methods mein se aakhri wala jo sirf naam liya gaya tha, bina worked karne ke: **Interquartile (Robust) Scaler**.

**Ek aur scaling method ki zaroorat kyun padi?**
Kyunki pehle wale methods (Min-Max, Mean Normalization, Z-score) sab **mean, minimum, ya maximum** pe depend karte hai — aur ye teeno bahut kharab hone lagte hai agar aapke data mein outliers (extreme values) ho. Yaad hai wo pehle wala example weights `67, 78, 900, −56, 389, −1` ka? Mean un bad values ki wajah se bahut door khinch gaya tha. **Robust Scaler** iss problem ko **median aur quartiles** use karke avoid karta hai — ye kuch extreme values se distract hone mein bahut zyada resistant hote hai.

**Formula**: ek value lo, **median (Q2)** subtract karo, fir **IQR** (75th percentile aur 25th percentile ke beech ka gap) se divide karo.

**Worked example**: wahi `2, 47, 90, 18, 5` use karke — sorted karne pe `2, 5, 18, 47, 90` ban jaata hai. Median (Q2) hai `18`. 25th percentile (Q1) hai `5`, aur 75th percentile (Q3) hai `47`, isliye IQR = `47 − 5 = 42`.
- `2` → `(2−18)/42 = −0.381`
- `47` → `(47−18)/42 = 0.690`
- `90` → `(90−18)/42 = 1.714`
- `18` → `0` (kyunki ye khud median hai)
- `5` → `(5−18)/42 = −0.310`

Ye khaaskar tab useful hai jab aapke data mein kuch ajeeb outlier values ho, kyunki — mean-based methods ke ulat — ye unse skew nahi hota.
