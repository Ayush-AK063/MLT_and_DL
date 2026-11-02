# Topic 8: Exercise — Gradient Descent on a Two-Variable Cost Function, Solved

Source: Lecture 10 (ES532: Introduction to Deep Learning), slide 28 (numbered 31 in the printed corner) — posed as an unsolved "Exercise" in the source PDF, giving only the cost function and asking for its two partial derivatives at learning rates $\eta=0.01$ and $\eta=0.1$, with no solution shown. Solved and verified independently below, following the same worked-derivation pattern from [[07_Worked_Derivation_Gradient_Descent_for_Linear_Regression]].

---

## 1) Technical Explanation

**The exercise, exactly as posed**: given the two-parameter cost function

$$J(m,b) = (m+b-5)^2 + (2m-b-1)^2$$

find $\dfrac{\partial J}{\partial m}$ and $\dfrac{\partial J}{\partial b}$, and consider running gradient descent with learning rates $\eta=0.01$ and $\eta=0.1$.

**Step 1 — the partial derivatives** (each treats the other variable as a constant, per the standard rule for partial differentiation):

$$\frac{\partial J}{\partial m} = 2(m+b-5)(1) + 2(2m-b-1)(2) = 2(m+b-5) + 4(2m-b-1)$$
$$= 2m+2b-10+8m-4b-4 = 10m-2b-14$$

$$\frac{\partial J}{\partial b} = 2(m+b-5)(1) + 2(2m-b-1)(-1) = 2(m+b-5) - 2(2m-b-1)$$
$$= 2m+2b-10-4m+2b+2 = -2m+4b-8$$

**Step 2 — finding the exact minimum analytically** (this is the point gradient descent is trying to converge *toward*, iteratively — solving it directly here provides a way to check the iterative process against a known correct answer, the same verification approach used throughout these notes). Setting both partial derivatives to zero simultaneously:

$$10m-2b-14=0 \ \Rightarrow\ 5m-b=7 \quad \text{(i)}$$
$$-2m+4b-8=0 \ \Rightarrow\ -m+2b=4 \ \Rightarrow\ m=2b-4 \quad \text{(ii)}$$

Substituting (ii) into (i): $5(2b-4)-b=7 \Rightarrow 10b-20-b=7 \Rightarrow 9b=27 \Rightarrow b=3$, and then $m=2(3)-4=2$.

**Checking this solution**: at $(m,b)=(2,3)$: $m+b-5 = 2+3-5=0$ and $2m-b-1=4-3-1=0$, so $J(2,3)=0^2+0^2=0$ — both terms hit exactly zero simultaneously, so this is a genuine exact solution, not just a numerical coincidence (this cost function was clearly constructed, like the toy example in [[07_Worked_Derivation_Gradient_Descent_for_Linear_Regression]], so that a perfect zero-error answer exists).

