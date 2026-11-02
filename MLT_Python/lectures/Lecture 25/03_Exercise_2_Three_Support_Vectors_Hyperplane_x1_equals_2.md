# Topic 3: Exercise 2: Three Support Vectors, Hyperplane x₁ = 2

Source: Lecture 25, slide 7 ("Numerical Exercise 2", with handwritten answers: support vectors S₁ = (1, 0, 1) (−), S₂ = (3, 1, 1) (+), S₃ = (3, −1, 1) (+); α₁ = −3.5, α₂ = 0.75, α₃ = 0.75; w̃ = Σ αᵢSᵢ = (1, 0, −2); "(i) Vertical, w = (1, 0)", "(ii) b = −2", "(iii) b + 2 = 0"). The slide gives only the answers. The full working below (dot products, equations, solution, checks) is ours, verified with numpy and scikit-learn. This is the **same dataset** we solved in Lecture 24, Topic 3 ([[03_Support_Vectors_Margin_Hard_and_Soft_Margin]] from Lecture 24).

---

## 1) Technical Explanation

### The question

"Suppose we are given the following positively labelled data points (3, 1), (3, −1), (6, 1), (6, −1), and the following negatively labelled data points (1, 0), (0, 1), (0, −1), (−1, 0). Find the optimal hyperplane for these data points."

Unlike Exercise 1, the labels are given explicitly here.

### Step 1–2: plot and support vectors

- The negative points form a diamond around the origin. The rightmost one is **(1, 0)**.
- The positive points form a rectangle at x₁ = 3 and x₁ = 6. The leftmost pair is **(3, 1)** and **(3, −1)**.
- The gap runs from x₁ = 1 to x₁ = 3, so the support vectors are:
  - S₁ = (1, 0), class −1
  - S₂ = (3, 1), class +1
  - S₃ = (3, −1), class +1
- These match the slide's choices, marked "−", "+" and "+" in the handwriting.

### Step 3: augment

  S̃₁ = (1, 0, 1), S̃₂ = (3, 1, 1), S̃₃ = (3, −1, 1)

### Step 4–5: dot products and equations

| · | S̃₁ | S̃₂ | S̃₃ |
|---|---|---|---|
| S̃₁ | 1+0+1 = **2** | 3+0+1 = **4** | 3+0+1 = **4** |
| S̃₂ | 4 | 9+1+1 = **11** | 9−1+1 = **9** |
| S̃₃ | 4 | 9 | 9+1+1 = **11** |

Equations (Σⱼ αⱼ S̃ⱼ·S̃ᵢ = yᵢ):

- ① 2α₁ + 4α₂ + 4α₃ = **−1**
- ② 4α₁ + 11α₂ + 9α₃ = **+1**
- ③ 4α₁ + 9α₂ + 11α₃ = **+1**

**Solving.**

- ② − ③ gives 2α₂ − 2α₃ = 0, so **α₂ = α₃** (expected from the symmetry about the x₁-axis).
- With α₃ = α₂:
  - ① becomes 2α₁ + 8α₂ = −1.
  - ② becomes 4α₁ + 20α₂ = 1.
- Doubling ① gives 4α₁ + 16α₂ = −2. Subtracting this from ② gives 4α₂ = 3, so **α₂ = α₃ = 0.75**.
- Then 2α₁ = −1 − 6 = −7, so **α₁ = −3.5**.

All three match the slide ✔.

### Step 6: hyperplane

  w̃ = −3.5·(1, 0, 1) + 0.75·(3, 1, 1) + 0.75·(3, −1, 1)
   = (−3.5 + 2.25 + 2.25, 0 + 0.75 − 0.75, −3.5 + 0.75 + 0.75)
   = **(1, 0, −2)**

- **w = (1, 0)**, so the line is **vertical** ("(i) Vertical" on the slide).
- **b = −2** ("(ii)").
- Hyperplane: x₁ − 2 = 0, i.e. **x₁ = 2**, halfway between x₁ = 1 and x₁ = 3.
- The slide's "(iii) b + 2 = 0" should be read as **x₁ − 2 = 0**. This is the same notational slip as in Exercise 1 ([[02_Exercise_1_Full_Solution_Alphas_and_Hyperplane_x1_equals_3]]).

**Margin:** 2/‖w‖ = 2/1 = **2**. The margin lines are x₁ = 1 (score −1) and x₁ = 3 (score +1).

**Checking all 8 points** (score = x₁ − 2):

| Positive points | Score | Negative points | Score |
|---|---|---|---|
| (3, 1), (3, −1) | **+1** (SVs) | (1, 0) | **−1** (SV) |
| (6, 1), (6, −1) | +4 | (0, 1), (0, −1) | −2 |
| | | (−1, 0) | −3 |

Every positive point scores ≥ +1 and every negative point scores ≤ −1 ✔.

**scikit-learn** (Lecture 24 run): w = (1, 0), b = −2, support vectors (1, 0), (3, 1), (3, −1). The true multipliers are α = 0.5, 0.25, 0.25, with αᵢyᵢ = −0.5, +0.25, +0.25. Again they differ from the shortcut's −3.5, 0.75, 0.75, but the **hyperplane is identical**. Why this happens is explained in [[06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method]].

---

## 2) Simple English Explanation

**The question.** Plus points: (3, 1), (3, −1), (6, 1), (6, −1). Minus points: (1, 0), (0, 1), (0, −1), (−1, 0). Find the best dividing line. This time the labels *are* given.

**Picture it.**
- The minus points make a small diamond around the centre (0, 0).
- The plus points make a rectangle further right.
- The minus point nearest the gap is (1, 0). The plus points nearest the gap are (3, 1) and (3, −1).
- So there are **three support vectors** this time. The slide marks them "−", "+", "+".

