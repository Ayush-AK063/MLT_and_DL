# Topic 5: Broad Categories of Problems — Regression vs Classification, Linear and Non-Linear

Source: Lecture 3, slides 26–28 (Broad Categories of Problem; Regression; Classification).

---

## 1) Technical Explanation

**Slide 26 — two broad problem types**, each drawn as an x–y scatter plot:

- **Regression** — predict a **continuous number y** from x. The plot: blue points along an upward trend with a red **fitted line** passing through them.
- **Classification** — predict a **category**. The plot: two groups of points (blue and green) in different regions, separated by a red **decision line**.

**Slide 27 — Regression, linear vs non-linear.**

- *Linear:* the fitted curve is a straight line through points that roughly lie on a line.
- *Non-linear:* the fitted red curve bends — rising, dipping, then rising again — to follow points that no straight line could fit.

**Slide 28 — Classification, linear vs non-linear.**

- *Linear:* a **straight line** separates the blue class from the green class (a few green points sit on the blue side — noise).
- *Non-linear:* the two classes overlap in a cluster, and the boundary is a closed **curve (an ellipse)**: blue points mostly inside, green mostly outside. No straight line can separate them.

**Connection to the perceptron.** A perceptron's boundary w·x + b = 0 is a straight line/plane, so it can only handle the **linear classification** case — see [[07_Linear_Separability_and_the_OR_Problem]] and [[08_Linear_Non_Separability_XOR_and_Hyperplanes]]. The same linear-vs-non-linear regression/classification ideas, and a worked regression with gradient descent, appear in Lecture 10 ([[02_Simple_Linear_Regression_Intuition_Home_Price_Example]]). Compare the representation point of [[08_Issue_and_Choice_of_Representation]]: the ellipse case becomes linearly separable after a suitable change of representation (e.g. using distance from the centre).

---

## 2) Simple English Explanation

Prediction problems come in two flavours:

- **Regression:** the answer is a **number** — e.g. the price of a house. You draw a line (or curve) through the dots and read off the answer.
- **Classification:** the answer is a **label** — e.g. spam or not spam. You draw a boundary that splits the dots into groups.

Each can be **linear** (a straight line is enough) or **non-linear** (you need a curve). For classification, if one group is *surrounded* by the other like an island, no straight line can split them — you need a loop. A single perceptron can only draw straight lines.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Prediction problems do tarah ki hoti hain:

- **Regression:** jawab ek **number** hota hai — jaise ghar ka daam. Aap dots ke beech se ek line (ya curve) kheenchte ho aur jawab padh lete ho.
- **Classification:** jawab ek **label** hota hai — jaise spam ya not spam. Aap ek boundary kheenchte ho jo dots ko groups mein baant deti hai.

Dono **linear** (seedhi line kaafi hai) ya **non-linear** (curve chahiye) ho sakti hain. Classification mein agar ek group doosre ke beech mein *ghira* ho, jaise tapu, to koi seedhi line unhe alag nahi kar sakti — loop chahiye. Ek akela perceptron sirf seedhi lines kheench sakta hai.