**Step 3 — demonstrating the iterative gradient descent update**, using $m_{\text{new}} = m_{\text{old}} - \eta \frac{\partial J}{\partial m}$ and $b_{\text{new}} = b_{\text{old}} - \eta \frac{\partial J}{\partial b}$ simultaneously each step (the exercise doesn't specify a starting point, so this starts from $m_0=0, b_0=0$ with $\eta=0.1$, purely to illustrate that the update rule actually converges toward the analytical answer found above):

| Step | $m$ | $b$ | $\partial J/\partial m$ | $\partial J/\partial b$ | $m_{\text{new}}$ | $b_{\text{new}}$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | $10(0)-2(0)-14=-14$ | $-2(0)+4(0)-8=-8$ | $0-0.1(-14)=1.40$ | $0-0.1(-8)=0.80$ |
| 1 | 1.40 | 0.80 | $10(1.4)-2(0.8)-14=-1.60$ | $-2(1.4)+4(0.8)-8=-7.60$ | $1.40+0.16=1.56$ | $0.80+0.76=1.56$ |
| 2 | 1.56 | 1.56 | $10(1.56)-2(1.56)-14=-1.52$ | $-2(1.56)+4(1.56)-8=-4.88$ | $1.56+0.152=1.71$ | $1.56+0.488=2.05$ |

After just 3 steps, $(m,b)$ has already moved from $(0,0)$ to roughly $(1.71, 2.05)$ — clearly heading toward the true minimum at $(2,3)$ found analytically above, with the size of each update shrinking as the point gets closer (a direct consequence of the gradient itself shrinking toward zero near the minimum). With enough further steps (or a larger learning rate like $\eta=0.1$ vs. the more cautious $\eta=0.01$ the exercise also mentions — see [[01_What_Is_Gradient_Descent_and_the_Learning_Rate]] from Lecture 0 for the general trade-off between the two), it would continue converging toward $(2,3)$.

---

## 2) Simple English Explanation

This exercise hands you a cost function with **two** dials to tune this time — $m$ and $b$ — instead of the single-dial example from the previous topic, and asks for its two slopes (one for each dial) without giving the answer. This note works through it fully.

**Finding each slope**: to find "how does the cost change if I nudge $m$ a little" (holding $b$ fixed), and separately "how does it change if I nudge $b$ a little" (holding $m$ fixed) — these are called partial derivatives. Working through the algebra carefully gives:

$$\frac{\partial J}{\partial m} = 10m - 2b - 14, \qquad \frac{\partial J}{\partial b} = -2m + 4b - 8$$

**Finding the actual best answer, to check against**: just like with the single-dial example, this cost function was built so that a perfect answer exists — solving both slopes-equal-zero equations together gives $m=2$, $b=3$, and plugging those back in confirms the cost is exactly **0** there. So we now know exactly where gradient descent *should* end up.

**Watching gradient descent actually get there**: starting from $m=0, b=0$ (an arbitrary starting guess, since the exercise doesn't specify one) and taking a few update steps with a learning rate of 0.1, both dials steadily creep toward the target: after 3 steps, $m$ and $b$ have already moved to roughly 1.71 and 2.05 — clearly on their way to the true answer of 2 and 3. Each step's nudge also gets a little smaller as it gets closer, since the slope itself flattens out near the minimum (a pattern you'll see over and over with gradient descent).

**Why bother solving this exactly, and then also doing it step by step?** Because it's a great way to double-check that the gradient descent *mechanism* — repeatedly nudging each parameter opposite to its slope — is genuinely walking toward the right answer, not just trusting the formula on faith. This is exactly the same technique used earlier in this lecture with the simpler one-dial example, just extended to two dials at once, which is exactly what happens in a real neural network with many, many more dials (weights and biases) all being adjusted at the same time.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye exercise tumhe is baar **do** dials tune karne ke liye deti hai — $m$ aur $b$ — pichle topic ke single-dial example ke bajaye, aur bina answer diye uske do slopes (har dial ke liye ek) puchti hai. Ye note ise poori tarah solve karta hai.

**Har slope dhoondhna**: "agar main $m$ ko thoda nudge karun to cost kaise change hoti hai" ($b$ ko fixed rakhte hue), aur alag se "agar main $b$ ko thoda nudge karun to kaise change hoti hai" ($m$ ko fixed rakhte hue) dhoondhne ke liye — inhe partial derivatives kehte hai. Algebra ko carefully work through karne par ye milta hai:

$$\frac{\partial J}{\partial m} = 10m - 2b - 14, \qquad \frac{\partial J}{\partial b} = -2m + 4b - 8$$

**Actual best answer dhoondhna, check karne ke liye**: bilkul single-dial example ki tarah, ye cost function is tarah banaya gaya tha ki ek perfect answer exist kare — dono slopes-equal-zero equations ko saath solve karna $m=2$, $b=3$ deta hai, aur unhe wapas plug karna confirm karta hai ki cost wahan exactly **0** hai. To ab hume exactly pata hai ki gradient descent ko *kahan* end up hona chahiye.

**Gradient descent ko actually wahan pahunchte dekhna**: $m=0, b=0$ se start karke (ek arbitrary starting guess, kyunki exercise koi specify nahi karti) aur 0.1 ki learning rate se kuch update steps lekar, dono dials steadily target ki taraf creep karte hai: 3 steps ke baad, $m$ aur $b$ already lagbhag 1.71 aur 2.05 tak move ho chuke hai — clearly 2 aur 3 ke asli answer ki taraf jaate hue. Har step ka nudge bhi thoda chhota hota jaata hai jaise-jaise wo close hota hai, kyunki slope khud minimum ke paas flatten ho jaata hai (ye pattern tum gradient descent mein baar-baar dekhoge).

**Ise exactly solve karne, aur phir step by step bhi karne ki zaroorat kyun hai?** Kyunki ye double-check karne ka ek achha tarika hai ki gradient descent ka *mechanism* — har parameter ko uske slope ke opposite baar-baar nudge karna — genuinely sahi answer ki taraf chal raha hai, sirf formula par bharosa karne ke bajaye. Ye bilkul wahi technique hai jo is lecture mein pehle simpler one-dial example ke saath use hui thi, bas do dials tak extend ki hui, jo bilkul wahi hai jo real neural network mein hota hai jahan bahut zyada dials (weights aur biases) ek saath adjust ho rahe hote hai.
