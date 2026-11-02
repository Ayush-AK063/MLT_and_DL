# Topic 4: Distance Metrics Used with k-NN

Source: Lecture 16, slide 7 ("Distance Metrics" — "Figure 1. Equations of selected distance functions", x and y are vectors of m attribute values). Enriched with web research (Minkowski family special cases, when each metric is used, Mahalanobis for k-NN).

---

## 1) Technical Explanation

k-NN needs a rule for "how far apart are two records?" ([[03_Issues_and_Choosing_the_Value_of_K]], issue ②). Slide 7 is a single figure listing **twelve** distance functions. In every formula below, **x** and **y** are two records, each a vector of **m** attribute values (x₁…x_m and y₁…y_m).

### The three you will use most (Minkowski family)

| Name | Formula (as on the slide) | Meaning |
|---|---|---|
| **Minkowski** | D(x,y) = ( Σᵢ₌₁..m \|xᵢ − yᵢ\|^r )^(1/r) | General family with a tunable exponent r |
| **Euclidean** | D(x,y) = √( Σᵢ (xᵢ − yᵢ)² ) | Straight-line ("as the crow flies") distance — Minkowski with **r = 2** |
| **Manhattan / city-block** | D(x,y) = Σᵢ \|xᵢ − yᵢ\| | Sum of absolute differences, like walking city blocks — Minkowski with **r = 1** |

(Research note) Minkowski with **r → ∞** becomes **Chebyshev**, below. Euclidean is the most commonly used default for k-NN; Manhattan is less sensitive to a single huge difference in one feature because it doesn't square it.

**Worked mini-example (verified).** x = (1, 2), y = (4, 6): differences are 3 and 4.
- Manhattan = 3 + 4 = **7**
- Euclidean = √(9 + 16) = √25 = **5**
- Chebyshev = max(3, 4) = **4**
- Minkowski r = 3 → (27 + 64)^(1/3) = 91^(1/3) ≈ **4.498**

Note the ordering Manhattan ≥ Euclidean ≥ … ≥ Chebyshev: as r increases the distance shrinks toward the largest single difference.

### The rest of the figure

| Name | Formula (slide) | What it does / when it is used |
|---|---|---|
| **Chebyshev** | D(x,y) = maxᵢ \|xᵢ − yᵢ\| | Only the *largest* single-attribute gap matters ("chessboard distance"); Minkowski with r = ∞ |
| **Camberra** (standard spelling: **Canberra**) | D(x,y) = Σᵢ \|xᵢ − yᵢ\| / ( \|xᵢ\| + \|yᵢ\| ) | Each term is a *relative* difference, so small values near zero weigh heavily; suited to non-negative data |
| **Quadratic** | D(x,y) = (x − y)ᵀ Q (x − y) = Σⱼ ( Σᵢ (xᵢ − yᵢ) qⱼᵢ ) (xⱼ − yⱼ) | Q is a **problem-specific positive-definite m×m weight matrix** that lets some attributes (and attribute *pairs*) count more |
| **Mahalanobis** | D(x,y) = [det V]^(1/m) (x − y)ᵀ V⁻¹ (x − y) | V is the **covariance matrix** of attributes A₁…A_m (vector of values of attribute j over the training instances 1…n). Accounts for correlation between features and for their different spreads |
| **Correlation** | D(x,y) = Σᵢ (xᵢ − x̄ᵢ)(yᵢ − ȳᵢ) / √( Σᵢ (xᵢ − x̄ᵢ)² Σᵢ (yᵢ − ȳᵢ)² ) | x̄ᵢ = ȳᵢ = *average value for attribute i in the training set*. As written this is the Pearson **correlation coefficient** (similarity); to use it as a distance one normally takes **1 − r** |
| **Chi-square** | D(x,y) = Σᵢ (1/sumᵢ) ( xᵢ/size_x − yᵢ/size_y )² | sumᵢ = sum of all values for attribute i in the training set; size_x = sum of all values in vector x. Designed for **count/histogram data** |
| **Kendall's Rank Correlation** | D(x,y) = 1 − (2 / (n(n−1))) Σᵢ₌₁..m Σⱼ₌₁..i−1 sign(xᵢ − xⱼ) sign(yᵢ − yⱼ) | sign(x) = −1, 0 or 1 if x < 0, x = 0, or x > 0. Compares the **rank ordering** of attributes in x vs. y rather than their values |

**How the figure's notation reads.** `Σᵢ₌₁..m` means "add up over all m features"; `|…|` is absolute value; `max` takes the largest term. The Quadratic and Mahalanobis rows are **matrix** formulas — their special case with Q = identity matrix (or V = identity) reduces to *squared* Euclidean distance (for Mahalanobis, the determinant factor is 1).

