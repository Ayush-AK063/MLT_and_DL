# Topic 6: Choosing k: SSE and the Elbow Method

Source: Lecture 23, slides 17–25 ("How to determine correct number of clusters (k)?"; the 16-point scatter with handwritten "Elbow method"; the same data split into k = 2, k = 4 and k = 6 clusters with "K? → Elbow method"; "SSE = Sum of Squared Errors" with SSE₁, SSE₂ and SSE = SSE₁ + SSE₂ + … + SSE_k, handwritten "k = 3, 4, 6"; the SSE-vs-K plot with the elbow at K = 4; "Elbow Technique" with the bent-arm cartoon). Enriched with our own scikit-learn runs (verification) and general knowledge.

---

## 1) Technical Explanation

### The question (slide 17)

"How to determine correct number of clusters (k)?" k-Means needs k as input ([[03_K_Means_Definition_Objective_and_History]]). With unlabelled data there is no ground truth to tell us the right k.

### Different k, different answers (slides 18–21)

The same 16 points from the walkthrough ([[05_K_Means_Visual_Walkthrough_k_Equals_2]]) are clustered three ways. Slide 18 is the raw scatter, titled "Elbow method".

| Slide | k | Clusters drawn (number of points) |
|---|---|---|
| 19 | 2 | red group (8) and green group (8), the result of the walkthrough |
| 20 | 4 | C1 left group (5), C2 upper group (5), C3 right group (3), C4 diagonal tail (3) |
| 21 | 6 | C1 (1, a single point), C2 (4), C3 (3), C4 (2), C5 (3), C6 (3), annotated "K? → Elbow method" |

Every split looks "valid", because k-Means will always return exactly k clusters. Going from k = 4 to k = 6 just chops natural groups into smaller pieces, and one cluster is a single point. We need a number that measures quality.

### SSE: Sum of Squared Errors (slides 22–23)

For each cluster j with centroid c_j, add up the squared distances of its points to c_j:

  **SSE_j = Σ_{x_i ∈ C_j} dist(x_i, c_j)²**

Then add these over all clusters:

  **SSE = SSE₁ + SSE₂ + … + SSE_k**

This is exactly the k-Means objective J, called *inertia* in scikit-learn. The slide's figure draws dashed lines from every point to its own star, and each dashed line is one term of the sum. The handwriting "k = 3, 4, 6" means: compute this SSE for each candidate k.

*Notation note.* The slide writes SSE₁ = Σ_{i=0}^{n} dist(x_i − c₁)² and SSE₂ = Σ_{i=0}^{m} dist(x_i − c₂)². Read this as "sum over the n points of cluster 1 (and the m points of cluster 2) of the squared distance between x_i and c". Strictly, the index should run from i = 1, and the distance should be written dist(x_i, c) rather than dist(x_i − c).

### The elbow plot (slides 24–25)

Plot SSE (y-axis) against K = 1, 2, …, 11 (x-axis). The handwritten notes are "Sum of Squared Error", "Elbow Method", "k = 4" and "Clusters".

- **SSE always goes down as k grows.** More centroids means every point can sit closer to one. At k = n every point is its own centroid and SSE = 0. So "smallest SSE" can't be the rule, because it would always pick k = n.
- **Look for the "elbow".** At first SSE drops steeply, because each extra centroid splits a real, spread-out group. After the true number of groups, extra centroids only split already-tight groups, and SSE flattens out. The bend between steep and flat is the elbow.
- On slide 24 the steep part runs K = 1 → 4 and the curve is almost flat from K = 4 to 11. So **k = 4** is chosen, circled in red with "k = 4" written beside it. That matches the four natural groups in slide 20.
- Slide 25 ("Elbow Technique") shows the same curve next to a cartoon of a bent arm: the optimum k is where the curve bends like an elbow.

### Verification: our own runs (not on the slides)

The slide plot has no numbers, so we ran scikit-learn `KMeans(n_init=10)` ourselves.

