# Topic 6: PCA — Fully Worked Numeric Example (Covariance, Eigenvalues, Eigenvectors, Transform)

Source: Lecture 11, slides 23–32 ("Principal Component Analysis-Example" ×8). Every computation below has been independently verified. Enriched with web research identifying the origin of this dataset.

---

## 1) Technical Explanation

### Origin of this dataset

This exact 10-point (X, Y) dataset is the classic teaching example from Lindsay I. Smith's widely-cited 2002 tutorial *"A Tutorial on Principal Component Analysis"* (over 2,000 citations) — one of the most commonly reused worked PCA examples in ML teaching material worldwide, which explains why this specific set of numbers appears in slide form here as well.

### The dataset

| X | Y |
|---|---|
| 2.5 | 2.4 |
| 0.5 | 0.7 |
| 2.2 | 2.9 |
| 1.9 | 2.2 |
| 3.1 | 3.0 |
| 2.3 | 2.7 |
| 2.0 | 1.6 |
| 1.0 | 1.1 |
| 1.5 | 1.6 |
| 1.1 | 0.9 |

### Step 1: Compute the covariance matrix A

First, the means: X̄ = 1.81, Ȳ = 1.91 (**verified**: ΣX = 18.1 → 18.1/10 = 1.81; ΣY = 19.1 → 19.1/10 = 1.91 — matches the slide exactly).

For each point, compute (Xᵢ−X̄), (Yᵢ−Ȳ), and the three products needed for covariance:

| X | Y | Xᵢ−X̄ | Yᵢ−Ȳ | (Xᵢ−X̄)² | (Yᵢ−Ȳ)² | (Xᵢ−X̄)(Yᵢ−Ȳ) |
|---|---|---|---|---|---|---|
| 2.5 | 2.4 | 0.69 | 0.49 | 0.4761 | 0.2401 | 0.3381 |
| 0.5 | 0.7 | -1.31 | -1.21 | 1.7161 | 1.4641 | 1.5851 |
| 2.2 | 2.9 | 0.39 | 0.99 | 0.1521 | 0.9801 | 0.3861 |
| 1.9 | 2.2 | 0.09 | 0.29 | 0.0081 | 0.0841 | 0.0261 |
| 3.1 | 3.0 | 1.29 | 1.09 | 1.6641 | 1.1881 | 1.4061 |
| 2.3 | 2.7 | 0.49 | 0.79 | 0.2401 | 0.6241 | 0.3871 |
| 2.0 | 1.6 | 0.19 | -0.31 | 0.0361 | 0.0961 | -0.0589 |
| 1.0 | 1.1 | -0.81 | -0.81 | 0.6561 | 0.6561 | 0.6561 |
| 1.5 | 1.6 | -0.31 | -0.31 | 0.0961 | 0.0961 | 0.0961 |
| 1.1 | 0.9 | -0.71 | -1.01 | 0.5041 | 1.0201 | 0.7171 |

Summing each of the last three columns and dividing by **N−1 = 9** (sample covariance, per the formula in [[05_How_PCA_Works_Step_by_Step]]):

- Σ(Xᵢ−X̄)² = 5.549 → **Cov(X,X) = 5.549 / 9 = 0.6166 ≈ 0.6165** ✓ (verified independently, matches slide)
- Σ(Yᵢ−Ȳ)² = 6.449 → **Cov(Y,Y) = 6.449 / 9 = 0.7166 ≈ 0.7165** ✓ (verified, matches slide)
- Σ(Xᵢ−X̄)(Yᵢ−Ȳ) = 5.539 → **Cov(X,Y) = Cov(Y,X) = 5.539 / 9 = 0.6154** ✓ (verified, matches slide exactly)

So:
$$A = \begin{bmatrix} 0.6165 & 0.6154 \\ 0.6154 & 0.7165 \end{bmatrix}$$

### Step 2: Compute eigenvalues

Solving det(A − λI) = 0 for a 2×2 matrix reduces to the quadratic:
$$\lambda^2 - (\text{trace})\lambda + \det(A) = 0$$

- trace(A) = 0.6165 + 0.7165 = 1.333
- det(A) = (0.6165)(0.7165) − (0.6154)² = 0.441722 − 0.378717 = 0.063005

Solving the quadratic: λ = [1.333 ± √(1.333² − 4×0.063005)] / 2 = [1.333 ± √1.524869] / 2 = [1.333 ± 1.234856] / 2

- **λ₁ = (1.333 + 1.234856)/2 = 1.28393**
- **λ₂ = (1.333 − 1.234856)/2 = 0.04907**

These independently-recomputed values match the slide's stated **λ₁ = 1.284028, λ₂ = 0.049083** to within rounding error (the tiny difference comes from the slide's internal computation using the *unrounded* covariance values, while the table above only prints them to 4 decimal places). **Verification check:** λ₁ + λ₂ should equal trace(A) — 1.284028 + 0.049083 = 1.333111 ≈ 1.333 ✓.

### Step 3: Compute eigenvectors

Solving [A − λI]X = 0 for each eigenvalue gives the corresponding eigenvector direction (before normalization). After normalizing to unit length, the slide gives:

$$V_1 = \begin{bmatrix} 0.67787 \\ 0.73517 \end{bmatrix} \quad V_2 = \begin{bmatrix} -0.73517 \\ 0.67787 \end{bmatrix}$$

