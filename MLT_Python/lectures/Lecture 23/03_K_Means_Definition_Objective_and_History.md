# Topic 3: k-Means: Definition, Objective and History

Source: Lecture 23, slide 5 ("k-Means Algorithm" definition, with handwritten sketch "n objects h1, h2, h3 … → C1, C2, C3 … Distance … k no. of clusters … Moving stops") and slide 8 (two coloured clusters C1/C2 with the note "kmeans → Clusters; K? — free parameter"). Enriched with web research (history: Steinhaus 1956, Lloyd 1957/1982, Forgy 1965, MacQueen 1967, Hartigan & Wong 1979).

---

## 1) Technical Explanation

### Slide 5: the definition

The slide makes three statements:

- "k-Means clustering algorithm proposed by **J. Hartigan and M. A. Wong [1979]**."
- "Given a set of **n distinct objects**, the k-Means clustering algorithm partitions the objects into **k number of clusters** such that **intracluster similarity is high but the intercluster similarity is low**."
- "In this algorithm, **user has to specify k**, the number of clusters, and consider the objects are defined with **numeric attributes** and thus using any one of the distance metric to demarcate the clusters."

**The handwritten sketch.** It shows n objects **h1, h2, h3, …** with arrows labelled "Distance" going to **C1, C2, C3**. Next to it is "**k = no. of clusters**", with example memberships such as C1 = (h1, h2, h5), C2 = (h4, h3, h6), C3 = (h7, …). On the right it says "**Moving stops**": the algorithm ends when the centroids stop moving.

### Slide 8: k is a free parameter

The same scatter as slide 7, now coloured: red points are C1 and green points are C2. The instructor wrote "kmeans → **Clusters**" and "**K? — free parameter**". k-Means does not learn k. You must supply it, and choosing it well is a separate problem ([[06_Choosing_k_SSE_and_the_Elbow_Method]]).

### The formal objective

k-Means looks for a partition C₁,…,C_k with centroids μ₁,…,μ_k that minimises the **within-cluster sum of squared errors** (SSE). scikit-learn calls this *inertia*:

  **J = SSE = Σ_{j=1..k} Σ_{x ∈ C_j} ‖x − μ_j‖²**,  where μ_j = (1/|C_j|) Σ_{x ∈ C_j} x.

- **"High intra-cluster similarity"** means a small J: points are close to their own centroid.
- **Low inter-cluster similarity follows automatically.** The total scatter of the data is fixed, and it splits into within-cluster scatter plus between-cluster scatter. So minimising the within part maximises the between part.

**Why the mean?** For a fixed set of points, the vector c that minimises Σ‖x − c‖² is exactly their arithmetic mean. That is why the "cluster centre" in step 3 of the algorithm is the mean ([[04_K_Means_Algorithm_Steps]]). With **Manhattan** distance the minimiser per coordinate would be the **median** (that variant is called *k-medians*). The worked example in this lecture uses Manhattan distance for *assignment* but still uses the *mean* for the update ([[08_Worked_Example_Eight_Points_Manhattan_Distance]]).

**"Numeric attributes".** A mean only makes sense for numbers. Categorical data needs k-Modes ([[02_Taxonomy_of_Clustering_Techniques]]).

**Complexity.**
- Finding the exact global minimum of J is **NP-hard** in general.
- The standard algorithm is a fast heuristic. Each iteration costs **O(n·k·d)** for n points, k clusters and d features.
- It always converges, because J never increases. But it converges only to a **local** minimum that depends on the starting centroids ([[09_K_Means_Limitations_k_means_plus_plus_and_scikit_learn]]).

### History: who "proposed" k-Means? (correction to slide 5)

Web research gives this timeline:

| Year | Who | Contribution |
|---|---|---|
| 1956 | Hugo Steinhaus | first described the idea of partitioning by nearest centres |
| 1957 | Stuart Lloyd (Bell Labs) | the standard iterative algorithm, for pulse-code modulation; not published until **1982** |
| 1965 | Edward Forgy | the same batch method independently, hence "Lloyd–Forgy" |
| 1967 | James MacQueen | coined the name **"k-means"**; online update version |
| 1979 | **J. A. Hartigan & M. A. Wong** | "Algorithm AS 136: A K-Means Clustering Algorithm", *Applied Statistics* 28(1). A more efficient variant that moves single points when that lowers SSE. It is the default `kmeans()` in R. |

So **Hartigan & Wong (1979) did not originate k-Means**. They published a well-known, efficient *version* of it. The step-by-step procedure on the next slide, which assigns all points and then recomputes all means, is actually **Lloyd's algorithm**. The "[1957, 1967]" years on slide 3 point to Lloyd and MacQueen, which agrees with this timeline.

---

## 2) Simple English Explanation

**What k-Means does, in one sentence.** You give it **n** data points and a number **k**, and it splits the points into **k groups** so that points in the same group are close together and the groups are far apart.

**Slide 5, plainly.**
- The slide says k-Means was proposed by Hartigan and Wong in 1979.
- It takes **n** objects and makes **k** clusters with "high intra-cluster similarity" (members of one group are alike) and "low inter-cluster similarity" (different groups are unlike).
- **You must tell it k yourself.**
- The data must be **numbers**, because it measures distance and computes averages.

**The teacher's sketch on slide 5.**
- Some objects, h1, h2, h3 and so on, are sent by "distance" to groups C1, C2, C3.
- So group C1 might end up with h1, h2, h5, and group C2 with h4, h3, h6.
- On the right: "**moving stops**". The algorithm keeps moving the group centres until they stop moving. Then it is finished.

