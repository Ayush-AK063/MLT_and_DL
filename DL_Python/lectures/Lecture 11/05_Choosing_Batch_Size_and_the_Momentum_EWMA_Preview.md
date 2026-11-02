# Topic 5: Choosing a Batch Size, and a First Look at EWMA

Source: Lecture 11 (ES532: Introduction to Deep Learning), slide 11. Enriched with web research on the standard exponentially weighted moving average (EWMA) framing of momentum.

---

## 1) Technical Explanation

This slide is a transitional one, bridging the mini-batch sizing discussion from [[04_MiniBatching_a_Large_Dataset_Worked_Example]] into the momentum topic that closes out this lecture ([[07_Momentum_Based_MiniBatch_Gradient_Descent]]).

**A practical rule of thumb for choosing between Batch GD and Mini-Batch GD**, based on the size of the training set $m$:

- If $m < 2000$: use **Batch Gradient Descent** (the dataset is small enough that computing the gradient over all of it every step isn't prohibitively expensive, and BGD's extra stability is worth having).
- If $m \geq 2000$: use **Mini-Batch Gradient Descent** instead (past this point, the dataset is large enough that BGD becomes impractically slow, motivating the memory/speed trade-offs covered in [[03_Gradient_Descent_Pseudocode_and_Memory_Motivation]] and [[04_MiniBatching_a_Large_Dataset_Worked_Example]]).

**SGD as a special case of mini-batch size**: the slide notes explicitly that SGD's mini-batch size is "exactly 1" — reinforcing the point made in Lecture 0's [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]] that SGD, Mini-Batch GD, and Batch GD are really all the *same* underlying algorithm, differing only in the batch size parameter: 1 example (SGD), some small number like 1000 (Mini-Batch), or the entire dataset $m$ (Batch).

**Introducing EWMA (Exponentially Weighted Moving Average)**, the mathematical tool underlying Momentum: the slide gives the recursive update

$$w_{\text{new}} = \beta \times w_{\text{old}} + (1-\beta) \times w_{\text{current}}, \qquad \beta \in [0,1]$$

with two worked numeric examples of the weighting: $\beta=0.9$ gives $0.9 w_{\text{old}} + 0.1 w_{\text{current}}$, and $\beta=0.6$ gives $0.6 w_{\text{old}} + 0.4 w_{\text{current}}$. This is the general-purpose "smooth out noisy data by blending in a fraction of the past" formula — applied to gradient updates, it becomes exactly the Momentum optimizer from Lecture 0's [[04_Momentum]] (compare this to $v_t = \gamma v_{t-1} + \eta\nabla_\theta J(\theta)$: the EWMA framing here is the same recursive-blending idea, expressed slightly differently). **Via web research**: a $\beta$ around **0.9** is the standard default recommendation in the field (roughly meaning "average over the last ~10 steps," since $\frac{1}{1-\beta}=10$ when $\beta=0.9$), though it's sometimes tuned anywhere from about 0.8 to 0.999 depending on the problem — higher $\beta$ means the average incorporates more history from further in the past, giving smoother but slower-reacting updates.

**Why this matters directly**: the slide connects this EWMA idea to the **zig-zag noise** visible in [[04_MiniBatching_a_Large_Dataset_Worked_Example]]'s 3D bowl diagram — reducing that zig-zag movement is named explicitly as the motivation for gradient descent Momentum (further described as "EWMA with RMSprop, Adam" in the slide's own annotation — i.e., Momentum, RMSprop, and Adam are all, in one way or another, applications of this same exponential-smoothing idea to the raw, noisy mini-batch gradients).

---

## 2) Simple English Explanation

This slide is a bridge — it wraps up the "how big should my mini-batches be" discussion and starts introducing the mathematical trick behind Momentum, which the rest of this lecture is building toward.

**A simple rule of thumb for picking Batch vs. Mini-Batch GD**: if you have fewer than 2000 training examples, just use plain Batch Gradient Descent — the dataset is small enough that there's no real downside. Once you have 2000 or more examples, switch to Mini-Batch Gradient Descent instead, for all the speed and memory reasons covered in the last two topics.

**A fun fact about SGD**: it's really just Mini-Batch Gradient Descent with the batch size set to exactly 1. So Batch GD, Mini-Batch GD, and SGD aren't three totally separate algorithms — they're the same algorithm with one dial (the batch size) turned to a different value each time: 1 for SGD, some small number (like 1000) for Mini-Batch, or the whole dataset for Batch.

**The math trick behind Momentum, introduced here for the first time**: it's called an "Exponentially Weighted Moving Average" (EWMA) — a general way to smooth out noisy, jumpy data by blending each new value with a fraction of the *previous* smoothed value, instead of trusting each new value completely on its own:

$$\text{new smoothed value} = \beta \times (\text{old smoothed value}) + (1-\beta) \times (\text{current raw value})$$

With $\beta=0.9$, the new value is 90% "trust the past" and 10% "trust what just happened right now" — a common, standard default setting. This exact blending trick, applied to the noisy gradient updates from mini-batch training (the zig-zagging path you saw in the previous topic), is precisely what Momentum, RMSprop, and Adam (all from Lecture 0) are doing under the hood — smoothing out the noise so the overall path toward the minimum is steadier and less jittery.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye slide ek bridge hai — ye "mere mini-batches kitne bade hone chahiye" wali discussion ko wrap up karti hai aur Momentum ke peeche ka mathematical trick introduce karna shuru karti hai, jiski taraf is lecture ka baaki hissa build kar raha hai.

**Batch vs. Mini-Batch GD choose karne ka ek simple rule of thumb**: agar tumhare paas 2000 se kam training examples hai, to bas plain Batch Gradient Descent use karo — dataset itna chhota hai ki koi real downside nahi hai. Ek baar tumhare paas 2000 ya zyada examples hon, to Mini-Batch Gradient Descent par switch kar do, un saare speed aur memory reasons ke liye jo pichle do topics mein cover kiye.

**SGD ke baare mein ek fun fact**: ye actually Mini-Batch Gradient Descent hi hai batch size ko exactly 1 set karke. To Batch GD, Mini-Batch GD, aur SGD teen totally separate algorithms nahi hai — ye same algorithm hai ek dial (batch size) ko har baar alag value pe set karke: SGD ke liye 1, Mini-Batch ke liye koi chhota number (jaise 1000), ya Batch ke liye poora dataset.

**Momentum ke peeche ka math trick, yahan pehli baar introduce**: ise "Exponentially Weighted Moving Average" (EWMA) kehte hai — noisy, jumpy data ko smooth karne ka ek general tarika, har naye value ko *pichle* smoothed value ke ek fraction ke saath blend karke, har naye value par akele completely trust karne ke bajaye:

$$\text{naya smoothed value} = \beta \times (\text{purana smoothed value}) + (1-\beta) \times (\text{current raw value})$$

$\beta=0.9$ ke saath, naya value 90% "past par trust karo" aur 10% "abhi jo hua use trust karo" hai — ek common, standard default setting. Ye exact blending trick, noisy gradient updates par apply kiya hua (mini-batch training se zig-zagging path jo tumne pichle topic mein dekha), exactly wahi hai jo Momentum, RMSprop, aur Adam (sab Lecture 0 se) hood ke neeche kar rahe hai — noise ko smooth karte hue taaki minimum ki taraf overall path steadier aur kam jittery ho.