**Add a 1 to each:** (1, 0, 1), (3, 1, 1), (3, −1, 1).

**All the dot products** (multiply matching numbers, then add):
- S₁·S₁ = 2, S₁·S₂ = 4, S₁·S₃ = 4
- S₂·S₂ = 11, S₂·S₃ = 9, S₃·S₃ = 11

**Three equations** ("minus support vector scores −1, plus ones score +1"):
- 2α₁ + 4α₂ + 4α₃ = −1
- 4α₁ + 11α₂ + 9α₃ = 1
- 4α₁ + 9α₂ + 11α₃ = 1

**Solve step by step:**
1. Subtract the third equation from the second: 2α₂ − 2α₃ = 0, so α₂ = α₃. (That makes sense: the two plus support vectors are mirror images.)
2. Replace α₃ by α₂:
   - 2α₁ + 8α₂ = −1
   - 4α₁ + 20α₂ = 1
3. Double the first one (4α₁ + 16α₂ = −2) and subtract it from the second: 4α₂ = 3, so **α₂ = α₃ = 0.75**.
4. Then 2α₁ = −1 − 6 = −7, so **α₁ = −3.5**. These are exactly the numbers on the slide.

**Build the line.**
- −3.5 × (1, 0, 1) + 0.75 × (3, 1, 1) + 0.75 × (3, −1, 1) = **(1, 0, −2)**.
- So w = (1, 0) means a vertical line, and b = −2.
- The line is **x₁ = 2**, exactly halfway between the minus edge (x₁ = 1) and the plus edge (x₁ = 3).
- The road is **2 units** wide.

**Check every point** (score = x₁ − 2):
- Plus points score +1, +1, +4, +4.
- Minus points score −1, −2, −2, −3.
- All are on the correct side and none is inside the road. ✔

**Already seen!** This is exactly the example we solved in Lecture 24, Topic 3, using a different method. Python's SVM gives the same line, x₁ = 2.

**Same small slip as before.** The slide writes "b + 2 = 0", but the line's equation is **x₁ − 2 = 0**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal (slide 7).**
- Positive points: (3, 1), (3, −1), (6, 1), (6, −1).
- Negative points: (1, 0), (0, 1), (0, −1), (−1, 0).
- Optimal hyperplane dhoondho. Is baar labels diye hue hain.

**Picture socho.**
- Negative points (0, 0) ke around ek chhota diamond banate hain.
- Positive points right mein ek rectangle.
- Gap ke sabse paas: negative mein **(1, 0)**, positive mein **(3, 1)** aur **(3, −1)**.
- Is baar **teen support vectors** hain. Slide pe teacher ne "−", "+", "+" mark kiya hai.

**1 jodo:** S̃₁ = (1, 0, 1), S̃₂ = (3, 1, 1), S̃₃ = (3, −1, 1).

**Saare dot products (slide pe nahi the, humne nikaale):**
- S₁·S₁ = 1 + 0 + 1 = **2**
- S₁·S₂ = 3 + 0 + 1 = **4**, S₁·S₃ = **4**
- S₂·S₂ = 9 + 1 + 1 = **11**, S₃·S₃ = **11**
- S₂·S₃ = 9 − 1 + 1 = **9**

**Teen equations:**
- ① 2α₁ + 4α₂ + 4α₃ = −1
- ② 4α₁ + 11α₂ + 9α₃ = 1
- ③ 4α₁ + 9α₂ + 11α₃ = 1

**Solve:**
1. ② − ③: 2α₂ − 2α₃ = 0, to **α₂ = α₃**. Dono plus SVs ek dusre ki mirror image hain, isliye barabar.
2. α₃ = α₂ daalo: ① → 2α₁ + 8α₂ = −1 aur ② → 4α₁ + 20α₂ = 1.
3. ① × 2 = 4α₁ + 16α₂ = −2. Ise ② se ghatao: 4α₂ = 3, to **α₂ = α₃ = 0.75**.
4. 2α₁ = −1 − 6 = −7, to **α₁ = −3.5**. Slide ke answers se bilkul match ✔.

**Hyperplane.**
- w̃ = −3.5(1, 0, 1) + 0.75(3, 1, 1) + 0.75(3, −1, 1).
  - x₁ part: −3.5 + 2.25 + 2.25 = 1
  - x₂ part: 0 + 0.75 − 0.75 = 0
  - bias part: −3.5 + 0.75 + 0.75 = −2
  - Total: **(1, 0, −2)**.
- w = (1, 0), to **vertical line** (slide ka "(i) Vertical"). b = −2 (slide ka "(ii)").
- Line: **x₁ − 2 = 0, yaani x₁ = 2**, jo 1 aur 3 ke theek beech hai.
- Slide ka "(iii) b + 2 = 0" asal mein **x₁ − 2 = 0** hona chahiye. Ye wahi chhoti galti hai jo Exercise 1 mein thi.
- Margin = 2/‖w‖ = **2**. Margin lines x₁ = 1 aur x₁ = 3 hain.

**Har point check (score = x₁ − 2):**
- Positive: (3, ±1) → **+1** (SV), (6, ±1) → +4.
- Negative: (1, 0) → **−1** (SV), (0, ±1) → −2, (−1, 0) → −3.
- Sab sahi side pe ✔.

**Ye pehle dekha hua hai!** Lecture 24 Topic 3 mein humne yahi dataset doosre tareeke se solve kiya tha. scikit-learn ne bhi x₁ = 2 diya, aur asli α = 0.5, 0.25, 0.25 the. Slide ke −3.5, 0.75, 0.75 shortcut wale helper numbers hain, par **line bilkul same** aati hai. Kyun? Topic 6 dekho.