**Slide 8: "K? — free parameter".** The algorithm can find groups, but it **cannot decide how many groups there should be**. That number k is a knob you set by hand. Later slides show how to pick a good k.

**What exactly is k-Means trying to make small?** For each point, measure the distance to its group's centre, square it, and add all of these up. That total is called the **SSE (sum of squared errors)**. k-Means wants the SSE as small as possible, so that every point sits snugly near its own centre.

**Why use the average as the centre?** If you want one spot that is as close as possible to a group of points (closeness measured with squared distances), the best spot is exactly their **average**.
- Example: points at 2, 4 and 9 on a line have average 5.
  - Squared distances from 5: 9 + 1 + 16 = **26**.
  - Squared distances from 4: 4 + 0 + 25 = **29**.
  - Squared distances from 6: 16 + 4 + 9 = **29**.
- 5 wins. That is why it is called "k-*Means*".

**A history correction.** The slide credits Hartigan and Wong (1979). The idea is actually older:
- Steinhaus described it in 1956.
- Stuart Lloyd built the standard algorithm in 1957, though it was published only in 1982.
- Forgy found the same method in 1965.
- MacQueen gave it the name "k-means" in 1967.
- Hartigan and Wong published a faster, cleverer **version** in 1979, which R still uses by default.

The step-by-step algorithm on the next slide is really Lloyd's version.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**k-Means ek line mein.** Tum ise **n** data points aur ek number **k** do. Ye points ko **k groups** mein baant deta hai, aise ki ek group ke points aapas mein paas hon aur alag groups door hon.

**Slide 5 seedhi bhasha mein.**
- Slide kehta hai ki k-Means Hartigan aur Wong ne 1979 mein diya.
- Ye **n** objects ko **k** clusters mein todta hai.
  - **Intra-cluster similarity high**: ek group ke andar sab milte-julte hon.
  - **Inter-cluster similarity low**: alag groups ek dusre se alag hon.
- **k tumhe khud batana padta hai.**
- Data **numbers** mein hona chahiye, kyunki distance aur average nikalna hai.

**Slide 5 pe teacher ka sketch.**
- Objects h1, h2, h3 … distance ke basis pe C1, C2, C3 mein ja rahe hain. Jaise C1 = (h1, h2, h5), C2 = (h4, h3, h6), C3 = (h7, …).
- Side mein likha hai "**k = no. of clusters**".
- Right side pe likha hai "**Moving stops**": algorithm centres ko tab tak move karta rehta hai jab tak woh rukk na jaayein. Ruk gaye to kaam khatam.

**Slide 8: "K? — free parameter".** Algorithm groups dhoondh leta hai, par **kitne groups hone chahiye ye khud decide nahi kar sakta**. k ek knob hai jo tumhe haath se set karna padta hai. Agle slides mein sahi k chunne ka tareeka (elbow method) aayega.

**Dhyan rakho:** k-NN (Lecture 16) ka k aur k-Means ka k alag cheezein hain.
- k-NN mein k = kitne **neighbours** se vote lena hai (supervised).
- k-Means mein k = kitne **clusters** banane hain (unsupervised).

**k-Means asal mein kya chhota karna chahta hai?**
- Har point ka apne group ke centre se distance naapo, use square karo, aur sabka total jodo.
- Is total ko **SSE (Sum of Squared Errors)** kehte hain. Formula hai J = Σ_j Σ_{x∈C_j} ‖x − μ_j‖².
- k-Means ki koshish hai ki SSE jitna ho sake chhota ho, yaani har point apne centre ke paas baitha ho.
- Is formula mein **SSE chhota** hone ka matlab hai groups andar se tight (intra-cluster similarity high). Data ka total failaav fixed hota hai, isliye andar ka failaav kam karne se groups ke beech ka failaav apne aap badh jata hai (inter-cluster similarity low).

**Centre ke liye average hi kyun?** Agar points ke sabse paas (squared distance se) ek jagah dhoondhni hai, to woh unka **average (mean)** hi hoti hai.
- Example: line pe points 2, 4, 9 hain. Average = 5.
  - 5 se squared distances: 9 + 1 + 16 = **26**.
  - 4 se: 4 + 0 + 25 = **29**.
  - 6 se: 16 + 4 + 9 = **29**.
- 5 sabse best hai. Isiliye naam hai "k-*Means*".
- Manhattan distance mein yahi kaam **median** karta (us version ko k-medians kehte hain).

**History ka correction.** Slide Hartigan & Wong (1979) ko credit deta hai, par idea purana hai:
- 1956: Steinhaus ne idea diya.
- 1957: Stuart Lloyd (Bell Labs) ne standard algorithm banaya, jo 1982 mein publish hua.
- 1965: Forgy ne wahi method alag se diya.
- 1967: MacQueen ne naam "k-means" rakha.
- 1979: Hartigan & Wong ne ek **fast, improved version** diya, jo R ka default hai.

Agle slide ka step-by-step algorithm asal mein **Lloyd ka algorithm** hai.

**Ek aur baat:** sabse best (global minimum) clustering dhoondhna NP-hard hai, yaani bahut mushkil. k-Means ek tez shortcut hai. Ye hamesha rukta hai (SSE kabhi badhta nahi), par zaroori nahi ki sabse best jawaab pe ruke. Ye **starting centres pe depend** karta hai (Topic 9 dekho).
