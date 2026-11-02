# Topic 8: Worked Example: Eight Points, Three Clusters, Manhattan Distance

Source: Lecture 23, slides 26–32 ("Example"; "Iteration-01" blank and filled tables; new centres after iteration 1; "Iteration-02" blank and filled tables; new centres after iteration 2), including the instructor's handwritten working on slides 26, 27 and 29. Every number was re-computed by us in Python. Iterations 3–4 (to convergence) are our own extension and are not on the slides.

---

## 1) Technical Explanation

### The problem (slide 26)

Cluster the eight points

  A1(2, 10), A2(2, 5), A3(8, 4), A4(5, 8), A5(7, 5), A6(6, 4), A7(1, 2), A8(4, 9)

into **k = 3** clusters.

- **Initial centres:** A1(2, 10) for C1, A4(5, 8) for C2 and A7(1, 2) for C3.
- **Distance function:** ρ(a, b) = |x₂ − x₁| + |y₂ − y₁|. This is the **Manhattan (L1)** distance ([[04_Distance_Metrics]] from Lecture 16).
- **Task:** find the three cluster centres after the **second iteration**.

Each iteration follows [[04_K_Means_Algorithm_Steps]]: assign every point to its nearest centre, then replace each centre by the **mean** of its points.

**Handwritten note on slide 26.** The instructor began a scratch table: Points | A1(2,10) | A4(5,8) | A7(1,2) | Final cluster. The first row reads A1(2,10): **0**, **5**, **8**, final cluster **A1**.

The third entry should be **9**, not 8: |1 − 2| + |2 − 10| = 1 + 8 = 9. The printed table on slides 27–28 correctly has 9. The final cluster is unaffected, since 0 is still the smallest.

### Iteration 1: centres (2, 10), (5, 8), (1, 2)

Distances are shown as |Δx| + |Δy|:

| Point | to C1 (2,10) | to C2 (5,8) | to C3 (1,2) | Cluster |
|---|---|---|---|---|
| A1(2,10) | 0+0 = **0** | 3+2 = 5 | 1+8 = 9 | **C1** |
| A2(2,5) | 0+5 = 5 | 3+3 = 6 | 1+3 = **4** | **C3** |
| A3(8,4) | 6+6 = 12 | 3+4 = **7** | 7+2 = 9 | **C2** |
| A4(5,8) | 3+2 = 5 | 0+0 = **0** | 4+6 = 10 | **C2** |
| A5(7,5) | 5+5 = 10 | 2+3 = **5** | 6+3 = 9 | **C2** |
| A6(6,4) | 4+6 = 10 | 1+4 = **5** | 5+2 = 7 | **C2** |
| A7(1,2) | 1+8 = 9 | 4+6 = 10 | 0+0 = **0** | **C3** |
| A8(4,9) | 2+1 = 3 | 1+1 = **2** | 3+7 = 10 | **C2** |

This matches the slide-28 table exactly ✔. On slide 27 the instructor wrote out one cell, A2 → C2 = |2 − 5| + |5 − 8| = 6, and summarised the result as C1 = {A1(2,10)}, C2 = {A3, A4, A5, A6, A8}, C3 = {A2, A7}.

**Update step (slide 29).**

- **C1** = {A1}: the only point, so the centre stays **(2, 10)**.
- **C2** = {A3, A4, A5, A6, A8}: ((8+5+7+6+4)/5, (4+8+5+4+9)/5) = (30/5, 30/5) = **(6, 6)** ✔
- **C3** = {A2, A7}: ((2+1)/2, (5+2)/2) = **(1.5, 3.5)** ✔

### Iteration 2: centres (2, 10), (6, 6), (1.5, 3.5)

| Point | to C1 (2,10) | to C2 (6,6) | to C3 (1.5,3.5) | Cluster |
|---|---|---|---|---|
| A1(2,10) | **0** | 4+4 = 8 | 0.5+6.5 = 7 | **C1** |
| A2(2,5) | 5 | 4+1 = 5 | 0.5+1.5 = **2** | **C3** |
| A3(8,4) | 12 | 2+2 = **4** | 6.5+0.5 = 7 | **C2** |
| A4(5,8) | 5 | 1+2 = **3** | 3.5+4.5 = 8 | **C2** |
| A5(7,5) | 10 | 1+1 = **2** | 5.5+1.5 = 7 | **C2** |
| A6(6,4) | 10 | 0+2 = **2** | 4.5+0.5 = 5 | **C2** |
| A7(1,2) | 9 | 5+4 = 9 | 0.5+1.5 = **2** | **C3** |
| A8(4,9) | 2+1 = **3** | 2+3 = 5 | 2.5+5.5 = 8 | **C1** ← moved from C2 |

