# Topic 5: Measuring Feature Redundancy — Correlation-Based and Distance-Based Measures

Source: Lecture 10, slides 10–14 ("Feature Selection - Measuring Feature Redundancy"), including a handwritten annotation slide (13).

---

## 1) Technical Explanation

Slide 10 states: **"Feature Redundancy is measured in terms of similarity information contributed by features."** Two broad families of similarity measures are named:
- **Correlation-based** features
- **Distance based** features

### Correlation-based redundancy measure (slide 11)

To detect redundant features, **correlation analysis** is performed, producing a correlation coefficient denoted **r** (this is the standard Pearson correlation coefficient). A **threshold** is chosen (e.g., |r| > 0.9) — any pair of features whose correlation exceeds that threshold is flagged as redundant, and one of the pair can typically be dropped.

$$ r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{\left[n\sum x^2 - (\sum x)^2\right]\left[n\sum y^2 - (\sum y)^2\right]}} $$

The slide shows three canonical scatter-plot shapes:
- **Positive correlation** (r is +ve) — as x increases, y tends to increase too; points trend upward left-to-right.
- **Negative correlation** — as x increases, y tends to decrease; points trend downward left-to-right.
- **No correlation** — points scattered with no discernible linear trend.

`r` ranges from −1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 meaning no linear relationship. The closer `|r|` is to 1, the more redundant the two features are considered — because knowing one almost fully tells you the other.

### Distance-based redundancy measures (slides 12–14)

Instead of correlation, redundancy can also be measured via how "close together" two feature vectors are in space — the intuition being that features which behave almost identically (small distance between them) are redundant.

#### Minkowski distance (general form)

$$ d(F_1, F_2) = \sqrt[r]{\sum_{i=1}^{n} (F_{1i} - F_{2i})^r} $$

This is a *family* of distance metrics parameterized by `r`:
- **r = 1 (L1 norm): Manhattan distance** — sum of absolute differences along each dimension (like navigating a city grid where you can only move along streets, not diagonally).
- **r = 2 (L2 norm): Euclidean distance** — the familiar straight-line ("as the crow flies") distance.
- **r = ∞ (L∞ / L-max norm)** — the distance becomes just the single largest absolute difference across all dimensions (from the handwritten annotation on slide 13).

The handwritten slide (13) additionally organizes these under the umbrella term **"Proximity"** — a function of proximity between two objects used to determine similarity (or dissimilarity):
- Euclidean Distance and Minkowski Distance are grouped as suited to **dense data** (e.g., 2D points, where every dimension typically has a meaningful, non-zero numeric value).
- Jaccard or Cosine distance are grouped as suited to **sparse, discrete data** (e.g., documents represented as word-count vectors, where most entries are zero).

