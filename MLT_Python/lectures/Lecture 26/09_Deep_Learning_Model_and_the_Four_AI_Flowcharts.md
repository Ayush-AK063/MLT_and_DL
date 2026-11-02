# Topic 9: The Deep Learning Model (MLP) and the Four AI Flowcharts

Source: Lecture 26, slides 20–23 ("Deep Learning Model": feed-forward deep network or multilayer perceptron, mathematical functions mapping input to output, composed of simpler functions, each layer provides a new representation, learning the right representation; "Representation learning" ×3: build-up of flowcharts for Rule-based system, Classic machine learning and Deep Learning, recreated from the *Deep Learning* book, Fig. 1.5). Enriched with web research (Goodfellow et al., *Deep Learning*, 2016, ch. 1 and ch. 6). The XOR network is our own illustration and was checked for all four inputs.

---

## 1) Technical Explanation

### Slide 20: the deep learning model

- **"Feed-forward deep network or multilayer perceptron (MLP)."** The standard example of a deep-learning model. Information flows one way, from input to output, through several layers. There are no loops ("feed-forward").
- **"Mathematical function that maps input to output."** An MLP is just a function y = f(x; θ), where θ is the set of all weights and biases.
- **"Composed of simpler functions."** f(x) = f⁽ᴸ⁾(… f⁽²⁾(f⁽¹⁾(x))). Each layer is h⁽ˡ⁾ = g(W⁽ˡ⁾ h⁽ˡ⁻¹⁾ + b⁽ˡ⁾): a weighted sum (like a perceptron, [[05_Perceptron_General_Architecture]] from Lecture 4) followed by a non-linear activation g (step, sigmoid, ReLU…).
- **"Each layer provides a new representation."** h⁽¹⁾ is a new description of x, h⁽²⁾ a new description of h⁽¹⁾, and so on ([[05_Deep_Learning_Building_Complex_Concepts_from_Simple_Ones]]).
- **"Learning the right representation."** All the W and b are learned together from labelled data, by gradient descent with back-propagation ([[06_Computational_Graphs_and_the_Depth_of_a_Model]]). The hidden representations are whatever turns out to make the final prediction accurate.

### Worked example (ours): an MLP solves XOR where one perceptron cannot

XOR outputs 1 when exactly one input is 1. A single perceptron cannot compute it, because the four points are **not linearly separable** ([[06_Linear_Separability_Concept]] from Lecture 4). Lecture 5 built OR and AND with single perceptrons ([[01_Perceptron_Logic_Gates_OR_and_AND]] from Lecture 5). Stack them:

- Hidden unit h₁ = step(x₁ + x₂ − 0.5) → this is **OR**
- Hidden unit h₂ = step(x₁ + x₂ − 1.5) → this is **AND**
- Output y = step(h₁ − h₂ − 0.5) → "OR but not AND" = **XOR**

(step(z) = 1 if z > 0, else 0.)

| x₁ | x₂ | h₁ (OR) | h₂ (AND) | h₁ − h₂ − 0.5 | y | XOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | −0.5 | 0 | 0 ✔ |
| 0 | 1 | 1 | 0 | +0.5 | 1 | 1 ✔ |
| 1 | 0 | 1 | 0 | +0.5 | 1 | 1 ✔ |
| 1 | 1 | 1 | 1 | −0.5 | 0 | 0 ✔ |

**Why this is representation learning in miniature.** In the original (x₁, x₂) space, XOR is not linearly separable. In the hidden representation (h₁, h₂), the four inputs become (0,0) → 0, (1,0) → 1, (1,0) → 1, (1,1) → 0. Now one straight line, h₁ − h₂ = 0.5, separates them. The hidden layer **changed the representation** so that the last layer's simple linear rule works: the same lesson as Cartesian → polar in [[02_Choice_of_Representation_Cartesian_vs_Polar_Coordinates]]. Here we chose the weights by hand. In a real MLP, training would find weights like these automatically.

### Slides 21–23: four kinds of AI system as flowcharts

The three slides build up the book's Fig. 1.5 one row at a time. In the book's version, **shaded boxes are components that learn from data**.

