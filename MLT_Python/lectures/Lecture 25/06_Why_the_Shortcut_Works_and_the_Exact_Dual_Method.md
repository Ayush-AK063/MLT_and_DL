# Topic 6: Why the Classroom Shortcut Works Here, When It Fails, and the Exact Method

Source: Research enrichment, not on the slides. It analyses the six-step "augmented vector" method of slides 1–7 ([[01_Exercise_1_Problem_and_the_Six_Step_Method]]). Based on the standard SVM dual formulation (Boser–Guyon–Vapnik 1992; Cortes–Vapnik 1995; see Lecture 24) and our own numpy / scikit-learn checks. All numbers were computed by us.

---

## 1) Technical Explanation

### What the shortcut really computes

The shortcut takes the chosen support vectors sᵢ with labels yᵢ ∈ {−1, +1}, augments them to s̃ᵢ = (sᵢ, 1), sets w̃ = Σ αᵢ s̃ᵢ, and solves

  Σⱼ αⱼ (s̃ⱼ · s̃ᵢ) = yᵢ  for every chosen support vector.

These equations say w̃·s̃ᵢ = yᵢ, i.e. **w·sᵢ + b = yᵢ**. That is the correct condition for a support vector: it lies on its margin line.

There is a catch. Forcing w̃ to be a combination of the s̃ᵢ picks, among all (w, b) that satisfy those equations, the one with the **smallest ‖w‖² + b²**. This is the minimum-norm solution of a linear system.

The real hard-margin SVM ([[03_Support_Vectors_Margin_Hard_and_Soft_Margin]] from Lecture 24) minimises **‖w‖² only**, and leaves b free:

  **True SVM:** minimise ½‖w‖² s.t. yᵢ(w·xᵢ + b) ≥ 1 for **all** points, with b unpenalised.

So the two methods agree only when penalising b doesn't change the answer.

### Why it gives the right answer in both exercises

- **Exercise 2** has three support vectors in 2-D, which gives three equations in three unknowns (w₁, w₂, b):
  - (1, 0): w₁ + b = −1
  - (3, 1): 3w₁ + w₂ + b = 1
  - (3, −1): 3w₁ − w₂ + b = 1
  
  These **fully determine** w = (1, 0), b = −2. There is no freedom left for the norm to choose, so any method that satisfies the equations gives the same line.
- **Exercise 1** has two support vectors, (2, 0) and (4, 0), which gives two equations, 2w₁ + b = −1 and 4w₁ + b = 1.
  - These fix w₁ = 1 and b = −3, and leave w₂ free.
  - Both methods minimise w₂² and set w₂ = 0.
  - Because both support vectors lie on the line x₂ = 0, the free part does not involve b, so the answers coincide.

### A case where it fails

Take **one support vector per class, not level with each other horizontally**: x₋ = (0, 1) in class −1 and x₊ = (2, 1) in class +1.

- **True SVM:** the perpendicular bisector of the segment between them, **x₁ = 1**. So w = (1, 0), b = −1, margin = 2. scikit-learn confirms w = (1, 0), b = −1.
- **Shortcut:**
  - Augmented vectors (0, 1, 1) and (2, 1, 1). Gram matrix [[2, 2], [2, 6]].
  - Equations: 2α₁ + 2α₂ = −1 and 2α₁ + 6α₂ = 1, so α₁ = −1 and α₂ = 0.5.
  - w̃ = −(0, 1, 1) + 0.5(2, 1, 1) = **(1, −0.5, −0.5)**.
  - Line: x₁ − 0.5x₂ − 0.5 = 0. It is **tilted**, with margin 2/√1.25 = **1.789 < 2**.

  It still puts both points on their margin lines, but it is **not** the maximum-margin hyperplane.

**Real data example (Iris, [[05_Iris_Setosa_vs_Versicolor_Choosing_the_Best_Line]]).** Use the correct support vectors (0.4, 1.9) and (1.1, 3.0).

- The shortcut gives w ≈ (2.312, 0.347), b ≈ −2.584, with margin **0.856**.
- The true SVM gives w = (0.824, 1.294), b = −3.788, with margin **1.304**.

The shortcut's line is noticeably worse.

### The exact method (dual form) for hand calculation

