# Topic 6: Applying EWMA to Gradient Descent — The Full Momentum Update Rule

Source: Lecture 12 (ES532: Introduction to Deep Learning), slide 10 (numbered **30** in the printed corner — another slide-number gap, noted below).

---

## 1) Technical Explanation

**Another gap in the source slides**: this slide is numbered 30, following directly after the previous topic's slide 28 — meaning **slide 29 is also missing** from this deck (in addition to the earlier 24–27 gap flagged in [[05_Comparing_Different_Beta_Values_Worked_Example]]). Flagged here for the same reason: nothing is reconstructed or guessed for the missing slide.

**The content on this slide finally assembles the pieces from every earlier topic in this lecture into the complete Momentum-based gradient descent update rule.**

**Step 1 — recall the plain (non-momentum) update rule**, for a single-parameter case ($W$ = a weight, $B$ = a bias):

$$W = W - \alpha \frac{\partial \text{cost}}{\partial W}, \qquad B = B - \alpha \frac{\partial \text{cost}}{\partial B}$$

**Step 2 — replace the raw gradient with its EWMA-smoothed version.** The slide labels the raw partial derivatives as $dW = \frac{\partial \text{cost}}{\partial W}$ and $dB = \frac{\partial \text{cost}}{\partial B}$, and defines their EWMA-smoothed counterparts, $V_{dW}$ and $V_{dB}$, using exactly the recurrence derived in [[03_Deriving_the_EWMA_Recurrence]] and [[04_General_EWMA_Formula_and_Effect_of_Beta]], applied here specifically to the gradients:

$$V_{dW_t} = \beta \cdot V_{dW_{t-1}} + (1-\beta) \cdot dW, \qquad V_{dB_t} = \beta \cdot V_{dB_{t-1}} + (1-\beta) \cdot dB$$

**Step 3 — the full Momentum update rule**, running for $t$ iterations:

$$W = W - \alpha \cdot V_{dW}, \qquad B = B - \alpha \cdot V_{dB}$$

**Reconciling this with Lecture 0's Momentum formula — a genuinely useful thing to check, since the two look different at first glance**: Lecture 0's [[04_Momentum]] wrote the update as $v_t = \gamma v_{t-1} + \eta\nabla_\theta J(\theta)$, $\theta = \theta - v_t$ — where the learning rate $\eta$ is baked directly **inside** the exponential average itself. This lecture's version keeps the smoothing ($V_{dW}$) and the learning rate ($\alpha$) **separate**, applying $\alpha$ only in the final update step. These are **not identical formulas**, but they express the same underlying idea (a decaying average of past gradients, used to smooth the update direction) with the learning rate factored differently — this lecture's version is closer to how the momentum-with-EWMA framing is taught in, e.g., Andrew Ng's Deep Learning Specialization, while Lecture 0's version follows the more common notation used in Ruder's overview paper and most deep learning library implementations. **The practical takeaway**: don't be confused if different sources write Momentum's formula slightly differently — the core mechanism (blend the current gradient with a decaying memory of past gradients, then step in that blended direction) is the same either way; only the exact placement of the learning rate constant differs, which just rescales the effective step size by a constant factor.

**The accompanying contour diagram**, again showing a zig-zag path — this is the same visual motif reused throughout this lecture and Lecture 11, reinforcing that this final formula is the precise mathematical answer to the "increase horizontal / reduce vertical movement" goal stated informally back in Lecture 11's [[07_Momentum_Based_MiniBatch_Gradient_Descent]].

---

## 2) Simple English Explanation

**A quick note on the source material**: this slide jumps from slide 28 (the previous topic) straight to slide 30 — meaning slide 29 is also missing from this deck, on top of the earlier gap already flagged. As before, nothing is invented to fill that gap.

**What this slide actually does**: it finally puts every ingredient from this lecture together into the complete, real formula for Momentum.

**Step 1**: start with the plain gradient descent update you already know — new weight = old weight minus (learning rate × raw gradient).

**Step 2**: instead of using that raw, noisy gradient directly, first run it through the EWMA smoothing formula from earlier in this lecture — giving you a smoothed version of the gradient, called $V_{dW}$ (and $V_{dB}$ for the bias).

**Step 3**: use *that smoothed version* in the update instead of the raw gradient:

$$\text{new } W = \text{old } W - (\text{learning rate}) \times V_{dW}$$

**A genuinely useful thing worth clearing up**: this looks a little different from the Momentum formula you saw way back in Lecture 0 — there, the learning rate was baked directly into the smoothing step itself, whereas here it's kept separate and only applied at the very end. Don't let that throw you off: both versions are doing the exact same core thing (blend the newest gradient with a fading memory of past gradients, then move in that blended direction) — they've just organized where the learning rate multiplication happens slightly differently, which different textbooks and courses do differently. The underlying idea is identical either way.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Source material par ek quick note**: ye slide 28 (pichla topic) se seedha 30 pe jump karti hai — matlab slide 29 bhi is deck se missing hai, us earlier gap ke upar jo already flag ho chuka. Pehle ki tarah, us gap ko fill karne ke liye kuch invent nahi kiya gaya.

**Ye slide actually kya karti hai**: ye finally is lecture ka har ingredient saath mein daal kar Momentum ka complete, real formula deti hai.

**Step 1**: plain gradient descent update se start karo jo tum already jaante ho — naya weight = purana weight minus (learning rate × raw gradient).

**Step 2**: us raw, noisy gradient ko direct use karne ke bajaye, pehle use is lecture ke earlier wale EWMA smoothing formula se guzaro — jisse tumhe gradient ka ek smoothed version milta hai, jise $V_{dW}$ kehte hai (aur bias ke liye $V_{dB}$).

**Step 3**: update mein raw gradient ke bajaye *wo smoothed version* use karo:

$$\text{naya } W = \text{purana } W - (\text{learning rate}) \times V_{dW}$$

**Ek genuinely useful cheez jise clear karna zaroori hai**: ye thoda alag dikhta hai us Momentum formula se jo tumne bahut pehle Lecture 0 mein dekha tha — wahan, learning rate directly smoothing step ke andar hi baked in thi, jabki yahan ye separate rakhi gayi hai aur sirf bilkul end mein apply hoti hai. Isse confuse mat hone do: dono versions exact same core kaam kar rahe hai (newest gradient ko past gradients ki ek fading memory ke saath blend karo, phir us blended direction mein move karo) — bas unhone learning rate multiplication kahan hoti hai wo thoda alag organize kiya hai, jo alag-alag textbooks aur courses alag-alag karte hai. Underlying idea dono mein identical hai.