**(a) 300 points in 4 well-separated blobs** (`make_blobs(centers=4, cluster_std=0.8, random_state=42)`):

| k | 1 | 2 | 3 | **4** | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| SSE | 19780.3 | 9211.2 | 1919.4 | **362.5** | 327.8 | 294.3 | 261.3 | 236.9 | 208.0 | 185.7 |
| drop vs previous | — | 53.4% | 79.2% | 81.1% | 9.6% | 10.2% | … | | | |

The curve drops sharply up to k = 4 and then barely moves. The elbow is at **k = 4**, the true number of blobs.

**(b) The 8-point dataset from this lecture's worked example** ([[08_Worked_Example_Eight_Points_Manhattan_Distance]]):

| k | 1 | 2 | **3** | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| SSE | 100.75 | 51.47 | **14.33** | 8.67 | 3.67 | 2.00 | 1.00 |
| absolute drop | — | 49.3 | 37.1 | 5.7 | 5.0 | 1.7 | 1.0 |

The big gains stop after k = 3, so the elbow is at **k = 3**, which is the k the exam question uses. The k = 1 value is easy to check by hand. The overall mean is (4.375, 5.875). Σx² − 8·4.375² = 199 − 153.125 = 45.875, and Σy² − 8·5.875² = 331 − 276.125 = 54.875. Total: 100.75 ✔.

### Limitations of the elbow method

- The elbow is a **visual judgement**. On real data the curve is often smooth, with no clear bend, and different people pick different k.
- SSE depends on feature scales, so standardise the features first.
- SSE favours round, equal-sized clusters, which is k-Means' own bias.

For these reasons the instructor wrote two more principled alternatives on slide 25: **(1) the Silhouette Coefficient method** and **(2) the Gap statistic** ([[07_Silhouette_Coefficient_and_Gap_Statistic]]).

---

## 2) Simple English Explanation

**The problem (slide 17).** k-Means needs you to say how many groups (k) you want, but with unlabelled data nobody knows the right answer. How do we choose?

**Same dots, different k (slides 18–21).**
- **k = 2**: two groups of 8.
- **k = 4**: four natural-looking groups: the left bunch, the top bunch, a small right bunch and the diagonal tail.
- **k = 6**: six groups, including one "group" that is a single lonely dot.

k-Means will happily make *any* number of groups you ask for, so we need a score that tells us which choice is sensible.

**The score: SSE (slides 22–23).**
- For each group, draw a line from every dot to the group's centre (the star). Measure each line, square it, and add them up. That is the group's SSE.
- Add the SSEs of all groups to get the total SSE.
- Small SSE = tight groups. Big SSE = loose, spread-out groups.
- The teacher wrote "k = 3, 4, 6" because you work out this total for each k you're considering.

**Why not just pick the k with the smallest SSE?** Because SSE *always* gets smaller when you add more groups. If every dot were its own group, SSE would be exactly 0. That's useless.

**The elbow idea (slides 24–25).** Draw a graph with k along the bottom and SSE going up the side.
- At first the line falls steeply. Each new group splits a big, messy group, so the SSE drops a lot.
- After a certain point, extra groups just chop up groups that were already tight. The SSE hardly changes and the line goes almost flat.
- The point where steep turns into flat looks like a **bent arm's elbow**. That is the best k.
- On the slide it is **k = 4**, and that matches the 4 natural groups on slide 20.

**We checked it ourselves.**
- We made 300 computer-generated dots in 4 clear bunches and ran k-Means for k = 1 to 10.
  - SSE fell from 19,780 to 9,211 to 1,919 to **362** as k went from 1 to 4.
  - Then it only crawled: 328, 294, 261, …
  - The elbow is clearly at 4. ✔
- On the 8 points of the exam example, SSE goes 100.75 → 51.47 → **14.33** → 8.67 → 3.67 …
  - The big drops stop after k = 3, so the elbow says 3, the same k the exam question asks for.

