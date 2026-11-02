# Topic 7: Beyond the Elbow: Silhouette Coefficient and Gap Statistic

Source: Lecture 23, slide 25 (handwritten beside the "Elbow Technique" plot: "① Silhouette Coefficient method", "② Gap statistic"). The slide only *names* these two methods. Everything else here is research enrichment: Rousseeuw (1987) for the silhouette; Tibshirani, Walther & Hastie (2001, *J. R. Statist. Soc. B* 63(2):411–423) for the gap statistic; scikit-learn documentation. All numbers below come from our own computations.

---

## 1) Technical Explanation

### Why we need more than the elbow

The elbow method ([[06_Choosing_k_SSE_and_the_Elbow_Method]]) only looks at **cohesion**, i.e. how tight each cluster is. And it needs a human to spot the bend. The two methods the instructor named give a **number to optimise**:

- The **silhouette** also measures **separation**, i.e. how far each cluster is from its neighbours.
- The **gap statistic** compares the clustering against what you would get from data that has **no** clusters at all.

### (1) Silhouette Coefficient (Rousseeuw, 1987)

For each point i in cluster A:

- **a(i)** = the average distance from i to the *other* points in its own cluster A. This measures cohesion: smaller is better.
- **b(i)** = the smallest, over every other cluster B, of the average distance from i to the points of B. In other words, b(i) is the average distance to the **nearest neighbouring cluster**. This measures separation: larger is better.
- The silhouette of point i is

  **s(i) = (b(i) − a(i)) / max{a(i), b(i)}**,  so −1 ≤ s(i) ≤ 1.

  If i is the only point in its cluster, s(i) is set to 0.

**Interpretation.**
- s ≈ 1: the point is well inside its cluster and far from others.
- s ≈ 0: the point lies on the border between two clusters.
- s < 0: the point is probably in the wrong cluster.

The **mean silhouette** over all points scores the whole clustering. **Choose the k with the highest mean silhouette.**

**Worked check on the lecture's 8 points.** We use the final k = 3 clustering of [[08_Worked_Example_Eight_Points_Manhattan_Distance]] and Euclidean distances: C1 = {A1, A4, A8}, C2 = {A3, A5, A6}, C3 = {A2, A7}.

*Point A8 (4, 9), in C1:*
- a = mean(d(A8,A1), d(A8,A4)) = mean(2.236, 1.414) = **1.825**
- average distance to C2 = (6.403 + 5.000 + 5.385)/3 = 5.596
- average distance to C3 = (4.472 + 7.616)/2 = 6.044
- b = min(5.596, 6.044) = **5.596**
- s(A8) = (5.596 − 1.825)/5.596 = **0.674**. A8 is well clustered.

*Point A2 (2, 5), in C3:*
- a = d(A2,A7) = **3.162**
- average distance to C1 = (5 + 4.243 + 4.472)/3 = 4.572
- average distance to C2 = (6.083 + 5 + 4.123)/3 = 5.069
- b = **4.572**
- s(A2) = (4.572 − 3.162)/4.572 = **0.308**. A2 is a borderline point, about as close to C1 as to its own partner A7.

*All eight points* (verified with `sklearn.metrics.silhouette_samples`):

| | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
|---|---|---|---|---|---|---|---|---|
| s(i) | 0.553 | 0.308 | 0.743 | 0.408 | 0.729 | 0.641 | 0.510 | 0.674 |

The mean is **0.571**.

*Mean silhouette for each k* (best k-Means run for each k):

| k | 2 | **3** | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| 8 points | 0.388 | **0.571** | 0.472 | 0.367 | 0.159 | 0.037 |

The maximum is at k = 3, which agrees with the elbow. On the 300-point, 4-blob data of Topic 6 the mean silhouette for k = 2…6 is 0.603, 0.778, **0.834**, 0.723, 0.587, with the maximum at k = 4 ✔.

**Cost.** Computing the silhouette needs all pairwise distances, O(n²), so it gets slow for very large n. In scikit-learn it is `silhouette_score(X, labels)`.

### (2) Gap Statistic (Tibshirani, Walther & Hastie, 2001)

