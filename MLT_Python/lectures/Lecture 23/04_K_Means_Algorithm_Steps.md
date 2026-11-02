# Topic 4: The k-Means Algorithm, Step by Step

Source: Lecture 23, slide 6 ("Algorithm 16.1: k-Means clustering", with handwritten notes "k = 2, 3, 4 —", "C1, C2, C3", "Centroid" and the phrase "convergence criterion" underlined). Enriched with general knowledge (convergence proof, stopping rules, empty-cluster handling).

---

## 1) Technical Explanation

### The algorithm as printed on slide 6

```
Algorithm 16.1: k-Means clustering
Input:  D is a dataset containing n objects, k is the number of clusters
Output: A set of k clusters
Steps:
1. Randomly choose k objects from D as the initial cluster centroids.
2. For each of the objects in D do
     • Compute distance between the current object and the k cluster centroids
     • Assign the current object to that cluster to which it is closest.
3. Compute the "cluster centers" of each cluster. These become the new cluster centroids.
4. Repeat steps 2–3 until the convergence criterion is satisfied
5. Stop
```

The instructor's annotations:

- Next to step 1: "**k = 2, 3, 4 —**". k is any value you choose.
- Next to step 2: "**C1, C2, C3**", the clusters being filled.
- Under step 3: "**Centroid**". The "cluster centre" is the centroid, i.e. the mean.
- The phrase "convergence criterion" in step 4 is underlined.

### The same thing in mathematical form (Lloyd's iteration)

- **Initialisation (step 1).** μ₁⁽⁰⁾,…,μ_k⁽⁰⁾ are k distinct objects drawn at random from D. This is called *Forgy initialisation*.
- **Assignment step (step 2).** For every object x_i, set c_i = argmin_j d(x_i, μ_j). The cluster C_j is the set of objects with c_i = j.
- **Update step (step 3).** μ_j = (1/|C_j|) Σ_{x∈C_j} x.
- **Repeat (step 4)** until the convergence criterion holds.

### Common convergence criteria (what "satisfied" means in step 4)

1. **No object changes cluster** between two iterations. This is the classical rule, and it is what slide 15 says: "repeat this till data points stop changing clusters".
2. **Centroids stop moving**, or move less than a tolerance ε. This is the "Moving stops" note on slide 5. scikit-learn's `tol` (default 1e-4) checks the change in centroid positions, relative to the data's variance.
3. **SSE improves by less than a small amount.**
4. **A maximum number of iterations is reached.** scikit-learn's `max_iter` defaults to 300.

### Why the algorithm is guaranteed to stop

The objective is J = Σ_j Σ_{x∈C_j} ‖x − μ_j‖² (see [[03_K_Means_Definition_Objective_and_History]]).

- The **assignment step** can only lower J or keep it the same. Each point moves to the centroid nearest to it, so its own squared distance cannot grow.
- The **update step** can only lower J or keep it the same. For a fixed cluster, the mean is the point that minimises the sum of squared distances.
- So J never increases. There are only finitely many ways to partition n points into k groups, so the algorithm must reach a partition that no longer changes, in a finite number of iterations.
- This guarantee needs Euclidean assignment to match the mean update. With another assignment metric, such as the Manhattan distance in this lecture's worked example, the same "no change ⇒ stop" rule still ends the run in practice.

**But: a local optimum, not a global one.** The final answer depends on the random choice in step 1. Different starting centroids can give different clusters with different SSE. In practice, people run the algorithm several times and keep the run with the lowest SSE (`n_init`), and/or use k-means++ seeding ([[09_K_Means_Limitations_k_means_plus_plus_and_scikit_learn]]).

### Practical details the slide leaves out

- **Ties.** If an object is equally close to two centroids, a fixed rule is used, e.g. "lowest cluster index wins".
- **Empty clusters.** If a centroid ends up with no points, its mean is undefined. Implementations re-seed it, for example at the point farthest from its current centre.
- **Cost.** Each iteration takes O(n·k·d) time. Usually only a few to a few dozen iterations are needed.
- **Feature scaling.** Distances are computed on raw features. A feature with a big numeric range dominates the distances unless the data is standardised first ([[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]] from Lecture 16).

The figures on slides 9–16 walk through these steps visually ([[05_K_Means_Visual_Walkthrough_k_Equals_2]]). Slides 26–32 carry them out on numbers ([[08_Worked_Example_Eight_Points_Manhattan_Distance]]).

---

## 2) Simple English Explanation

Slide 6 gives the whole recipe. Think of it as placing **k flag-poles** on a field and letting people walk to the nearest pole.

**Input:** your data (n objects) and the number of groups you want (k). The teacher wrote "k = 2, 3, 4…" to say k can be any number you choose.

**Output:** k groups.