This matches the slide-31 table ✔. Two points tie between C1 and C2: A2 (5 vs 5) and A7 (9 vs 9). Neither tie matters, because C3 is clearly nearest for both (distance 2).

The one change is that **A8 moves from C2 to C1**. Its old centre (5, 8) was pulled away to (6, 6) by A3, A5 and A6.

**Update step (slide 32).**

- **C1** = {A1, A8}: ((2+4)/2, (10+9)/2) = **(3, 9.5)** ✔
- **C2** = {A3, A4, A5, A6}: ((8+5+7+6)/4, (4+8+5+4)/4) = (26/4, 21/4) = **(6.5, 5.25)** ✔
- **C3** = {A2, A7}: **(1.5, 3.5)** (unchanged) ✔

**Answer to the exam question:** after the second iteration the centres are **C1(3, 9.5), C2(6.5, 5.25), C3(1.5, 3.5)** ✔.

### Our extension: running to convergence (not on the slides)

The slides stop after two iterations because the question asks only for that. The algorithm has **not** converged yet.

**Iteration 3: centres (3, 9.5), (6.5, 5.25), (1.5, 3.5).**

| Point | to C1 | to C2 | to C3 | Cluster |
|---|---|---|---|---|
| A1 | **1.5** | 9.25 | 7 | C1 |
| A2 | 5.5 | 4.75 | **2** | C3 |
| A3 | 10.5 | **2.75** | 7 | C2 |
| A4(5,8) | 2+1.5 = **3.5** | 1.5+2.75 = 4.25 | 8 | **C1** ← moved from C2 |
| A5 | 8.5 | **0.75** | 7 | C2 |
| A6 | 8.5 | **1.75** | 5 | C2 |
| A7 | 9.5 | 8.75 | **2** | C3 |
| A8 | **1.5** | 6.25 | 8 | C1 |

New centres:

- C1 = {A1, A4, A8}: ((2+5+4)/3, (10+8+9)/3) = **(3.67, 9)**
- C2 = {A3, A5, A6}: ((8+7+6)/3, (4+5+4)/3) = **(7, 4.33)**
- C3 = {A2, A7}: **(1.5, 3.5)**

**Iteration 4.** No point changes cluster, so the algorithm has **converged**.

**Final clusters:** C1 = {A1, A4, A8} (top-left), C2 = {A3, A5, A6} (right), C3 = {A2, A7} (bottom-left).

**SSE (squared Euclidean, measured after each update) falls every iteration:**

| After | Iteration 1 | Iteration 2 | Iteration 3 (final) |
|---|---|---|---|
| SSE | 37.0 | 23.25 | 14.33 |

For example, after iteration 2: C1 contributes 1.25 + 1.25 = 2.5, C2 contributes 3.8125 + 9.8125 + 0.3125 + 1.8125 = 15.75, and C3 contributes 2.5 + 2.5 = 5. Total: 23.25.

14.33 is also the best SSE that scikit-learn finds for k = 3 on these points ([[06_Choosing_k_SSE_and_the_Elbow_Method]]), so this run reached the global optimum.

**Euclidean cross-check.** Re-running with Euclidean distance gives exactly the same assignments in every iteration. On this dataset the choice of metric doesn't change the answer.

**Subtle point.** The example assigns points with Manhattan distance but updates centres with the **mean**. Strictly, the mean minimises *squared Euclidean* error. The centre that minimises total Manhattan distance is the coordinate-wise **median**, and using it gives the **k-medians** algorithm. The slide's mix is the common textbook convention and works fine here. It just means the "SSE never increases" guarantee of [[04_K_Means_Algorithm_Steps]] isn't strictly guaranteed for this hybrid.

---

## 2) Simple English Explanation

**The question.**
- We have 8 places on a map: A1(2,10), A2(2,5), A3(8,4), A4(5,8), A5(7,5), A6(6,4), A7(1,2), A8(4,9).
- We want 3 groups, and we start the three centres at A1, A4 and A7.
- Distance is "**city-block**" distance: how far you go left/right plus how far you go up/down. For example, from (2,5) to (5,8) is 3 across + 3 up = 6.
- Find the centres after 2 rounds.

