# Topic 4: The scikit-learn SVM Page, and Code That Checks Both Exercises

Source: Lecture 25, slide 8 (screenshot of the scikit-learn User Guide, "1.4. Support Vector Machines", version 1.9.0 stable, showing the definition, the advantages list and the start of "The disadvantages of support vector machines include:"). Enriched with the rest of that documentation page (disadvantages, complexity, practical tips) and our own code run (scikit-learn 1.9.1).

---

## 1) Technical Explanation

### What slide 8 shows

**Definition (as on the page):** "Support vector machines (SVMs) are a set of supervised learning methods used for **classification**, **regression** and **outliers detection**."

- Classification is `SVC`, `NuSVC` and `LinearSVC`.
- Regression is `SVR`.
- Outlier/novelty detection is `OneClassSVM`.

**Advantages (as on the page):**
1. Effective in **high dimensional spaces**.
2. Still effective in cases where the **number of dimensions is greater than the number of samples**.
3. Uses a subset of training points in the decision function (called **support vectors**), so it is also **memory efficient**.
4. **Versatile**: different kernel functions can be specified for the decision function. Common kernels are provided, and custom kernels are possible too.

These are the same points as Lecture 24's "Advantages" slide ([[07_Advantages_Disadvantages_and_Applications]] from Lecture 24).

**Disadvantages** (the slide cuts off at the heading; the documentation continues):
- If the number of features is much greater than the number of samples, avoiding over-fitting by choosing the kernel and the regularization term (C) is crucial.
- SVMs do not directly provide probability estimates. scikit-learn computes them with an expensive internal five-fold cross-validation (`probability=True`).

**Sections listed in the page's sidebar:** 1.4.1 Classification, 1.4.2 Regression, 1.4.3 Density estimation / novelty detection, 1.4.4 Complexity, 1.4.5 Tips on Practical Use, 1.4.6 Kernel functions, 1.4.7 Mathematical formulation, 1.4.8 Implementation details.

- *Complexity*: kernel-SVM training time grows roughly between O(n_features·n²) and O(n_features·n³) in the number of samples n.
- *Tips*: scale the data (e.g. to [0, 1] or with standardisation), tune C (and γ) by cross-validation, and consider `class_weight` for imbalanced data.

### Code that reproduces both exercises

```python
import numpy as np
from sklearn.svm import SVC

# Exercise 1 (labels assumed: left cluster = -1, right cluster = +1)
neg = [(1,.5),(1,1),(1,-.5),(-.5,.5),(.5,.5),(2,0)]
pos = [(4,0),(4.5,1),(4.5,.5),(5,-1),(5.5,0)]
X1 = np.array(neg + pos); y1 = np.r_[-np.ones(6), np.ones(5)]
svm1 = SVC(kernel="linear", C=1e6).fit(X1, y1)       # huge C ≈ hard margin
print(svm1.coef_, svm1.intercept_)    # [[1. 0.]] [-3.]   -> x1 = 3
print(svm1.support_vectors_)          # [[2. 0.] [4. 0.]]
print(svm1.dual_coef_)                # [[-0.5  0.5]]      (alpha_i * y_i)
print(2 / np.linalg.norm(svm1.coef_)) # 2.0                -> margin

# Exercise 2
X2 = np.array([[3,1],[3,-1],[6,1],[6,-1],[1,0],[0,1],[0,-1],[-1,0]])
y2 = np.array([1,1,1,1,-1,-1,-1,-1])
svm2 = SVC(kernel="linear", C=1e6).fit(X2, y2)
print(svm2.coef_, svm2.intercept_)    # ≈ [[1. 0.]] ≈ [-2.] -> x1 = 2
print(svm2.support_vectors_)          # [[1. 0.] [3. 1.] [3. -1.]]
```

These outputs come from our run.

- **Exercise 1:** w = (1, 0), b = −3, support vectors (2, 0) and (4, 0), margin 2. This matches slides 5–6 ([[02_Exercise_1_Full_Solution_Alphas_and_Hyperplane_x1_equals_3]]).
- **Exercise 2:** w ≈ (1, 0), b ≈ −2, support vectors (1, 0), (3, ±1). This matches slide 7 ([[03_Exercise_2_Three_Support_Vectors_Hyperplane_x1_equals_2]]).

**Notes on reading the output.**
- `coef_` (w) is available only for `kernel="linear"`.
- `dual_coef_` stores **αᵢ·yᵢ** for the support vectors, using the *true* Lagrange multipliers. These are 0.5 and 0.5 in Exercise 1, not the shortcut's −6.5 and 3.5 ([[06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method]]).
- `SVC` has no separate "hard margin" switch. A very large C (here 10⁶) makes slack so expensive that the solution equals the hard-margin one when the data is separable.

**Checking the shortcut's linear systems with numpy:**

```python
S = np.array([[2,0,1],[4,0,1]])          # augmented support vectors (Exercise 1)
G = S @ S.T                              # [[5, 9], [9, 17]]
alpha = np.linalg.solve(G, [-1, 1])      # [-6.5, 3.5]
print(alpha @ S)                         # [ 1.  0. -3.]  = (w1, w2, b)
```

