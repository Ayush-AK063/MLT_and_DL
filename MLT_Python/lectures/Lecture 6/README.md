# Lecture 6 — Data Cleaning Methods (ES514: Machine Learning Techniques)

Source PDF: `Lecture 6 Data Cleaning Methods.pdf` (43 slides — very detailed, math/worked-example heavy)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_and_Correction_on_ESS_Tour.md](00_Recap_and_Correction_on_ESS_Tour.md) | Recap of Lecture 5 + a correction about the "ESS Tour" content |
| [01_Structured_Data_and_Types_of_Features.md](01_Structured_Data_and_Types_of_Features.md) | Structured data (Iris example), full feature-type taxonomy |
| [02_Data_Preprocessing_Overview_and_Need.md](02_Data_Preprocessing_Overview_and_Need.md) | Definition, "90% of ML effort," incomplete/noisy/inconsistent data |
| [03_Preprocessing_Needs_for_Unstructured_Data.md](03_Preprocessing_Needs_for_Unstructured_Data.md) | Text (lowercase, stopwords, stemming) & image (resize, denoise, segmentation) prep |
| [04_Data_Quality_Dimensions.md](04_Data_Quality_Dimensions.md) | Accuracy, completeness, consistency, timeliness, believability, interpretability |
| [05_Data_Preprocessing_Four_Major_Tasks.md](05_Data_Preprocessing_Four_Major_Tasks.md) | Cleaning → Integration → Transformation → Reduction pipeline |
| [06_Data_Cleaning_Introduction_and_Real_World_Example.md](06_Data_Cleaning_Introduction_and_Real_World_Example.md) | Data cleaning definition + instructor's own published research (turbofan RUL/CMAPSS) |
| [07_Missing_Values_Concepts_and_Handling_Techniques.md](07_Missing_Values_Concepts_and_Handling_Techniques.md) | Missing value causes; remove/manual-fill/imputation overview |
| [08_Missing_Values_Worked_Example_Remove_and_Manual_Fill.md](08_Missing_Values_Worked_Example_Remove_and_Manual_Fill.md) | Forest-fires dataset worked example: removing rows vs manual fill |
| [09_Missing_Values_Imputation_Methods.md](09_Missing_Values_Imputation_Methods.md) | Mean/median/mode imputation (worked), outlier caveat, hot/cold deck, nearest neighbor |
| [10_Noisy_Data_Detection_Boxplot_and_Scatter.md](10_Noisy_Data_Detection_Boxplot_and_Scatter.md) | Noise definition, boxplot/scatter detection, causes, smoothing techniques overview |
| [11_Binning_Method_Worked_Example.md](11_Binning_Method_Worked_Example.md) | Full binning walkthrough (9-number example): mean/boundary/median smoothing |
| [12_Outlier_Analysis_and_Detection_Methods.md](12_Outlier_Analysis_and_Detection_Methods.md) | Univariate/multivariate outliers; IQR method (chapati example); Z-score method |
| [13_Regression_Smoothing_and_Inconsistent_Data.md](13_Regression_Smoothing_and_Inconsistent_Data.md) | Regression for smoothing; resolving inconsistent data |

Every slide across the 43-page deck is accounted for — nothing skipped, including every worked numeric example and formula. Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — no images, per current preference.

**Note**: This lecture's recap slide confirms the "European Spallation Source (ESS) Tour" content flagged in Lecture 5's notes was likely an intentional real-world example (tied to "scientific/machine-generated unstructured data"), not a stray file-mixing error as originally guessed — see file 00 for the correction.
