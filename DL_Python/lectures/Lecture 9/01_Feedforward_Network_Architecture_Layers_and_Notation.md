# Topic 1: Feedforward Network Architecture — Layers and Notation

Source: Lecture 9 (ES532: Introduction to Deep Learning), slides 3–9.

---

## 1) Technical Explanation

This topic builds up, piece by piece, the standard notation this course uses for a **feedforward neural network (FFNN)** — a network where information flows in one direction only, from input to output, through a stack of layers.

**The pieces, in the order the slides introduce them:**

1. **Input**: the network's input is an $n$-dimensional vector, $x = (x_1, x_2, \dots, x_n)$.
2. **Hidden layers**: the network contains $L-1$ hidden layers (the slide's own example uses 2 hidden layers), each with $n$ neurons.
3. **Output layer**: one final output layer with $k$ neurons — i.e., $k$ output classes, for a $k$-way classification problem.
4. **Pre-activation vs. activation**: every neuron in every hidden layer and the output layer is conceptually split into **two parts**:
   - **Pre-activation** $a_i$ — the raw weighted-sum-plus-bias value computed at layer $i$, before any activation function is applied.
   - **Activation** $h_i$ — the value *after* the activation function is applied to $a_i$.
   Both $a_i$ and $h_i$ are **vectors** (one entry per neuron in that layer), not single numbers.
5. **Layer numbering**: the input layer is called the **0th layer**, and the output layer is called the **$L$th layer**. So for a network with $L-1$ hidden layers, the layers are numbered $0$ (input) through $L$ (output), with hidden layers occupying $1$ through $L-1$.
6. **Weights and biases between layers**: $W_i \in \mathbb{R}^{n \times n}$ and $b_i \in \mathbb{R}^n$ are the weight matrix and bias vector connecting layer $i-1$ to layer $i$, for $0 < i < L$ (i.e. for all the hidden-to-hidden and input-to-hidden connections). Separately, $W_L \in \mathbb{R}^{k \times n}$ and $b_L \in \mathbb{R}^k$ are the weight matrix and bias vector connecting the **last hidden layer to the output layer** — note the dimensions change here, since the output layer has $k$ neurons rather than $n$.
7. **Final output**: $h_L = \hat{y} = f(x)$ — the activation at the very last layer *is* the network's predicted output $\hat{y}$, and the whole network, end to end, computes some function $f$ of the input $x$.

**Why this matters**: this notation — $x$, $a_i$, $h_i$, $W_i$, $b_i$, and the $0$-to-$L$ layer indexing — is the standard scaffolding this course will keep reusing for every deeper topic on neural networks going forward (the actual layer-by-layer computation in [[02_PreActivation_and_Activation_Equations]], the full network function in [[03_Output_Layer_and_Full_Network_Function]], and eventually backpropagation in a later lecture). Getting comfortable with exactly what each symbol means, and which are vectors vs. matrices vs. scalars, pays off across the rest of the course.

---

## 2) Simple English Explanation

This topic is basically a vocabulary-building exercise: it sets up all the labels and names this course will use to talk about a multi-layer neural network, piece by piece.

Picture a network drawn as columns of circles (neurons), stacked left to right: a column of input neurons, then one or more columns of "hidden" neurons in the middle, then a final column of output neurons.

- **Input**: the leftmost column — just the raw numbers you feed in, $n$ of them.
- **Hidden layers**: the middle columns — the slides' example has 2 of them, each with $n$ neurons. These are called "hidden" because you don't directly see their values from outside the network; they're intermediate computation.
- **Output layer**: the rightmost column, with $k$ neurons — one for each possible class/category the network is trying to predict.
- **Pre-activation vs. activation, inside each neuron**: think of each neuron as doing its job in two steps. Step 1 ("pre-activation"): multiply all the incoming numbers by their weights and add them up, plus a bias — this raw number is called $a$. Step 2 ("activation"): squash that raw number $a$ through an activation function (like sigmoid or ReLU from earlier topics) to get the final value the neuron actually passes forward — called $h$.
- **Layer numbering**: to keep things simple, the input column is called "layer 0," and the columns count up from there, ending with the output column as "layer $L$."
- **Weights and biases connecting layers**: every arrow between one column and the next column has a weight on it (these weights, collectively, are written as a matrix $W$), and every neuron has a small extra "nudge" number called a bias ($b$) added in too.
- **The big picture**: the very last layer's output, $h_L$, *is* the network's final prediction, $\hat{y}$ — and the entire chain of computation from input to that final prediction is what the network's overall function $f(x)$ means.

This is essentially the "cast of characters" for everything that follows — once you know what $x$, $a_i$, $h_i$, $W_i$, and $b_i$ each mean, the equations in the rest of this lecture become much easier to read.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic basically ek vocabulary-building exercise hai: ye sab labels aur naam set up karta hai jo ye course ek multi-layer neural network ke baare mein baat karne ke liye use karega, ek-ek karke.

Socho ek network jo columns of circles (neurons) ki tarah drawn hai, left se right stack hue hai: input neurons ka ek column, phir beech mein ek ya do "hidden" neurons ke columns, phir ek final column output neurons ka.

- **Input**: sabse left wala column — bas wo raw numbers jo tum feed karte ho, $n$ tadaad mein.
- **Hidden layers**: beech ke columns — slides ke example mein 2 hai, har ek mein $n$ neurons. Inhe "hidden" isliye kehte hai kyunki tum network se bahar se inki values seedha nahi dekh sakte; ye intermediate computation hai.
- **Output layer**: sabse right wala column, $k$ neurons ke saath — har possible class/category ke liye ek jo network predict karne ki koshish kar raha hai.
- **Pre-activation vs. activation, har neuron ke andar**: socho har neuron apna kaam do steps mein karta hai. Step 1 ("pre-activation"): saare incoming numbers ko unke weights se multiply karo aur add kar do, plus ek bias — ye raw number $a$ kehlata hai. Step 2 ("activation"): us raw number $a$ ko ek activation function (jaise sigmoid ya ReLU pichle topics se) se squash karo taaki final value mile jo neuron actually aage pass karta hai — ise $h$ kehte hai.
- **Layer numbering**: cheezein simple rakhne ke liye, input column ko "layer 0" kehte hai, aur columns wahan se count up hote hai, output column "layer $L$" ke saath end hote hai.
- **Layers ko connect karne wale weights aur biases**: ek column se dusre column tak har arrow par ek weight hai (ye weights, collectively, ek matrix $W$ ki tarah likhe jaate hai), aur har neuron mein ek chhota extra "nudge" number bhi add hota hai jise bias ($b$) kehte hai.
- **Bada picture**: sabse last layer ka output, $h_L$, hi network ki final prediction hai, $\hat{y}$ — aur input se us final prediction tak ki poori computation chain hi network ke overall function $f(x)$ ka matlab hai.

Ye essentially aage jo aayega uska "cast of characters" hai — ek baar tumhe pata chal jaaye $x$, $a_i$, $h_i$, $W_i$, aur $b_i$ ka kya matlab hai, is lecture ke baaki equations padhna bahut aasan ho jaata hai.
