# Topic 8: Linear Non-Separability (XOR) and Hyperplanes in n Dimensions

Source: Lecture 3, slides 32–33 (LINEAR NON-SEPARABILITY with the handwritten XOR table and "NAND, NOR problems" figures; line / plane / hyperplane slide). Slide 34 is "Thank you".

---

## 1) Technical Explanation

**Definition (slide 32).** *If no straight line can possibly separate the samples belonging to two classes, then it is not possible for a single perceptron to achieve the classification task. The samples are "Not-Linearly separable".*

**The XOR problem.** Handwritten truth table on the slide:

| x₁ | x₂ | XOR output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Plotted on the plane, the 1-class points are the diagonal pair (0,1) and (1,0), and the 0-class points are the other diagonal pair (0,0) and (1,1). Any straight line that puts (0,1) and (1,0) on one side would have to put (0,0) or (1,1) there too. **Proof sketch (not on the slide):** suppose weights w₁, w₂ and bias b satisfy the four conditions. Then b ≤ 0 (for (0,0) → 0), w₁ + b > 0 and w₂ + b > 0 (for the two 1-points), and w₁ + w₂ + b ≤ 0 (for (1,1) → 0). Adding the two middle inequalities: w₁ + w₂ + 2b > 0. Subtracting the last: b > 0 — contradicting b ≤ 0. So **no single perceptron computes XOR**, which is the central limitation Minsky and Papert pointed out in 1969 ([[02_History_of_the_Perceptron_and_the_Biological_Neuron]]) and which multilayer perceptrons overcome — worked through in Lecture 7 (XOR implementation) after Lecture 6 (MLPs).

**Flag — "NAND, NOR problems" label.** The slide writes "NAND, NOR Problems" above two grid pictures labelled *Peninsula* and *Island* (grids of × and ○ where one symbol forms a block or an enclosed region). But **NAND and NOR are linearly separable** — one perceptron computes each (e.g. NAND: −x₁ − x₂ + 1.5 > 0; NOR: −x₁ − x₂ + 0.5 > 0 — both checked here against all four input pairs). So these are not valid examples of non-separability. The two grids are better read as generic *non-linearly-separable region shapes* (a region and an enclosed island); the "NAND, NOR" annotation is likely a slip or refers to something not shown.

**Hyperplanes (slide 33).**

- 2-D inputs (x₁, x₂): a **line (1-D)** separates two classes.
- 3-D inputs (x₁, x₂, x₃): a **plane (2-D)** separates them.
- In n dimensions you need an **(n−1)-dimensional hyperplane**.
- "In general, linear separability is used to check if you can separate points in an n-dimensional space using only n−1 dimensions."

The hyperplane is the set w·x + b = 0 of [[03_The_Perceptron_Function]]: the weights vector w is perpendicular to it and the bias shifts it away from the origin. The slide's handwritten labels ("line-1D", "plane-2D", "hyperplane", and a 4-input sketch x₁…x₄) are consistent with this rule: n inputs → an (n−1)-dimensional hyperplane.

---

## 2) Simple English Explanation

Some problems cannot be split by **any** straight line. The classic one is **XOR** ("exclusive or": the answer is 1 only if the two inputs are *different*). On the graph, the two "1" points sit at opposite corners of a square, and so do the two "0" points — like a chess-board pattern. Try to draw one straight line separating them: you can't. So a single perceptron **cannot** learn XOR. (A short algebra proof is in the technical section.) This was a famous weakness pointed out in 1969.

**Careful:** the slide mentions NAND and NOR as examples too, but those *can* be solved by one perceptron — the slide label looks like a slip.

**More dimensions:** with 2 inputs the splitter is a **line**, with 3 inputs a flat **sheet (plane)**, and with n inputs a flat "sheet" with one dimension fewer than the space — a **hyperplane**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Kuch problems **kisi bhi** seedhi line se alag nahi ho sakti. Classic example **XOR** hai ("exclusive or": jawab 1 tabhi jab dono inputs *alag* hon). Graph par, dono "1" points square ke opposite corners par hain, aur dono "0" points bhi — chess-board jaisa pattern. Ek seedhi line se unhe alag karne ki koshish karo: nahi ho sakta. To ek akela perceptron XOR **nahi seekh sakta**. (Chhota algebra proof technical section mein hai.) 1969 mein ye ek mashhoor kamzori batayi gayi thi.

**Dhyan rahe:** slide NAND aur NOR ko bhi example batati hai, par unhe ek perceptron *solve kar sakta hai* — slide ka label galti jaisa lagta hai.

**Zyada dimensions:** 2 inputs par splitter ek **line** hai, 3 inputs par ek chapti **sheet (plane)**, aur n inputs par ek aisi "sheet" jisme space se ek dimension kam hota hai — **hyperplane**.
