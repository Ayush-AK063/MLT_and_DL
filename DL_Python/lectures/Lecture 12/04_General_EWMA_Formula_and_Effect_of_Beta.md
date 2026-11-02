# Topic 4: The General EWMA Formula, and What Beta Controls

Source: Lecture 12 (ES532: Introduction to Deep Learning), slide 8 (numbered 23 in the printed corner).

---

## 1) Technical Explanation

Generalizing the term-by-term expansion from [[03_Deriving_the_EWMA_Recurrence]] ($V_1, V_2, V_3, V_4$) into a single closed-form expression for any $t$:

$$V_t = (1-\beta)\left[\theta_t + \beta\theta_{t-1} + \beta^2\theta_{t-2} + \beta^3\theta_{t-3} + \cdots + \beta^{t-1}\theta_1 + \beta^t\theta_0\right], \qquad 0 < \beta < 1$$

This is exactly the pattern already verified inductively in [[03_Deriving_the_EWMA_Recurrence]] — the coefficient on the data point from $k$ steps ago is $(1-\beta)\beta^k$.

**What happens as $t$ grows large**: the slide notes that "if $t$ is high enough," then $\beta^t \approx 0$. This is a direct consequence of $0<\beta<1$: raising a fraction to a large power drives it toward zero. **Verifying this concretely**: for $\beta=0.9$ and $t=50$, $\beta^t = 0.9^{50} \approx 0.00515$ — already less than 1% of its starting weight; by $t=100$, $0.9^{100}\approx0.0000266$, essentially negligible. This confirms the slide's stated conclusion: the **earliest** data points (like $\theta_0$, with coefficient $\beta^t$) end up contributing an amount that shrinks toward nothing as more steps accumulate — i.e., very old data effectively "falls out" of the average on its own, without needing to be explicitly discarded.

**The direct consequence for weighting, restated**: **lower weight → older data points**; **higher weight → newer data points** — exactly the exponential-decay-with-age property already established in the previous topic.

**Connecting $\beta$ to smoothness, and back to the Momentum motivation**: the slide's final line ties this directly back to the original goal from [[01_Momentum_Update_Rule_BGD_vs_MBGD_Paths]]: **"Smoother → increase Horizontal movement."** A larger $\beta$ means the average incorporates a longer effective history (more past terms with non-negligible weight before $\beta^k$ decays away), which produces a **smoother** curve — and in the context of gradient descent, a smoother update direction means more of the *consistent*, genuinely-useful (horizontal, toward-the-minimum) component of the movement survives the averaging, while the *inconsistent*, oscillating (vertical, back-and-forth) component keeps cancelling itself out. This is precisely the mechanism, now expressed with an actual formula, behind the "increase horizontal / reduce vertical movement" goal stated (without the underlying math) back in Lecture 11's [[07_Momentum_Based_MiniBatch_Gradient_Descent]].

---

## 2) Simple English Explanation

This topic writes out the general version of the pattern the previous topic found by hand — instead of working out $V_1$, then $V_2$, then $V_3$ one at a time, here's the formula for *any* step $t$ all at once: it's a weighted blend of every data point ever seen, where each one's weight shrinks the further back in time it was, following the $(1-\beta)\beta^{\text{age}}$ pattern already worked out.

**A neat consequence, checked with real numbers**: since $\beta$ is a fraction less than 1, raising it to a high power makes it shrink toward zero — quickly. For example, with $\beta=0.9$: after just 50 steps, $\beta^{50}$ has already shrunk to about half a percent of its original size; after 100 steps, it's essentially zero. In plain terms: **really old data points naturally fade out of the average almost completely on their own** — you don't have to do anything special to "forget" them, the math does it for you automatically.

**Connecting this back to why we're doing all this in the first place**: the slide sums up the payoff in one line — a bigger $\beta$ means a *smoother* average (since it blends in more history before that history fades away), and a smoother average means more of the genuinely useful, consistently-downhill part of your gradient updates survives, while the random back-and-forth noise keeps cancelling itself out. This is the actual mathematical reason behind the "more horizontal movement, less vertical wobble" goal that Lecture 11 described only in pictures — now you have the formula that actually makes it happen.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic pichle topic ne jo pattern hand se dhoondha tha uska general version likhta hai — $V_1$, phir $V_2$, phir $V_3$ ek-ek karke work out karne ke bajaye, yahan *kisi bhi* step $t$ ke liye ek saath formula hai: ye ab tak dekhe gaye har data point ka ek weighted blend hai, jahan har ek ka weight utna hi shrink hota hai jitna wo time mein peeche hai, us $(1-\beta)\beta^{\text{age}}$ pattern ko follow karte hue jo already work out ho chuka.

**Ek neat consequence, real numbers se check kiya**: kyunki $\beta$ 1 se kam ka ek fraction hai, use high power tak raise karna use zero ki taraf shrink karta hai — jaldi. Jaise, $\beta=0.9$ ke saath: bas 50 steps ke baad, $\beta^{50}$ already apne original size ka lagbhag half percent tak shrink ho chuka hai; 100 steps ke baad, ye essentially zero hai. Simple shabdon mein: **bahut purane data points naturally average se almost completely apne aap fade out ho jaate hai** — unhe "bhoolne" ke liye tumhe kuch special karne ki zaroorat nahi, math ye tumhare liye automatically kar deta hai.

**Ise wapas connect karna ki hum ye sab pehli jagah kyun kar rahe hai**: slide payoff ko ek line mein summarize karti hai — ek bada $\beta$ ka matlab hai ek *smoother* average (kyunki ye us history fade hone se pehle usme se zyada blend karta hai), aur ek smoother average ka matlab hai ki tumhare gradient updates ka genuinely useful, consistently-downhill part zyada survive karta hai, jabki random back-and-forth noise apne aap cancel hota rehta hai. Yahi actual mathematical wajah hai us "zyada horizontal movement, kam vertical wobble" wale goal ke peeche jo Lecture 11 ne sirf pictures mein describe kiya tha — ab tumhare paas wo formula hai jo ise actually hone deta hai.
