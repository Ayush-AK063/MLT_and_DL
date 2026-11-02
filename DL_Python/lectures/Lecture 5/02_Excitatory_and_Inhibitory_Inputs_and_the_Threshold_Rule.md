# Topic 2: Excitatory and Inhibitory Inputs, and the Threshold Rule

Source: Lecture 5, slides 4–9 (inputs can be excitatory or inhibitory; g(x) = Σxᵢ; y = f(g(x)) = 1 if g(x) ≥ θ; θ the thresholding parameter; the weighted network figure with "θ > nw − p").

---

## 1) Technical Explanation

**Two kinds of input (slide 4).** *The inputs can be excitatory or inhibitory.* An **excitatory** input pushes the neuron toward firing; an **inhibitory** input suppresses it. The instructor's examples: *positive side* for excitatory inputs, and **"high temperature"** as an inhibitory input in the "play outside" example (if it is too hot, you do not go out regardless of other conditions).

**The inhibition rule (slide 5).** *y = 0 if any xᵢ is inhibitory (i.e. active), else…* — an inhibitory input that is **on** forces the output to **0** unconditionally (an *absolute veto*); the handwritten note says the same: **"Inhibitory o/p is always zero"**.

**Aggregation (slides 5–6).**

g(x₁, x₂, …, xₙ) = g(x) = Σᵢ₌₁ⁿ xᵢ

(the number of excitatory inputs that are on).

**Decision (slides 7–8).**

y = f(g(x)) = 1 if g(x) ≥ θ
  = 0 if g(x) < θ

**θ is called the thresholding parameter** (slide 8). The handwritten annotation on slide 7 labels "Threshold" on θ.

**Weighted picture (slide 9, counter 138).** A network with excitatory inputs x₁…xₙ, each with the same weight **w**, and inhibitory inputs xₙ₊₁…xₙ₊ₘ, each with weight **−p**, all into a unit Y with output y. The slide's handwritten **threshold condition** reads **θ > nw − p**. *Interpretation (the slide does not spell it out):* if **all n** excitatory inputs are on (sum = nw) and **one** inhibitory input is also on (−p), the total nw − p must still fall **below θ** so the neuron stays silent — i.e. a single inhibitory input has enough strength to veto everything else. That is exactly the "absolute inhibition" rule above, expressed with weights.

**Summary of the MP unit.**

| Property | MP neuron |
|---|---|
| Inputs | binary {0,1}, excitatory or inhibitory |
| Aggregation | g(x) = Σ xᵢ (excitatory) |
| Output | y = 1 iff no inhibitory input is on **and** g(x) ≥ θ |
| Parameters | only θ (set by hand, not learned) |

Compare [[03_The_Perceptron_Function]] in Lecture 3: the perceptron uses a weighted sum and a bias; the MP neuron is the special case of equal weights with a separate inhibition veto.

---

## 2) Simple English Explanation

Inputs come in two flavours:

- **Excitatory** = "go ahead" signals (they add 1 to the count).
- **Inhibitory** = "stop" signals. If even **one** is on, the neuron says **0** no matter what else is happening. (Example: if the **temperature is too high**, you don't play outside even if it isn't raining.)

If no stop-signal is on, the neuron counts the "go ahead" signals (**g**) and compares the count with a number called the **threshold θ**:

- count **≥ θ** → output **1**,
- count **< θ** → output **0**.

The picture with weights **w** (go signals) and **−p** (stop signals) says the same thing with numbers: the stop signal is so strong that **θ > nw − p**, meaning even if all n go-signals are on, one stop-signal keeps the total under the threshold.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Inputs do tarah ke hote hain:

- **Excitatory** = "aage badho" signals (ye count mein 1 jodte hain).
- **Inhibitory** = "ruko" signals. Agar ek bhi on ho to neuron **0** bolta hai chahe baaki kuch bhi ho. (Example: agar **temperature bahut zyada** hai to aap bahar nahi khelte, chahe baarish na ho.)

Agar koi ruko-signal on nahi hai, to neuron "aage badho" signals ko gintaa hai (**g**) aur count ko ek number **threshold θ** se compare karta hai:

- count **≥ θ** → output **1**,
- count **< θ** → output **0**.

Weights wali picture (**w** go-signals ke liye aur **−p** stop-signals ke liye) wahi baat numbers se kehti hai: stop signal itna strong hai ki **θ > nw − p**, yaani saare n go-signals on hon tab bhi ek stop-signal total ko threshold se neeche rakhta hai.
