# Topic 2: SGD, BGD, and MBGD — Compared in Detail

Source: Lecture 11 (ES532: Introduction to Deep Learning), slides 5–7.

---

## 1) Technical Explanation

Building on the three types named in [[00_Recap_Gradient_Descent_Definition_and_Types]] (and originally in Lecture 0's [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]]), this lecture goes deeper into each one's specific properties, use cases, and failure modes.

### Stochastic Gradient Descent (SGD)

- Computes the gradient for **only one random sample** at each iteration.
- This makes it **faster and more efficient** than the alternatives, since it doesn't need to process the whole dataset per update.
- **Downside**: its randomness means it can, in some cases, converge to a **suboptimal solution / local minimum** rather than the true global minimum.
- **Mitigation**: **decrease the learning rate over time** — this reduces the size of parameter updates as training progresses, which is exactly the learning-rate-annealing/scheduling idea already flagged as a challenge (and partial fix) back in Lecture 0's [[03_Challenges_in_Gradient_Descent_Optimization]] ("Learning rate schedules... reducing the learning rate according to a pre-defined schedule").
- **Variants named on the slide**: **Mini-Batch SGD** (gradient descent on a random subset of data) and **Momentum SGD** (adds a term to the gradient update to help avoid getting stuck at a local minimum — this is exactly the [[04_Momentum]] algorithm from Lecture 0, and the subject this lecture itself builds toward in [[07_Momentum_Based_MiniBatch_Gradient_Descent]]).
- **Applications named**: classification, regression, and neural machine translation — SGD (in its mini-batch form, as the slide itself later clarifies) is the dominant choice in deep learning specifically.

### Batch Gradient Descent (BGD)

- Computes the gradient based on the **average of the gradients of all data samples** in the training set.
- Because the gradient must be calculated over the **entire dataset** every single iteration, BGD is **computationally expensive for huge datasets**.
- **Advantage**: this also makes it **more stable** and less prone to overfitting compared to SGD (since each update reflects the true, exact gradient rather than a noisy single-sample estimate).
- The learning rate must be chosen carefully so the step size doesn't grow uncontrollably or cause the algorithm to diverge from the minimum.
- **Where it's actually used**: simpler models with less data — the slide names **linear regression and logistic regression** specifically, and explicitly states BGD is "not so much" used in deep learning, "where the training set is typically large and the models have many parameters" (tying directly back to why the home-price linear regression example in Lecture 10 could reasonably use a small, complete dataset per update, while a real neural network generally cannot).

### Mini-Batch Gradient Descent (MBGD)

- Described directly as **a combination of SGD and BGD**.
- Computes the gradient over a **subset of the data**, called the mini-batch, rather than either one full example (SGD) or the whole dataset (BGD).
- This gives it **faster computation than BGD** while **avoiding the overfitting/instability issues of SGD**.
- **The mini-batch size is a genuine trade-off**: smaller mini-batches converge faster per unit of computation but introduce more variability/noise into the optimization; larger mini-batches converge more stably but take longer to process per step.
- The learning rate must again be carefully tuned to avoid oscillation or divergence — the same general concern that applies to every gradient-descent variant.
- **Where it's used**: widely in deep learning, across classification, regression, and neural machine translation — this is the practical default for training neural networks, as already noted in Lecture 0's [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]] ("Mini-batch gradient descent is typically the algorithm of choice when training a neural network").

**Summary of the trade-off triangle** these three slides collectively describe: BGD is the most **stable** but least **scalable**; SGD is the most **scalable/fast per step** but least **stable**; MBGD sits deliberately in between, and is why it's the practical default for real deep learning workloads — exactly the motivation for the worked mini-batch sizing example in [[04_MiniBatching_a_Large_Dataset_Worked_Example]].

---

## 2) Simple English Explanation

This topic gives a much more detailed, practical breakdown of the three gradient descent flavors you've already met, covering their real strengths, weaknesses, and typical use cases.

**SGD (one example at a time)**: fast, because it never waits to process the whole dataset before making a move — but its randomness means it can sometimes wander into a decent-but-not-best answer instead of the true best one. The standard fix is to gradually shrink the step size as training goes on, so its later steps become more careful and precise. SGD has two well-known variants: a "mini-batch" version (small groups instead of single examples) and a "momentum" version (which smooths out its jumpiness — the exact topic this lecture builds toward).

**BGD (the whole dataset every time)**: very stable and reliable, because every single step is based on the *complete, exact* picture of the error — no randomness, no guessing. The catch: recomputing something over the entire dataset every single step gets extremely slow and expensive once the dataset is large, which is exactly why it's mostly used for simpler problems (like the basic linear/logistic regression examples from earlier lectures) and rarely for deep learning, where datasets and models are both usually huge.

**MBGD (a small batch at a time)**: the practical middle ground — small enough batches to stay fast, but big enough to smooth out most of SGD's random jitteriness. The batch size itself is a genuine dial to tune: smaller batches move fast but bounce around more; bigger batches are steadier but slower per step. This balance is exactly why mini-batch gradient descent is the default choice for training real neural networks in practice.

**The big-picture trade-off**: think of a dial with "stability" on one end and "speed/scalability" on the other. Batch GD is all the way at the stability end; SGD is all the way at the speed end; Mini-batch GD deliberately sits in the middle, which is exactly why it wins out as the practical default for real deep learning work.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic un teen gradient descent flavors ka ek bahut zyada detailed, practical breakdown deta hai jo tum already mil chuke ho, unki real strengths, weaknesses, aur typical use cases cover karte hue.

**SGD (ek time pe ek example)**: fast hai, kyunki ye poora dataset process karne ka wait kabhi nahi karta move lene se pehle — lekin uski randomness ka matlab hai ki ye kabhi-kabhi ek decent-but-not-best answer mein bhatak sakta hai, asli best answer ke bajaye. Standard fix ye hai ki training aage badhte waqt gradually step size shrink kar do, taaki uske baad ke steps zyada careful aur precise ban jaayein. SGD ke do well-known variants hai: ek "mini-batch" version (single examples ke bajaye chhote groups) aur ek "momentum" version (jo uski jumpiness ko smooth karta hai — bilkul wahi topic jiski taraf ye lecture build kar rahi hai).

**BGD (har baar poora dataset)**: bahut stable aur reliable hai, kyunki har single step *complete, exact* error ki picture par based hai — koi randomness nahi, koi guessing nahi. Catch ye hai: poore dataset par har single step kuch recompute karna extremely slow aur expensive ho jaata hai jab dataset bada ho, isi wajah se ye zyadatar simpler problems ke liye use hota hai (jaise earlier lectures ke basic linear/logistic regression examples) aur deep learning ke liye rarely, jahan datasets aur models dono usually huge hote hai.

**MBGD (ek time pe ek chhota batch)**: practical middle ground — itne chhote batches ki fast rahe, lekin itne bade ki SGD ki zyadatar random jitteriness smooth ho jaaye. Batch size khud ek genuine dial hai tune karne ke liye: chhote batches fast move karte hai lekin zyada bounce karte hai; bade batches steadier hai lekin har step slower. Ye balance hi exact wajah hai ki mini-batch gradient descent real neural networks train karne ke liye default choice hai practice mein.

**Bade picture wala trade-off**: ek dial socho jispar ek end pe "stability" hai aur doosre end pe "speed/scalability" hai. Batch GD bilkul stability wale end pe hai; SGD bilkul speed wale end pe hai; Mini-batch GD jaan-bujh kar beech mein baithta hai, isi wajah se ye real deep learning work ke liye practical default ban jaata hai.
