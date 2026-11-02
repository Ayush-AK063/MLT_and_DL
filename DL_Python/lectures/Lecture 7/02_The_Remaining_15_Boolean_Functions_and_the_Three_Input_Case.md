# Topic 2: The Remaining 15 Boolean Functions, and Moving to 3 Inputs (8 Hidden Perceptrons)

Source: Lecture 7, slides 10–14 ("It should be clear that the same network can be used to represent the remaining 15 Boolean functions also"; "Each Boolean function will result in a different set of non-contradicting inequalities … Try it!"; "What if we have more than 3 inputs?" — followed by the 8-perceptron figure; "What if we have more than n inputs?").

---

## 1) Technical Explanation

**The other 15 functions (slides 10–11).** With two inputs there are 2^(2²) = **16 Boolean functions**; XOR is one, so the *same* network can represent the **remaining 15**. Each function gives a **different** set of four inequalities (w₁…w₄ each on one side of w₀ according to that function's truth table), and each set is non-contradicting and satisfiable "by appropriately setting w₁, w₂, w₃, w₄". The slide ends with *"Try it!"* — an exercise.

**Verified here:** with the hidden layer of Lecture 6 and the output rule Σ wᵢhᵢ ≥ w₀ (take wᵢ = the target output for the input hᵢ detects and w₀ = 1), **all 16** functions come out exactly right. For example, AND of the ±1 inputs is w = (0,0,0,1); OR is w = (0,1,1,1); NAND is w = (1,1,1,0); XNOR is w = (1,0,0,1).

**Three inputs (slides 12–13).** The question slide reads *"What if we have more than 3 inputs?"*, but the figure that follows shows the **3-input** case itself: inputs x₁, x₂, x₃; **8 hidden perceptrons** with **bias = −3**; and eight second-layer weights w₁…w₈. (Flag: the title says "more than 3" while the content treats exactly 3 — most likely a wording slip for "What if we have 3 inputs?".) The slide text:

- *Again each of the 8 perceptrons will fire only for one of the 8 inputs.*
- *Each of the 8 weights in the second layer is responsible for one of the 8 inputs and can be adjusted to produce the desired output for that input.*

**Why bias = −3 and 8 units.** With three ±1 inputs there are 2³ = 8 input patterns, one hidden unit each, weights ±1 matching the pattern. The weighted sum is **3 only on an exact match** (all three products +1) and ≤ 1 otherwise (it changes by 2 for each mismatched input), so the bias −3 makes the unit fire only on that pattern. (Generalising the bias −2 for 2 inputs: **bias = −n** for n inputs.) Verified here: for n = 3 exactly one of the 8 units fires per input, and all **2⁸ = 256** Boolean functions of three inputs are realised.

**Slide 14** ("What if we have more than n inputs?") is a title-only lead-in to the theorem; "more than n" should again be read as "n inputs" ([[03_Theorem_Any_Boolean_Function_with_2_to_the_n_Hidden_Perceptrons]]).

---

## 2) Simple English Explanation

**Other logic functions:** with two inputs there are **16** possible logic functions (AND, OR, XOR, NAND, …). The very same network can do all 16 — you just choose the final weights differently each time. For each function you write four little rules (one per doorbell: "must be above the bar" or "must be below the bar"); they never contradict each other. The slide says "Try it!" — pick any function and set the weights.

**Three inputs:** now there are 2×2×2 = **8** possible input combinations, so we use **8 doorbell neurons** (and a built-in penalty of −3 so each only rings for its own combination). The final neuron has 8 weights, one per doorbell, which you set to the answer wanted for that combination.

(The slide title says "more than 3 inputs", but the picture is of exactly 3 inputs — a small wording slip.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Baaki logic functions:** do inputs ke saath **16** possible logic functions hote hain (AND, OR, XOR, NAND, …). Wahi network un sab 16 ko kar sakta hai — bas har baar aakhri weights alag chunne hote hain. Har function ke liye aap chaar chhote rules likhte ho (har doorbell ke liye: "bar se upar hona chahiye" ya "neeche"); wo kabhi ek-doosre se nahi takrate. Slide kehti hai "Try it!" — koi bhi function chuno aur weights set karo.

**Teen inputs:** ab 2×2×2 = **8** possible input combinations hain, isliye hum **8 doorbell neurons** use karte hain (aur −3 ki built-in penalty taaki har ek sirf apni combination par bajey). Aakhri neuron ke 8 weights hain, har doorbell ke liye ek, jinhe aap us combination ke liye chahiye wale jawab par set karte ho.

(Slide ka title "more than 3 inputs" kehta hai, par picture bilkul 3 inputs ki hai — chhoti si wording ki galti.)
