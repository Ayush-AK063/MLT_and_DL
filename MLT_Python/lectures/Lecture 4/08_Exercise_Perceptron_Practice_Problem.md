# Topic 8: Exercise — Linear Separability & Perceptron Design (Worked Solution)

Source: Lecture 4, slides 29–30 (Exercise, with blank graph grid on slide 30 for plotting).

**The exercise as given in the lecture**:
> Consider 2-D samples belonging to two classes:
> - Class I: (0,0), (0,1), (1,0), (-1,-1)
> - Class II: (2.1, 0), (0, -2.5), (1.6, -1.6)
>
> (i) Are these points linearly separable?
> (ii) Design a perceptron that separates the patterns from both classes.

This topic file preserves the exercise exactly as given, **and** walks through a full worked solution — so this note is self-contained for study/revision purposes.

---

## 1) Technical Explanation (Full Worked Solution)

**Step 1 — Plot and inspect the points.**
- Class I points `(0,0), (0,1), (1,0), (-1,-1)` all lie close to the origin, with coordinate magnitudes no larger than 1 in any direction.
- Class II points `(2.1,0), (0,-2.5), (1.6,-1.6)` all lie noticeably farther from the origin, generally in the direction of "positive x, negative y" (the lower-right region of the plane).

**Step 2 — Check for a separating line (linear separability).**
Try the candidate linear boundary `x1 − x2 = c` (i.e., difference between the two coordinates) and evaluate it at every point:

| Point | Class | x1 − x2 |
|---|---|---|
| (0,0) | I | 0 |
| (0,1) | I | −1 |
| (1,0) | I | 1 |
| (−1,−1) | I | 0 |
| (2.1,0) | II | 2.1 |
| (0,−2.5) | II | 2.5 |
| (1.6,−1.6) | II | 3.2 |

Class I values of `x1 − x2` range from **−1 to 1**. Class II values range from **2.1 to 3.2**. Since these two ranges **do not overlap**, any threshold value between 1 and 2.1 (e.g., `c = 1.5`) cleanly separates the two classes.

**Answer to (i)**: **Yes, these points are linearly separable** — a straight line of the form `x1 − x2 = 1.5` separates Class I from Class II with zero misclassifications.

**Step 3 — Design a perceptron from this separating line.**
Recall from Topic 4/5 that a perceptron's decision rule has the form:
`output = w1·x1 + w2·x2 + b`, then apply threshold `≥ 0 → Class II`, `< 0 → Class I`.

Rewriting the separating line `x1 − x2 − 1.5 = 0` directly gives the perceptron's weights and bias:
- **w1 = 1**
- **w2 = −1**
- **bias b = −1.5**

**Decision rule**: compute `y = (1)·x1 + (−1)·x2 + (−1.5)`.
- If `y ≥ 0` → classify as **Class II**
- If `y < 0` → classify as **Class I**

**Verification** (plugging in a couple of points):
- Class I point `(1,0)`: `y = 1(1) + (−1)(0) − 1.5 = 1 − 1.5 = −0.5` → negative → Class I ✓ (correct)
- Class II point `(2.1,0)`: `y = 1(2.1) + (−1)(0) − 1.5 = 2.1 − 1.5 = 0.6` → positive → Class II ✓ (correct)
- Class II point `(0,−2.5)`: `y = 1(0) + (−1)(−2.5) − 1.5 = 2.5 − 1.5 = 1.0` → positive → Class II ✓ (correct)

All 7 points classify correctly with this simple perceptron — confirming both that the data is linearly separable and that this particular perceptron design (`w1=1, w2=−1, b=−1.5`) correctly solves it. (Note: this is *one valid solution* — many other weight/bias combinations, corresponding to any line between the two clusters, would also work correctly.)

---

## 2) Simple English Explanation

This is a practice problem that asks you to apply everything from this lecture: can a perceptron separate two groups of points, and if so, what weights/bias would do it?

**The two groups**:
- **Class I**: four points that are all close to the center of the graph — (0,0), (0,1), (1,0), (−1,−1).
- **Class II**: three points that are all farther away, off toward the bottom-right — (2.1,0), (0,−2.5), (1.6,−1.6).

