# Topic 4: Evaluation on Small Data — Holdout, Stratified Sampling, and Why One Split Isn't Enough

Source: Lecture 17, slides 11–12 ("Evaluation on 'small' data, 1" and "2", with the instructor's B1…B5 block sketch and the notes "Cross-Validation → k-fold Cross Validation"). Enriched with web research (stratification, variance of a single split).

---

## 1) Technical Explanation

**The holdout method (slide 11).** *Reserve a certain amount of data for testing and use the remainder for training.* Usually **one third for testing, the rest for training** — the same split as [[03_Train_Test_Split_Large_Data_and_Validation_Set]].

**Problem with unbalanced datasets.** With "unbalanced" data, a random sample *might not be representative*: there may be **few or no instances of some classes** in the training or test part.

**Stratified sampling** is the slide's fix — an *advanced version of balancing the data*: **make sure each class is represented with approximately equal proportions in both subsets** (i.e. the same class proportions as the full dataset).

*Worked example (illustrative).* A dataset has 90 healthy and 10 sick patients (10 % sick). A random 1/3 test set of 33 patients could by chance contain 0 sick patients, so recall on the sick class cannot even be measured. Stratified: the test set gets 33 × 0.9 ≈ 30 healthy and ≈ 3 sick; the training set gets 60 healthy and ≈ 7 sick — the 90 : 10 ratio is preserved in both.

**Small data: one split is unreliable (slide 12).** *What if we have a small data set?*
- *The chosen 2/3 for training may **not be representative**.*
- *The chosen 1/3 for testing may **not be representative**.*

So the score depends heavily on **luck of the split**: a different random split can give a quite different accuracy (high variance of the estimate). With little data we also cannot afford to waste a third of it on testing only.

**The instructor's solution (handwriting).** Draw the whole dataset as a bar cut into blocks **B₁ B₂ B₃ B₄ B₅** and write **→ Cross-Validation → k-fold Cross Validation**: let *every* block take a turn as the test set. This is developed fully in [[05_k_Fold_Cross_Validation]]; a second resampling approach, the bootstrap, is in [[06_The_Bootstrap_and_Out_of_Bag_Validation]].

**Summary of choices by data size.**

| Data size | Recommended |
|---|---|
| Large (thousands+) | Single train/test (or train/val/test) split |
| Small | Stratified k-fold cross-validation (often 10-fold), repeated if possible; or bootstrap |
| Imbalanced classes (any size) | Stratify the splits |

---

## 2) Simple English Explanation

**Holdout** means: lock away a part of your data (about one third) as the "exam," and learn from the rest (two thirds).

**Trouble 1 – uneven groups.** Suppose only 10 of 100 patients are sick. If you grab a random third for the exam, by bad luck it might contain **no sick patients at all** — the exam can't test the one thing you care about! **Stratified sampling** fixes this: make sure every group (healthy, sick) appears in the same proportion in both the study pile and the exam pile. Here: roughly 30 healthy and 3 sick in the exam; 60 healthy and 7 sick in the study pile.

**Trouble 2 – little data.** If you have only a small amount of data, any single split can be unlucky: the study pile might not represent everyone, and the exam pile might be unusually easy or hard. So one score can't be trusted.

**Solution (the teacher's sketch):** cut the data into 5 blocks (B1–B5) and let each block take a turn as the exam. That's **cross-validation** — next topic.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Holdout** ka matlab: apne data ka ek hissa (lagbhag 1/3) "exam" ke liye alag rakh do aur baaki 2/3 se seekho.

**Pehli problem – unbalanced groups.** Maan lo 100 mein se sirf 10 patients bimaar hain. Agar tum random 1/3 data test ke liye uthao, to ho sakta hai ki bad luck se usmein **ek bhi bimaar patient na aaye** — yaani exam us cheez ko test hi nahi kar raha jo sabse important thi! **Stratified sampling** iska ilaaj hai: dono hisson (train aur test) mein har class ka ratio wahi rakho jo poore data mein hai. Yahan: test mein ~30 healthy aur ~3 bimaar, train mein 60 healthy aur ~7 bimaar.

**Doosri problem – data kam hai.** Chhote data par koi bhi ek split unlucky ho sakta hai: train wala hissa sabko represent na kare, ya test wala hissa zyada aasaan/mushkil nikle. Isliye ek score par bharosa nahi kar sakte.

**Solution (sir ne board par likha):** data ko 5 blocks (B1–B5) mein todo aur **har block ko ek baar test banne ka mauka do.** Isi ko **Cross-Validation / k-fold Cross Validation** kehte hain — agla topic.
