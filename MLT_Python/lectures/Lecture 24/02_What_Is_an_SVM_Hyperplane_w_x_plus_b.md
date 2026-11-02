# Topic 2: What Is an SVM? The Hyperplane w·x + b = 0

Source: Lecture 24, slides 3–4 ("Support Vector Machines (SVMs)": supervised, hyperplane, w·x + b = 0, cats-vs-dogs example 3×Weight + 2×Height − 50 = 0, with handwritten "Hyperplanes / feature space", "wx + b = 0", "3*Weight + 2*Height − (50) = 0"; hand-drawn sketch of "+" and "−" points separated by a line labelled "Hyperplane (Decision boundary)"). Worked numbers are our own illustration of the slide's equation.

---

## 1) Technical Explanation

### Slide 3, point by point

- "SVMs are **supervised** machine learning algorithms used for **classification and regression** tasks." Supervised means the training data carries labels, unlike clustering in Lecture 23 ([[01_What_Is_Clustering_Unsupervised_Grouping]] from Lecture 23).
  - The classification version is the subject of this lecture.
  - The regression version is called **SVR** (Support Vector Regression). It fits a "tube" of width ε around the data instead of separating classes.
- "**Hyperplane**: a decision boundary that separates data points of different classes in the **feature space**."
  - The instructor's sketch shows several candidate lines through a cloud of points, labelled "Hyperplanes" and "feature space".
- "Mathematical representation: **w·x + b = 0**."
- "Example: if we classify animals into **cats (+1)** and **dogs (−1)** based on weight and height, the hyperplane could be **3 × Weight + 2 × Height − 50 = 0**."
  - The instructor circled the −50: that is the bias b.

**Slide 4** (hand-drawn) shows "+" points at the top-left, "−" points below, and a straight line between them labelled "**Hyperplane (Decision boundary)**".

### What a hyperplane is

In a d-dimensional feature space, a hyperplane is the set of points x with

  **w·x + b = w₁x₁ + w₂x₂ + … + w_dx_d + b = 0**

- **w** (weight vector) is perpendicular (normal) to the hyperplane. It sets the hyperplane's **orientation**.
- **b** (bias) shifts the hyperplane away from the origin. It sets the hyperplane's **position**.
- In 2-D a hyperplane is a **line**. In 3-D it is a **plane**. In d-D it is a flat (d−1)-dimensional surface.

**Decision rule:** predict ŷ = **sign(w·x + b)**, i.e. +1 if w·x + b > 0 and −1 if it is < 0. This is exactly the perceptron's form ([[05_Perceptron_General_Architecture]] from Lecture 4). What makes SVM different is *how* w and b are chosen ([[03_Support_Vectors_Margin_Hard_and_Soft_Margin]]).

**Signed distance from a point to the hyperplane:**

  **distance(x) = (w·x + b) / ‖w‖**,  where ‖w‖ = √(w₁² + … + w_d²).

The sign of this value tells you the side, and its size tells you how far the point is from the boundary.

### Worked example with the slide's hyperplane (our numbers)

Take w = (3, 2), b = −50, and features x = (Weight, Height). Then ‖w‖ = √(3² + 2²) = √13 ≈ 3.606.

| Animal (Weight, Height) | w·x + b | Prediction | Distance (w·x+b)/‖w‖ |
|---|---|---|---|
| (10, 15) | 3·10 + 2·15 − 50 = **+10** | +1 → **cat** | 10/3.606 = **2.77** |
| (5, 10) | 15 + 20 − 50 = **−15** | −1 → **dog** | −15/3.606 = **−4.16** |
| (8, 13) | 24 + 26 − 50 = **0** | on the boundary, undecided | 0 |

- The weights tell us that 1 unit of Weight moves the score 3 points and 1 unit of Height moves it 2 points.
- The line crosses the Weight axis at Weight = 50/3 ≈ 16.7 (Height = 0) and the Height axis at Height = 25 (Weight = 0).

**Caveats.**
- The slide's equation is illustrative. No units or data are given, so we can't say whether these weights are realistic.
- Which side is called +1 is a convention. Multiplying w and b by −1 gives the same line with the labels swapped.
- Many different (w, b) describe the same line, e.g. (6, 4, −100). SVM fixes this freedom by a scaling convention, the "canonical" hyperplane (see Topic 3).

---

## 2) Simple English Explanation

**What is an SVM?** A Support Vector Machine is a **supervised** learning method: it learns from examples that already have the right answer attached ("this is a cat", "this is a dog"). It is mainly used to **classify** (put things into groups such as cat/dog or spam/not-spam). A version of it can also **predict numbers** (regression).

**What is a hyperplane?** It is just the **dividing line** between the two classes.
- With 2 features (like weight and height) it is an ordinary straight line on a graph.
- With 3 features it is a flat sheet, like a wall.
- With more features it is the same idea in more dimensions. We can't picture it, but the maths works the same way.

