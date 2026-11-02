# Topic 5: The Least Squares Method — Formula and Worked Example (Exam Grades)

Source: Lecture 13, slides 20–24 (Exercise, "Least Squares Method", full worked derivation of a and b, final prediction). Enriched with web research (Gauss–Legendre history of least squares) and independently re-verified numerically.

---

## 1) Technical Explanation

**The exercise (slide 20).** A table gives the Midterm exam grade (X) and Final exam grade (Y) for 12 students:

| X (Midterm) | 72 | 50 | 81 | 74 | 94 | 86 | 59 | 83 | 65 | 33 | 88 | 81 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Y (Final)** | 84 | 63 | 77 | 78 | 90 | 75 | 49 | 79 | 77 | 52 | 74 | 90 |

The task: use the **Least Squares Method** to find the equation predicting Final grade from Midterm grade, then predict the Final grade for a student who scored **86** on the midterm. The handwritten annotation restates the objective precisely: "minimize the sum of squared differences" — i.e., minimize Σ(ŷᵢ − yᵢ)², the same Δ²-minimization principle introduced visually in [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]], now being applied formally.

**What the Least Squares Method is (slide 21).** Defined on the slide as: a method used to find the best-fitting line or curve for a set of data points, widely used in statistics, regression analysis, data fitting and predictive modeling — and it works by **minimizing the sum of squared differences between the observed data points and the predicted values**. (Slide cites [geeksforgeeks.org/maths/least-square-method](https://www.geeksforgeeks.org/maths/least-square-method/) as its source.)

**A brief history worth knowing (not on the slide).** The method itself predates modern regression/ML by roughly two centuries. It was first published by **Adrien-Marie Legendre** in 1805 (in an appendix to his book on comet orbits), while **Carl Friedrich Gauss** claimed to have been using the same method privately since 1795 and published his own derivation in 1809. This led to a real, documented priority dispute between the two mathematicians — Legendre publicly accused Gauss of taking credit for his idea. Modern historians of statistics (e.g., Stephen Stigler) generally credit Gauss with likely discovering the method first but Legendre with the priority of *publication* — a useful reminder that "least squares" long predates computers, and was originally developed for problems like fitting orbits of comets and planets from noisy astronomical measurements. (Source: [Gauss and the Invention of Least Squares — Annals of Statistics/Project Euclid](https://projecteuclid.org/journals/annals-of-statistics/volume-9/issue-3/Gauss-and-the-Invention-of-Least-Squares/10.1214/aos/1176345451.full).)

**The formulas (slide 22).** For the line **y = a + bx** (note: here **a** is the intercept and **b** is the slope — the opposite letter convention from y = mx+b used earlier in the lecture, so watch the swap):

- **a → intercept**
- **b → slope or coefficient**

**b = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)²**

**ȳ = a + b·x̄**, rearranged to **a = ȳ − b·x̄**

where x̄ and ȳ are the sample means of X and Y respectively. This is the standard closed-form (calculus-derived) solution that directly minimizes the sum of squared errors for simple linear regression — no iteration or guessing required, unlike more general optimization methods (e.g., gradient descent) needed for models that don't have a closed-form solution.

**The full worked calculation (slides 23–24).**

- x̄ = 72.17, ȳ = 74 (means of the 12 midterm and final scores)
- The slide builds a table of (x−x̄), (y−ȳ), (x−x̄)(y−ȳ), and (x−x̄)² for every student, then sums the last two columns:
  - Σ(x−x̄)(y−ȳ) = **2004**
  - Σ(x−x̄)² = **3445.67**
- **b = 2004 / 3445.67 = 0.5816**
- **a = ȳ − b·x̄ = 74 − 0.5816 × 72.17 = 32.02**
- Final equation: **y = 32.02 + 0.5816x**
- Prediction for x = 86: **y = 32.02 + 0.5816 × 86 = 82.04**

**Independent verification.** I recomputed the entire table from scratch (x̄ = 72.1667, ȳ = 74) and reproduced the slide's per-row values to within normal rounding (e.g., student 2: x−x̄ = −22.17, y−ȳ = −11, product = 243.83 vs. the slide's 243.87 — a rounding artifact from the slide using x̄ rounded to 72.17 rather than the exact 72.1667). The column sums matched exactly: Σ(x−x̄)(y−ȳ) = **2004.0**, Σ(x−x̄)² = **3445.67**, giving:

- **b = 0.581600...** (slide: 0.5816 ✓)
- **a = 32.0279...** (slide: 32.02 ✓)
- **Prediction at x = 86: y = 82.0455** (slide: 82.04 ✓, matches to the shown precision — a cross-check with NumPy's `polyfit` gave the identical slope and intercept, confirming the by-hand derivation.)

So the slide's worked example is fully correct — this is the same b formula used to verify the home-price example's slope in [[02_Simple_Linear_Regression_Worked_Example_Home_Prices]], applied here on real integer exam-score data end-to-end.

---

## 2) Simple English Explanation

This is the lecture's big "now let's actually do the math by hand, all the way through" example. We have 12 students, and for each one we know their **Midterm score (X)** and **Final exam score (Y)**. The goal: find a formula that predicts a student's Final score just from knowing their Midterm score, then use it to guess the Final score of a student who got 86 on the midterm.

**What is the "Least Squares Method"?** It's just the official name for the trick already used earlier in the lecture: draw a line through the data such that if you measure the vertical gap between each real point and the line, square each gap, and add them all up, that total is as small as it can possibly be. This method is over 200 years old — it was first published in 1805 by a French mathematician named Legendre, though the German mathematician Gauss claimed he'd secretly been using it since 1795. This actually caused a famous argument between the two of them about who really deserves the credit! It was originally invented to help astronomers fit smooth orbit paths to noisy telescope measurements of comets and planets — long, long before anyone had a computer, let alone "machine learning."

**The two formulas you need:**
- **b (the slope)** = "how much X and Y move together" divided by "how spread out X is." In formula form: add up (each x minus the average x) times (each y minus the average y), for every student, then divide by the sum of (each x minus the average x) squared.
- **a (the intercept)** = the average of Y, minus b times the average of X.

**Doing it step by step with the real numbers:**
1. Average midterm score (x̄) = 72.17. Average final score (ȳ) = 74.
2. For every student, work out how far their midterm is from 72.17, and how far their final is from 74, multiply those two differences together, and add all 12 up. This total comes out to **2004**.
3. Also square each "how far the midterm is from 72.17" value and add those up too — this comes to **3445.67**.
4. Divide: b = 2004 ÷ 3445.67 = **0.5816**. This is the slope — for every extra point on the midterm, the final score tends to go up by about 0.58 points.
5. a = 74 − (0.5816 × 72.17) = **32.02**. This is the intercept.
6. So the formula is: **Final = 32.02 + 0.5816 × Midterm**.
7. For a midterm score of 86: Final = 32.02 + 0.5816 × 86 = **82.04**.

I redid this entire calculation independently from scratch (not just trusting the slide) and got matching numbers all the way through — average, both sums, slope, intercept, and the final prediction of about 82.05 (the 0.01 difference from the slide's 82.04 is just because the slide rounded the average midterm score to 72.17 instead of carrying the full 72.1667 through the calculation). So this worked example is correct and trustworthy to learn from.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Yeh lecture ka bada "ab poori maths hath se karke dikhate hain" example hai. Humare paas 12 students hain, aur har ek ka **Midterm score (X)** aur **Final exam score (Y)** pata hai. Goal: ek formula dhundo jo sirf Midterm score se Final score predict kar de, phir usse ek student ka Final score guess karo jisne midterm mein 86 liya tha.

**"Least Squares Method" kya hai?** Yeh bas usi trick ka official naam hai jo lecture mein pehle use hua tha: data ke through ek aisi line kheencho ki agar har real point aur line ke beech ka vertical gap naapo, har gap ko square karo, aur sabko add karo, toh wo total sabse kam ho. Yeh method 200 saal se bhi purani hai — pehli baar 1805 mein ek French mathematician Legendre ne publish kiya tha, jabki German mathematician Gauss ne claim kiya ki wo isko secretly 1795 se hi use kar raha tha. Isse dono ke beech ek famous jhagda hua tha ki asli credit kiska hai! Yeh originally astronomers ki help ke liye invent hua tha, taaki wo telescope se li gayi noisy measurements se comets aur planets ka smooth orbit path fit kar sakein — bahut pehle, jab computer toh door, "machine learning" ka naam bhi nahi tha.

**Do formulas chahiye:**
- **b (slope)** = "X aur Y kitna saath move karte hain" ko divide karo "X kitna spread out hai" se. Formula mein: har student ke liye (uska x minus average x) ko (uska y minus average y) se multiply karo, sabko add karo, phir (x minus average x) ke square ke total se divide karo.
- **a (intercept)** = average Y minus (b times average X).

**Step-by-step real numbers ke saath:**
1. Average midterm score (x̄) = 72.17. Average final score (ȳ) = 74.
2. Har student ke liye, unka midterm 72.17 se kitna door hai, aur unka final 74 se kitna door hai, dono differences ko multiply karo, aur sab 12 ko add karo. Total aata hai **2004**.
3. Har "midterm 72.17 se kitna door" value ko square karke bhi add karo — yeh aata hai **3445.67**.
4. Divide karo: b = 2004 ÷ 3445.67 = **0.5816**. Yeh slope hai — har extra midterm point ke liye, final score roughly 0.58 points badhta hai.
5. a = 74 − (0.5816 × 72.17) = **32.02**. Yeh intercept hai.
6. Toh formula ban gaya: **Final = 32.02 + 0.5816 × Midterm**.
7. Midterm score 86 ke liye: Final = 32.02 + 0.5816 × 86 = **82.04**.

Maine yeh poori calculation khud independently redo ki (sirf slide pe trust nahi kiya) aur matching numbers aaye poore raaste mein — average, dono sums, slope, intercept, aur final prediction bhi ≈82.05 (0.01 ka farak slide ke average midterm ko 72.17 pe round karne ki wajah se hai, poore 72.1667 ko carry karne ki jagah). Toh yeh worked example sahi hai aur seekhne layak hai.
