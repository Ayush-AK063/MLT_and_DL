# Topic 2: Batch, Stochastic, and Mini-Batch Gradient Descent

Source: Lecture 0, Section 2 (Gradient descent variants) of Ruder's overview paper.

---

## 1) Technical Explanation

There are **three variants** of gradient descent, differing only in **how much data** is used to compute the gradient for a single parameter update. This is a trade-off between the **accuracy** of the update and the **time** it takes to perform one.

### 2.1 Batch Gradient Descent (a.k.a. Vanilla Gradient Descent)

Computes the gradient of the cost function w.r.t. the parameters $\theta$ using the **entire training dataset** at once:

$$\theta = \theta - \eta \cdot \nabla_\theta J(\theta)$$

```
for i in range(nb_epochs):
    params_grad = evaluate_gradient(loss_function, data, params)
    params = params - learning_rate * params_grad
```

- One update = one full pass over the whole dataset's gradient computation.
- **Pros**: guaranteed to converge to the global minimum for convex surfaces, and to a local minimum for non-convex surfaces (like neural networks).
- **Cons**: can be very slow, and is **intractable** for datasets that don't fit in memory. It also does not allow **online learning** (updating the model incrementally as new examples arrive).

### 2.2 Stochastic Gradient Descent (SGD)

Performs a parameter update for **each individual training example** $x^{(i)}, y^{(i)}$:

$$\theta = \theta - \eta \cdot \nabla_\theta J(\theta; x^{(i)}; y^{(i)})$$

```
for i in range(nb_epochs):
    np.random.shuffle(data)
    for example in data:
        params_grad = evaluate_gradient(loss_function, example, params)
        params = params - learning_rate * params_grad
```

- Batch GD wastes computation recomputing gradients for very similar examples before every single update. SGD removes this redundancy by updating after just one example — usually much faster, and it supports online learning.
- SGD's updates have **high variance**, causing the loss to fluctuate heavily (visualized as a jagged, noisy decreasing curve rather than a smooth one — see the diagram on the site for this topic).
- This fluctuation is double-edged: it lets SGD jump to potentially **better** local minima it might otherwise never reach, but it also means SGD keeps "overshooting" and never exactly settles at the minimum.
- **Key theoretical result**: if the learning rate is decreased slowly over time (annealed), SGD shows *the same convergence behaviour* as batch gradient descent — almost certainly converging to the local minimum (non-convex case) or global minimum (convex case).
- The training data is shuffled at the start of every epoch (see the "Shuffling and Curriculum Learning" topic later in this lecture) to avoid feeding examples in a biased, meaningful order.

### 2.3 Mini-Batch Gradient Descent

Takes the best of both worlds — an update for every **mini-batch of $n$ training examples**:

$$\theta = \theta - \eta \cdot \nabla_\theta J(\theta; x^{(i:i+n)}; y^{(i:i+n)})$$

```
for i in range(nb_epochs):
    np.random.shuffle(data)
    for batch in get_batches(data, batch_size=50):
        params_grad = evaluate_gradient(loss_function, batch, params)
        params = params - learning_rate * params_grad
```

- (a) Reduces the **variance** of parameter updates compared to per-example SGD → more stable convergence.
- (b) Lets the computation use highly optimized matrix operations that deep learning libraries are built for (computing a gradient over a batch as one matrix multiply is far more efficient on a GPU than looping example-by-example).
- Common mini-batch sizes: **50 to 256**, though this varies by application (modern practice, as of 2026, commonly uses larger batches — 128 to several thousand — especially with large models and distributed/multi-GPU training, though the tuning trade-offs discussed later in this paper still apply in spirit).
- **Mini-batch gradient descent is the algorithm of choice in practice** for training neural networks. The term "SGD" is used loosely in the literature to refer to mini-batch gradient descent too — the paper explicitly notes this and, for simplicity, drops the $x^{(i:i+n)}; y^{(i:i+n)}$ notation for all the algorithms discussed in the rest of the overview (Momentum, Adam, etc.), even though they are typically run on mini-batches.

