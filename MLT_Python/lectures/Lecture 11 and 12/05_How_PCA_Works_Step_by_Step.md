# Topic 5: How PCA Works — Step by Step (Informal Walkthrough + Formal Mathematical Procedure)

Source: Lecture 11, slides 18–22 ("How Principal Component Analysis Works" ×3, an unlabeled 2D→1D transformation diagram, "Principal Component Analysis" — Stepwise working ×2). This is the slides' own mechanical walkthrough of PCA, which is more procedurally detailed than the general algorithm description already given in [[07_Feature_Extraction_PCA_SVD_LDA]] from Lecture 10 — that file is not repeated here, only cross-referenced.

---

## 1) Technical Explanation

### The core mechanism, in three bullets (slide 18)

> "PCA uses linear algebra to transform data into new features called principal components. It finds these by calculating eigenvectors (directions) and eigenvalues (importance) from the covariance matrix. PCA selects the top components with the highest eigenvalues and projects the data onto them [to] simplify the dataset."
>
> **Note:** It prioritizes the directions where the data varies the most, because more variation = more useful information.

This single paragraph is the entire mechanism in miniature: **eigenvectors give direction, eigenvalues give importance**, and PCA simply keeps the most-important directions.

### The four-step informal process (slide 19)

1. **Standardize the data.** Different features can have wildly different units and scales (e.g., salary in thousands vs. age in tens) — to compare them fairly, every feature is rescaled to have **mean = 0** and **standard deviation = 1**. Without this, a large-scale feature like salary would dominate the variance calculation purely because of its units, not because it's actually more informative — this is the same scale-sensitivity issue covered for Z-score/Min-Max scaling in Lecture 8's normalization topics.
2. **Calculate the covariance matrix.** This matrix captures, for every *pair* of features, whether they tend to increase/decrease together (positive covariance), move oppositely (negative covariance), or show no relationship (near-zero covariance). This is the same covariance concept used in Pearson correlation ([[05_Measuring_Feature_Redundancy_Correlation_and_Distance]] from Lecture 10), just kept unnormalized (correlation is covariance divided by the product of the two standard deviations).
3. **Find the principal components.** PCA identifies new axes along which the data spreads out the most:
   - **1st Principal Component (PC1):** the single direction of maximum variance (most spread).
   - **2nd Principal Component (PC2):** the next-best direction, constrained to be **perpendicular (orthogonal) to PC1** — and so on for PC3, PC4, etc., each perpendicular to all previous PCs.
4. **Pick the top directions and transform the data.** After computing eigenvalues/eigenvectors, rank them by how much variance (information) they capture, then:
   - Select the top *k* components that together capture most of the variance (a common target is ~95%).
   - Transform (project) the original dataset onto just these top *k* components — this is the actual dimensionality-reduction step, replacing the original *n* features with *k* new ones (*k* < *n*).

### Visual example — 2D → 1D (slide 20)