**Weak points.**
- Sometimes the curve bends smoothly with no clear elbow, and people disagree on where it is.
- So the teacher wrote down two better-defined methods to learn next: the **Silhouette Coefficient** and the **Gap Statistic**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Problem (slide 17).** k-Means ko batana padta hai ki kitne groups (k) chahiye, par bina labels ke data mein sahi jawaab kisi ko nahi pata. To k kaise chunein?

**Wahi dots, alag k (slides 18–21).**
- **k = 2**: 8 aur 8 ke do groups.
- **k = 4**: chaar natural groups: left jhund (5), upar wala jhund (5), right ka chhota jhund (3), aur tirchhi poonchh (3).
- **k = 6**: chhe groups, jinmein ek "group" sirf ek akela dot hai (C1).

k-Means jitne groups maango utne bana deta hai, isliye hume ek score chahiye jo bataye kaunsa k sahi hai.

**Score: SSE, yaani Sum of Squared Errors (slides 22–23).**
- Har group ke har dot se uske centre (star) tak line kheencho, us line ki lambai ka square lo, aur sab jodo. Ye us group ka SSE hai: SSE_j = Σ dist(x_i, c_j)².
- Saare groups ka SSE jodo: SSE = SSE₁ + SSE₂ + … + SSE_k.
- SSE chhota hai to groups tight hain. SSE bada hai to groups bikhre hue hain.
- Teacher ne likha "k = 3, 4, 6", yaani har candidate k ke liye ye total nikaalo.
- (Slide pe notation thoda dheela hai: Σ_{i=0}^{n} aur dist(x_i − c) likha hai. Sahi tareeke se i = 1 se shuru hona chahiye aur dist(x_i, c) likhna chahiye. Matlab same hai.)

**Sabse kam SSE wala k kyun nahi?** Kyunki groups badhao to SSE *hamesha* ghatta hai. Har dot ka apna group bana do to SSE = 0. Ye bekaar answer hai.

**Elbow idea (slides 24–25).** Graph banao: neeche k (1 se 11) aur upar SSE.
- Shuru mein line tezi se girti hai, kyunki har naya group ek bade, bikhre group ko todta hai aur SSE bahut kam hota hai.
- Ek point ke baad naye groups sirf pehle se tight groups ko kaat-te hain. SSE lagbhag same rehta hai aur line seedhi (flat) ho jaati hai.
- Jahan tez girawat flat mein badalti hai, woh mudi hui baanh ki **kohni (elbow)** jaisi dikhti hai. Wahi best k hai.
- Slide pe ye **k = 4** hai (teacher ne circle kiya), jo slide 20 ke 4 natural groups se match karta hai.
- Slide 25 pe mude hue haath ka cartoon isi kohni ko dikhata hai.

**Humne khud check kiya (slides pe numbers nahi the).**
- **300 dots, 4 saaf jhund** (scikit-learn `make_blobs`):
  - SSE: k=1 → 19780, k=2 → 9211, k=3 → 1919, **k=4 → 362**, phir 328, 294, 261 …
  - k = 4 tak har baar 50–80% girawat, phir sirf ~10%. Elbow = 4 ✔.
- **Exam wale 8 points** (Topic 8):
  - SSE: 100.75 → 51.47 → **14.33** → 8.67 → 3.67 → 2 → 1.
  - Girawat: 49.3, 37.1, phir sirf 5.7, 5.0 … Elbow = **3**, wahi k jo sawaal mein diya hai ✔.
  - k = 1 ka SSE haath se: mean = (4.375, 5.875). x-part = 199 − 8×4.375² = 45.875 aur y-part = 331 − 8×5.875² = 54.875. Total = **100.75** ✔.

**Kamzoriyan.**
- Elbow aankh se dekh ke decide hota hai. Kabhi curve smooth hota hai aur saaf kohni nahi dikhti.
- Features ka scale SSE ko badal deta hai, isliye pehle scaling karo.

Isliye teacher ne slide 25 pe do aur methods likhe: **(1) Silhouette Coefficient** aur **(2) Gap Statistic**. Ye agle topic mein hain.
