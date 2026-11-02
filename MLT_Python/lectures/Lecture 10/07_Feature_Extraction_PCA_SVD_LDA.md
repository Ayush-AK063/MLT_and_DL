# Topic 7: Feature Extraction — PCA, SVD, and LDA

Source: Lecture 10, slide 6 (names only: "Principal Component Analysis", "Singular-Valued Decomposition", "Linear Discriminant Analysis" listed under Feature Extraction). The slides give zero mechanical detail on any of these three — this entire topic file is built from web research, per the standing workflow rule for genuinely new, unexplained content.

---

## 1) Technical Explanation

Recall from [[02_Data_Reduction_Techniques_Overview]]: Feature Extraction methods create **new** features as combinations of the original ones, rather than selecting a subset of existing features. PCA, SVD, and LDA are the three methods named on slide 6.

### Principal Component Analysis (PCA)

PCA is an **unsupervised** technique (it does not use target/class labels) that finds new axes — called **principal components** — along which the data has maximum variance, and re-expresses the data along those axes.

**The algorithm, step by step:**
1. **Standardization** — scale every original feature to have mean 0 and unit variance. This is essential because PCA is sensitive to the scale of variables — a feature measured in thousands (like salary) would otherwise dominate a feature measured in small units (like age) purely due to scale, not real importance.
2. **Compute the covariance matrix** — this captures how every pair of features varies together across the dataset.
3. **Compute eigenvectors and eigenvalues** of the covariance matrix. Each eigenvector represents a possible new axis (a "direction" in feature space); its corresponding eigenvalue represents how much variance in the data lies along that axis.
4. **Order the eigenvectors by their eigenvalues, largest first.** The eigenvector with the largest eigenvalue is the **first principal component (PC1)** — the single direction along which the data varies the most. The second-largest gives **PC2** (constrained to be perpendicular/orthogonal to PC1), and so on.
5. **Project the original data onto the top-k principal components** — this is the dimensionality reduction step: instead of keeping all original features, keep only the first few PCs that together explain most of the total variance (e.g., "the first 3 PCs explain 95% of the variance").

