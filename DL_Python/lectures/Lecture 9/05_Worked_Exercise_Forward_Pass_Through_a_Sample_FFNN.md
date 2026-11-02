# Topic 5: Worked Exercise — Forward Pass Through a Sample Feedforward Network

Source: Lecture 9 (ES532: Introduction to Deep Learning), slide 16 (numbered 20 in the printed slide corner) — posed as an unsolved "Exercise" in the source PDF. The forward-pass computation below was worked out and verified independently, since the slide itself gives no solution.

---

## 1) Technical Explanation

The lecture ends with an **exercise**: a concrete, fully-specified feedforward network with actual numeric weights, ready to compute by hand — a perfect chance to apply every equation from [[01_Feedforward_Network_Architecture_Layers_and_Notation]] through [[03_Output_Layer_and_Full_Network_Function]] to real numbers, instead of just symbols.

**The network, exactly as specified in the slide:**
- Inputs: $x_1 = 0.3$, $x_2 = 0.5$.
- Hidden layer 1: neurons $h_{11}, h_{12}$, with weights $w_1=0.1$ ($x_1 \to h_{11}$), $w_2=0.2$ ($x_1 \to h_{12}$), $w_3=0.3$ ($x_2 \to h_{11}$), $w_4=0.4$ ($x_2 \to h_{12}$), and bias $b_1 = 0.5$ (shared by both neurons in this layer).
- Hidden layer 2: neurons $h_{21}, h_{22}$, with weights $w_5=0.5$ ($h_{11}\to h_{21}$), $w_6=0.6$ ($h_{11}\to h_{22}$), $w_7=0.7$ ($h_{12}\to h_{21}$), $w_8=0.8$ ($h_{12}\to h_{22}$), and bias $b_2 = 0.5$.
- Output layer: neurons $y_1, y_2$, with weights $w_9=0.9$ ($h_{21}\to y_1$), $w_{10}=0.1$ ($h_{21}\to y_2$), $w_{11}=0.2$ ($h_{22}\to y_1$), $w_{12}=0.3$ ($h_{22}\to y_2$) — **no bias given for the output layer** in the diagram (only $b_1$ and $b_2$ are shown), so it's taken as 0.
- Activation function throughout: **sigmoid**, $\sigma(z) = \frac{1}{1+e^{-z}}$, for every layer including the output layer (the slide states "AF = sigmoid" with no separate output activation named, so $O = g = \sigma$ here — a simpler case than the general $g$-vs-$O$ distinction from [[03_Output_Layer_and_Full_Network_Function]]).
- Targets: $y_1 = 0$, $y_2 = 1$ (this is what the network's output *should* end up close to, after training — the exercise itself only asks for the current, untrained forward pass).

**Step 1 — pre-activation and activation at hidden layer 1**, using $a_i = b_i + W_i h_{i-1}$ and $h_i = \sigma(a_i)$ from [[02_PreActivation_and_Activation_Equations]]:

$$a_{11} = w_1 x_1 + w_3 x_2 + b_1 = (0.1)(0.3) + (0.3)(0.5) + 0.5 = 0.03 + 0.15 + 0.5 = 0.68$$
$$a_{12} = w_2 x_1 + w_4 x_2 + b_1 = (0.2)(0.3) + (0.4)(0.5) + 0.5 = 0.06 + 0.20 + 0.5 = 0.76$$
$$h_{11} = \sigma(0.68) \approx 0.6637, \qquad h_{12} = \sigma(0.76) \approx 0.6814$$

**Step 2 — pre-activation and activation at hidden layer 2:**

$$a_{21} = w_5 h_{11} + w_7 h_{12} + b_2 = (0.5)(0.6637) + (0.7)(0.6814) + 0.5 \approx 0.3319 + 0.4770 + 0.5 = 1.3089$$
$$a_{22} = w_6 h_{11} + w_8 h_{12} + b_2 = (0.6)(0.6637) + (0.8)(0.6814) + 0.5 \approx 0.3982 + 0.5451 + 0.5 = 1.4434$$
$$h_{21} = \sigma(1.3089) \approx 0.7873, \qquad h_{22} = \sigma(1.4434) \approx 0.8089$$

**Step 3 — pre-activation and activation at the output layer:**

$$a_{y_1} = w_9 h_{21} + w_{11} h_{22} = (0.9)(0.7873) + (0.2)(0.8089) \approx 0.7086 + 0.1618 = 0.8704$$
$$a_{y_2} = w_{10} h_{21} + w_{12} h_{22} = (0.1)(0.7873) + (0.3)(0.8089) \approx 0.0787 + 0.2427 = 0.3214$$
$$\hat{y}_1 = \sigma(0.8704) \approx 0.7048, \qquad \hat{y}_2 = \sigma(0.3214) \approx 0.5796$$

**Result of the forward pass**: $\hat{y}_1 \approx 0.7048$, $\hat{y}_2 \approx 0.5796$ — compared against the targets $y_1=0$, $y_2=1$.

**Comparing prediction to target, using the squared-error formula from [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]]**: $(\hat{y}_1 - y_1)^2 = (0.7048-0)^2 \approx 0.4968$, and $(\hat{y}_2-y_2)^2 = (0.5796-1)^2 \approx 0.1767$. For this single example ($N=1$), the total error is $\approx 0.4968 + 0.1767 = 0.6735$ — a fairly large error, which makes sense: these weights were just picked arbitrarily for the exercise, not learned, so there's no reason to expect the network to already be close to the target.

