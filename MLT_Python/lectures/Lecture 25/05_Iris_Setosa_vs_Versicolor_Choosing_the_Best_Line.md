# Topic 5: Iris Setosa vs Versicolor: Choosing the Best Line, Support Vectors and Margin

Source: Lecture 25, slides 9–14:
- Slide 9: iris flower photo with "petal" and "sepal" measurement arrows.
- Slide 10: scatter of Petal Length vs Petal Width with legend Setosa / Versicolor.
- Slide 11: the same scatter with three candidate separating lines (blue, black, orange).
- Slide 12: black vs orange line, with dashed distances to the nearest points.
- Slide 13: black line, handwritten "SV" arrows and "Margin".
- Slide 14: "Support Vectors" and "Margin" labels.

Enriched with our own scikit-learn run on the **real** Iris data (Fisher, 1936) and a hand derivation of its maximum-margin line.

---

## 1) Technical Explanation

### Slides 9–10: the data

- **Slide 9** shows an iris flower. The **petal** (inner, upright part) and the **sepal** (outer, drooping part) each have a length and a width. This is the famous Iris dataset from Lecture 1 ([[03_Iris_Dataset_Case_Study]] from Lecture 1).
- **Slide 10** plots two species using two features. The x-axis is **Petal Width** and the y-axis is **Petal Length**.
  - **Setosa** (green squares) sit lower-left.
  - **Versicolor** (blue diamonds) sit upper-right, with one versicolor point drawn far up-left.
- The two classes are separable by a straight line, so this is a hard-margin linear SVM problem.

### Slide 11: many lines separate the classes

Three lines are drawn: blue (shallow), black (steeper) and orange (steepest). **Each one** separates the training points perfectly. So "separates the data" is not enough to choose a line. This is the same question as Lecture 24's "Which hyperplane shall we use?" ([[04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin]] from Lecture 24).

### Slide 12: compare by distance to the nearest points

Only the black and orange lines remain. Dashed segments show the perpendicular distance from the nearest points to each line.

- The **orange line** passes very close to the top-left versicolor point and to a setosa point near the bottom. Its smallest distance is tiny.
- The **black line** keeps a larger distance from the nearest points of **both** classes.

The SVM picks the line whose minimum distance to the data, the **margin**, is largest. That is the black line.

### Slides 13–14: support vectors and margin

- The black line is kept.
- The instructor's purple arrows mark "**SV**": the top-left versicolor point and nearby setosa and versicolor points.
- Slide 14 labels **Support Vectors** (arrows to five points near the line, from both species) and the **Margin** (the dashed distance from the line to a nearby point).

*Caveat about the illustration.* In an exact hard-margin solution, **every** support vector lies at exactly the same distance 1/‖w‖ from the hyperplane, because all of them sit on the margin lines w·x + b = ±1. In slide 14's figure the dashed segments have visibly different lengths, so it is a schematic, not a computed solution.

### The real data, solved (our run: scikit-learn `SVC(kernel='linear', C=10⁶)`)

The real Iris data has 50 setosa and 50 versicolor flowers. Features are (petal width, petal length) in cm.

**Ranges:**
- Setosa: width 0.1–0.6, length 1.0–1.9.
- Versicolor: width 1.0–1.8, length 3.0–5.1.

The real classes are separated by a wide gap. The real data has **no** versicolor flower near the setosa cluster, unlike the outlier drawn in slide 10's schematic.

**Result:**
- w = **(0.824, 1.294)**, b = **−3.788**.
- Hyperplane: 0.824·width + 1.294·length − 3.788 = 0. It is a downward-sloping diagonal, like the black line on the slides.
- Only **two** support vectors: setosa **(0.4, 1.9)** and versicolor **(1.1, 3.0)**.
- Margin = 2/‖w‖ = **1.304 cm**.
- Training accuracy **100%**.

**Hand derivation (two support vectors).** With one support vector per class, x₋ = (0.4, 1.9) and x₊ = (1.1, 3.0), the maximum-margin hyperplane is the **perpendicular bisector** of the segment between them:

- d = x₊ − x₋ = (0.7, 1.1), ‖d‖² = 0.49 + 1.21 = **1.70**
- w = 2d/‖d‖² = (1.4, 2.2)/1.70 = **(0.8235, 1.2941)** ✔
- midpoint m = (0.75, 2.45), b = −w·m = −(0.6176 + 3.1706) = **−3.788** ✔
- margin = 2/‖w‖ = ‖d‖ = √1.70 = **1.304** ✔
- Check: w·x₋ + b = 0.3294 + 2.4588 − 3.788 = **−1.00**, and w·x₊ + b = 0.9059 + 3.8824 − 3.788 = **+1.00** ✔

**Using the model.**
- A flower with petal width 0.5 and length 2.0 scores 0.412 + 2.588 − 3.788 = **−0.788**, so it is **setosa**.
- A flower with width 1.2 and length 4.0 scores 0.988 + 5.176 − 3.788 = **+2.376**, so it is **versicolor**.
- These match `predict` and `decision_function` in our run.

---

## 2) Simple English Explanation

**Slide 9: the flower.** An iris flower has inner upright petals and outer drooping sepals. For each, we can measure the length and the width. Botanists measured 150 flowers this way; that's the famous Iris dataset from Lecture 1.

**Slide 10: the graph.**
- Petal width goes along the bottom and petal length goes up the side.
- **Setosa** flowers (green squares) have small petals, so they sit in the lower-left.
- **Versicolor** flowers (blue diamonds) have bigger petals, so they sit upper-right.
- A straight line can split them.

**Slide 11: but which line?** Three different lines (blue, black, orange) all split the two groups perfectly. They're all "correct" on this data, so we need a tie-breaker.

