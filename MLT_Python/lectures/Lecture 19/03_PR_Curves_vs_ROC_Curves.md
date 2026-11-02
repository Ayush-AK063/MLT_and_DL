# Topic 3: PR Curves vs. ROC Curves

Source: Lecture 19, slide 7 ("PR Curves Vs ROC Curves"). Enriched with a worked comparison and web research (Saito & Rehmsmeier, 2015, on PR plots for imbalanced data).

---

## 1) Technical Explanation

**What each curve plots (slide 7).**
- *A ROC curve represents a relation between **sensitivity (recall)** and the **False Positive Rate** (not precision).* ROC plots **TPR vs. FPR**.
- The **PR curve** plots **Precision vs. Recall** (recall on the x-axis, precision on the y-axis).

**When to use which (slide 7).**
- *If your question is "How well can this classifier be expected to perform **in general**?" → go with a **ROC curve**.*
- *If **true negatives are not very valuable** to the problem, or **negative examples are abundant**, then the **PR curve** is typically more appropriate.* For example, *if the class is **highly imbalanced** and positive samples are very rare, use the PR curve.*
- The PR curve answers: ***"How meaningful is a positive result from my classifier?"*** (that is precision.)

**Why the difference arises.** TN appears in the ROC axis FPR = FP/(FP + TN) but **not** in precision = TP/(TP + FP) or recall = TP/(TP + FN) ([[01_Classification_Metrics_Accuracy_Precision_Recall_F1]] from Lecture 18). When negatives vastly outnumber positives, TN is huge, so FPR stays tiny even when there are many false positives, making the ROC curve look excellent while the *precision* is poor.

**Worked example (illustrative, verified).** A test set has **10 positives and 990 negatives**. A model, at some threshold, catches 8 of the 10 positives (TPR = 0.80) and wrongly flags 40 negatives.
- FPR = 40/990 = **0.040** → the ROC point (0.04, 0.80) sits near the top-left: it looks great.
- Precision = TP/(TP + FP) = 8/(8 + 40) = **0.167** — five out of every six alarms are false.
- Recall = 0.80; F1 = 2·0.167·0.8/(0.967) ≈ **0.276**.
So the ROC point says "excellent", the PR point says "mostly false alarms". This is exactly the slide's point: with rare positives use PR.

**Baselines differ.** ROC's random baseline is always the **diagonal** (AUC = 0.5) regardless of class balance. The PR baseline is a **horizontal line at the positive rate** (= prevalence, here 10/1000 = 0.01), so PR AUCs are harder to read in absolute terms but more sensitive to imbalance (research: Saito & Rehmsmeier 2015 argue that the PR plot is more informative than the ROC plot for imbalanced data because it evaluates the fraction of true positives among positive predictions).

**Practical guide.**

| Situation | Prefer |
|---|---|
| Balanced classes; both classes matter | **ROC / AUC** |
| Rare positives (fraud, rare disease); care about the quality of positive alerts | **PR curve** (average precision) |
| Compare how well models *rank* overall | ROC AUC |
| Choose an operating threshold under a precision requirement | PR curve |

Both curves are built from the *same* sorted-score threshold sweep ([[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]]); they just plot different pairs of rates.

**PR points for Example 1 (computed from the slide's table).** After the top 1, 2, 3, … instances the (recall, precision) pairs are (0.2, 1.0), (0.4, 1.0), (0.4, 0.667), (0.6, 0.75), (0.8, 0.8), (0.8, 0.667), (0.8, 0.571), (0.8, 0.5), (1.0, 0.556), (1.0, 0.5) — precision jumps up and down while recall only increases, giving the typical saw-tooth PR curve ([[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]]).

---

## 2) Simple English Explanation

There are two popular "report-card pictures" for a yes/no model:

- **ROC curve:** *catch rate* (TPR) against *false-alarm rate* (FPR). Answers: "Overall, how well can this model tell the two groups apart?"
- **PR curve:** *precision* (when it says yes, how often is it right?) against *recall* (catch rate). Answers: "How trustworthy is a positive result?"

**When does it matter?** When almost everything is negative (say 1 sick person in 100). Then the false-alarm *rate* looks tiny even if you raise lots of false alarms, because it's measured against a huge number of healthy people. The ROC curve then looks wonderful. The PR curve is not fooled, because precision looks directly at "of my alarms, how many were real?"

**Example:** 10 sick, 990 healthy. The model finds 8 of the 10 sick but also wrongly flags 40 healthy people.
- False-alarm rate = 40 ÷ 990 = 4 % → ROC point looks great.
- Precision = 8 ÷ 48 = 17 % → five of every six alarms are false!

**Rule from the slide:** general ability to separate → ROC. Rare positives or negatives don't matter much → PR.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yes/no model ke liye do popular "report card" graphs hain:

- **ROC curve:** *catch rate* (TPR) vs *false-alarm rate* (FPR). Sawaal: "Overall ye model dono groups ko kitna accha alag kar sakta hai?"
- **PR curve:** *precision* (jab model "haan" bole to kitni baar sahi?) vs *recall* (catch rate). Sawaal: "Ek positive result par kitna bharosa kar sakte hain?" (slide: "How meaningful is a positive result from my classifier")

**Farak kab padta hai?** Jab lagbhag sab negative ho (maan lo 100 mein 1 bimaar). Tab false-alarm **rate** bahut chhota dikhta hai chahe kitne hi false alarm ho, kyunki wo bahut saare healthy logon se divide hota hai. Isliye ROC curve bahut accha dikhta hai. PR curve dhokha nahi khaata, kyunki precision seedha dekhta hai "mere alarms mein se kitne asli the?"

**Example:** 10 bimaar, 990 healthy. Model 10 mein se 8 bimaar pakadta hai par 40 healthy ko galti se flag kar deta hai.
- FPR = 40 ÷ 990 = **4%** → ROC point accha dikhta hai.
- Precision = 8 ÷ 48 = **17%** → har 6 alarm mein se 5 jhoothe!
- F1 sirf ≈ 0.28.

**Slide ka rule:** general separation ability → **ROC**. Positives bahut rare hain ya true negatives zyada kaam ke nahi → **PR curve**.

Baseline bhi alag hota hai: ROC ka random baseline hamesha diagonal (AUC 0.5); PR ka baseline ek horizontal line hai jo positive rate par hoti hai (yahan 0.01).
