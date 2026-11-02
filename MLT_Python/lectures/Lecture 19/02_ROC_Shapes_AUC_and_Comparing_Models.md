# Topic 2: ROC Shapes, AUC, and Comparing Models

Source: Lecture 19, slides 5, 6 and 11 ("ROC Curves" with the ideal / worst / typical panels and the instructor's AUC shading, "Multiple ROC Curves", and "AUC (Area Under the ROC Curve) score" with the area formula). Enriched with web research (AUC as a ranking probability, AUC < 0.5, trapezoid rule).

---

## 1) Technical Explanation

**Three canonical ROC shapes (slide 5).** Three small plots (TPR vs. FPR, both 0–1); the instructor shades the area under each and labels it **AUC**, and adds "Threshold ↑Th / ↓Th".

| Panel | Shape | Slide's description | AUC |
|---|---|---|---|
| 1 | Goes straight up the left edge to (0,1), then straight across the top | *"This is an **ideal situation**. Model has an ideal measure of separability. It is perfectly able to distinguish between positive class and negative class."* | **1.0** (whole square) |
| 2 | The **diagonal** from (0,0) to (1,1) | *"This is the **worst situation**. When AUC is approximately **0.5**, model has **no discrimination capacity** to distinguish between positive class and negative class. **Random predictions.**"* | **0.5** (a triangle = ½) |
| 3 | A smooth concave curve above the diagonal | A typical useful model (no caption) | between 0.5 and 1 |

**Area Under the Curve (AUC) — slide 11.** AUC = *Area Under the ROC Curve* — a single number summarizing performance over **all** thresholds. The slide's guide:
- **High AUC (close to 1):** the model effectively distinguishes between positive and negative instances.
- **Low AUC (close to 0):** the model struggles to differentiate between the two classes.
- **AUC around 0.5:** the model doesn't learn any meaningful patterns, i.e. it is doing **random guessing.**

**⚠️ A correction on "AUC close to 0" (research).** An AUC near 0 does not mean "struggles to differentiate" — it means the model separates the classes *very well but with the labels reversed* (it ranks negatives above positives). Flipping its predictions would give AUC ≈ 1 − AUC ≈ 1. The *worst* (least informative) value is **0.5**, which is what the slide says for random guessing. "Below the diagonal: worse than random" on slide 10 is the same fact ([[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]]).

**Probabilistic meaning (slide 10, verified in the worked examples).** AUC = the **probability that a randomly chosen positive instance is ranked ahead of (scored higher than) a randomly chosen negative instance** (ties counted as ½). This equals the Wilcoxon–Mann–Whitney U statistic (research). *Check:* Example 1 has 5 positives × 5 negatives = 25 pairs; positive scores {0.90, 0.80, 0.60, 0.55, 0.50} vs. negative scores {0.70, 0.54, 0.53, 0.51, 0.40} → 19 of 25 pairs rank the positive higher = **0.76**, exactly the trapezoid area ([[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]]); Example 2 gives 16/25 = **0.64** ([[05_Worked_Example_2_Trapezoid_Rule_AUC_0_64]]).

**Computing the area (slide 11 formula).** Between two consecutive ROC points (x₁, y₁) and (x₂, y₂) the area under the segment is a **trapezoid**:

**Area = (x₂ − x₁)(y₁ + y₂) / 2**

AUC = the sum of these strips over the whole curve (the instructor labels the two points "(x₁, y₁)" and "(x₂, y₂)" on the slide). Vertical moves have x₂ − x₁ = 0 and contribute nothing.

**Multiple ROC curves (slide 6).** *Comparison of multiple classifiers is usually straightforward, especially when no curves cross each other. Curves close to the perfect ROC curve have a better performance level than the ones closest to the baseline.* The slide's figure shows three curves with the dashed diagonal baseline: a **"great model"** (blue, hugging the top-left corner, AUC near 1), a **"good model"** (red, in between) and a **"bad model"** (green, only slightly above the diagonal). Rule: if one curve lies entirely above another, it is better at *every* threshold; if curves **cross**, AUC alone hides the fact that each model is better in a different region (e.g. at low FPR vs. high FPR), so pick by the operating range you care about.

**Rough interpretation scale (research, a convention not a law).** 0.5 ≈ no skill; 0.7–0.8 acceptable; 0.8–0.9 good; > 0.9 excellent.

**Advantages of AUC:** threshold-free, summarizes ranking quality, insensitive to the choice of cut-off. **Limits:** says nothing about calibration (are the probabilities accurate?), and can look rosy on very imbalanced data — see [[03_PR_Curves_vs_ROC_Curves]].

---

## 2) Simple English Explanation

Imagine three models and you draw each one's ROC curve:

1. **Perfect model:** the line shoots straight up the left side and runs across the top. The area under it is **1** (the whole square). It never makes a mistake.
2. **Coin-flip model:** the line is the **diagonal**. The area under it is **0.5** (half the square). It knows nothing — same as guessing.
3. **Normal good model:** a bulging curve above the diagonal. The more it bulges towards the top-left corner, the bigger the area (somewhere between 0.5 and 1).

**AUC = the area under the curve.** One number to compare models:
- Close to **1** → very good at telling positives from negatives.
- Around **0.5** → just guessing.
- Close to **0** → actually *reversed* (it gets things backwards — the slide says "struggles", but really you could flip its answers and get a great model).

**Cute meaning of AUC:** pick one random positive person and one random negative person. AUC is the chance that the model gave the positive person the **higher** score. AUC 0.76 means that's true 76 times out of 100.

**Comparing models:** draw all their curves on one graph. The curve closest to the top-left corner wins. (If two curves cross, one model is better in one region, the other elsewhere.) In the slide's picture: blue "great" > red "good" > green "bad".

**How to compute the area:** chop it into thin strips and add up. Each strip's area = width × average height = (x₂ − x₁)(y₁ + y₂) ÷ 2.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Teen models socho aur har ka ROC curve banao:

1. **Perfect model:** line seedhi left side se upar jaati hai aur phir top par seedhi chalti hai. Area **1** (poora square). Koi galti nahi.
2. **Sikka-uchhalne wala model:** line **diagonal** hai. Area **0.5** (aadha square). Isse kuch nahi aata — guessing ke barabar. Slide kehti hai: "no discrimination capacity, random predictions."
3. **Normal accha model:** diagonal ke upar ubhra hua curve. Jitna top-left corner ki taraf bulge, utna area zyada (0.5 se 1 ke beech).

**AUC = curve ke neeche ka area.** Models compare karne ke liye ek number:
- **1 ke paas** → positives aur negatives ko bahut accha alag karta hai.
- **0.5 ke aas-paas** → bas guessing.
- **0 ke paas** → slide kehti hai "struggle karta hai", par asal mein model **ulta** hai (positives ko negatives se neeche rank karta hai). Uske answers flip kar do to AUC ≈ 1 ho jayega. Sabse "bekaar" value 0.5 hai, 0 nahi.

**AUC ka cute matlab:** ek random positive aur ek random negative person uthao. AUC = probability ki model ne positive ko **zyada score** diya. AUC 0.76 matlab 100 mein se 76 baar aisa hota hai. (Humne examples mein pairs gin kar verify kiya: Example 1 = 19/25 = 0.76, Example 2 = 16/25 = 0.64.)

**Models compare karna (slide 6):** sab curves ek graph par banao. Jo curve top-left corner ke sabse paas, wo best: blue "great" > red "good" > green "bad". Agar do curves **cross** karein, to ek model kisi region mein behtar hota hai aur dusra dusre region mein — tab AUC akela kaafi nahi.

**Area nikaalne ka formula (slide 11):** area ko patli strips mein kaato aur jodo. Har strip = width × average height = **(x₂ − x₁)(y₁ + y₂) ÷ 2** (trapezoid).

Thumb rule: 0.5 = bekaar, 0.7–0.8 theek, 0.8–0.9 accha, 0.9+ bahut accha.
