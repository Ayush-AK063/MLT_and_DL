# Topic 7: Worked Derivation — Gradient Descent for a Simple Linear Model

Source: Lecture 10 (ES532: Introduction to Deep Learning), slides 24–27 (numbered 27–30 in the printed corner). The differentiation and the final numeric check below were independently re-derived and verified against the slide's own handwritten result.

---

## 1) Technical Explanation

This topic walks through gradient descent end to end on the simplest possible model, in four explicit steps, exactly as the slides lay them out.

**Step 1 — Model equation.** Assume a prediction formula $\hat{y} = mx$ (the slides note this starts as $\hat{y}=mx+c$ with intercept $c$, then simplify by setting $c=0$ for this derivation, leaving a single parameter $m$ to solve for).

**Step 2 — Cost function.** To measure error across $n$ data points:

$$J(m) = \sum_{i=1}^{n} (y_i - m x_i)^2$$

— the familiar sum-of-squared-residuals idea from [[02_Simple_Linear_Regression_Intuition_Home_Price_Example]], written now explicitly as a function of the single parameter $m$.

**Step 3 — Gradient descent update rule:**

$$m_{\text{new}} = m_{\text{old}} - \eta \frac{dJ}{dm}$$

where $\eta$ (the learning rate) is set to $0.01$ in the slide's example — this is exactly the same update-rule *shape* as $\theta = \theta - \eta\nabla_\theta J(\theta)$ from Lecture 0's [[01_What_Is_Gradient_Descent_and_the_Learning_Rate]], just specialized to the single scalar parameter $m$ here.

**Step 4 — A concrete numeric worked example.** The slides use a tiny 2-point dataset:

| $x$ | $y$ |
|---|---|
| 1 | 2 |
| 2 | 4 |

(Note: this is exactly $y = 2x$ with zero noise — every point lies perfectly on a line through the origin, so the "best fit" should recover $m=2$ exactly.)

Substituting into $J(m)$:

$$J(m) = (y_1 - m x_1)^2 + (y_2 - m x_2)^2 = (2-m)^2 + (4-2m)^2$$

**Differentiating** (independently re-derived and verified here, since the slide shows the working but this confirms it's correct):

$$\frac{dJ}{dm} = 2(2-m)(-1) + 2(4-2m)(-2) = -2(2-m) - 4(4-2m)$$
$$= -4+2m-16+8m = 10m-20$$

This matches the slide's own handwritten derivative exactly. **Checking the slide's two annotated points on this line**:
- At $m=0$: $\frac{dJ}{dm} = 10(0)-20 = -20$ — matches the slide's handwritten "$m=0,-20$" note.
- Setting $\frac{dJ}{dm}=0$ to find the minimum: $10m-20=0 \Rightarrow m=2$, and $J(2) = (2-2)^2+(4-4)^2 = 0$ — matches the slide's own "$m=2, J(m)=0$" annotation exactly.

**Why $m=2$ gives exactly zero error**: because this toy dataset was constructed as an exact straight line ($y=2x$) with no noise, the true best-fit slope is exactly recoverable, and the cost function's minimum genuinely reaches zero — this won't generally happen with real, noisy data (like the home-price dataset in [[03_Simple_Linear_Regression_Worked_Example_Verified]], where the minimum cost is some positive number, not zero), but it makes this toy example clean enough to verify the whole gradient-descent-arrives-at-the-right-answer pipeline by hand.

**Generalizing beyond a single parameter**: the slide's final annotation notes that the same idea generalizes from $\min J(m)$ (one parameter) to $\min J(m,b)$ (two parameters, once the intercept is added back in) and, in general, to $\min J(\theta)$ for any parameter vector $\theta$ — exactly the general form from Lecture 9's [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]]. The two-parameter case is worked through fully in [[08_Exercise_Two_Variable_Gradient_Descent_Solved]].

---

## 2) Simple English Explanation

This topic takes the abstract idea of gradient descent and actually grinds through the arithmetic on the simplest model you could pick, step by step.

**The setup**: a prediction rule with just one dial to tune, $\hat{y} = mx$ (a straight line through the origin — no intercept, just a slope). The "how wrong am I" measure is the usual sum-of-squared-errors, written here as a function of just that one dial, $m$: $J(m)$.

