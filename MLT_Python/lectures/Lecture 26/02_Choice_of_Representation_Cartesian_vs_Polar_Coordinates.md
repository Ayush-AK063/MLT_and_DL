# Topic 2: Choice of Representation: Cartesian vs Polar Coordinates

Source: Lecture 26, slide 6 ("Choice of Representation", figure from the *Deep Learning* book, Fig. 1.1, with the note on Cartesian vs polar coordinates). Enriched with web research (Goodfellow, Bengio & Courville, *Deep Learning*, 2016, ch. 1). The logistic-regression experiment and all numbers are ours, run with scikit-learn.

---

## 1) Technical Explanation

### What the slide shows

Two scatter plots of the **same dataset**:

- **Left, Cartesian coordinates (x, y):** blue circles form a blob around the origin; green triangles form a ring around them.
- **Right, polar coordinates (r, θ):** the same points re-plotted with r (distance from the origin) on the horizontal axis and θ (angle) on the vertical axis. Blue circles now form a vertical strip on the left (small r), green triangles a strip on the right (large r).

The slide's note: "Cartesian coordinates use a grid of (x, y) to measure horizontal and vertical distances, while polar coordinates use a distance and angle (r, θ) from a central origin."

The book's caption makes the point explicit: in Cartesian coordinates the two classes **cannot be separated by a straight line**; in polar coordinates a **vertical line** separates them.

### The conversion formulas

From Cartesian to polar:

- **r = √(x² + y²)**
- **θ = atan2(y, x)** (the angle from the positive x-axis, taking the quadrant into account)

Back from polar to Cartesian: x = r cos θ, y = r sin θ.

Checks (ours):

| (x, y) | r | θ |
|---|---|---|
| (3, 4) | √(9 + 16) = **5** | atan2(4, 3) = **53.13°** |
| (−2, 0) | **2** | **180°** |
| (0, 1.5) | **1.5** | **90°** |

### Why one representation is linearly separable and the other is not

