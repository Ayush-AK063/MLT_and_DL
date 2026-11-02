# Topic 6: Computational Graphs and the Depth of a Model

Source: Lecture 26, slides 13–15 ("Computational Graphs", from the *Deep Learning* book, Fig. 1.3: the graph σ(w₁x₁ + w₂x₂) built from the element set {+, ×, σ}, and the same model as one "Logistic Regression" node; note on slide 15: "Depth of architecture in terms of length of the path from input to output. Previous shallow architecture can do computation in parallel but not sequential."). Enriched with web research (Goodfellow et al., *Deep Learning*, 2016, ch. 1 and §6.5.1). Worked numbers are ours.

---

## 1) Technical Explanation

### What a computational graph is

A **computational graph** draws a calculation as a network:

- each **node** is either an input value or one elementary operation;
- each **arrow** carries a value from one node into the operation that uses it.

The allowed operations are listed in an **element set**. The calculation flows from the inputs at the bottom to the output at the top.

### Slide 13: logistic regression as a graph with element set {+, ×, σ}

The graph computes

  **ŷ = σ(w₁x₁ + w₂x₂)**,  where **σ(z) = 1 / (1 + e⁻ᶻ)** is the logistic sigmoid ([[03_The_Sigmoid_Function_and_Decision_Boundary]] from Lecture 15).

Bottom to top:

1. Inputs: w₁, x₁, w₂, x₂ (four leaf nodes).
2. Two **×** nodes: w₁·x₁ and w₂·x₂.
3. One **+** node: z = w₁x₁ + w₂x₂.
4. One **σ** node: ŷ = σ(z).