This distinction matters practically: Euclidean/Minkowski distances are sensitive to the *absolute magnitude* of differences across all dimensions (which works well for dense numeric data), while Jaccard/Cosine measures are designed to handle vectors where most values are zero and only the *pattern of non-zero entries* (or their relative direction) really matters — which is typical of sparse data like documents (where each dimension is a vocabulary word, and most words don't appear in a given document).

The handwritten slide also notes that when r = 1 in the Minkowski formula applied to *binary* data, the result is called **Hamming distance**, defined as the number of bit positions where two binary vectors differ.

#### Binary-feature similarity metrics (slide 14)

For features whose values are binary (0/1), three metrics are commonly used, all built from four counts:
- `n11` = number of positions where **both** features are 1
- `n00` = number of positions where **both** features are 0
- `n10` = number of positions where feature 1 is 1 and feature 2 is 0
- `n01` = number of positions where feature 1 is 0 and feature 2 is 1

1. **Hamming distance** — the number of positions where the two binary vectors differ, i.e., `n10 + n01`.
2. **Jaccard distance** = 1 − Jaccard Similarity, where:
   $$ \text{Jaccard Similarity} = \frac{n_{11}}{n_{01} + n_{10} + n_{11}} $$
   Note that `n00` (positions where both are 0) is *excluded* from this formula — Jaccard similarity deliberately ignores "both absent" agreement, which matters a lot for sparse data (e.g., two documents both *not* containing a rare word shouldn't count as meaningful similarity).
3. **Simple Matching Coefficient (SMC)**:
   $$ SMC = \frac{n_{11} + n_{00}}{n_{00} + n_{01} + n_{10} + n_{11}} $$
   Unlike Jaccard, SMC *does* count "both zero" as agreement — appropriate when a 0 is just as meaningful as a 1 (e.g., a Yes/No survey feature, where "both said No" is genuine agreement, unlike "both documents lack this rare word").

#### Cosine similarity

$$ \cos(F_1, F_2) = \frac{F_1 \cdot F_2}{|F_1||F_2|} $$

This measures the cosine of the angle between two feature vectors, ranging from −1 (opposite direction) to +1 (same direction), with 0 meaning orthogonal (unrelated) vectors. Unlike Euclidean distance, cosine similarity ignores the *magnitude* of the vectors and only cares about their *direction* — which is why it's popular for sparse, high-dimensional data like text (a short document and a long document repeating the same topic should be considered "similar" even though their raw word-count magnitudes differ wildly).

Fully worked numeric examples for Euclidean distance, Jaccard coefficient, and Cosine similarity (independently verified) are provided in [[06_Worked_Examples_Euclidean_Jaccard_Cosine]].

---

## 2) Simple English Explanation

Two features are "redundant" if they're basically saying the same thing. How do you measure "basically the same thing" mathematically? Two families of tools:

**Family 1 — Correlation (`r`)**
This checks: "when one feature goes up, does the other go up too (or down)?" You get a number between −1 and +1:
- Close to +1: they move together (both up or both down) — very redundant.
- Close to −1: they move in exact opposite directions — also very redundant (just inverted), since knowing one still tells you the other.
- Close to 0: no relationship — not redundant, each carries its own separate information.
You pick a cutoff (a "threshold") — if two features' correlation crosses that cutoff, you call them redundant and can safely drop one.

**Family 2 — Distance/Similarity**
Instead of asking "do they move together," this family asks: "how far apart are these two features, treated as points/vectors?" If they're very close together (small distance) or point in a very similar direction, they're redundant.
- **Euclidean distance** — the ordinary straight-line distance you'd measure with a ruler.
- **Manhattan distance** — distance if you could only move along a grid (like walking city blocks, no diagonal shortcuts).
- **Minkowski distance** — a general formula that includes both Euclidean and Manhattan as special cases (and more).
- **Hamming distance** — for features made of 0s and 1s, simply "how many positions are different between them?"
- **Jaccard similarity** — for 0/1 features, "of all the positions where at least one of us is 1, how many are we both 1?" — a way to measure overlap while intentionally ignoring places where both are simply 0 (since "we both don't have this" often isn't meaningful — think of two shopping lists: both *not* buying eggs isn't really "similarity").
- **Simple Matching Coefficient (SMC)** — same idea as Jaccard, but this time "both are 0" *does* count as agreement — useful when 0 genuinely means something (like a "No" answer on a survey).
- **Cosine similarity** — instead of distance, this measures the *angle* between two vectors. It's used a lot for text data, because it doesn't care if one document is way longer than another (bigger numbers) — it only cares if they "point in the same direction" (talk about similar topics in similar proportions).

The handwritten slide groups these into two practical camps: Euclidean/Minkowski work well for **dense** numeric data (like coordinates), while Jaccard/Cosine work well for **sparse** data where most values are zero (like word-counts in documents).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Do features "redundant" hote hain jab wo basically same baat keh rahe hote hain. Isse mathematically measure karne ke do families hain:

**Family 1 — Correlation (`r`)**
Ye check karta hai: "jab ek feature badhta hai, to doosra bhi badhta hai (ya ghatta hai)?" Tumhe -1 se +1 ke beech ek number milta hai:
- +1 ke paas: dono saath-saath move karte hain (dono badhte ya dono ghatte hain) — bahut redundant.
- -1 ke paas: dono bilkul opposite direction mein move karte hain — ye bhi redundant hai (bas inverted), kyunki ek pata hone se doosra bhi pata chal jaata hai.
- 0 ke paas: koi relationship nahi — redundant nahi, har ek apni alag information deta hai.
Tum ek cutoff (threshold) choose karte ho — agar do features ka correlation us cutoff ko cross kare, to unhe redundant maan lo aur ek ko safely hata do.

**Family 2 — Distance/Similarity**
"Saath move karte hain ya nahi" poochhne ke bajaye, ye poochhta hai: "ye do features, points/vectors samajh ke, kitni door hain ek doosre se?" Agar wo bahut paas hain (chhoti distance) ya similar direction mein point karte hain, to wo redundant hain.
- **Euclidean distance** — ruler se naapi jaane wali seedhi line ki distance.
- **Manhattan distance** — jaise tum sirf grid pe move kar sakte ho (city blocks jaise chalna, koi diagonal shortcut nahi).
- **Minkowski distance** — ek general formula jismein Euclidean aur Manhattan dono special cases ke roop mein aa jaate hain.
- **Hamming distance** — 0 aur 1 wale features ke liye, bas "kitni positions alag hain dono mein?"
- **Jaccard similarity** — 0/1 features ke liye, "un sabhi positions mein se jahan kam se kam ek 1 hai, kitni positions mein dono 1 hain?" — ye overlap measure karta hai lekin jaan-boojh kar un jagah ko ignore karta hai jahan dono sirf 0 hain (kyunki "dono ke paas ye nahi hai" aksar meaningful nahi hota — do shopping lists socho: dono ka eggs na khareedna real "similarity" nahi hai).
- **Simple Matching Coefficient (SMC)** — Jaccard jaisa hi idea, lekin is baar "dono 0 hain" bhi agreement ginte hain — useful jab 0 ka genuinely koi matlab ho (jaise survey mein "No" jawab).
- **Cosine similarity** — distance ke bajaye, ye do vectors ke beech ka *angle* measure karta hai. Text data ke liye bahut use hota hai, kyunki isse fark nahi padta ki ek document doosre se bahut zyada lamba hai (bade numbers) — bas ye dekhta hai ki wo "same direction mein point karte hain" ya nahi (similar topics, similar proportion mein baat karte hain).

Handwritten slide inhe do practical groups mein baantta hai: Euclidean/Minkowski **dense** numeric data ke liye achhe hain (jaise coordinates), jabki Jaccard/Cosine **sparse** data ke liye achhe hain jahan zyada tar values zero hoti hain (jaise documents mein word-counts).