The slide shows a simple 2-feature dataset (axes: "Radius" and "Area") with two candidate directions drawn through the data: **PC1** (steeper, more closely tracking the data's actual spread) and **PC2** (a lower-variance direction). The variance captured along PC1 is visibly larger than the variance along PC2 (shown with labeled brace brackets), confirming PC1 > PC2 in terms of information captured. Since PC1 alone captures most of the spread, projecting this 2D data onto just the PC1 axis (a 2D → 1D transformation) loses relatively little information — a concrete, visual instance of the general 4-step process above with n=2, k=1.

### Formal mathematical procedure (slides 21–22)

The same process stated with explicit equations:

1. **Construct the covariance matrix, A.** For two features X, Y:
   $$Cov(X,Y) = \frac{1}{N-1}\sum_{i=1}^{N}(X_i - \bar{X})(Y_i - \bar{Y})$$
   (Note the **N−1** denominator — this is the *sample* covariance formula, not the population version which would divide by N. This detail is confirmed by the fully worked numeric example in [[06_PCA_Worked_Example_Covariance_Eigen]], which reproduces this exact formula with N−1=9 for a 10-point dataset.)

2. **Compute the eigenvalues of the covariance matrix**, by solving:
   $$\det(A - \lambda I) = 0$$
   where λ (lambda) represents an eigenvalue and I is the identity matrix. This equation, expanded out, becomes a polynomial in λ — solving it yields one eigenvalue per original feature/dimension.

3. **Compute the eigenvector corresponding to each eigenvalue found in step 2**, by solving:
   $$[A - \lambda I]\,X = 0$$
   for the vector X — each solution X is the eigenvector (direction) associated with that particular eigenvalue.

4. **Sort the eigenvectors in decreasing order of their eigenvalues**, and choose the top *k* eigenvectors with the largest eigenvalues — these become the retained principal components.

5. **Transform the data along the principal component axes** — project the original (standardized) dataset onto the chosen eigenvectors to obtain the final, reduced-dimension dataset.

This five-step formal procedure and the four-step informal one describe **the same process** — steps 1–2 of the formal version correspond to steps 1–2 of the informal version (standardize is implicit before constructing A properly), step 3 of the formal version is the mechanism behind "find eigenvectors" in step 3 of the informal version, and steps 4–5 formalize "pick top directions and transform" from step 4 of the informal version.

---

## 2) Simple English Explanation

Here's PCA's entire recipe in plain terms:

1. **Make all your measurements comparable.** If one column is "salary in rupees" (values in lakhs) and another is "age in years" (values under 100), you first rescale both so they're on the same footing — otherwise salary would unfairly dominate just because its numbers are bigger, not because it's more important.
2. **Figure out how every pair of features moves together.** This is the covariance matrix — it's basically a table answering "when feature A goes up, does feature B tend to go up too, go down, or do its own thing?" for every pair of features.
3. **Find the best new directions to look at the data from.** The first new direction (PC1) is chosen to be the one direction where the data is *most* spread out. The second (PC2) is the next-best direction, but it's required to be at a right angle to the first — think of PC1 and PC2 like two perpendicular rulers you lay over your data.
4. **Keep only the best few directions, and re-plot your data using just those.** You typically keep enough directions to cover ~95% of the original spread, discard the rest, and now describe every data point using only those kept directions — fewer numbers per data point than you started with, but almost as much real information.

The formal math version just writes this same recipe using precise equations: the covariance formula (step 1 above), then "eigenvalue" and "eigenvector" are just the formal mathematical names for "how important is this direction" and "what exactly is this direction," found by solving det(A − λI) = 0 and [A − λI]X = 0 respectively.

---

## 3) Hinglish Explanation (Beginner-Friendly)

PCA ka poora recipe simple bhasha mein:

1. **Apni saari measurements ko comparable banao.** Agar ek column "salary in rupees" hai (values lakhon mein) aur doosra "age in years" hai (values 100 se kam), to pehle dono ko rescale karo taaki wo ek jaisi footing pe hon — warna salary unfairly dominate kar degi sirf isliye ki uske numbers bade hain, isliye nahi ki wo zyada important hai.
2. **Pata karo har pair of features saath mein kaise move karte hain.** Ye covariance matrix hai — ye basically ek table hai jo batata hai "jab feature A badhta hai, to kya feature B bhi badhta hai, ya ghatta hai, ya apna alag kaam karta hai?" — har pair of features ke liye.
3. **Data dekhne ke liye sabse acche naye directions dhundo.** Pehla naya direction (PC1) wo hai jahan data *sabse zyada* failaa hua hai. Doosra (PC2) agla-best direction hai, lekin ye pehle ke right angle pe hona zaroori hai — PC1 aur PC2 ko do perpendicular rulers jaisa socho jo tum apne data pe rakhte ho.
4. **Sirf sabse acche kuch directions rakho, aur apna data sirf unhi se re-plot karo.** Usually itne directions rakhte ho ki ~95% original failaav cover ho jaaye, baaki discard karo, aur ab har data point ko sirf un rakhe hue directions se describe karo — shuru se kam numbers per data point, lekin almost utni hi real information.

Formal math version bas isi recipe ko precise equations mein likhta hai: covariance formula (step 1 upar), phir "eigenvalue" aur "eigenvector" bas formal mathematical naam hain "ye direction kitni important hai" aur "ye direction exactly kya hai" ke liye, jo det(A − λI) = 0 aur [A − λI]X = 0 solve karke milte hain.
