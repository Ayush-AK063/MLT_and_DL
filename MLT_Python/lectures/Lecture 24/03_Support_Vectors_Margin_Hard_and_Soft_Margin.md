# Topic 3: Support Vectors, Margin, Hard and Soft Margin

Source: Lecture 24, slides 5–8 (definitions of Support Vectors, Margin, Hard Margin, Soft Margin, Kernel Function and Types of Kernels; hand-drawn sketches with "Class 1", "Class 2", "Margin", "Hyperplane", distances "d" on both sides, "* Maximize the Margin" and circled "support vectors"; figure from towardsdatascience.com showing "Support Vectors (Class 1/2)", "Hyperplane", "Margin"). Enriched with the standard maximum-margin formulation (Boser–Guyon–Vapnik 1992; Cortes–Vapnik 1995) and our own scikit-learn verification of a small example.

---

## 1) Technical Explanation

### Slide 5 definitions (quoted)

- **Support Vectors**: "the data points that are closest to the hyperplane. These points influence the orientation and position of the hyperplane."
- **Margin**: "the distance between the hyperplane and the nearest data point of either class. SVM tries to **maximize this margin** to improve classification confidence."
- **Hard Margin**: "assumes data is perfectly separable by the hyperplane. All data points must lie outside the margin."
- **Soft Margin**: "allows some misclassification or margin violations for non-linearly separable data."
- **Kernel Function**: "transforms data into a higher-dimensional space to make it linearly separable."
  - Types of kernels: **Linear** (linearly separable data), **Polynomial** (curved boundaries), **RBF** (complex relationships).
  - Kernels are covered in [[06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick]].

### Slides 6–8: the pictures

- **Slide 6** (hand-drawn). "+" points form **Class 1** and "−" points form **Class 2**.
  - A red **Hyperplane** sits between them, with two dashed blue **Margin** lines parallel to it, one on each side.
  - Arrows marked **d** show that the gap is the same distance d on both sides.
  - The note reads "**\* Maximize the Margin**".
- **Slide 7.** Same sketch, with the "+" and the "−" that touch the margin lines circled and labelled "**support vectors**".
- **Slide 8** (towardsdatascience figure). Blue squares are Class 1 and red circles are Class 2.
  - A solid **hyperplane** has two dashed margin lines.
  - The points lying on the dashed lines are labelled **Support Vectors (Class 1)** and **Support Vectors (Class 2)**.
  - The double arrow between the dashed lines is labelled **Margin**.

### The maths behind "maximise the margin" (hard margin)

Training data: (x_i, y_i) with labels y_i ∈ {+1, −1}.

1. **Canonical scaling.** Scale w and b so that the closest points satisfy |w·x + b| = 1. Then every training point obeys

   **y_i (w·x_i + b) ≥ 1.**

   The two margin lines are w·x + b = +1 and w·x + b = −1. The support vectors are the points that lie exactly on them.
2. **Margin width.**
   - The distance from the hyperplane to either margin line is d = 1/‖w‖ (from distance = |w·x + b|/‖w‖, [[02_What_Is_an_SVM_Hyperplane_w_x_plus_b]]).
   - The full gap between the dashed lines is **2/‖w‖**.
   - Slide 5 defines the margin as the hyperplane-to-nearest-point distance (= d). Many books call the full width 2d the margin. Either way, maximising one maximises the other.
3. **Optimisation problem (primal):**

   **minimise ½‖w‖²  subject to  y_i (w·x_i + b) ≥ 1 for all i.**

   Maximising 2/‖w‖ is the same as minimising ‖w‖ (or ½‖w‖², which is easier to differentiate). This is a **convex quadratic program**, so it has a unique global optimum. That is an advantage over the perceptron, which stops at *any* separating line.
4. **Why "support vectors"?** In the solution, w = Σ α_i y_i x_i, where the Lagrange multiplier α_i is **non-zero only for the support vectors**. Points far from the boundary have α_i = 0. You could delete them and the hyperplane would not move. This is what slide 5 means by "these points influence the orientation and position of the hyperplane".

### Worked example (our own; verified with scikit-learn `SVC(kernel='linear', C=10⁶)`)

- Class +1: (3, 1), (3, −1), (6, 1), (6, −1).
- Class −1: (1, 0), (0, 1), (0, −1), (−1, 0).

