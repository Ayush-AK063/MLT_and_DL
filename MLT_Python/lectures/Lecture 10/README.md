# Lecture 10 — Data Pre-Processing III: Data Reduction (ES514: Machine Learning Techniques)

Source PDF: `Lecture 10 Data Reduction.pdf` (23 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Dimensionality_Reduction_and_Curse_of_Dimensionality.md](01_Dimensionality_Reduction_and_Curse_of_Dimensionality.md) | What dimensionality/dimensionality reduction means, the curse of dimensionality, the optimal-features-vs-performance curve, and the concrete benefits of data reduction |
| [02_Data_Reduction_Techniques_Overview.md](02_Data_Reduction_Techniques_Overview.md) | The two-branch taxonomy: Feature Selection (pick a subset) vs. Feature Extraction (blend into new features) |
| [03_Feature_Selection_Relevance_and_Redundancy.md](03_Feature_Selection_Relevance_and_Redundancy.md) | The two drivers of feature selection — maximizing relevance, minimizing redundancy — and the Roll Number / Age / Height / Weight worked example |
| [04_Feature_Selection_Methods_Filter_Wrapper_Embedded.md](04_Feature_Selection_Methods_Filter_Wrapper_Embedded.md) | Filter, Wrapper, and Embedded feature-selection methods explained in full (research-enriched — slides only name these) |
| [05_Measuring_Feature_Redundancy_Correlation_and_Distance.md](05_Measuring_Feature_Redundancy_Correlation_and_Distance.md) | Correlation coefficient `r`; Minkowski/Euclidean/Manhattan distance; Hamming, Jaccard, SMC (binary features); Cosine similarity; dense-vs-sparse data grouping from the handwritten annotation slide |
| [06_Worked_Examples_Euclidean_Jaccard_Cosine.md](06_Worked_Examples_Euclidean_Jaccard_Cosine.md) | Three fully worked, independently verified numeric examples: Euclidean distance, Jaccard coefficient, Cosine similarity |
| [07_Feature_Extraction_PCA_SVD_LDA.md](07_Feature_Extraction_PCA_SVD_LDA.md) | PCA, SVD, and LDA explained in full (research-enriched — slides only name these), including PCA-vs-LDA comparison |

Every slide across the 23-slide deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference (see note below about the site version).

## Notes on this lecture

- **No recap slide** at the start of this deck — Lecture 10 opens a genuinely new unit (Data Reduction), so there is no `00_` recap file; numbering starts at the first topic.
- **Heavily enriched with web research** for content the slides only name without explaining: [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] (Filter/Wrapper/Embedded methods — slide 6 lists these as three bullet points with zero elaboration) and [[07_Feature_Extraction_PCA_SVD_LDA]] (PCA/SVD/LDA — same situation, slide 6 only names them). Both files were built essentially entirely from research since the source PDF gives no mechanical detail on any of these six techniques.
- **Verified all three worked numeric examples independently** (slides 15–23): Euclidean distance (sum of squared differences = 81.75, distance ≈ 9.04 — the slides never state this final square-rooted answer, only the intermediate table, so it's added in [[06_Worked_Examples_Euclidean_Jaccard_Cosine]]), Jaccard coefficient (0.4, distance 0.6 — matches slide exactly), and Cosine similarity (0.729 — matches slide exactly).
- **Handwritten slide (slide 13)** contains a proximity-measures taxonomy (Euclidean/Minkowski for dense data, Jaccard/Cosine for sparse/discrete data) plus a note that Minkowski with r=1 on binary data is called Hamming distance, and r=∞ is the L∞/L-max norm. This has been folded directly into [[05_Measuring_Feature_Redundancy_Correlation_and_Distance]] alongside the typed slide content on the same topic.
- **Images/graphs added to the site version only** (not the `.md` files, which stay text-only per the existing convention): three slide diagrams — the classifier-performance-vs-dimensionality curve (slide 4), the three correlation scatter plots (slide 11), and the Jaccard-coefficient position grid (slide 19) — were recreated as hand-drawn, theme-aware **inline SVG** (not screenshots/PNGs) and wired into the site via a new `site/diagrams.js` file, keyed by `"<lectureNum>-<topicId>"` and rendered by `app.js` just under the topic heading, above the Technical/Simple/Hinglish tabs. This is a new, narrowly-scoped site feature — `build_site.py` itself is untouched, and `diagrams.js` is hand-written like `app.js`/`style.css`, not generated. Adding a diagram for a future lecture/topic just means adding one more entry to `site/diagrams.js`.
