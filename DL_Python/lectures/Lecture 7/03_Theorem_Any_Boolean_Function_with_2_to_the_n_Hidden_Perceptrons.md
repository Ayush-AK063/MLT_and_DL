# Topic 3: The Theorem — Any Boolean Function of n Inputs with 2ⁿ Hidden Perceptrons

Source: Lecture 7, slides 15–17 (Theorem; Proof (informal); Note; Catch).

---

## 1) Technical Explanation

**Theorem (slide 15).** *Any Boolean function of n inputs can be represented exactly by a network of perceptrons containing **1 hidden layer with 2ⁿ perceptrons** and **one output layer containing 1 perceptron**.*

**Proof, informal (slide 16).** *We just saw how to construct such a network.* Spelled out:

1. **Hidden layer:** for each of the 2ⁿ possible input patterns create one perceptron with weights ±1 matching that pattern (+1 where the pattern is +1, −1 where it is −1) and bias **−n**. Its weighted sum equals n **only** for its own pattern and is at most n − 2 for every other pattern (each mismatched input lowers the sum by 2), so it fires for exactly that one input.
2. **Output layer:** one perceptron whose weight on hidden unit k equals the desired output for pattern k, with a threshold between "no 1-pattern active" and "a 1-pattern active". Because exactly one hidden unit is active per input, the output reproduces the truth table row by row.

(Checked by script for n = 2 and n = 3: exactly one hidden unit fires per input, and all 2^(2ⁿ) functions — 16 and 256 — are realised.)

**Note (slide 16).** *A network of 2ⁿ + 1 perceptrons is **not necessary but sufficient**. For example, we already saw how to represent the AND function with just 1 perceptron* ([[03_Implementing_Boolean_Functions_AND_OR_NOR_NOT_with_MP_Units]], Lecture 5). The theorem gives an *upper bound* that works for every function; particular functions (the linearly separable ones) need far fewer units. (The slide's total 2ⁿ + 1 = hidden units + the output unit.)

**Catch (slide 17).** *As n increases, the number of perceptrons in the hidden layer obviously increases exponentially.* Concretely:

| n inputs | hidden perceptrons 2ⁿ |
|---|---|
| 2 | 4 |
| 3 | 8 |
| 10 | 1,024 |
| 20 | 1,048,576 |

So the theorem is a statement about **representation power** (what *can* be represented), not about **efficiency**, and not about **learning** (the weights here were constructed, not trained). Deeper networks can often represent the same function with exponentially fewer units — a motivation for *deep* rather than merely wide networks (background; not stated on the slide).

This theorem is the Boolean precursor of the **Universal Approximation Theorem** for arbitrary functions that opens Lecture 8 ([[00_Recap_From_Boolean_to_Arbitrary_Functions]]) and is stated again in Lecture 9 ([[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]]).

---

## 2) Simple English Explanation

**The promise:** for *any* logic function with n yes/no inputs, you can build a two-step network that gets it exactly right: a middle row with **2ⁿ** neurons and one final neuron.

**Why:** n inputs can be combined in 2ⁿ ways. Give each combination its own "doorbell" neuron that rings only for that exact combination. The final neuron then just says, for each doorbell, "answer 1" or "answer 0". Since exactly one doorbell rings for any input, the table is reproduced perfectly.

**Not always needed:** this is a safe recipe, not the cheapest one. AND, for instance, needs just one neuron.

**The catch:** the number of middle neurons doubles with every extra input — 10 inputs need 1,024; 20 inputs need over a million. So it works on paper but is hopelessly large for big problems.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Vaada:** n yes/no inputs wale *kisi bhi* logic function ke liye aap do-step ka network bana sakte ho jo bilkul sahi jawab de: beech ki row mein **2ⁿ** neurons aur ek aakhri neuron.

**Kaise:** n inputs 2ⁿ tareeke se mil sakte hain. Har combination ko uska apna "doorbell" neuron do jo sirf usi exact combination par bajey. Aakhri neuron har doorbell ke liye bas kehta hai "jawab 1" ya "jawab 0". Kisi bhi input par theek ek doorbell bajti hai, isliye table bilkul sahi ban jaata hai.

**Hamesha zaroori nahi:** ye ek surakshit recipe hai, sabse sasta nahi. Jaise AND ko sirf ek neuron chahiye.

**Pench:** har extra input par beech ke neurons doguna ho jaate hain — 10 inputs ko 1,024 chahiye; 20 inputs ko das lakh se zyada. To ye kaagaz par chalta hai par bade problems ke liye bahut bada hai.
