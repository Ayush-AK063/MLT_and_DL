# Topic 5: Worked Example — Logistic Regression for Exam Pass Probability

Source: Lecture 15, slides 23–26 (the pass/fail exercise, log(odds) model, both sub-questions solved). Independently re-verified numerically end-to-end.

---

## 1) Technical Explanation

**The exercise (slide 23).** A dataset of 5 students records how many hours each studied and whether they passed (1) or failed (0) an exam:

| Hours Study | Pass (1) / Fail (0) |
|---|---|
| 29 | 0 |
| 15 | 0 |
| 33 | 1 |
| 28 | 1 |
| 39 | 1 |

The exercise states that a logistic regression model has **already been fit** (by "the optimizer," i.e., whatever fitting procedure — not shown here, since this exercise focuses only on *using* the fitted model, unlike the from-scratch derivations in earlier lectures) to give this log-odds equation:

**log(odds) = −64 + 2 × hours**

Two questions are asked:
1. **Calculate the probability of passing for a student who studied 33 hours.**
2. **At least how many hours must a student study so that P(pass) > 95%?**

**The sigmoid formula, restated (slide 23):** S(x) = 1/(1+e⁻ˣ) — same formula as [[03_The_Sigmoid_Function_and_Decision_Boundary]], here named S(x) instead of sigmoid(z), applied directly to the log-odds value to convert it into a probability.

**Question 1 — solving for x1=33 hours (slide 24):**

- z = −64 + 2×33 = −64 + 66 = **2**
- P = 1/(1+e⁻²) = **0.88**

So a student who studied 33 hours has an **88% predicted probability of passing**. Sanity-checking this against the raw data: the table shows a student who studied exactly 33 hours *did* pass (Y=1) — consistent with an 88% predicted probability (a high but not certain chance).

**Question 2 — solving for the minimum hours needed for P > 0.95 (slides 25–26).** This runs the sigmoid formula *backwards*: instead of "given hours, find P," it's "given the target P, find the hours." Starting from:

P = 1/(1+e⁻ᶻ) = 0.95

Step-by-step algebra (as shown on the slide):
1. 0.95 × (1+e⁻ᶻ) = 1
2. 0.95 × e⁻ᶻ = 1 − 0.95 = 0.05
3. e⁻ᶻ = 0.05/0.95 = 0.0526
4. Take the natural log of both sides: −z = ln(0.0526) ≈ −2.945
5. So **z ≈ 2.95**

The slide uses the identity **ln(eˣ) = x** to justify taking the natural log on both sides — this is exactly what "undoes" the exponential, the same inverse relationship that makes logarithms useful for solving equations where the unknown is stuck in an exponent.

Then, substituting z back into the original log-odds equation to solve for hours:

- z = −64 + 2×hours
- 2.95 = −64 + 2×hours
- 2×hours = 2.95 + 64 = 66.95
- **hours = 66.95 / 2 = 33.47**

