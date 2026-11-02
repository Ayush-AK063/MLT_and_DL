# Topic 2: Taxonomy of Clustering Techniques

Source: Lecture 23, slide 3 (tree diagram "Clustering Techniques" with handwritten notes "Distance based", "Hierarchical Decomposition", "Dense regions of objects (Neighborhood)") and slide 4 (table "Method / General Characteristics"). Enriched with web research (Han, Kamber & Pei, *Data Mining: Concepts and Techniques*, Ch. 10, whose overview table slide 4 reproduces) and general knowledge of the original papers.

---

## 1) Technical Explanation

### Slide 3: the family tree

The slide splits clustering techniques into **five families**. Each family lists named algorithms with the year the slide gives. The instructor's handwritten note on each family is in quotes.

| Family | Handwritten note | Algorithms on the slide |
|---|---|---|
| **Partitioning methods** | "Distance based" | k-Means [1957, 1967]; k-Medoids (dashed arrow to its variants **PAM [1990], CLARA [1990], CLARANS [1994]**); k-Modes [1998]; Fuzzy c-means [1999] |
| **Hierarchical methods** | "Hierarchical Decomposition" | **Divisive** → DIANA [1990]. **Agglomerative** → AGNES [1990], BIRCH [1996], CURE [1998], ROCK [1999], "Chamelon" [1999] (spelled CHAMELEON in the literature) |
| **Density-based methods** | "Dense regions of objects (Neighborhood)" | STING [1997], DBSCAN [1996], CLIQUE [1998], DENCLUE [1998], OPTICS [1999], Wave Cluster [1998] |
| **Graph-based methods** | none | MST Clustering [1999], OPOSSUM [2000], SNN Similarity Clustering [2001, 2003] |
| **Model-based clustering** | marked with a bracket | EM Algorithm [1977], AutoClass [1996], COBWEB [1987], ANN Clustering [1982, 1989] |

### Slide 4: general characteristics

This table matches the overview table of clustering methods in Han, Kamber & Pei, Chapter 10.

| Method | General characteristics (from the slide) |
|---|---|
| **Partitioning** | Find mutually exclusive clusters of spherical shape · distance-based · may use **mean or medoid** to represent the cluster centre · effective for small- to medium-size data sets |
| **Hierarchical** | Clustering is a hierarchical decomposition (multiple levels) · **cannot correct erroneous merges or splits** · may incorporate microclustering or consider object "linkages" |
| **Density-based** | Can find **arbitrarily shaped** clusters · clusters are dense regions separated by low-density regions · each point must have a **minimum number of points within its "neighbourhood"** · may filter out outliers |
| **Grid-based** | Use a multiresolution grid data structure · fast processing time, typically independent of the number of data objects but dependent on grid size |

### What each family actually does

- **Partitioning.** Choose k, then split the n objects into k non-overlapping groups. Each group is represented by a centre, and points are moved between groups to reduce a cost.
  - **k-Means** uses the **mean** as the centre. The mean need not be an actual data point.
  - **k-Medoids** (PAM = Partitioning Around Medoids) uses a **medoid**, the most central *real* object. This makes it more robust to outliers.
  - **CLARA** runs PAM on samples, and **CLARANS** uses a randomised search, so both scale to larger data.
  - **k-Modes** (Huang 1998) is for **categorical** data. It uses modes and a mismatch count instead of means and Euclidean distance.
  - **Fuzzy c-means** gives each point a **degree of membership** in every cluster instead of a hard assignment.
- **Hierarchical.** Builds a tree of clusters called a *dendrogram*. You cut the tree at some level to get the clusters.
  - **Agglomerative** methods work bottom-up: start with every point as its own cluster and repeatedly merge the two closest clusters (AGNES).
  - **Divisive** methods work top-down: start with one cluster and repeatedly split it (DIANA).
  - The slide-4 weakness "cannot correct erroneous merges or splits" means a merge is never undone later.
  - BIRCH uses a compact CF-tree for big data. CURE uses several representative points per cluster. ROCK works with categorical links. CHAMELEON uses dynamic modelling on a k-NN graph.
- **Density-based.** A cluster is a region where points are packed densely.
  - **DBSCAN** (1996) has two parameters: a radius ε and a minimum count MinPts. A *core point* has at least MinPts neighbours within ε. Clusters grow from core points, and points in sparse areas are labelled **noise**. That is why the slide says density methods "may filter out outliers".
  - These methods find **arbitrary shapes**, such as rings or crescents, where k-Means fails.
  - OPTICS orders points by density reachability, so one run covers many ε values. DENCLUE uses density functions.
