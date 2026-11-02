# Topic 4: Geometric Interpretation of an MP Unit — Lines (2 Inputs) and Planes (3 Inputs)

Source: Lecture 5, slides 20–27 ("Can any Boolean function be represented using a McCulloch–Pitts unit?"; OR and AND on a plane with shaded regions; Tautology; "What if we have more than 2 inputs?" with the cube figure).

---

## 1) Technical Explanation

**The question (slide 20):** *Can any Boolean function be represented using a McCulloch–Pitts unit?* Before answering, the lecture gives the **geometric interpretation** of an MP unit: a unit with inputs x₁, x₂ and threshold θ outputs 1 exactly when **x₁ + x₂ ≥ θ**. The boundary x₁ + x₂ = θ is a **line** in the (x₁, x₂) plane; everything on the line and on one side gives 1, the other side gives 0.

**OR (slide 21).** θ = 1, so the rule is x₁ + x₂ ≥ 1 (the slide writes x₁ + x₂ = Σᵢ₌₁² xᵢ ≥ 1). The four input points:

| Point | x₁ + x₂ | ≥ 1? | y |
|---|---|---|---|
| (0,0) | 0 | no | 0 |
| (0,1) | 1 | yes (on the line) | 1 |
| (1,0) | 1 | yes (on the line) | 1 |
| (1,1) | 2 | yes | 1 |

The shaded half-plane x₁ + x₂ ≥ 1 contains (0,1), (1,0), (1,1); the point (0,0) lies on the other side. The instructor's "Case 1: x₁ + x₂ = 1" lists the combinations 0+1, 1+0 on the line and 1+1 above it, all giving 1.

**AND (slide 22).** θ = 2: x₁ + x₂ ≥ 2. Only (1,1) satisfies it (it lies on the boundary line, marked "+ve side"); (0,0), (0,1), (1,0) fall on the "−ve side".

**Tautology — always ON (slides 22–23).** θ = 0: x₁ + x₂ ≥ 0 holds for every input in {0,1}², so the output is **always 1** — a function that is true for all inputs. The boundary line x₁ + x₂ = 0 has **all four points on its positive side** (arrows labelled "positive side").

**More than 2 inputs (slides 24–27).** *Instead of a line we will have a plane.* With three inputs the points are the 8 corners of the unit **cube** (figure: corners (0,0,0), (0,0,1), (0,1,0), (1,0,0), (0,1,1), (1,0,1), (1,1,0), (1,1,1)). For OR (θ = 1), the plane x₁ + x₂ + x₃ = 1 passes through the three corners (1,0,0), (0,1,0), (0,0,1) (the blue triangle drawn inside the cube) and **(0,0,0) lies on one side while the remaining 7 points lie on the other side** — the instructor's handwritten count: *8 inputs: 1st side = 1 point, 2nd side = 7 points*. (The slide's coordinate labels place the cube's z axis vertical; the corner labelled (0,1,1) on the slide appears at the top-left.)

**A subtle point about "separation".** In an MP unit the boundary points themselves count as ON (because f uses ≥ θ). So for OR the points (0,1) and (1,0) lie *on* the line, not strictly beside it. In the perceptron of Lecture 3 (f = 1 iff w·x + b > 0, strict) the line would be nudged (e.g. x₁ + x₂ = 0.3) so that no point sits on it ([[07_Linear_Separability_and_the_OR_Problem]]). The two descriptions are equivalent: x₁ + x₂ ≥ 1 is the same as x₁ + x₂ − 0.5 > 0 on binary inputs.

**Answer to the opening question** — taken up in [[05_Linear_Separability_of_Boolean_Functions]]: *not every* Boolean function.

---

## 2) Simple English Explanation

Draw the two inputs as a graph: x₁ across, x₂ up. The four possible input pairs are the four corners of a square. An MP unit draws **one straight line** across the graph and says "1" for corners on or beyond the line, and "0" for the rest.

- **OR** (threshold 1): the line x₁ + x₂ = 1 cuts off only the corner (0,0). Everything else is "1".
- **AND** (threshold 2): the line x₁ + x₂ = 2 touches only (1,1). Just that corner is "1".
- **Always ON** (threshold 0): the line sits so low that all four corners are on the "1" side.

With **three inputs** the picture becomes a **cube** with 8 corners and the line becomes a flat **sheet** (plane). For OR, the sheet slices off the single corner (0,0,0) from the other 7.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Do inputs ko graph par draw karo: x₁ aadi taraf, x₂ upar. Do inputs ke chaar possible pairs ek square ke chaar corners hain. Ek MP unit graph par **ek seedhi line** kheenchta hai aur line par ya uske paar wale corners ke liye "1" bolta hai, baaki ke liye "0".

- **OR** (threshold 1): line x₁ + x₂ = 1 sirf corner (0,0) ko kaat deti hai. Baaki sab "1" hain.
- **AND** (threshold 2): line x₁ + x₂ = 2 sirf (1,1) ko chhoti hai. Sirf wahi corner "1" hai.
- **Hamesha ON** (threshold 0): line itni neeche hai ki chaaron corners "1" wali taraf hain.

**Teen inputs** ke saath picture ek **cube** ban jaati hai jisme 8 corners hain aur line ek chapti **sheet (plane)** ban jaati hai. OR ke liye, sheet akele corner (0,0,0) ko baaki 7 se alag kar deti hai.
