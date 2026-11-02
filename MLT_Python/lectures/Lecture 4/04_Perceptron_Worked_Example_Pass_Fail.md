# Topic 4: Perceptron Worked Example — Student Pass/Fail

Source: Lecture 4, slides 14–19 (handwritten "Whether or not someone can squat more than body weight" example, then the formal Student Pass/Fail example built up step-by-step).

This topic walks through the **exact same worked example the lecture builds incrementally** — every equation and rule is preserved and explained in order, so nothing is skipped.

---

## 1) Technical Explanation

**Warm-up example (slide 14)**: The lecture first illustrates the perceptron idea with a fitness-themed example: predicting *"whether or not someone can squat more than body weight"*, given two inputs — **years of lifting experience** (e.g., 3 years) and **body weight** (e.g., 60 kg). These two inputs flow into a **"Process input"** step, which outputs a decision: "Squats more than body weight" (yes/no). This is credited to **Frank Rosenblatt, 1957**, reinforcing the historical connection from the previous topic.

**Formal example — Student Pass/Fail (slides 15–19)**, built up incrementally:

**Step 1 (slide 15) — Define the problem and inputs**:
- **Problem**: predict Student **Pass/Fail** as the output.
- **Inputs**: `x1 → Attendance` (paired with weight `w1`), `x2 → Homework` (paired with weight `w2`).

**Step 2 (slide 16) — Draw the network structure**: `x1` and `x2` feed into an intermediate node `y` via weighted connections (`w1`, `w2` respectively), and `y` feeds into a final node `z`, which represents the Pass/Fail decision.

**Step 3 (slide 17) — Write the weighted sum equation**:
`y = x1·w1 + x2·w2`
This is the **weighted sum** — each input is multiplied by its corresponding weight, and the products are added together. This is the mathematical core of how a perceptron combines multiple inputs into a single value.

**Step 4 (slide 18) — Add the bias term**:
`y = x1·w1 + x2·w2 + b`
A **bias `b`** is added to the weighted sum. The bias shifts the decision boundary independently of the inputs — allowing the perceptron to output a non-zero value even when all inputs are zero, and giving the model an extra degree of freedom to fit the data correctly (explored further in Topic 7, [[07_Weights_Bias_and_Real_World_Perceptron_Examples]]).

**Step 5 (slide 19) — Apply a threshold rule to get the final decision**:
```
y ≥ th  →  Pass
y < th  →  Fail
```
Here `th` (threshold) is a cutoff value: if the computed `y` value meets or exceeds the threshold, the perceptron outputs "Pass"; otherwise, it outputs "Fail." This threshold rule is the perceptron's **activation function** in its most basic form — a **step function** that converts a continuous weighted-sum value into a binary (categorical) decision.

**Putting it all together**: Given a student's attendance (`x1`) and homework score (`x2`), the trained perceptron computes `y = x1·w1 + x2·w2 + b`, then compares `y` against a threshold to decide Pass or Fail. The weights `w1`, `w2` and bias `b` are the parameters that would be **learned** from training data (labelled examples of students with known Pass/Fail outcomes) — though the specific learning algorithm (how weights get updated) is not covered in this lecture.

---

## 2) Simple English Explanation

This section builds up, step by step, a tiny working example of how a perceptron makes a decision — using a "will this student pass or fail" problem.

**Step 1 — What are we predicting, and from what?**
We want to predict: will a student **Pass or Fail**? We'll base this on two pieces of information:
- `x1` = the student's **Attendance**
- `x2` = the student's **Homework** score

Each of these inputs gets its own "importance number" called a **weight** — `w1` for attendance, `w2` for homework.

**Step 2 — How the pieces connect**
Picture the two inputs (`x1`, `x2`) flowing into a middle step (`y`), which then leads to a final decision (`z`) — Pass or Fail.

**Step 3 — Combine the inputs (weighted sum)**
The perceptron multiplies each input by its weight, then adds them together:
`y = x1×w1 + x2×w2`
This is just a way of saying: "combine attendance and homework, but let some matter more than others depending on the weight."

**Step 4 — Add a bias**
`y = x1×w1 + x2×w2 + b`
A **bias** `b` is a small extra number added on top — think of it as a built-in "default lean" toward pass or fail, independent of the student's attendance or homework, that helps the model fit real data better.

**Step 5 — Turn the number into a Pass/Fail decision**
Now that we have a single number `y`, we need to turn it into an actual decision. The rule is simple:
- If `y` is **greater than or equal to** some cutoff value (the **threshold**), the answer is **Pass**.
- If `y` is **less than** the threshold, the answer is **Fail**.

**Overall**: given a student's attendance and homework, this tiny perceptron does some simple math (multiply, add, add a bias) and then compares the result to a cutoff to decide Pass or Fail. In real training, the weights and bias wouldn't be picked randomly — they'd be learned automatically from many past examples of real students and their actual outcomes.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section step-by-step dikhata hai ki ek Perceptron kaise decision leta hai — "student pass hoga ya fail" wale example se.

**Warm-up Example (Squat wala example)**:
Lecture pehle ek fitness wala example deta hai: **"Kya insaan apne body weight se zyada squat kar sakta hai?"** — 2 inputs se predict karna: kitne saal se lifting kar raha hai (jaise 3 saal), aur body weight (jaise 60 kg). Ye idea 1957 mein **Frank Rosenblatt** ne diya tha.

**Ab formal example — Student Pass/Fail:**

**Step 1 — Kya predict karna hai, aur kis se?**
Hum predict karna chahte hai: student **Pass hoga ya Fail**? Iske liye 2 information use karenge:
- `x1` = Student ki **Attendance**
- `x2` = Student ka **Homework** score

Har input ka apna "importance number" hota hai jise **weight** kehte hai — `w1` attendance ke liye, `w2` homework ke liye.

**Step 2 — Pieces kaise connect hote hai**
`x1` aur `x2` ek beech ke step (`y`) mein jaate hai, jo fir final decision (`z`) tak pahunchta hai — Pass ya Fail.

**Step 3 — Inputs ko combine karna (Weighted Sum)**
Perceptron har input ko uske weight se multiply karta hai, fir sabko add karta hai:
`y = x1×w1 + x2×w2`
Iska matlab hai: "attendance aur homework ko combine karo, lekin weight ke hisaab se kisi ko zyada important maano."

**Step 4 — Bias add karna**
`y = x1×w1 + x2×w2 + b`
Ek **bias** `b` extra number hota hai jo add hota hai — isko ek "built-in tendency" samjho jo student ke attendance/homework se independent hoti hai, aur model ko real data ke saath fit hone mein madad karti hai.

**Step 5 — Number ko Pass/Fail decision mein badalna**
Ab humare paas ek single number `y` hai, isse actual decision banana hai. Rule simple hai:
- Agar `y` **threshold (cutoff value) se zyada ya barabar** hai → **Pass**
- Agar `y` **threshold se kam** hai → **Fail**

**Overall summary:**
Student ki attendance aur homework dekh kar, ye chhota perceptron simple maths karta hai (multiply, add, bias add), fir result ko ek cutoff se compare karke Pass/Fail decide karta hai. Real training mein, weights aur bias **random nahi choose kiye jaate** — wo bahut saare purane real students ke data se (jinka actual result pata hai) **automatically seekhe jaate hai**.
