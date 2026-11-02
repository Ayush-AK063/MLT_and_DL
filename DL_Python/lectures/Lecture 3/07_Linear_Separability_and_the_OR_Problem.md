# Topic 7: Linear Separability and the OR Problem (Building a Perceptron from a Line)

Source: Lecture 3, slides 30–31 (LINEAR SEPARABILITY; hand-worked "OR Problem").

---

## 1) Technical Explanation

**Definition (slide 30).** *For 2-dimensional inputs, if there exists a line that separates all samples of one class from the other class, then such a classification problem is called "linearly separable", i.e. separable by a linear combination of inputs.* Companion statement: *An appropriate perceptron can be derived from the equation of the separating line.* The figure shows two scatter plots: **Linearly Separable** (red and blue groups with a line between them) and **Not Linearly Separable** (red and blue dots mixed together).

**The OR problem, worked by hand (slide 31).** Truth table:

| x₁ | x₂ | OR output | Class (as marked) |
|---|---|---|---|
| 0 | 0 | 0 | Class 1 (circle ○) |
| 0 | 1 | 1 | Class 2 (cross ×) |
| 1 | 0 | 1 | Class 2 (×) |
| 1 | 1 | 1 | Class 2 (×) |

Plot the four points on the (x₁, x₂) plane. A separating line is drawn cutting the axes at **(0.3, 0)** and **(0, 0.3)**, with the origin on one side and the other three points on the other. The line's equation in intercept form is

x₁/0.3 + x₂/0.3 = 1 ⟹ x₁ + x₂ = 0.3 ⟹ **x₁ + x₂ − 0.3 = 0**.

Reading off the perceptron: weights **w₁ = 1, w₂ = 1**, bias **b = −0.3** (the "−0.3" on the neuron in the slide), output "OR problem". So

f(x₁, x₂) = 1 if x₁ + x₂ − 0.3 > 0, else 0.

**Verification (done here).**

| (x₁, x₂) | x₁ + x₂ − 0.3 | f | OR |
|---|---|---|---|
| (0, 0) | −0.3 | 0 | 0 ✓ |
| (0, 1) | 0.7 | 1 | 1 ✓ |
| (1, 0) | 0.7 | 1 | 1 ✓ |
| (1, 1) | 1.7 | 1 | 1 ✓ |

All four rows match, so one perceptron computes OR. The value 0.3 is not special: any threshold strictly between 0 and 1 works (the line only has to pass between (0,0) and the other points). The same trick gives AND (e.g. x₁ + x₂ − 1.5 > 0) — this is the Boolean-function theme revisited in Lecture 5 (McCulloch–Pitts thresholding logic).

**General rule.** Linearly separable problem ⟹ some perceptron solves it exactly (the geometry of the line is the perceptron: weights = the line's coefficients, bias = its constant). Not linearly separable ⟹ no single perceptron can ([[08_Linear_Non_Separability_XOR_and_Hyperplanes]]).

---

## 2) Simple English Explanation

If you can draw **one straight line** that puts all the "yes" dots on one side and all the "no" dots on the other, the problem is **linearly separable**, and one perceptron can solve it — the perceptron *is* that line.

**OR example.** OR is "1 if either input is 1". Put the four input pairs on a graph: only (0,0) gives 0. A line cutting the axes at 0.3 on each side keeps (0,0) alone on one side. That line is x₁ + x₂ = 0.3, so the perceptron says "add the two inputs, subtract 0.3; if the result is positive, output 1". Check: (0,0) → −0.3 → 0 ✓; the other three give 0.7, 0.7, 1.7 → 1 ✓.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Agar aap **ek seedhi line** kheench sakte ho jo saare "haan" dots ek taraf aur saare "naa" dots doosri taraf kar de, to problem **linearly separable** hai, aur ek perceptron use solve kar sakta hai — perceptron *wahi line* hai.

**OR ka example.** OR ka matlab "agar koi bhi input 1 ho to output 1". Chaaron input pairs ko graph par rakho: sirf (0,0) ka output 0 hai. Ek line jo axes ko har taraf 0.3 par kaate, (0,0) ko akela ek taraf rakhti hai. Wo line x₁ + x₂ = 0.3 hai, to perceptron kehta hai "dono inputs jodo, 0.3 ghatao; agar result positive ho to output 1". Check karo: (0,0) → −0.3 → 0 ✓; baaki teen 0.7, 0.7, 1.7 dete hain → 1 ✓.
