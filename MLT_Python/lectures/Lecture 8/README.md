# Lecture 8 — Data Transformation & Data Discretization (ES514: Machine Learning Techniques)

Source PDF: `Lecture 8 Data Transformation and Data Discreatization.pdf` (33 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_and_Robust_Scaler_Worked_Example.md](00_Recap_and_Robust_Scaler_Worked_Example.md) | Recap + the 7th scaling method (Interquartile/Robust Scaler), fully worked & verified |
| [01_Aggregation_Generalization_and_Feature_Construction.md](01_Aggregation_Generalization_and_Feature_Construction.md) | Aggregation/Generalization recap; Feature Construction in depth (Label/One-Hot/Dummy Encoding, ranking, Bag-of-Words/TF-IDF/Word Embeddings) |
| [02_Data_Transformation_Formal_Strategies.md](02_Data_Transformation_Formal_Strategies.md) | Formal transformation definition; strategy list showing overlap with Cleaning & Reduction |
| [03_Discretization_Introduction_and_Income_Example.md](03_Discretization_Introduction_and_Income_Example.md) | What discretization is; the income low/medium/high rule |
| [04_Discretization_by_Binning_Equal_Width_and_Frequency.md](04_Discretization_by_Binning_Equal_Width_and_Frequency.md) | Equal-width vs equal-frequency binning — both fully worked & verified (12-value price example) |
| [05_Discretization_by_Clustering.md](05_Discretization_by_Clustering.md) | "Biggest gaps" clustering discretization — worked & verified, compared against both binning methods |
| [06_Concept_Hierarchy.md](06_Concept_Hierarchy.md) | Concept hierarchies for price, location, and time attributes |

Every slide across the 33-page deck is accounted for. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

**Math verification**: The Robust Scaler example (file 00) and both binning + clustering discretization examples (files 04–05) were independently recalculated and confirmed to exactly match the lecture's stated results — including determining that the Robust Scaler's Q1/Q3 were computed via the linear-interpolation percentile method (NumPy/pandas default), not a simple sorted-half-split method.
