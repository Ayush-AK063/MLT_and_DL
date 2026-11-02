# Topic 9: k-Means in Practice: Limitations, k-means++ and scikit-learn

Source: Research enrichment, not on the slides. It builds on slides 3–4 (partitioning methods find "spherical" clusters), slide 6 (random initial centroids) and slide 8 ("K? free parameter"). References: Arthur & Vassilvitskii, "k-means++: The Advantages of Careful Seeding" (SODA 2007); scikit-learn `KMeans` documentation (v1.9.1, run locally); Hartigan & Wong (1979). All experiment numbers are from our own runs.

---

## 1) Technical Explanation

### Strengths

- **Simple and fast.** Each iteration is O(n·k·d), and convergence usually takes few iterations. It scales to millions of points, and the mini-batch variant scales further.
- **Guaranteed to converge**, because the SSE never increases ([[04_K_Means_Algorithm_Steps]]).
- **Easy to interpret.** Each cluster is summarised by one prototype, its centroid.
- **Widely used as a building block:** vector quantisation, image colour compression, initialising Gaussian mixture models (EM), and feature engineering.

### Limitations (and how they are handled)

| Limitation | Why it happens | Remedy |
|---|---|---|
| **k must be given** (slide 8: "free parameter") | the objective always improves with larger k | elbow, silhouette, gap statistic ([[06_Choosing_k_SSE_and_the_Elbow_Method]], [[07_Silhouette_Coefficient_and_Gap_Statistic]]) |
| **Sensitive to the initial centroids → local optima** | Lloyd's iteration is a greedy descent | multiple restarts (`n_init`), **k-means++** seeding |
| **Assumes convex, roughly spherical, similar-size clusters** (slide 4: "clusters of spherical shape") | boundaries are perpendicular bisectors, so clusters are convex Voronoi cells ([[05_K_Means_Visual_Walkthrough_k_Equals_2]]) | density-based methods (DBSCAN), spectral clustering, Gaussian mixtures |
| **Sensitive to outliers** | the mean is pulled by extreme values, and the error is squared | k-medoids / PAM ([[02_Taxonomy_of_Clustering_Techniques]]), remove outliers first |
| **Sensitive to feature scale** | Euclidean distance is dominated by large-range features | standardise / normalise first ([[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]] from Lecture 16) |
| **Numeric data only** (slide 5) | a mean needs numbers | k-modes for categorical data, one-hot encoding |
| **Hard assignment** | each point belongs to exactly one cluster | fuzzy c-means, Gaussian mixture (soft) |
| **High dimensions** | distances become less informative (curse of dimensionality) | reduce dimension first, e.g. PCA ([[01_Dimensionality_Reduction_and_Curse_of_Dimensionality]] from Lecture 10) |

### Experiment 1: initialisation really matters (the lecture's 8 points, k = 3)

We ran k-Means **200 times**, each time with a single random start (`n_init=1`). We counted which final SSE each run reached.

| Initialisation | final SSE = 14.333 (global best) | worse local optima (45.8, 47.1, 47.3, 56.4, 58.7) |
|---|---|---|
| `init='random'` (k random data points, exactly as slide 6, step 1) | **161 / 200 (80.5%)** | 39 / 200 |
| `init='k-means++'` | **198 / 200 (99%)** | 2 / 200 (all at 45.8) |

So even on 8 points, about 1 random start in 5 gets stuck in a clearly worse clustering. The slide's given starting centres (A1, A4, A7) happen to lead to the global optimum ([[08_Worked_Example_Eight_Points_Manhattan_Distance]]).

On a harder case (1,000 points, 10 blobs, k = 10, 50 single-start runs each):

- **Random seeding:** mean SSE 1699.8, worst 9806.8, and only 4% of runs within 1% of the best.
- **k-means++ seeding:** mean SSE 499.2, worst 661.9, and 30% of runs within 1% of the best.
- The best SSE found was 467.8 either way.

### k-means++ seeding (Arthur & Vassilvitskii, 2007)

1. Choose the first centre uniformly at random from the data points.
2. For every point x, compute D(x), the distance to the nearest centre already chosen.
3. Choose the next centre at random, with probability proportional to **D(x)²** ("D² weighting"). Far-away points are therefore likely to become centres.
4. Repeat steps 2–3 until k centres are chosen. Then run normal Lloyd iterations.

**Guarantee:** the expected SSE is within an **O(log k)** factor of the optimum. This is the default seeding in scikit-learn.

### Experiment 2: non-convex shapes

On the "two moons" dataset (300 points, two interleaved crescents) we compared each method's clusters with the true moon labels:

- **k-Means (k = 2):** agreement score (Adjusted Rand Index) **0.24**. It cuts the moons with a straight line.
- **DBSCAN (ε = 0.3, MinPts = 5):** ARI **1.00**, a perfect recovery.

This is the slide-4 statement in action: partitioning methods find spherical clusters, while density-based methods "can find arbitrarily shaped clusters".

### k-Means in scikit-learn

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
X_scaled = StandardScaler().fit_transform(X)   # usually advisable; skipped below to match the slides

km = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=0)
labels = km.fit_predict(X)
print(labels)               # [1 2 0 1 0 0 2 1]  -> {A3,A5,A6}, {A1,A4,A8}, {A2,A7}
print(km.cluster_centers_)  # [[7, 4.333], [3.667, 9], [1.5, 3.5]]
print(km.inertia_)          # 14.333  (= SSE)
km.predict([[3, 3]])        # assign a NEW point to the nearest centroid
```

This output was verified by our run. scikit-learn reaches the same final clusters as our hand iteration. The cluster *numbers* are arbitrary, because clusters have no inherent order.

**Key parameters** (scikit-learn 1.9.1 defaults):

- `n_clusters = 8`
- `init = 'k-means++'`
- `n_init = 'auto'`: 1 run with k-means++, 10 runs with `'random'`
- `max_iter = 300`
- `tol = 1e-4`: relative tolerance on centroid movement
- `algorithm = 'lloyd'`: `'elkan'` uses the triangle inequality to skip distance computations

Note that scikit-learn's `KMeans` **always uses Euclidean distance**. A Manhattan-distance version like the slide example would need custom code or k-medoids/k-medians. Related classes are `MiniBatchKMeans` for large data and `sklearn.metrics.silhouette_score`. In R, the default `kmeans()` uses the **Hartigan–Wong** algorithm mentioned on slide 5.

### k-Means vs k-NN: a frequent confusion

| | k-NN (Lecture 16) | k-Means (this lecture) |
|---|---|---|
| Type | supervised **classification/regression** | unsupervised **clustering** |
| Meaning of k | number of **neighbours** that vote | number of **clusters** |
| Training | none ("lazy": store the data) | iterative: learn k centroids |
| Prediction for a new x | majority label of its k nearest training points | index of the nearest centroid |

([[03_Issues_and_Choosing_the_Value_of_K]] from Lecture 16.)

---

## 2) Simple English Explanation

**What k-Means is good at.**
- It is simple, quick even on huge data, always finishes, and its answer is easy to explain: "these are the k typical points (centres) and everyone belongs to the nearest one".
- It is used for things like reducing a photo to 16 colours, grouping customers, or as a first step for fancier methods.

**Where it struggles.**
1. **You must choose k.** Use the elbow, silhouette or gap statistic to help.
2. **The starting centres matter.**
   - We tried the lecture's 8 points 200 times with random starting centres. About **4 in 5 runs** found the best grouping (SSE 14.33). About **1 in 5** got stuck in a clearly worse one (SSE around 46–59).
   - With a smarter start called **k-means++**, 198 of 200 runs found the best answer.
   - Real software also runs several starts and keeps the best one.
3. **It only likes round blobs.**
   - Its borders are always straight lines between centres.
   - On two banana-shaped "moons" curled into each other, k-Means just cuts straight across them. It scored only 0.24 out of 1 for matching the real shapes.
   - DBSCAN, a density-based method from slide 3, found both moons perfectly (score 1.00).
4. **Outliers pull it around.** One extreme point drags the average. k-Medoids, which uses a real middle point, is more robust.
5. **Units matter.** If one feature is salary in rupees and another is age in years, salary dominates. Scale your features first.
6. **Numbers only.** For categories like colour or city, use k-Modes.
7. **Each point gets exactly one group.** For partial membership, use fuzzy c-means or Gaussian mixtures.

**How k-means++ picks smarter starting centres.**
- Pick the first centre at random from the data.
- For the next centre, prefer points that are **far** from the centres already chosen. The chance of being picked is proportional to the squared distance.
- Repeat until you have k centres. This spreads the starting centres out across the data.
- It is mathematically guaranteed to start within a reasonable factor of the best answer.

**Using it in Python.**
- `KMeans(n_clusters=3).fit_predict(X)` gives a group number for each point.
- `.cluster_centers_` gives the centres.
- `.inertia_` gives the SSE.
- `.predict(new_points)` puts new points into the nearest group.
- On the exam's 8 points it returns centres (7, 4.33), (3.67, 9), (1.5, 3.5) and SSE 14.33, exactly what we got by hand when we ran the iterations to the end.
- Note: Python's `KMeans` always uses straight-line distance, not the city-block distance of the exam question.

**Don't mix up k-NN and k-Means!**
- **k-NN** is a *classifier* (needs labels). Its k is "how many neighbours vote".
- **k-Means** is *clustering* (no labels). Its k is "how many groups to make".

---

## 3) Hinglish Explanation (Beginner-Friendly)

**k-Means ki taakat.**
- Simple hai, bade data pe bhi tez hai, hamesha rukta hai (converge karta hai), aur answer samajhna aasaan hai: "ye k centres hain, har point sabse paas wale centre ka hai".
- Photo ko 16 colours mein badalna, customers ke groups banana, ya Gaussian Mixture jaise bade methods ka pehla step, sab mein use hota hai.

**Kamzoriyan aur unke ilaaj.**
1. **k khud chunna padta hai.** Elbow, silhouette ya gap statistic se madad lo (Topic 6 aur 7).
2. **Starting centres se result badalta hai (local minimum).**
   - Humne lecture ke 8 points pe 200 baar random start se k-Means chalaya (bilkul slide 6, step 1 ki tarah).
   - **161/200 (80.5%)** baar best answer (SSE 14.33) mila. **39 baar** worse answer (SSE 45.8 se 58.7) pe atak gaya.
   - **k-means++** start ke saath **198/200** baar best answer mila.
   - Isliye software kai baar chalata hai aur best rakhta hai (`n_init`).
3. **Sirf gol (spherical/convex) jhund pasand karta hai.**
   - Borders hamesha seedhi lines hoti hain.
   - "Two moons" (do kele jaise ek-dusre mein ghuse aakaar) pe k-Means seedha beech se kaat deta hai, aur match score sirf **0.24** aaya.
   - **DBSCAN** (density-based, slide 3) ne dono moons perfect pakde, score **1.00**.
   - Yahi slide 4 kehta hai: partitioning → spherical clusters, density-based → koi bhi shape.
4. **Outliers centre ko kheench lete hain**, kyunki average aur squared error dono extreme value se prabhavit hote hain. Ilaaj: k-Medoids (PAM).
5. **Scale ka asar.** Salary (lakhs) aur age (saal) saath ho to salary haavi ho jayegi. Pehle StandardScaler lagao.
6. **Sirf numbers.** Categories (city, colour) ke liye k-Modes.
7. **Hard assignment.** Har point sirf ek group mein jata hai. Thoda-thoda membership chahiye to fuzzy c-means ya Gaussian mixture.
8. **Bahut zyada features** hon to distance kam kaam ka reh jata hai (curse of dimensionality). Pehle PCA lagao (Lecture 10).

**k-means++ kaise smart start deta hai.** (Arthur & Vassilvitskii, 2007)
1. Pehla centre data mein se random chuno.
2. Har point ki sabse paas wale chune hue centre se doori D(x) nikaalo.
3. Agla centre random chuno, par jiski doori zyada ho uske chune jaane ka chance zyada ho (probability ∝ D(x)²). Door wale points centre bante hain, aur centres phail jaate hain.
4. k centres hone tak repeat karo, phir normal k-Means chalao.

Guarantee: expected SSE best answer ke O(log k) guna ke andar hota hai. scikit-learn ka default yahi hai.

**Python (scikit-learn) mein.**
- `KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(X)` har point ka group number deta hai.
- `.cluster_centers_` centres deta hai, `.inertia_` SSE deta hai, aur `.predict(naye_points)` naye points ko nearest centre ka group deta hai.
- Exam ke 8 points pe answer: centres (7, 4.333), (3.667, 9), (1.5, 3.5), aur SSE = 14.333. Ye wahi hai jo humne haath se iterations aakhir tak chala ke paaya (Topic 8). Cluster numbers (0/1/2) ka koi matlab nahi, sirf naam hain.
- Defaults (version 1.9.1): `init='k-means++'`, `n_init='auto'`, `max_iter=300`, `tol=1e-4`, `algorithm='lloyd'`.
- Dhyan do: scikit-learn ka KMeans **hamesha Euclidean distance** use karta hai. Exam jaisa Manhattan wala version iske paas nahi hai.
- R ka default `kmeans()` Hartigan–Wong algorithm use karta hai, wahi naam jo slide 5 pe hai.

**k-NN vs k-Means, confuse mat hona!**
- **k-NN** (Lecture 16): supervised classifier, labels chahiye. k = kitne **padosi** vote karenge. Training mein kuch nahi seekhta (lazy).
- **k-Means**: unsupervised clustering, labels nahi chahiye. k = kitne **groups** banane hain. Training mein k centroids seekhta hai.
