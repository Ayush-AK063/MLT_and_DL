# Topic 5: Scaling/Normalization — Z-score Method & Decimal Scaling Method

Source: Lecture 7, slides 17–18 (Z Score method, Decimal scaling method).

Same running dataset as Topic 4: `X = [2, 47, 90, 18, 5]`.

---

## 1) Technical Explanation

### Method 3: Z-score Method

**Formula**: `X' = (X − X̄) / σ`

Where `X̄` is the mean and `σ` (sigma) is the **standard deviation** of the feature column. This is the same formula introduced for **outlier detection** in Lecture 6 ([[12_Outlier_Analysis_and_Detection_Methods]] from Lecture 6) — here it's repurposed not to flag outliers, but as a general-purpose **scaling** technique. Unlike Min-Max/Mean normalization (which use the range `Xmax − Xmin` as the denominator), Z-score uses the **standard deviation**, making it sensitive to how spread out the data actually is (not just its min/max extremes).

**Worked example**: `X = [2, 47, 90, 18, 5]`, mean `X̄ = 32.4` (as computed in Topic 4).
- Verifying the standard deviation used: computing deviations from the mean (`−30.4, 14.6, 57.6, −14.4, −27.4`), squaring them (`924.16, 213.16, 3317.76, 207.36, 750.76`), summing (`5413.2`), and dividing by **(n−1) = 4** (the *sample* standard deviation formula) gives a variance of `1353.3`, so `σ ≈ 36.79`.
- `X=2`: `(2−32.4)/36.79 = −30.4/36.79 = −0.826`
- `X=47`: `(47−32.4)/36.79 = 14.6/36.79 = 0.397`
- `X=90`: `(90−32.4)/36.79 = 57.6/36.79 = 1.566`
- `X=18`: `(18−32.4)/36.79 = −14.4/36.79 = −0.391`
- `X=5`: `(5−32.4)/36.79 = −27.4/36.79 = −0.745`

Result: `X' = [−0.826, 0.397, 1.566, −0.391, −0.745]` — exactly matching the lecture's stated output, confirming the **sample** (n−1) standard deviation formula was used, not the population (n) version.

---

### Method 4: Decimal Scaling Method

**Formula**: `X' = X / 10^j`

Where `j` is *"maximum of the count of digits in minimum and maximum value of feature vector corresponding to X"* — i.e., count how many digits are in the largest-magnitude value in the column, and use that count as `j`.

**Worked example**: `X = [2, 47, 90, 18, 5]`. The maximum value is `90`, which has **2 digits**, so `j = 2`, meaning divide every value by `10² = 100`.
- `X=2`: `2/100 = 0.02`
- `X=47`: `47/100 = 0.47`
- `X=90`: `90/100 = 0.90`
- `X=18`: `18/100 = 0.18`
- `X=5`: `5/100 = 0.05`

Result: `X' = [0.02, 0.47, 0.90, 0.18, 0.05]` — exactly matching the lecture's stated output.

**Note on decimal scaling's simplicity**: unlike the other methods, this doesn't require computing a mean, standard deviation, or the exact min/max — just the digit-count of the largest value — making it the computationally cheapest normalization method covered, though it doesn't guarantee the resulting range is exactly [0,1] the way Min-Max does (it only guarantees results stay below 1 in magnitude, assuming all original values are positive).

---

## 2) Simple English Explanation

### Z-score Method

This is the exact same formula you saw earlier for spotting outliers (in Lecture 6) — but here it's being reused as a scaling technique instead. It measures how many "standard deviations" away from the average each value is.
- The formula: take a number, subtract the average, then divide by the standard deviation (a measure of how spread out the data is).
- Applying it to `2, 47, 90, 18, 5` (average = 32.4): `2` → `−0.826`, `47` → `0.397`, `90` → `1.566`, `18` → `−0.391`, `5` → `−0.745`.
- The key difference from Min-Max/Mean normalization: instead of dividing by the "range" (biggest minus smallest), Z-score divides by the standard deviation — a statistic that captures how "typical" the spread of the data is, which can behave differently if there are a few extreme values.

### Decimal Scaling Method

This is the simplest method of the bunch. You just figure out how many digits are in your largest number, and divide every value by 10 raised to that many digits.
- In our example, the biggest number is `90`, which has 2 digits. So you divide everything by `10² = 100`.
- Applying it: `2` → `0.02`, `47` → `0.47`, `90` → `0.90`, `18` → `0.18`, `5` → `0.05`.
- This is basically just "moving the decimal point" — super quick to calculate, since you don't need to know the average or the standard deviation, just how big the numbers are.

---

## 3) Hinglish Explanation (Beginner-Friendly)

### Z-score Method

Ye bilkul wahi formula hai jo aapne pehle outliers dhoondhne ke liye dekha tha (Lecture 6 mein) — lekin yaha isse scaling technique ki tarah reuse kiya ja raha hai. Ye measure karta hai ki har value average se kitne "standard deviations" door hai.
- Formula: ek number lo, average subtract karo, fir standard deviation (data kitna spread out hai iska measure) se divide karo.
- `2, 47, 90, 18, 5` (average = 32.4) pe apply karke: `2` → `−0.826`, `47` → `0.397`, `90` → `1.566`, `18` → `−0.391`, `5` → `−0.745`.
- Min-Max/Mean Normalization se main farak: "range" (sabse bada minus sabse chhota) se divide karne ke bajaye, Z-score standard deviation se divide karta hai — ek statistic jo batati hai data kitna "typical" spread hua hai, jo kuch extreme values hone pe alag behave kar sakti hai.

### Decimal Scaling Method

Ye sabme sabse simple method hai. Aap bas ye pata karo ki aapke sabse bade number mein kitne digits hai, aur har value ko `10` ko utni power se raise karke divide karo.
- Humare example mein, sabse bada number `90` hai, jisme 2 digits hai. To sab kuch `10² = 100` se divide karo.
- Apply karke: `2` → `0.02`, `47` → `0.47`, `90` → `0.90`, `18` → `0.18`, `5` → `0.05`.
- Ye basically **decimal point ko move karna** hai — bahut jaldi calculate ho jaata hai, kyunki aapko average ya standard deviation janna zaroori nahi, bas numbers kitne bade hai wo jaanna hai.
