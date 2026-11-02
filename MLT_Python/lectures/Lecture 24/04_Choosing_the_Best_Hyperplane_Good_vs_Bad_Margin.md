# Topic 4: Which Hyperplane? Maximum Margin, Good vs Bad Margin, Hard vs Soft

Source: Lecture 24, slides 9–11, all titled "How can we decide a separating line for the classes? Which hyperplane shall we use?":
- Slide 9: the Alice-vs-Cinderella figure with "Negative Hyperplane", "Positive Hyperplane", "Maximum Margin Hyperplane (Maximum Margin Classifier)", "Maximum Margin", "Support Vectors".
- Slide 10: "Good Margin" vs "Bad Margin".
- Slide 11: "Hard Margin" vs "Soft Margin".

Enriched with the soft-margin/hinge-loss formulation and our own scikit-learn demonstration.

---

## 1) Technical Explanation

### The question

Several lines can separate two linearly separable classes. A perceptron would stop at any of them ([[06_Linear_Separability_Concept]] from Lecture 4). Which one should we pick? SVM's answer: the one with the **maximum margin**.

### Slide 9: anatomy of the maximum-margin classifier

The axes are x1 and x2. Red ✖ points (pictures of Alice) are on the left and green ✖ points (pictures of Cinderella) are on the right. The figure labels:

| Label | Meaning (canonical form, see [[03_Support_Vectors_Margin_Hard_and_Soft_Margin]]) |
|---|---|
| **Negative Hyperplane** (red dashed) | w·x + b = −1, passes through the nearest red point(s) |
| **Positive Hyperplane** (green dashed) | w·x + b = +1, passes through the nearest green point(s) |
| **Maximum Margin Hyperplane / Maximum Margin Classifier** (solid black) | w·x + b = 0, exactly halfway between them |
| **Maximum Margin** | the gap between the two dashed lines, 2/‖w‖ |
| **Support Vectors** (circled red ✖ and green ✖) | the points lying on the dashed lines |

### Slide 10: good margin vs bad margin

- **Good Margin 😀:** the hyperplane sits so that "all support vectors have the same distance with the maximum margin hyperplane". It is equidistant from both classes and the gap is as wide as possible. (The slide misspells "support" as "sector".)
- **Bad Margin ☹:** the hyperplane is "very close to either class −1 support vectors or class +1 support vectors". It still separates the training data, but one class has almost no room. A new point slightly off its training cluster would be misclassified.

The maximum-margin solution is always a "good margin": at the optimum the nearest points of both classes are exactly 1/‖w‖ away.