**Idea.** Even random, structureless data has an SSE that falls as k grows. So compare the real data's within-cluster dispersion W_k with what you'd expect under a **null reference distribution** that has no clusters, typically uniform over the data's bounding box.

  **Gap(k) = E*[log W_k^ref] − log W_k**

- W_k is the pooled within-cluster sum of squares, i.e. the SSE.
- E* is estimated by clustering **B** reference data sets (e.g. B = 20 to 100) and averaging their log W_k.
- s_k = sd_k · √(1 + 1/B) is the simulation standard error.

**Rule ("1-standard-error"):** choose the **smallest k with Gap(k) ≥ Gap(k+1) − s_{k+1}**. A large gap means the real data is much more clustered than random noise.

**Our run** (4-blob data, B = 20 uniform reference sets):

| k | 1 | 2 | 3 | **4** | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Gap(k) | −0.156 | 0.040 | 1.196 | **2.431** | 2.332 | 2.242 | 2.190 |
| s_k | 0.030 | 0.037 | 0.029 | 0.042 | 0.039 | 0.025 | 0.032 |

At k = 4: Gap(4) = 2.431 ≥ Gap(5) − s₅ = 2.332 − 0.039 = 2.293 ✔. No smaller k satisfies the rule, so the gap statistic picks **k = 4**.

**Advantages.** Unlike the elbow and the silhouette, the gap statistic can also answer "**k = 1**", meaning there is no real cluster structure. That happens when the real data looks no more clustered than uniform noise.

### Comparison

| Method | Measures | Rule | Can say "no clusters"? | Cost |
|---|---|---|---|---|
| Elbow | cohesion (SSE) | visual bend | no | cheap |
| Silhouette | cohesion **and** separation | max mean s | no (needs k ≥ 2) | O(n²) |
| Gap statistic | SSE vs random reference | smallest k with Gap(k) ≥ Gap(k+1) − s_{k+1} | **yes** | B extra clusterings per k |

---

## 2) Simple English Explanation

On slide 25 the teacher wrote two more ways to choose k besides the elbow. The slide just names them, so here is what they are.

**Why bother?** The elbow only checks how tight the groups are, and you have to "eyeball" the bend. These two give an actual number to pick from.

**(1) Silhouette Coefficient: "Am I in the right group?"**

Every point asks itself two questions:
- **a** = "On average, how far am I from the others in *my own* group?" Small is good.
- **b** = "On average, how far am I from the points of the *nearest other* group?" Big is good.

Its score is **s = (b − a) / (the bigger of a and b)**, which always lies between −1 and +1:
- Close to **+1**: I'm snug in my group and far from the others. 👍
- Around **0**: I'm sitting on the fence between two groups.
- **Negative**: I'm probably in the wrong group.

Average the score over all points and choose the k with the **highest average**.

**Example with the exam's 8 points** (final groups C1 = {A1, A4, A8}, C2 = {A3, A5, A6}, C3 = {A2, A7}):
- **Point A8 (4, 9).**
  - Its group-mates A1 and A4 are 2.236 and 1.414 away, so a = 1.825.
  - The nearest other group is C2, whose points are on average 5.596 away, so b = 5.596.
  - s = (5.596 − 1.825)/5.596 = **0.67**. A8 is clearly in the right place.
- **Point A2 (2, 5).**
  - Its only group-mate A7 is 3.162 away, so a = 3.162.
  - The nearest other group (C1) is on average 4.572 away, so b = 4.572.
  - s = (4.572 − 3.162)/4.572 = **0.31**. A2 is fine, but close to the fence.
- The average over all 8 points is **0.571**. Trying other k gives 0.388 (k=2), 0.472 (k=4), 0.367 (k=5), so **k = 3 wins**, the same as the elbow.

**(2) Gap Statistic: "Is this better than random?"**
- Even totally random dots get a smaller SSE when you add more groups. So the gap statistic asks: *how much tighter are my real groups than the groups you'd get from random dots spread evenly over the same area?*
- That difference (on a log scale) is the **gap**.
- Pick the smallest k after which the gap stops growing meaningfully, allowing for a little random wobble (the "standard error").
- On the 4-bunch test data the gap climbed −0.16, 0.04, 1.20, **2.43** and then slipped to 2.33, 2.24 … So it picks **k = 4** ✔.
- A nice bonus: if the data has **no real groups at all**, the gap statistic can tell you so (k = 1). The other methods can't.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Slide 25 pe teacher ne elbow ke alawa k chunne ke do aur tareeke likhe: **① Silhouette Coefficient** aur **② Gap statistic**. Slide pe sirf naam hain, details yahan hain.

