# Topic 5: Bootstrap Aggregation (Bagging)

Source: Lecture 22, slides 13–14 ("Bootstrap Aggregation (Bagging)" text; "Bagging: Example" two-panel figure A and B). Enriched with general knowledge (Breiman 1996, variance reduction, OOB).

---

## 1) Technical Explanation

**Slide 13 — the claim.**
- Decision trees are **very sensitive to the data they are trained on**: small changes in the training set can give **significantly different tree structures** (high variance).
- Random forest takes advantage of this by letting **each tree sample with replacement** from the dataset, so different training sets produce different trees.
- This process is called **bagging** (**B**ootstrap **agg**regat**ing**; Breiman, 1996).

**Slide 14 — Panel A: "Bootstrap Sampling and Multiple Trees".** The *Training set* (a 2-D scatter of green **Class A** and red **Class B** points on axes 0–3 and 0–2) is resampled into **Sample 1 … Sample N**; each sample trains **Tree 1 … Tree N**, each producing its own row of predictions (green/red dots).

**Panel B: "Parallel Prediction with Independent Trees".** An input **X** goes to Tree 1, Tree 2, … Tree N **in parallel**. Tree 1 → **Class B**, Tree 2 → **Class A**, Tree N → **Class B**. **Majority Vote** → **Random Forest Decision** (2 B vs 1 A → **Class B**). The legend marks root, split and leaf nodes.

**Algorithm.**
```
for b = 1..B:
    D_b = bootstrap sample of the training set (size m, with replacement)
    T_b = train a tree on D_b
prediction(x) = majority vote of T_1(x)…T_B(x)      (classification)
             or average of T_1(x)…T_B(x)            (regression)
```

