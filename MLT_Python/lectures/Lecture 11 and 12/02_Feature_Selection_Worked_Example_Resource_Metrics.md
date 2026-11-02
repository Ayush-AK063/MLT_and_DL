# Topic 2: Applied Worked Example — Feature Selection on Cloud Resource-Utilization Data

Source: Lecture 11, slides 7–9 ("Example" ×3). This example is reproduced from a real research paper: Patel, Y.S., Jaiswal, R. & Misra, R., *"Deep learning-based multivariate resource utilization prediction for hotspots and coldspots mitigation in green cloud data centers"*, J Supercomput 78, 5806–5855 (2022), https://doi.org/10.1007/s11227-021-04107-6 — notably, **Dr. Yashwant Singh Patel, this course's own instructor, is the lead author.** Enriched with web research on the statistical methods named in the table (Kendall's Tau, Granger causality, Mutual Information) that the slides use but don't define.

---

## 1) Technical Explanation

### The dataset (slide 7)

The example works with **cloud data-center resource-usage metrics** — 11 raw features describing how a server/node is using its resources:

| Metric | Description |
|---|---|
| CPU | Usage of aggregated CPU |
| MEM | Usage of aggregated memory |
| MAXM | Maximum memory utilization observed |
| VM | Assigned memory (may or may not be used) |
| MAXC | Maximum CPU utilization (over interval) |
| UPC | Aggregate unmapped page cache |
| TPC | Usage of total page cache |
| CPI | Cycles per instruction over all nodes |
| MAXD | Maximum disk I/O time detected (over interval) |
| DSP | Disk capacity space utilization over all nodes |
| MAI | Memory accesses per instruction over all nodes |
| DIO | Disk I/O time over all nodes |

This is a **real, high-dimensional feature set** of the kind [[01_Dimensionality_Reduction_and_Curse_of_Dimensionality]] from Lecture 10 discusses in the abstract — the paper's goal is to predict resource "hotspots" and "coldspots" (nodes that are over- or under-utilized) in a green (energy-efficient) cloud data center, and it needs to first cut this list down to the metrics that actually matter for the prediction task.

### Applying six different filter methods (slide 8)

The paper runs **six different filter-style feature selection methods** on this 11-feature set (VM is used as a stand-in target/reference column in the table; MAXC is dropped from consideration in some analyses per the paper) and records which features each method flags as relevant (✓) or not (✗):

| Method | VM | MEM | UPC | MAXM | TPC | DIO | MAXC | DSP | MAI | CPI | MAXD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Kendall | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ |
| ANOVA | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ |
| Pearson | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Spearman | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Granger causality | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| Mutual information | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |

Notice: **MEM, UPC, and TPC are selected by every single method** — a strong signal these are genuinely important, relevant features. **MAXM is rejected by five of six methods** — a strong signal it's not useful for this prediction task. Other features (MAXC, DSP, MAI, CPI, MAXD, DIO) get mixed verdicts depending on the method, illustrating a key real-world lesson: **different filter methods can disagree**, because they're measuring different kinds of relationships (linear vs. rank-based vs. causal vs. information-theoretic) — which is exactly why the paper runs six of them rather than trusting just one, and why in practice you'd often look for features that multiple methods agree on.

### What each method actually measures

The slides name six methods without defining most of them. Two (Pearson, Spearman) were already covered under correlation-based redundancy measures in [[05_Measuring_Feature_Redundancy_Correlation_and_Distance]] from Lecture 10; the remaining four are explained here:

- **Kendall (Kendall's Tau, τ):** A rank-based, non-parametric correlation measure — like Spearman, it doesn't assume a linear relationship, but it works differently: it counts **concordant pairs** (where two data points are ranked in the same relative order on both variables) versus **discordant pairs** (ranked in opposite order), and computes τ = (C − D) / [n(n−1)/2], where C and D are the concordant/discordant pair counts and n is the number of observations. τ ranges from −1 (perfect disagreement) to +1 (perfect agreement); it tends to be more robust to small sample sizes and ties than Spearman, and is often preferred in fields (e.g., some finance/reliability applications) where a more interpretable "probability of agreement" reading is useful.
- **ANOVA (Analysis of Variance, F-test):** Tests whether the *means* of a numeric feature differ significantly across groups (e.g., across different target-class labels). It produces an F-statistic — a larger F-score means the feature's values differ more across groups than would be expected by chance alone, suggesting the feature carries information relevant to distinguishing those groups. Commonly used when the target is categorical and the feature is continuous.
- **Granger causality:** A statistical test (from time-series econometrics, introduced by Clive Granger) for whether one time series **helps predict another beyond what the second series' own past values already predict**. Concretely, it compares two forecasting models for a target series *y*: one using only *y*'s own past values, and one using both *y*'s past values *and* a candidate feature *x*'s past values. If adding *x* significantly improves the prediction of *y*'s future, *x* is said to "Granger-cause" *y*. This is naturally suited to this resource-utilization example since it's time-series data (metrics measured over intervals) — a feature like DIO (disk I/O) might not correlate strongly with the target in a simple linear sense, yet still carry genuinely predictive, time-lagged information, which Granger causality can catch but Pearson correlation would miss. Important caveat: despite the name, Granger causality identifies *useful predictors*, not true cause-and-effect relationships in the everyday sense.
- **Mutual Information:** An information-theory measure of how much knowing one variable **reduces uncertainty** about another — formally, the reduction in entropy of the target variable given knowledge of the feature. Unlike Pearson/Spearman/Kendall (all of which are forms of correlation), mutual information can detect **any** kind of statistical dependency, including complex non-linear, non-monotonic relationships that correlation-based measures are blind to. A mutual information score of 0 means the two variables are statistically independent; higher scores mean stronger dependency (of any shape). This is why Mutual Information selects MAI and CPI when several correlation-based methods (Pearson, Spearman, Kendall, ANOVA) reject them — those features may have a non-linear relationship with the target that only an information-theoretic measure picks up.

### Visualizing the six methods' scores (slide 9, Fig. 15)

The paper's Fig. 15 plots each method's raw score per feature as a bar chart, with reference lines at the overall mean score (M), 0.5×M, 0.75×M, and 1.5×M — features scoring above these thresholds are the ones flagged ✓ in the table above. Visually: Pearson and Spearman show MEM/VM as clearly dominant (tallest bars); Granger causality shows a very different pattern with VM scoring near zero (hence ✗ for VM under Granger in the table) while UPC/TPC/DSP score highest; Mutual Information's bars are comparatively flat across most features (all comfortably above threshold) except MAXM and CPI, reflecting that information-theoretic dependency was detected broadly across this feature set.

---

## 2) Simple English Explanation

This example is from a real research paper — written by the very professor teaching this course — about predicting when a cloud-computing server is being overworked ("hotspot") or underused ("coldspot"), which matters for saving energy in data centers. Before building a prediction model, the paper had 11 different measurements of server behavior (like CPU usage, memory usage, disk activity) and needed to figure out which of those actually matter for predicting hotspots/coldspots.

Instead of trusting one method, the paper tried **six different statistical tests** and checked which features each test says are useful. Three features (memory usage, unmapped page cache, total page cache) were picked by *every single test* — that's about as confident as you can be that they matter. One feature (maximum memory observed) was rejected by almost every test — a strong sign to drop it. The rest were a mixed bag, which teaches an important lesson: **different statistical tests look for different kinds of patterns**, so they can genuinely disagree, and no single test is automatically "the right one."

The four new tests explained:
- **Kendall's Tau** — like Spearman's rank correlation (from Lecture 10), but counts how often pairs of values agree in ranking order versus disagree, and turns that into a score.
- **ANOVA** — checks whether a feature's average value looks meaningfully different when you split the data into groups (useful when your target is a category, like "hotspot" vs "not hotspot").
- **Granger causality** — specifically for data measured over time: it checks whether knowing a feature's *past* values genuinely helps predict a target's *future* values, better than just looking at the target's own past. It's less about "does A go up when B goes up" (which correlation checks) and more about "does knowing A's history help forecast B."
- **Mutual Information** — the most flexible of the four: it checks if knowing one variable reduces your uncertainty about another, *no matter what shape* that relationship takes (straight line, curve, anything) — unlike correlation methods, which only really catch straight-line or monotonic relationships.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye example ek real research paper se hai — jo isi course ke professor ne khud likha hai — jisme predict kiya jaata hai ki kab koi cloud-computing server overworked ("hotspot") hai ya underused ("coldspot"), jo data centers mein energy bachane ke liye important hai. Prediction model banane se pehle, paper ke paas server behavior ki 11 alag measurements thi (jaise CPU usage, memory usage, disk activity), aur figure out karna tha ki inme se kaunsi actually hotspot/coldspot predict karne mein kaam aati hain.

Ek method pe bharosa karne ke bajaye, paper ne **chhe alag statistical tests** try kiye aur check kiya har test kaunse features ko useful bolta hai. Teen features (memory usage, unmapped page cache, total page cache) *har ek test* ne select kiye — itna confident tum aur kisi cheez pe nahi ho sakte ki ye important hain. Ek feature (maximum memory observed) ko lagbhag har test ne reject kiya — drop karne ka strong signal. Baaki mixed the, jo ek important lesson sikhata hai: **alag-alag statistical tests alag-alag tarah ke patterns dhundte hain**, isliye ye genuinely disagree kar sakte hain, aur koi ek test automatically "sahi wala" nahi hota.

Chaar naye tests samjhao:
- **Kendall's Tau** — Spearman's rank correlation (Lecture 10 se) jaisa, lekin ye count karta hai ki pairs of values kitni baar ranking order mein agree karte hain versus disagree, aur usse ek score banata hai.
- **ANOVA** — check karta hai ki kisi feature ka average value meaningfully different lagta hai jab data ko groups mein split karo (useful jab target ek category ho, jaise "hotspot" ya "not hotspot").
- **Granger causality** — specifically time ke saath measure hue data ke liye: ye check karta hai ki kisi feature ke *past* values jaanna genuinely target ke *future* values predict karne mein madad karta hai, sirf target ki apni past history dekhne se zyada. Ye "jab A badhta hai to B bhi badhta hai" (jo correlation check karta hai) se zyada "kya A ki history jaanna B forecast karne mein madad karta hai" pe focus karta hai.
- **Mutual Information** — in chaaron mein sabse flexible: ye check karta hai ki ek variable jaanne se doosre ke baare mein uncertainty kam hoti hai ya nahi, *chahe relationship ka shape kuch bhi ho* (straight line, curve, kuch bhi) — unlike correlation methods, jo sirf straight-line ya monotonic relationships pakadte hain.

Sources (web research):
- [Granger Causality - A possible Feature Selection Method in Marketing Mix Modeling (MMM) — TechRxiv](https://www.techrxiv.org/users/778033/articles/919090-granger-causality-a-possible-feature-selection-method-in-marketing-mix-modeling-mmm)
- [Why Aren't More Data Scientists Using Granger Causality? — Medium](https://medium.com/@daniel.kreutzjans/why-arent-more-data-scientists-using-granger-causality-7400c49d10a0)
- [Understanding Kendall's Tau Rank Correlation — Medium](https://ishanjainoffical.medium.com/understanding-kendalls-tau-rank-correlation-c959a7daea56)
- [Feature Selection Based on Mutual Information Gain for Classification and Regression — Medium](https://guhanesvar.medium.com/feature-selection-based-on-mutual-information-gain-for-classification-and-regression-d0f86ea5262a)
- Source paper: Patel, Y.S., Jaiswal, R. & Misra, R. "Deep learning-based multivariate resource utilization prediction for hotspots and coldspots mitigation in green cloud data centers." J Supercomput 78, 5806–5855 (2022). https://doi.org/10.1007/s11227-021-04107-6
