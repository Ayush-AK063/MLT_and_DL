# Topic 10: AdaMax and Nadam — Two Extensions of Adam

Source: Lecture 0, Sections 4.7 (AdaMax) and 4.8 (Nadam) of Ruder's overview paper.

---

## 1) Technical Explanation

### AdaMax

In [[09_Adam]], the $v_t$ term scales the gradient inversely proportional to the $\ell_2$ norm of past and current gradients:

$$v_t = \beta_2 v_{t-1} + (1-\beta_2)|g_t|^2$$

This can be generalized to an $\ell_p$ norm (Kingma and Ba, the original Adam authors, parameterize $\beta_2$ as $\beta_2^p$ for this generalization):

$$v_t = \beta_2^p v_{t-1} + (1-\beta_2^p)|g_t|^p$$

Large-$p$ norms are generally numerically unstable, which is why $\ell_1$ and $\ell_2$ are the common practical choices. However, the special case $p \to \infty$ (the $\ell_\infty$, or "infinity," norm) turns out to behave in a particularly **stable** way. Taking this limit, the authors define AdaMax's $u_t$ (renamed to avoid confusion with Adam's $v_t$):

$$u_t = \beta_2^\infty v_{t-1} + (1-\beta_2^\infty)|g_t|^\infty = \max(\beta_2 \cdot v_{t-1}, |g_t|)$$

Plugging this into the Adam update rule in place of $\sqrt{\hat{v}_t} + \epsilon$ gives the **AdaMax update rule**:

$$\theta_{t+1} = \theta_t - \frac{\eta}{u_t}\hat{m}_t$$

Because $u_t$ is defined via a $\max$ operation rather than an accumulating sum, it is **not** biased toward zero the way $m_t$ and $v_t$ in Adam are — so, unlike Adam, **no bias correction is needed for $u_t$**. Good default values: $\eta = 0.002$, $\beta_1 = 0.9$, $\beta_2 = 0.999$.

### Nadam (Nesterov-accelerated Adaptive Moment Estimation)

Adam can be understood as a combination of [[08_RMSprop]] (contributing $v_t$) and [[04_Momentum]] (contributing $m_t$). Since [[05_Nesterov_Accelerated_Gradient]] (NAG) is known to be superior to vanilla Momentum, it's natural to ask: can Adam be combined with NAG instead of plain Momentum? **Nadam** (Dozat, 2016) does exactly this.

The derivation (Dozat's specific reformulation, as walked through step by step in the paper): starting from the vanilla momentum update $m_t = \gamma m_{t-1} + \eta g_t,\ \theta_{t+1} = \theta_t - m_t$, and NAG's modification of it (compute $g_t$ at the look-ahead point $\theta_t - \gamma m_{t-1}$), Dozat proposes an alternative way to add the "look-ahead" property: instead of applying the momentum step twice (once inside the gradient computation, once for the parameter update), apply the **look-ahead momentum vector directly** to the current update:

$$g_t = \nabla_{\theta_t} J(\theta_t), \quad m_t = \gamma m_{t-1} + \eta g_t, \quad \theta_{t+1} = \theta_t - (\gamma m_t + \eta g_t)$$

Notice this uses the **current** momentum vector $m_t$ (not the previous one $m_{t-1}$) to look ahead. Applying the same substitution to Adam's update rule — replacing the bias-corrected estimate of the *previous* momentum vector, $\hat{m}_{t-1}$, with the bias-corrected estimate of the *current* one, $\hat{m}_t$ — and expanding through the algebra (shown in full in the paper) yields the final **Nadam update rule**:

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t}+\epsilon}\left(\beta_1 \hat{m}_t + \frac{(1-\beta_1)g_t}{1-\beta_1^t}\right)$$

Note that $\hat{v}_t$ needs no modification from ordinary Adam — only the momentum term $\hat{m}_t$ is changed to bake in the NAG-style look-ahead correction.

---

## 2) Simple English Explanation

These two algorithms are both small "what if we tweak one ingredient of Adam" experiments.

**AdaMax** asks: "Adam measures how big recent gradients have been using something like a weighted average of their *squares*. What if, instead, we just always used the single **biggest** gradient seen recently (in a fading-memory sense), rather than an average?" It turns out this "just track the max" approach is mathematically a specific limiting case (an "infinity norm") of the more general family Adam belongs to, and it behaves in a numerically well-behaved, stable way. A nice bonus: because it's based on a maximum rather than an accumulating average, it doesn't suffer from the same "started at zero, so early estimates are biased" issue Adam has — so this particular part doesn't need the bias-correction trick at all.

**Nadam** asks: "Adam already borrows the 'building up speed' idea from Momentum — what if we gave it the *smarter*, look-ahead version of that idea instead (NAG, from earlier in this lecture), since NAG is known to be an improvement over plain Momentum?" Nadam works out the math to plug NAG's "peek ahead before committing" trick into Adam's update rule, keeping Adam's per-dial adaptive step-sizing (the $v_t$ part) completely unchanged and only upgrading the momentum part.

Neither of these is a completely new idea — they're both "take Adam, swap out one piece for a slightly smarter version of that piece" — which is a common and useful way research on optimizers has progressed: most of the algorithms in this lecture build directly on the one before it, fixing one specific, identifiable flaw at a time.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye dono algorithms Adam ke "ek ingredient tweak karke dekhte hai" jaise chhote experiments hai.

**AdaMax** puchta hai: "Adam recent gradients kitne bade rahe ye measure karta hai unke *squares* ka ek weighted average use karke. Kya ho agar hum iske bajaye bas hamesha recently dekha gaya sabse **bada** gradient use karein (fading-memory sense mein), average ke bajaye?" Ye "bas max track karo" wala approach mathematically Adam ke bade family ka ek specific limiting case ("infinity norm") nikalta hai, aur ye numerically kaafi stable tarike se behave karta hai. Ek achhi bonus: kyunki ye ek maximum par based hai na ki accumulating average par, isme wo "zero se start hua tha isliye early estimates biased hai" wali problem nahi aati jo Adam mein thi — isliye is particular part ko bias-correction trick ki zaroorat hi nahi padti.

**Nadam** puchta hai: "Adam already Momentum se 'speed build up karna' wala idea borrow karta hai — kya ho agar hum use uska *smarter*, look-ahead version dein (NAG, jo pehle is lecture mein padha), kyunki NAG plain Momentum se better hai?" Nadam math nikal ke NAG ka "commit karne se pehle peek ahead karo" trick Adam ke update rule mein fit karta hai, Adam ka per-dial adaptive step-sizing (jo $v_t$ wala part hai) bilkul same rakhte hue, sirf momentum wale part ko upgrade karte hue.

In dono mein se koi bhi bilkul nayi idea nahi hai — dono "Adam lo, ek piece ko uske thode smarter version se replace karo" jaise hai — jo optimizers ki research aage badhne ka ek common aur useful tarika hai: is lecture ke zyadatar algorithms seedhe pichle wale par build karte hai, ek time pe ek specific, identifiable flaw fix karte hue.
