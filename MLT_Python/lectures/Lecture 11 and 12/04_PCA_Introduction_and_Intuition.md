# Topic 4: Principal Component Analysis — Definition, Key Facts, and Geometric Intuition

Source: Lecture 11, slides 13–17 ("Principal Component Analysis" ×5). Builds on the conceptual PCA overview already given in [[07_Feature_Extraction_PCA_SVD_LDA]] from Lecture 10 — that file covered the algorithm steps from web research since Lecture 10's slides gave zero mechanical detail; this lecture's slides now supply the instructor's own definitions, terminology, and diagrams, which this file presents directly.

---

## 1) Technical Explanation

### Definition (slide 13)

> **Principal Component Analysis (PCA):** It is a technique of dimensionality reduction which performs the said task by reducing the higher-dimensional feature-space to a lower-dimensional feature-space. It also helps to make visualization of large datasets simple.

The slide's own diagram shows this concretely: a 3D "original data space" (three gene-expression axes: Gene 1, Gene 2, Gene 3) containing several colored clusters of points lying roughly on a slanted plane, transformed by PCA into a 2D "component space" (axes PC1, PC2) where the same clusters are now clearly separated and plotted on a flat grid. The key visual insight: the clusters were always separable — PCA just re-orients the axes so that separability becomes visible in fewer dimensions, rather than being "hidden" across three original axes.

### Key facts about PCA (slides 14–15)

- **Principal components are new features constructed as linear combinations (mixtures) of the initial feature set.** This matches the formal definition from [[03_Feature_Extraction_Recap]]: each PC is some weighted sum of the original features, e.g. PC₁ = w₁F₁ + w₂F₂ + ... + wₙFₙ.
- **The newly constructed principal components are all uncorrelated with each other.** Even if the original features were highly correlated/redundant (recall [[05_Measuring_Feature_Redundancy_Correlation_and_Distance]] from Lecture 10), PCA guarantees its output axes carry no linear redundancy between them — each PC captures genuinely distinct information.
- **PCA preserves as much of the original dataset's information as possible** while still achieving the reduction — it isn't an arbitrary reduction, it's specifically the reduction that loses the least.
- **Principal components are denoted PCᵢ**, where i = 0, 1, 2, 3, ..., n depending on the number of features in the original dataset (i.e., you can compute as many PCs as there were original features, though you'd typically keep only the first few).
- **PC1 alone explains the largest share of information** about the original feature set; each subsequent PC (PC2, PC3, ...) explains a progressively smaller share, in strictly decreasing order.

### The scree plot — visualizing decreasing information (slide 16)

The slide shows a bar chart titled "Percentage of explained variances" against "Principal Components" (1 through 10) — this type of chart is commonly called a **scree plot**. In the example shown, PC1 explains roughly 41% of the total variance, PC2 about 18%, PC3 about 12%, dropping steeply and then leveling off toward PC8–PC10 (each explaining only a few percent). This is exactly the decreasing-information pattern stated in the facts above, made visual — and in practice, a scree plot like this is how you decide **how many components to keep**: you look for the "elbow" (the point where the bars stop dropping steeply and start flattening out), since components past that point add little additional information for the cost of keeping an extra dimension.

### Geometric intuition (slide 17)

> "Geometrically, it can be said that principal components are lines pointing the directions that capture the maximum amount of information about the data. Simply, principal components are new axes to get better data visibility with clear difference in observations."

In other words: instead of viewing your data along the original, arbitrary measurement axes (e.g., "Age" axis, "Salary" axis), PCA finds new axes — rotated versions of the original coordinate system — chosen specifically so that the data's spread (variance) is maximized along the first new axis, then the next-most along a second axis perpendicular to the first, and so on. Viewed along these new axes, patterns and differences between data points that were hard to see along the original axes often become visually obvious — exactly as illustrated in the Gene 1/2/3 → PC1/PC2 diagram on slide 13.

---

## 2) Simple English Explanation

PCA is a technique that takes data with a lot of measurements (dimensions) and re-expresses it using fewer new measurements, while keeping as much of the important information as possible — and as a bonus, makes the data much easier to visualize and understand.

Think of it like photographing a 3D object with a camera. Standing at a random angle, the photo might make the object look confusing or overlapping. But there's usually *some* angle from which the photo shows the object's shape most clearly — the most "spread out" and informative view. PCA finds exactly that best angle (and the second-best angle perpendicular to it, and so on), and re-describes your data as if viewed from those best angles instead of the original, arbitrary ones you started with.

Key things to remember about PCA's new "photograph axes" (the principal components):
- Each one is a **mix** of the original measurements, not a single original measurement kept as-is.
- They never repeat information — each one shows you something genuinely new that the others don't.
- The first one (PC1) always shows you the *most* useful view; each next one shows progressively less.
- A **scree plot** (bar chart of how much each PC explains) helps you decide where to stop — usually you stop once the bars flatten out, because the remaining PCs aren't adding much.

---

## 3) Hinglish Explanation (Beginner-Friendly)

PCA ek technique hai jo bahut saari measurements (dimensions) wale data ko lekar usse kam nayi measurements mein re-express karti hai, jabki zyada se zyada important information bachaye rakhti hai — aur bonus mein, data ko visualize karna aur samajhna bhi bahut aasan ban jaata hai.

Isse aise socho jaise kisi 3D object ki photo kisi camera se khींchna. Random angle pe khade ho ke photo confusing ya overlapping lag sakti hai. Lekin usually *koi* angle aisa hota hai jahan se photo object ki shape sabse clearly dikhati hai — sabse "failaa hua" aur informative view. PCA exactly wahi best angle dhundta hai (aur doosra-best angle jo pehle ke perpendicular ho, aur aise hi aage), aur tumhare data ko un best angles se dekha hua describe karta hai, original arbitrary angles se nahi.

PCA ke naye "photograph axes" (principal components) ke baare mein yaad rakhne wali baatein:
- Har ek original measurements ka **mix** hai, koi single original measurement as-is nahi rakha jaata.
- Ye kabhi information repeat nahi karte — har ek tumhe kuch genuinely naya dikhata hai jo doosre nahi dikhate.
- Pehla wala (PC1) hamesha sabse *zyada* useful view dikhata hai; har agla progressively kam dikhata hai.
- Ek **scree plot** (bar chart jo dikhata hai har PC kitna explain karta hai) ye decide karne mein madad karta hai ki kahan rukna hai — usually tum tab rukte ho jab bars flat ho jaayein, kyunki baaki PCs zyada kuch add nahi kar rahe.
