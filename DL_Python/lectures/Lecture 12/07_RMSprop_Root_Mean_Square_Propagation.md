# Topic 7: RMSprop — Root Mean Square Propagation

Source: Lecture 12 (ES532: Introduction to Deep Learning), slides 11–12 (title slide plus the slide numbered 33 in the printed corner).

---

## 1) Technical Explanation

This lecture closes by applying the **exact same EWMA tool** derived in [[03_Deriving_the_EWMA_Recurrence]] a **second time** — not to the raw gradient (as Momentum did in [[06_Momentum_Applied_to_Gradient_Descent_Updates]]), but to the **squared** gradient — yielding **RMSprop** (Root Mean Square Propagation), named directly on the slide, with its purpose stated plainly: **"Speedup the Training of Model."**

This is the same algorithm already covered from a different angle in this repo's Lecture 0, [[08_RMSprop]] — that topic focused on RMSprop's historical origin (Geoff Hinton's unpublished Coursera lecture) and its relationship to Adadelta; this lecture instead derives it from scratch as a direct extension of the Momentum/EWMA machinery just built.

**The update rule, exactly as given (for single parameters $W$ and $B$, as the slide explicitly notes)**:

$$W = W - \alpha \cdot \frac{dW}{\sqrt{S_{dW}}+\epsilon}, \qquad B = B - \alpha \cdot \frac{dB}{\sqrt{S_{dB}}+\epsilon}$$

where $S_{dW}$ and $S_{dB}$ are **exponentially weighted averages of the *squared* gradients** — the same EWMA recurrence as before, just applied to $(dW)^2$ and $(dB)^2$ instead of to $dW$ and $dB$ directly:

$$S_{dW} = \beta \cdot S_{dW,\text{prev}} + (1-\beta)\cdot(dW)^2, \qquad S_{dB} = \beta \cdot S_{dB,\text{prev}} + (1-\beta)\cdot(dB)^2$$

$\epsilon = 10^{-8}$ is a small smoothing constant, added specifically to prevent division by zero (matching the $\epsilon$ from Lecture 0's [[06_Adagrad]] and [[08_RMSprop]]).

**The mechanism, made explicit by the slide's own circled annotations**: $\dfrac{dW}{\sqrt{S_{dW}}}\downarrow$ and $\dfrac{dB}{\sqrt{S_{dB}}}\downarrow$ — meaning that as $S_{dW}$ (the running average of squared gradients for that parameter) **grows larger**, the effective step size for that parameter **shrinks**. This is exactly the per-parameter adaptive learning rate mechanism already described in Lecture 0's Adagrad/RMSprop topics: a parameter whose gradients have historically been large and noisy gets automatically **dampened**, while a parameter with small, gentle gradients keeps a relatively larger effective step.

**"Problem of Overshooting," explained with a concrete numeric scenario — genuinely useful, not present in Lecture 0's treatment**: the slide walks through what happens if $S_{dB}$ stays at (or very near) **zero** while the raw gradient $dB$ is large (the slide's example: $dB=10$). Without the $\epsilon$ term, the update would involve dividing by $\sqrt{0}=0$, producing an enormous (technically undefined/infinite) step — the update "shoots up very high." This is exactly *why* $\epsilon$ exists in the formula: it's not just a generic numerical-stability afterthought, but a specific guard against this precise overshooting failure mode, where a parameter that has had a small or zero squared-gradient history suddenly receives one large gradient and would otherwise take a wildly oversized step in response.

**Where this lecture leaves off**: with RMSprop's core update rule and its overshooting-prevention role for $\epsilon$ now derived, but without covering Adam (RMSprop + Momentum combined, already introduced from a different angle in Lecture 0's [[09_Adam]]) — this is a natural candidate for whatever the next lecture in this course turns out to cover, once it's added to this repo.

---

## 2) Simple English Explanation

This lecture wraps up by taking the exact same smoothing trick used for Momentum and applying it a second time, but to a slightly different quantity — giving you **RMSprop**, whose whole point, as the slide puts it directly, is to **"speed up the training of the model."**

