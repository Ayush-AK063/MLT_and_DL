# Topic 12: Outlier Analysis — Types & Detection Methods (IQR, Boxplot, Z-score)

Source: Lecture 6, slides 36–41 (Outlier Analysis, Extreme Value Analysis — IQR method with worked example, Box-Plot method, Z-score method).

---

## 1) Technical Explanation

**Definition**: *"An outlier is an object that deviates significantly from the rest of the objects."* Causes: **measurement or execution error**. *"The analysis of outlier data is referred to as outlier analysis or outlier mining."* Illustrated visually with a "school of fish" analogy — one differently-colored fish standing out from a large uniform school — and a scatter plot showing one point far separated from three natural clusters (labeled C1, C2, C3).

**Types of Outliers (slide 37)**:
- **Univariate**: *"a data point that consists of an extreme value on one variable"* — an outlier detectable by looking at just a single feature/column in isolation.
- **Multivariate**: *"a combination of unusual scores on at least two variables"* — a point that isn't necessarily extreme on any single variable, but is unusual when multiple variables are considered together.

**Outlier Detection and Handling Methods — four named categories**:
1. Extreme Value Analysis
2. Linear Models
3. Proximity-based Methods
4. Information Theoretic Methods

(Only the first is worked through in detail in this lecture, via two specific techniques: IQR and Z-score.)

**Method 1 — IQR (InterQuartile Range) / "Numeric Outlier" method (slide 38)**:
- Described as *"the simplest, nonparametric outlier detection method in a one-dimensional feature space."*
- Calculate the first quartile (**Q1**, 25th percentile) and third quartile (**Q3**, 75th percentile).
- `IQR = Q3 − Q1`
- A data point `xᵢ` is an outlier if: `xᵢ > Q3 + k(IQR)` **or** `xᵢ < Q1 − k(IQR)`, where `k ≥ 0` (commonly `k = 1.5`).

**Worked example — the "chapati" dataset**: `6, 2, 1, 5, 4, 3, 50` (representing the number of chapatis eaten at lunch by 7 people).
- Sorted: `1, 2, 3, 4, 5, 6, 50`
- Q1 (25th percentile) = **2**
- Q2 (50th percentile, the median) = **4.0**
- Q3 (75th percentile) = **6**
- `IQR = Q3 − Q1 = 6 − 2 = 4`
- Using `k = 1.5`: lower bound = `Q1 − 1.5×IQR = 2 − 6 = −4` (lecture states the range as effectively `0` on the low end, since chapati count can't be negative); upper bound = `Q3 + 1.5×IQR = 6 + 6 = 12`.
- Since `50 > 12`, **50 is flagged as an outlier** — correctly matching intuition (nobody realistically eats 50 chapatis at lunch when everyone else ate 1–6).

**Method 1 continued — Box-Plot method (slide 39)**: visually formalizes the exact same IQR logic. A boxplot shows Q1, Q2 (median), Q3 as the box, with "whiskers" extending to `Q1 − 1.5×IQR` and `Q3 + 1.5×IQR`; any points beyond the whiskers are outliers. The accompanying normal-distribution diagram shows this bound roughly corresponds to about **±2.698 standard deviations (σ)** from the mean under a Gaussian assumption, capturing the central ~99.3% of data (0.35% + 24.65% + 50% + 24.65% + 0.35% = 100%, with the two 0.35% tail regions representing the outlier zones beyond the whiskers).

**Method 2 — Z-score (slides 40–41)**:
- A **parametric** outlier detection method for one or low-dimensional feature spaces, which **assumes a Gaussian (normal) distribution** of the data.
- Formula: `z = (x − μ) / σ`, where `x` is a data point, `μ` is the mean of all data points, and `σ` is the standard deviation.
- A point is an outlier if its absolute z-score exceeds a threshold: `|zᵢ| > z_thr`.
- **Commonly used threshold values**: **2.5, 3.0, or 3.5** — meaning a point more than 2.5–3.5 standard deviations away from the mean is flagged as unusual/extreme.
- Key distinction from IQR: Z-score explicitly assumes normally-distributed data (parametric), while IQR makes no distributional assumption (nonparametric) — making IQR more broadly applicable when the data's distribution shape is unknown or non-Gaussian.

---

## 2) Simple English Explanation

This section teaches you how to formally define and *find* outliers — not just eyeball them on a chart, but calculate exactly which points count as outliers.

**What's an outlier?** A data point that's dramatically different from the rest — usually caused by a measurement mistake or something going wrong during data collection. Think of it like spotting one oddly-colored fish in a huge school of identical fish — it just stands out.

**Two types of outliers:**
- **Univariate** — a point that's extreme on just *one* measurement (like someone's height being 3 meters — obviously wrong on that single feature alone).
- **Multivariate** — a point that's not extreme on any single measurement, but is weird when you look at a *combination* of measurements together (like a person who is 5 years old but 6 feet tall — neither number alone is impossible, but together they don't make sense).

