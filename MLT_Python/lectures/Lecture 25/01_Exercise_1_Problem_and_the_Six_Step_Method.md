# Topic 1: Numerical Exercise 1: The Problem and the Six-Step Method

Source: Lecture 25, slides 1–2 ("Numerical Exercise": question, the six solution steps, and handwritten notes "SVs (x, y) → 3D", "3D → (…, 1) → Bias", "α₁, α₂ = ?", "→ Σ wᵢ αᵢ"; slide 2 repeats the question alone). Builds directly on Lecture 24 ([[03_Support_Vectors_Margin_Hard_and_Soft_Margin]] from Lecture 24).

---

## 1) Technical Explanation

### The question (slides 1–2)

"Consider the following set of data points given, find the **optimal hyperplane** for these data points:

(1, 0.5), (1, 1), (1, −0.5), (−0.5, 0.5), (0.5, 0.5), (2, 0), (4, 0), (4.5, 1), (4.5, 0.5), (5, −1), (5.5, 0)."

**Missing information: the class labels.** The question lists 11 points but never says which are positive and which are negative. The solution (slides 3–6) implicitly treats them as two clusters:

- **Class −1 (left):** (1, 0.5), (1, 1), (1, −0.5), (−0.5, 0.5), (0.5, 0.5), (2, 0). These are the six points with x₁ ≤ 2.
- **Class +1 (right):** (4, 0), (4.5, 1), (4.5, 0.5), (5, −1), (5.5, 0). These are the five points with x₁ ≥ 4.

Because the solution sets the left support vector's equation equal to −1 and the right one's to +1, the left cluster must be the negative class. In an exam, state this assumption explicitly.

### The six-step recipe (slide 1)

| Step | Slide text | Meaning |
|---|---|---|
| 1 | Draw all the points on plane | plot them and see the two clusters and the gap |
| 2 | Find the support vectors | the closest point(s) of each class across the gap |
| 3 | Add the bias (b) value in vectors to convert 2D to 3D form | **augment** each support vector with a 1: s = (x₁, x₂) → s̃ = (x₁, x₂, 1). Handwritten: "SVs (x, y) → 3D", "3D → (…, 1) → Bias" |
| 4 | Consider parameters for every support vector like α₁, α₂, etc. | one unknown αᵢ per support vector. Handwritten: "α₁, α₂ = ?" |
| 5 | Find the linear equations and solve them to find parameter values | one equation per support vector: Σⱼ αⱼ (s̃ⱼ · s̃ᵢ) = yᵢ (−1 or +1) |
| 6 | Final equation for hyperplane is … | w̃ = Σ αᵢ s̃ᵢ. Its first entries are w, and its last entry is b. Handwritten: "→ Σ wᵢ αᵢ" (read: w̃ = Σ αᵢ s̃ᵢ) |

The instructor ticked steps 1–3 while explaining them.

**Why "add a 1"?** With x̃ = (x₁, x₂, 1) and w̃ = (w₁, w₂, b):

  w̃ · x̃ = w₁x₁ + w₂x₂ + b·1 = w·x + b

So the bias is absorbed into the weight vector as one extra coordinate. This is a standard trick, and it is the same "bias as a weight on a constant input of 1" used for the perceptron ([[05_Perceptron_General_Architecture]] from Lecture 4). The slide calls it "converting 2D to 3D". This is a bookkeeping change, not the kernel lift of [[06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick]] from Lecture 24.

**What the equations in step 5 say.** For a support vector, the canonical SVM condition is w·sᵢ + b = yᵢ, i.e. exactly +1 or −1 ([[03_Support_Vectors_Margin_Hard_and_Soft_Margin]] from Lecture 24). Writing w̃ = Σⱼ αⱼ s̃ⱼ and substituting gives

  **Σⱼ αⱼ (s̃ⱼ · s̃ᵢ) = yᵢ** for each support vector i,

a small linear system with as many equations as unknowns.

**Important caveat.**
- In this recipe the αᵢ are **signed coefficients**, e.g. −6.5 and 3.5 in Exercise 1. They are *not* the Lagrange multipliers of SVM theory, which are always ≥ 0.
- The recipe is a classroom **shortcut**. It reproduces the true maximum-margin hyperplane in both exercises of this lecture, but not for every dataset.
- [[06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method]] explains when it works and gives the exact method.

---

## 2) Simple English Explanation