**The key twist**: instead of smoothing the raw gradient itself (like Momentum does), RMSprop smooths the **squared** gradient. Squaring throws away the direction/sign information and keeps only the *size* — so this running average, called $S_{dW}$ (or $S_{dB}$ for the bias), is really tracking "how big have this parameter's gradients typically been recently," regardless of which way they've been pointing.

**What that size-tracking buys you**: the update rule divides the current gradient by (roughly) the square root of that running average. That means: if a particular weight's gradients have recently been consistently *large*, its effective step size automatically shrinks (dividing by a big number makes the step smaller) — reining in a parameter that's been jumping around a lot. If a weight's gradients have been small and gentle, its step size stays relatively larger. Each parameter effectively gets its own personalized, self-adjusting step size.

**A concrete "what could go wrong" scenario the slide walks through**: what if that running average of squared gradients happens to sit right at (or very close to) zero, and then suddenly a large gradient shows up? Dividing by a number close to zero produces a *huge* result — the update "shoots up very high," wildly overshooting where it should go. This is exactly why the formula includes a tiny safety number, $\epsilon$ (about 0.00000001) — added to the denominator specifically to stop it from ever getting dangerously close to zero, preventing this overshoot.

**What's left for later**: this lecture stops at RMSprop itself, without going on to combine it with Momentum into Adam (which is a separate algorithm already covered from a different angle back in Lecture 0). That combination is a natural thing to expect in whatever the next lecture in this course turns out to be, once it's added here.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture ek exact same smoothing trick le kar wrap up hoti hai jo Momentum ke liye use hui thi, lekin usse ek thodi alag quantity par apply karte hue — jisse tumhe **RMSprop** milta hai, jiska pura point, jaise slide directly kehti hai, hai model ki training **"speed up"** karna.

**Key twist**: raw gradient ko khud smooth karne ke bajaye (jaise Momentum karta hai), RMSprop **squared** gradient ko smooth karta hai. Square karna direction/sign information phenk deta hai aur sirf *size* rakhta hai — isliye ye running average, jise $S_{dW}$ (ya bias ke liye $S_{dB}$) kehte hai, actually track karta hai "is parameter ke gradients recently typically kitne bade rahe hai," chahe wo kis taraf point kar rahe hon.

**Us size-tracking se kya milta hai**: update rule current gradient ko us running average ke (roughly) square root se divide karta hai. Iska matlab: agar ek particular weight ke gradients recently consistently *bade* rahe hai, uska effective step size automatically shrink ho jaata hai (ek bade number se divide karna step ko chhota banata hai) — ek aise parameter ko control mein rakhte hue jo bahut jump kar raha tha. Agar ek weight ke gradients chhote aur gentle rahe hai, uska step size relatively bada rehta hai. Har parameter ko effectively apna khud ka, personalized, self-adjusting step size milta hai.

**Ek concrete "kya galat ho sakta hai" scenario jo slide walk through karti hai**: kya ho agar squared gradients ka wo running average bilkul zero (ya usse bahut close) par baith jaaye, aur phir achanak ek bada gradient aa jaaye? Zero ke close ek number se divide karna ek *huge* result deta hai — update "shoot up very high" karta hai, wildly overshoot karte hue jahan use jaana chahiye tha. Yahi exact wajah hai ki formula mein ek chhota safety number, $\epsilon$ (lagbhag 0.00000001), include hota hai — denominator mein add kiya jaata hai specifically ise kabhi bhi dangerously zero ke close jaane se rokne ke liye, is overshoot ko prevent karte hue.

**Baad ke liye kya bacha hai**: ye lecture RMSprop tak hi ruk jaati hai, use Momentum ke saath combine karke Adam banane tak nahi jaati (jo ek separate algorithm hai jo already Lecture 0 mein ek alag angle se cover ho chuka). Ye combination is course ki agli lecture mein expect karne layak natural cheez hai, jab bhi wo yahan add hogi.