**By hand.**
- The closest opposing points are (1, 0) on the −1 side and (3, ±1) on the +1 side.
- The widest gap is the vertical line halfway between x₁ = 1 and x₁ = 3, i.e. **x₁ = 2**.
- Canonical form: w = (1, 0), b = −2. Check:
  - (3, ±1): 3 − 2 = **+1** ✔
  - (1, 0): 1 − 2 = **−1** ✔
- Every other point gives a value of at least +1 or at most −1. For example (6, 1) → +4 and (−1, 0) → −3.
- ‖w‖ = 1, so the full margin = 2/1 = **2** (from x₁ = 1 to x₁ = 3).

**scikit-learn result.**
- w = (1.000, 0), b = −2.001.
- Support vectors: (1, 0), (3, 1), (3, −1). Margin 1.999.
- Dual coefficients α_i y_i = −0.5, +0.25, +0.25. Check:
  - w = −0.5·(1,0) + 0.25·(3,1) + 0.25·(3,−1) = (−0.5 + 1.5, 0) = (1, 0) ✔
  - Σ α_i y_i = 0 ✔
- The other 5 points have α = 0. Moving (6, 1) to (10, 5) would not change the answer.

### Hard vs soft margin, in symbols

The hard margin needs **every** point to satisfy y_i(w·x_i + b) ≥ 1. If the classes overlap, or a single outlier crosses over, no solution exists. The **soft margin** (Cortes & Vapnik 1995) adds a slack ξ_i ≥ 0 per point:

  **minimise ½‖w‖² + C Σ ξ_i  subject to  y_i (w·x_i + b) ≥ 1 − ξ_i, ξ_i ≥ 0.**

- ξ_i = 0: the point is outside the margin, on the correct side.
- 0 < ξ_i ≤ 1: the point is inside the margin but still correctly classified (a "margin violation").
- ξ_i > 1: the point is misclassified.
- **C** sets how expensive violations are. The full treatment, with a numeric demo, is in [[04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin]] and [[05_Gamma_and_Regularization_C]].

---

## 2) Simple English Explanation

**Support vectors.** Picture two teams standing on either side of a road. The players standing **right at the edge of the road** are the support vectors. They are the "front line". They alone decide where the road can run. Players far back don't matter: if they walked away, the road would stay exactly where it is. That's why the method is named after them.

**Margin.** The margin is how much **empty space** there is between the dividing line and the nearest players. The teacher's sketch shows the line, two dashed lines parallel to it, and the same distance **d** on both sides. Then it says "**Maximize the Margin**". A wide empty road means a new person arriving can be classified confidently. A narrow road means small mistakes flip the answer.

**Why the widest road is best.** Many lines can separate two groups, but a line that almost touches one group is risky: a slightly different new point could land on the wrong side. The line in the **middle of the widest possible road** leaves the most room for error on both sides.

**Hard margin vs soft margin.**
- **Hard margin:** "Nobody is allowed on the road, and nobody may be on the wrong side." This works only if the two groups are perfectly separable. A single stray point makes it impossible.
- **Soft margin:** "A few people may stand on the road or even on the wrong side, but each one costs a penalty." This is what real data needs, because real data is messy. How big the penalty is gets controlled by a setting called **C**, covered in Topic 5.

**A small example we checked with Python.**
- Plus points: (3, 1), (3, −1), (6, 1), (6, −1). Minus points: (1, 0), (0, 1), (0, −1), (−1, 0).
- The nearest minus point is at x = 1 and the nearest plus points are at x = 3. So the widest road runs from x = 1 to x = 3, and the dividing line is down its middle at **x = 2**.
- The road is **2 units wide**.
- The support vectors are (1, 0), (3, 1) and (3, −1), the three points touching the road's edges.
- Python's SVM found exactly this. It also confirmed that the other five points have zero influence on the answer.