The teacher's drawing on slide 4 shows "+" points on one side, "−" points on the other, and the line between them: the **hyperplane, or decision boundary**.

**The formula w·x + b = 0.**
- **x** is the list of features of one animal, e.g. (weight, height).
- **w** is a list of weights saying how important each feature is.
- **b** is a single number that slides the line up or down. The teacher circled the −50, which is b.
- Multiply each feature by its weight, add them up, add b, and you get a **score**:
  - **Score > 0** → one side → **cat (+1)**
  - **Score < 0** → other side → **dog (−1)**
  - **Score = 0** → exactly on the line

**Let's try the slide's line: 3 × Weight + 2 × Height − 50.**
- **Animal with weight 10, height 15:** 30 + 30 − 50 = **+10**. Positive, so **cat**.
- **Animal with weight 5, height 10:** 15 + 20 − 50 = **−15**. Negative, so **dog**.
- **Animal with weight 8, height 13:** 24 + 26 − 50 = **0**. Right on the line, so the model can't decide.

**How far from the line?** Divide the score by the "length" of the weights, √(3² + 2²) = √13 ≈ 3.6.
- The first animal is 10/3.6 ≈ **2.8** units away on the cat side.
- The second is 15/3.6 ≈ **4.2** units away on the dog side.
- The farther from the line, the more confident the answer. That idea is the heart of SVM: the **margin**, explained next.

(The numbers on the slide are just an example. They don't come from real measurements, and which side is called "cat" is only a choice.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**SVM kya hai?** Support Vector Machine ek **supervised** learning method hai, yaani ye aise examples se seekhta hai jinke saath sahi jawaab (label) pehle se hota hai ("ye cat hai", "ye dog hai").
- Mainly **classification** ke liye use hota hai: cheezon ko groups mein daalna, jaise cat/dog ya spam/not-spam.
- Iska ek version numbers bhi predict kar sakta hai (regression). Use **SVR** kehte hain.
- Lecture 23 (clustering) unsupervised tha, bina labels ka. SVM uska ulta hai, isme labels chahiye.

**Hyperplane kya hai?** Do classes ke beech ki **baantne wali line**.
- 2 features (weight, height) ho to graph pe seedhi line.
- 3 features ho to ek flat chadar (deewar jaisi).
- Zyada features ho to wahi idea zyada dimensions mein. Dikh nahi sakta, par maths same hai.
- Slide 3 pe teacher ne kai lines bana ke likha "Hyperplanes" aur "feature space". Slide 4 pe "+" ek taraf, "−" doosri taraf, aur beech mein line: **Hyperplane (Decision boundary)**.

**Formula w·x + b = 0.**
- **x** = ek animal ke features, jaise (weight, height).
- **w** = har feature ka weight, yaani feature kitna important hai. w hyperplane ki direction (orientation) tay karta hai.
- **b** = bias, ek number jo line ko upar-neeche khiskata hai (position). Teacher ne −50 circle kiya, wahi b hai.
- Har feature ko uske weight se guna karo, sab jodo, b jodo, to **score** milta hai:
  - **Score > 0** → **cat (+1)**
  - **Score < 0** → **dog (−1)**
  - **Score = 0** → bilkul line ke upar
- Ye rule perceptron (Lecture 4) jaisa hi hai. SVM ka farq ye hai ki w aur b *kaise* chune jaate hain (agla topic).

**Slide ki line se example: 3 × Weight + 2 × Height − 50.**
- **Weight 10, Height 15:** 3×10 + 2×15 − 50 = 30 + 30 − 50 = **+10**. Positive, to **cat**.
- **Weight 5, Height 10:** 15 + 20 − 50 = **−15**. Negative, to **dog**.
- **Weight 8, Height 13:** 24 + 26 − 50 = **0**. Line ke upar hai, decide nahi ho sakta.

**Line se kitni doori?** Formula: doori = (w·x + b)/‖w‖, jahan ‖w‖ = √(3² + 2²) = √13 ≈ 3.606.
- Pehla animal: 10/3.606 ≈ **2.77** units, cat side pe.
- Doosra animal: −15/3.606 ≈ **−4.16**, yaani 4.16 units dog side pe.
- Jitna door, utna confident jawaab. Yahi SVM ka dil hai: **margin** (agla topic).

**Dhyan do:**
- Slide ke numbers sirf example hain, koi real data ya units nahi diye.
- Kaunsa side "cat" hai ye sirf convention hai. w aur b ko −1 se guna karo to wahi line milegi, bas labels ulat jaayenge.
- Ek hi line ko kai (w, b) se likh sakte hain, jaise (6, 4, −100) bhi wahi line hai. SVM is confusion ko ek scaling rule (canonical hyperplane) se fix karta hai.
