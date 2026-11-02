# Topic 1: What Is a ROC Curve? — Ranking Instead of Classifying, and How the Curve Is Built

Source: Lecture 19, slides 4, 8, 9 and 10 ("ROC Curves" definition with the instructor's "show performance of classification models", "Ranking instead of classifying" with the sliding-threshold confusion matrices, and "ROC curves" with the Observations list). Enriched with web research (origin in radar signal detection).

---

## 1) Technical Explanation

**Definition (slide 4).**
- *A **receiver operating characteristic curve**, i.e. **ROC curve**, is a graphical plot that illustrates the diagnostic ability of a **binary classifier system as its discrimination threshold is varied**.*
- It is used to evaluate *the accuracy of a test to discriminate diseased cases from normal cases.*
- *A ROC curve is a way to **compare diagnostic tests**. It is a plot of the **true positive rate against the false positive rate**.*
- Instructor's note: **"Show performance of classification models."**

**Axes.** x-axis = **FPR = FP/(FP + TN)**; y-axis = **TPR = TP/(TP + FN)** ([[00_Recap_TPR_FPR_and_the_Blood_Test_Threshold_Idea]]). Both lie in [0, 1], so the plot is a unit square.

**Ranking instead of classifying (slides 8–9).** *Classifiers such as logistic regression can output a **probability** of belonging to a class (or something similar)* ([[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15). We can use this to **rank** the instances and take action on the cases at the top of the list — e.g. *we may have a budget, so we must target the most promising individuals*. Ranking also lets us visualize performance with many techniques (ROC being the main one).

**One ranking → many confusion matrices (slide 9).** Sort the instances by **score**, highest first (slide: 0.99, 0.98, 0.96, 0.90, 0.88, 0.87, 0.85, 0.80, 0.70 with true class 1 or 0). Putting the **threshold** at different positions in the list — "everything above the line is predicted positive (Y), everything below negative (N)" — gives a different confusion matrix each time. The slide shows five matrices (p/n are the actual positive/negative columns; Y/N the predicted rows), for a dataset of 100 positives and 100 negatives:

| Threshold position | TP (Y,p) | FP (Y,n) | FN (N,p) | TN (N,n) | TPR = TP/100 | FPR = FP/100 |
|---|---|---|---|---|---|---|
| above everything | 0 | 0 | 100 | 100 | 0 | 0 |
| after top-1 region | 1 | 0 | 99 | 100 | 0.01 | 0 |
| further down | 2 | 0 | 98 | 100 | 0.02 | 0 |
| further down | 2 | 1 | 98 | 99 | 0.02 | 0.01 |
| further down | 6 | 4 | 94 | 96 | 0.06 | 0.04 |

Each row is **one point (FPR, TPR)**. Sliding the threshold from the top of the list to the bottom traces out the ROC curve. (The instructor's note on slide 5: **threshold ↑ → fewer predicted positives; threshold ↓ → more.**)

⚠️ *Caveat:* the slide is "adapted from [1]" and shows only 9 of the instances while the matrices count 200 (100 + 100); the last matrix (6 TP, 4 FP) does not match the 9 listed rows one-for-one (those would give 5 TP, 4 FP down to 0.70), so treat the matrices as an illustration of the idea, not a row-by-row calculation.

**Reading the ROC plot (slide 10, "Observations").** *ROC curves are a very general way to represent and compare the performance of different models (on a binary classification task).* In the slide's figure an orange piece-wise curve rises from (0,0) towards the top-left star labelled **"Perfection"**, with a blue dashed diagonal labelled **"Random guessing"**; small confusion-matrix thumbnails mark the points.

| Point / feature | Meaning |
|---|---|
| **(0, 0)** | Threshold so high that the model **predicts always negative** (TP = FP = 0) |
| **(1, 1)** | Threshold so low that it **predicts always positive** (FN = TN = 0) |
| **(0, 1) — top-left corner** | **Perfection**: all positives caught, no false alarms |
| **Diagonal line** (TPR = FPR) | **Random classifier** |
| **Below the diagonal** | **Worse than random** (predictions systematically inverted) |
| Curves of different classifiers | Can be **compared** on one plot |
| **AUC** | *Probability that a randomly chosen positive instance will be ranked ahead of a randomly chosen negative instance* — see [[02_ROC_Shapes_AUC_and_Comparing_Models]] |

**Origin (research).** The term comes from **signal detection theory** developed in World War II for radar: the "receiver operator" had to decide whether a blip was an enemy aircraft or noise, and the curve described how well they traded correct detections against false alarms. It was later adopted in medicine (diagnostic tests, hence "diseased vs. normal" on the slide) and machine learning.

**Building a ROC curve — algorithm.**
1. Sort instances by score, descending; let P = number of positives, N = number of negatives.
2. Start at (0, 0). Walk down the list: for a **positive** instance move **up** by 1/P; for a **negative** instance move **right** by 1/N.
3. End at (1, 1). Worked in [[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]] and [[05_Worked_Example_2_Trapezoid_Rule_AUC_0_64]].

---

## 2) Simple English Explanation

**The problem:** many models don't just say "yes/no"; they give a **score** (like a probability). To turn a score into yes/no you pick a **cut-off**. Pick a high cut-off → you say "yes" rarely (few false alarms, but you miss real cases). Pick a low cut-off → you say "yes" a lot (you catch most real cases, but make many false alarms).

**Ranking:** line everyone up from highest score to lowest. Drawing the cut-off line at different places gives different scoreboards (confusion matrices). Slide 9 shows five of them.

**The ROC curve** is just a picture of all those scoreboards at once:
- **Across (x-axis):** false-alarm rate (FPR).
- **Up (y-axis):** catch rate (TPR).
- Each possible cut-off gives one dot; joining the dots gives the curve.

**How to read it:**
- **Bottom-left (0,0):** the model says "no" to everyone.
- **Top-right (1,1):** the model says "yes" to everyone.
- **Top-left corner:** perfect — catches everything, no false alarms. ⭐
- **Diagonal line:** pure guessing (coin flip).
- **Below the diagonal:** worse than guessing.
- **AUC (area under the curve):** one number summarizing the curve; it equals the chance that a random positive person gets a *higher* score than a random negative person.

**Easy way to draw it:** sort by score; for each real-positive step **up**, for each real-negative step **right**.

History fun-fact: ROC comes from World War II radar operators who had to decide "plane or noise?"

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Problem:** bahut se models sirf "haan/na" nahi bolte, wo ek **score** (jaise probability) dete hain. Is score ko haan/na mein badalne ke liye **cut-off (threshold)** chunna padta hai. Cut-off **bada** rakho → "haan" kam bolega (false alarm kam, par asli cases chhoot jayenge). Cut-off **chhota** rakho → "haan" zyada bolega (zyada asli cases pakdega, par false alarm bhi zyada).

**Ranking:** sabko highest score se lowest score tak line mein lagao. Cut-off ki line alag-alag jagah kheenchne par alag-alag scoreboard (confusion matrix) bante hain — slide 9 mein 5 aise matrices dikhaye hain. Sir ke note ke hisaab se: **threshold ↑ → positive kam; threshold ↓ → positive zyada.**

**ROC curve** in sab scoreboards ki ek hi tasveer hai:
- **x-axis (aage):** FPR (false alarm rate)
- **y-axis (upar):** TPR (catch rate / recall)
- Har cut-off ek **dot** deta hai; dots jodne par curve ban jata hai.

**Kaise padhein:**
- **(0,0) neeche-baayein:** model sabko "na" bolta hai (always negative).
- **(1,1) upar-daayein:** model sabko "haan" bolta hai (always positive).
- **(0,1) upar-baayein corner:** **perfect** — sab pakde, koi false alarm nahi ⭐ (slide mein "Perfection").
- **Diagonal line:** random guessing (sikka uchhalna).
- **Diagonal ke neeche:** random se bhi **bura**.
- **AUC:** curve ke neeche ka area — ek number mein poori kahani; matlab ek random positive ko random negative se **zyada score** milne ki probability.

**Curve banane ka aasaan tareeka:** score se sort karo; har **asli positive** par **upar** chalo (1/P), har **asli negative** par **daayein** chalo (1/N). Poora worked example aage hai.

Fun fact: ROC ka naam WWII ke radar operators se aaya, jinhe decide karna tha ki "jahaz hai ya noise?"

⚠️ Slide 9 ke matrices schematic hain (200 examples, par table mein sirf 9 dikhaye) — isliye har matrix ko table ki rows se one-to-one match mat karo.