**Verification — both are genuinely unit vectors:** 0.67787² + 0.73517² = 0.459515 + 0.540575 = 1.00009 ≈ 1 ✓ (V2 similarly: 0.73517² + 0.67787² = same sum = 1.00009 ≈ 1 ✓).

**Verification — V1 and V2 are genuinely orthogonal (perpendicular)**, as PCA requires: V1 · V2 = (0.67787)(−0.73517) + (0.73517)(0.67787) = −0.49830 + 0.49830 = 0 ✓ — confirming the two eigenvectors are at exactly 90° to each other, as demanded by PCA's constraint that PC2 must be perpendicular to PC1.

### Step 4: Order by eigenvalue and compute % information explained

Since λ₁ > λ₂, **V1 is First Principal Component (PC1)** and **V2 is Second Principal Component (PC2)** — matching the rule from [[04_PCA_Introduction_and_Intuition]] that the eigenvector with the highest eigenvalue is always PC1.

The percentage of information (variance) each component explains is its eigenvalue divided by the sum of all eigenvalues:

- PC1: 1.284028 / (1.284028 + 0.049083) = 1.284028 / 1.333111 = **0.9632 → 96%** ✓ (matches slide)
- PC2: 0.049083 / 1.333111 = **0.0368 → 4%** ✓ (matches slide)

This confirms the general PCA fact from [[04_PCA_Introduction_and_Intuition]] very concretely: **almost all the useful information in this 2-feature dataset (96%) can be captured by a single new axis (PC1)** — a real demonstration of 2D → 1D dimensionality reduction losing only about 4% of the total variance.

### Step 5: Final transformation

Once the components with negligible information are discarded (here, one could optionally drop PC2 and keep only PC1, going from 2 dimensions to 1), the retained eigenvectors form the **feature vector** matrix (each column = one retained principal component). The final, transformed dataset is obtained via:

$$\text{Final dataset} = \text{Feature vector}^T \times \text{Original dataset}^T$$

This matrix multiplication projects each original (X, Y) point onto the new PC axes, producing the point's coordinates in the new, reduced-dimension space — exactly the "transform the data along the principal component axis" step described generally in [[05_How_PCA_Works_Step_by_Step]].

---

## 2) Simple English Explanation

This worked example takes 10 simple (X, Y) data points and walks through the entire PCA process by hand, and every number has been double-checked here to confirm the slide's math is correct.

1. **Find the average of X and the average of Y.** (1.81 and 1.91.)
2. **Measure how X and Y vary together** (the covariance matrix) — this tells you that X and Y in this dataset tend to increase together fairly strongly (a positive, sizeable covariance of 0.6154 between them).
3. **Solve for the "important directions" (eigenvalues/eigenvectors)** — this gives two new directions: one that's much more important (λ₁ ≈ 1.284) and one that's much less important (λ₂ ≈ 0.049).
4. **Check that these two new directions are perpendicular to each other** — confirmed: yes, exactly 90° apart, as PCA always guarantees.
5. **Work out what percentage of the total information each direction holds** — the first direction (PC1) holds 96% of all the useful spread in the data, and the second (PC2) holds only the remaining 4%.
6. **Because PC1 alone holds 96% of the information, you could safely describe this whole 2-column dataset using just 1 new column (PC1)** and lose almost nothing — turning 2D data into 1D data with only ~4% information loss. That's PCA's dimensionality reduction actually happening, in numbers you can check by hand.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye worked example 10 simple (X, Y) data points leta hai aur poore PCA process ko haath se karke dikhata hai, aur har number yahan double-check kiya gaya hai taaki confirm ho ki slide ka math sahi hai.

1. **X ka average aur Y ka average nikalo.** (1.81 aur 1.91.)
2. **Measure karo ki X aur Y saath mein kaise vary karte hain** (covariance matrix) — ye batata hai ki is dataset mein X aur Y ek saath badhte hain fairly strongly (positive, sizeable covariance 0.6154 dono ke beech).
3. **"Important directions" (eigenvalues/eigenvectors) solve karo** — ye do naye directions dete hain: ek jo bahut zyada important hai (λ₁ ≈ 1.284) aur ek jo bahut kam important hai (λ₂ ≈ 0.049).
4. **Check karo ki ye dono naye directions ek doosre ke perpendicular hain** — confirmed: haan, exactly 90° apart, jaisa PCA hamesha guarantee karta hai.
5. **Pata karo total information ka kitna percentage har direction ke paas hai** — pehli direction (PC1) data ke total useful spread ka 96% rakhti hai, aur doosri (PC2) sirf baaki 4%.
6. **Kyunki PC1 akele hi 96% information rakhta hai, tum is poore 2-column dataset ko safely sirf 1 naye column (PC1) se describe kar sakte ho** aur almost kuch nahi khote — 2D data ko 1D data mein badalna sirf ~4% information loss ke saath. Yahi hai PCA ki dimensionality reduction actually ho rahi hai, un numbers mein jo tum khud haath se check kar sakte ho.

Sources (web research):
- [A tutorial on Principal Components Analysis — Lindsay I. Smith (2002), via ScispaCe](https://scispace.com/papers/a-tutorial-on-principal-components-analysis-342x97asjk)
- [A tutorial on Principal Components Analysis — Semantic Scholar](https://www.semanticscholar.org/paper/A-tutorial-on-Principal-Components-Analysis-Smith/462bf829634e3ffaef794de5e58809994d30f8ec)