**Question (i): Can one straight line separate them?**
Yes. If you look at each point and calculate "first number minus second number" (`x1 − x2`), you'll notice something neat: for every Class I point, this value comes out between −1 and 1. For every Class II point, it comes out between 2.1 and 3.2. Since these two ranges of numbers never overlap, you can pick any cutoff number in between (like 1.5) and perfectly separate the two groups every single time. That means: **yes, this data is linearly separable.**

**Question (ii): What perceptron (weights + bias) would do this separation?**
Since the rule that worked was "x1 − x2, compared to 1.5," we can directly turn that into perceptron weights:
- Weight on x1 = **1**
- Weight on x2 = **−1**
- Bias = **−1.5**

So the perceptron computes: `(1 × x1) + (−1 × x2) + (−1.5)`. If that result is 0 or higher, it's Class II; if it's negative, it's Class I.

We can double-check this actually works by trying it on a couple of real points:
- Point (1,0), which is Class I: `1(1) − 1(0) − 1.5 = −0.5` → negative → correctly says Class I.
- Point (2.1,0), which is Class II: `1(2.1) − 1(0) − 1.5 = 0.6` → positive → correctly says Class II.

Both check out — this perceptron design correctly separates all seven points.

---

## 3) Hinglish Explanation (Beginner-Friendly, with Full Solved Answer)

Ye ek practice question hai jisme aapko is poore lecture ka concept apply karna hai: **kya perceptron in do groups ko alag kar sakta hai, aur agar haan, to kaunse weights/bias se?**

**Do groups:**
- **Class I**: 4 points jo graph ke beech (center) ke paas hai — (0,0), (0,1), (1,0), (−1,−1)
- **Class II**: 3 points jo center se kaafi door hai, neeche-dayein taraf — (2.1,0), (0,−2.5), (1.6,−1.6)

**Sawaal (i): Kya ek seedhi line se ye alag ho sakte hai?**
**Haan, ho sakte hai.** Agar aap har point ka "pehla number - doosra number" (`x1 − x2`) nikalo, to ek pattern dikhega:
- Class I ke saare points ke liye ye value **−1 se 1 ke beech** aati hai.
- Class II ke saare points ke liye ye value **2.1 se 3.2 ke beech** aati hai.

Kyunki ye 2 ranges **kabhi overlap nahi hoti**, aap in dono ke beech koi bhi cutoff number (jaise **1.5**) choose kar sakte ho aur har baar dono groups ko perfectly alag kar sakte ho.

**Isliye jawaab hai: Haan, ye data Linearly Separable hai.**

**Sawaal (ii): Kaunsa perceptron (weights + bias) ye separation kar sakta hai?**
Jo rule kaam kiya wo tha "x1 − x2, compare 1.5 se" — ise seedhe perceptron weights mein badal sakte hai:
- x1 ka weight = **1**
- x2 ka weight = **−1**
- Bias = **−1.5**

Perceptron ye calculate karega: `(1 × x1) + (−1 × x2) + (−1.5)`. Agar result **0 ya usse zyada** ho → **Class II**. Agar **negative** ho → **Class I**.

**Verify karke dekhte hai (kuch points pe):**
- Point (1,0), jo Class I hai: `1(1) − 1(0) − 1.5 = −0.5` → negative → sahi se **Class I** bata raha hai ✓
- Point (2.1,0), jo Class II hai: `1(2.1) − 1(0) − 1.5 = 0.6` → positive → sahi se **Class II** bata raha hai ✓
- Point (0,−2.5), jo Class II hai: `1(0) − 1(−2.5) − 1.5 = 2.5 − 1.5 = 1.0` → positive → sahi se **Class II** bata raha hai ✓

Sab 7 points sahi classify ho rahe hai is simple perceptron se — matlab ye confirm hota hai ki data linearly separable hai, aur ye particular perceptron (`w1=1, w2=−1, b=−1.5`) use sahi tarike se solve karta hai.

**Note**: Ye **ek** valid solution hai — do groups ke beech se guzarti koi bhi doosri line (alag weights/bias ke saath) bhi sahi answer degi.