(The book's figure has no bias term. Adding one would need one more input leaf feeding the + node; the depth would not change.)

**Worked example (ours).** w = (2, −1), x = (1, 3):

- × nodes: 2·1 = **2**, (−1)·3 = **−3**
- + node: z = 2 + (−3) = **−1**
- σ node: σ(−1) = 1 / (1 + e¹) = 1 / 3.7183 = **0.2689**

So the model gives probability ≈ 0.27 of class 1. A second check: w = (0.5, 1), x = (2, 1) gives z = 2 and σ(2) = **0.8808**.

### Slides 14–15: the same model with a different element set

On the right, the element set contains just one operation, **"Logistic Regression"**. The whole model is now a single node taking the vectors **w** and **x** as input and outputting σ(w·x).

Same mathematical function, two different drawings.

### Depth = length of the longest path from input to output

The note on slide 15: depth of an architecture is measured "in terms of the length of the path from input to output".

- With element set **{+, ×, σ}**: the longest path is w₁ → × → + → σ, which is **3 operations**. **Depth = 3.**
- With element set **{Logistic Regression}**: w → LR, **1 operation**. **Depth = 1.**

**There is no single correct depth for a model.** Depth depends on what you count as one step, that is, on the element set. The book makes exactly this point: the same function has depth 3 or depth 1 depending on the language used to describe it. In neural networks the usual convention is to count **layers** (each layer = affine transform + activation as one step), so "a 50-layer network" means depth 50 in that language.

The book also describes a second way of measuring depth, used for probabilistic models: the depth of the graph describing **how concepts relate to each other**, rather than the depth of the computation. For example, a model might first find eyes in a face image and then use them to refine its estimate of the face, which can make the computation graph much deeper than the concept graph.

### "Shallow can compute in parallel but not sequentially"

The second sentence of slide 15's note is compressed. It refers to the book's second view of depth: **depth = how many sequential steps a program can take.**

- Each layer can be seen as the state of the computer's memory after executing one batch of instructions **in parallel**.
- A **shallow** model (one layer, such as logistic regression as a single node) does all its work in one parallel step. Nothing it computes can be used as the input to a later step.
- A **deep** model can run more instructions **in sequence**. Later steps can refer back to results of earlier steps (corners use edges, parts use corners). This gives much more expressive power. The book notes that not all the information in a layer's activations must encode factors of variation; some of it can be "state" that helps the network organise its computation, like counters or pointers in a program.

So a shallow architecture can compute many things side by side, but cannot chain computations where the next step needs the previous one's result. Depth adds that chaining.

### Why computational graphs matter beyond this slide

All modern deep-learning libraries (PyTorch, TensorFlow, JAX) represent models as computational graphs. Once the graph exists, the library computes gradients automatically by applying the chain rule backwards along the arrows. This is **back-propagation** (the book's §6.5). For our small graph, ∂ŷ/∂w₁ = σ(z)(1 − σ(z))·x₁; at the worked example this is 0.2689 × 0.7311 × 1 = 0.1966. That is how the weights of every layer get trained.

---

## 2) Simple English Explanation

**A computational graph is a drawing of a calculation.** Each circle is either a number we start with or one simple operation (add, multiply, squash). Arrows show which results flow into which operation. You read it from the bottom (inputs) to the top (answer). The **element set** is the list of operations you are allowed to use.

**Slide 13: the graph for logistic regression** using three operations: **+** (add), **×** (multiply) and **σ** (sigmoid, a function that squashes any number into the range 0 to 1, from Lecture 15).

Bottom to top:
1. Start with four numbers: w₁, x₁, w₂, x₂ (two weights, two inputs).
2. Multiply: w₁ × x₁ and w₂ × x₂.
3. Add those two results.
4. Put the sum through σ to get a probability.

**Let's try it with numbers:** weights w = (2, −1), inputs x = (1, 3).
- Multiply: 2 × 1 = 2, and −1 × 3 = −3.
- Add: 2 + (−3) = −1.
- Sigmoid: σ(−1) = 1 / (1 + e¹) = 1 / 3.718 ≈ 0.27.

So the model says "27% chance of class 1". Another try: w = (0.5, 1), x = (2, 1) → 1 + 1 = 2 → σ(2) ≈ 0.88.

**Slides 14–15: the same calculation drawn differently.** If "logistic regression" itself is allowed as one single operation, the whole graph becomes one box with inputs w and x. Same answer, simpler drawing.

**What is "depth"?** The number of steps on the longest path from an input to the output.
- With {+, ×, σ}: multiply → add → sigmoid = **3 steps, depth 3**.
- With {Logistic Regression}: **1 step, depth 1**.

So depth isn't a fixed property of the maths. **It depends on what you count as one step.** In neural networks people usually count layers.

**"Shallow models compute in parallel but not in sequence":** think of a kitchen. A shallow model is like many cooks each doing one job at the same moment, with no one allowed to use another's result. A deep model is like an assembly line: one cook chops, the next fries what was chopped, the next plates what was fried. Because later steps can build on earlier ones, a deep model can do much more complicated things, like edges → corners → parts → objects.

**Why it matters:** modern tools like PyTorch and TensorFlow store every model as such a graph. Then the computer can automatically work backwards through the arrows to find how to adjust every weight. This is called *back-propagation*, and it is how deep networks learn.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Computational graph** ek calculation ka diagram hai. Har circle (node) ya to ek input value hai ya ek chhota operation (add, multiply, sigmoid). Arrows dikhate hain ki kaun sa result kis operation me ja raha hai. Neeche (inputs) se upar (output) padhte hain. **Element set** = allowed operations ki list.

**Slide 13: Logistic regression ka graph, element set {+, ×, σ}.**
Formula: **ŷ = σ(w₁x₁ + w₂x₂)**, jahan σ(z) = 1/(1 + e⁻ᶻ) sigmoid hai (Lecture 15), jo kisi bhi number ko 0 aur 1 ke beech daba deta hai.

Neeche se upar:
1. Inputs: w₁, x₁, w₂, x₂ (do weights, do inputs).
2. Do **×** nodes: w₁·x₁ aur w₂·x₂.
3. Ek **+** node: z = w₁x₁ + w₂x₂.
4. Ek **σ** node: ŷ = σ(z).

(Book ke figure me bias b nahi hai. Daalna ho to + node me ek aur input jaayega, depth same rahegi.)

**Numbers ke saath (humara example):** w = (2, −1), x = (1, 3).
- Multiply: 2×1 = **2**, (−1)×3 = **−3**
- Add: z = 2 + (−3) = **−1**
- Sigmoid: σ(−1) = 1/(1 + e¹) = 1/3.718 = **0.2689**
Matlab class 1 ki probability lagbhag 27%. Doosra check: w = (0.5, 1), x = (2, 1) → z = 2 → σ(2) = **0.8808**.

**Slides 14–15: same model, alag element set.** Agar "Logistic Regression" khud ek operation maan lo, to poora graph ek hi node ban jaata hai jisme w aur x jaate hain. Function wahi, drawing alag.

**Depth = input se output tak ka sabse lamba path.**
- {+, ×, σ} se: w₁ → × → + → σ = **3 steps, depth 3**.
- {Logistic Regression} se: w → LR = **1 step, depth 1**.

Yaani depth ki koi ek "sahi" value nahi hai, **ye depend karta hai ki ek step kise maana**. Neural networks me aam taur pe layers count karte hain: "50-layer network" = depth 50.

**Slide 15 ka note: "shallow architecture parallel me compute kar sakta hai, sequential nahi."** Book ka view: har layer ko aise socho jaise computer ne kuch instructions **ek saath (parallel)** chala diye. Shallow model (ek layer) sab kuch ek hi parallel step me karta hai, kisi result ko agle step me use nahi kar sakta. Deep model zyada instructions **ek ke baad ek (sequence)** chala sakta hai, aur baad wale steps pehle wale results use kar sakte hain (corners edges ko use karte hain, parts corners ko). Isse power bahut badh jaati hai.

Kitchen example: shallow = bahut saare cooks ek saath alag-alag kaam, koi kisi ka result use nahi karta. Deep = assembly line: ek kaatta hai, agla kaati hui cheez fry karta hai, agla plate me lagata hai.

**Ye kyun important hai:** PyTorch, TensorFlow jaise tools har model ko computational graph ki tarah store karte hain. Fir chain rule se arrows ke ulte direction me chal ke har weight ka gradient automatically nikaal lete hain: isi ko **back-propagation** kehte hain. Humare example me ∂ŷ/∂w₁ = σ(z)(1 − σ(z))·x₁ = 0.2689 × 0.7311 × 1 = 0.1966. Isi se deep network ki har layer train hoti hai.
