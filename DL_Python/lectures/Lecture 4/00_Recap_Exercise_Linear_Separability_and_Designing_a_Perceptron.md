# Topic 0: Opening Exercise — Are These Points Linearly Separable? Design a Perceptron

Source: Lecture 4, slides 2–3 (Exercise; the same slide with the instructor's handwritten solution). It applies Lecture 3's linear-separability ideas.

---

## 1) Technical Explanation

**The exercise (slide 2).** Consider 2-D samples of two classes:

- **Class I:** (0,0), (0,1), (1,0), (−1,−1)
- **Class II:** (2.1, 0), (0, −2.5), (1.6, −1.6)

(i) Are these points linearly separable? (ii) Design a perceptron that separates the patterns of both classes.

**Solution (slide 3, handwritten; verified here).**

(i) **Yes**, they are linearly separable. Plotting Class I as ○ and Class II as ×, all the ○ lie on or near the origin side and all the × lie on the far, lower-right side.

(ii) The instructor draws a separating line through **(1.5, 0)** and **(0, −1.5)**. In intercept form:

x₁/1.5 + x₂/(−1.5) = 1 ⟹ x₁ − x₂ = 1.5 ⟹ **x₁ − x₂ − 1.5 = 0**.

The perceptron: weights **w₁ = 1, w₂ = −1**, bias **b = −1.5** (the neuron sketched in the slide's top-left corner), with output **1 for Class II** and **0 for Class I**:

f(x₁, x₂) = 1 if x₁ − x₂ − 1.5 > 0, else 0.

**Check of all seven points.**

| Point | x₁ − x₂ − 1.5 | f | Class |
|---|---|---|---|
| (0,0) | −1.5 | 0 | I ✓ |
| (0,1) | −2.5 | 0 | I ✓ |
| (1,0) | −0.5 | 0 | I ✓ |
| (−1,−1) | −1.5 | 0 | I ✓ |
| (2.1,0) | 0.6 | 1 | II ✓ |
| (0,−2.5) | 1.0 | 1 | II ✓ |
| (1.6,−1.6) | 1.7 | 1 | II ✓ |

All correct. The line is **not unique** — any line that separates the groups works (for instance x₁ − x₂ − 1 = 0 also does: Class I gives at most 0 − 1 = −1 < 0, Class II gives at least 2.1 − 1 = 1.1 > 0). The same recipe was used for OR in [[07_Linear_Separability_and_the_OR_Problem]] of Lecture 3: write the separating line, read off weights and bias.

**Connection.** Here the perceptron is designed *by hand* from a drawn line. The rest of this lecture shows how the machine can **find** such weights **itself** from examples ([[02_Perceptron_Learning_Algorithm_Steps_and_Update_Rule]]).

---

## 2) Simple English Explanation

You are given two groups of dots on a graph. Question 1: can **one straight line** separate them? Yes — the first group clusters near the centre, the second sits further to the lower right.

Question 2: build the perceptron for that line. Pick a line crossing the x-axis at 1.5 and the y-axis at −1.5. Its equation is x₁ − x₂ = 1.5. So the perceptron computes "x₁ minus x₂ minus 1.5" and says **group II** if the answer is positive, **group I** if not. Test all seven dots: the four group-I dots give −1.5, −2.5, −0.5, −1.5 (all negative) and the three group-II dots give 0.6, 1.0, 1.7 (all positive). 

---

## 3) Hinglish Explanation (Beginner-Friendly)

Aapko graph par dots ke do groups diye gaye hain. Sawal 1: kya **ek seedhi line** unhe alag kar sakti hai? Haan — pehla group center ke paas hai, doosra neeche-dayein door.

Sawal 2: us line ke liye perceptron banao. Ek line lo jo x-axis ko 1.5 par aur y-axis ko −1.5 par kaate. Uski equation x₁ − x₂ = 1.5 hai. To perceptron "x₁ minus x₂ minus 1.5" nikalta hai aur agar answer positive ho to **group II** bolta hai, warna **group I**. Saare saat dots test karo: group-I ke chaar dots −1.5, −2.5, −0.5, −1.5 dete hain (sab negative) aur group-II ke teen dots 0.6, 1.0, 1.7 dete hain (sab positive).
