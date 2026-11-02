# Topic 6: Kernels: Linear vs Non-linear Problems and the Kernel Trick

Source: Lecture 24, slides 15–19:
- Slide 15: "Linear vs. nonlinear problems", panels A and B.
- Slide 16: "Fig. 1: SVM schematic diagram" (a)–(c), "Linear to nonlinear", "Feature space map", "Complex in low dimension", "Simple in higher dimension", handwritten "kernel transformation".
- Slide 17: ring-shaped x–y scatter.
- Slide 18: the same data plotted against z = x² + y², with one point circled.
- Slide 19: "This transformation is called kernel".

Also slide 5's kernel list and slide 2's note "kernels 2D → 3D". Enriched with the kernel-trick derivation (Boser–Guyon–Vapnik 1992) and our own verification runs.

---

## 1) Technical Explanation

### Slide 15: linear vs non-linear problems

- **Panel A:** green and blue points split by a straight dotted diagonal. The problem is **linearly separable**, and a linear SVM is enough.
- **Panel B:** blue points form a blob in the centre, surrounded by a ring of green points. A dotted **circle** separates them. **No straight line can**, so the problem is non-linear. This is the same situation as XOR in [[06_Linear_Separability_Concept]] from Lecture 4.

### Slide 16: the SVM schematic

- **(a)** A linear SVM: the hyperplane, the margin and circled support vectors between blue dots and red triangles.
- **(b)** "Linear to nonlinear": red triangles inside an ellipse, surrounded by blue dots. "**Complex in low dimension**."
- **(c)** "Feature space map": the same points lifted into **3-D**, where a flat yellow **hyperplane** separates them. "**Simple in higher dimension**."
- The handwritten arrow from (b) to (c) reads "**kernel transformation**".

### Slides 17–19: the worked idea, z = x² + y²

- **Slide 17.** Green squares cluster around the origin and blue diamonds form a ring around them in the x–y plane. There is no straight separator.
- **Slide 18.** Add a new coordinate **z = x² + y²**, the squared distance from the origin.
  - Points near the centre get a small z and points on the ring get a large z.
  - Plotted on the vertical z axis, the classes are now separated by a **horizontal line** z = constant. That line is a hyperplane in the new space, and it is a **circle** x² + y² = constant back in the original space.
  - One blue diamond is circled in red. It was the blue point lying among the green ones near the centre on slide 17. After the transformation it is still below the line. Even in the new space, this point needs the **soft margin** to be tolerated as an error ([[04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin]]).
- **Slide 19.** "This transformation is called **kernel**."

*Precise terminology.*
- The mapping φ(x, y) = (x, y, x² + y²) is a **feature map**.
- A **kernel** is the function that returns the dot product in that new space: **K(u, v) = φ(u)·φ(v)**.
- The slide's informal wording ("the transformation is the kernel") is common in introductory material.

### The kernel trick: why we never need to compute φ

When the SVM problem is written in its **dual form**, the data appear only inside dot products:

  maximise Σ αᵢ − ½ Σᵢ Σⱼ αᵢ αⱼ yᵢ yⱼ (xᵢ·xⱼ),  0 ≤ αᵢ ≤ C, Σ αᵢ yᵢ = 0

  prediction f(x) = sign( Σᵢ αᵢ yᵢ (xᵢ·x) + b )

Replace every xᵢ·xⱼ with K(xᵢ, xⱼ), and the SVM works in φ-space **without ever computing φ**. That space can even be infinite-dimensional, as it is for RBF.

**Verification (our numbers): the degree-2 polynomial kernel.**
- Let K(a, c) = (a·c)² with a = (1, 2) and c = (3, 4).
- Directly: a·c = 3 + 8 = 11, so K = **121**.
- Through the explicit map φ(v) = (v₁², √2·v₁v₂, v₂²):
  - φ(a) = (1, 2√2, 4) and φ(c) = (9, 12√2, 16).
  - φ(a)·φ(c) = 9 + 48 + 64 = **121** ✔
- One multiplication in 2-D gives the same answer as building and multiplying the 3-D vectors.

### The kernels on slide 5 (formulas as in scikit-learn)