**Kyun chahiye?** Elbow sirf groups ki tightness dekhta hai, aur kohni aankh se dhoondhni padti hai. Ye dono methods ek pakka number dete hain.

**① Silhouette Coefficient: "Kya main sahi group mein hoon?"**

Har point khud se do sawaal poochta hai:
- **a(i)** = apne hi group ke baaki points se meri average doori. Kam ho to achha.
- **b(i)** = sabse paas wale *doosre* group ke points se meri average doori. Zyada ho to achha.

Score: **s(i) = (b − a) / max(a, b)**, jo hamesha −1 se +1 ke beech hota hai.
- **+1 ke paas**: apne group mein aaram se baitha hai, doosron se door hai 👍.
- **0 ke paas**: do groups ki boundary (deewar) pe baitha hai.
- **Negative**: shayad galat group mein hai.
- Agar point apne group mein akela hai to s = 0 maan lete hain.

Saare points ka average lo, aur jis k pe **average sabse zyada** ho, wahi k chuno.

**Exam wale 8 points pe example** (final groups: C1 = {A1, A4, A8}, C2 = {A3, A5, A6}, C3 = {A2, A7}, Euclidean distance):
- **A8 (4, 9).**
  - Group-mates A1 aur A4 se doori 2.236 aur 1.414 hai, to a = (2.236 + 1.414)/2 = **1.825**.
  - C2 se average doori (6.403 + 5 + 5.385)/3 = 5.596. C3 se (4.472 + 7.616)/2 = 6.044. Chhoti wali lo: b = **5.596**.
  - s = (5.596 − 1.825)/5.596 = **0.674**. Bilkul sahi group mein hai.
- **A2 (2, 5).**
  - Sirf ek group-mate A7 hai, 3.162 door, to a = **3.162**.
  - C1 se average (5 + 4.243 + 4.472)/3 = 4.572, C2 se 5.069. To b = **4.572**.
  - s = (4.572 − 3.162)/4.572 = **0.308**. Theek hai, par boundary ke kareeb hai.
- Saare 8 points ke scores: 0.553, 0.308, 0.743, 0.408, 0.729, 0.641, 0.510, 0.674. Average = **0.571**.
- Doosre k ke averages: k=2 → 0.388, **k=3 → 0.571**, k=4 → 0.472, k=5 → 0.367. **k = 3 jeeta**, elbow wala hi jawaab ✔.
- 4-jhund wale 300-point data pe silhouette k = 4 pe sabse zyada (0.834) aaya ✔.
- Kamzori: har point ka har point se distance chahiye (O(n²)), to bahut bade data pe slow hai.

**② Gap Statistic: "Kya ye random se behtar hai?"** (Tibshirani, Walther, Hastie, 2001)
- Bilkul random dots mein bhi groups badhane se SSE ghatta hai. To gap statistic poochta hai: *mere asli groups utne hi area mein barabar faile random dots ke groups se kitne zyada tight hain?*
- Formula: **Gap(k) = (random data ka average log SSE) − (asli data ka log SSE)**. Random data ko B baar (jaise 20) banake cluster karte hain.
- Rule: **sabse chhota k jahan Gap(k) ≥ Gap(k+1) − s(k+1)**. Yahan s random wobble ka standard error hai.
- Humare run mein (4 jhund, B = 20): Gap = −0.156, 0.040, 1.196, **2.431**, 2.332, 2.242, 2.190.
  - k = 4 pe check: 2.431 ≥ 2.332 − 0.039 = 2.293 ✔. Usse chhota koi k rule pass nahi karta, to **k = 4**.
- Bonus: agar data mein **koi asli group hai hi nahi**, to gap statistic k = 1 bol sakta hai. Elbow aur silhouette ye nahi kar sakte.

**Teen methods ek line mein:**
- Elbow: SSE ka mod dekho (sasta, par aankh se).
- Silhouette: tightness + doori dono, max average lo.
- Gap: random se tulna, aur "koi cluster nahi" bhi bata sakta hai.
