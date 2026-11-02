# Topic 6: Adagrad

Source: Lecture 0, Section 4.3 (Adagrad) of Ruder's overview paper.

---

## 1) Technical Explanation

Momentum and NAG solve the problem of adapting updates to the **slope** of the error surface, and speed up SGD as a whole. **Adagrad** (Duchi et al., 2011) tackles a *different* problem: adapting the update to **each individual parameter**, giving important-but-rare parameters bigger updates and frequent parameters smaller ones.

Let $g_{t,i} = \nabla_\theta J(\theta_{t,i})$ be the gradient of the objective w.r.t. parameter $\theta_i$ at time step $t$. The plain SGD update for parameter $i$ is:

$$\theta_{t+1,i} = \theta_{t,i} - \eta \cdot g_{t,i}$$

Adagrad instead modifies the learning rate **per parameter, per time step**, based on the history of gradients seen so far for that specific parameter:

$$\theta_{t+1,i} = \theta_{t,i} - \frac{\eta}{\sqrt{G_{t,ii} + \epsilon}} \cdot g_{t,i}$$

where $G_t \in \mathbb{R}^{d \times d}$ is a diagonal matrix whose $i$-th diagonal entry is the **sum of the squares of all past gradients** for parameter $\theta_i$ up to time $t$, and $\epsilon$ is a tiny smoothing constant (around $10^{-8}$) that just prevents division by zero. Vectorized, using element-wise operations:

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t + \epsilon}} \odot g_t$$

**Effect**: a parameter that has received large gradients repeatedly (a frequent, well-explored parameter) accumulates a large $G_{t,ii}$, which **shrinks** its effective learning rate. A parameter that rarely gets a gradient at all (a rare feature) accumulates a small $G_{t,ii}$, so its effective learning rate stays close to $\eta$ — it gets a comparatively **larger** update whenever it does show up. This is exactly the fix for Challenge 3 in [[03_Challenges_in_Gradient_Descent_Optimization]].

**Real-world validation cited in the paper**: Dean et al. (2012) found Adagrad greatly improved SGD's robustness and used it to train large-scale neural nets at Google — including a famous system that learned to recognize cats from unlabeled YouTube video frames. Pennington et al. (2014) used Adagrad to train **GloVe** word embeddings, precisely because infrequent words in a text corpus need much larger updates than very frequent ones (e.g., "the" vs. a rare technical term) — a textbook case of the sparse-data scenario Adagrad is designed for.

**Main benefit**: eliminates the need to manually tune the learning rate — most implementations just default $\eta = 0.01$ and leave it there.

**Main weakness**: $G_t$ only ever **accumulates** (every added term $g_{t,i}^2$ is positive, so it never shrinks). This means the effective learning rate **monotonically decreases** over the whole course of training and eventually becomes infinitesimally small — at which point the parameter essentially stops learning anything new, even if it hasn't actually converged. This specific flaw is exactly what motivates the next two algorithms, [[07_Adadelta]] and [[08_RMSprop]].

---

## 2) Simple English Explanation

Previous ideas (Momentum, NAG) were about the *shape of the terrain* — steep vs. shallow directions. Adagrad is about something different: **not every dial (parameter) should get the same-size nudge.**

Imagine you're adjusting hundreds of dials to tune a machine. Some dials are for common, frequently-relevant settings — you end up nudging them constantly. Others are for rare, specialized settings that only matter occasionally — you barely ever touch them. If you gave every dial the exact same-size nudge each time, the rarely-touched dials would take forever to reach a good setting, since they only get a handful of chances.

**Adagrad's fix**: it keeps a running tally, for every single dial separately, of how much total "nudging energy" that dial has already received (technically, the sum of squared gradients). A dial that's been nudged a lot gets a **smaller** effective nudge size going forward (it's already been well-adjusted, so be gentler). A dial that's barely been touched keeps a **larger** effective nudge size (it needs to catch up).

This turned out to be genuinely useful for real systems — Google used it to train large neural networks (including one that famously learned to spot cats in YouTube videos on its own), and it was used to train GloVe, a well-known word-embedding technique, exactly because rare words need much bigger updates than extremely common words like "the" or "and."

**The catch**: because Adagrad's running tally only ever grows (you can never "undo" past nudging energy), every dial's effective nudge size keeps shrinking forever, the longer training goes on. Eventually it shrinks so much that the dial basically freezes and stops learning anything new — even if it hasn't actually reached its best setting yet. This is the exact flaw that the next two topics, Adadelta and RMSprop, were invented to fix.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Pichhle ideas (Momentum, NAG) terrain ke *shape* ke baare mein the — steep vs. shallow directions. Adagrad kuch alag baat karta hai: **har dial (parameter) ko same-size nudge nahi milna chahiye.**

Socho tum sainkdo dials adjust kar rahe ho ek machine tune karne ke liye. Kuch dials common, frequently-relevant settings ke liye hai — unhe tum baar-baar nudge karte ho. Kuch dials rare, specialized settings ke liye hai jo sirf kabhi-kabhi matter karti hai — unhe tum shaayad hi touch karte ho. Agar tum har dial ko exact same-size nudge do har baar, to jo dials kam touch hote hai wo achhi setting tak pahunchne mein bahut time lenge, kyunki unhe sirf handful chances milte hai.

**Adagrad ka fix**: ye har ek dial ke liye alag se ek running tally rakhta hai ki us dial ko ab tak kitni total "nudging energy" mil chuki hai (technically, past gradients ka square sum). Jo dial bahut nudge ho chuka hai, use aage se **chhota** effective nudge milta hai (wo already well-adjusted hai, isliye gentle raho). Jo dial shaayad hi touch hua hai, use **bada** effective nudge milta rehta hai (use catch up karna hai).

Ye real systems mein genuinely useful nikla — Google ne isse bade neural networks train kiye (including ek jisne famously YouTube videos mein khud se billiyan pehchanna seekh liya), aur GloVe (ek well-known word-embedding technique) train karne mein bhi use hua, exactly isliye kyunki rare words ko "the" ya "and" jaise bahut common words ke comparison mein bahut zyada bade updates chahiye hote hai.

**Catch ye hai**: kyunki Adagrad ka running tally sirf badhta hi jaata hai (tum past nudging energy ko kabhi "undo" nahi kar sakte), har dial ka effective nudge size training jitni lambi chalti hai utna shrink hota jaata hai. Eventually ye itna shrink ho jaata hai ki dial lagbhag freeze ho jaata hai aur naya kuch seekhna band kar deta hai — chahe wo abhi apni best setting tak pahuncha bhi na ho. Yahi exact flaw hai jise fix karne ke liye agle do topics, Adadelta aur RMSprop, banaye gaye the.
