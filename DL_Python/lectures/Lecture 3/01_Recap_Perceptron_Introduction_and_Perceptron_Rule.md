# Topic 1: Recap — The Perceptron Introduction, plus the Squat Example, Multi-Input Perceptron and the Perceptron Rule

Source: Lecture 3, slides 4–17 (What is a Perceptron? ×2; Perceptron ×8 build-ups; weights-and-bias slide; two network figures; Perceptron rule). Slides 4 and 6–14 are the same slides as Lecture 2's perceptron section.

---

## 1) Technical Explanation

**Already covered — see Lecture 2, [[09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications]].** These repeated slides are *not* re-derived here:

- the **student pass/fail** problem (inputs x₁ = attendance, x₂ = homework; y = x₁w₁ + x₂w₂ (+ b); y ≥ th → Pass, y < th → Fail),
- the **general perceptron** diagram with inputs x₁…x_N, weights w₀…w_N, weighted sum Σ and activation function f, including the *net input function*, *activation function*, *positive or negative weights* and the *error ŷ ≠ y* annotation,
- the **definitions of weights and bias** (weights are numerical values on the connections between neurons; biases are additional parameters that adjust a neuron's output).

**New in Lecture 3.**

1. **The squat example (slide 5).** A hand-drawn example for the same model: *Whether or not someone can squat more than body weight, given years of lifting experience and body weight.* Inputs: "3 years lifting" and "60 kg body weight" feed a "process input" node whose output is "squats more than body weight". Annotated **Frank Rosenblatt, 1957**, crediting the perceptron's inventor. It is another instance of "weighted inputs → one yes/no decision".

2. **Multi-input perceptron figure, no annotations (slide 15, counter 84).** The inputs 1, x₁ … x_N with weights w₀ … w_N flow into Σ, then an activation node, then output y — the same diagram as in Lecture 2 before annotation.

3. **Clean textbook version (slide 16).** Labelled boxes — *Inputs, Weights, Net input function, Activation function* — with inputs 1, x₁, x₂ … x_m, weights w₀ … w_m, a Σ node, a **step-function** activation node and a single output.

4. **The Perceptron rule (slide 17).** The same figure with an **Error** box: the output is compared against the target and the **error is fed back to the weights** (arrow from the Error box back to the weights). The slide title is "Perceptron rule". It states the *idea* of learning — adjust weights from the error — without the update formula; the formula is the subject of **Lecture 4, "Perceptron Learning Algorithm"** (not yet in this repo).

**Consistency check.** This feedback loop is exactly the "flow backward information" hook of [[00_Can_You_See_Mistakes_in_the_Network]].

---

## 2) Simple English Explanation

Most of these slides repeat last lecture's story of the pass/fail perceptron (clues × importance → add → decide), so go back to [[09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications]] if you need it.

What's new:

- **A gym example:** "Can this person squat more than their body weight?" The clues are *years of lifting* and *body weight*. The perceptron mixes them and answers yes/no. (The slide credits **Frank Rosenblatt, 1957**, who invented the perceptron.)
- **Neat diagrams** of the whole machine: inputs → importance numbers (weights) → add them up (net input) → activation (the yes/no switch) → output.
- **The Perceptron rule:** compare the output with the right answer; if wrong, send the error **back** to nudge the weights. How exactly to nudge them comes next lecture.

---

## 3) Hinglish Explanation (Beginner-Friendly)

In zyada tar slides pichle lecture ki pass/fail perceptron wali kahani dohrati hain (clues × importance → jodo → decide karo), to zaroorat ho to [[09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications]] par wapas jaao.

Jo naya hai:

- **Gym ka example:** "kya ye insaan apne body weight se zyada squat kar sakta hai?" Clues hain *kitne saal lifting ki* aur *body weight*. Perceptron inhe mila kar haan/naa mein jawab deta hai. (Slide **Frank Rosenblatt, 1957** ko credit deti hai, jinhone perceptron invent kiya.)
- Poori machine ke **saaf diagrams**: inputs → importance numbers (weights) → sab jodo (net input) → activation (haan/naa ka switch) → output.
- **Perceptron rule:** output ko sahi jawab se compare karo; agar galat ho to error ko **peeche** bhejo aur weights ko thoda hilao. Kaise hilana hai, ye agle lecture mein aayega.
