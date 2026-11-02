# Topic 12: Parallelizing and Distributing SGD

Source: Lecture 0, Section 5 (Parallelizing and distributing SGD) of Ruder's overview paper.

---

## 1) Technical Explanation

SGD is, by its nature, **inherently sequential**: each update depends on the parameters from the step before it, so you make progress one step at a time. This gives good convergence, but can be slow on large datasets. Running SGD **asynchronously** (multiple workers updating in parallel, without waiting for each other) is faster, but poor communication between workers can hurt convergence — updates can conflict or become stale. The paper covers five specific approaches proposed to address this, given the wide availability of large-scale clusters at the time:

- **Hogwild!** (Niu et al., 2011): allows multiple processors to perform SGD updates **in parallel on shared memory, without locking the parameters** — i.e., without the usual safety mechanism that would normally prevent two processes from overwriting each other's work. This sounds risky, but the authors show it works well specifically when the **input data is sparse**: since each individual update only touches a small fraction of all parameters, it becomes statistically unlikely that two processors will collide and overwrite each other's useful work at the same time. Under that sparsity condition, Hogwild! achieves an almost-optimal rate of convergence despite the lack of locking.

- **Downpour SGD** (Dean et al., 2012): an asynchronous SGD variant used inside Google's **DistBelief** framework — notably, the direct predecessor to TensorFlow. It runs multiple replicas of the same model in parallel, each training on a different subset of the data, and each replica sends its updates to a **parameter server** (itself split across many machines, each storing/updating a fraction of the model's parameters). The weakness: because the replicas never directly communicate with each other (no weight/update sharing between replicas), their individual parameter copies are constantly at risk of **diverging** from one another, which can hinder overall convergence.

- **Delay-tolerant algorithms for SGD** (McMahan and Streeter, 2014): extend [[06_Adagrad]] to the parallel setting specifically by making the algorithm adapt not just to past gradients (as regular Adagrad does) but *also* to the **update delays** inherent in an asynchronous, distributed system — shown to work well in practice.

- **TensorFlow** (Google, 2015/2016): Google's own open-sourced framework for implementing and deploying large-scale ML models, built directly on their experience running DistBelief. Its distributed version (released April 2016) represents computation as a **graph split into a subgraph per device**, with communication between devices handled via explicit Send/Receive node pairs.

- **Elastic Averaging SGD (EASGD)** (Zhang et al., 2015): links the parameters of multiple asynchronous SGD workers together using an "elastic force" — conceptually, a **center variable** stored on the parameter server that each worker's local parameters are gently pulled toward, without being forced to match it exactly. This lets local variables fluctuate further from the shared center than in the tightly-coupled Downpour SGD setup, allowing for more independent exploration of the parameter space by each worker — shown empirically to improve performance by helping the overall system find better local optima than a more tightly synchronized approach would.

**Context for a 2026 reader**: this section is now primarily of historical interest — the underlying research problem (train faster by spreading SGD across many machines/GPUs) is still very much alive, but the specific systems named here have mostly been superseded: DistBelief evolved directly into TensorFlow, which itself is now used alongside (and in many research settings has been overtaken in popularity by) PyTorch's own distributed training tooling. The core ideas, though — asynchronous vs. synchronous updates, parameter servers, and the tension between fast-but-risky asynchrony and slow-but-safe synchrony — remain foundational to how today's largest models (including large language models trained across thousands of GPUs) are actually trained.

---

## 2) Simple English Explanation

So far, everything in this lecture has assumed one single "walker" making one step at a time down the hill. This section asks: what if we used a whole **team** of walkers, spread across many computers, to search for the bottom faster?

The catch is coordination. If everyone moves completely independently and only occasionally checks in, they might get in each other's way, overwrite each other's progress, or end up wandering off in inconsistent directions. If everyone has to constantly stop and perfectly synchronize with the whole team before taking a single step, that's safe but painfully slow — you lose all the speed benefit of having a team in the first place. The five approaches here are all different answers to "how much should the team members check in with each other?"