So a student needs to study **at least about 33.47 hours** (in practice, this would be rounded up to 34 hours, since you can't study a negative fraction of an hour short of the requirement and still clear the threshold) to have more than a 95% predicted chance of passing.

**Independent verification.** I recomputed both parts from scratch using the exact same formulas:
- Q1: z = 2 exactly; P = 1/(1+e⁻²) = **0.8807970...** ≈ 0.88 ✓ (matches the slide's "88% chance" exactly)
- Q2: solving 1/(1+e⁻ᶻ) = 0.95 precisely gives z = **2.9444...** (the slide's rounded 0.0526 gives z ≈ 2.945, matching within normal rounding) → hours = (2.9444+64)/2 = **33.472...** ✓ (matches the slide's 33.47 essentially exactly)

Both parts of this worked example check out precisely.

**Why this matters as a general pattern.** This exercise demonstrates the *other direction* of using a fitted logistic regression model beyond simple prediction: not just "given an input, what's the probability?" but "given a target probability, what input is needed to reach it?" This second direction requires **inverting** the sigmoid function — which is exactly the **logit function** (log-odds), the same concept introduced in [[03_The_Sigmoid_Function_and_Decision_Boundary]]: sigmoid and logit are mathematical inverses of each other, so going from probability back to the underlying linear score always means taking a log-odds transform, exactly as done step-by-step here.

---

## 2) Simple English Explanation

Here's a small, complete example that uses everything from this lecture end-to-end. Five students' study hours and pass/fail results:

| Hours Study | Pass (1) / Fail (0) |
|---|---|
| 29 | 0 |
| 15 | 0 |
| 33 | 1 |
| 28 | 1 |
| 39 | 1 |

We're told (not shown how it was derived — just given, as something a fitting algorithm already worked out) that the relationship between study hours and the log-odds of passing is:

**log(odds) = −64 + 2 × hours**

**Question 1: What's the probability of passing if you studied 33 hours?**

Plug 33 into the formula: −64 + 2×33 = −64+66 = **2**. Now run this through the sigmoid formula: 1/(1+e⁻²). Working that out gives **0.88**, i.e., an **88% chance of passing**. I double-checked this calculation myself and got the exact same 88%.

**Question 2: How many hours do you need to study to have more than a 95% chance of passing?**

This is the same question *backwards* — instead of "given hours, find the probability," it's "given the probability I want (95%), find the hours." You do this by algebraically undoing each step: starting from 0.95 = 1/(1+e⁻ᶻ), you solve for z first (this comes out to about **2.95**), and *then* plug that z back into "z = −64 + 2×hours" and solve for hours:

2.95 = −64 + 2×hours → 2×hours = 66.95 → **hours = 33.47**

So you'd need to study at least about **33.47 hours** — in real life you'd round that up to **34 hours**, since anything less wouldn't quite clear the 95% bar. I redid this whole backward calculation myself independently and got the same 33.47 hours, confirming the slide's answer is correct.

**The big-picture point of this example**: a fitted logistic regression model isn't just useful for "given an input, predict the probability" (like Question 1) — you can also run it *in reverse* to answer "what input do I need to guarantee a certain probability?" (like Question 2). This reverse direction always involves working with log-odds, the same "log(odds)" idea that shows up throughout this lecture.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yeh ek chhota, complete example hai jo is poori lecture ki sabhi cheezein end-to-end use karta hai. Paanch students ke study hours aur pass/fail results:

| Hours Study | Pass (1) / Fail (0) |
|---|---|
| 29 | 0 |
| 15 | 0 |
| 33 | 1 |
| 28 | 1 |
| 39 | 1 |

Humein bataya gaya hai (yeh nahi dikhaya gaya ki kaise derive hua — bas diya gaya hai, jaise koi fitting algorithm pehle se nikaal chuka hai) ki study hours aur pass hone ke log-odds ke beech relationship yeh hai:

**log(odds) = −64 + 2 × hours**

**Sawaal 1: Agar kisi ne 33 hours study kiya, toh pass hone ki probability kya hai?**

Formula mein 33 daalo: −64 + 2×33 = −64+66 = **2**. Ab isko sigmoid formula se pass karo: 1/(1+e⁻²). Yeh calculate karne pe **0.88** aata hai, matlab **88% pass hone ka chance**. Maine yeh calculation khud double-check ki aur exact same 88% mila.

**Sawaal 2: Kitne hours study karna padega taaki pass hone ka chance 95% se zyada ho?**

Yeh wahi sawaal hai *ulta* — "hours diye hain, probability nikalo" ki jagah, "probability chahiye (95%), hours nikalo." Yeh karte hain har step ko algebraically ulta karke: 0.95 = 1/(1+e⁻ᶻ) se shuru karke, pehle z nikalte hain (yeh roughly **2.95** aata hai), aur *phir* us z ko "z = −64 + 2×hours" mein wapas daalke hours nikalte hain:

2.95 = −64 + 2×hours → 2×hours = 66.95 → **hours = 33.47**

Toh kam se kam **33.47 hours** study karna padega — real life mein isko round up karke **34 hours** bolenge, kyunki isse kam se 95% bar clear nahi hoga. Maine yeh poora backward calculation khud independently redo kiya aur same 33.47 hours mila, confirming ki slide ka answer sahi hai.

**Is example ka big-picture point yeh hai**: ek fitted logistic regression model sirf "input diya hai, probability predict karo" (jaise Sawaal 1) ke liye useful nahi hai — usko *reverse* mein bhi run kar sakte ho yeh poochhne ke liye "kaunsa input chahiye ek certain probability guarantee karne ke liye?" (jaise Sawaal 2). Yeh reverse direction hamesha log-odds ke saath kaam karta hai, wahi "log(odds)" idea jo poori lecture mein dikhta hai.
