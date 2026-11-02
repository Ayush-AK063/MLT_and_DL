# Topic 3: Multiple Linear Regression — Worked Example (Home Prices)

Source: Lecture 13, slides 12–17 (extended home price dataset with 3 features, multiple regression equation, coefficients, features terminology). Independently verified numerically, with real-dataset cross-check via web research.

---

## 1) Technical Explanation

**The extended dataset (slide 12).** The single-feature home price example from [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]] is now extended with two more input columns — `bedrooms` and `age` — and a **new set of price values** (not the same prices as the earlier example, since a different, more realistic dataset is now in play):

| area | bedrooms | age | price |
|---|---|---|---|
| 2600 | 3 | 20 | 550000 |
| 3000 | 4 | 15 | 565000 |
| 3200 | *(blank)* | 18 | 610000 |
| 3600 | 3 | 30 | 595000 |
| 4000 | 5 | 8 | 760000 |

Note the **blank cell** for `bedrooms` on the 3200-sqft row — this is a genuine missing value in the source data, not a formatting slip. The slide does not explicitly address how to handle it, but this connects directly to the missing-data-handling techniques covered earlier in the course: mean/median imputation, discussed in [[09_Missing_Values_Imputation_Methods]] from Lecture 6. The standard practical fix (used by the well-known tutorial this dataset is drawn from — see "Verification" below) is to fill the missing value with the **median** of the other bedroom counts.

**The multiple regression equation (slides 13–17).** With three input features now, a single slope `m` is no longer enough — each feature gets its *own* coefficient:

**price = m₁ × area + m₂ × bedrooms + m₃ × age + b**

Generalized with x-notation (slide 17): **y = m₁x₁ + m₂x₂ + m₃x₃ + b**