**The update rule**: nudge $m$ a little bit in the downhill direction each time — $m_{\text{new}} = m_{\text{old}} - \eta \times (\text{slope of } J \text{ at the current } m)$ — with the nudge size ($\eta$, the learning rate) set to a small number, 0.01, in this example.

**A tiny toy dataset to test it on**: two points, $(1,2)$ and $(2,4)$ — notice these are exactly "$y = 2 \times x$," a perfect, noise-free relationship, so we already know the "right" answer should be $m=2$.

Working out $J(m)$ for these two points and taking its derivative (checked here by hand, and it matches the slide's own working): $\frac{dJ}{dm} = 10m - 20$.

**Testing this formula at two spots**: at $m=0$, the slope of the cost function is $-20$ (steeply downhill — telling you to increase $m$, which makes sense, since $m=0$ predicts a flat line at zero, badly undershooting both real points). Setting the slope to exactly zero (the flattest point, i.e. the minimum) and solving gives $m=2$ — and at $m=2$, the total error $J(m)$ actually comes out to exactly **0**. That's a satisfying confirmation: gradient descent, following this exact slope formula step by step, will correctly walk from any starting $m$ toward $m=2$, the genuinely correct answer for this perfectly clean toy dataset.

**Why zero error is special here, and won't always happen**: this only reaches exactly zero because the toy data was made up to be a perfect straight line with no randomness in it. Real data (like the actual home-price numbers from earlier in this lecture) is noisy, so the best a model can usually do is *minimize* the error, not eliminate it completely — but the mechanics of *how* gradient descent finds that minimum are identical either way.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic gradient descent ke abstract idea ko leta hai aur actually arithmetic ko grind karta hai sabse simple model par, step by step.

**Setup**: ek prediction rule jisme tune karne ke liye sirf ek dial hai, $\hat{y} = mx$ (origin se guzarti ek straight line — koi intercept nahi, bas slope). "Kitna galat hoon" measure wahi usual sum-of-squared-errors hai, yahan sirf us ek dial, $m$, ke function ki tarah likha hua: $J(m)$.

**Update rule**: har baar $m$ ko thoda sa downhill direction mein nudge karo — $m_{\text{new}} = m_{\text{old}} - \eta \times (\text{current } m \text{ par } J \text{ ka slope})$ — nudge size ($\eta$, learning rate) is example mein ek chhota number, 0.01, set hai.

**Test karne ke liye ek chhota toy dataset**: do points, $(1,2)$ aur $(2,4)$ — notice karo ye exactly "$y = 2 \times x$" hai, ek perfect, noise-free relationship, isliye hume pehle se pata hai ki "sahi" answer $m=2$ hona chahiye.

In do points ke liye $J(m)$ nikaal ke aur uska derivative lekar (yahan hand se check kiya, aur ye slide ki apni working se match karta hai): $\frac{dJ}{dm} = 10m - 20$.

**Is formula ko do spots par test karte hai**: $m=0$ par, cost function ka slope $-20$ hai (steeply downhill — tumhe $m$ badhaane ko keh raha hai, jo samajh mein aata hai, kyunki $m=0$ ek flat line predict karta hai zero par, dono real points ko badly undershoot karte hue). Slope ko exactly zero set karna (sabse flat point, matlab minimum) aur solve karna $m=2$ deta hai — aur $m=2$ par, total error $J(m)$ actually exactly **0** aata hai. Ye ek satisfying confirmation hai: gradient descent, is exact slope formula ko step by step follow karte hue, kisi bhi starting $m$ se sahi tarike se $m=2$ ki taraf chalega, jo is perfectly clean toy dataset ka genuinely correct answer hai.

**Zero error yahan special kyun hai, aur hamesha nahi hoga**: ye sirf isliye exactly zero tak pahunchta hai kyunki toy data ko ek perfect straight line bana ke banaya gaya tha, koi randomness ke bina. Real data (jaise is lecture ke earlier wale actual home-price numbers) noisy hota hai, isliye model usually best jo kar sakta hai wo error ko *minimize* karna hai, use completely eliminate karna nahi — lekin gradient descent us minimum ko *kaise* dhoondta hai uska mechanics dono cases mein identical hai.
