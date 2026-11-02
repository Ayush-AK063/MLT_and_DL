# Topic 2: Exercise 1, Full Solution: Support Vectors, α₁ = −6.5, α₂ = 3.5, Hyperplane x₁ = 3

Source: Lecture 25, slides 3–6:
- Slide 3: "Solution: Step 1: Draw all the points on plane", with the plot "Data Points in Plane" and handwritten S₁, S₂ and the augmented vectors.
- Slide 4: handwritten equations ① to ④ and α₁ = −6.5, α₂ = 3.5.
- Slide 5: handwritten w̃ computation; "for orientation of line", "for bias"; horizontal / vertical / diagonal cases; "b = −3".
- Slide 6: "Solution: Hyperplane, Support Vectors, Margin" plot.

Every number was re-checked by hand and with numpy / scikit-learn (`SVC(kernel='linear', C=10⁶)`).

---

## 1) Technical Explanation

### Step 1: plot (slide 3)

The plot "Data Points in Plane" (axes x₁ from −1 to 6, x₂ from −1.5 to 1.5) shows:

- a **left cluster**: (−0.5, 0.5), (0.5, 0.5), (1, 1), (1, 0.5), (1, −0.5), (2, 0);
- a **right cluster**: (4, 0), (4.5, 1), (4.5, 0.5), (5, −1), (5.5, 0).

The instructor drew a dashed curve in the empty band around x₁ ≈ 3 and wrote "2D to 3D".

### Step 2: support vectors

- The point of the left (−1) cluster closest to the right cluster is **(2, 0)**, circled as **S₁**.
- The point of the right (+1) cluster closest to the left cluster is **(4, 0)**, circled as **S₂**.
- (The handwriting labels both columns "S₂". The left one is S₁.)
- Every other point is farther from the gap. For example, (4.5, ·) is 0.5 farther right than (4, 0), and (1, ·) is 1 farther left than (2, 0).

### Step 3: augment with a 1 (bias coordinate)

  **S̃₁ = (2, 0, 1)**, **S̃₂ = (4, 0, 1)**

### Steps 4–5: equations (slide 4)

Unknowns α₁ and α₂, with w̃ = α₁S̃₁ + α₂S̃₂. The handwritten conditions are:

- ① α₁ S̃₁·S̃₁ + α₂ S̃₂·S̃₁ = **−1**, written "w.r.t. S₁" (S₁ is a negative support vector)
- ② α₁ S̃₁·S̃₂ + α₂ S̃₂·S̃₂ = **+1**, written "w.r.t. S₂" (S₂ is a positive support vector)

Dot products:

- S̃₁·S̃₁ = 2·2 + 0·0 + 1·1 = **5**
- S̃₁·S̃₂ = 2·4 + 0·0 + 1·1 = **9**
- S̃₂·S̃₂ = 4·4 + 0·0 + 1·1 = **17**

So the system is:

- ③ **5α₁ + 9α₂ = −1**
- ④ **9α₁ + 17α₂ = +1**

**Solving.** Multiply ③ by 9 and ④ by 5:

- 45α₁ + 81α₂ = −9
- 45α₁ + 85α₂ = 5

