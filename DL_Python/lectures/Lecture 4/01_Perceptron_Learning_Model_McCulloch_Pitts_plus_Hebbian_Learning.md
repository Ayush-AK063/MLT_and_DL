# Topic 1: The Perceptron Learning Model — McCulloch–Pitts Neuron plus Hebbian Weight Adjustment

Source: Lecture 4, slides 4–7 (Perceptron; Perceptron Learning ×2 — the second adds the Y formula; annotated Perceptron diagram).

---

## 1) Technical Explanation

**Slide 4 — headline facts.**

- *The first learning machine: the Perceptron — built at Cornell, 1960* (see [[02_History_of_the_Perceptron_and_the_Biological_Neuron]] in Lecture 3 for the date discussion).
- *The perceptron is a **linear classifier used for supervised learning*** — supervised because each training example comes with the correct label.
- *The Perceptron Learning model is a combination of two concepts:* the **McCulloch–Pitts model of an artificial neuron** (a binary-threshold unit; developed in Lecture 5) and the **Hebbian learning rule of adjusting weights**.

Background on the second ingredient: Hebb's idea (1949) is often summarised as "neurons that fire together wire together" — a connection strengthens when the two neurons it joins are active together. The perceptron rule is an *error-driven* variant: weights change in proportion to the **input** and to the **error**, rather than to co-activation alone (see the update Δwᵢ = α·e·xᵢ in [[02_Perceptron_Learning_Algorithm_Steps_and_Update_Rule]]). The slide only names the two concepts.

**Slides 5–6 — the model has 4 parts:**

1. **Inputs from other neurons** (x₁ … xₙ)
2. **Weights and bias** (w₁ … wₙ, plus the threshold θ)
3. **Net sum** — the summation function Σ xᵢwᵢ
4. **Activation function**, here a **threshold**:

   Y = 1 if f(x) ≥ θ, and Y = 0 if f(x) < θ,

   where f(x) = Σ xᵢwᵢ is the net sum (slide 6 adds this formula).

The accompanying block diagram: inputs xᵢ with weights wᵢ enter the *summation function*; its *net-sum* output goes to a *threshold θ* unit (the *activation function*) producing output y; an **Error** box compares y with the target and feeds back to adjust the weights/bias.

**Slide 7 — the annotated figure** repeats Lecture 3's hand-drawn diagram: inputs x₁…x_N with weights w₀…w_N (w₀ being the bias on the constant input 1), net input function w₀ + x₁w₁ + … + x_N w_N, activation function (set the threshold), output y, and the error (ŷ ≠ y) loop. See [[01_Recap_Perceptron_Introduction_and_Perceptron_Rule]] in Lecture 3.

**Two threshold conventions — keep them straight.** Lecture 3 writes f(x) = 1 if w·x + b > 0; this lecture writes Y = 1 if Σxᵢwᵢ ≥ θ. They are the same decision with **b = −θ** (and ≥ vs > differing only at an exact tie).

---

## 2) Simple English Explanation

The perceptron learns by *being corrected*, which is what "supervised learning" means: we show examples **with the right answers**, and it adjusts itself when it gets one wrong.

It is built from two old ideas:

1. A simple **artificial neuron** (the McCulloch–Pitts model): add up weighted inputs and fire (1) if the total reaches a threshold, otherwise stay quiet (0).
2. A **learning rule inspired by Hebb**: connections get adjusted based on activity — here, based on the input and on how wrong the output was.

Four parts: **inputs → weights and bias → add them up (net sum) → activation (fire or not)**. If the output is wrong, the **Error** box sends a correction back to the weights.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Perceptron *sudhaare jaane* se seekhta hai, yahi "supervised learning" ka matlab hai: hum examples **sahi jawabon ke saath** dikhate hain, aur jab wo galat hota hai to khud ko adjust karta hai.

Ye do purane ideas se bana hai:

1. Ek simple **artificial neuron** (McCulloch–Pitts model): weighted inputs ko jodo aur agar total threshold tak pahunche to fire (1) karo, warna chup (0).
2. **Hebb se prerit learning rule**: connections ko activity ke hisaab se adjust karo — yahan input aur output kitna galat tha, uske hisaab se.

Chaar hisse: **inputs → weights aur bias → sabko jodo (net sum) → activation (fire karna ya nahi)**. Agar output galat ho, to **Error** box weights ko correction wapas bhejta hai.
