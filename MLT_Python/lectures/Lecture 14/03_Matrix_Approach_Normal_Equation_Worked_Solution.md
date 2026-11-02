# Topic 3: The Matrix Approach — Normal Equation and Full Worked Solution

Source: Lecture 14, slides 8–15 ("Matrix Approach", 2×2 matrix inverse recap, the Y/X matrices, β = (XᵀX)⁻¹XᵀY, the full computation, and the final prediction). Enriched with web research (normal equation derivation). Independently re-verified numerically, matching the slide's handwritten result almost exactly.

---

## 1) Technical Explanation

**Why matrices are needed (slides 8–9).** For the two-predictor plant dry weight example from [[02_Worked_Exercise_Setup_Plant_Dry_Weight_Dataset]], the target model is:

**y = β₀ + β₁×x₁ + β₂×x₂**, with **β = [β₀, β₁, β₂]ᵀ** — a 3×1 column vector of unknowns to solve for.

Since there are 7 data rows and only 3 unknowns, this is an **overdetermined system** — more equations than unknowns — so there is generally no exact solution that satisfies all 7 rows perfectly. The matrix approach finds the β that minimizes the total squared error across all 7 rows simultaneously (the same least-squares principle from [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]] from Lecture 13, now generalized to work for any number of predictors at once, whereas that lecture's b-formula only handled one).

**Building the matrices (slides 8, 10–11).** Two matrices are constructed from the 7-row dataset:

- **Y** — the 7×1 column vector of the dependent variable (dry weight) values.
- **X** — a 7×3 matrix: the **first column is all 1s** (this represents the intercept β₀, exactly the way the "+b" or "+c" constant is absorbed into the matrix formulation), and the second and third columns are X1 and X2 respectively:

```
      ⎡78.5⎤        ⎡1   7   2.6⎤
      ⎢74.3⎥        ⎢1   1   2.9⎥
      ⎢104.3⎥       ⎢1  11   5.6⎥
Y  =  ⎢87.6⎥   X  =  ⎢1  11   3.1⎥
      ⎢95.9⎥        ⎢1   7   5.2⎥
      ⎢109.2⎥       ⎢1  11   5.5⎥
      ⎣102.7⎦        ⎣1   3   7.1⎦
```

**The normal equation (slides 11–13).** The slide states the closed-form matrix solution directly:

**β = (XᵀX)⁻¹XᵀY**

This is called the **normal equation**. Where does it come from (not derived on the slide, filled in via research)? Starting from the least-squares goal — minimize the sum of squared errors (Y − Xβ)ᵀ(Y − Xβ) — taking the derivative of this expression with respect to β and setting it to zero gives **XᵀXβ = XᵀY** (these are literally called "the normal equations" in statistics), and solving for β by multiplying both sides by (XᵀX)⁻¹ gives the formula above. This is exactly analogous to solving a simple equation like 3β=9 by dividing both sides by 3 — except here "dividing" by a matrix means multiplying by its inverse, because matrix division isn't directly defined. (Source: [Normal Equation in Linear Regression — GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/ml-normal-equation-in-linear-regression/); [Deriving Normal Equation for Multiple Linear Regression — Medium](https://medium.com/@bhanu0925/deriving-normal-equation-for-multiple-linear-regression-85241965ee3b).)

The slide also recaps (slide 10) the general **2×2 matrix inverse formula** as a warm-up reminder: for A = [[a,b],[c,d]], A⁻¹ = (1/(ad−bc)) × [[d,−b],[−c,a]]. The actual (XᵀX) here is **3×3**, which needs the more general matrix-inverse procedure (cofactors/adjugate, or Gaussian elimination) rather than this 2×2 shortcut — the slide includes the 2×2 formula purely as a conceptual reminder of what "matrix inverse" means before jumping to the 3×3 case.

**Computing XᵀX (slides 13–14).**

XᵀX (a 3×3 matrix) works out to:

```
⎡  7    51    32   ⎤
⎢ 51   471   235   ⎥
⎣ 32   235  163.84 ⎦
```

**Computing (XᵀX)⁻¹ (slide 14):**

```
⎡ 1.79   −0.068  −0.253 ⎤
⎢−0.068   0.010  −0.001 ⎥
⎣−0.253  −0.001   0.057 ⎦
```

**Computing β = (XᵀX)⁻¹XᵀY (slide 15):**

**β₀ = 51.5697, β₁ = 1.49, β₂ = 6.72**

So the fitted regression equation is: **y = 51.5697 + 1.49×x1 + 6.72×x2** (the slide also writes a rounded version, 51.5 + 1.5×x1 + 6.7×x2, for quick mental use).