Subtract: 4α₂ = 14, so **α₂ = 3.5**. Then 5α₁ = −1 − 9(3.5) = −32.5, so **α₁ = −6.5**. Both values match the slide ✔. (Check with Cramer's rule: det = 5·17 − 9·9 = 4, α₁ = (−17 − 9)/4 = −6.5, α₂ = (5 + 9)/4 = 3.5.)

### Step 6: the hyperplane (slide 5)

  w̃ = −6.5·(2, 0, 1) + 3.5·(4, 0, 1) = (−13, 0, −6.5) + (14, 0, 3.5) = **(1, 0, −3)**

- **w = (1, 0)** is the part the instructor marks "for orientation of line".
- **b = −3** is the part marked "for bias".
- **Hyperplane:** 1·x₁ + 0·x₂ − 3 = 0, i.e. **x₁ = 3**, a **vertical line** ✔.

**The orientation rule on slide 5.** w is the **normal** (perpendicular) to the line:

| w | Line w·x + b = 0 | Slide's label |
|---|---|---|
| (0, 1) | x₂ = −b, **horizontal** | (i) Horizontal |
| (1, 0) | x₁ = −b, **vertical** | (ii) Vertical (our case) |
| (1, 1) | x₁ + x₂ = −b, **diagonal** with slope −1 | (iii) Diagonal |

**About "b + 3 = 0" on slide 5.** The note "b = −3" is right, but "b + 3 = 0 plus side" is not the hyperplane equation. The equation is **x₁ − 3 = 0** (x₁ = 3).
- Points with x₁ − 3 > 0 lie on the **plus side**: the right cluster, class +1.
- Points with x₁ − 3 < 0 lie on the minus side.

### Slide 6: result, with margin

- The **hyperplane** is the red line x₁ = 3.
- The **margin lines** are purple dashed at x₁ = 2 (w·x + b = −1) and x₁ = 4 (w·x + b = +1).
- The **support vectors** (2, 0) and (4, 0) sit on them.
- The **margin** arrows show 1 unit on each side: d = 1/‖w‖ = 1, and the full width is 2/‖w‖ = **2**.

**Every point checked** (score w·x + b = x₁ − 3):

| Point | Score | Point | Score |
|---|---|---|---|
| (−0.5, 0.5) | −3.5 | (4, 0) | **+1** (SV) |
| (0.5, 0.5) | −2.5 | (4.5, 1) | +1.5 |
| (1, 1), (1, 0.5), (1, −0.5) | −2 | (4.5, 0.5) | +1.5 |
| (2, 0) | **−1** (SV) | (5, −1) | +2 |
| | | (5.5, 0) | +2.5 |

All left points score ≤ −1 and all right points score ≥ +1, so the canonical constraints yᵢ(w·xᵢ + b) ≥ 1 hold ✔.

**scikit-learn agrees.** It gives w = (1, 0), b = −3, support vectors (2, 0) and (4, 0), and margin 2. Its true dual coefficients are αᵢyᵢ = −0.5 and +0.5, so the true multipliers are α = 0.5 each. The slide's −6.5 and 3.5 are different numbers because they come from the augmented shortcut ([[06_Why_the_Shortcut_Works_and_the_Exact_Dual_Method]]).

---

## 2) Simple English Explanation

**Step 1: draw.**
- On the graph, six points sit on the left (from x = −0.5 to x = 2) and five on the right (from x = 4 to x = 5.5).
- Between x = 2 and x = 4 there is an empty strip. The best dividing line will run through it.

**Step 2: front-line points (support vectors).**
- The left group's point closest to the gap is **(2, 0)**. Call it S₁.
- The right group's point closest to the gap is **(4, 0)**. Call it S₂.
- (The teacher's handwriting labels both "S₂", but the left one is S₁.)

**Step 3: add a 1.** S₁ = (2, 0, 1) and S₂ = (4, 0, 1).

**Steps 4–5: two equations.**
- "Dot product" means multiply matching numbers and add:
  - S₁·S₁ = 2×2 + 0×0 + 1×1 = **5**
  - S₁·S₂ = 2×4 + 0 + 1 = **9**
  - S₂·S₂ = 4×4 + 0 + 1 = **17**
- The rules are "S₁ must score −1" and "S₂ must score +1":
  - 5α₁ + 9α₂ = −1
  - 9α₁ + 17α₂ = +1
- Solve them like any pair of school equations:
  - Multiply the first by 9 and the second by 5: 45α₁ + 81α₂ = −9 and 45α₁ + 85α₂ = 5.
  - Subtract: 4α₂ = 14, so **α₂ = 3.5**.
  - Put it back: 5α₁ = −1 − 31.5 = −32.5, so **α₁ = −6.5**.

**Step 6: build the line.**
- −6.5 × (2, 0, 1) = (−13, 0, −6.5)
- 3.5 × (4, 0, 1) = (14, 0, 3.5)
- Add them: **(1, 0, −3)**.
- So w = (1, 0) and b = −3. The line is 1·x₁ + 0·x₂ − 3 = 0, which means **x₁ = 3**: a vertical line exactly halfway between 2 and 4.

**Reading the direction (slide 5).** The w part tells you which way the line faces. w is an arrow pointing *across* the line, not along it.
- w = (0, 1) → horizontal line
- w = (1, 0) → vertical line (our case)
- w = (1, 1) → slanted line going down to the right

**The picture on slide 6.**
- The red line at x = 3 is the hyperplane.
- The purple dashed lines at x = 2 and x = 4 are the edges of the "road".
- The points (2, 0) and (4, 0) sit right on those edges; they are the support vectors.
- The road is 1 unit wide on each side, **2 units** in total.

**Checking every point.** The score of each point is just x₁ − 3.
- Left points: −3.5, −2.5, −2, −2, −2, −1. All negative.
- Right points: +1, +1.5, +1.5, +2, +2.5. All positive.
- Nobody is inside the road. ✔

**A small slip on slide 5.** It says "b + 3 = 0". The real line equation is **x₁ − 3 = 0**. Points where x₁ − 3 is positive are on the "plus side".

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Step 1: plot karo (slide 3).**
- Left mein 6 points: (−0.5, 0.5), (0.5, 0.5), (1, 1), (1, 0.5), (1, −0.5), (2, 0).
- Right mein 5 points: (4, 0), (4.5, 1), (4.5, 0.5), (5, −1), (5.5, 0).
- x = 2 aur x = 4 ke beech khaali patti hai. Best line isi mein se jaayegi. Teacher ne wahan dashed curve bana ke "2D to 3D" likha.

**Step 2: support vectors.**
- Left group ka gap ke sabse paas point: **(2, 0)**, yaani S₁.
- Right group ka sabse paas point: **(4, 0)**, yaani S₂.
- (Handwriting mein dono pe "S₂" likha hai, par left wala S₁ hai.)

**Step 3: 1 jodo.** S̃₁ = (2, 0, 1), S̃₂ = (4, 0, 1).

**Steps 4–5: equations (slide 4).**
- Teacher ki equations:
  - ① α₁ S₁·S₁ + α₂ S₂·S₁ = −1 (S₁ ke hisaab se, kyunki S₁ negative hai)
  - ② α₁ S₁·S₂ + α₂ S₂·S₂ = +1 (S₂ ke hisaab se, positive)
- Dot product = matching numbers ka guna karke jodo:
  - S₁·S₁ = 4 + 0 + 1 = **5**
  - S₁·S₂ = 8 + 0 + 1 = **9**
  - S₂·S₂ = 16 + 0 + 1 = **17**
- To equations ban gayi:
  - ③ **5α₁ + 9α₂ = −1**
  - ④ **9α₁ + 17α₂ = 1**
- Solve:
  - ③ × 9 → 45α₁ + 81α₂ = −9, aur ④ × 5 → 45α₁ + 85α₂ = 5.
  - Ghatao: 4α₂ = 14, to **α₂ = 3.5**.
  - Wapas daalo: 5α₁ = −1 − 31.5 = −32.5, to **α₁ = −6.5** ✔ (slide se match).

**Step 6: hyperplane (slide 5).**
- w̃ = α₁S̃₁ + α₂S̃₂ = −6.5(2, 0, 1) + 3.5(4, 0, 1) = (−13, 0, −6.5) + (14, 0, 3.5) = **(1, 0, −3)**.
- Pehle do numbers **w = (1, 0)**: teacher ne likha "for orientation of line".
- Aakhri number **b = −3**: "for bias".
- Line: 1·x₁ + 0·x₂ − 3 = 0, yaani **x₁ = 3**: ek **vertical line**, 2 aur 4 ke theek beech.

**Direction kaise padhein (slide 5).** w line ke *perpendicular* (90°) wala teer hai, line ke saath nahi.
- (i) w = (0, 1) → **horizontal** line
- (ii) w = (1, 0) → **vertical** line (humara case)
- (iii) w = (1, 1) → **diagonal** line (x₁ + x₂ = constant, slope −1)

**Chhoti galti.** Slide 5 pe "b + 3 = 0 plus side" likha hai. Sahi equation **x₁ − 3 = 0** hai. Jahan x₁ − 3 > 0 ho, woh **plus side** (right cluster, class +1) hai.

**Slide 6 ki picture.**
- Laal line x₁ = 3 hyperplane hai.
- Purple dashed lines x₁ = 2 (score −1) aur x₁ = 4 (score +1) margin ki lines hain.
- (2, 0) aur (4, 0) unpe baithe support vectors hain.
- Margin dono taraf 1 unit hai, total **2/‖w‖ = 2**.

**Har point check kiya (score = x₁ − 3):**
- Left: −3.5, −2.5, −2, −2, −2, **−1** (SV).
- Right: **+1** (SV), +1.5, +1.5, +2, +2.5.
- Sab apni side pe, koi margin ke andar nahi ✔.
- scikit-learn ne bhi w = (1, 0), b = −3, margin 2 diya. Uske asli α dono 0.5 hain. Slide ke −6.5 aur 3.5 shortcut wale helper numbers hain, isliye alag hain (Topic 6).
