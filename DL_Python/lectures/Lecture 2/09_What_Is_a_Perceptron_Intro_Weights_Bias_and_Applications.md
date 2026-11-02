# Topic 9: What Is a Perceptron? — The Pass/Fail Example, Weights and Bias, and Applications

Source: Lecture 2, slides 31–46 (What is a Perceptron?; Perceptron ×8 build-up slides with handwritten annotations; Example 1: Image Recognition ×2; Example 2: Autonomous Vehicles ×2; a final network picture; Thank you). The same perceptron slides are reused in Lecture 3 — see [[01_Recap_Perceptron_Introduction_and_Perceptron_Rule]] there for the continuation.

---

## 1) Technical Explanation

**Slide 31 — "What is a Perceptron?"** A title-only slide that opens the topic.

**The running problem (slides 32–36): *Student Pass/Fail* output.** Inputs: **x₁ = attendance** with weight **w₁**, and **x₂ = homework** with weight **w₂**. The slides build the model one piece at a time:

1. Two inputs x₁, x₂ feed a node **y** through weights w₁, w₂; y feeds the output **z (pass/fail)**.
2. The node computes the **weighted sum**

   y = x₁·w₁ + x₂·w₂

3. A **bias b** is added:

   y = x₁·w₁ + x₂·w₂ + b

4. A **threshold** rule gives the decision:

   y ≥ th → **Pass**; y < th → **Fail**.

**General perceptron (slides 37–38).** Inputs x₁ … x_N (plus a constant input 1 whose weight is the bias w₀) are multiplied by weights w₀ … w_N and combined by a **weighted sum Σ**:

net input = w₀ + x₁·w₁ + x₂·w₂ + … + x_N·w_N

which then passes through an **activation function f** (the decision threshold is set here) to give the output **ŷ**. Slide 38's annotations: the Σ part is the **net-input function**, f is the **activation function**; the **weights can be positive or negative**; and the **error** (ŷ ≠ y — the prediction differs from the true label) is used to **flow back and change the weights** — the learning step, developed in [[01_Recap_Perceptron_Introduction_and_Perceptron_Rule]] and the Perceptron Learning Algorithm of Lecture 4.

**Linear boundary (slide 39).** The scatter plot of **positive objects** (red dots, upper right) and **negative objects** (blue triangles, lower left) is split by a straight **linear boundary**. Handwritten notes: *"Only handle linearly separable data"* and *"struggle with more complex problem"*.

**Weights and bias (slide 40).** *Weights are numerical values assigned to the connections between neurons. Biases are additional parameters that adjust the output of a neuron.*

**Example 1 — Image recognition (slides 41–42).** Detecting cats, dogs or facial features. **Weights** find which pixels are important (e.g. for a cat: ears, whiskers, eyes get more importance). **Biases** keep the network adaptable to changes in image conditions (slight shifts in lighting, position, orientation).

**Example 2 — Autonomous vehicles (slides 43–44).** Networks process camera, radar and lidar data to decide to stop at a red light or avoid obstacles. **Weights** focus the network on pedestrians, road signs, other vehicles, adjusting their significance to the car's current needs. **Biases** let the car adapt to conditions like fog or night.

**Slide 45** shows a drawn multilayer network (inputs on the left narrowing to a single output) — a preview of the multilayer perceptrons of Lecture 6 ([[02_Network_of_Perceptrons_MLP_Introduction]]). Slide 46 is "Thank you".

**Worked check of the pass/fail model (illustrative; the slides give no numbers).** Take w₁ = 0.6, w₂ = 0.4, b = −0.5, th = 0, x₁ = 0.9 (90% attendance), x₂ = 0.5. Then y = 0.9·0.6 + 0.5·0.4 − 0.5 = 0.54 + 0.20 − 0.50 = 0.24 ≥ 0 → **Pass**. With attendance 0.4: y = 0.24 + 0.20 − 0.50 = −0.06 < 0 → **Fail**. These numbers are invented here only to show the arithmetic.

**Note on bias and threshold.** Putting a bias b and a threshold th in the same rule is redundant: y + b ≥ th is the same as y ≥ th − b. Many texts fold the threshold into the bias and compare to 0 — which is exactly the slide-37 form with the extra input "1" and weight w₀.

---

## 2) Simple English Explanation

A **perceptron** is the simplest artificial "brain cell". It takes some numbers in, decides how important each is, adds them up, and makes a yes/no decision.

**Example — will a student pass?** Two clues: how much they **attend** (x₁) and their **homework** (x₂). Each clue has an **importance** (a *weight*): maybe attendance counts more. The perceptron:

1. multiplies each clue by its importance and adds them (y = x₁w₁ + x₂w₂),
2. adds a small fixed nudge, the **bias** (b),
3. says **Pass** if the total reaches a bar (the *threshold*), otherwise **Fail**.

If its answer is wrong, the error is used to **adjust the weights** — that is how it learns.

*A made-up example:* attendance counts 0.6, homework 0.4, bias −0.5, and the bar is 0. A student with 0.9 attendance and 0.5 homework scores 0.54 + 0.20 − 0.50 = 0.24, above the bar → **Pass**. With only 0.4 attendance the score is 0.24 + 0.20 − 0.50 = −0.06, below the bar → **Fail**.

On a graph, a perceptron draws one **straight line** between "yes" and "no" points, so it only works when a straight line can separate them (*linearly separable*). Real tasks like recognising a cat are harder, which is why we later join many perceptrons into networks.

**Why weights and bias?** Weights say *which inputs matter* (in a cat photo, ears and whiskers). The bias lets the neuron still work when conditions shift (lighting, fog, night driving).

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Perceptron** sabse simple artificial "dimaag ka cell" hai. Ye kuch numbers leta hai, decide karta hai ki har number kitna important hai, sabko jodta hai, aur ek haan/naa ka decision leta hai.

**Example — kya student pass hoga?** Do clues: wo kitna **attend** karta hai (x₁) aur uska **homework** (x₂). Har clue ki ek **importance** hai (*weight*): shayad attendance ka weight zyada ho. Perceptron:

1. har clue ko uski importance se multiply karke jodta hai (y = x₁w₁ + x₂w₂),
2. ek chhota fixed nudge, **bias** (b), add karta hai,
3. agar total ek bar (*threshold*) tak pahunche to **Pass** bolta hai, warna **Fail**.

Agar jawab galat ho, to error ka use **weights adjust** karne mein hota hai — yahi seekhne ka tareeka hai.

Graph par perceptron "haan" aur "naa" points ke beech **ek seedhi line** kheenchta hai, isliye wo tabhi kaam karta hai jab seedhi line unhe alag kar sake (*linearly separable*). Cat pehchanne jaise real kaam mushkil hain, isliye baad mein hum bahut saare perceptrons ko jodkar networks banate hain.

**Weights aur bias kyun?** Weights batate hain *kaunse inputs matter karte hain* (cat photo mein kaan aur whiskers). Bias neuron ko tab bhi kaam karne deta hai jab conditions badlein (roshni, kohra, raat mein gaadi chalana).

**Worked check (sirf samjhane ke liye, slides mein numbers nahi hain):** w₁=0.6, w₂=0.4, b=−0.5, th=0, x₁=0.9, x₂=0.5 lo. Tab y = 0.54 + 0.20 − 0.50 = 0.24 ≥ 0 → **Pass**. Attendance 0.4 ho to y = 0.24 + 0.20 − 0.50 = −0.06 < 0 → **Fail**.
