# Topic 3: Deriving the EWMA Recurrence, Step by Step

Source: Lecture 12 (ES532: Introduction to Deep Learning), slide 7 (numbered 22 in the printed corner). The unrolled expansion below was independently re-derived and verified term by term against the slide's own working.

---

## 1) Technical Explanation

**The EWMA recurrence, as defined on the slide**:

$$V_t = \beta \times V_{t-1} + (1-\beta) \times \theta_t, \qquad 0 < \beta < 1$$

with each term labeled directly: $V_t$ is the **average at timestep $t$**; $V_{t-1}$ is the **average at $(t-1)$ time** (the "previous average"); $\beta$ is a **hyperparameter**; $\theta_t$ is the **current data point** at time $t$.

**A discrepancy in the slide's own initialization, worth flagging and resolving**: the slide's first (black) annotation states $V_0 = \theta$, but its own subsequent worked-out expansion (in red, alongside) is only internally consistent if $V_0 = 0$. Re-deriving the unrolled recursion from $V_0=0$ term by term (independently verified here):

$$V_1 = \beta V_0 + (1-\beta)\theta_1 = \beta(0) + (1-\beta)\theta_1 = (1-\beta)\theta_1$$
$$V_2 = \beta V_1 + (1-\beta)\theta_2 = \beta(1-\beta)\theta_1 + (1-\beta)\theta_2 = (1-\beta)[\theta_2 + \beta\theta_1]$$
$$V_3 = \beta V_2 + (1-\beta)\theta_3 = (1-\beta)[\theta_3 + \beta\theta_2 + \beta^2\theta_1]$$
$$V_4 = \beta V_3 + (1-\beta)\theta_4 = (1-\beta)[\theta_4 + \beta\theta_3 + \beta^2\theta_2 + \beta^3\theta_1]$$

Every one of these matches the slide's own red-annotated expansion exactly, confirming $V_0=0$ (not $\theta$) is the initialization actually used throughout the rest of the derivation — the initial "$V_0=\theta$" note is best read as an early, uncorrected first pass that the slide's own later working supersedes.

**The pattern this reveals**: at each successive step, the **most recent** data point ($\theta_t$) gets the largest individual weight, $(1-\beta)$, while each older data point $\theta_{t-k}$ gets weight $(1-\beta)\beta^k$ — shrinking **geometrically** (exponentially) with how far back in time it is. This is exactly why it's called an *exponentially* weighted average: the weighting of past data points decays exponentially, not linearly, with age — matching the slide's own note that $\beta^3 < \beta^2 < \beta^1 < \beta^0$ (since $0<\beta<1$), meaning **older data points systematically receive lower weight**.

**A genuinely important gap in this derivation, not mentioned on the slide (via web research)**: initializing $V_0=0$ causes a well-known **bias toward zero** in the earliest few steps of the average, since $V_1 = (1-\beta)\theta_1$ is a severe underestimate of $\theta_1$ itself whenever $\beta$ is close to 1 (e.g. at $\beta=0.9$, $V_1$ is only 10% of $\theta_1$). The standard fix, **bias correction** — dividing $V_t$ by $(1-\beta^t)$ — is exactly the technique already covered in this repo's Lecture 0, [[09_Adam]] (Adam's $\hat{m}_t = m_t/(1-\beta_1^t)$), where the same $V_0=0$-initialization bias is corrected explicitly. **This lecture's derivation does not include or mention this correction anywhere** — a real gap worth being aware of: the raw EWMA formula as presented here will systematically underestimate the true recent average during its first several steps, exactly the flaw Adam's bias-correction step was specifically designed to fix.

---

## 2) Simple English Explanation

This topic takes the EWMA idea from the previous topic and works out its actual formula, step by step, checking every line of the math along the way.

**The formula**: each new smoothed value is a blend — mostly the previous smoothed value, plus a small dose of the newest raw data point:

$$V_t = \beta \times V_{t-1} + (1-\beta) \times \theta_t$$

**A small mix-up in the slide worth pointing out**: the slide first says the starting value $V_0$ equals $\theta$ (the very first data point), but if you actually work through its own later math, that only makes sense if $V_0$ starts at **0** instead. Redoing the unrolling by hand from $V_0=0$ (checked here, line by line) exactly matches everything else on the slide — so $V_0=0$ is clearly the version that was actually meant and used, and the earlier "$V_0=\theta$" note looks like a rough first draft that got left in.

**What the unrolled math reveals**: if you keep expanding the formula, you find that the newest data point always gets the biggest individual weight, and every older data point gets a smaller weight than the one after it — shrinking exponentially fast the further back you go. That's literally what "exponentially weighted" means in the name: old information doesn't get thrown away completely, but it fades out fast and predictably.

**A real gap in this lecture's coverage, worth knowing about**: starting the average at exactly 0 causes a well-known problem — during the very first few steps, the smoothed value badly *underestimates* the true recent trend (since it's still "remembering" that fake starting value of 0). There's a standard fix for this called **bias correction**, which this lecture never mentions — but it's exactly the same fix already covered back in Lecture 0 when Adam was introduced ([[09_Adam]]), where dividing by a correction factor fixes precisely this early-steps underestimate. Worth keeping in mind: the plain formula on this slide has that flaw baked in, uncorrected.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic pichle topic wala EWMA idea leta hai aur uska actual formula step by step work out karta hai, raaste mein math ki har line check karte hue.

**Formula**: har naya smoothed value ek blend hai — zyadatar purana smoothed value, plus newest raw data point ki thodi si dose:

$$V_t = \beta \times V_{t-1} + (1-\beta) \times \theta_t$$

**Slide mein ek chhota mix-up point out karne layak**: slide pehle kehti hai ki starting value $V_0$ equal $\theta$ hai (bilkul pehla data point), lekin agar tum uski apni baad ki math actually work through karo, to ye sirf tab samajh mein aata hai jab $V_0$ **0** se start ho. $V_0=0$ se unrolling ko hand se dobara karna (yahan check kiya, line by line) slide par baaki sab kuch se exactly match karta hai — to $V_0=0$ clearly wo version hai jo actually intended aur use kiya gaya tha, aur earlier wala "$V_0=\theta$" note ek rough first draft jaisa lagta hai jo reh gaya.

**Unrolled math kya reveal karta hai**: agar tum formula ko expand karte raho, to tumhe milega ki newest data point ko hamesha sabse bada individual weight milta hai, aur har purana data point us se pichle wale se chhota weight paata hai — jitna zyada peeche jaate ho, exponentially fast shrink hota hai. Yahi literally matlab hai naam mein "exponentially weighted" ka: purani information poori tarah discard nahi hoti, lekin ye fast aur predictably fade out hoti hai.

**Is lecture ki coverage mein ek real gap, jaanna zaroori hai**: average ko exactly 0 se start karna ek well-known problem create karta hai — bilkul pehle kuch steps mein, smoothed value asli recent trend ko badly *underestimate* karta hai (kyunki wo abhi bhi us fake starting value 0 ko "yaad rakh raha" hai). Iska ek standard fix hai jise **bias correction** kehte hai, jo ye lecture kabhi mention nahi karti — lekin ye bilkul wahi fix hai jo Lecture 0 mein Adam introduce karte time already cover ho chuka ([[09_Adam]]), jahan ek correction factor se divide karna exactly is early-steps underestimate ko fix karta hai. Yaad rakhna: is slide ka plain formula mein ye flaw uncorrected baked in hai.
