# Topic 1: The Overall Feature Selection Process, and the Filter/Wrapper/Embedded Approaches

Source: Lecture 11, slides 1–6 ("Overall Feature Selection Process", "Feature Selection Approaches" ×3, "Python libraries for feature selection"). This picks up where [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] from Lecture 10 left off — Lecture 10's slide only *named* Filter/Wrapper/Embedded with zero elaboration, so that file was built entirely from web research. Lecture 11's own slides now supply the instructor's own definitions and a process diagram, so this file presents that slide content directly (not re-derived from scratch) and cross-references Lecture 10's file for the deeper analogy/pros-cons breakdown rather than repeating it.

---

## 1) Technical Explanation

### The overall feature selection process (slide 1)

Regardless of which approach (Filter/Wrapper/Embedded) is used, feature selection as a whole follows one general loop:

```
Original Set → Subset Generation → Subset Evaluation → Stopping Criterion? 
                     ↑                                         │
                     └──────────── No ────────────────────────┘
                                                                │ Yes
                                                          Results Validation
```

1. **Subset Generation** — produce a candidate subset of features from the original set (using some search strategy — could be sequential, random, or exhaustive).
2. **Subset Evaluation** — score that candidate subset against some criterion ("goodness of subset") — this is exactly the point where Filter, Wrapper, and Embedded approaches diverge, since each uses a *different kind* of criterion (see below).
3. **Stopping Criterion** — check whether to keep iterating (generate a new subset and re-evaluate) or stop. Typical stopping conditions: a fixed number of iterations reached, adding/removing more features no longer improves the score, or a target subset size is reached.
4. **Results Validation** — once the loop stops, the chosen subset is validated (e.g., checking it actually performs well on unseen/test data, not just the data used during selection).

This is the general skeleton; what changes between the three approaches below is specifically **how "Subset Evaluation" is done** — using statistics alone, using a trained model's performance, or using signals produced automatically during training.

### Filter Approach

Slide 3's own definition: *"the feature subset is selected based on statistical measures. No learning algorithm is employed to evaluate the goodness of the feature selected. Commonly used metrics include correlation, chi square, Fisher score, ANOVA, Information Gain, etc."*

Flow: `All features → Select the best features (statistically) → Learning algorithm → Performance evaluation`. Note the statistical selection step happens *before* any model sees the data — the learning algorithm only comes in afterward, to actually use the already-chosen features.

### Wrapper Approach

Slide 4's own definition: *"for every candidate subset, the learning model is trained and the result is evaluated by running the learning algorithm. Computationally very expensive but superior in performance. Requires some method to search the space of all possible subsets of features."*

Flow: `All features → [Select features iteratively ⇄ Learning algorithm] → Performance evaluation` — the iterative loop (select → train → evaluate → re-select) is drawn as a closed cycle on the slide, visually matching the general process diagram from slide 1.

### Embedded Approach

Slide 5's own definition: *"These methods encompass the benefits of both the wrapper and filter methods. It includes interactions of features but also maintaining reasonable computational cost. Embedded methods are iterative in the sense that [they take] care of each iteration of the model training process and carefully extract those features which contribute the most to the training for a particular iteration."* Slide examples: **decision trees** (which inherently select features at each split) and **regularization techniques like Lasso**.

Flow: `Set of all features → [Generate a subset ⇄ Learning Algorithm + Performance] → Selecting the best subset` — selection happens *inside* the same loop that trains the model, rather than before it (Filter) or as a separate repeated wrapper around it (Wrapper).

