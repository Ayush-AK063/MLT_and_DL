# Topic 8: RMSprop

Source: Lecture 0, Section 4.5 (RMSprop) of Ruder's overview paper.

---

## 1) Technical Explanation

**RMSprop** is an **unpublished** adaptive learning-rate method — it was never formally published as a paper, but instead proposed by **Geoff Hinton** in Lecture 6e of his Coursera "Neural Networks for Machine Learning" course. Despite never being a peer-reviewed publication, it became (and remains) one of the most widely used optimizers in deep learning, precisely because it is simple and works well.

RMSprop and [[07_Adadelta]] were developed **independently, around the same time**, both aiming to resolve exactly the same flaw: Adagrad's radically and permanently diminishing learning rate. In fact, RMSprop turns out to be **mathematically identical** to the very first intermediate update rule derived along the way to Adadelta:

$$E[g^2]_t = 0.9\, E[g^2]_{t-1} + 0.1\, g_t^2$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{E[g^2]_t + \epsilon}}\, g_t$$

In other words: like Adadelta, RMSprop divides the learning rate by an **exponentially decaying average of squared gradients** (a decaying RMS, hence the name "Root Mean Square propagation"). Unlike the *final* Adadelta update rule though, RMSprop stops at this point — it does **not** go on to also track a decaying average of squared parameter updates and use that to eliminate the learning rate entirely. RMSprop still needs an explicit learning rate $\eta$.

Hinton's suggested defaults: $\gamma = 0.9$ for the decay rate, and $\eta = 0.001$ as a good default learning rate.

**Why this matters in practice**: because RMSprop is simpler than Adadelta (one fewer moving part — no separate tracking of update magnitudes) while solving the same core Adagrad problem, it became — and, as of 2026, remains — one of the most commonly reached-for default optimizers for many kinds of neural networks, especially recurrent networks, and it is also a direct mathematical building block of [[09_Adam]], covered next.

---

## 2) Simple English Explanation

RMSprop solves the exact same problem as Adadelta (Adagrad's nudge sizes shrinking to nothing forever) using the exact same core trick — a fading, "recent-history-only" memory of how big each dial's past adjustments have been, instead of a memory that never forgets.

What's interesting about RMSprop is *where it came from*: it wasn't introduced in a formal research paper at all. It was simply mentioned by a famous AI researcher, **Geoff Hinton**, in one slide of an online video lecture — and yet it turned out to work so well that it became (and still is) one of the most popular optimizers used in practice, published paper or not.

RMSprop is basically a **simpler cousin** of Adadelta — it uses the same fading-memory trick to shrink the effective learning rate for dials that have recently had large gradients, but it stops one step short of Adadelta's fancier trick of eliminating the learning rate entirely. You still pick a learning rate for RMSprop (Hinton's suggested default is a small number, 0.001), it's just that RMSprop automatically adjusts how that learning rate gets scaled per-dial, per-step.

---

## 3) Hinglish Explanation (Beginner-Friendly)

RMSprop bhi wahi problem solve karta hai jo Adadelta karta hai (Adagrad ke nudge sizes forever shrink ho kar zero ho jaana) — isi core trick se: har dial ke past adjustments ki fading, "sirf recent-history" memory, na ki wo memory jo kabhi kuch bhoolti nahi.

RMSprop ke baare mein interesting baat ye hai ki *ye aaya kahan se*: isse kisi formal research paper mein introduce hi nahi kiya gaya tha. Ise sirf ek famous AI researcher, **Geoff Hinton**, ne apne ek online video lecture ki ek slide mein mention kiya tha — aur phir bhi ye itna achha kaam karta hai ki ye practice mein sabse popular optimizers mein se ek ban gaya (aur aaj bhi hai), chahe koi published paper ho ya na ho.

RMSprop basically Adadelta ka ek **simpler cousin** hai — ye same fading-memory trick use karta hai un dials ka effective learning rate shrink karne ke liye jinke recent gradients bade rahe hai, lekin ye Adadelta ke us extra fancy trick tak nahi jaata jo learning rate ko completely eliminate kar deta hai. RMSprop mein tumhe abhi bhi ek learning rate choose karni padti hai (Hinton ka suggested default ek chhota number hai, 0.001), bas RMSprop automatically adjust karta hai ki wo learning rate har dial, har step pe kaise scale ho.
