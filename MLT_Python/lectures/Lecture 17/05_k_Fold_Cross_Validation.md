# Topic 5: k-Fold Cross-Validation (Stratified Ten-Fold, Repeated CV)

Source: Lecture 17, slides 13–15 ("Cross-validation", "Cross-validation example" with the instructor's "10-fold CV" note, "More on cross-validation"). Enriched with web research (Kohavi 1995 study on why ten folds, leave-one-out).

---

## 1) Technical Explanation

**Definition (slide 13).** Cross-validation is **more useful in small datasets** ([[04_Holdout_Stratified_Sampling_and_the_Small_Data_Problem]]).
1. **Step 1:** split the data into **k subsets (folds) of equal size**.
2. **Step 2:** **each subset in turn is used for testing** and the remainder for training — this is **k-fold cross-validation**.
3. For classification the subsets are often **stratified** before the split.
4. The **error estimates are averaged** to give one overall error estimate.

**The example figure (slide 14).** A row of equal boxes = the data in equal-sized groups. *Hold aside one group for testing (the red box, labelled "Test") and use the rest to build the model; repeat* — the red box moves one position each round (first group, …, last group). The instructor writes **"10-fold CV"** to mean this with k = 10.

**Algorithm.**

```
split data into k folds F1..Fk (stratified for classification)
for i in 1..k:
    train on all folds except Fi
    test on Fi  -> error_i
CV error = (error_1 + ... + error_k) / k
```

**Worked example (illustrative, k = 5 and 10-fold sizes).** 100 examples, 5-fold: each fold has 20; in every round 80 train / 20 test; every example is tested **exactly once** and used for training in k − 1 = 4 rounds. If the five fold accuracies are 0.80, 0.85, 0.75, 0.90, 0.80, the CV accuracy = (0.80+0.85+0.75+0.90+0.80)/5 = **0.82**. For **10-fold**: 10 rounds of 90 train / 10 test. With a stratified 80 : 20 class split each fold has 8 and 2 instances of the two classes.

**Why ten? (slide 15).** *Standard method for evaluation: **stratified ten-fold cross-validation**. Why ten? Extensive experiments have shown that this is the best choice to get an accurate estimate.* (Research: this is the conclusion of Ron Kohavi's 1995 IJCAI study comparing cross-validation and bootstrap — ten-fold stratified CV gave the best bias/variance balance for model selection, even better than the more expensive leave-one-out.) The number is empirical, not a law: 5-fold is a common cheaper alternative.

**Variance reduction (slide 15).**
- **Stratification reduces the estimate's variance.**
- **Repeated stratified CV** is better still: e.g. *ten-fold CV repeated ten times* (different random fold assignments), results averaged → 100 train/test runs, reducing variance further.

**Special case.** **Leave-one-out CV (LOOCV)**: k = n (each fold = one instance). Nearly unbiased but costly and high-variance (research).

**Cost and use.** k-fold CV trains k models. Final deployment model is normally retrained on all the data. CV is also the standard tool for **choosing hyper-parameters** such as k in k-NN ([[03_Issues_and_Choosing_the_Value_of_K]] from Lecture 16): compute the CV error for each candidate k and keep the best. Keep any further test set separate ([[03_Train_Test_Split_Large_Data_and_Validation_Set]]).

**Contrast with bootstrap.** CV samples *without replacement* — each instance sits in exactly one test fold. See [[06_The_Bootstrap_and_Out_of_Bag_Validation]] for sampling *with* replacement.

---

## 2) Simple English Explanation

When data is scarce, a single exam can be unfair. **Cross-validation** gives *everyone a turn*.

1. Cut your data into **k equal piles** (say 5).
2. Round 1: pile 1 is the exam, piles 2–5 are for studying. Record the score.
3. Round 2: pile 2 is the exam, the others are for studying. Record the score.
4. … continue until every pile has been the exam once.
5. **Average** all the scores. That's your final, more trustworthy score.

Example: 100 examples in 5 piles of 20. Each round studies from 80 and is tested on 20. Scores 0.80, 0.85, 0.75, 0.90, 0.80 → average **0.82**.

**Why 10 piles?** The teacher says experiments show **10-fold** gives a very reliable estimate — it's the standard choice. Two extras: **stratified** (every pile has the same class mix, which makes the estimate steadier) and **repeated** (do the whole thing 10 times with different random piles and average everything).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Jab data kam ho to ek akela exam unfair ho sakta hai. **Cross-validation** mein **sabko ek-ek baar mauka** milta hai.

1. Data ko **k barabar piles (folds)** mein todo (maan lo 5).
2. Round 1: pile 1 = exam (test), piles 2–5 = padhai (train). Score likh lo.
3. Round 2: pile 2 = exam, baaki padhai. Score likh lo.
4. … jab tak har pile ek baar exam na ban jaye.
5. Saare scores ka **average** lo — ye hai final, zyada bharosemand score.

Example: 100 examples, 5 piles of 20. Har round mein 80 se seekhte hain aur 20 par test. Scores 0.80, 0.85, 0.75, 0.90, 0.80 → average = (0.80+0.85+0.75+0.90+0.80)/5 = **0.82**. Slide 14 mein lal (red) box wahi pile hai jo us round mein test hai; aage har round mein wo box khisakta jata hai. Sir ne "10-fold CV" likha hai matlab k = 10.

**Dus hi kyun?** Slide ke hisaab se bahut experiments se pata chala ki **10-fold** sabse accurate estimate deta hai — isliye ye standard hai (Kohavi 1995 ki study ka bhi yahi nateeja tha). Do extra cheezein: **Stratified** (har pile mein class ka mix same, isse variance kam) aur **Repeated** (poora process 10 baar alag random piles ke saath, phir average).

k-NN mein sahi k chunne ke liye bhi yahi CV use hoti hai: har k ke liye CV error nikaalo, jo sabse kam ho wahi k rakho.
