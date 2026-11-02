# Topic 4: The Claim — Any Boolean Function with One Hidden Layer (and the XOR Question)

Source: Lecture 6, slides 27–35 ("We claim that this network can be used to implement any Boolean function (linearly separable or not!)"; "Astonishing claim! Well, not really, if you understand what is going on"; the four perceptrons fire for (−1,−1), (−1,1), (1,−1), (1,1)), with the instructor's handwritten check and the question "XOR function?".

---

## 1) Technical Explanation

**The claim (slides 27–28).** *This network can be used to implement any Boolean function (linearly separable or not!). In other words, we can find w₁, w₂, w₃, w₄ such that the truth table of any Boolean function can be represented by this network.*

**"Astonishing claim! Well, not really, if you understand what is going on" (slides 29–30).** The explanation comes next.

**Each hidden perceptron fires for exactly one input (slides 31–35).** *Each perceptron in the middle layer fires only for a specific input, and no two perceptrons fire for the same input:*

- the **first** fires for **(−1, −1)**,
- the **second** for **(−1, +1)** (slide prints it with braces),
- the **third** for **(+1, −1)**,
- the **fourth** for **(+1, +1)**.

The handwritten check on slide 32 confirms: for h₁ and input (−1,−1) the sum is (−1)(−1) + (−1)(−1) = 2 (≥ 2 ⇒ fires); for h₂ and input (−1, 1): (−1)(−1) + (1)(1) = 1 + 1 = 2 ⇒ fires. The full table is in [[02_Network_of_Perceptrons_MLP_Introduction]].

**Why the claim holds — the output layer picks the 1-rows.** Because only one hidden unit is active per input, the output neuron's weighted sum Σ wᵢhᵢ equals the single weight wᵢ of the active unit. So choose **wᵢ = (desired output for the input that hᵢ detects)** and an output threshold between 0 and 1 (here: output 1 iff Σ wᵢhᵢ ≥ 1). The slide does not fix the output neuron's threshold or activation; this choice is an illustration made here.

**Verification (done here).** With hidden units as above and w ∈ {0,1}⁴, **all 2⁴ = 16 Boolean functions of two inputs were realised** exactly (checked row by row). In particular:

| Function | (w₁, w₂, w₃, w₄) | Outputs for (−1,−1), (−1,1), (1,−1), (1,1) |
|---|---|---|
| **XOR** | (0, 1, 1, 0) | 0, 1, 1, 0 ✓ |
| AND (in ±1, true = +1) | (0, 0, 0, 1) | 0, 0, 0, 1 ✓ |
| OR | (0, 1, 1, 1) | 0, 1, 1, 1 ✓ |

**The XOR question (slide 36's handwritten note).** The instructor writes **"XOR function?"** over the final slide with the four input pairs (−1,−1), (−1,1), (1,−1), (1,1) written above h₁…h₄. This poses the natural test: XOR cannot be done by one perceptron ([[08_Linear_Non_Separability_XOR_and_Hyperplanes]], Lecture 3), but with this network it is just "weight h₂ and h₃ positively, h₁ and h₄ zero" — worked in full in Lecture 7 (XOR Implementation Example).

**Honest limits of the claim (background, not on the slides).**

- It is a statement about **representation**, not **learning**: weights are chosen by inspection, not found by a training algorithm.
- It needs **2ⁿ hidden perceptrons for n inputs** (one per input pattern) — exponential. With n = 20 that is over a million units; deeper networks can represent many functions with far fewer units.
- It foreshadows the **Universal Approximation Theorem** (arbitrary functions, not just Boolean) that Lecture 8 and Lecture 9 return to ([[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]], [[00_Recap_From_Boolean_to_Arbitrary_Functions]]).

---

## 2) Simple English Explanation

**The big claim:** this small network (two inputs → four middle neurons → one output neuron) can do **any** logic function you can write a truth table for — even ones a single neuron cannot, like XOR.

**Why it isn't magic:** the four middle neurons are like **four doorbells, one per possible input pair**. For each input pair, **exactly one** doorbell rings: the first for (−1,−1), the second for (−1,+1), the third for (+1,−1), the fourth for (+1,+1). The final neuron just has to say, for each doorbell, whether the answer should be 1 or 0.

**Example — XOR** ("answer 1 when the two inputs are different"): the doorbells for (−1,+1) and (+1,−1) should give 1, the other two should give 0. So give weight 1 to the second and third middle neurons and weight 0 to the first and fourth. Check all four inputs — it works. 

**Catches:** (1) we picked the weights by thinking, not by learning; (2) we needed one middle neuron per possible input, which explodes as inputs grow (20 inputs → over a million neurons). Smarter, deeper networks avoid that.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Bada dawa:** ye chhota network (do inputs → chaar beech ke neurons → ek output neuron) **koi bhi** logic function kar sakta hai jiska truth table likha ja sake — wo bhi jo ek neuron nahi kar sakta, jaise XOR.

**Ye jaadu kyun nahi hai:** chaar beech ke neurons **chaar doorbells** jaise hain, har possible input-pair ke liye ek. Har input-pair par **theek ek** doorbell bajti hai: pehli (−1,−1) par, doosri (−1,+1) par, teesri (+1,−1) par, chauthi (+1,+1) par. Aakhri neuron ko bas har doorbell ke liye batana hai ki answer 1 hona chahiye ya 0.

**Example — XOR** ("answer 1 jab dono inputs alag hon"): (−1,+1) aur (+1,−1) ki doorbells ko 1 deni chahiye, baaki do ko 0. To doosre aur teesre beech wale neuron ko weight 1 do aur pehle aur chauthe ko weight 0. Chaaron inputs check karo — kaam karta hai.

**Kamiyan:** (1) weights humne sochkar chune, seekhkar nahi; (2) har possible input ke liye ek beech ka neuron chahiye tha, jo inputs badhne par bahut bada ho jaata hai (20 inputs → das lakh se zyada neurons). Smart, deeper networks isse bachate hain.