**Slide 12: the tie-breaker is the safety gap.**
- Look at how close each line comes to the nearest flowers (the dashed lines).
- The **orange** line almost touches one blue diamond and one green square. A new flower that's slightly different could easily land on the wrong side.
- The **black** line keeps a comfortable distance from both groups.
- SVM picks the line with the **biggest gap to the nearest points**. That's the black one.

**Slides 13–14: names.**
- The flowers closest to the black line are the **support vectors**; the teacher wrote "SV" with arrows.
- The gap between the line and them is the **margin**.
- Small print: in a perfectly computed SVM, all support vectors sit at *exactly* the same distance from the line. The slide's drawing shows slightly different distances because it's a sketch, not a calculation.

**We tried it on the real flowers.**
- In the real data, the two species are far apart:
  - setosa petals are 1.0–1.9 cm long;
  - versicolor petals are 3.0–5.1 cm long.
- (The lonely blue diamond drawn near the setosa group on the slide doesn't exist in the real data.)
- Python's SVM found the line **0.824 × width + 1.294 × length − 3.788 = 0**, a slanted line like the black one.
- Only **two** flowers turned out to be support vectors: a setosa with petal (0.4 cm wide, 1.9 cm long) and a versicolor with petal (1.1, 3.0).
- The safety gap is **1.30 cm** wide.
- It classifies all 100 flowers correctly.

**Checking by hand.**
- When there's one support vector on each side, the best line is simply the line that **cuts the segment between them in half at a right angle**.
- The segment from (0.4, 1.9) to (1.1, 3.0) has length √1.70 ≈ 1.30. That's exactly the margin.
- The line passes through its midpoint (0.75, 2.45).

**Trying new flowers.**
- A flower with petals 0.5 wide and 2.0 long scores −0.79: negative, so **setosa**.
- One with petals 1.2 wide and 4.0 long scores +2.38: positive, so **versicolor**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 9: phool.** Iris phool mein andar khade **petals** aur bahar latakte **sepals** hote hain. Dono ki length aur width naap sakte hain. Isi se bana famous Iris dataset Lecture 1 mein padha tha.

**Slide 10: graph.**
- Neeche (x-axis) Petal Width, upar (y-axis) Petal Length.
- **Setosa** (hare squares) ke petals chhote hain, to woh neeche-left mein hain.
- **Versicolor** (neele diamonds) ke bade hain, to upar-right mein hain.
- Ek seedhi line inhe alag kar sakti hai.

**Slide 11: par kaunsi line?** Teen lines (neeli, kaali, orange) teeno dono groups ko perfectly alag karti hain. Training data pe sab "sahi" hain, to tie-breaker chahiye. Ye wahi Lecture 24 wala sawaal hai: "Which hyperplane shall we use?"

**Slide 12: tie-breaker = safety gap.**
- Har line sabse paas wale phoolon se kitni door hai (dashed lines) dekho.
- **Orange** line ek neele diamond aur ek hare square ko lagbhag chhoo rahi hai. Thoda alag naya phool aaya to galat side gir sakta hai.
- **Kaali** line dono groups se aaraam ki doori rakhti hai.
- SVM wahi line chunta hai jiski **sabse paas wale points se doori (margin) sabse zyada** ho. Isliye kaali line.

**Slides 13–14: naam.**
- Kaali line ke sabse paas wale phool **support vectors** hain (teacher ne purple arrows se "SV" likha).
- Line aur unke beech ka gap **margin** hai.
- ⚠ Chhoti baat: asli calculated SVM mein **saare** support vectors line se *bilkul barabar* doori (1/‖w‖) pe hote hain, kyunki sab margin lines (w·x + b = ±1) pe baithe hote hain. Slide 14 ki drawing mein dooriyan alag-alag dikhti hain, kyunki woh sketch hai, calculation nahi.

**Humne asli phoolon pe chalaya** (50 setosa + 50 versicolor):
- Asli data mein dono species bahut door hain:
  - Setosa: width 0.1–0.6, length 1.0–1.9 cm.
  - Versicolor: width 1.0–1.8, length 3.0–5.1 cm.
  - Slide 10 pe setosa ke paas jo akela neela diamond bana hai, woh asli data mein nahi hai.
- scikit-learn ka answer:
  - Line: **0.824 × width + 1.294 × length − 3.788 = 0**, ek tirchhi line, slide ki kaali line jaisi.
  - Sirf **do** support vectors: setosa **(0.4, 1.9)** aur versicolor **(1.1, 3.0)**.
  - Margin = **1.304 cm**, aur saare 100 phool sahi ✔.

**Haath se check (do support vectors wala shortcut).** Har side ek support vector ho to best line unhe jodne wali line ka **perpendicular bisector** hoti hai (beech se 90° pe kaatne wali).
- d = (1.1 − 0.4, 3.0 − 1.9) = (0.7, 1.1), aur ‖d‖² = 0.49 + 1.21 = **1.70**.
- w = 2d/‖d‖² = (1.4, 2.2)/1.7 = **(0.8235, 1.2941)** ✔
- Midpoint = (0.75, 2.45), b = −w·midpoint = −(0.6176 + 3.1706) = **−3.788** ✔
- Margin = ‖d‖ = √1.70 = **1.304** ✔
- Check: setosa SV ka score **−1.00**, versicolor SV ka **+1.00** ✔

**Naye phool:**
- Petal (0.5, 2.0): 0.412 + 2.588 − 3.788 = **−0.788** → **setosa**.
- Petal (1.2, 4.0): 0.988 + 5.176 − 3.788 = **+2.376** → **versicolor**.
