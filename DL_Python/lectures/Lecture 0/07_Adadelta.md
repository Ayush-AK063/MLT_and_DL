# Topic 7: Adadelta

Source: Lecture 0, Section 4.4 (Adadelta) of Ruder's overview paper.

---

## 1) Technical Explanation

**Adadelta** (Zeiler, 2012) is an extension of [[06_Adagrad]] designed specifically to fix Adagrad's one big weakness: its aggressive, **monotonically decreasing** learning rate that eventually shrinks to almost nothing.

Instead of accumulating **all** past squared gradients forever (as Adagrad does), Adadelta restricts this to a **decaying average** over a fixed-size window $w$ — but rather than literally storing $w$ past squared gradients (inefficient), it's implemented recursively as an exponentially decaying average:

$$E[g^2]_t = \gamma E[g^2]_{t-1} + (1-\gamma) g_t^2$$

$\gamma$ plays a role similar to the momentum term, usually set around **0.9**. Rewriting vanilla SGD in terms of a parameter update vector $\Delta\theta_t$ (for clarity):

$$\Delta\theta_t = -\eta \cdot g_{t,i}, \qquad \theta_{t+1} = \theta_t + \Delta\theta_t$$

Adagrad's update vector, in this notation, is $\Delta\theta_t = -\frac{\eta}{\sqrt{G_t + \epsilon}} \odot g_t$. Replacing the ever-growing $G_t$ with the decaying average $E[g^2]_t$ gives:

$$\Delta\theta_t = -\frac{\eta}{\sqrt{E[g^2]_t + \epsilon}} g_t = -\frac{\eta}{RMS[g]_t} g_t$$

(the denominator is just the **root mean squared** — RMS — of the gradient, hence the shorthand notation).

**A second, more subtle fix**: the paper's authors noted that the *units* of this update don't actually match physically — the update to $\theta$ should have the same hypothetical units as $\theta$ itself, but $\frac{\eta}{RMS[g]_t} g_t$ doesn't satisfy that (this holds for SGD, Momentum, and Adagrad too, not just this intermediate version of Adadelta). To fix this, they define a **second** exponentially decaying average — this time of the squared **parameter updates** themselves, not the gradients:

$$E[\Delta\theta^2]_t = \gamma E[\Delta\theta^2]_{t-1} + (1-\gamma)\Delta\theta_t^2$$

giving $RMS[\Delta\theta]_t = \sqrt{E[\Delta\theta^2]_t + \epsilon}$. Since $RMS[\Delta\theta]_t$ isn't known yet at the current step (it depends on the very update being computed), it's approximated using the RMS of updates up to the **previous** step, $RMS[\Delta\theta]_{t-1}$. Substituting this in place of the learning rate $\eta$ finally gives the **Adadelta update rule**:

$$\Delta\theta_t = -\frac{RMS[\Delta\theta]_{t-1}}{RMS[g]_t} g_t, \qquad \theta_{t+1} = \theta_t + \Delta\theta_t$$

**The headline result**: with Adadelta, you don't even need to set a default learning rate $\eta$ at all — it has been eliminated entirely from the final update rule, replaced by the ratio of two RMS quantities the algorithm tracks on its own.

---

## 2) Simple English Explanation

Adagrad had one real problem: its memory of "how much this dial has been nudged" **never forgets anything**, so eventually every dial's effective nudge size shrinks to basically zero and learning grinds to a halt.

**Adadelta's fix is simple in spirit: give it a short-term memory instead of a lifetime memory.** Instead of remembering *everything* that's ever happened to a dial, it only really "remembers" a recent, fading window of history — recent nudges count a lot, nudges from way back barely count at all anymore. This is done with a mathematical trick called an "exponentially decaying average," which is just a smooth, efficient way to say "mostly care about the recent past, and let the old past quietly fade out" without literally having to store a long list of old values.

There's also a second, more technical fix in the same spirit: the algorithm also keeps a similar fading memory of *how big its own past adjustments have been*, and uses that to figure out an appropriate step size on its own — which means, remarkably, **you don't even need to hand-pick a learning rate for Adadelta at all**. It works out a sensible step size from its own recent history of gradients and updates.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Adagrad mein ek real problem thi: "ye dial kitna nudge ho chuka hai" ki iski memory **kabhi kuch bhoolti nahi**, isliye eventually har dial ka effective nudge size lagbhag zero ho jaata hai aur learning ruk jaati hai.

**Adadelta ka fix simple hai: usse lifetime memory ki jagah short-term memory do.** Har cheez jo kabhi hui hai use yaad rakhne ke bajaye, ye sirf ek recent, fade hoti hui window ki history "yaad" rakhta hai — recent nudges bahut matter karte hai, bahut purane nudges lagbhag matter hi nahi karte. Ye ek mathematical trick se hota hai jise "exponentially decaying average" kehte hai — ye bas ek smooth, efficient tarika hai ye kehne ka ki "zyadatar recent past ki parwaah karo, aur purane past ko quietly fade out hone do" bina literally purani values ki ek lambi list store kiye.

Ek aur, zyada technical fix bhi isi spirit mein hai: algorithm apne khud ke past adjustments kitne bade the, uski bhi ek similar fading memory rakhta hai, aur usse use karke khud hi ek appropriate step size nikaal leta hai — jiska matlab hai, remarkably, **Adadelta ke liye tumhe learning rate hand-pick karne ki zaroorat hi nahi hai.** Ye apne recent gradients aur updates ki history se khud ek sensible step size nikaal leta hai.