**The final prediction (slide 15).** For x1 = 5, x2 = 4:

y = 51.5 + 1.5×5 + 6.7×4 = 51.5 + 7.5 + 26.8 = **85.8**

**Independent verification.** I rebuilt the X and Y matrices exactly as given and recomputed everything from scratch using standard matrix algebra:

- **XᵀX** computed to **[[7, 51, 32], [51, 471, 235], [32, 235, 163.84]]** — matches the slide exactly.
- **(XᵀX)⁻¹** computed to **[[1.7996, −0.0685, −0.2532], [−0.0685, 0.0101, −0.0011], [−0.2532, −0.0011, 0.0571]]** — matches the slide's handwritten values to the precision shown.
- **β** computed to **[51.5697, 1.4974, 6.7233]** — matches the slide's β₀ = 51.5697 exactly, and β₁ ≈ 1.49, β₂ ≈ 6.72 match the slide's rounded values exactly.
- **Prediction at x1=5, x2=4** using the *full-precision* coefficients: y = 51.5697 + 1.4974×5 + 6.7233×4 = **85.95**. Using the slide's own *rounded* coefficients (51.5, 1.5, 6.7): y = **85.8**, exactly matching the slide's stated final answer. The small 0.15 gap between 85.8 and 85.95 is purely from the slide's intentional rounding of β for easy mental arithmetic — not an error.
- As a sanity check on the fit's quality: plugging all 7 original X1/X2 rows back through the fitted equation gives predictions within roughly ±1 to ±4 grams of the true Y values (residuals ranging from about −1.4 to +4.2), which is a reasonably tight fit for real (noisy) data — confirming this is a genuine, well-behaved least-squares solution, unlike the under-determined 5-row home-price example flagged in [[03_Multiple_Linear_Regression_Worked_Example_Home_Prices]] from Lecture 13 (that one had too few data points for its 4 unknowns; this one has a comfortable 7 data points for 3 unknowns).

**A practical note the slides don't mention.** Computing (XᵀX)⁻¹ directly, as done by hand here, works fine for a small number of features, but has two real-world limitations worth knowing: (1) it's computationally expensive for large numbers of features (inverting an n×n matrix generally costs on the order of n³ operations), and (2) it fails outright if XᵀX is *singular* (non-invertible) — which happens when two or more input features are perfectly or near-perfectly correlated with each other (multicollinearity). This is exactly the practical motivation behind **Ridge regression** (introduced in [[04_Types_of_Regression_Models_Overview]] from Lecture 13): adding the L2 penalty term also has the side effect of making XᵀX guaranteed to be invertible even when the raw data is collinear. For very large datasets, iterative methods like **gradient descent** are typically used instead of computing the matrix inverse directly.

---

## 2) Simple English Explanation

Now we actually solve the plant-dry-weight problem from the last topic. With two inputs (X1 and X2) instead of one, the neat little slope formula from Lecture 13 doesn't work anymore — we need a more powerful, general tool: **matrices**.

**Step 1 — arrange the data as two matrices.** Put all 7 "Y" values (dry weights) into one column, called **Y**. Then build a second table called **X**, where the first column is just a column of 1s (this trick represents the "+ constant" part of the formula), and the next two columns are the X1 and X2 values:

```
Y = [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7]  (one column, 7 rows)

X = [1, 7, 2.6]
    [1, 1, 2.9]
    [1, 11, 5.6]
    [1, 11, 3.1]     (three columns, 7 rows)
    [1, 7, 5.2]
    [1, 11, 5.5]
    [1, 3, 7.1]
```

**Step 2 — use the magic formula.** There's a single formula that directly spits out the best-fit coefficients for *any* number of inputs, called the **normal equation**:

**β = (XᵀX)⁻¹XᵀY**

Don't worry about deriving this — think of it as the "grown-up," any-number-of-inputs version of the slope formula from Lecture 13. (Xᵀ means "flip the X table on its side" — turn rows into columns. The little ⁻¹ means "matrix inverse," which is the matrix version of "1 divided by," since you can't literally divide by a table of numbers.)

**Step 3 — grind through the arithmetic.** This is genuinely a lot of number-crunching by hand (which is exactly why, in real life, you'd never do this manually — you'd use code). Multiplying Xᵀ by X gives a small 3×3 table of numbers; inverting that 3×3 table gives another 3×3 table of numbers; multiplying that by Xᵀ and then by Y finally gives the answer — the three coefficients we actually wanted:

**β₀ ≈ 51.57, β₁ ≈ 1.49, β₂ ≈ 6.72**