| System | Flowchart | What is learned from data |
|---|---|---|
| **Rule-based system** | Input → Hand-designed program → Output | nothing |
| **Classic machine learning** | Input → Hand-designed **features** → Mapping from features → Output | only the mapping (the classifier) |
| **Representation learning** | Input → Features → Mapping from features → Output | features **and** mapping |
| **Deep learning** | Input → Simple features → Additional layers of more abstract features → Mapping from features → Output | all feature levels **and** the mapping |

Read it as a progression. Each step down the table hands one more piece of the job from humans to data:

- **Rule-based** (e.g., Cyc, expert systems, [[07_Machine_Learning_and_AI_Venn_Diagram_and_the_Cyc_Project]]): humans write the whole program.
- **Classic ML** (e.g., HOG + SVM, [[08_Conventional_Machine_Learning_Pipeline_SIFT_and_HOG]]; or Iris measurements + KNN): humans design the features, the model learns the mapping.
- **Representation learning** (e.g., shallow autoencoder, PCA features + classifier): features are learned too, in one step.
- **Deep learning** (e.g., MLP, CNN): features are learned as a hierarchy, simple → abstract, and the mapping on top.

### Differences between the slide and the book's figure (flag)

The slide's redrawing differs from the book's Fig. 1.5 in three small ways:

1. In the **Classic machine learning** row, the second box says "Hand designed **program**". The book says "Hand-designed **features**". The intended meaning is features: in classic ML the human designs the features, not the whole program. Otherwise this row would not differ from the rule-based row except for the extra box.
2. The book has **four** labelled columns. The slide draws the last two rows inside one box labelled "**Deep Learning**", and uses "Representation learning" as the slide title. In the book, the row Input → Features → Mapping → Output is labelled **representation learning** (not necessarily deep), and only the row with the extra "abstract features" layer is **deep learning**.
3. On the slide the "**Abstract feature**" box is not shaded. In the book, "Additional layers of more abstract features" **is** shaded, because those layers are learned from data. That is the whole point of deep learning.

For exams, use the book's version as shown in the table above.

---

## 2) Simple English Explanation

**Slide 20: what a deep learning model looks like.**

- The standard example is the **multilayer perceptron (MLP)**, also called a feed-forward deep network. "Feed-forward" means information only goes one way: from the input, through several layers, to the output.
- It is just a big **mathematical function**: numbers in, answer out.
- That big function is built by **chaining small simple functions**. Each layer takes the numbers from the previous layer, does a weighted sum (like the perceptron from Lecture 4), and then a small "squash" or "switch" step.
- **Each layer gives a new description** of the input.
- All the weights are **learned from examples**, so the network finds the right descriptions by itself.

**A tiny example: XOR.** XOR means "exactly one of the two inputs is 1". One perceptron can't do it: if you plot the four cases, you can't separate the 1s from the 0s with a straight line (Lecture 4). But in Lecture 5 we built OR and AND from single perceptrons. Put them in a hidden layer:

- h₁ = OR(x₁, x₂): 1 if at least one input is 1.
- h₂ = AND(x₁, x₂): 1 only if both are 1.
- Output = "h₁ is on but h₂ is off" = XOR.

Check all four cases:
- (0, 0): OR = 0, AND = 0 → output 0. Correct.
- (0, 1): OR = 1, AND = 0 → output 1. Correct.
- (1, 0): OR = 1, AND = 0 → output 1. Correct.
- (1, 1): OR = 1, AND = 1 → output 0. Correct.

The hidden layer gave a **new description** (OR, AND) of the input. In that new description a simple straight-line rule works. That is exactly what deep learning does, just with many more layers and with the weights found automatically instead of by hand.

**Slides 21–23: four kinds of AI system, from "humans do everything" to "data does everything":**

1. **Rule-based system:** input → a program a human wrote → output. Nothing is learned. (Like Cyc.)
2. **Classic machine learning:** input → features a human designed → a learned mapping → output. Only the last part is learned. (Like HOG + SVM, or flower measurements + KNN.)
3. **Representation learning:** input → features **learned** from data → learned mapping → output.
4. **Deep learning:** input → simple learned features → more abstract learned features (more layers) → learned mapping → output.

In the book's picture, shaded boxes are the parts learned from data. With each step down, more boxes are shaded.