**The maths in one breath.**
- SVM scales the line's formula so that the edge points score exactly +1 or −1. The road's width then works out to **2/‖w‖**.
- So "make the road as wide as possible" becomes "make ‖w‖ as small as possible, while every point scores at least +1 on its own side".
- This kind of problem has exactly one best answer, so the training never gets stuck.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Support vectors.** Socho do teams ek sadak ke dono taraf khadi hain. Jo players **sadak ke bilkul kinare** khade hain, wahi support vectors hain, yaani "front line". Sirf wahi decide karte hain ki sadak kahan se guzregi. Peeche khade players ka koi role nahi. Woh chale bhi jaayein to sadak wahin rahegi. Isiliye method ka naam inhi pe hai. Slide 7 pe teacher ne kinare wale "+" aur "−" ko circle karke likha "support vectors". Slide 8 ki figure mein bhi dashed lines pe pade points "Support Vectors (Class 1/2)" hain.

**Margin.** Dividing line aur sabse paas wale points ke beech ki **khaali jagah**. Slide 6 ke sketch mein beech mein hyperplane hai, dono taraf dashed margin lines hain, aur dono taraf same doori **d** hai. Upar likha hai "**Maximize the Margin**". Sadak chaudi hai to naya point aane pe confident jawaab milta hai. Sadak patli hai to chhoti si galti se jawaab palat jata hai.

**Sabse chaudi sadak hi kyun?** Do groups ko alag karne wali bahut lines ho sakti hain. Par jo line ek group ko lagbhag chhoo rahi ho, woh risky hai, kyunki thoda alag naya point galat taraf gir sakta hai. **Sabse chaudi sadak ke beech** wali line dono taraf sabse zyada galti ki jagah chhodti hai.

**Hard margin vs soft margin.**
- **Hard margin:** "Sadak pe koi nahi khada hoga aur koi galat taraf nahi hoga." Ye tabhi chalega jab data perfectly separable ho. Ek bhi bhatka hua point ho to solution hi nahi milega.
- **Soft margin:** "Kuch log sadak pe ya galat taraf bhi khade ho sakte hain, par har ek pe penalty lagegi." Real data hamesha thoda gandha hota hai, isliye yahi practical hai. Penalty kitni badi ho, ye **C** decide karta hai (Topic 5).
  - Formula: minimise ½‖w‖² + C Σξ_i, jahan ξ_i (slack) batata hai ki point kitna rule tod raha hai.
  - ξ = 0: sahi taraf, margin ke bahar.
  - 0 < ξ ≤ 1: margin ke andar, par sahi taraf.
  - ξ > 1: galat taraf (misclassified).

**Maths, aasaan bhasha mein.**
1. SVM line ke formula ko aise scale karta hai ki kinare wale points ka score exactly +1 ya −1 aaye. Rule: har point ke liye y_i(w·x_i + b) ≥ 1.
2. Tab hyperplane se har margin line ki doori = 1/‖w‖, aur poori sadak ki chaudai = **2/‖w‖**.
3. "Sadak chaudi karo" ka matlab ho gaya "‖w‖ chhota karo": **minimise ½‖w‖²**, is shart ke saath ki har point apni side pe score ≥ 1 de.
4. Ye convex problem hai, yaani sirf ek best answer hai aur training kahin atakti nahi (perceptron jaisa nahi, jo koi bhi line pakad leta hai).
5. Answer mein w = Σ α_i y_i x_i aata hai, aur α_i sirf support vectors ke liye non-zero hota hai. Baaki sab ka α = 0.

**Example jo humne Python se check kiya.**
- Plus points: (3,1), (3,−1), (6,1), (6,−1). Minus points: (1,0), (0,1), (0,−1), (−1,0).
- Sabse paas wala minus point x = 1 pe hai aur sabse paas wale plus points x = 3 pe. To sabse chaudi sadak x = 1 se x = 3 tak hai, aur line beech mein **x = 2** pe.
- Formula: w = (1, 0), b = −2.
  - Check: (3, ±1) → 3 − 2 = **+1** ✔, (1, 0) → 1 − 2 = **−1** ✔.
  - (6,1) → +4 aur (−1,0) → −3, dono margin ke bahar.
- Sadak ki chaudai = 2/‖w‖ = 2/1 = **2**.
- Support vectors: (1,0), (3,1), (3,−1).
- scikit-learn ne bhi bilkul yahi diya: w = (1, 0), b ≈ −2, α·y = −0.5, +0.25, +0.25.
  - Check: −0.5×(1,0) + 0.25×(3,1) + 0.25×(3,−1) = (1, 0) ✔.
  - Baaki 5 points ka α = 0. Unhe hata do ya door khiskao, answer nahi badlega.