So the fitted formula is: **dry weight = 51.57 + 1.49 × (organic matter) + 6.72 × (nitrogen)**. I redid every single one of these matrix calculations independently from scratch, and got numbers matching the slide's handwriting almost exactly at every step — the 3×3 table, its inverse, and the final β values all check out.

**Step 4 — use it to predict.** Plug in organic matter = 5, nitrogen = 4:

dry weight = 51.5 + 1.5×5 + 6.7×4 = 51.5 + 7.5 + 26.8 = **85.8 grams**

(I got 85.95 using the un-rounded coefficients, and exactly 85.8 using the slide's rounded ones — same answer either way, just rounding.)

**One useful real-world thing the slides don't mention**: this "invert a matrix by hand" approach is fine for a tiny example like this one, but it gets painfully slow (and sometimes literally impossible, if some of your input columns are too similar to each other) once you have lots of features or lots of data. This is exactly why real ML tools either use smarter numerical tricks, or use a completely different approach called **gradient descent** which gradually nudges the coefficients toward the best answer step by step, instead of computing the exact matrix inverse in one shot.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab hum actually solve karte hain plant-dry-weight wala problem jo pichle topic mein set up kiya tha. Do inputs (X1 aur X2) hone ki wajah se, Lecture 13 wala simple slope formula kaam nahi karega — ek zyada powerful, general tool chahiye: **matrices**.

**Step 1 — data ko do matrices mein arrange karo.** Saari 7 "Y" values (dry weights) ko ek column mein daalo, naam **Y**. Phir ek doosra table banao **X**, jisme pehla column sirf 1s ka hai (yeh trick formula ke "+ constant" part ko represent karta hai), aur agle do columns X1 aur X2 ki values hain:

```
Y = [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7]  (ek column, 7 rows)

X = [1, 7, 2.6]
    [1, 1, 2.9]
    [1, 11, 5.6]
    [1, 11, 3.1]     (teen columns, 7 rows)
    [1, 7, 5.2]
    [1, 11, 5.5]
    [1, 3, 7.1]
```

**Step 2 — magic formula use karo.** Ek hi formula hai jo directly best-fit coefficients de deta hai *kitne bhi* inputs ke liye, jise **normal equation** bolte hain:

**β = (XᵀX)⁻¹XᵀY**

Isko derive karne ki tension mat lo — isse Lecture 13 wale slope formula ka "bada, kitne bhi inputs handle karne wala" version samjho. (Xᵀ ka matlab hai "X table ko side pe flip karo" — rows ko columns bana do. Chhota ⁻¹ ka matlab "matrix inverse" hai, jo "1 se divide karna" ka matrix version hai, kyunki numbers ke table se seedha divide nahi kar sakte.)

**Step 3 — arithmetic grind karo.** Yeh genuinely bahut zyada number-crunching hai hath se (isiliye real life mein kabhi manually nahi karte — code use karte hain). Xᵀ ko X se multiply karne pe ek chhota 3×3 table milta hai; us 3×3 table ko invert karne se ek aur 3×3 table milta hai; usko Xᵀ se aur phir Y se multiply karne pe finally answer milta hai — teen coefficients jo humein chahiye the:

**β₀ ≈ 51.57, β₁ ≈ 1.49, β₂ ≈ 6.72**

Toh fitted formula yeh hai: **dry weight = 51.57 + 1.49 × (organic matter) + 6.72 × (nitrogen)**. Maine yeh har ek matrix calculation khud independently redo ki scratch se, aur almost har step pe slide ki handwriting se matching numbers mile — 3×3 table, uska inverse, aur final β values, sab check out ho gaye.

**Step 4 — predict karne ke liye use karo.** Organic matter = 5, nitrogen = 4 daalo:

dry weight = 51.5 + 1.5×5 + 6.7×4 = 51.5 + 7.5 + 26.8 = **85.8 grams**

(Maine 85.95 paaya un-rounded coefficients se, aur bilkul 85.8 slide ke rounded coefficients se — dono se jawab same hai, bas rounding ka farak hai.)

**Ek useful real-world baat jo slides nahi batati**: yeh "matrix ko hath se invert karo" approach chhote example ke liye theek hai, lekin bahut slow ho jaata hai (aur kabhi-kabhi literally impossible, agar kuch input columns ek dusre se bahut similar hon) jab bahut saare features ya bahut zyada data ho. Isiliye real ML tools ya toh smarter numerical tricks use karte hain, ya ek bilkul alag approach use karte hain jise **gradient descent** bolte hain, jo coefficients ko step-by-step best answer ki taraf dheere-dheere push karta hai, exact matrix inverse ek hi shot mein nikalne ke bajaye.