**Practical guidance (research).**
- No single metric is best on every dataset; Euclidean and Manhattan are the strong, common defaults, and the best choice is found empirically (e.g. with cross-validation, like k).
- **Feature scaling matters for all of these**: if one attribute is measured in the hundreds and another in decimals, the big-range attribute dominates the distance. This lecture's own movie example shows the problem — see [[06_Worked_Example_Predicting_Movie_Genre]] and [[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]].
- For binary/set data the related **Jaccard** and **cosine** measures are used instead — see [[06_Worked_Examples_Euclidean_Jaccard_Cosine]] from Lecture 10.
- Computing the *squared* Euclidean distance (skip the square root) gives the same neighbor ranking and is faster — used in [[07_Worked_Example_Paper_Tissue_Classification]].

---

## 2) Simple English Explanation

To find the "nearest" neighbors we first need a way to measure **how different two things are**. The slide shows a menu of 12 "rulers." They all take two records and give back one number: **small = very similar, big = very different.**

The three everyday ones:
- **Euclidean** — the straight line between two points, like a bird flying. (Square the gaps, add, take the square root.)
- **Manhattan** — walk only along the streets like in a city grid: add up the horizontal gap and the vertical gap.
- **Minkowski** — a "master ruler" with a dial (r). Dial = 1 gives Manhattan, dial = 2 gives Euclidean.

Try it: two points (1, 2) and (4, 6). The gaps are 3 across and 4 up.
- Manhattan: 3 + 4 = 7 blocks of walking.
- Euclidean: √(3² + 4²) = √25 = 5 — a straight shortcut.
- Chebyshev: just the biggest gap, 4.

The fancier rulers:
- **Chebyshev** — only the single biggest difference counts.
- **Canberra** — measures differences *relative* to how big the values are.
- **Mahalanobis / Quadratic** — smart rulers that know some features are related or more important than others (they use a table of weights/relationships).
- **Correlation, Kendall** — check whether two records *rise and fall together* (their pattern/order) rather than their exact values.
- **Chi-square** — used for count data (like word counts).

One warning: if one feature is measured in big numbers (like 160 minutes) and another in small ones (like 7.4 stars), the big one will drown out the small one. Fix the scales first.

---

## 3) Hinglish Explanation (Beginner-Friendly)

k-NN mein "sabse paas" decide karne ke liye hume ek **scale/ruler** chahiye jo do records ke beech ka farak naape. Slide 7 mein aise **12 distance formulas** ki list hai. Sab ek hi kaam karte hain: do records lo, ek number do — **chhota number = bahut similar, bada number = bahut alag.**

Teen sabse common:
- **Euclidean** — seedhi line wala distance (jaise chidiya udke jaaye). Gap ka square, sab jodo, phir square root.
- **Manhattan (city-block)** — jaise sheher mein sirf galiyon (grid) se chalte ho: horizontal gap + vertical gap jodo.
- **Minkowski** — ek "master formula" jisme ek dial (r) hai. r = 1 → Manhattan, r = 2 → Euclidean.

Example: points (1, 2) aur (4, 6). Gap 3 (aage) aur 4 (upar).
- Manhattan: 3 + 4 = **7**
- Euclidean: √(9+16) = √25 = **5**
- Chebyshev: sabse bada gap = **4**

Baaki formulas:
- **Chebyshev** — sirf sabse bada gap ginta hai.
- **Canberra** (slide mein "Camberra" likha hai, spelling Canberra hoti hai) — gap ko values ke size ke hisaab se relative naapta hai.
- **Quadratic / Mahalanobis** — smart rulers hain jo jaante hain ki kuch features aapas mein related hain ya zyada important hain (inme matrix use hota hai; covariance matrix V wala Mahalanobis hai).
- **Correlation, Kendall** — dekhte hain ki do records ka pattern/order ek jaisa upar-neeche ho raha hai ya nahi.
- **Chi-square** — count wale data (jaise word counts) ke liye.

Dhyaan do: slide ka correlation formula asal mein similarity (r) deta hai; ise distance banane ke liye aam taur par **1 − r** lete hain.

⚠️ Ek zaroori baat: agar ek feature bade numbers mein hai (jaise duration 160 min) aur dusra chhote mein (jaise rating 7.4), to bada wala sab kuch daba dega. Isliye distance naapne se pehle features ko **same scale** par laana chahiye — aage movie example mein ye problem dikhegi.
