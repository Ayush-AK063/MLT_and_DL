# Topic 7: Worked Example — Classifying a Paper Tissue as Good or Bad (K = 3)

Source: Lecture 16, slides 17–20 ("K-NN Classifier – Numerical Example 1" and its four-part solution: parameter K, squared distances, ranking, gathering categories and majority vote). Independently re-verified numerically.

---

## 1) Technical Explanation

**Problem (slide 17).** A survey (people's opinions) plus objective testing give two attributes for four paper-tissue samples: **X1 = Acid Durability (seconds)** and **X2 = Strength (kg/square meter)**, and a class **Y = Good / Bad**:

| X1 (Acid durability) | X2 (Strength) | Y |
|---|---|---|
| 7 | 7 | Bad |
| 7 | 4 | Bad |
| 3 | 4 | Good |
| 1 | 4 | Good |

A new tissue passes the laboratory test with **X1 = 3, X2 = 7**. *Without another expensive survey, can we guess its classification?* The **query instance** is (3, 7).

**Step 1 — Determine K (slide 17).** Suppose **K = 3**.

**Step 2 — Calculate the distance to every training sample (slides 17–18).** The slide computes the **squared** Euclidean distance — *"instead of calculating the distance we compute square distance which is faster to calculate (without square root)"*. This is valid because √ is increasing: if a² < b² then a < b, so the **neighbor ranking is identical** with or without the root.

Squared distance to (3, 7) = (X1 − 3)² + (X2 − 7)²:

| X1 | X2 | Computation | Squared distance |
|---|---|---|---|
| 7 | 7 | (7−3)² + (7−7)² = 16 + 0 | **16** |
| 7 | 4 | (7−3)² + (4−7)² = 16 + 9 | **25** |
| 3 | 4 | (3−3)² + (4−7)² = 0 + 9 | **9** |
| 1 | 4 | (1−3)² + (4−7)² = 4 + 9 | **13** |

(All four match the slide, re-verified.)

**Step 3 — Sort and pick the nearest K (slide 19).**

| X1 | X2 | Sq. distance | Rank (min distance) | In 3-nearest? |
|---|---|---|---|---|
| 3 | 4 | 9 | **1** | Yes |
| 1 | 4 | 13 | **2** | Yes |
| 7 | 7 | 16 | **3** | Yes |
| 7 | 4 | 25 | 4 | **No** |

**Step 4 — Gather the categories (slide 20).** The fourth row's category is *not* included because its rank (4) is greater than K (= 3):

| Rank | Sample | Y |
|---|---|---|
| 1 | (3, 4) | Good |
| 2 | (1, 4) | Good |
| 3 | (7, 7) | Bad |
| 4 | (7, 4) | — (excluded) |

**Step 5 — Simple majority.** *2 Good and 1 Bad* → the new tissue (X1 = 3, X2 = 7) is classified **Good**.

**Observations (our analysis).**
- The true (rooted) distances are √9 = 3, √13 ≈ 3.606, √16 = 4, √25 = 5; same order, as promised.
- The *nearest-by-feature* sample (7, 7) — identical in X2 and 4 away in X1 — is "Bad" but only ranks 3rd; the two closer "Good" samples win the vote. With **k = 1** the answer is Good (sample (3,4)); with **k = 4** (all samples) it would be a **2–2 tie** — a live demonstration of why k should be odd ([[01_Nearest_Neighbor_Idea_and_Basic_Rule]], [[05_The_k_NN_Algorithm_Step_by_Step]]).
- Both features here are on a comparable 1–7 scale, so — unlike the movie example — no scaling problem arises ([[06_Worked_Example_Predicting_Movie_Genre]]).
- For k = 1 and k = 3 the answer is Good; this example is a clean walk-through of all five algorithm steps from [[05_The_k_NN_Algorithm_Step_by_Step]].

---

## 2) Simple English Explanation

**The situation:** A factory makes paper tissue and tests two things: how long it survives acid (**X1**) and how strong it is (**X2**). Four earlier samples were judged **Good** or **Bad** by people. Now there's a new tissue with X1 = 3 and X2 = 7. Is it Good or Bad — without surveying people again?

**Step 1 — Choose k = 3** (ask 3 neighbors).

**Step 2 — Measure how far the new tissue is from each old one.** To keep it quick, the slide skips the final square-root (the order of "closest to farthest" stays exactly the same). For each old sample: (acid gap)² + (strength gap)².

| Old sample (X1, X2) | Distance² | Judged |
|---|---|---|
| (7, 7) | 16 | Bad |
| (7, 4) | 25 | Bad |
| (3, 4) | 9 | Good |
| (1, 4) | 13 | Good |

**Step 3 — Rank from closest:** 9 (1st), 13 (2nd), 16 (3rd), 25 (4th). The top 3 are the neighbors. The (7, 4) sample is 4th, so it is **left out**.

**Step 4 — What did the 3 neighbors say?** Good, Good, Bad.

**Step 5 — Vote:** 2 Good vs 1 Bad → **the new tissue is Good.** ✅

Fun check: if we'd asked all 4 (k = 4) it would be 2 Good, 2 Bad — a tie! That's why we use an odd k like 3.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Situation:** Ek factory paper tissue banati hai aur do cheezein test karti hai: acid mein kitni der tikta hai (**X1**) aur kitna strong hai (**X2**). Pehle ke 4 samples ko logon ne **Good** ya **Bad** bola tha. Ab ek naya tissue aaya jiska X1 = 3 aur X2 = 7 hai. Bina dobara mehenga survey kiye bataao — Good hai ya Bad?

**Step 1 — K = 3 lo** (3 neighbors se poochho).

**Step 2 — Naye tissue se har purane sample ka distance nikalo.** Sir ne yahan **square distance** liya (square root nahi liya) kyunki wo tez hai aur "kaun paas, kaun door" ka order bilkul same rehta hai. Formula: (X1 ka gap)² + (X2 ka gap)².

| Purana sample (X1, X2) | Distance² | Label |
|---|---|---|
| (7, 7) | (7−3)² + (7−7)² = 16 + 0 = **16** | Bad |
| (7, 4) | (7−3)² + (4−7)² = 16 + 9 = **25** | Bad |
| (3, 4) | (3−3)² + (4−7)² = 0 + 9 = **9** | Good |
| (1, 4) | (1−3)² + (4−7)² = 4 + 9 = **13** | Good |

**Step 3 — Rank (paas se door):** 9 → 1st, 13 → 2nd, 16 → 3rd, 25 → 4th. Pehle 3 hi neighbors hain. (7, 4) ka rank 4 hai, isliye wo **include nahi hota** (slide mein "No" likha hai).

**Step 4 — 3 neighbors ne kya bola?** Good, Good, Bad.

**Step 5 — Vote:** 2 Good vs 1 Bad → **naya tissue Good hai ✅**

Bonus: agar k = 4 lete (sab 4 samples) to 2 Good aur 2 Bad — **tie** ho jata! Isiliye hum k odd (jaise 3) rakhte hain. Aur yahan dono features 1–7 ki similar range mein hain, to scaling ki problem nahi aayi (movie example mein aayi thi).