In the true dual solution, w = Σ αᵢ yᵢ xᵢ with **αᵢ ≥ 0**, the extra condition **Σ αᵢ yᵢ = 0**, and b is a separate unknown. For the chosen support vectors, solve:

  Σⱼ αⱼ yⱼ (xⱼ · xᵢ) + b = yᵢ  (one equation per support vector)
  Σᵢ αᵢ yᵢ = 0

**Exercise 1** with x₋ = (2, 0) and x₊ = (4, 0):

- Σαy = 0 forces α₋ = α₊ = α, so w = α(4, 0) − α(2, 0) = (2α, 0).
- (4, 0): 8α + b = 1. (2, 0): 4α + b = −1.
- So **α = 0.5**, **b = −3**, **w = (1, 0)** ✔. These are scikit-learn's values: `dual_coef_` = −0.5, +0.5.

**Exercise 2** with x₁ = (1, 0)(−), x₂ = (3, 1)(+), x₃ = (3, −1)(+):

- Σαy = 0 gives α₁ = α₂ + α₃. By symmetry α₂ = α₃ = a and α₁ = 2a.
- w = −2a(1, 0) + a(3, 1) + a(3, −1) = (4a, 0).
- (1, 0): 4a + b = −1. (3, 1): 12a + b = 1.
- So **a = 0.25**, giving α = (0.5, 0.25, 0.25), **b = −2** and **w = (1, 0)** ✔, exactly scikit-learn's values.

**The failure case done properly:**

- α₋ = α₊ = α, so w = α((2, 1) − (0, 1)) = (2α, 0).
- (2, 1): 4α + b = 1. (0, 1): b = −1.
- So α = 0.5 and **w = (1, 0), b = −1**, i.e. x₁ = 1 ✔.

**Two-support-vector closed form.** For one support vector per class, x₋ and x₊, let d = x₊ − x₋ and m = (x₊ + x₋)/2:

  **w = 2d/‖d‖², b = −w·m, margin = ‖d‖**

### Exam advice

1. If the question follows the slide method, show the slide's six steps. Your marks depend on them, and they give the correct line for symmetric textbook data like Exercises 1–2.
2. **Always sanity-check** the final line:
   - The support vectors must score exactly ±1.
   - **Every other point** must satisfy yᵢ(w·xᵢ + b) ≥ 1. If one doesn't, your choice of support vectors was wrong.
   - The line should sit **midway** between the classes, perpendicular to the gap.
3. For two support vectors that are not aligned, use the closed form above or the exact dual equations. They are just as short and always correct.

---

## 2) Simple English Explanation

**What the shortcut does.** The classroom recipe forces each support vector to score exactly −1 or +1. That part is right: support vectors should sit exactly on the edges of the "road". But the way it builds the answer, by mixing the 3-D support vectors, quietly prefers answers where the **shift number b is small** as well as the direction numbers. A real SVM only cares about making the **road as wide as possible**. It doesn't care how big b is.

**Why it still worked in both exercises.**
- **Exercise 2:** three support vectors give three equations, and the line has three unknowns. There's only one possible answer, so any honest method lands on it.
- **Exercise 1:** both support vectors lie on the same horizontal line (y = 0). The leftover freedom only affects the tilt, and both methods choose "no tilt". So they agree again.

**When it goes wrong.**
- Example: one minus point at (0, 1) and one plus point at (2, 1).
- The true best line is the vertical line **x = 1**, exactly halfway, with a road 2 wide.
- The shortcut gives a **tilted** line, x₁ − 0.5x₂ = 0.5, with a road only 1.79 wide.
- It still separates the two points, but it isn't the widest road.
- On the real Iris flowers the shortcut's road would be 0.86 cm wide instead of the true 1.30 cm.

**The proper way, still easy by hand.** The official SVM adds one extra rule: "the α's of the plus side and the minus side must balance" (Σ αᵢyᵢ = 0), and it keeps b as its own unknown.
- **Exercise 1:** the balance rule makes both α's equal.
  - Two short equations, 8α + b = 1 and 4α + b = −1, give α = 0.5 and b = −3.
  - The line is x₁ = 3, the same as the slide.
- **Exercise 2:**
  - Balance plus symmetry gives α = 0.5, 0.25, 0.25 and b = −2, so the line is x₁ = 2, the same as the slide.
  - These are the α values Python reports.

**A super-quick rule for two support vectors.** The best line is the one that cuts the segment between them **in half, at a right angle**, and the road's width equals the length of that segment.