**A small slip in the teacher's scratch work (slide 26).** The teacher wrote the distance from A1(2,10) to A7(1,2) as 8. It is actually 1 across + 8 down = **9**. The printed table has 9, and the answer for A1 doesn't change.

**Round 1.**
- Measure each place's distance to the three centres (2,10), (5,8), (1,2), and join the closest:
  - A1 → 0 to itself → **C1**
  - A2 → 5, 6, **4** → **C3**
  - A3 → 12, **7**, 9 → **C2**
  - A4 → **0** to itself → **C2**
  - A5 → 10, **5**, 9 → **C2**
  - A6 → 10, **5**, 7 → **C2**
  - A7 → **0** to itself → **C3**
  - A8 → 3, **2**, 10 → **C2**
- So C1 = {A1}, C2 = {A3, A4, A5, A6, A8}, C3 = {A2, A7}.
- Move each centre to the average of its members:
  - C1 stays at (2, 10). It has only one member.
  - C2: x-average = (8+5+7+6+4)/5 = 30/5 = 6, and y-average = (4+8+5+4+9)/5 = 30/5 = 6, so **(6, 6)**.
  - C3: ((2+1)/2, (5+2)/2) = **(1.5, 3.5)**.

**Round 2.**
- Measure again to (2,10), (6,6), (1.5,3.5):
  - A1 → 0, 8, 7 → C1
  - A2 → 5, 5, **2** → C3
  - A3 → 12, **4**, 7 → C2
  - A4 → 5, **3**, 8 → C2
  - A5 → 10, **2**, 7 → C2
  - A6 → 10, **2**, 5 → C2
  - A7 → 9, 9, **2** → C3
  - A8 → **3**, 5, 8 → **C1**
- **The one change: A8 switches from C2 to C1.** The C2 centre moved away to (6, 6), so A8 is now closer to C1.
- A2 and A7 each have two equal numbers (5 and 5; 9 and 9), but those aren't their smallest. Their smallest is 2 (C3), so there is no real tie.
- New averages:
  - C1 = {A1, A8}: ((2+4)/2, (10+9)/2) = **(3, 9.5)**
  - C2 = {A3, A4, A5, A6}: (26/4, 21/4) = **(6.5, 5.25)**
  - C3 = {A2, A7}: still **(1.5, 3.5)**

**✅ Exam answer:** after 2 rounds the centres are **(3, 9.5), (6.5, 5.25), (1.5, 3.5)**. We re-checked every number with a computer.

**What happens if we keep going? (our extra work)**
- **Round 3:** A4(5,8) is now 3.5 from C1 but 4.25 from C2, so A4 switches to C1. New centres: C1 = {A1, A4, A8} → (3.67, 9), C2 = {A3, A5, A6} → (7, 4.33), C3 stays (1.5, 3.5).
- **Round 4:** nobody switches, so we stop.
- Final groups: {A1, A4, A8} top-left, {A3, A5, A6} right, {A2, A7} bottom-left.
- The "tightness score" (SSE) got better every round: 37 → 23.25 → 14.33. 14.33 is the best possible for 3 groups on these points.
- Using normal straight-line distance instead of city-block gives exactly the same groups here.

