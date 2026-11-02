# Topic 2: The Pre-Activation and Activation Equations

Source: Lecture 9 (ES532: Introduction to Deep Learning), slides 11–12 (numbered 12 and 14 in the printed slide corner).

---

## 1) Technical Explanation

Building on the layer notation from [[01_Feedforward_Network_Architecture_Layers_and_Notation]], this topic gives the actual **formulas** used to compute one layer's values from the previous layer's values.

**Pre-activation at layer $i$:**

$$a_i(x) = b_i + W_i \, h_{i-1}(x)$$

In words: take the *activation output* of the previous layer, $h_{i-1}(x)$ (a vector), multiply it by this layer's weight matrix $W_i$, and add this layer's bias vector $b_i$. The result, $a_i(x)$, is the pre-activation vector for layer $i$.

The slide illustrates this concretely with a worked matrix example (for a layer with 3 neurons receiving input from a previous layer):

$$a = \begin{bmatrix} a_{11} \\ a_{12} \\ a_{13} \end{bmatrix} = \begin{bmatrix} b_{11} \\ b_{12} \\ b_{13} \end{bmatrix} + \begin{bmatrix} W_{12} & W_{13} & \cdots \\ W_{21} & \cdots & \\ W_{31} & \cdots & W_{33} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$

This is exactly an ordinary matrix-vector multiplication plus a vector addition — each row of the weight matrix, dotted with the previous layer's activation vector, produces one entry of the pre-activation vector, and the corresponding bias entry is added on top. This is precisely why $W_i$ needs to be a full matrix (not a single number) whenever a layer has more than one neuron: each output neuron in layer $i$ needs its own row of weights, one weight per input neuron from layer $i-1$.

**Activation at layer $i$:**

$$h_i(x) = g\big(a_i(x)\big)$$

where $g$ is the **activation function** — applied **element-wise** to every entry of the pre-activation vector $a_i(x)$ — and can be any of the functions from [[00_Recap_Activation_Functions_Table]] (logistic/sigmoid, tanh, linear, ReLU, etc.), chosen as a design decision for the network. The slide spells this out concretely too: applying $g$ to each entry of the pre-activation vector individually produces the corresponding entry of the activation vector:

$$\begin{bmatrix} a_{11} \\ a_{12} \\ a_{13} \end{bmatrix} \xrightarrow{g} \begin{bmatrix} g(a_{11}) \\ g(a_{12}) \\ g(a_{13}) \end{bmatrix}$$

**Putting the two together**: to compute layer $i$'s output from layer $i-1$'s output, first compute the pre-activation ($a_i = b_i + W_i h_{i-1}$), then apply the activation function element-wise ($h_i = g(a_i)$). Repeating this layer by layer, starting from the input ($h_0 = x$) and moving forward through every hidden layer, is exactly what "feedforward" means: information flows strictly forward, one layer feeding the next, with no loops or backward connections within a single pass.

---

## 2) Simple English Explanation

This topic gives the actual step-by-step recipe for computing what happens at one layer of the network, given the previous layer's output.

**Step 1 — the "raw score" (pre-activation):** take everything the previous layer handed you (a bunch of numbers, one per neuron there), multiply each of those numbers by its own weight, add them all up, and then add one more small number (the bias) on top. Do this separately for every neuron in the current layer. The result is a batch of raw, unprocessed numbers — one per neuron in this layer — before anything "smart" happens to them.

**Step 2 — the "smoothing" (activation):** take each of those raw numbers from Step 1 and run it through an activation function — sigmoid, ReLU, or whichever one was chosen for this layer (see the earlier topics on why these functions matter). This turns the raw numbers into the layer's actual output values, which then get handed forward to the *next* layer as its input.

So really, every layer does the exact same two-step dance: (1) weighted sum + bias → raw number, (2) squash that raw number through an activation function → final output for this layer. Then that output becomes the next layer's input, and the whole process repeats, layer after layer, moving strictly forward from the input all the way to the output — which is exactly why it's called a "feedforward" network: the information only ever flows forward, never backward, in a single pass through the network.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic actual step-by-step recipe deta hai ye compute karne ke liye ki ek layer mein kya hota hai, pichli layer ke output ko dekhte hue.

**Step 1 — "raw score" (pre-activation):** pichli layer ne tumhe jo kuch bhi diya hai (kayi numbers, ek har neuron ke liye wahan), un har number ko uske apne weight se multiply karo, sabko add kar do, aur phir ek aur chhota number (bias) upar add kar do. Ye alag se karo har neuron ke liye current layer mein. Result ek batch of raw, unprocessed numbers hai — ek har neuron ke liye is layer mein — inke saath koi "smart" cheez hone se pehle.

**Step 2 — "smoothing" (activation):** Step 1 ke har raw number ko lo aur use ek activation function se guzaro — sigmoid, ReLU, ya jo bhi is layer ke liye choose kiya gaya tha (pehle wale topics dekho ye samajhne ke liye ki ye functions kyun matter karte hai). Ye raw numbers ko is layer ke actual output values mein badal deta hai, jo phir *agli* layer ko uske input ki tarah aage pass kar diye jaate hai.

To actually, har layer bilkul same do-step dance karti hai: (1) weighted sum + bias → raw number, (2) us raw number ko ek activation function se squash karo → is layer ka final output. Phir wo output agli layer ka input ban jaata hai, aur poora process repeat hota hai, layer ke baad layer, seedha input se lekar output tak forward move karte hue — isi wajah se ise "feedforward" network kehte hai: information sirf hamesha forward flow karti hai, kabhi backward nahi, network se ek single pass mein.
