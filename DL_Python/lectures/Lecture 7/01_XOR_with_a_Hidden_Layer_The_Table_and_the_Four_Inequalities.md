# Topic 1: Implementing XOR with the Hidden-Layer Network — The Table and the Four Inequalities

Source: Lecture 7, slides 2–9 (XOR Function: network with hidden units labelled (−1,−1), (−1,1), (1,−1), (1,1); "Let w₀ be the bias output of the neuron (i.e. it will fire if Σwᵢhᵢ ≥ w₀)"; the truth-table built up row by row; "This results in the following four conditions to implement XOR"; "Unlike before, there are no contradictions now").

---

## 1) Technical Explanation

**Set-up.** The network is the one from [[02_Network_of_Perceptrons_MLP_Introduction]] (Lecture 6): two inputs, four hidden perceptrons h₁…h₄ with ±1 weights and bias −2, and one output perceptron fed through weights w₁…w₄. On the slides the four hidden units are now **labelled with the input pair they detect**: (−1,−1), (−1,1), (1,−1), (1,1). The output perceptron fires iff

Σᵢ₌₁⁴ wᵢhᵢ ≥ w₀,

where **w₀ is the output neuron's threshold ("bias output")** (the slide's wording).

**The table (slides 3–7).** Rows are the XOR truth table; the inputs are written 0/1 (0 ↔ the −1 "false" of the network, 1 ↔ +1 "true"). Exactly one hᵢ is 1 per row:

| x₁ | x₂ | XOR | h₁ | h₂ | h₃ | h₄ | Σ wᵢhᵢ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 0 | 0 | w₁ |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 | w₂ |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | w₃ |
| 1 | 1 | 0 | 0 | 0 | 0 | 1 | w₄ |

**The four conditions (slides 8–9).** Rows with XOR = 0 need Σ wᵢhᵢ < w₀; rows with XOR = 1 need Σ wᵢhᵢ ≥ w₀:

- **w₁ < w₀**
- **w₂ ≥ w₀**
- **w₃ ≥ w₀**
- **w₄ < w₀**

**"Unlike before, there are no contradictions now and the system of inequalities can be satisfied"** — "before" refers to the single-perceptron attempt, where the four conditions on (w₁, w₂, b) contradicted each other ([[08_Linear_Non_Separability_XOR_and_Hyperplanes]] gives the algebraic proof). Here **each wᵢ is responsible for exactly one of the four inputs** and can be adjusted independently to get the desired output for that input — the four inequalities involve four *different* unknowns, so they cannot clash.

**A concrete solution (illustration, not on the slide; verified here).** Take **w = (0, 1, 1, 0) and w₀ = 1**: 0 < 1 ✓, 1 ≥ 1 ✓, 1 ≥ 1 ✓, 0 < 1 ✓. Then the network outputs 0, 1, 1, 0 for the four inputs — XOR. Many other choices work (e.g. w = (−1, 1, 1, −1), w₀ = 0).

**Why it escapes the single-perceptron limit.** The hidden layer *re-represents* the inputs: in the space (h₁, h₂, h₃, h₄) the four input points become the four corners of a 4-D "one-hot" cube, and in that new representation the XOR labels are linearly separable (a hyperplane Σwᵢhᵢ = w₀ separates {e₂, e₃} from {e₁, e₄}). This is exactly the "good representation makes the problem easy" theme of [[08_Issue_and_Choice_of_Representation]] (Lecture 1) and [[02_Representation_Learning_and_Factors_of_Variation]] (Lecture 2) — here realised by hand-wiring.

---

## 2) Simple English Explanation

Recall the middle layer has four "doorbell" neurons, one for each possible input pair; for any input exactly one doorbell rings. XOR means "answer 1 when the two inputs are *different*".

Make a table: for input (0,0) only doorbell 1 rings, for (0,1) only doorbell 2, for (1,0) only doorbell 3, for (1,1) only doorbell 4. The final neuron adds up the weights of the doorbells that rang and fires if the sum reaches its bar w₀. So we need:

- doorbell 1 (input 0,0 → answer 0): **w₁ below the bar**,
- doorbell 2 (0,1 → answer 1): **w₂ at or above the bar**,
- doorbell 3 (1,0 → answer 1): **w₃ at or above the bar**,
- doorbell 4 (1,1 → answer 0): **w₄ below the bar**.

Each rule is about a *different* weight, so they never fight. Example: bar w₀ = 1; weights 0, 1, 1, 0. With one neuron on its own, the rules *did* fight — which is why one neuron can't do XOR but this team can.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yaad karo beech ki layer mein chaar "doorbell" neurons hain, har possible input pair ke liye ek; kisi bhi input par theek ek doorbell bajti hai. XOR ka matlab: "jawab 1 jab dono inputs *alag* hon".

Ek table banao: input (0,0) par sirf doorbell 1 bajti hai, (0,1) par sirf doorbell 2, (1,0) par sirf doorbell 3, (1,1) par sirf doorbell 4. Aakhri neuron un doorbells ke weights jodta hai jo baji, aur agar sum uski bar w₀ tak pahunche to fire karta hai. To hume chahiye:

- doorbell 1 (input 0,0 → jawab 0): **w₁ bar se neeche**,
- doorbell 2 (0,1 → jawab 1): **w₂ bar ke barabar ya upar**,
- doorbell 3 (1,0 → jawab 1): **w₃ bar ke barabar ya upar**,
- doorbell 4 (1,1 → jawab 0): **w₄ bar se neeche**.

Har rule ek *alag* weight ke baare mein hai, isliye wo kabhi takrate nahi. Example: bar w₀ = 1; weights 0, 1, 1, 0. Akele ek neuron ke saath ye rules aapas mein takrate the — isiliye ek neuron XOR nahi kar sakta par ye team kar sakti hai.
