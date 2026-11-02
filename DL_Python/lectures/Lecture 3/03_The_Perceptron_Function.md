# Topic 3: The Perceptron Function f(x)

Source: Lecture 3, slides 20–21 (Perceptron function ×2).

---

## 1) Technical Explanation

*"Perceptron is a function that maps its input x, which is multiplied with the learned weight coefficient; an output value f(x) is generated."* The slide's equation:

f(x) = 1 if w · x + b > 0, and 0 otherwise.

Symbols (slide 20):

- **w** — vector of real-valued weights,
- **b** — bias, "an element that adjusts the boundary away from origin without any dependence on the input value",
- **x** — vector of input values.

**Slide 21:** **m** is the number of inputs, and the dot product is written out as

w · x = Σᵢ₌₁ᵐ wᵢ xᵢ.

So f(x) = 1 exactly when w₁x₁ + w₂x₂ + … + w_m x_m + b > 0. The output can be encoded as **1 or 0**, or as **1 or −1**, "depending on which activation function is used": the {1, 0} version is the *step (threshold) function*, the {1, −1} version is the *sign function* (as in slide 18 of [[02_History_of_the_Perceptron_and_the_Biological_Neuron]]).

**Why the bias matters.** The set w·x = −b is a line (2-D) or hyperplane (higher D) whose position is shifted away from the origin by b. Without b the boundary would always pass through the origin and could not separate, say, a cluster at (3, 3) from one at (4, 4) — [[08_Linear_Non_Separability_XOR_and_Hyperplanes]] develops the geometry.

**Worked check (illustrative numbers).** w = (2, −1), b = −1, x = (1, 0.5): w·x + b = 2·1 − 1·0.5 − 1 = 0.5 > 0 → f = 1. For x = (0.2, 0.5): 0.4 − 0.5 − 1 = −1.1 → f = 0. (Numbers invented to show the arithmetic.)

**Link back to Lecture 2.** In the pass/fail example the threshold rule "y ≥ th" becomes "y − th ≥ 0", i.e. b = −th ([[09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications]]). Note one tiny difference: here the rule is strict ">" while the pass/fail slide uses "≥". The behaviour only differs when the sum is *exactly* 0; texts differ on which side that case falls.

---

## 2) Simple English Explanation

The perceptron is just a small formula. Take every input, multiply by its weight, add everything up, add the bias, and ask: *is the total bigger than zero?*

- Yes → output **1**.
- No → output **0** (some books use −1 instead of 0; it's only a naming choice).

**w** is the list of weights (how important each input is), **x** is the list of inputs, **b** is the bias (a fixed nudge that moves the decision line away from the centre), and **m** is how many inputs there are.

*Tiny example:* weights 2 and −1, bias −1, inputs 1 and 0.5 → 2×1 − 1×0.5 − 1 = 0.5, which is above 0, so the output is 1. With inputs 0.2 and 0.5 the total is −1.1, so the output is 0.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Perceptron bas ek chhota sa formula hai. Har input ko uske weight se multiply karo, sabko jodo, bias add karo, aur poocho: *kya total zero se bada hai?*

- Haan → output **1**.
- Naa → output **0** (kuch books 0 ki jagah −1 use karti hain; ye sirf naam ka farq hai).

**w** weights ki list hai (har input kitna important hai), **x** inputs ki list hai, **b** bias hai (ek fixed nudge jo decision line ko center se door khisaka deta hai), aur **m** inputs ki ginti hai.

*Chhota example:* weights 2 aur −1, bias −1, inputs 1 aur 0.5 → 2×1 − 1×0.5 − 1 = 0.5, jo 0 se bada hai, isliye output 1. Inputs 0.2 aur 0.5 lo to total −1.1 hai, to output 0.