A **linear classifier** (perceptron, logistic regression, linear SVM) draws a straight line w₁f₁ + w₂f₂ + b = 0 in feature space ([[06_Linear_Separability_Concept]] from Lecture 4, [[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15).

- In (x, y), any straight line cuts through the ring. Points of both classes end up on both sides. The data is **not linearly separable**.
- In (r, θ), the class depends only on r: blue has small r, green has large r. The vertical line **r = c** (for some c between the blob's edge and the ring's inner edge) separates them perfectly. In that representation the problem is linearly separable.

### Our experiment

We generated 400 points like the figure: 200 "blue" with r uniform in [0, 1], 200 "green" with r uniform in [2, 3], angles uniform in [0, 2π). Then we trained plain logistic regression on each representation:

| Features given to logistic regression | Training accuracy |
|---|---|
| (x, y), Cartesian | **53.75%** (barely better than a 50% coin toss) |
| (r, θ), polar | **100%** |
| r alone | **100%** |

With polar features the learned weights were ≈ 4.90 for r and ≈ −0.02 for θ (θ is ignored), with intercept −7.44. The decision boundary is r = 7.44 / 4.90 ≈ **1.52**, which falls in the gap between 1 and 2, as expected.

Same data, same algorithm. Only the representation changed, and accuracy went from chance level to perfect.

### Lessons

1. **The model was not the problem; the features were.** A simple linear model is enough once the representation is right.
2. Here a human who looked at the picture could guess "use the distance from the centre". That is **hand-designed feature engineering** ([[03_Learning_Representations_and_Why_Hand_Designed_Features_Are_Hard]]).
3. For real data (images with millions of pixels), nobody can look at the picture and guess the right transformation. **Representation learning** asks the machine to find it ([[04_Representation_Learning_and_Factors_of_Variation]]).
4. The same idea drives the SVM **kernel trick** from Lecture 24: map data into a space where a linear boundary works ([[06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick]] from Lecture 24). An RBF kernel would also solve this ring dataset. The difference is that in an SVM the kernel is chosen by a person, while deep learning *learns* the mapping.

---

## 2) Simple English Explanation

The slide shows **one set of points drawn in two different ways**.

**Picture 1 (Cartesian, the usual x–y graph):** blue dots sit in a ball in the middle. Green triangles form a ring around the ball, like the white of a fried egg around the yolk. Try to separate blue from green with **one straight ruler line**: impossible. Wherever you put the ruler, it cuts through the ring.

**Picture 2 (polar):** we describe each point differently. Instead of "how far right, how far up", we say "**how far from the centre (r)**, and **in which direction (θ, the angle)**". Now plot distance on the horizontal axis and angle on the vertical axis. All the blue dots are close to the centre, so they line up on the left. All the green triangles are far away, so they line up on the right. **One vertical line now separates them perfectly.**

**How to convert:**
- Distance: r = √(x² + y²). For the point (3, 4): √(9 + 16) = √25 = 5.
- Angle: the direction of the point. For (3, 4) it is about 53°. For (−2, 0) it is 180° (straight left). For (0, 1.5) it is 90° (straight up).

**We tested it.** We made 400 points like the slide's and asked a simple straight-line classifier (logistic regression) to separate them:
- Using x and y: it got only **53.75%** right, barely better than tossing a coin.
- Using distance and angle: **100%** right. It even learned to ignore the angle and just say "if distance is more than about 1.52, it's green".

**The lesson:** the same simple method went from useless to perfect just because we described the data better. Here a person could spot the trick ("use distance from the centre"). But for a photo made of millions of pixels, nobody can spot the right trick by eye. That is why we want computers to **learn the right description themselves**, which is what deep learning does.

This is similar to the SVM "kernel trick" from Lecture 24, where we moved data into a new space so a straight line could split it. The difference: with SVM, *we* pick the kernel; with deep learning, the network *learns* the transformation.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Slide me **ek hi data do tarah se draw** kiya gaya hai.

**Left picture, Cartesian (x, y):** Blue circles beech me ek gola bana rahe hain, green triangles uske chaaron taraf ek ring (anda ka safed hissa aur beech me yolk jaisa). Ek **seedhi line** se blue aur green alag karne ki koshish karo: impossible. Line kahin bhi rakho, ring ko kaategi hi. Matlab data **linearly separable nahi** hai.

**Right picture, Polar (r, θ):** Har point ko "kitna right, kitna upar" ki jagah "**centre se kitni doori (r)** aur **kis direction me (θ, angle)**" se describe karo. Horizontal axis pe r aur vertical pe θ. Blue sab centre ke paas hain to left me ek patti ban gayi, green door hain to right me. Ab **ek vertical line r = c** se dono perfectly alag.

**Conversion formula:**
- r = √(x² + y²)
- θ = atan2(y, x), yaani positive x-axis se angle
- Example: (3, 4) → r = √(9 + 16) = 5, θ = 53.13°. (−2, 0) → r = 2, θ = 180°. (0, 1.5) → r = 1.5, θ = 90°.

**Humara experiment:** Slide jaisa 400 points ka data banaya: 200 blue (r 0 se 1 ke beech), 200 green (r 2 se 3 ke beech), angle random. Fir simple **logistic regression** (seedhi line wala classifier, Lecture 15) chalaya:
- (x, y) features se accuracy sirf **53.75%**, lagbhag sikka uchhalne jitna (50%).
- (r, θ) features se **100%**.
- Sirf r se bhi **100%**. Model ne r ka weight ≈ 4.90 aur θ ka ≈ −0.02 rakha (yaani angle ignore), intercept −7.44. Boundary r = 7.44/4.90 ≈ **1.52**, bilkul 1 aur 2 ke gap me.

Same data, same algorithm, sirf representation badla aur result chance level se perfect ho gaya.

**Seekh:**
1. Problem model me nahi thi, **features** me thi. Sahi representation mile to seedhi line bhi kaafi hai.
2. Yahan insaan picture dekh ke guess kar sakta tha "centre se doori use karo". Isko **hand-designed feature** kehte hain.
3. Par real data, jaise photo ke lakhon pixels, me koi aankh se sahi transformation guess nahi kar sakta. Isliye chahte hain ki machine khud representation seekhe: **representation learning**.
4. Lecture 24 ka SVM **kernel trick** bhi yahi karta hai, data ko aise space me le jaata hai jahan line kaam kare. Fark ye hai ki SVM me kernel hum chunte hain, deep learning me network mapping **khud seekhta** hai.