**Why bagging reduces variance (standard result).** If B models each have variance σ² and pairwise correlation ρ, the variance of their average is **ρσ² + (1 − ρ)σ²/B**. Increasing B kills the second term, but the first term (ρσ²) remains — so **lowering the correlation ρ between trees** is the other lever. Bootstrapping lowers ρ somewhat; feature randomness lowers it further ([[06_Feature_Randomness_Random_Subset_of_Features_per_Split]]). Bagging mainly reduces **variance**, not bias ([[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17).

**Bagging vs. random forest.** *Bagging* = bootstrap + aggregate any base learner (here trees). A **random forest = bagging of decision trees + random feature subsets at each split.** If you bag trees but let every split consider all features you get "bagged trees", not yet a random forest.

**Out-of-bag (OOB) estimate.** Each tree leaves out ≈ 36.8% of rows ([[04_Random_Sampling_with_Replacement_Bootstrap]]); predicting each row using only the trees that never saw it gives a validation-like accuracy for free (scikit-learn: `oob_score=True`).

**Parallelism.** Trees are independent → can be trained simultaneously ([[07_Bagging_vs_Boosting_Comparison]]).

---

## 2) Simple English Explanation

**The key observation (slide 13).** A decision tree is very **sensitive** to the data it learns from: change a few of the training examples and you can get a quite different tree. Normally that's a weakness. **Bagging turns it into a strength**: if the trees come out different, then a crowd of them gives a more reliable answer than any one of them.

**The recipe.**
1. Make many "practice sets", each by drawing rows at random **with replacement** (balls pulled from a bag and put back).
2. Grow one tree on each practice set. Because the practice sets differ, the trees differ.
3. For a new case, let **every tree vote** and take the majority.

**The name.** **Bagging** is short for **B**ootstrap **agg**regat**ing**: "resample the data (bootstrap), then combine the answers (aggregate)".

**Reading the picture on slide 14.**
- **Left, Panel A — "Bootstrap sampling and multiple trees".** At the top is the training set, a scatter of green dots (Class A) and red dots (Class B). It is resampled into Sample 1 … Sample N, and each sample grows its own Tree 1 … Tree N, each with its own list of predictions.
- **Right, Panel B — "Parallel prediction with independent trees".** A new input X goes to Tree 1, Tree 2 … Tree N **at the same time**. Tree 1 says Class B, Tree 2 says Class A, Tree N says Class B. The **majority vote** is Class B (two against one), so the forest's decision is **Class B**.

**Why does averaging help?** Imagine measuring a table with a wobbly ruler. One measurement may be off in either direction; the average of many measurements is much closer to the truth because the errors cancel. Trees are the same: each is "wobbly" (high variance), and averaging calms the wobble. There is a catch — the errors only cancel if the trees' errors are *different*. If all the trees were identical copies the average would be just as wobbly as one tree. (In maths: ensemble variance = ρσ² + (1−ρ)σ²/B, where σ² is one tree's variance, ρ how alike the trees are, and B how many trees. More trees kills the second part, but the first part remains unless ρ is small.)

**Bagging vs. a random forest.** Bagging = bootstrap samples + vote. A **random forest = bagging of decision trees + a random selection of questions at each split** (next topic). Bagging mostly reduces *variance* (the wobbliness), not bias.

**A free bonus: out-of-bag testing.** Each tree never sees about 37% of the rows. We can test each row using only the trees that never saw it, giving an honest accuracy estimate without setting aside a separate test set.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Main observation (slide 13).** Decision tree apne data ke prati bahut **sensitive** hota hai: training examples thode badlo to kaafi alag tree ban sakta hai. Aam taur par ye kamzori hai. **Bagging ise taakat bana deta hai**: agar trees alag-alag bante hain, to unki bheed kisi bhi ek tree se zyada bharosemand jawaab deti hai.

**Recipe.**
1. Bahut saare "practice sets" banao, har ek rows ko random aur **with replacement** (thaile se ball nikaal kar wapas daal kar) uthakar.
2. Har practice set par ek tree ugao. Practice sets alag hain, isliye trees alag banenge.
3. Naye case ke liye **har tree vote kare** aur majority le lo.

**Naam.** **Bagging** = **B**ootstrap **agg**regat**ing**: "data ko resample karo (bootstrap), phir jawaab jodo (aggregate)".

**Slide 14 ki picture padho.**
- **Left, Panel A — "Bootstrap sampling and multiple trees".** Sabse upar training set hai, hare dots (Class A) aur laal dots (Class B) ka scatter. Use resample karke Sample 1 … Sample N banaye gaye, aur har sample apna Tree 1 … Tree N ugata hai, har ek ki apni predictions ki list.
- **Right, Panel B — "Parallel prediction with independent trees".** Naya input X Tree 1, Tree 2 … Tree N ko **ek saath** jata hai. Tree 1 kehta hai Class B, Tree 2 kehta hai Class A, Tree N kehta hai Class B. **Majority vote** Class B hai (do vs ek), isliye forest ka decision **Class B**.

**Average se fayda kyun?** Socho tum ek dagmagate ruler se mez naap rahe ho. Ek naap kisi bhi taraf galat ho sakta hai; bahut saare naapon ka average sach ke kaafi paas hota hai kyunki galtiyan cancel ho jaati hain. Trees bhi aise hi hain: har ek "dagmagata" hai (high variance), aur average dagmagahat ko shaant karta hai. Ek shart hai — galtiyan tabhi cancel hongi jab trees ki galtiyan *alag-alag* hon. Agar saare trees ek jaise copy hote to average bhi ek tree jitna hi dagmagata. (Maths mein: ensemble variance = ρσ² + (1−ρ)σ²/B, jahan σ² ek tree ka variance, ρ trees kitne milte-julte, aur B trees ki sankhya hai. Zyada trees doosra hissa khatam kar dete hain, par pehla hissa tab tak rehta hai jab tak ρ chhota na ho.)

**Bagging vs random forest.** Bagging = bootstrap samples + vote. **Random forest = decision trees ka bagging + har split par sawaalon ka random selection** (agla topic). Bagging mainly *variance* (dagmagahat) kam karta hai, bias nahi.

**Free bonus: out-of-bag testing.** Har tree lagbhag 37% rows kabhi nahi dekhta. Hum har row ko sirf unhi trees se test kar sakte hain jinhone use nahi dekha, aur bina alag test set rakhe ek imaandaar accuracy estimate mil jata hai.