**What this exercise is actually building toward**: the slide poses this network and stops — it's an exercise, not a worked solution, precisely because the *next* step (using this error to figure out how to adjust every weight — backpropagation) is the subject of a future lecture not yet in this repo. This file computes and verifies the **forward pass only** (turning the given inputs and weights into a prediction), which is the necessary first half of that process; the second half — computing gradients and updating $w_1$ through $w_{12}$ and $b_1$, $b_2$ to reduce this error — will be added once that lecture arrives.

---

## 2) Simple English Explanation

This lecture ends by handing you a fully-built, tiny neural network — every weight, every bias, every input number specified — and says "now go compute it," without giving the answer. This note works through that computation by hand, step by step, since the slide itself leaves it as homework.

**The setup, in plain terms**: 2 input numbers go in. They get combined (using the given weights, exactly like the recipe from the "pre-activation and activation" topic) into 2 numbers at the first hidden layer. Those 2 numbers get combined again into 2 numbers at a second hidden layer. Those get combined one final time into the 2 output numbers, which are the network's actual prediction. Every single "combine" step uses the sigmoid squashing function you learned about back in Lecture 8.

**Working through it**:
1. First hidden layer: combining the inputs with their weights and the bias gives two raw numbers (0.68 and 0.76), which sigmoid turns into about **0.66** and **0.68**.
2. Second hidden layer: combining *those* numbers with the next set of weights and bias gives two more raw numbers (about 1.31 and 1.44), which sigmoid turns into about **0.79** and **0.81**.
3. Output layer: combining those with the final set of weights (no bias this time — the diagram doesn't show one for the output layer) gives two more raw numbers (about 0.87 and 0.32), and sigmoid turns those into the network's final answer: about **0.70** and **0.58**.

**So the network currently predicts** roughly "70%" for the first output and "58%" for the second — but the *actual* correct answers (the targets given in the exercise) are 0 and 1. That's a pretty big miss on both counts, especially the first one (predicted 0.70, wanted 0). That's completely expected here, though: these weights were just made up for the exercise, not learned from real training — a network only gets good at its job *after* training adjusts its weights to shrink exactly this kind of error.

**Why the exercise stops here**: figuring out *how* to adjust all 12 weights and 2 biases to make the prediction closer to the target is a whole separate, important topic called backpropagation — which is exactly what this course is building toward next, in a lecture not yet added to this repo. This note only covers getting the prediction *out* of the network (the "forward pass") — the fixing-the-weights part comes later.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture tumhe ek poori tarah bana hua, chhota sa neural network dekar khatam hoti hai — har weight, har bias, har input number diya hua hai — aur kehti hai "ab isse compute karo," bina answer diye. Ye note us computation ko step-by-step hand se karke dikhata hai, kyunki slide khud ise homework ki tarah chhod deti hai.

**Setup, simple shabdon mein**: 2 input numbers andar jaate hai. Unhe combine kiya jaata hai (diye gaye weights use karke, bilkul "pre-activation and activation" wale topic ke recipe ki tarah) pehli hidden layer ke 2 numbers banane ke liye. Wo 2 numbers phir se combine hote hai doosri hidden layer ke 2 numbers banane ke liye. Wo ek aakhri baar combine hote hai 2 output numbers banane ke liye, jo network ki actual prediction hai. Har ek "combine" step sigmoid squashing function use karta hai jo tumne Lecture 8 mein seekha tha.

**Isse work through karte hai**:
1. Pehli hidden layer: inputs ko unke weights aur bias ke saath combine karna do raw numbers deta hai (0.68 aur 0.76), jinhe sigmoid lagbhag **0.66** aur **0.68** mein badal deta hai.
2. Doosri hidden layer: *un* numbers ko agle set ke weights aur bias ke saath combine karna do aur raw numbers deta hai (lagbhag 1.31 aur 1.44), jinhe sigmoid lagbhag **0.79** aur **0.81** mein badal deta hai.
3. Output layer: unhe final set ke weights ke saath combine karna (is baar koi bias nahi — diagram output layer ke liye koi nahi dikhata) do aur raw numbers deta hai (lagbhag 0.87 aur 0.32), aur sigmoid unhe network ke final answer mein badal deta hai: lagbhag **0.70** aur **0.58**.

**To abhi network predict karta hai** roughly "70%" pehle output ke liye aur "58%" doosre ke liye — lekin *asli* sahi answers (exercise mein diye gaye targets) 0 aur 1 hai. Ye dono counts mein kaafi bada miss hai, khaaskar pehla (predict 0.70, chahiye tha 0). Ye yahan bilkul expected hai though: ye weights exercise ke liye bas bana diye gaye the, real training se seekhe nahi gaye the — ek network apne kaam mein tab hi achha hota hai jab training uske weights ko adjust karke exactly is tarah ki error ko shrink karti hai.

**Exercise yahan kyun ruk jaati hai**: 12 weights aur 2 biases ko adjust karna, taaki prediction target ke zyada close ho, ye ek poora alag, important topic hai jise backpropagation kehte hai — jo exactly wahi hai jiski taraf ye course aage badh raha hai, ek aisi lecture mein jo abhi is repo mein add nahi hui. Ye note sirf network se prediction *nikalna* (forward pass) cover karta hai — weights fix karne wala part baad mein aayega.
