# Topic 2: Worked Exercise Setup — Plant Dry Weight Dataset

Source: Lecture 14, slides 6–7 ("Exercise").

---

## 1) Technical Explanation

**The dataset (slides 6–7).** A new worked example is introduced — a classic-style multiple-regression exercise relating a plant's dry weight to two soil measurements, across 7 observations:

| Y (plant dry weight, grams) | X1 (soil organic matter, %) | X2 (supplemental soil nitrogen, kg per 100 m²) |
|---|---|---|
| 78.5 | 7 | 2.6 |
| 74.3 | 1 | 2.9 |
| 104.3 | 11 | 5.6 |
| 87.6 | 11 | 3.1 |
| 95.9 | 7 | 5.2 |
| 109.2 | 11 | 5.5 |
| 102.7 | 3 | 7.1 |

The slide's own annotation identifies the roles clearly:
- **Y** is the **dependent variable** — plant dry weight is the outcome we want to predict.
- **X1 and X2** are the **independent variables** — soil organic matter and supplemental nitrogen are the inputs used to predict Y.

**The task (slide 7), given in two parts:**
1. **Obtain the regression equation** — i.e., find the actual numeric coefficients that best fit this data, not just the general symbolic form.
2. **Predict the dry weight** for a new case where soil organic matter (X1) = 5 and soil nitrogen (X2) = 4.

**The equation form to be fitted (slide 7's annotation):**

**y = β₀ + β₁ × x₁ + β₂ × x₂**

This introduces one more, equally standard, notation for regression coefficients: **β (beta)** — β₀, β₁, β₂ are called the **regression coefficients**. This is the third naming convention the lecture sequence has now used for essentially the same concept:
- m / b (Lecture 13, simple regression: slope/intercept)
- a / b or a₀…aₙ (Lecture 13's multiple-regression intro and this lecture's slide 5: intercept/coefficients)
- β₀, β₁, β₂ (this exercise, and standard in statistics literature more broadly — "beta" is in fact the most common symbol used for regression coefficients in academic statistics papers)

All three notations describe the exact same mathematical object — there is no conceptual difference, just different textbooks/instructors preferring different Greek/Latin letters. This exercise is deliberately solved using the **matrix approach** (rather than the earlier Σ(x−x̄)(y−ȳ)/Σ(x−x̄)² formula), because with two or more predictors, the single-variable slope formula from [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]] from Lecture 13 no longer applies directly — that formula only works for exactly one x. The matrix-based normal equation method, worked through step-by-step in [[03_Matrix_Approach_Normal_Equation_Worked_Solution]], is the general solution that works for any number of predictors, including this two-predictor case.

---

## 2) Simple English Explanation

Here's a brand new example to practice multiple regression on. Imagine a scientist growing plants, measuring three things about each plant/plot of soil:

| Plant dry weight (Y) | Soil organic matter (X1) | Soil nitrogen added (X2) |
|---|---|---|
| 78.5 | 7 | 2.6 |
| 74.3 | 1 | 2.9 |
| 104.3 | 11 | 5.6 |
| 87.6 | 11 | 3.1 |
| 95.9 | 7 | 5.2 |
| 109.2 | 11 | 5.5 |
| 102.7 | 3 | 7.1 |

The question we want answered: **does more organic matter and more nitrogen in the soil lead to heavier, healthier plants?** And if so, by exactly how much?

- **Y (dry weight)** is what we're trying to predict.
- **X1 (organic matter) and X2 (nitrogen)** are the two clues we're using to predict it.

**The task has two parts:**
1. Find the actual formula (with real numbers plugged in) that best predicts Y from X1 and X2.
2. Use that formula to predict the dry weight of a plant grown in soil with organic matter = 5 and nitrogen = 4 (values that don't appear directly in the table).

The target formula shape is: **y = β₀ + β₁×x₁ + β₂×x₂**. Notice this uses yet another letter — **β (pronounced "beta")** — instead of m/b or a₀/a₁/a₂ from before. Don't let this confuse you: β₀, β₁, β₂ mean exactly the same thing as "intercept, coefficient-for-first-input, coefficient-for-second-input" from the previous topic. Different books and teachers just like different letters for the same idea — β happens to be the most commonly used one in professional statistics.

Since we now have *two* inputs instead of one, the simple slope formula from Lecture 13 (which only works for a single x) won't cut it anymore. The next topic, [[03_Matrix_Approach_Normal_Equation_Worked_Solution]], shows the proper general method — using matrices — that works no matter how many inputs you have.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yeh ek bilkul naya example hai multiple regression practice karne ke liye. Socho ek scientist plants ugaa raha hai, aur har plant/soil-plot ke baare mein teen cheezein measure kar raha hai:

| Plant ka dry weight (Y) | Soil organic matter (X1) | Soil nitrogen added (X2) |
|---|---|---|
| 78.5 | 7 | 2.6 |
| 74.3 | 1 | 2.9 |
| 104.3 | 11 | 5.6 |
| 87.6 | 11 | 3.1 |
| 95.9 | 7 | 5.2 |
| 109.2 | 11 | 5.5 |
| 102.7 | 3 | 7.1 |

Sawaal yeh hai: **kya zyada organic matter aur zyada nitrogen soil mein hone se plant zyada bhari/healthy hota hai?** Aur agar haan, toh kitna zyada?

- **Y (dry weight)** wo cheez hai jo predict karni hai.
- **X1 (organic matter) aur X2 (nitrogen)** do clues hain jinse predict karte hain.

**Task ke do parts hain:**
1. Actual formula dhundo (real numbers ke saath) jo X1 aur X2 se Y ko best predict kare.
2. Us formula se predict karo ki agar organic matter = 5 aur nitrogen = 4 ho, toh dry weight kya hogi (yeh values table mein directly nahi hain).

Target formula ka shape yeh hai: **y = β₀ + β₁×x₁ + β₂×x₂**. Notice karo ki yahan ek aur naya letter use hua hai — **β (bolte hain "beta")** — pehle wale m/b ya a₀/a₁/a₂ ki jagah. Confuse mat ho — β₀, β₁, β₂ ka matlab bilkul wahi hai jo "intercept, pehle input ka coefficient, dusre input ka coefficient" tha pichle topic mein. Alag books aur teachers bas alag letters pasand karte hain same idea ke liye — β professional statistics mein sabse zyada common letter hai.

Ab humare paas *do* inputs hain, ek ki jagah, toh Lecture 13 wala simple slope formula (jo sirf ek x ke liye kaam karta hai) kaam nahi karega. Agla topic, [[03_Matrix_Approach_Normal_Equation_Worked_Solution]], sahi general method dikhata hai — matrices use karke — jo kitne bhi inputs ho, kaam karta hai.