- **Grid-based.** Quantise the space into cells and cluster the cells instead of the points. The cost then depends on the number of cells, not on n.
- **Graph-based.** Treat points as nodes and similarities as weighted edges, then cut the graph. For example, remove the longest edges of a **minimum spanning tree**, or use shared-nearest-neighbour (SNN) similarity.
- **Model-based.** Assume the data come from a statistical model and fit it.
  - **EM** (Dempster, Laird & Rubin 1977) fits a mixture of Gaussians. It gives *soft* assignments, and k-Means is its hard-assignment limiting case.
  - **COBWEB** builds a conceptual hierarchy. **AutoClass** is Bayesian.
  - **ANN clustering** refers to neural approaches such as Kohonen's self-organising maps (1982) and adaptive resonance theory.

### Points to note (cross-checked with the source book)

1. **Slide 3 and slide 4 don't fully match.** Slide 4 has a **grid-based** row, but slide 3's tree has no grid-based branch. Slide 3 instead puts **STING, CLIQUE and WaveCluster under density-based**. In Han, Kamber & Pei those three are the standard examples of **grid-based** methods. CLIQUE is really a hybrid: grid-based subspace clustering that keeps the dense cells. For exams, follow the slide, but remember the textbook calls STING and WaveCluster grid-based.
2. **Years on slide 3 are "landmark" dates, not always first publication.**
   - k-Means [1957, 1967]: Lloyd's 1957 Bell Labs report and MacQueen's 1967 paper, which coined the name.
   - Fuzzy c-means is usually credited to Dunn (1973) and Bezdek (1981), so the "1999" on the slide is probably a later reference.
3. **Partitioning methods need k in advance and favour spherical (convex) clusters.** This is why the lecture goes on to ask "how to determine k?" ([[06_Choosing_k_SSE_and_the_Elbow_Method]]).

---

## 2) Simple English Explanation

There isn't just one way to cluster. Slide 3 is a "family tree" with **five families**, and slide 4 describes the four classic ones. The teacher wrote a short memory hint next to each family.

**1. Partitioning methods (hint: "distance based").**
- You decide in advance how many groups you want (k). The method then cuts the data into exactly k separate groups, so every point belongs to exactly one group.
- Each group has a "centre", and points join the nearest centre.
- **k-Means**, the star of this lecture, uses the **average position** of the group as its centre.
- **k-Medoids** uses the most central **real** data point instead of an average, so one crazy outlier can't drag the centre away. PAM, CLARA and CLARANS are versions of k-Medoids, the last two built for big data.
- **k-Modes** works with categories like "red/blue/green" instead of numbers.
- **Fuzzy c-means** lets a point belong partly to several groups, e.g. 70% group A, 30% group B.
- Slide 4 says these methods find **round-ish** groups, use distance, and work well for small-to-medium data.

**2. Hierarchical methods (hint: "hierarchical decomposition").**
- Instead of one answer, you get a whole **family tree of groups**, from "everyone in one group" down to "everyone alone".
- **Bottom-up (agglomerative)**: start with every point alone and keep joining the two closest groups. AGNES, BIRCH, CURE, ROCK and CHAMELEON work this way.
- **Top-down (divisive)**: start with one big group and keep splitting it. DIANA works this way.
- Weakness: once two groups are joined (or split), the method **never undoes it**, even if it was a mistake.

**3. Density-based methods (hint: "dense regions of objects, neighbourhood").**
- A cluster is a **crowded area**, like a busy market square, separated from other crowds by emptier space.
- **DBSCAN** asks: does this point have at least a minimum number of neighbours within a small radius? If yes, it is in a crowd. If a point is alone in an empty area, it is marked as **noise (an outlier)**.
- These methods can find groups of **any shape**, such as a ring or a banana shape, which k-Means cannot.

**4. Grid-based methods (only on slide 4).**
- Lay a grid over the space like graph paper and work with the squares instead of individual points.
- This is **very fast**, because the work depends on the number of squares, not the number of points.

**5. Graph-based and model-based methods (slide 3).**
- **Graph-based**: think of points as cities and similarities as roads, then cut the weakest roads to separate groups.
- **Model-based**: assume the data was generated by some mathematical recipe (for example, a mix of bell curves) and work out the recipe. **EM** is the famous one. It gives soft, probability-style memberships.