**Why a wide margin generalises better.**
- Intuitively, a wide gap is robust to small noise in new points.
- Theoretically, VC theory bounds the capacity of large-margin separators, so they overfit less ([[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17).

### Slide 11: hard margin vs soft margin figures

- **Hard Margin:** two dotted margin lines with **no point between them**. The support vectors sit exactly on the dotted lines, and all other points are outside.
- **Soft Margin:** a wider margin. Some points sit **inside** the margin, and one red point lies on the **green side**. Dotted arrows from these points to their own margin line show the **slack** ξ_i that each violation costs.

**Soft-margin objective** (Cortes & Vapnik, 1995):

  **minimise ½‖w‖² + C Σᵢ ξᵢ  s.t.  yᵢ(w·xᵢ + b) ≥ 1 − ξᵢ, ξᵢ ≥ 0**

At the optimum, ξᵢ = max(0, 1 − yᵢ(w·xᵢ + b)). This is the **hinge loss**. So the soft-margin SVM minimises

  ½‖w‖² (keeps the margin wide) + C × Σ hinge losses (penalises violations).

### Demonstration (our own run, scikit-learn `SVC(kernel='linear')`)

Take the 8-point example from Topic 3, where the best hard-margin line was x₁ = 2 with margin 2. Now add one **noisy point (2.5, 0) labelled −1**. It sits on the "+" side of that line.

| C | Learned boundary | Margin 2/‖w‖ | Training accuracy | What happened |
|---|---|---|---|---|
| 10⁶ (≈ hard margin) | 4x₁ − 11 = 0 → **x₁ = 2.75** | **0.5** | 9/9 = 100% | squeezes between the noisy point (2.5) and (3, ±1) to classify everything correctly; very narrow margin |
| 1 (soft) | x₁ − 2 = 0 → **x₁ = 2** | **2.0** | 8/9 ≈ 88.9% | ignores the outlier and keeps the wide, sensible margin |

For C = 1 the noisy point scores w·x + b = 2.5 − 2 = +0.5. It is predicted +1 although its label is −1, so its slack is ξ = 1 − (−1)(+0.5) = **1.5**. Slack above 1 means "misclassified". The SVM accepts that one error to keep the margin four times wider.

This is slide 11 in numbers: a hard margin bends to fit every point, outliers included, while a soft margin trades a little training accuracy for a wider, more robust margin. The trade-off is controlled by C ([[05_Gamma_and_Regularization_C]]).

---

## 2) Simple English Explanation

**The question on all three slides:** many lines could separate the two groups. Which one should we choose?

**Slide 9: Alice vs Cinderella.**
- Red crosses (Alice fans) are on the left and green crosses (Cinderella fans) are on the right.
- Three lines are drawn:
  - a red dashed line touching the closest red cross: the "**negative hyperplane**";
  - a green dashed line touching the closest green cross: the "**positive hyperplane**";
  - a solid black line exactly in the middle: the "**maximum margin hyperplane**", which is the classifier SVM uses.
- The gap between the dashed lines is the **maximum margin**.
- The two circled crosses touching the dashed lines are the **support vectors**.

**Slide 10: good margin vs bad margin.**
- **Good margin 😀:** the dividing line is the same distance from the nearest red and the nearest green points, and that distance is as big as possible.
- **Bad margin ☹:** the line still separates the training points, but it hugs one group very closely. A new green point slightly to the left of the others would land on the wrong side.
- It's like parking exactly in the middle of your space instead of scraping the car on your left.
- (The slide says "sector vectors" by mistake. It means "support vectors".)

**Slide 11: hard margin vs soft margin.**
- **Hard margin:** the strip between the dotted lines is completely empty, and every point is on its own correct side.
- **Soft margin:** the strip is wider, but a few points are allowed inside it, and one red point is even on the green side. The little arrows show how far each rule-breaker is from where it "should" be. Each one adds a penalty.

**Our experiment: why soft margins help.**
- We took the earlier example (best line x = 2, road 2 units wide) and added one **wrongly placed point** at (2.5, 0) that belongs to the minus team but sits on the plus side.
- **Hard-ish SVM (huge penalty, C = 1,000,000):** it refuses to make any mistake. It moves the line to x = 2.75 and squeezes the road down to just **0.5 units**. Everything is correct on training data, but the road is dangerously narrow because of one odd point.
- **Soft SVM (normal penalty, C = 1):** it keeps the line at x = 2 with the wide **2-unit road** and simply accepts that the odd point is misclassified. 8 out of 9 training points are correct, but the model is far more sensible for new data.
- The odd point's "penalty size" (slack) is 1.5. Anything above 1 means "on the wrong side".

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Teeno slides ka sawaal:** do groups ko alag karne wali kai lines ho sakti hain, to kaunsi chunein? SVM ka jawaab: **jiska margin sabse bada ho**.

**Slide 9: Alice vs Cinderella.**
- Left mein laal ✖ (Alice), right mein hare ✖ (Cinderella).
- Teen lines hain:
  - **Negative hyperplane** (laal dashed): sabse paas wale laal point ko chhooti hai (w·x + b = −1).
  - **Positive hyperplane** (hari dashed): sabse paas wale hare point ko chhooti hai (w·x + b = +1).
  - **Maximum Margin Hyperplane / Maximum Margin Classifier** (kaali solid): dono ke theek beech mein (w·x + b = 0). Yahi SVM ka final classifier hai.
- Dono dashed lines ke beech ka gap **Maximum Margin** hai, jo 2/‖w‖ ke barabar hai.
- Dashed lines ko chhoone wale circle kiye hue points **Support Vectors** hain.

**Slide 10: good margin vs bad margin.**
- **Good margin 😀:** line dono taraf ke support vectors se **barabar doori** pe hai, aur woh doori sabse badi hai. Slide pe galti se "sector vectors" likha hai, matlab "support vectors" hai.
- **Bad margin ☹:** line training data ko alag to kar deti hai, par ek group se bilkul chipki hui hai (class −1 ya +1 ke support vectors ke bahut paas). Naya point thoda bhi idhar-udhar hua to galat side chala jayega.
- Car parking jaisa socho: beech mein park karo, ek taraf ki car se ragad ke nahi.
- Theory bhi kehti hai (VC theory) ki chauda margin = kam overfitting (Lecture 17).

**Slide 11: hard margin vs soft margin.**
- **Hard margin:** dotted lines ke beech ki patti bilkul khaali hai, aur har point apni sahi side pe hai.
- **Soft margin:** patti chaudi hai, par kuch points andar aa gaye hain. Ek laal point to hare side pe hai. Chhote teer dikhate hain ki har rule todne wala kitna door hai (**slack ξ**), aur har ek pe penalty lagti hai.
- Formula: **minimise ½‖w‖² + C Σξ_i**.
  - Pehla hissa margin chauda rakhta hai.
  - Doosra hissa galtiyon pe jurmana lagata hai. Ise **hinge loss** bhi kehte hain: max(0, 1 − y(w·x + b)).

**Humara experiment: soft margin kyun zaroori hai.**
- Topic 3 wala example lo (best line x = 2, sadak 2 units chaudi). Usme ek **galat jagah wala point (2.5, 0)** jodo. Iska label −1 hai, par ye + side pe baitha hai.
- **C = 10⁶ (lagbhag hard margin):** koi galti bardaasht nahi. Line ko x = **2.75** pe khiska diya, aur sadak sirf **0.5** units reh gayi. Training pe 9/9 sahi, par ek ajeeb point ki wajah se sadak khatarnaak tarike se patli ho gayi.
- **C = 1 (soft margin):** line **x = 2** pe hi rahi aur sadak **2 units** chaudi rahi. Woh ajeeb point galat classify hua: score = 2.5 − 2 = +0.5, label −1. Slack = 1 − (−1)(0.5) = **1.5**, aur 1 se zyada slack ka matlab hai galat side. Training 8/9 (88.9%), par naye data ke liye model kahin zyada samajhdaar hai.
- Yahi slide 11 ka message hai: hard margin har point (outlier bhi) ke hisaab se mud jata hai, soft margin thodi training accuracy dekar chauda aur mazboot margin rakhta hai. Ye balance **C** control karta hai (agla topic).
