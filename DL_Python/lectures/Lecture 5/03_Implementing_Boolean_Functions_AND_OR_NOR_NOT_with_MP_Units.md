# Topic 3: Implementing Boolean Functions with MP Units — AND, OR, NOR, NOT

Source: Lecture 5, slides 10–19 ("Let us implement some Boolean functions using this McCulloch–Pitts (MP) neuron"; A McCulloch Pitts unit, then AND, OR, NOR, NOT built up one at a time, with the instructor's handwritten truth tables).

---

## 1) Technical Explanation

The recipe is always the same: choose **θ** (and decide which inputs are inhibitory); the unit then computes y = 1 iff no inhibitory input is on and Σ(excitatory xᵢ) ≥ θ ([[02_Excitatory_and_Inhibitory_Inputs_and_the_Threshold_Rule]]).

**A generic MP unit with 3 inputs, θ = ?** (slides 11–12) — the question "what should θ be?" is then answered per function.

**AND (3 inputs, slide 12).** The handwritten 8-row truth table lists (x₁, x₂, x₃) → y, with y = 1 only for **(1,1,1)** (circled). For (1,1,1), g(x) = 3, and f fires iff g(x) ≥ θ, so **θ = 3**. Output is 0 for every other row because g(x) ≤ 2 < 3.

**OR (3 inputs, slide 13).** Handwritten: *θ = 1 — "any of the inputs is 1"*. Fires whenever at least one input is on.

**NOR (2 inputs, slides 15–17).** Handwritten: *"if any inhibitory is 1, then o/p is 0"*; *x₁ = 1 or x₂ = 1 ⇒ y = 0*; **θ = 0**. Both inputs are inhibitory, so with no input on, g(x) = 0 ≥ 0 gives y = 1; if either input is on, the inhibition forces y = 0. That is exactly NOR (1 only when both inputs are 0).

**NOT (1 input, slides 18–19).** Handwritten table: x₁ = 0 → y = 1; x₁ = 1 → y = 0; the single input is inhibitory with **θ = 0**.

**Verification of all gates (done here, all rows).**

| x₁ x₂ x₃ | AND (θ=3) | OR (θ=1) |
|---|---|---|
| 0 0 0 | 0 | 0 |
| 0 0 1 | 0 | 1 |
| 0 1 0 | 0 | 1 |
| 0 1 1 | 0 | 1 |
| 1 0 0 | 0 | 1 |
| 1 0 1 | 0 | 1 |
| 1 1 0 | 0 | 1 |
| 1 1 1 | 1 | 1 |

| x₁ x₂ | NOR (both inhibitory, θ=0) | | x₁ | NOT (inhibitory, θ=0) |
|---|---|---|---|---|
| 0 0 | 1 | | 0 | 1 |
| 0 1 | 0 | | 1 | 0 |
| 1 0 | 0 | | | |
| 1 1 | 0 | | | |

All rows agree with the Boolean definitions. Note the same θ rule gives general "at least k of n" functions: θ = k (e.g. θ = 2 on three inputs is the comedy-show "at least 2 of 3" example of [[01_McCulloch_Pitts_Neuron_Model_Aggregation_g_and_Decision_f]]).

**Why NOR and NOT matter.** NOR (and NAND) are **universal** gates: any Boolean function can be built by *networks* of NOR units. A *single* MP unit, however, can only do the linearly separable ones ([[05_Linear_Separability_of_Boolean_Functions]]); XOR needs a network — Lecture 6 ([[02_Network_of_Perceptrons_MLP_Introduction]]) and Lecture 7.

**Slide-counter note.** The running slide numbers skip some values (e.g. 140, 146, 147); the PDF flows continuously, and the content (AND → OR → NOR → NOT) is complete.

---

## 2) Simple English Explanation

A single MP neuron can act as a logic gate if we choose its **threshold** well.

- **AND** (all inputs must be on): with 3 inputs, set the threshold to **3** — only when all three are on does the count reach 3.
- **OR** (any input on is enough): set the threshold to **1**.
- **NOR** ("none on"): make both inputs **stop-signals** and set the threshold to **0**. Nothing on → fires (1). Any input on → the stop-signal silences it (0).
- **NOT** (flip): one stop-signal input, threshold 0. Input 0 → output 1; input 1 → output 0.

Check the AND table: out of the 8 possible combinations only (1,1,1) gives 1. For OR only (0,0,0) gives 0. For NOR only (0,0) gives 1. For NOT the output is the opposite of the input.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek akela MP neuron logic gate ki tarah kaam kar sakta hai agar hum uska **threshold** sahi chunein.

- **AND** (saare inputs on hone chahiye): 3 inputs ke liye threshold **3** rakho — sirf jab teeno on hon tab count 3 tak pahunchta hai.
- **OR** (koi bhi ek input on kaafi hai): threshold **1** rakho.
- **NOR** ("koi bhi on nahi"): dono inputs ko **ruko-signal** banao aur threshold **0** rakho. Kuch on nahi → fire (1). Koi bhi input on → ruko-signal use chup kara deta hai (0).
- **NOT** (ulta): ek ruko-signal input, threshold 0. Input 0 → output 1; input 1 → output 0.

AND ka table check karo: 8 combinations mein se sirf (1,1,1) 1 deta hai. OR mein sirf (0,0,0) 0 deta hai. NOR mein sirf (0,0) 1 deta hai. NOT mein output input ka ulta hota hai.