**Steps:**
1. **Pick k starting centres at random.** Choose k of the data points themselves and plant a flag at each. These are the first "centroids".
2. **Everyone joins the nearest flag.** For every data point, measure its distance to each flag and send it to the closest one. Now you have groups C1, C2, C3, … (as the teacher wrote next to step 2).
3. **Move each flag to the middle of its group.** For each group, take the average of all its points. That average spot is the new centre, or "**centroid**", as the teacher wrote.
4. **Repeat steps 2 and 3.** Once flags move, some people may now be closer to a different flag, so they switch. Then the flags move again.
5. **Stop** when the "convergence criterion" (underlined by the teacher) is met. Usually that means **nobody switched groups** in the last round, or the flags **stopped moving**. Some programs also stop after a fixed maximum number of rounds.

**Why does it always finish?** Think of the "total squared distance" from each person to their flag as a score we want to make small.
- When people walk to their nearest flag, the score can only go down or stay the same.
- When a flag moves to the middle of its group, the score can only go down or stay the same.
- A score that keeps going down can't do so forever when there are only a limited number of ways to form groups. So eventually nothing changes, and it stops.

**The catch.** Where it stops depends on where you planted the flags at the start. A bad start can leave you stuck in a "good but not best" answer. That is why real software runs it several times from different random starts and keeps the best result.

**Things the slide doesn't mention:**
- If a point is exactly equally far from two flags, a simple fixed rule decides which one it joins.
- If a flag ends up with nobody near it, the program moves it somewhere useful.
- If one feature is measured in big numbers (salary in rupees) and another in small numbers (age in years), the big one will dominate the distances. So we usually scale the features first, just like with k-NN.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Slide 6 poori recipe deta hai. Socho ek maidan mein **k jhande (flags)** gaadne hain, aur har insaan sabse paas wale jhande ke paas chala jata hai.

**Input:** data (n objects) aur kitne groups chahiye (k). Teacher ne likha "k = 2, 3, 4 …", yaani k tum kuch bhi choose kar sakte ho.

**Output:** k clusters.

**Steps:**
1. **Random k starting centres chuno.** Data ke hi k points uthao aur unpe jhande gaad do. Ye pehle "centroids" hain.
2. **Har point sabse paas wale jhande ke paas jaye.** Har point ka har jhande se distance naapo aur jo sabse kam ho, us group mein daal do. Ab groups C1, C2, C3 … ban gaye (teacher ne step 2 ke paas yahi likha).
3. **Har jhanda apne group ke beech mein le jao.** Har group ke saare points ka average nikaalo. Wahi naya centre hai, jise teacher ne "**Centroid**" likha.
4. **Step 2 aur 3 dobara karo.** Jhande hile to kuch points ab doosre jhande ke zyada paas ho sakte hain, isliye woh group badlenge. Phir jhande dobara hilenge.
5. **Stop** jab "convergence criterion" (teacher ne underline kiya) poora ho jaye. Matlab:
   - Kisi bhi point ne group nahi badla, ya
   - Jhande hilna band ho gaye (slide 5 ka "Moving stops"), ya
   - SSE mein sudhaar bahut chhota reh gaya, ya
   - Maximum rounds poore ho gaye (scikit-learn mein `max_iter = 300`).

**Ye hamesha rukta kyun hai?** Har point ki apne jhande se squared distance jodo. Ye score (SSE) hai jo chhota karna hai.
- Jab points sabse paas wale jhande pe jaate hain, score ya to ghatta hai ya same rehta hai.
- Jab jhanda group ke average pe jata hai, tab bhi score ya ghatta hai ya same rehta hai (average hi squared distance ko sabse kam karta hai).
- Groups banane ke tareeke limited hain, aur score kabhi badhta nahi. Isliye ek din kuch nahi badlega aur algorithm ruk jayega.

**Lekin ek pakad hai.** Kahan rukega, ye shuru ke random jhandon pe depend karta hai. Galat start se algorithm "theek-thaak par best nahi" jawaab (**local minimum**) pe atak sakta hai. Isliye software ise kai baar alag random starts se chalata hai aur sabse kam SSE wala result rakhta hai (`n_init`). Ek smart start ka tareeka **k-means++** bhi hai (Topic 9).

**Jo slide nahi batata:**
- **Tie**: point do jhandon se barabar door ho to ek fixed rule lagta hai, jaise chhote number wala cluster.
- **Khaali cluster**: kisi jhande ke paas koi point nahi bacha to program use kisi useful jagah shift kar deta hai.
- **Scaling**: ek feature bade numbers mein ho (salary) aur doosra chhote mein (age), to bada feature distance pe haavi ho jayega. Isliye pehle features ko scale karte hain, bilkul k-NN ki tarah (Lecture 16).
- **Time**: har round mein n × k × d calculation hoti hai, aur aam taur pe kuch hi rounds lagte hain.