Running the same code for Exercise 2 (S = [[1,0,1],[3,1,1],[3,−1,1]], y = [−1, 1, 1]) gives G = [[2,4,4],[4,11,9],[4,9,11]], α = [−3.5, 0.75, 0.75] and w̃ = (1, 0, −2) ✔.

---

## 2) Simple English Explanation

**Slide 8 is a screenshot of the official scikit-learn help page** for SVMs. scikit-learn is the Python library we've used throughout the course.

**What the page says:**
- SVMs can do three jobs:
  - **classification**: put things into groups;
  - **regression**: predict a number;
  - **outlier detection**: spot unusual points.
- **Good points:**
  1. They work well when each example has **lots of features**.
  2. They still work even when there are **more features than examples**.
  3. They only need to remember the **support vectors**, so they're **memory efficient**.
  4. They're **flexible**: you can choose different kernels (straight, curved, RBF) or even write your own.
- **Weak points** (the slide cuts off here, so we read the rest of the page):
  - With far more features than examples you must pick the kernel and C carefully, or the model will overfit.
  - SVMs don't naturally give "how sure am I" probabilities. Python can compute them, but it's slow.
- **Practical tip from the page:** always **scale** your data first, and tune C and gamma with cross-validation.

**Letting the computer check our homework.**
- We typed both exercises into Python.
- **Exercise 1:** Python found the line **x₁ = 3**, support vectors **(2, 0) and (4, 0)**, and a road **2 units wide**. That is exactly the slide's answer.
- **Exercise 2:** Python found **x₁ = 2** with support vectors **(1, 0), (3, 1), (3, −1)**. Again it matches.
- We also let numpy solve the teacher's small equation systems directly. It returned α = −6.5 and 3.5 (Exercise 1) and α = −3.5, 0.75, 0.75 (Exercise 2), exactly as on the slides.
- **One thing that may confuse you:** Python's own "α" values are different (0.5 and 0.5 for Exercise 1). They are the official SVM α values, while the classroom shortcut produces different helper numbers. Both lead to the same line. Topic 6 explains why.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 8 scikit-learn ke official help page (User Guide 1.4, version 1.9.0) ka screenshot hai.** scikit-learn wahi Python library hai jo hum poore course mein use kar rahe hain.

**Page kya kehta hai:**
- SVM teen kaam karta hai:
  - **classification** (`SVC`);
  - **regression**, yaani number predict karna (`SVR`);
  - **outlier detection**, yaani ajeeb points pakadna (`OneClassSVM`).
- **Fayde:**
  1. **Bahut features** wale data pe achha.
  2. **Features, samples se zyada** hon tab bhi chalta hai.
  3. Sirf **support vectors** yaad rakhta hai, isliye **memory efficient**.
  4. **Versatile**: alag-alag kernels (linear, poly, RBF) ya apna custom kernel bhi de sakte ho.
  - Ye wahi points hain jo Lecture 24 ke "Advantages" slide pe the.
- **Nuksaan** (slide pe heading ke baad kat gaya, humne page se padha):
  - Features bahut zyada aur samples kam hon to kernel aur C dhyan se chunne padte hain, warna overfitting hogi.
  - Probability seedhe nahi deta. `probability=True` se milti hai, par andar 5-fold cross-validation chalta hai, isliye slow.
- **Tips:** data ko **scale** karo, aur C/γ cross-validation se tune karo.
- **Complexity:** training time samples ke saath n² se n³ ke beech badhta hai.

**Computer se homework check karwaya.**
- **Exercise 1** (left = −1, right = +1 maan ke): `SVC(kernel="linear", C=1e6)`.
  - w = (1, 0), b = −3, yaani **x₁ = 3**.
  - Support vectors **(2, 0), (4, 0)**, margin **2**. Slide se bilkul match ✔.
- **Exercise 2:** w ≈ (1, 0), b ≈ −2, yaani **x₁ = 2**. Support vectors (1, 0), (3, ±1) ✔.
- C = 10⁶ kyun? SVC mein alag "hard margin" button nahi hai. Bahut bada C galti ko itna mehnga bana deta hai ki answer hard margin jaisa hi aata hai.
- numpy se teacher ke equation systems bhi solve karwaye:
  - Ex 1: Gram matrix [[5, 9], [9, 17]], α = [−6.5, 3.5], w̃ = (1, 0, −3) ✔.
  - Ex 2: Gram [[2, 4, 4], [4, 11, 9], [4, 9, 11]], α = [−3.5, 0.75, 0.75], w̃ = (1, 0, −2) ✔.
- **Confuse mat hona:** scikit-learn ke `dual_coef_` mein **asli** α·y hota hai. Ex 1 mein woh −0.5 aur +0.5 hai, yaani asli α = 0.5 dono. Slide ke −6.5, 3.5 shortcut ke helper numbers hain. Dono se line same aati hai, kyun? Topic 6 mein.
