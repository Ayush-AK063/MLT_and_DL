# Topic 2: A Network of Perceptrons — The 2-Input, 4-Perceptron Construction

Source: Lecture 6, slides 9–19 ("We will now see how to implement any Boolean function using a network of perceptrons…"; the construction built up edge by edge: True = +1, False = −1; 2 inputs and 4 perceptrons; red edge w = −1, blue edge w = +1; bias −2; output perceptron with weights to be learned).

---

## 1) Technical Explanation

**Goal (slide 9).** Show how **any** Boolean function — not just linearly separable ones ([[05_Linear_Separability_of_Boolean_Functions]], Lecture 5) — can be implemented by a **network of perceptrons**. This is the multilayer perceptron (MLP) idea.

**Conventions (slide 10).** *True = +1 and False = −1.* Two inputs x₁, x₂, and **four perceptrons** in a middle row.

**Wiring (slides 11–14).** *Each input is connected to all four perceptrons with specific weights*, drawn as **red edges (w = −1)** and **blue edges (w = +1)**. Reading the slide's figure (confirmed by the handwritten check on slide 24), the four hidden perceptrons h₁ … h₄ have weights:

| Hidden unit | weight from x₁ | weight from x₂ |
|---|---|---|
| h₁ | −1 (red) | −1 (red) |
| h₂ | −1 (red) | +1 (blue) |
| h₃ | +1 (blue) | −1 (red) |
| h₄ | +1 (blue) | +1 (blue) |

**Bias (slide 15).** *The bias (w₀) of each perceptron is −2, i.e. each perceptron will fire only if the weighted sum of its inputs is ≥ 2.*

**Output (slides 16–19).** *Each of these perceptrons is connected to an output perceptron by weights (which need to be learned)* — called w₁ … w₄ — and *the output of this perceptron (y) is the output of the network*.

**Why this works — verified.** For input (x₁, x₂) ∈ {−1, +1}², the weighted sum of hidden unit hᵢ is the dot product of its weight pair with the input. Every pair has entries ±1, so the sum equals **2 when the input equals the "pattern" of that unit** (each of the two products is +1) and is **0 or −2 otherwise**:

| Input (x₁, x₂) | h₁ sum | h₂ sum | h₃ sum | h₄ sum | Fires (sum ≥ 2) |
|---|---|---|---|---|---|
| (−1, −1) | **2** | 0 | 0 | −2 | h₁ only |
| (−1, +1) | 0 | **2** | −2 | 0 | h₂ only |
| (+1, −1) | 0 | −2 | **2** | 0 | h₃ only |
| (+1, +1) | −2 | 0 | 0 | **2** | h₄ only |

So **exactly one hidden perceptron fires for each input, and a different one for each input** — a "one-hot" detector layer. (This is the content of slides 31–35, see [[04_Claim_Any_Boolean_Function_Using_One_Hidden_Layer_of_Perceptrons]].) The output perceptron then only has to pick which of these detectors should mean "output 1".

**Link to earlier lectures.** Each hidden unit is a perceptron of Lecture 3 ([[03_The_Perceptron_Function]]) — weighted sum, bias, threshold. The slide-5 figure of Lecture 5 had a single neuron; here neurons feed neurons. The lecture's networks are "hand-wired", as in Lecture 5, not trained — the output weights are "to be learned", though for Boolean functions they can be written down directly (next topics).

---

## 2) Simple English Explanation

One neuron can only draw one straight line. To do harder logic, use **a team of neurons in two steps**.

**Set-up:** call "true" **+1** and "false" **−1**. Take two inputs and a middle row of **four neurons**. Every input connects to every middle neuron; a **blue** line multiplies the input by **+1**, a **red** line by **−1**. Each middle neuron also has a built-in penalty (bias) of **−2**, so it fires only if its total reaches **2**.

**What each middle neuron does:** think of each as a **detector for exactly one input pair**:

- the first fires only for (−1, −1),
- the second only for (−1, +1),
- the third only for (+1, −1),
- the fourth only for (+1, +1).

*Why?* Each neuron's lines are set to match its pair, so the multiplications give +1 +1 = **2** only for the matching input; any other input gives 0 or −2. So for any input, **exactly one** middle neuron lights up. A final neuron collects their signals through weights w₁…w₄ and produces the answer.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek neuron sirf ek seedhi line kheench sakta hai. Mushkil logic ke liye **neurons ki team do steps mein** use karo.

**Set-up:** "true" ko **+1** aur "false" ko **−1** kaho. Do inputs lo aur beech mein **chaar neurons** ki ek row. Har input har beech wale neuron se juda hai; **neeli** line input ko **+1** se multiply karti hai, **laal** line **−1** se. Har beech wale neuron par ek built-in penalty (bias) **−2** bhi hai, isliye wo tabhi fire karta hai jab uska total **2** tak pahunche.

**Har beech wala neuron kya karta hai:** har ek ko **ek hi input-pair ka detector** samjho:

- pehla sirf (−1, −1) par fire karta hai,
- doosra sirf (−1, +1) par,
- teesra sirf (+1, −1) par,
- chautha sirf (+1, +1) par.

*Kyun?* Har neuron ki lines uske pair se match karne ke liye set hain, to multiplication se +1 +1 = **2** sirf matching input par milta hai; baaki kisi bhi input par 0 ya −2 aata hai. To kisi bhi input ke liye **theek ek** beech wala neuron jalta hai. Aakhri neuron weights w₁…w₄ ke zariye unke signals ikatthe karke answer deta hai.