**Key property:** the resulting principal components are guaranteed to be uncorrelated with each other (since they're orthogonal directions), even if the original features were highly correlated/redundant — which is exactly the redundancy problem discussed in [[05_Measuring_Feature_Redundancy_Correlation_and_Distance]]. PCA is one systematic way of resolving that redundancy: instead of manually deciding which correlated feature to drop, PCA mathematically blends correlated features into a smaller set of uncorrelated components.

### Singular Value Decomposition (SVD)

SVD is a more general **matrix factorization** technique from linear algebra. It decomposes any rectangular matrix **X** (rows = data points, columns = features) into the product of three matrices:

$$ X = U \Sigma V^T $$

- **U** — an orthogonal matrix whose columns are called the "left singular vectors."
- **Σ (Sigma)** — a diagonal matrix of "singular values," always arranged in decreasing order of magnitude. These singular values play a role directly analogous to PCA's eigenvalues — they indicate how much of the data's total variation each corresponding direction captures.
- **V^T** — the transpose of an orthogonal matrix whose columns ("right singular vectors") are directly related to PCA's principal-component directions.

**For dimensionality reduction:** keep only the top-k largest singular values (and their corresponding vectors in U and V), discarding the rest — this gives the best possible rank-k approximation of the original matrix, capturing the most significant patterns while discarding the least significant (often noisy) ones.

**Relationship to PCA:** SVD is, in fact, the underlying computational machinery that PCA implementations typically use in practice — running PCA on standardized data is mathematically equivalent to running SVD on that same standardized data matrix. The main practical advantage of SVD is that it can be applied directly to non-square, even very sparse, matrices — making it popular for large-scale applications like recommendation systems (where the data matrix is users × items, mostly empty) and text/document analysis (documents × vocabulary words, also mostly empty, i.e., sparse — recall the sparse-data grouping from [[05_Measuring_Feature_Redundancy_Correlation_and_Distance]]).

### Linear Discriminant Analysis (LDA)

LDA is a **supervised** technique — unlike PCA and SVD, it explicitly uses the class labels of the data during dimensionality reduction, making it specifically suited to classification tasks.

**Core idea:** instead of finding directions of maximum overall variance (like PCA), LDA finds directions that **best separate the known classes** from each other. Concretely, LDA seeks a projection where, simultaneously:
- Data points belonging to the **same class** end up as close together as possible (minimizing within-class scatter).
- The **centers (means) of different classes** end up as far apart as possible (maximizing between-class scatter).

This is achieved by maximizing the ratio of between-class variance to within-class variance — the resulting projection axes are called **linear discriminants**.

**PCA vs. LDA — when to use which:**

| | PCA | LDA |
|---|---|---|
| Uses class labels? | No (unsupervised) | Yes (supervised) |
| Optimizes for | Maximum overall variance in the data | Maximum separability between known classes |
| Best suited for | Exploratory analysis, visualization, general compression, unlabeled data | Classification tasks where you already know class labels and want features optimized specifically to distinguish them |
| Number of usable components | Up to the original number of features | Limited to (number of classes − 1) |

In practice, LDA often outperforms PCA specifically for classification-focused dimensionality reduction, precisely because it optimizes for the thing you actually care about (separating known classes) rather than a generic proxy (overall variance) — but it requires labeled data, which PCA does not.

---

## 2) Simple English Explanation

All three techniques take your pile of original features and squeeze them into a smaller number of *new*, blended features — but each squeezes in a different way, with a different goal.

**PCA — "Find the directions where the data spreads out the most."**
Imagine scattering a handful of rice grains on a table, and the pile happens to naturally stretch out more along one diagonal direction than any other. PCA finds that "longest stretch" direction first (Principal Component 1), then the next-longest stretch direction that's perpendicular to the first (PC2), and so on. If you only keep the first 2–3 of these new directions, you've captured most of how the data varies, using far fewer numbers than the original feature count — and as a nice side-effect, these new directions are guaranteed to not repeat information (unlike your original, possibly redundant, features).

**SVD — "The universal machine behind PCA, that also works on messy, sparse data."**
SVD is a general mathematical recipe for breaking any rectangular table of numbers into three simpler pieces, ordered from "most important pattern" to "least important pattern." Running PCA is, behind the scenes, basically running SVD. What makes SVD extra useful is that it works great even when your data table is mostly empty/zero (like a giant "which user bought which product" table, where most users haven't bought most products) — which is exactly the kind of data that shows up in recommendation systems (Netflix, Amazon) and text analysis.

**LDA — "Find the directions that best separate the known groups."**
Now imagine you already know each rice grain is either "red" or "blue" (labeled classes), and instead of just finding where the whole pile spreads out (PCA's approach), you specifically want to find the direction where red grains and blue grains separate from each other as cleanly as possible — reds clustered tightly together, blues clustered tightly together, and the two clusters as far apart as possible. That's LDA. Because it uses the known labels, it tends to work better than PCA specifically when your end goal is classification (telling groups apart) — but you need labels to use it at all, unlike PCA/SVD which work on unlabeled data too.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Teeno techniques tumhare original features ke dher ko chhote, blended, *naye* features mein compress karte hain — lekin har ek alag tareeke se, alag goal ke saath.

**PCA — "Wo directions dhundo jahan data sabse zyada failaa hua hai."**
Socho tum table pe chawal ke daane bikhraate ho, aur wo pile naturally ek diagonal direction mein sabse zyada faili hui hai kisi aur direction ke muqable. PCA pehle wo "sabse lambi failaav" wali direction dhundta hai (Principal Component 1), phir agli-lambi failaav wali direction jo pehli ke perpendicular ho (PC2), aur aise hi aage. Agar tum sirf pehli 2-3 directions rakho, to tumne data ke zyada tar variation ko capture kar liya, original feature count se kaafi kam numbers mein — aur ek achhi side-effect ye hai ki ye naye directions guaranteed taur pe information repeat nahi karte (unlike tumhare original, shayad redundant, features).

**SVD — "PCA ke peeche ka universal machine, jo messy, sparse data pe bhi kaam karta hai."**
SVD ek general mathematical recipe hai jo kisi bhi rectangular table of numbers ko teen simpler pieces mein todta hai, "sabse important pattern" se "sabse kam important pattern" tak order karke. PCA chalana, peeche se dekha jaaye to, basically SVD chalane jaisa hi hai. SVD ko extra useful ye baat banati hai ki ye tab bhi bahut achha kaam karta hai jab tumhara data table zyada tar khaali/zero ho (jaise ek bahut bada "kaunse user ne kaunsa product khareeda" table, jahan zyada tar users ne zyada tar products nahi khareede) — ye bilkul waisa data hai jo recommendation systems (Netflix, Amazon) aur text analysis mein dikhta hai.

**LDA — "Wo directions dhundo jo known groups ko best separate karti hain."**
Ab socho tumhe pehle se pata hai ki har chawal ka daana ya to "red" hai ya "blue" (labeled classes), aur poore pile ke overall failaav ko dhoondne ke bajaye (PCA ka approach), tum specifically wo direction dhundna chahte ho jahan red daane aur blue daane ek doosre se sabse saaf tarike se separate ho jaayein — reds ek jagah tight cluster mein, blues doosri jagah tight cluster mein, aur dono clusters ek doosre se jitna door ho sake utna door. Yahi LDA hai. Kyunki ye known labels use karta hai, isliye ye PCA se behtar kaam karta hai specifically jab tumhara end goal classification ho (groups ko alag-alag pehchaanna) — lekin isse use karne ke liye labels chahiye hi chahiye, PCA/SVD ke ulat jo unlabeled data pe bhi kaam karte hain.

Sources (web research):
- [A Step-by-Step Explanation of Principal Component Analysis (PCA) — LinkedIn](https://www.linkedin.com/pulse/step-by-step-explanation-principal-component-analysis-sheetal)
- [Principal Component Analysis (PCA): Explained Step-by-Step — Built In](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
- [Principal Component Analysis Made Easy: A Step-by-Step Tutorial — Towards Data Science](https://towardsdatascience.com/principal-component-analysis-made-easy-a-step-by-step-tutorial-184f295e97fe/)
- [Singular Value Decomposition for Dimensionality Reduction in Python — MachineLearningMastery.com](https://machinelearningmastery.com/singular-value-decomposition-for-dimensionality-reduction-in-python/)
- [Dimensionality Reduction Techniques — PCA, LCA and SVD (Medium)](https://medium.com/nerd-for-tech/dimensionality-reduction-techniques-pca-lca-and-svd-f2a56b097f7c)
- [PCA vs LDA — No more confusion! (Medium)](https://medium.com/@seshu8hachi/pca-vs-lda-no-more-confusion-fc21fb8d06e9)
- [Comprehensive Guide on Linear Discriminant Analysis — Analytics Vidhya](https://www.analyticsvidhya.com/blog/2024/03/comprehensive-guide-on-linear-discriminant-analysis/)
- [What Is the Difference Between PCA and LDA? — 365 Data Science](https://365datascience.com/tutorials/python-tutorials/lda-vs-pca/)
