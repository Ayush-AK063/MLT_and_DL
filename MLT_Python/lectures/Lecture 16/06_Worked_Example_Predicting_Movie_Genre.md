# Topic 6: Worked Example — Predicting a Movie's Genre ("Barbie")

Source: Lecture 16, slides 13–16 (dataset slide, the handwritten Euclidean-distance derivation slide, "Step 1: Calculate Distances / Step 2 / Step 3" with the instructor's red-ink answers). Independently re-verified numerically; the scaling problem hidden in this example is analysed as an extension.

---

## 1) Technical Explanation

**Problem (slide 13).** Predict the **genre** of the movie **"Barbie"** with **IMDB rating = 7.4** and **duration = 114** (minutes), given four labelled movies:

| Movie | IMDB Rating (x₁) | Duration (x₂) | Genre |
|---|---|---|---|
| Mission Impossible | 8.0 | 160 | Action |
| Gadar 2 | 6.2 | 170 | Action |
| Rocky & Rani | 7.2 | 168 | Comedy |
| OMG 2 | 8.2 | 155 | Comedy |

**Distance formula (slide 14, handwritten).** For points P(x₁, y₁) and Q(x₂, y₂) in the 2-D plane (rating on one axis, duration on the other):

d(P, Q) = √( (x₂ − x₁)² + (y₂ − y₁)² )

**Step 1 — Euclidean distance from Barbie (7.4, 114) to each movie (slide 15).**

| Movie | Computation | Exact | Slide's (rounded) |
|---|---|---|---|
| Mission Impossible (8.0, 160) | √(0.6² + 46²) = √(0.36 + 2116) = √2116.36 | 46.004 | **46** |
| Gadar 2 (6.2, 170) | √(1.2² + 56²) = √(1.44 + 3136) = √3137.44 | 56.013 | **56** |
| Rocky & Rani (7.2, 168) | √(0.2² + 54²) = √(0.04 + 2916) = √2916.04 | 54.0004 | **54** |
| OMG 2 (8.2, 155) | √(0.8² + 41²) = √(0.64 + 1681) = √1681.64 | 41.008 | **41** |

All four values match the slide's red-ink answers after rounding (re-verified).

**Step 2 — Select the K nearest neighbors.** Sorted ascending: **41 (OMG 2, Comedy) < 46 (Mission Impossible, Action) < 54 (Rocky & Rani, Comedy) < 56 (Gadar 2, Action)**.

- **k = 1:** nearest is OMG 2 → **Comedy** (the circled "41" on the slide).
- **k = 3:** the three smallest are 41, 46, 54 (the slide writes "41, 46, 54") → labels **Comedy, Action, Comedy**.

**Step 3 — Majority voting (classification).** For k = 3: Comedy 2, Action 1 → **Comedy**. The slide's final answer: **Barbie → Comedy** (both k = 1 and k = 3 agree).

(The instructor's "A, C, C" note next to the 54 row tallies the three chosen neighbors' genres: Action, Comedy, Comedy.)

**⚠️ Hidden problem: the result is decided almost entirely by duration.** Look at the distances: the rating difference contributes at most 1.2² = 1.44 to a squared distance, while the duration difference contributes 41² = 1681 to 56² = 3136. The rating is practically ignored — the ranking above is *identical* to ranking movies by |duration − 114| alone. That is a **feature-scale problem** ([[04_Distance_Metrics]], [[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]]).

**Extension (our check, not on the slide): min–max scaling.** Scale each feature to 0–1 using the training range (rating 6.2–8.2, duration 155–170). Barbie becomes (0.6, −2.733) — note it lies *outside* the training range because 114 min is shorter than every training movie — and distances become:

| Movie | Scaled distance |
|---|---|
| OMG 2 (Comedy) | 2.762 |
| Mission Impossible (Action) | 3.081 |
| Rocky & Rani (Comedy) | 3.601 |
| Gadar 2 (Action) | 3.781 |

The order is unchanged, so **k = 1 and k = 3 still give Comedy**. The conclusion survives here, but only because all four training durations are far above Barbie's; in general scaling can change the answer. Also, a 4-movie training set is far too small to trust — this is a teaching toy. (Note too that Barbie lies far from *every* training movie, which is a warning sign that all neighbors are poor matches.)

**A sanity check on K.** With N = 4, the rule k ≈ √N gives 2 — even, so use 1 or 3 ([[03_Issues_and_Choosing_the_Value_of_K]]).

---

## 2) Simple English Explanation

**The question:** We know four movies and their genres. A new movie, "Barbie," scores 7.4 stars and runs 114 minutes. Is it Action or Comedy?

**Idea:** Put each movie as a dot on a graph (rating across, length up). Find which known movies are **nearest** to Barbie's dot and copy their genre.

**Measuring distance** (the straight-line rule): take the rating gap and the length gap, square both, add them, take the square root.

| Movie | Rating gap | Length gap | Distance |
|---|---|---|---|
| Mission Impossible (Action) | 0.6 | 46 | ≈ 46 |
| Gadar 2 (Action) | 1.2 | 56 | ≈ 56 |
| Rocky & Rani (Comedy) | 0.2 | 54 | ≈ 54 |
| OMG 2 (Comedy) | 0.8 | 41 | ≈ 41 |

**Closest first:** OMG 2 (41), Mission Impossible (46), Rocky & Rani (54), Gadar 2 (56).

- Ask **1 neighbor** (k = 1): OMG 2 → **Comedy**.
- Ask **3 neighbors** (k = 3): OMG 2 (Comedy), Mission Impossible (Action), Rocky & Rani (Comedy) → 2 Comedy vs 1 Action → **Comedy**.

**Answer: Barbie is predicted to be Comedy.**

**A catch:** look at the "Rating gap" column — it's tiny (0.2 to 1.2) compared to the "Length gap" (41 to 56). Minutes are such big numbers that they completely **drown out** the star rating. So really, the answer was chosen only by movie length! It's like comparing people by "height in millimetres" and "age in years" — millimetres will dominate. The proper fix is to **rescale both to the same range (0 to 1)** first. We tried that: the order stayed the same here, so the answer is still Comedy — but you can't rely on that always.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal:** Humare paas 4 movies hain jinki genre pata hai. Ek nayi movie "Barbie" hai — rating 7.4, duration 114 minute. Ye Action hai ya Comedy?

**Idea:** Har movie ko graph par ek dot samjho (ek axis par rating, dusre par duration). Dekho Barbie ke dot ke **sabse paas** kaun si movies hain aur unki genre copy kar lo.

**Distance ka formula (seedhi line):** rating ka gap aur duration ka gap lo, dono ka square, jodo, phir square root.

| Movie | Rating gap | Duration gap | Distance |
|---|---|---|---|
| Mission Impossible (Action) | 0.6 | 46 | ≈ **46** |
| Gadar 2 (Action) | 1.2 | 56 | ≈ **56** |
| Rocky & Rani (Comedy) | 0.2 | 54 | ≈ **54** |
| OMG 2 (Comedy) | 0.8 | 41 | ≈ **41** |

Jaise: Mission Impossible ke liye √(0.6² + 46²) = √(0.36 + 2116) = √2116.36 ≈ 46.

**Paas se door ka order:** OMG 2 (41) → Mission Impossible (46) → Rocky & Rani (54) → Gadar 2 (56).

- **k = 1:** sabse paas OMG 2 → **Comedy**.
- **k = 3:** OMG 2 (Comedy), Mission Impossible (Action), Rocky & Rani (Comedy) → 2 Comedy, 1 Action → **Comedy**. (Sir ke "A, C, C" note ka matlab yahi hai: Action, Comedy, Comedy.)

**Final answer: Barbie = Comedy ✅** (k=1 aur k=3 dono mein same).

**Ek chhupi hui problem ⚠️:** "Rating gap" column dekho — bahut chhota (0.2 se 1.2) hai, jabki "Duration gap" bahut bada (41 se 56). Matlab minutes ke bade numbers ne rating ko **dabaa diya** — answer sirf duration se tay hua, rating ka koi role hi nahi raha! Ye waisa hi hai jaise kisi ko "height millimetre mein" aur "age saal mein" se compare karo — millimetre hi jeet jayega. Iska ilaaj: dono features ko pehle **same range (0 se 1)** mein scale karo. Humne scale karke bhi check kiya — order wahi raha, to yahan answer Comedy hi rahta hai. Lekin hamesha aisa hoga ye zaroori nahi, isliye k-NN se pehle **feature scaling** zaroor karo.

Aur 4 movies ka data bahut kam hai — ye sirf samjhane wala chhota example hai.