**Small mistakes in the slide's drawing:** compared with the book, (1) the classic ML row should say "hand-designed *features*", not "hand-designed program"; (2) the book keeps "representation learning" and "deep learning" as separate rows, while the slide puts both under "Deep Learning"; and (3) the "Abstract feature" box should be shaded, because it is learned. Use the book's version in exams.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 20: Deep Learning Model.**

- **"Feed-forward deep network ya multilayer perceptron (MLP)":** deep learning ka standard example. Information sirf ek direction me jaati hai: input → kai layers → output. Koi loop nahi.
- **"Mathematical function that map input to output":** MLP bas ek function hai y = f(x; θ), θ = saare weights aur biases.
- **"Composed of simpler functions":** f(x) = f⁽ᴸ⁾(…f⁽²⁾(f⁽¹⁾(x))). Har layer: h = g(W·h_pichhla + b), yaani weighted sum (Lecture 4 ka perceptron jaisa) + ek non-linear activation g (step, sigmoid, ReLU).
- **"Each layer provides a new representation":** har layer input ka naya description deti hai.
- **"Learning right representation":** saare W aur b data se ek saath seekhe jaate hain (gradient descent + back-propagation, Topic 6).

**Humara example: XOR (jo ek perceptron nahi kar sakta).** XOR = 1 jab exactly ek input 1 ho. Chaar points ko ek seedhi line se alag nahi kar sakte (Lecture 4, linear separability). Lecture 5 me OR aur AND single perceptron se banaye the. Unko hidden layer me rakho:

- h₁ = step(x₁ + x₂ − 0.5) → **OR**
- h₂ = step(x₁ + x₂ − 1.5) → **AND**
- y = step(h₁ − h₂ − 0.5) → "OR hai par AND nahi" = **XOR**

(step(z) = 1 agar z > 0, warna 0)

Chaaron cases check:
- (0,0): h₁=0, h₂=0, 0−0−0.5 = −0.5 → y = 0 ✔
- (0,1): h₁=1, h₂=0, 1−0−0.5 = +0.5 → y = 1 ✔
- (1,0): h₁=1, h₂=0 → +0.5 → y = 1 ✔
- (1,1): h₁=1, h₂=1, 1−1−0.5 = −0.5 → y = 0 ✔

**Ye representation learning ka chhota version hai:** (x₁, x₂) space me XOR line se alag nahi hota. Hidden layer ke naye representation (h₁, h₂) me points ban gaye (0,0)→0, (1,0)→1, (1,1)→0, aur ab ek line h₁ − h₂ = 0.5 se alag ho jaate hain. Bilkul Topic 2 ke Cartesian → polar jaisa. Yahan weights humne haath se chune, asli MLP me training khud aise weights dhoondh leti hai.

**Slides 21–23: Chaar tarah ke AI systems (Deep Learning book, Fig 1.5).** Book me **shaded boxes = jo data se seekhe jaate hain**.

1. **Rule-based system:** Input → Hand-designed program → Output. Kuch nahi seekha jaata (jaise Cyc).
2. **Classic machine learning:** Input → Hand-designed **features** → Mapping from features → Output. Sirf mapping (classifier) seekhi jaati hai (jaise HOG + SVM, ya Iris measurements + KNN).
3. **Representation learning:** Input → Features → Mapping → Output. Features bhi seekhe jaate hain (jaise shallow autoencoder).
4. **Deep learning:** Input → Simple features → Aur abstract features ki extra layers → Mapping → Output. Saare feature levels + mapping seekhe jaate hain (jaise MLP, CNN).

Har step pe kaam ka ek aur hissa insaan se data ke paas chala jaata hai.

**Slide ki drawing me book se teen chhote fark (flag):**
1. Classic ML row me slide pe "Hand designed **program**" likha hai, book me "Hand-designed **features**". Sahi meaning features hai: classic ML me insaan features banata hai, poora program nahi.
2. Book me chaar alag columns hain. Slide ne last do rows ek box me daal ke "Deep Learning" label diya. Book me Input → Features → Mapping → Output wali row **representation learning** hai, aur sirf extra "abstract features" wali row **deep learning** hai.
3. Slide pe "Abstract feature" box shaded nahi hai, book me shaded hai, kyunki wo layers data se seekhi jaati hain. Deep learning ka main point hi yahi hai.

Exam me book wala version (upar ki list) likhna.