**The task.** We are given 11 points on a graph and asked for the "optimal hyperplane", the best dividing line with the widest possible gap (Lecture 24).

**One thing the question forgets.** It never says which points belong to which class! Looking at the solution, the teacher treats:
- the **left group** (six points from x = −0.5 to x = 2) as the **negative class (−1)**;
- the **right group** (five points from x = 4 to x = 5.5) as the **positive class (+1)**.

In an exam, write that assumption down.

**The six-step recipe on slide 1:**
1. **Plot the points.** You'll see two clumps with an empty strip between them.
2. **Find the support vectors.** These are the points from each clump that face each other across the gap, the "front-line" points.
3. **Add a 1 to each support vector.** (2, 0) becomes (2, 0, 1). The extra 1 is a trick that lets the "shift" number b ride along inside the vector, so we can handle the slope and the shift in one calculation. The teacher calls this "2D → 3D".
4. **Give each support vector an unknown number**: α₁, α₂, and so on.
5. **Write one equation per support vector and solve.** Each equation says "this support vector must score exactly −1 (if negative) or +1 (if positive)".
6. **Build the answer**: multiply each 3-D support vector by its α and add them up. The first two numbers you get are the direction of the line (w), and the last number is the shift (b).

**Fair warning.**
- The α numbers this recipe produces can be negative. They are helper numbers, not the "official" α of SVM theory, which are never negative.
- The recipe is a classroom shortcut. It gives the correct answer for both exercises in this lecture, and Topic 6 shows when it can go wrong and what to do instead.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal (slides 1–2).** 11 points diye hain: (1, 0.5), (1, 1), (1, −0.5), (−0.5, 0.5), (0.5, 0.5), (2, 0), (4, 0), (4.5, 1), (4.5, 0.5), (5, −1), (5.5, 0). Inka **optimal hyperplane** dhoondhna hai, yaani woh dividing line jiska margin (khaali patti) sabse chauda ho (Lecture 24).

**Sawaal ek cheez bhool gaya: labels!** Kaunsa point kis class ka hai, ye nahi likha. Solution dekh ke pata chalta hai:
- **Left group** (x = −0.5 se 2 tak, 6 points) = **class −1 (negative)**.
- **Right group** (x = 4 se 5.5, 5 points) = **class +1 (positive)**.

Exam mein ye assumption likh dena.

**Slide 1 ke 6 steps:**
1. **Saare points plot karo.** Do jhund dikhenge, beech mein khaali patti.
2. **Support vectors dhoondho.** Har jhund ka woh point jo gap ke paar doosre jhund ke saamne hai (front-line).
3. **Har support vector mein 1 jodo.** (2, 0) → (2, 0, 1). Teacher ne likha "SVs (x, y) → 3D" aur "(…, 1) → Bias".
   - Fayda: x̃ = (x₁, x₂, 1) aur w̃ = (w₁, w₂, b) lo, to w̃·x̃ = w₁x₁ + w₂x₂ + b = w·x + b. Bias b vector ke andar hi aa gaya.
   - Perceptron (Lecture 4) mein bhi bias ko "constant input 1 ka weight" maana tha.
   - Ye sirf hisaab ka tareeka hai, Lecture 24 wala kernel (z = x² + y²) nahi.
4. **Har support vector ke liye ek unknown lo**: α₁, α₂ … (teacher: "α₁, α₂ = ?").
5. **Har support vector ki ek equation likho aur solve karo.** Equation kehti hai: "is support vector ka score exactly −1 (negative) ya +1 (positive) ho". Formula: Σⱼ αⱼ (s̃ⱼ · s̃ᵢ) = yᵢ.
6. **Final hyperplane:** w̃ = Σ αᵢ s̃ᵢ. Pehle do numbers = w (line ki direction), aakhri number = b (shift). Teacher ne likha "→ Σ wᵢ αᵢ".

Teacher ne step 1–3 pe tick lagaya hai.

**Saavdhaan.**
- Is shortcut mein α negative bhi aa sakte hain (Exercise 1 mein −6.5 aur 3.5). Ye helper numbers hain, SVM theory ke asli Lagrange multipliers (jo hamesha ≥ 0 hote hain) nahi.
- Ye ek classroom shortcut hai. Is lecture ke dono exercises mein sahi answer deta hai, par har data pe nahi. Kab chalta hai aur sahi general tareeka kya hai, ye Topic 6 mein hai.