---

## 2) Simple English Explanation

Think of training a model as trying to find the best "settings" by repeatedly checking how wrong the current settings are and nudging them to be a little less wrong. The question this topic answers is: **each time you check "how wrong am I," how much of your data do you look at?**

**Batch Gradient Descent** — look at your *entire* dataset before making even one adjustment.
- Like a chef who tastes a giant pot of soup completely (checking every corner) before deciding to add a pinch of salt. Very thorough, very accurate — but painfully slow if the pot is huge, and impossible if the pot is bigger than your kitchen (i.e., data doesn't fit in memory).

**Stochastic Gradient Descent (SGD)** — adjust after looking at just *one* example at a time.
- Like tasting a single spoonful, adjusting the salt immediately, tasting the next spoonful, adjusting again. Much faster per adjustment, but each individual spoonful might not represent the whole pot well — so your salt level will jump around a lot before it settles near the right amount. Interestingly, this "jumpiness" occasionally helps: it can bounce you out of a decent-but-not-great answer into a better one.

**Mini-Batch Gradient Descent** — adjust after looking at a small handful of examples (say, 50) at a time.
- Like tasting a small ladle-full instead of one spoonful or the whole pot. This is the sweet spot: enough examples to make your adjustment reasonably steady and reliable, but small enough to stay fast — and computers happen to be extremely efficient at processing data in these small batches all at once (rather than one at a time). This is what's actually used in essentially all real-world neural network training, and people often just call it "SGD" for short even though it's really mini-batch.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Model train karna matlab baar-baar check karna ki abhi ke settings kitni galat hai, aur unhe thoda kam galat karne ke liye adjust karna. Ye topic ye batata hai: **har baar "kitna galat hoon" check karte time, kitna data dekhte ho?**

**Batch Gradient Descent** — poora dataset dekho, tab jaake ek adjustment karo.
- Jaise ek cook ek bade bartan ka poora soup chakh (taste) kar le (har corner check karke), tab namak dale. Bahut thorough, bahut accurate — lekin agar bartan bahut bada hai to bahut slow hoga, aur agar bartan kitchen se bhi bada hai (matlab data memory mein fit hi nahi hota) to impossible hai.

**Stochastic Gradient Descent (SGD)** — sirf *ek* example dekho, turant adjust karo.
- Jaise ek chammach (spoon) bhar soup chakho, turant namak adjust karo, agla chammach chakho, phir adjust karo. Har adjustment bahut fast hota hai, lekin ek chammach pure bartan ko sahi tarah represent nahi karta — isliye tumhara namak level bahut zyada uchhal-kood (fluctuate) karega before settle hone ke. Interesting baat: ye "jumpiness" kabhi-kabhi help bhi karti hai — ye tumhe ek theek-thaak answer se nikaal kar kisi better answer tak pahuncha sakti hai.

**Mini-Batch Gradient Descent** — ek chhoti si handful (jaise 50) examples dekho, phir adjust karo.
- Jaise poora bartan ya ek chammach ke bajaye ek chhoti si karchi (ladle) bhar soup chakho. Ye sabse balanced tarika hai: itna data ki adjustment steady aur reliable rahe, lekin itna kam ki fast bhi rahe — aur computers is tarah ke chhote batches ko ek saath process karne mein bahut efficient hote hai (ek-ek example ki jagah). Real-world mein neural networks lagbhag hamesha isi tarike se train hote hai, aur log ise short mein sirf "SGD" bhi bol dete hai, chahe technically wo mini-batch ho.

**Yaad rakho**: [[03_Challenges_in_Gradient_Descent_Optimization]] topic mein aage dekhenge ki mini-batch gradient descent use karne par bhi kaunsi problems aati hai — jinhe solve karne ke liye Momentum, Adam jaise algorithms banaye gaye.