- **Hogwild!** — let everyone just barge ahead and update a shared notebook (the parameters) without any "wait your turn" rule at all. Risky in general, but if everyone's updates only ever touch a tiny, mostly-non-overlapping corner of the notebook (true when the data is sparse), collisions are rare enough that this reckless-sounding approach works great anyway.
- **Downpour SGD** — several separate teams each work on their own copy of the notebook using their own slice of data, occasionally mailing their updates to a central "clerk" (the parameter server) who applies them. Since the teams never talk to each other directly, their copies of the notebook can slowly drift apart from each other, which can cause problems.
- **Delay-tolerant Adagrad** — a version of Adagrad specifically smart enough to notice "hey, this update I just received is actually a bit stale/delayed" and adjust accordingly, instead of blindly trusting every incoming update as perfectly up-to-date.
- **TensorFlow** — the actual software tool Google built (evolving from an earlier internal system called DistBelief) to make all of this large-scale, multi-machine training practical to actually run.
- **Elastic Averaging SGD** — instead of a strict "everyone must match the shared notebook exactly," each worker is gently *pulled toward* a shared central version, like a rubber band, but is still free to wander a bit on their own. This freedom to explore a little independently, it turns out, actually helps find better answers overall.

Even though the specific tools named here (DistBelief, this exact version of TensorFlow) are now historical, the underlying trade-off — fast-but-risky independence vs. slow-but-safe coordination — is exactly the same challenge engineers still solve today when training today's much larger models across huge clusters of GPUs.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab tak is lecture mein humne socha ki sirf ek hi "walker" hai jo ek time pe ek step leta hai pahad ke neeche. Ye section puchta hai: agar hum bahut saare computers pe phaila hua ek pura **team** use karein, sabse neeche waali jagah jaldi dhoondhne ke liye, to kya hoga?

Problem coordination ki hai. Agar sab completely independently move karein aur sirf kabhi-kabhi check-in karein, to ho sakta hai wo ek doosre ke raaste mein aa jaaye, ek doosre ka progress overwrite kar dein, ya inconsistent directions mein bhatak jaaye. Agar sabko har single step lene se pehle ruk kar pure team ke saath perfectly synchronize karna pade, to ye safe hai lekin bahut slow — team hone ka speed benefit hi kho jaata hai. Yahan diye 5 approaches sab is sawaal ke alag-alag jawab hai: "team members ko ek doosre se kitna check-in karna chahiye?"

- **Hogwild!** — sabko bas aage badhne do aur ek shared notebook (parameters) update karne do bina kisi "apni baari ka wait karo" rule ke. Generally risky, lekin agar har kisi ke updates notebook ke sirf ek chhote, mostly-non-overlapping corner ko touch karte hai (jo tab hota hai jab data sparse ho), to collisions itne rare hote hai ki ye reckless lagne wala approach phir bhi achha kaam karta hai.
- **Downpour SGD** — kai alag teams apne apne notebook ki copy pe kaam karte hai apne data ke slice ke saath, kabhi-kabhi apne updates ek central "clerk" (parameter server) ko bhejte hai jo unhe apply karta hai. Kyunki teams ek doosre se seedha baat nahi karti, unke notebook ki copies slowly ek doosre se drift ho sakti hai, jo problems create kar sakta hai.
- **Delay-tolerant Adagrad** — Adagrad ka ek version jo specifically itna smart hai ki notice kar sake "arey, ye update jo mujhe abhi mila hai wo thoda stale/delayed hai" aur uske hisaab se adjust kare, iske bajaye ki har incoming update ko perfectly up-to-date maan le.
- **TensorFlow** — wo actual software tool jo Google ne banaya (ek pehle ke internal system, DistBelief, se evolve karke) taaki is tarah ki large-scale, multi-machine training actually practical ho sake run karna.
- **Elastic Averaging SGD** — ek strict "sabko shared notebook exactly match karna hoga" ke bajaye, har worker ko gently ek shared central version ki taraf *pull* kiya jaata hai, jaise ek rubber band, lekin wo phir bhi thoda apni marzi se bhatak sakta hai. Ye thoda independently explore karne ki azaadi, actually better answers dhoondhne mein help karti hai.

Chahe yahan naam liye gaye specific tools (DistBelief, is exact version ka TensorFlow) ab historical ho chuke hai, lekin underlying trade-off — fast-but-risky independence vs. slow-but-safe coordination — bilkul wahi challenge hai jo engineers aaj bhi solve karte hai jab wo aaj ke bahut bade models ko huge GPU clusters mein train karte hai.