**For your exam.**
- Use the teacher's steps if asked, because they give the right answer on neat textbook data.
- Always check your final line:
  - the support vectors score exactly ±1;
  - every other point scores at least +1 on its side (or at most −1);
  - the line sits right in the middle of the gap.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Shortcut asal mein kya karta hai?**
- Class wala recipe har support vector ko exactly −1 ya +1 score dene pe majboor karta hai. Ye sahi hai, kyunki support vectors ko margin lines pe hi hona chahiye.
- Par jis tareeke se answer banata hai (3-D support vectors ka mix, w̃ = Σαᵢs̃ᵢ), woh chupke se aisa answer pasand karta hai jisme **b (shift) bhi chhota** ho. Technically ye ‖w‖² + b² ko minimum karta hai.
- Asli SVM sirf **‖w‖ chhota** (sadak chaudi) karna chahta hai. Use b ki koi parwaah nahi.

**Dono exercises mein phir bhi sahi kyun aaya?**
- **Exercise 2:** 3 support vectors se 3 equations aur 3 unknowns (w₁, w₂, b). Sirf ek hi answer possible hai (w = (1, 0), b = −2), isliye koi bhi tareeka wahi dega.
- **Exercise 1:** dono SVs (2, 0) aur (4, 0) ek hi horizontal line (x₂ = 0) pe hain. Equations w₁ = 1 aur b = −3 fix kar deti hain, sirf w₂ free bachta hai. Dono methods w₂ = 0 chunte hain, isliye same answer.

**Kab galat hota hai?**
- **Example:** minus point (0, 1), plus point (2, 1).
  - **Asli SVM:** beech mein vertical line **x₁ = 1**, sadak 2 chaudi.
  - **Shortcut:** Gram [[2, 2], [2, 6]], α = (−1, 0.5), w̃ = (1, −0.5, −0.5). Yaani **tirchhi line** x₁ − 0.5x₂ − 0.5 = 0, sadak sirf **1.789** chaudi.
  - Dono points ko alag to karti hai, par sabse chaudi sadak nahi.
- **Asli Iris data pe:** shortcut ka margin **0.856** aata hai, jabki sahi margin **1.304** hai. Kaafi kharab.

**Sahi tareeka (dual form), haath se bhi aasaan.**
- Asli SVM mein w = Σ αᵢyᵢxᵢ, **αᵢ ≥ 0**, ek extra rule **Σ αᵢyᵢ = 0** (plus aur minus side ke α balance hon), aur b alag unknown.
- **Exercise 1:**
  - Balance rule se α₋ = α₊ = α, to w = (2α, 0).
  - (4, 0): 8α + b = 1, aur (2, 0): 4α + b = −1.
  - **α = 0.5, b = −3, w = (1, 0)**. Line x₁ = 3 ✔. scikit-learn ke `dual_coef_` (−0.5, +0.5) bhi yahi kehte hain.
- **Exercise 2:**
  - α₁ = α₂ + α₃. Symmetry se α₂ = α₃ = a, to α₁ = 2a, aur w = (4a, 0).
  - (1, 0): 4a + b = −1, aur (3, 1): 12a + b = 1.
  - **a = 0.25**, to α = (0.5, 0.25, 0.25), b = −2. Line x₁ = 2 ✔ (scikit-learn wale hi numbers).
- **Fail wala case sahi tareeke se:**
  - w = (2α, 0). (2, 1): 4α + b = 1, aur (0, 1): b = −1.
  - α = 0.5, to **x₁ = 1** ✔.

**Do SVs ka super-shortcut formula:**
- d = x₊ − x₋ aur m = (x₊ + x₋)/2 lo.
- **w = 2d/‖d‖², b = −w·m, margin = ‖d‖**.
- Yaani best line dono SVs ko jodne wali line ko **beech se 90° pe kaatti** hai.

**Exam ke liye salaah:**
1. Agar sawaal teacher ke method pe hai, to slide ke 6 steps hi dikhao. Saaf-suthre textbook data (Exercise 1, 2) pe woh sahi answer deta hai.
2. Answer hamesha check karo:
   - SVs ka score exactly ±1 ho.
   - **Baaki har point** ka yᵢ(w·xᵢ + b) ≥ 1 ho. Agar nahi, to support vectors galat chune the.
   - Line dono classes ke beech mein, gap ke perpendicular ho.
3. Do SVs tirchhe (not aligned) hon, to upar wala closed formula ya dual equations use karo. Utne hi chhote hain aur hamesha sahi.
