# Topic 11: Visualizing the Algorithms, and Which Optimizer to Use

Source: Lecture 0, Sections 4.9 (Visualization of algorithms) and 4.10 (Which optimizer to use?) of Ruder's overview paper.

---

## 1) Technical Explanation

The paper illustrates the practical behavior of the algorithms covered so far (SGD, Momentum, NAG, Adagrad, Adadelta, RMSprop) with two visualizations (recreated as diagrams on the site for this topic, based on animations originally by Alec Radford):

**Loss surface contours (the Beale function)**: all algorithms start from the same point on a contour plot of a genuinely tricky, curvy 2D test loss surface, and their different paths to the minimum are plotted. Adagrad, Adadelta, and RMSprop head off **immediately in the right direction** and converge at a similarly fast pace. Momentum and NAG, by contrast, initially get **led off-track** — visually, this looks exactly like a ball rolling downhill and overshooting, consistent with the "heavy ball" intuition from [[04_Momentum]]. NAG is able to correct its course **sooner** than plain Momentum, thanks to its look-ahead responsiveness, and it does eventually reach the minimum.

**Saddle point behavior**: at a genuine saddle point (positive slope in one dimension, negative in another — see [[03_Challenges_in_Gradient_Descent_Optimization]]), SGD, Momentum, and NAG all find it **difficult to break the symmetry** of the saddle at first, though Momentum and NAG eventually manage to escape it. Adagrad, RMSprop, and Adadelta, on the other hand, **quickly head down the negative-slope direction** — with Adadelta leading the charge. The conclusion drawn: the **adaptive learning-rate methods** (Adagrad, Adadelta, RMSprop, and by extension Adam) are the most suitable and provide the best convergence in exactly these kinds of tricky scenarios (curvy surfaces and saddle points) that plague plain SGD-family methods.

**So, which optimizer should you actually use? (the paper's own practical guidance, 2016)**
- If your input data is **sparse**, one of the adaptive learning-rate methods is likely to give the best results — with the added bonus that you won't need to hand-tune the learning rate and can typically just use the default.
- **RMSprop**, **Adadelta**, and **Adam** are all very similar algorithms that tend to do well in similar circumstances: RMSprop is an extension of Adagrad addressing its diminishing-learning-rate problem; Adadelta is nearly identical to RMSprop except that it additionally uses the RMS of parameter *updates* in the update rule's numerator (eliminating the need for an explicit learning rate); Adam adds bias-correction and momentum on top of RMSprop.
- Kingma et al. (the Adam authors) show Adam's bias-correction helps it slightly **outperform RMSprop** toward the end of training, as gradients tend to become sparser. The paper's own conclusion: **Adam might be the best overall choice**.
- Interestingly, the paper also notes that many published papers (even in 2016) still used **vanilla SGD without momentum**, paired with a simple hand-designed learning-rate annealing schedule. SGD usually does find a minimum eventually, but tends to take significantly longer, is much more sensitive to a good initialization and a well-tuned annealing schedule, and is more likely to get stuck at saddle points (rather than local minima) than the adaptive methods are.
- **Bottom line from the paper**: if fast convergence matters and you're training a deep or complex network, choose one of the adaptive learning-rate methods.

**Note on how this has aged (as of 2026, per web research and current practice)**: Adam (and its refinement, AdamW — see [[09_Adam]]) has gone on to become the dominant default optimizer for training most large modern neural networks, including transformers, largely confirming this paper's 2016 conclusion. Well-tuned SGD-with-momentum variants are still sometimes preferred for certain computer-vision architectures where they can generalize slightly better given enough training time and careful tuning, but for the vast majority of practical deep learning work today, an Adam-family optimizer remains the sensible default starting point this paper already pointed toward.

---

## 2) Simple English Explanation

Imagine racing several different "route-finding strategies" (SGD, Momentum, NAG, Adagrad, Adadelta, RMSprop) down two different kinds of tricky terrain, all starting from the exact same spot, to see who reaches the bottom fastest and most reliably.

**On a winding, curvy valley**: the "adapt each dial individually" strategies (Adagrad, Adadelta, RMSprop) head straight for the goal almost immediately and get there quickly. The "heavy rolling ball" strategies (Momentum, NAG) initially overshoot and wander off course — exactly like a heavy ball would, rolling too far before correcting — but NAG (the "smarter ball" from earlier) recovers and corrects its path sooner than plain Momentum does.

**On a mountain-pass-shaped saddle point**: SGD, Momentum, and NAG all get stuck for a while, struggling to figure out which way is actually "down" when the terrain is symmetric and confusing right where they're standing. The "adapt each dial individually" group, though, quickly senses the one direction that actually slopes downward and heads that way — Adadelta leading the pack.

**The paper's practical takeaway, in plain terms**: if you're not sure which optimizer to pick, an "adaptive" one (and Adam specifically, which combines the best ideas from several of them) is usually a safe, strong default — especially if you don't want to spend a lot of time manually tuning a learning rate. Plain SGD can still get the job done, but it typically needs more careful babysitting (a good starting point, a well-designed schedule for shrinking the step size over time) and is more prone to getting stuck on flat, confusing terrain (saddle points) along the way.

This recommendation has held up remarkably well: nearly a decade later, Adam (and its refined cousin, AdamW) remains the most commonly used default optimizer for training modern neural networks, including today's large language models.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho kayi alag "raasta-dhoondhne ki strategies" (SGD, Momentum, NAG, Adagrad, Adadelta, RMSprop) ek race lagate hai do tarah ke tricky terrain mein neeche jaane ki, sab ek hi jagah se start karte hue, ye dekhne ke liye ki kaun sabse fast aur reliably sabse neeche pahunchta hai.

**Ek ghumaavdaar, curvy valley pe**: "har dial ko individually adapt karo" wali strategies (Adagrad, Adadelta, RMSprop) lagbhag turant goal ki taraf seedha jaati hai aur jaldi pahunch jaati hai. "Heavy rolling ball" wali strategies (Momentum, NAG) shuru mein overshoot karti hai aur raaste se bhatak jaati hai — bilkul jaise ek heavy ball karti, bahut door tak roll ho kar phir correct karti — lekin NAG ("smarter ball" jo pehle padha) Momentum se jaldi recover kar leti hai aur apna path correct kar leti hai.

**Ek mountain-pass jaisi saddle point pe**: SGD, Momentum, aur NAG teeno kuch der ke liye fas jaate hai, ye figure out karne mein struggle karte hai ki actually "neeche" kaunsi taraf hai jab terrain symmetric aur confusing hai jahan wo khade hai. "Har dial ko individually adapt karo" wala group jaldi hi us ek direction ko sense kar leta hai jo actually neeche ki taraf slope karti hai aur us taraf badh jaata hai — Adadelta sabse aage.

**Paper ka practical takeaway, simple shabdon mein**: agar tumhe pata nahi kaunsa optimizer choose karna hai, to ek "adaptive" wala (aur specifically Adam, jo kayi ideas ke best parts combine karta hai) usually ek safe, strong default hai — khaaskar agar tum learning rate manually tune karne mein zyada time nahi lagaana chahte. Plain SGD bhi kaam kar sakta hai, lekin usse usually zyada careful babysitting chahiye (achhi starting point, step size ko time ke saath shrink karne ka ek achha schedule) aur wo flat, confusing terrain (saddle points) mein fasne ke zyada chances rakhta hai.

Ye recommendation remarkably well hold hui hai: lagbhag ek dashak baad bhi, Adam (aur uska refined cousin, AdamW) aaj bhi modern neural networks train karne ka sabse commonly used default optimizer hai, including aaj ke bade language models.
