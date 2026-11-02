# Topic 4: Types of Regression Models

Source: Lecture 13, slides 18–19 ("Types of Regression Models", "Regression Models"). Enriched with web research (L1/L2 regularization, sigmoid/log-odds, bias-variance tradeoff for polynomial degree).

---

## 1) Technical Explanation

The slides list five types of regression models, each with a one-line definition and (where applicable) its formula. The handwritten annotation on slide 19 also notes that Ridge uses **L2** regularization and Lasso uses **L1** regularization.

**1. Simple Linear Regression** — uses **one** independent input variable to predict a single continuous output using a straight-line formula: **y = a + bx**. This is exactly what was worked through in [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]] (there written as price = m×area + b — same equation, different letter names for slope/intercept).

**2. Multiple Linear Regression** — uses **two or more** independent input variables to predict a single continuous output y: **y = a₀ + a₁x₁ + a₂x₂ + … + aₙxₙ**. Covered in [[03_Multiple_Linear_Regression_Worked_Example_Home_Prices]].

**3. Polynomial Regression** — fits a non-linear, *curved* relationship by using higher-order exponents (powers) of the input variable(s): **y = a₀ + a₁x + a₂x² + … + aₙxⁿ**, for some positive integer n > 1. It's still technically "linear regression" in the statistical sense (the model is linear in its *coefficients* a₀…aₙ, even though the resulting curve is not a straight line) — it just uses x², x³, etc. as additional engineered features alongside x. A real risk with polynomial regression that the slide doesn't mention: choosing too high a degree n lets the curve bend enough to pass almost exactly through every training point, which looks like a perfect fit on paper but actually **overfits** — it captures noise in the training data rather than the true underlying trend, and performs badly on new, unseen data. This is the classic **bias–variance tradeoff**: low-degree polynomials risk *underfitting* (too rigid, high bias), very high-degree polynomials risk *overfitting* (too flexible, high variance); the right degree is the one where error on held-out/test data is lowest, not where error on the training data is lowest. (Source: [Bias-Variance Trade-off and Polynomial Regression — Medium](https://medium.com/@senihberkay/bias-variance-trade-off-overfitting-underfitting-polynomial-regression-46d5fa53c4bf).)

**4. Logistic Regression** — used when the dependent variable is **binary** (0/1, True/False, Yes/No), despite the name containing "regression." The slide gives only the one-line definition; the mechanism (not covered on the slide, filled in via research) is: instead of directly predicting 0 or 1, logistic regression first computes a normal linear combination like ordinary regression (m₁x₁+m₂x₂+…+b), then passes that number through the **sigmoid function** σ(z) = 1/(1+e⁻ᶻ), which squashes any real number into a probability strictly between 0 and 1. Equivalently, logistic regression fits a straight line not to the raw probability but to the **log-odds** (also called the *logit*) of the outcome — log(p/(1−p)) — which *is* a linear function of the inputs, even though the resulting probability curve (after applying sigmoid) is S-shaped, not straight. A threshold (commonly 0.5) is then applied to the predicted probability to make the final Yes/No call. (Source: [Understanding Logistic Regression — Towards Data Science](https://towardsdatascience.com/understanding-logistic-regression-the-odds-ratio-sigmoid-mle-et-al-740cebf349a3/); [GeeksforGeeks — Logistic Regression](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/).)

**5. Ridge and Lasso Regression** — apply mathematical penalties to simpler linear models to **prevent overfitting** and **manage correlated inputs** (multicollinearity). Both work by adding a penalty term to the least-squares error being minimized, so the model is discouraged from assigning very large coefficients to any one feature:
- **Ridge regression** uses **L2 regularization**: the penalty added is the *sum of the squares* of the coefficients (λΣmᵢ²). This shrinks coefficients toward zero but essentially never makes them exactly zero — every feature stays in the model, just with a dampened influence. Useful when you believe most/all features genuinely matter somewhat.
- **Lasso regression** uses **L1 regularization**: the penalty added is the *sum of the absolute values* of the coefficients (λΣ|mᵢ|). This can shrink some coefficients **all the way to exactly zero**, effectively removing those features from the model entirely — so Lasso doubles as an automatic feature-selection method, which connects back to the feature-selection material in [[01_Feature_Selection_Process_and_Approaches]] from Lecture 11 and 12 (combined session). Useful when you suspect only a handful of your features actually matter and want the model to discover which ones.
- In both, λ (lambda) is a tunable "how much to penalize" knob: λ=0 recovers ordinary linear regression exactly; larger λ shrinks coefficients more aggressively.
(Source: [Ridge Regression vs Lasso Regression — GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/ridge-regression-vs-lasso-regression/); [L1 and L2 Regularization Methods, Explained — Built In](https://builtin.com/data-science/l2-regularization).)

---

## 2) Simple English Explanation

This is just a "menu" of the five main flavours of regression, going from simplest to most advanced:

**1. Simple Linear Regression** — one input, one output, one straight line. "Bigger house area → bigger price" using just a single straight-line formula. Already fully worked through in [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]].

**2. Multiple Linear Regression** — same idea, but with several inputs at once (area AND bedrooms AND age, all contributing to price). Worked through in [[03_Multiple_Linear_Regression_Worked_Example_Home_Prices]].

**3. Polynomial Regression** — for when a straight line just doesn't fit the data shape well, and you need a *curve* instead. You do this by adding "x squared," "x cubed," etc. as extra inputs, which lets the line bend. The catch: if you let it bend *too* much (too high a power), the curve will wiggle around and pass through every single training point perfectly — but that's actually a bad sign, not a good one! It means the model has basically memorized the exact training examples instead of learning the real underlying trend, and it will do a poor job predicting brand new data it hasn't seen. This is called **overfitting**, and picking the right amount of "bendiness" is one of the core skills in ML.

**4. Logistic Regression** — despite having "regression" in the name, this one is actually used for **yes/no-type predictions** (e.g., "will this customer buy the product? yes/no", "is this email spam? yes/no") — not for predicting a number like price. It works by computing a regular regression-style score internally, then squishing that score through a special S-shaped curve (called the **sigmoid function**) that always outputs a number between 0 and 1 — you can read that number as "probability of yes." If the probability is above 0.5, you call it "yes"; otherwise "no."

**5. Ridge and Lasso Regression** — these are "safety net" versions of regular regression, used when you're worried your model is overfitting or when some of your input features are too similar to each other (like both "area in sqft" and "area in sq meters" — basically the same information twice). Both add a small penalty that discourages any one feature's weight/coefficient from growing too huge:
- **Ridge** gently shrinks all coefficients toward (but not to) zero.
- **Lasso** can shrink some coefficients all the way to exactly zero — meaning it can automatically decide "this feature doesn't matter, throw it out entirely," which is genuinely useful when you have lots of features and aren't sure which ones actually help.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yeh basically regression ke 5 main "flavours" ka menu hai, simple se advanced tak:

**1. Simple Linear Regression** — ek input, ek output, ek straight line. "Bada ghar area → zyada price" — sirf ek straight-line formula use karke. Yeh pura worked out hai [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]] mein.

**2. Multiple Linear Regression** — same idea, lekin ek saath kai inputs ke saath (area AUR bedrooms AUR age, sab milke price decide karte hain). [[03_Multiple_Linear_Regression_Worked_Example_Home_Prices]] mein worked out hai.

**3. Polynomial Regression** — jab straight line data ke shape mein fit nahi baithti, tab curve chahiye hota hai. Yeh karte hain "x ka square," "x ka cube," waghera ko extra inputs ki tarah add karke, jisse line mud sakti hai. Catch yeh hai: agar isse zyada hi mudne do (bahut high power), toh curve itna zyada wiggle karega ki har ek training point ko perfectly touch kar lega — lekin yeh actually acha sign nahi hai, bura hai! Iska matlab model ne training examples ko yaad kar liya hai (memorize), real pattern seekha nahi. Isse naye, na-dekhe data pe prediction kharab hoga. Isko **overfitting** bolte hain, aur sahi amount ki "bendiness" choose karna ML ki core skills mein se ek hai.

**4. Logistic Regression** — naam mein "regression" hone ke bawajood, yeh actually **haan/na type predictions** ke liye use hota hai (jaise "kya yeh customer product kharidega? haan/na", "kya yeh email spam hai? haan/na") — number predict karne ke liye nahi (jaise price). Yeh andar ek normal regression-style score nikalta hai, phir usko ek special S-shape curve (**sigmoid function**) se squeeze karta hai jo hamesha 0 aur 1 ke beech ka number deta hai — usko "probability of yes" samajh sakte ho. Agar probability 0.5 se zyada hai, toh "yes" bolte hain; warna "no."

**5. Ridge aur Lasso Regression** — yeh normal regression ke "safety net" versions hain, jab aapko lagta hai model overfit ho raha hai, ya kuch input features ek dusre se bahut similar hain (jaise "area in sqft" aur "area in sq meters" — basically wahi info do baar). Dono ek chhota penalty add karte hain jo kisi bhi ek feature ke weight/coefficient ko bahut bada hone se rokta hai:
- **Ridge** sabhi coefficients ko dheere se zero ki taraf shrink karta hai (par bilkul zero nahi karta).
- **Lasso** kuch coefficients ko bilkul zero tak shrink kar sakta hai — matlab yeh khud decide kar sakta hai "yeh feature matter nahi karta, ise poori tarah hata do," jo genuinely useful hai jab aapke paas bahut saare features hon aur pata na ho konse actually kaam ke hain.