**Two small mismatches worth knowing.**
- Slide 3 lists STING, CLIQUE and Wave Cluster under density-based, but the textbook this table comes from calls them **grid-based**, and slide 3 has no grid branch at all.
- Some years on the tree are later milestones rather than first inventions. For example, fuzzy c-means really dates from the 1970s–80s.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Clustering karne ka sirf ek tareeka nahi hai. Slide 3 ek "family tree" hai jismein **paanch families** hain, aur slide 4 unmein se chaar classic families ki khaasiyat batata hai. Teacher ne har family ke paas yaad rakhne ke liye chhota hint likha hai.

**1. Partitioning methods (hint: "Distance based").**
- Pehle tum decide karte ho ki kitne groups chahiye (k). Phir method data ko exactly k alag groups mein kaat deta hai, aur har point sirf ek group mein jata hai.
- Har group ka ek "centre" hota hai, aur point sabse paas wale centre ke group mein chala jata hai.
- **k-Means** (is lecture ka hero) centre ke liye group ki **average position (mean)** leta hai.
- **k-Medoids** average nahi leta, sabse beech wala **asli data point (medoid)** leta hai, isliye ek ajeeb outlier centre ko kheench nahi pata. PAM, CLARA aur CLARANS iske versions hain. CLARA aur CLARANS bade data ke liye bane hain.
- **k-Modes** numbers ki jagah categories (red/blue/green) ke liye hai.
- **Fuzzy c-means** mein ek point thoda-thoda kai groups mein ho sakta hai, jaise 70% A aur 30% B.
- Slide 4 kehta hai ki ye methods **gol (spherical)** groups dhoondhte hain, distance use karte hain, aur small se medium data ke liye achhe hain.

**2. Hierarchical methods (hint: "Hierarchical Decomposition").**
- Ek answer ki jagah groups ka poora **khandaani tree (dendrogram)** milta hai: "sab ek group mein" se lekar "har point akela" tak.
- **Agglomerative (neeche se upar)**: har point akela shuru karta hai, phir sabse paas wale do groups baar-baar jode jaate hain. AGNES, BIRCH, CURE, ROCK aur CHAMELEON aise kaam karte hain.
- **Divisive (upar se neeche)**: ek bada group shuru mein hota hai, phir use baar-baar todte hain. DIANA aise kaam karta hai.
- Kamzori: ek baar merge ya split ho gaya to **wapas undo nahi hota**, chahe galti hi kyun na ho.

**3. Density-based methods (hint: "Dense regions of objects, Neighborhood").**
- Cluster matlab **bheed wala area**, jaise bazaar ka bheed bhara chowk, jo doosri bheed se khaali jagah se alag hai.
- **DBSCAN** poochta hai: kya is point ke ek chhote radius (ε) ke andar kam se kam MinPts padosi hain? Haan to point bheed ka hissa hai. Agar point khaali jagah mein akela hai to use **noise (outlier)** maan lete hain.
- Ye kisi bhi **shape** ke group dhoondh sakte hain, jaise ring ya kela-shape, jo k-Means nahi kar pata.

**4. Grid-based methods (sirf slide 4 mein).**
- Space pe graph paper jaisa grid bichhao aur points ki jagah squares (cells) pe kaam karo.
- Ye **bahut fast** hai, kyunki kaam squares ki sankhya pe depend karta hai, points ki sankhya pe nahi.

**5. Graph-based aur model-based (slide 3).**
- **Graph-based**: points ko shehar aur similarity ko sadak samjho, phir sabse kamzor sadkein kaat ke groups alag karo. Jaise minimum spanning tree ki sabse lambi edges hata dena.
- **Model-based**: maan lo data kisi maths recipe se bana hai (jaise kai bell curves ka mix), aur woh recipe nikaalo. **EM (1977)** famous hai, jo probability wali soft membership deta hai. k-Means ise hard-assignment wala simple case maana ja sakta hai.

**Do chhoti galtiyan / mismatch yaad rakho.**
- Slide 3 mein STING, CLIQUE aur Wave Cluster density-based ke neeche likhe hain, jabki jis textbook (Han, Kamber & Pei) se slide 4 ki table li gayi hai, wahan ye **grid-based** ke examples hain. Saath hi slide 3 mein grid ki branch hi nahi hai. Exam mein slide wala answer likho, par asli classification bhi pata honi chahiye.
- Kuch saal "milestone" hain, pehli khoj nahi. Jaise fuzzy c-means asal mein 1973–1981 (Dunn, Bezdek) ka hai, aur k-Means ke [1957, 1967] ka matlab Lloyd (1957) aur MacQueen (1967) hai.
