# Topic 3: Terminology — Input Layer, Hidden Layer, Output Layer, and Layer 1 / Layer 2 Weights

Source: Lecture 6, slides 20–26 (Terminology — the network "contains 3 layers"; input layer; hidden layer; output layer; h₁…h₄; layer 1 weights; layer 2 weights), with the instructor's handwritten labels.

---

## 1) Technical Explanation

Applied to the network of [[02_Network_of_Perceptrons_MLP_Introduction]]:

- *This network contains **3 layers**.*
- **Input layer** — the layer containing the inputs (x₁, x₂).
- **Hidden layer** — the *middle layer containing the 4 perceptrons*. It is "hidden" because its outputs are neither the network's inputs nor its final output; they are internal.
- **Output layer** — the final layer containing **one output neuron** (it produces y).
- **h₁, h₂, h₃, h₄** — the outputs of the four hidden perceptrons.
- **Layer 1 weights** — *the red and blue edges* (from the inputs to the hidden layer), each ±1.
- **Layer 2 weights** — **w₁, w₂, w₃, w₄**, connecting the hidden layer to the output neuron (handwritten "layer 2 weight" next to the top edges and "layer 1 weights" next to the bottom ones).

The handwritten bias shown on the figure: **bias = −2** for the hidden units.

**Flag — layer-counting conventions.** This deck counts the **input layer** as one of the 3 layers (input, hidden, output). Many texts instead count only layers with computation and call the same network a **2-layer network** (one hidden layer + output). Lecture 9 uses a numbering from 0 to L ([[01_Feedforward_Network_Architecture_Layers_and_Notation]]) — check which convention is meant whenever someone says "n-layer network".

**Information flow.** x → (layer 1 weights) → h → (layer 2 weights) → y. Each arrow goes only forward — this *feedforward* structure is formalised in Lecture 9. Its multi-layer version is also what the Lecture 2 slides called a "multilayer perceptron" ([[05_Simple_to_Complex_Features_and_Conventional_ML_vs_Deep_Learning]]).

---

## 2) Simple English Explanation

Names for the parts of our little neuron team:

- **Input layer:** the row where the information enters (x₁, x₂).
- **Hidden layer:** the middle row of four neurons. "Hidden" simply means you don't see it from outside — it is neither the input nor the answer.
- **Output layer:** the last neuron, which gives the answer y.
- **h₁–h₄:** what the four hidden neurons say.
- **Layer 1 weights:** the first set of connections (the coloured red/blue lines) from inputs to hidden neurons.
- **Layer 2 weights (w₁–w₄):** the second set, from hidden neurons to the output neuron.

The slide counts this as a **3-layer network** (input + hidden + output). Some books call the very same thing a 2-layer network — so always check which way of counting is used.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Hamari chhoti neuron team ke hisson ke naam:

- **Input layer:** wo row jahan information andar aati hai (x₁, x₂).
- **Hidden layer:** beech ki chaar neurons ki row. "Hidden" ka matlab bas itna hai ki bahar se dikhti nahi — ye na input hai na answer.
- **Output layer:** aakhri neuron, jo answer y deta hai.
- **h₁–h₄:** chaaron hidden neurons kya bol rahe hain.
- **Layer 1 weights:** pehla set connections ka (laal/neeli lines) inputs se hidden neurons tak.
- **Layer 2 weights (w₁–w₄):** doosra set, hidden neurons se output neuron tak.

Slide ise **3-layer network** gintii hai (input + hidden + output). Kuch books isi ko 2-layer network kehti hain — isliye hamesha check karo ki gintii kaise ki ja rahi hai.