**A fine point.** The example measures with city-block distance but moves centres to the *average*. For city-block distance the perfectly matching centre would be the *median* (that's called k-medians). The mix is common in textbooks and works fine here.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal (slide 26).**
- 8 points hain: A1(2,10), A2(2,5), A3(8,4), A4(5,8), A5(7,5), A6(6,4), A7(1,2), A8(4,9).
- Inhe **3 clusters** mein baantna hai. Shuruaati centres: C1 = A1(2,10), C2 = A4(5,8), C3 = A7(1,2).
- Distance **Manhattan** hai: ρ(a,b) = |x₂ − x₁| + |y₂ − y₁|, yaani left-right kitna chalo + upar-neeche kitna chalo. Jaise (2,5) se (5,8): |2−5| + |5−8| = 3 + 3 = **6**. Ye teacher ne slide 27 pe likh ke dikhaya.
- **Do iterations ke baad centres batao.**

**Teacher ki chhoti galti (slide 26 ka scratch table).** A1(2,10) se A7(1,2) ki doori "8" likhi hai, par sahi hai |1−2| + |2−10| = 1 + 8 = **9**. Printed table mein 9 hi hai, aur A1 ka cluster (C1) waise bhi nahi badalta.

**Iteration 1 (centres (2,10), (5,8), (1,2)).**

Har point ki teeno centres se doori, aur jo sabse kam ho, wahi cluster:

| Point | C1 | C2 | C3 | Cluster |
|---|---|---|---|---|
| A1 | 0 | 5 | 9 | C1 |
| A2 | 5 | 6 | **4** | C3 |
| A3 | 12 | **7** | 9 | C2 |
| A4 | 5 | **0** | 10 | C2 |
| A5 | 10 | **5** | 9 | C2 |
| A6 | 10 | **5** | 7 | C2 |
| A7 | 9 | 10 | **0** | C3 |
| A8 | 3 | **2** | 10 | C2 |

Groups: C1 = {A1}, C2 = {A3, A4, A5, A6, A8}, C3 = {A2, A7}.

Naye centres (average):
- C1: akela A1 hai, to **(2, 10)** hi rahega.
- C2: x = (8+5+7+6+4)/5 = 30/5 = 6, y = (4+8+5+4+9)/5 = 30/5 = 6, to **(6, 6)**.
- C3: x = (2+1)/2 = 1.5, y = (5+2)/2 = 3.5, to **(1.5, 3.5)**.

**Iteration 2 (centres (2,10), (6,6), (1.5,3.5)).**

| Point | C1 | C2 | C3 | Cluster |
|---|---|---|---|---|
| A1 | **0** | 8 | 7 | C1 |
| A2 | 5 | 5 | **2** | C3 |
| A3 | 12 | **4** | 7 | C2 |
| A4 | 5 | **3** | 8 | C2 |
| A5 | 10 | **2** | 7 | C2 |
| A6 | 10 | **2** | 5 | C2 |
| A7 | 9 | 9 | **2** | C3 |
| A8 | **3** | 5 | 8 | **C1** (C2 se shift hua!) |

- **Ek hi badlaav: A8 C2 se C1 mein aa gaya.** C2 ka centre (5,8) se khisak ke (6,6) chala gaya, to A8 ab C1 ke zyada paas hai.
- A2 (5, 5) aur A7 (9, 9) mein do barabar numbers hain, par unka sabse chhota 2 (C3) hai, to koi asli tie nahi.

Naye centres:
- C1 = {A1, A8}: ((2+4)/2, (10+9)/2) = **(3, 9.5)**
- C2 = {A3, A4, A5, A6}: ((8+5+7+6)/4, (4+8+5+4)/4) = (26/4, 21/4) = **(6.5, 5.25)**
- C3 = {A2, A7}: **(1.5, 3.5)**, koi badlaav nahi.

**✅ Exam ka answer:** 2nd iteration ke baad **C1(3, 9.5), C2(6.5, 5.25), C3(1.5, 3.5)**. Humne har number Python se dobara check kiya, sab sahi hai.

**Aage kya hota? (humara extra kaam, slide pe nahi)**
- **Iteration 3:** A4(5,8) ki C1 (3,9.5) se doori 2 + 1.5 = **3.5**, aur C2 (6.5,5.25) se 1.5 + 2.75 = 4.25. To A4 C1 mein chala gaya.
  - Naye centres: C1 = {A1, A4, A8} → (11/3, 27/3) = **(3.67, 9)**, C2 = {A3, A5, A6} → (21/3, 13/3) = **(7, 4.33)**, C3 = **(1.5, 3.5)**.
- **Iteration 4:** kisi point ne cluster nahi badla, to **converge** ho gaya, stop.
- **Final clusters:** {A1, A4, A8} upar-left, {A3, A5, A6} right side, {A2, A7} neeche-left.
- SSE har round ghata: **37 → 23.25 → 14.33**. 14.33 hi 3 clusters ka sabse best SSE hai (scikit-learn ne bhi yahi diya).
- Euclidean (seedhi line) distance use karo to bhi bilkul yahi groups bante hain.

**Ek baareek baat.** Is example mein distance Manhattan se naapi, par centre **mean (average)** se nikala. Manhattan ke liye perfect centre asal mein **median** hota hai (us algorithm ko k-medians kehte hain). Textbooks mein ye mix common hai aur yahan sahi kaam karta hai. Exam mein slide wala tareeka (mean) hi use karo.