The slides label the parts of this equation explicitly (slides 15–16):
- **y (price)** is still the single **dependent variable**.
- **x₁, x₂, x₃ (area, bedrooms, age)** are the **independent variables**, now also called **features** — this is the first time the course uses the word "feature," which is standard ML terminology for an input column used to make a prediction.
- **m₁, m₂, m₃** are called **coefficients** (rather than "the slope," since there isn't one single slope anymore — each feature has its own weight indicating how much it individually pulls the prediction up or down, holding the other features fixed).
- **b** remains the intercept, same role as before.

**The task posed (slide 13).** Given this data, predict the price of a home with:
1. 3000 sqft area, 3 bedrooms, 40 years old
2. 2500 sqft area, 4 bedrooms, 5 years old

**Verification and an important caveat.** Unlike the simple linear regression example, this multiple-regression problem is **not something the slides show being solved by hand** — and for good reason: fitting m₁, m₂, m₃, and b from only 5 data points (one of which has a missing feature) is a 4-unknowns, 5-equations least-squares problem, which is technically solvable but numerically fragile. I fit it directly (filling the missing bedroom value with the median of the other 4 values, 3.5) and got:

- m₁ (area) ≈ **198.47**
- m₂ (bedrooms) ≈ **−116,583.74**
- m₃ (age) ≈ **−14,267.78**
- b (intercept) ≈ **656,046.54**

This gives predictions of ≈ **₹330,999** for query 1 and ≈ **₹614,552** for query 2. However, the *negative* bedroom coefficient here (more bedrooms → lower predicted price, holding area/age fixed) is a red flag: it's not physically sensible, and it's a textbook symptom of fitting too many parameters to too few, noisy data points (the model is essentially memorizing quirks of these specific 5 rows rather than learning a stable real-world trend).

This exact dataset (area/bedrooms/age/price, with the same missing bedroom cell) is, in fact, the well-known home-price dataset from a widely used machine-learning tutorial series (the "codebasics" Multiple Linear Regression tutorial), which normally includes a **6th row** (4100 sqft, 6 bedrooms, 8 years, ₹810,000) that the slide's version omits. Fitting scikit-learn's `LinearRegression` on the full 6-row dataset (median-imputed bedrooms) gives a much more stable, intuitively-signed fit: m₁ (area) ≈ 112.06, m₂ (bedrooms) ≈ +23,388.88, m₃ (age) ≈ −3,231.72, b ≈ 221,323.00 — predicting ≈ ₹498,408 for query 1 and ≈ ₹578,876 for query 2. (Source: [codebasics/py — ML/2_linear_reg_multivariate](https://github.com/codebasics/py/blob/master/ML/2_linear_reg_multivariate/2_linear_regression_multivariate.ipynb).)

**Takeaway worth flagging explicitly**: the slide's 5-row version of this dataset is genuinely under-determined for a reliable 3-feature fit — this is a good real illustration of why multiple regression needs *enough data relative to the number of features* to give trustworthy, well-signed coefficients, and why in practice this kind of fitting is always done in code (e.g., `sklearn.linear_model.LinearRegression`) rather than by hand, unlike the single-feature case in [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]] which is small enough to verify by hand.

---

## 2) Simple English Explanation

Now the same house-price idea gets one level harder: instead of predicting price from *just* area, we add two more clues — **number of bedrooms** and **age of the house** (in years).

| area | bedrooms | age | price |
|---|---|---|---|
| 2600 | 3 | 20 | 550000 |
| 3000 | 4 | 15 | 565000 |
| 3200 | ? (missing!) | 18 | 610000 |
| 3600 | 3 | 30 | 595000 |
| 4000 | 5 | 8 | 760000 |

Notice one entry is **blank** — the number of bedrooms for the 3200-sqft house wasn't recorded. This is a real, common problem with real data, and you can't just skip that row; the usual trick (and what the original tutorial this data comes from actually does) is to fill it in with a sensible guess — typically the **median** bedroom count of the other houses.

**The formula now has 3 "weights" instead of 1**: `price = m1×area + m2×bedrooms + m3×age + b`. Each input now gets its own personal multiplier (m1, m2, m3) that says how much that particular thing matters for price, and these inputs are now called **features** — that's just the standard word for "a column of data you feed the model."

The question the slide asks: what would a house cost with (a) 3000 sqft, 3 bedrooms, 40 years old, and (b) 2500 sqft, 4 bedrooms, 5 years old?

**Here's the honest, useful catch**: the slide never actually shows you the numbers m1, m2, m3, b for this problem — and when I computed them myself from just these 5 rows, I got a genuinely *weird* result: the "bedrooms" weight came out *negative*, meaning the formula would say "more bedrooms = cheaper house," which doesn't match common sense. This isn't a mistake in my math — it's what actually happens when you try to fit a formula with 4 unknowns (m1, m2, m3, b) using only 5 data points, one of which is even missing a value. There just isn't enough data to pin down a trustworthy answer; the formula ends up fitting noise/coincidences in these specific 5 houses instead of a real pattern.

I tracked down where this exact dataset comes from — a very popular machine learning tutorial online that uses this same table but with **one extra 6th house**. With that extra data point, the fit becomes sensible: more bedrooms genuinely pushes the price up a bit, more age pushes it down a bit, and the predictions come out to roughly ₹498,408 and ₹578,876 for the two questions. The lesson here: **multiple regression needs enough data relative to how many features you're using**, or the answer becomes unreliable — and this is exactly why, in real practice, nobody fits these by hand; you always use code (like Python's scikit-learn library) which handles this properly.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab wahi ghar-price wala idea ek level tough ho jaata hai: sirf area se predict karne ke bajaye, do aur clues add hote hain — **bedrooms ki sankhya** aur **ghar ki age** (saalon mein).

| area | bedrooms | age | price |
|---|---|---|---|
| 2600 | 3 | 20 | 550000 |
| 3000 | 4 | 15 | 565000 |
| 3200 | ? (missing!) | 18 | 610000 |
| 3600 | 3 | 30 | 595000 |
| 4000 | 5 | 8 | 760000 |

Ek entry **khaali** hai — 3200 sqft ghar ke bedrooms record nahi hue. Yeh real data mein bahut common problem hai, aur is row ko simply skip nahi kar sakte; usual trick (aur jo original tutorial yeh data karta hai) yeh hai ki uski jagah ek sensible guess bhar do — generally baaki bedrooms ka **median**.

**Formula mein ab 3 "weights" hain, 1 ki jagah**: `price = m1×area + m2×bedrooms + m3×age + b`. Har input ka apna alag multiplier hai (m1, m2, m3) jo batata hai ki wo cheez price ke liye kitni matter karti hai, aur inputs ko ab **features** bolte hain — yeh standard word hai "data ka ek column jo model ko diya jaata hai" ke liye.

Slide ka sawaal: agar ek ghar (a) 3000 sqft, 3 bedroom, 40 saal purana ho, aur (b) 2500 sqft, 4 bedroom, 5 saal purana ho, toh price kya hogi?

**Yahan ek honest aur useful catch hai**: slide kabhi bhi m1, m2, m3, b ke numbers nahi dikhati is problem ke liye — aur jab maine khud calculate kiya sirf in 5 rows se, toh genuinely **ajeeb** result mila: "bedrooms" ka weight **negative** aaya, matlab formula bolega "zyada bedrooms = sasta ghar," jo common sense ke against hai. Yeh mera calculation mistake nahi hai — yeh actually hota hai jab aap 4 unknowns (m1, m2, m3, b) ko sirf 5 data points se fit karne ki koshish karte ho, jisme se ek mein toh value hi missing hai. Itna data nahi hai ki ek trustworthy answer nikle; formula in 5 specific ghar ke coincidences ko fit kar raha hai, kisi real pattern ko nahi.

Maine pata lagaya ki yeh exact dataset kahan se aaya — ek bahut popular machine learning tutorial jisme yahi table hai lekin ek **6th ghar extra** ke saath. Us extra data ke saath, fit sensible ban jaata hai: zyada bedrooms se price genuinely thodi badhti hai, zyada age se thodi ghatati hai, aur predictions aate hain roughly ₹498,408 aur ₹578,876 dono sawaalon ke liye. Yahan se seekh yeh hai: **multiple regression ke liye features ke hisaab se kaafi data chahiye**, warna answer unreliable ho jaata hai — aur isiliye real practice mein koi bhi hath se yeh fit nahi karta; hamesha code use karte hain (jaise Python ki scikit-learn library), jo isko sahi tarike se handle karti hai.
