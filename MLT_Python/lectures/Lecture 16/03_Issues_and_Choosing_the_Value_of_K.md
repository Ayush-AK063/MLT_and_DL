# Topic 3: Issues in Nearest-Neighbor Classifiers and Choosing the Value of K

Source: Lecture 16, slides 5–6 ("Nearest-Neighbor Classifiers: Issues", "Value of K" with the rule of thumb K = sqrt(N) and the instructor's N = 100 example). Enriched with web research (cross-validation for choosing k, under-/over-fitting behaviour).

---

## 1) Technical Explanation

**The five issues (slide 5).** The slide lists what must be decided or controlled when using a nearest-neighbor classifier:

1. **The value of k** — how many nearest neighbors to retrieve.
2. **Choice of distance metric** — how to compute the distance between records ([[04_Distance_Metrics]]).
3. **Computational complexity** — each prediction needs distances to stored points ([[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]]).
4. **Size of the training set** — more data = better coverage, but slower queries.
5. **Dimension of data** — number of features; many dimensions make "nearest" less meaningful.

The instructor's handwriting on slide 6 circles the first two as the two *choices the user must make*: **① k? (k = √N)** and **② Distance metric.**

**Choosing k (slide 6).**

- *If k is **too small**, the classifier is **sensitive to noise points*** — with k = 1 a single mislabeled or outlying training point can flip the prediction (high variance, over-fitting; the decision boundary becomes jagged and follows every noisy point).
- *If k is **too large**, the neighborhood may include points from **other classes*** — the vote is dominated by far-away points, so the classifier ignores local structure (high bias, under-fitting). In the extreme k = N, **every** query gets the single most common class of the whole training set.

The slide's figure shows this: a query **x** surrounded by a tight cluster of 5 `+` points, inside a huge red dashed circle that also contains many `−` points. With a small k, x is correctly classed `+`; with a very large k the circle swallows the `−` majority and x is misclassified.

**Rule of thumb: K = √N** (N = number of training points). The instructor's worked note: **N = 100 → k = √100 = 10.**

**⚠️ Observation (flagged, not hidden).** The slide's own example gives k = **10, an even number** — which conflicts with the advice on [[01_Nearest_Neighbor_Idea_and_Basic_Rule]] that k should be odd to avoid ties (and see the contradiction noted in [[05_The_k_NN_Algorithm_Step_by_Step]]). The standard practical fix is to **round √N to the nearest odd number** (here 9 or 11). The √N rule is also only a *starting point*, not a law.

**Better practice (research).** The reliable way to pick k is **cross-validation**: try several candidate k values (typically odd values 1, 3, 5, 7, … up to about √N), measure accuracy on held-out validation data for each, and keep the k that performs best. Plotting validation error against k usually shows the U-shape: high error at k = 1 (noise), a sweet spot, then rising error again as k grows large (washed-out neighborhoods). Tie-breaking and data scaling interact with this choice — see [[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]].

**Worked mini-example.** Suppose a query has its 5 nearest labels in order of closeness: `+, −, −, +, −`.
- k = 1 → `+`.
- k = 3 → (+, −, −) → `−`.
- k = 5 → (3 `−`, 2 `+`) → `−`.

The prediction flipped between k = 1 and k = 3, showing how strongly the answer depends on k.

---

## 2) Simple English Explanation

Before using k-NN you have to make a few decisions:

1. **How many neighbors to ask (k)?**
2. **How do we measure "close"?** (the distance rule)
3. **How slow will it be?** (it checks every stored example every time)
4. **How much data do we have?**
5. **How many features does each example have?**

The two big decisions are **k** and **the distance rule**.

**Picking k is like asking for opinions:**
- Ask **only 1 person** (k too small): if that one person is odd or mistaken, you get a wrong answer. Too sensitive to "noise."
- Ask **the entire city** (k too big): you hear from people who are far away and nothing like you, so the loud majority drowns out your real neighbors.
- The sweet spot is somewhere in the middle.

A common starting guess is **k = square root of the number of examples**. With 100 examples, √100 = 10. One catch: the slide's answer, 10, is an even number, and even numbers can cause ties — so in practice people nudge it to 9 or 11. The best method is to **test a few k values on data you set aside** and keep the one that scores best.

Quick example: the 5 nearest neighbors are `+, −, −, +, −`. Ask 1 neighbor → `+`. Ask 3 → `−`. Ask 5 → `−`. See how the answer changed just because k changed?

---

## 3) Hinglish Explanation (Beginner-Friendly)

k-NN use karne se pehle kuch cheezein decide karni padti hain (slide 5):

1. **k kitna rakhein?**
2. **Distance kaise naapein?**
3. **Computation kitni lagegi?** (har baar saare stored points se distance)
4. **Training set kitna bada hai?**
5. **Features (dimensions) kitne hain?**

Sabse zaroori do hain: **k** aur **distance metric** (sir ne slide par inhe ① aur ② likh kar circle kiya hai).

**k chunna aise samjho:**
- **k bahut chhota** (jaise 1): sirf ek aadmi se poochh liya. Agar wo galat/ajeeb nikla to answer galat. Isse kehte hain **noise ke prati sensitive**.
- **k bahut bada**: poore sheher se poochh liya, jisme door ke aise log bhi aa gaye jo tumse bilkul alag hain (**doosri class ke points**). To asli paas wale neighbors ki awaaz dab jaati hai.
- Sahi k beech mein kahin hota hai.

**Rule of thumb: k = √N** (N = training points ki sankhya). Sir ka example: N = 100 to k = √100 = **10**. 

Dhyaan do ✋: ye 10 **even** number hai, aur even k mein tie ho sakta hai — jabki slide 3 mein khud kaha tha ki k odd rakho. Isliye practical mein √N ko nazdeeki odd number (9 ya 11) mein round kar lete hain. Aur sabse behtar tareeka hai **cross-validation**: alag-alag k try karo, validation data par accuracy dekho, jo sabse acchi ho wahi rakho.

Example: sabse paas ke 5 neighbors ke labels `+, −, −, +, −` hain. k=1 → `+`. k=3 → (+,−,−) → `−`. k=5 → 3 minus, 2 plus → `−`. Dekha? Sirf k badalne se answer badal gaya!