For the fuller mechanical breakdown of *how* each of these three actually computes its criterion (forward/backward selection, RFE, LASSO's L1 penalty, tree-split importance), the pros/cons, and a cricket-team analogy, see [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] from Lecture 10 — that content is not repeated here.

### Python libraries for feature selection (slide 6)

A practical reference table of which Python library implements which method under each approach:

| Method | Sklearn | MLXtend | Feature-engine |
|---|---|---|---|
| **Filter** | Variance, ANOVA, Correlation (with target), Mutual information | — | Cardinality, Duplication, Correlation (among features) |
| **Wrapper** | Forward search, Backward search | Forward search, Backward search, Exhaustive search | — |
| **Embedded** | Lasso, Decision tree importance, Coefficients | — | — |
| **Other** | Recursive feature elimination | — | Recursive feature elimination, Recursive feature addition, Permutation importance, Population Stability Index, Target encoding, Information gain, Probe feature selection, Single feature models, MRMR |

This table matters practically: it tells you that if you're using scikit-learn, filter methods (variance threshold, `SelectKBest` with ANOVA/correlation/mutual-info scoring), wrapper search (`SequentialFeatureSelector`), and embedded methods (`Lasso`, tree `.feature_importances_`) are *all* directly available — you don't need extra libraries for the basics. MLXtend adds exhaustive wrapper search (try literally every subset — only feasible for a small number of features, since the count of subsets grows as 2ⁿ). Feature-engine specializes in the "Other" category — advanced filter-adjacent techniques like MRMR (Minimum Redundancy Maximum Relevance) and permutation importance.

---

## 2) Simple English Explanation

Feature selection, no matter which method you use, always follows the same basic loop: **pick a group of features → check how good that group is → decide whether to try again or stop → double-check the final choice works on new data.** What changes between Filter, Wrapper, and Embedded is only the middle step — *how* "how good is this group" gets measured.

- **Filter** measures goodness using plain statistics (like correlation), *before* any model is even involved — like judging job applicants purely from their resume, no interview.
- **Wrapper** measures goodness by actually training the real model on that group of features and checking its score — like giving every applicant a real trial task, which is thorough but slow and expensive since you repeat it for every combination.
- **Embedded** measures goodness as a side-effect of one single training run — like a probation period where you learn who's valuable while they're already doing the job, instead of a separate round of trials for each combination.

The Python table is just a practical cheat-sheet: scikit-learn alone already gives you tools for all three approaches; you'd reach for MLXtend only if you want to literally try *every* possible subset (exhaustive search), and for Feature-engine if you want fancier techniques like MRMR.

See [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] from Lecture 10 for the full cricket-team analogy and pros/cons of each — this file focuses on the process diagram and the slide's own wording instead of repeating that.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Feature selection, chahe koi bhi method use karo, hamesha isi loop mein chalta hai: **features ka ek group choose karo → check karo ye group kitna achha hai → decide karo dobara try karna hai ya rukna hai → aakhir mein double-check karo ki chosen features naye data pe bhi sahi kaam karte hain.** Filter, Wrapper, aur Embedded mein sirf beech wala step alag hota hai — yaani "kitna achha hai" kaise measure karte ho.

- **Filter** sirf plain statistics se measure karta hai (jaise correlation), koi model involve kiye bina — jaise kisi candidate ko sirf resume dekh ke judge karna, interview liye bina.
- **Wrapper** asli model ko us features ke group pe train karke, uska score dekh ke measure karta hai — jaise har candidate ko ek real trial task dena, jo thorough hai lekin slow aur mehnga bhi, kyunki har combination ke liye ye repeat karna padta hai.
- **Embedded** ek hi training run ke side-effect ke roop mein measure karta hai — jaise ek probation period jahan tum candidate ki value seekh lete ho jabki wo already kaam kar raha hai, alag-alag trials ke bina.

Python table bas ek practical cheat-sheet hai: scikit-learn akele hi teeno approaches ke liye tools deta hai; MLXtend tab chahiye jab tum literally *har* possible subset try karna chaho (exhaustive search), aur Feature-engine tab jab tumhe MRMR jaisi advanced techniques chahiye.

Cricket-team analogy aur har method ke pros/cons ke liye [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] Lecture 10 se dekho — ye file sirf process diagram aur slide ke apne definitions pe focus karti hai, wahi cheez dobara nahi likhi.