**Method 1 — The IQR method (using quartiles)**: Split your sorted data into four equal parts. Q1 is the value 25% of the way through, Q3 is the value 75% of the way through. The gap between them (Q3 − Q1) is called the IQR. Anything that falls too far below Q1 or too far above Q3 (specifically, more than 1.5× the IQR distance) is considered an outlier.

**A fun worked example**: Imagine 7 people reporting how many chapatis they ate at lunch: 6, 2, 1, 5, 4, 3, and **50**. Obviously, 50 chapatis is absurd compared to everyone else eating 1–6. Running the actual math (Q1=2, Q3=6, IQR=4, upper cutoff = 6 + 1.5×4 = 12) confirms it mathematically: since 50 is way above 12, **it's officially flagged as an outlier** — matching our common sense.

**The Box-Plot method** is just a visual way of showing this exact same IQR calculation — the "box" shows Q1 to Q3, and the "whiskers" extend out to the 1.5×IQR cutoff points. Anything plotted beyond the whiskers is an outlier.

**Method 2 — The Z-score method**: This one assumes your data roughly follows a bell-curve (normal/Gaussian) shape. It measures how many "standard deviations" away from the average each point is, using the formula `z = (value − average) / standard deviation`. If a point's z-score (ignoring plus/minus sign) is bigger than a chosen cutoff — commonly 2.5, 3.0, or 3.5 — it's flagged as an outlier. The key difference from IQR: Z-score only really works well if your data actually looks like a bell curve; IQR doesn't require that assumption, making it more flexible.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section sikhata hai outliers ko **formal tarike se define aur calculate** karna — sirf chart dekh kar guess nahi karna, balki exactly ye batana ki kaunse points outlier hai.

**Outlier kya hai?**
Ek data point jo baaki sab se **dramatically alag** hai — usually kisi measurement mistake ya data collection mein kuch galat hone ki wajah se. Socho ek badi machhliyon ki school (jhund) mein ek alag-color wali machhli dekhna — wo bas standout karti hai.

**Outliers ke 2 types:**
- **Univariate** — ek point jo sirf **ek** measurement pe extreme hai (jaise kisi ki height 3 meter hona — sirf isi ek feature pe obviously galat hai).
- **Multivariate** — ek point jo kisi single measurement pe extreme nahi hai, lekin jab **combination** mein dekha jaaye to weird hai (jaise koi 5 saal ka bacha jiski height 6 feet ho — koi bhi number akela impossible nahi hai, lekin dono saath mein sense nahi banate).

**Method 1 — IQR Method (Quartiles use karke):**
Apne sorted data ko 4 equal parts mein baanto. **Q1** wo value hai jo 25% raste tak hai, **Q3** wo value hai jo 75% raste tak hai. In dono ke beech ka gap (Q3 − Q1) ko **IQR** kehte hai. Jo bhi cheez Q1 se bahut neeche ya Q3 se bahut upar hai (specifically, 1.5× IQR distance se zyada), wo outlier maana jaata hai.

**Ek maza aane wala worked example**: Socho 7 log batate hai lunch mein kitne chapati khaye: 6, 2, 1, 5, 4, 3, aur **50**. Obviously, 50 chapati bahut ajeeb hai jab baaki sab ne 1-6 khaye. Actual maths lagane pe (Q1=2, Q3=6, IQR=4, upper cutoff = 6 + 1.5×4 = 12) mathematically bhi confirm hota hai: kyunki 50, 12 se bahut zyada hai, **isko officially outlier mark kiya jaata hai** — jo humare common sense se match karta hai.

**Box-Plot Method** basically isi IQR calculation ko visually dikhane ka tarika hai — "box" Q1 se Q3 tak dikhata hai, aur "whiskers" (musse) 1.5×IQR cutoff points tak extend hote hai. Jo bhi whiskers ke bahar plot hota hai, wo outlier hai.

**Method 2 — Z-score Method:**
Ye assume karta hai ki aapka data roughly bell-curve (normal/Gaussian) shape follow karta hai. Ye measure karta hai ki har point average se kitne "standard deviations" door hai, is formula se: `z = (value − average) / standard deviation`. Agar kisi point ka z-score (plus/minus sign ignore karke) ek chosen cutoff se bada hai — commonly **2.5, 3.0, ya 3.5** — to use outlier mark kiya jaata hai. IQR se main farak: Z-score sirf tab achha kaam karta hai jab data actually bell curve jaisa ho; IQR ko aisi koi assumption nahi chahiye, isliye ye zyada flexible hai.
