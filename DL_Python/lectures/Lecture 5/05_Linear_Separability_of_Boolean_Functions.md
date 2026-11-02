# Topic 5: Linear Separability of Boolean Functions — What a Single MP Neuron Can and Cannot Do

Source: Lecture 5, slides 28–29 (A single McCulloch–Pitts neuron can be used to represent Boolean functions which are linearly separable; definition of linear separability for Boolean functions).

---

## 1) Technical Explanation

**Statement (slide 28).** *A single McCulloch–Pitts neuron can be used to represent Boolean functions which are linearly separable.*

**Definition (slide 29).** *Linear separability (for Boolean functions): there exists a line (plane) such that all inputs which produce a 1 lie on one side of the line (plane) and all inputs which produce a 0 lie on the other side of the line (plane).*

This answers the question posed in [[04_Geometric_Interpretation_of_an_MP_Unit_Lines_and_Planes]]: **no — only linearly separable Boolean functions** can be computed by one MP unit.

**Examples checked in this lecture.** AND, OR, NOR, NOT and the tautology are all linearly separable (each was realised with one unit in [[03_Implementing_Boolean_Functions_AND_OR_NOR_NOT_with_MP_Units]]). **XOR is not** — see the algebraic proof in [[08_Linear_Non_Separability_XOR_and_Hyperplanes]] of Lecture 3 (the 1-points (0,1),(1,0) and 0-points (0,0),(1,1) are on opposite diagonals of the square). The lecture deck does not work XOR here; it is the starting point of Lecture 6/7.

**How many Boolean functions are separable?** (Background, not on the slide.) With n inputs there are 2^(2ⁿ) Boolean functions. For n = 2 there are 16, and **14 are linearly separable** — all except XOR and XNOR. For n = 3 only 104 of the 256 are threshold-computable, and the fraction collapses rapidly as n grows. This is why a single unit is far too weak for general logic and why networks of units are needed (Lecture 6).

**Relation to the perceptron.** The same statement holds for the perceptron of Lecture 3 ([[07_Linear_Separability_and_the_OR_Problem]]), with the generalisation that the perceptron's weights are real numbers and *learnable* ([[03_Worked_Example_Boolean_AND_Perceptron_Learning_Epoch_by_Epoch]]), whereas the basic MP unit's weights are fixed and its θ is chosen by hand.

---

## 2) Simple English Explanation

One MP neuron can do a logic job **only if** you can draw one straight line (or flat sheet, with 3 or more inputs) that puts all the "1" cases on one side and all the "0" cases on the other.

- AND, OR, NOR, NOT: yes, a line works.
- XOR ("exactly one is on"): no line works — you need more than one neuron working together.

So the answer to "can any logic function be made with one MP neuron?" is **no, only the line-separable ones**. (Even among 2-input functions, 14 of the 16 work; XOR and XNOR are the two that don't.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek MP neuron koi logic kaam **tabhi** kar sakta hai jab aap ek seedhi line (ya 3+ inputs ke liye chapti sheet) kheench sako jo saare "1" cases ek taraf aur saare "0" cases doosri taraf kar de.

- AND, OR, NOR, NOT: haan, line kaam karti hai.
- XOR ("theek ek input on"): koi line kaam nahi karti — aapko ek se zyada neurons ko milkar kaam karna padega.

To "kya koi bhi logic function ek MP neuron se ban sakta hai?" ka jawab hai **nahi, sirf line se alag hone wale**. (2-input functions mein bhi 16 mein se 14 kaam karte hain; XOR aur XNOR do hain jo nahi karte.)