| Kernel | K(x, z) | Use (slide 5) |
|---|---|---|
| **Linear** | x·z | "suitable for linearly separable data". Also good for very high-dimensional data such as text. |
| **Polynomial** | (γ x·z + r)^d | "for curved boundaries". The degree d controls the flexibility. |
| **RBF (Gaussian)** | exp(−γ‖x − z‖²) | "captures complex relationships". scikit-learn's default. The γ knob is in [[05_Gamma_and_Regularization_C]]. |
| (Sigmoid) | tanh(γ x·z + r) | not on the slide; neural-network-like |

A valid kernel must correspond to a dot product in some space. Formally this is **Mercer's condition**: the kernel matrix must be positive semi-definite.

### Experiment (our own; `make_circles`, 400 points, inner circle vs ring, 70/30 split)

| Model | Train accuracy | Test accuracy | # support vectors |
|---|---|---|---|
| Linear SVM on (x, y) | 0.657 | 0.633 | 274 |
| **Linear SVM on (x, y, z = x² + y²)** (slide 18's idea, explicit φ) | **1.000** | **1.000** | 15 |
| Polynomial kernel, degree 2 | 1.000 | 1.000 | 11 |
| RBF kernel (defaults) | 1.000 | 1.000 | 18 |

- In this data, z ranges over 0.013–0.255 for inner points and 0.637–1.436 for ring points. A single threshold on z separates them perfectly, exactly as in slide 18.
- The linear SVM on raw (x, y) is barely better than guessing, and most points become support vectors.

---

## 2) Simple English Explanation

**Slide 15: the problem.**
- In picture **A**, a straight line separates green from blue. That's easy.
- In picture **B**, blue dots sit in the middle and green dots surround them like a ring. **No straight line** can separate them. You need a circle.
- A plain SVM only draws straight lines, so what can we do?

**The clever idea (slides 16–19): add a new dimension.**
- Slide 17 shows green squares in the middle and blue diamonds in a ring around them. Now give every point a **height**: z = x² + y², which is just "how far you are from the centre, squared".
  - Points in the middle get a small height and stay low.
  - Points on the ring get a big height and float up.
- On slide 18, plotted with this height, the blue points are all up high and the green ones are down low. Now a **flat horizontal line** separates them perfectly.
- When you bring that flat cut back to the original flat picture, it becomes a **circle**, which is exactly what we needed.
- Slide 16 shows the same idea in 3-D. The points look tangled when flat ("complex in low dimension"). Lift them into 3-D and a flat sheet slices between them ("simple in higher dimension"). The teacher wrote "kernel transformation" on the arrow.
- On slide 18 one blue point is circled. It was hiding among the green points near the centre, so even after lifting it stays low on the wrong side. The soft margin simply accepts it as one mistake.

**What's a "kernel"?**
- Slide 19 says "this transformation is called kernel".
- More precisely, the kernel is a shortcut formula that tells the SVM how similar two points would be **after** lifting, without actually doing the lifting. This is the famous "**kernel trick**".
- It matters because some lifts go into thousands or even infinitely many dimensions, which a computer could never build directly.

**Checking the trick with real numbers.**
- Take points (1, 2) and (3, 4).
- Shortcut: (1×3 + 2×4)² = 11² = **121**.
- Long way: lift both points into 3-D, (1, 2.83, 4) and (9, 16.97, 16), and multiply matching parts: 9 + 48 + 64 = **121**.
- Same answer, but the shortcut needed far less work.

**The three kernels on slide 5:**
- **Linear:** a straight boundary, for data that is already separable.
- **Polynomial:** gently curved boundaries.
- **RBF:** very flexible boundaries for complicated shapes. This is the default in Python's scikit-learn.

**Our experiment on ring-shaped data:**
- A plain straight-line SVM got only **63%** right.
- Adding the slide's height z = x² + y² gave **100%**.
- The polynomial and RBF kernels also got **100%**, automatically, without us inventing the height feature ourselves.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 15: problem.**
- Picture **A** mein seedhi line green aur blue ko alag kar deti hai. Aasaan hai (linearly separable).
- Picture **B** mein blue beech mein hain aur green unke chaaron taraf ring bana rahe hain. **Koi seedhi line** inhe alag nahi kar sakti, circle chahiye. Ye Lecture 4 ke XOR jaisa non-linear problem hai.
- Simple SVM sirf seedhi line kheenchta hai. Ab kya karein?

**Smart idea (slides 16–19): ek naya dimension jodo.**
- Slide 17: green squares beech mein, blue diamonds ring mein. Har point ko ek **unchai (height)** do: **z = x² + y²**, yaani centre se doori ka square.
  - Beech wale points ki height kam, woh neeche rahenge.
  - Ring wale points ki height zyada, woh upar uth jaayenge.
- Slide 18: is height ke saath plot karo to saare blue upar aur saare green neeche. Ab ek **seedhi horizontal line** (orange) inhe perfectly alag kar deti hai.
- Ye flat line jab original x–y picture mein wapas laate ho, to woh **circle** (x² + y² = constant) ban jaati hai. Bilkul wahi jo chahiye tha!
- Slide 16 3-D mein yahi dikhata hai: flat picture mein points uljhe hue ("complex in low dimension"), 3-D mein uthao to ek flat sheet (hyperplane) beech se kaat deti hai ("simple in higher dimension"). Teacher ne arrow pe likha "**kernel transformation**". Slide 2 ka "kernels 2D → 3D" bhi yahi hai.
- Slide 18 pe ek blue point laal circle mein hai. Ye slide 17 mein beech mein green ke saath chhupa tha, isliye upar uthne ke baad bhi line ke neeche (galat side) hai. Ise **soft margin** ek galti maan ke chhod deta hai.

**"Kernel" asal mein kya hai?**
- Slide 19 kehta hai "This transformation is called kernel".
- Thoda precise baat: transformation φ ko **feature map** kehte hain. **Kernel** woh shortcut formula hai jo batata hai ki uthane ke *baad* do points kitne similar (dot product) honge, bina asal mein uthaye: K(u, v) = φ(u)·φ(v). Isi ko "**kernel trick**" kehte hain.
- Kyun zaroori? Kuch transformations hazaaron ya infinite dimensions mein le jaate hain (jaise RBF). Computer unhe seedhe bana hi nahi sakta, par shortcut se kaam chal jata hai.
- SVM ke dual form mein data sirf dot products (xᵢ·xⱼ) ke roop mein aata hai, isliye har dot product ko K(xᵢ, xⱼ) se badal do, bas.

**Trick ko numbers se check karo.** Points (1, 2) aur (3, 4) lo.
- **Shortcut:** (1×3 + 2×4)² = 11² = **121**.
- **Lamba raasta:** φ(v) = (v₁², √2·v₁v₂, v₂²) se 3-D mein le jao: (1, 2√2, 4) aur (9, 12√2, 16). Ab dot product: 9 + 48 + 64 = **121** ✔.
- Same jawaab, par shortcut mein kahin kam mehnat.

**Slide 5 ke kernels:**
- **Linear** (x·z): seedhi boundary, already separable data ke liye. Text jaise bahut zyada features wale data pe bhi badhiya.
- **Polynomial** ((γx·z + r)^d): halki curved boundaries. Degree d se flexibility badhti hai.
- **RBF** (exp(−γ‖x − z‖²)): bahut flexible, complicated shapes ke liye. scikit-learn ka default yahi hai.
- (Sigmoid bhi hota hai, par slide pe nahi hai.)
- Valid kernel ke liye **Mercer's condition** honi chahiye, yaani kernel kisi space ka dot product hona chahiye.

**Humara experiment (ring wala data, 400 points):**
- Seedhi line wala SVM, raw (x, y) pe: test sirf **63.3%**, aur 274 support vectors (lagbhag sab points).
- Slide ki height z = x² + y² jodke linear SVM: **100%**. Is data mein andar wale points ka z 0.013–0.255 aur ring wale ka 0.637–1.436 hai, to ek seedhi line saaf kaat deti hai.
- Polynomial (degree 2) aur RBF kernel: dono **100%**, apne aap, bina humare height feature banaye.
