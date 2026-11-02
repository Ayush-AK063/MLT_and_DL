# Topic 2: Data Reduction Techniques — Overview (Feature Selection vs. Feature Extraction)

Source: Lecture 10, slide 6 ("Data Reduction Techniques").

---

## 1) Technical Explanation

The slide presents a two-branch taxonomy of data reduction techniques:

### Branch 1: Feature Selection — "find the best set of features"

This branch **picks a subset of the original features** and discards the rest — no new features are created, the surviving features are literally columns from the original dataset. The slide names three families of methods:
- **Filter methods**
- **Wrapper methods**
- **Embedded methods**

Each of these is explained in depth, with research beyond the slides, in [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]].

### Branch 2: Feature Extraction — "methods of constructing combinations of the variables to get around these problems while still describing the data"

This branch **creates brand-new features** as mathematical combinations (usually linear combinations) of the original ones. The original columns are transformed into a smaller number of new columns, each of which is a blend of the old ones. The slide names three methods:
- **Principal Component Analysis (PCA)**
- **Singular-Valued Decomposition (SVD)**
- **Linear Discriminant Analysis (LDA)**

None of these three are explained on the slides beyond being named — this lecture's slides only give the taxonomy, not the mechanics. Since this is a genuinely new topic not covered elsewhere, full explanations (via web research) are given in [[07_Feature_Extraction_PCA_SVD_LDA]].

### The key conceptual difference

| | Feature Selection | Feature Extraction |
|---|---|---|
| What survives | A subset of the **original** features, unchanged | **New** features, each a combination of originals |
| Interpretability | High — you still know exactly what "feature 3" physically means | Lower — a "principal component" is a weighted blend of many original features, harder to interpret physically |
| Typical use case | When you want to know *which* original measurements actually matter | When you want to compress information into fewer dimensions regardless of which original measurement contributed |

---

## 2) Simple English Explanation

There are two fundamentally different ways to shrink your dataset's feature list:

**Way 1 — Feature Selection: "Pick the best players from the existing team."**
You have, say, 20 original features. You look at all 20 and decide "these 6 are genuinely useful, the other 14 are junk or duplicates" — and you throw away the 14. The 6 that remain are exactly the same columns you started with, untouched. Filter, Wrapper, and Embedded are three different strategies for *how* you decide which 6 to keep (details in [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]]).

**Way 2 — Feature Extraction: "Blend ingredients into a new smaller set of super-ingredients."**
Instead of picking a subset, you mathematically *combine* all 20 original features into, say, 3 brand-new features — each new feature is like a smoothie made from a bit of every original ingredient. You lose the ability to say "this new feature is exactly the original height column," but you can capture almost all the useful information from all 20 originals using far fewer numbers. PCA, SVD, and LDA are three different recipes for making this smoothie (details in [[07_Feature_Extraction_PCA_SVD_LDA]]).

Both approaches solve the same underlying problem (too many dimensions) but in fundamentally different ways — one keeps things transparent and interpretable, the other prioritizes compact, information-dense representations.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Data ke features kam karne ke do fundamentally alag tareeke hain:

**Tareeka 1 — Feature Selection: "Existing team mein se best players chuno."**
Maan lo tumhare paas 20 original features hain. Tum sabko dekh kar decide karte ho ki "in mein se 6 genuinely useful hain, baaki 14 ya to junk hain ya duplicate" — aur us 14 ko hata do. Jo 6 bache, wo bilkul waisi hi hain jaisi shuru mein thi — koi change nahi hua unmein. Filter, Wrapper, aur Embedded — ye teen strategies hain ki *kaise* decide karein kaunse 6 rakhne hain ([[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] mein detail).

**Tareeka 2 — Feature Extraction: "Ingredients ko blend karke naye chhote super-ingredients banao."**
Subset chunne ke bajaye, tum mathematically saare 20 original features ko mix karke, maan lo, 3 bilkul naye features bana dete ho — har naya feature ek "smoothie" jaisa hai jismein har original ingredient ka thoda-thoda hissa hai. Ab tum ye nahi bata sakte ki "ye naya feature bilkul original height column hai" — lekin bahut kam numbers mein tum 20 originals ki almost saari useful information capture kar lete ho. PCA, SVD, aur LDA — ye teen tareeke hain ye smoothie banane ke ([[07_Feature_Extraction_PCA_SVD_LDA]] mein detail).

Dono approach same problem solve karte hain (bahut zyada dimensions), lekin bilkul alag tareeke se — ek transparent aur samajhne-laayak rehta hai, doosra compact aur information-dense representation ko priority deta hai.
