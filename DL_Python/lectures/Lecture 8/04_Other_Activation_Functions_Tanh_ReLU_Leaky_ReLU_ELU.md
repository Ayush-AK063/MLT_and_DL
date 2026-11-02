# Topic 4: Other Activation Functions — Tanh, ReLU, Leaky ReLU, ELU, and More

Source: Lecture 8 (ES532: Introduction to Deep Learning), slides 23–24 (activation function table, cited to https://iq.opengenus.org/linear-activation-function/). Enriched with web research on ReLU's origin.

---

## 1) Technical Explanation

The sigmoid function is just **one** example of a broader family of "activation functions" — the function applied to a neuron's weighted sum before it becomes the neuron's output. The slides present a table of the most common ones, with their equation, derivative, and output range:

| Activation Function | Equation | Derivative | Range |
|---|---|---|---|
| **Linear** | $f(x) = x$ | $f'(x) = 1$ | $(-\infty, \infty)$ |
| **Binary Step** | $f(x) = 0$ if $x<0$, else $1$ | $f'(x) = 0$ if $x \neq 0$, undefined at $x=0$ | $\{0, 1\}$ |
| **Sigmoid** | $f(x) = \sigma(x) = \frac{1}{1+e^{-x}}$ | $f'(x) = f(x)(1-f(x))$ | $(0, 1)$ |
| **Tanh (Hyperbolic Tangent)** | $f(x) = \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ | $f'(x) = 1 - f(x)^2$ | $(-1, 1)$ |
| **ReLU (Rectified Linear Unit)** | $f(x) = 0$ if $x<0$, else $x$ — i.e. $\max(0,x)$ | $f'(x) = 0$ if $x<0$, $1$ if $x>0$, undefined at $x=0$ | $[0, \infty)$ |
| **Softplus** | $f(x) = \ln(1+e^x)$ | $f'(x) = \frac{1}{1+e^{-x}}$ (i.e. the sigmoid function) | $(0,1)$ *(the slide's own range column; note Softplus's actual output range is $(0,\infty)$ — see verification note below)* |
| **Leaky ReLU** | $f(x) = 0.01x$ if $x<0$, else $x$ | $f'(x) = 0.01$ if $x<0$, $1$ if $x \geq 0$ | *(slide states $(-1,1)$; see verification note)* |
| **ELU (Exponential Linear Unit)** | $f(x) = \alpha(e^x - 1)$ if $x \leq 0$, else $x$ | $f'(x) = \alpha e^x$ if $x<0$, $1$ if $x>0$ | $[0, \infty)$ *(slide's column; the actual lower bound is $-\alpha$, see note)* |

**Verification note (checking the slide's own numbers, per the usual workflow)**: a couple of the "Range" entries in the source table appear to be typos/copy-paste artifacts from the source website, not mathematically correct for the functions as defined:
- **Softplus**, $f(x)=\ln(1+e^x)$, is always positive and grows without bound as $x \to \infty$ — its true range is $(0, \infty)$, not $(0,1)$ (that narrower range actually belongs to the sigmoid function listed just above it in the source table).
- **Leaky ReLU**, $f(x) = 0.01x$ for $x<0$ and $f(x)=x$ for $x \geq 0$, is unbounded in both directions (a large negative $x$ gives a large negative, if scaled-down, output; a large positive $x$ passes through unchanged) — its true range is $(-\infty, \infty)$, not $(-1,1)$.
- **ELU**'s true range is $[-\alpha, \infty)$, not $[0,\infty)$ — for $x \leq 0$, $f(x) = \alpha(e^x-1)$ approaches $-\alpha$ as $x \to -\infty$ (since $e^x \to 0$) but never goes below it, while for $x>0$ it passes through unbounded, matching the slide's $[0,\infty)$ only for the positive half.

These are flagged here rather than silently corrected in the table, per the usual convention of surfacing anomalies in the source material.

**A second, hand-drawn activation function worth naming from the slide's own annotation**: the instructor's handwritten notes also describe a **Leaky ReLU generalization** as $f(x) = \max(\alpha x, x)$ with $\alpha$ typically a small value like 0.01 — this is exactly the piecewise Leaky ReLU definition above, just written as a single $\max$ expression instead of a case split.

---

## 2) Simple English Explanation

Sigmoid isn't the only "smoothing function" available — it's one member of a whole family of options, called **activation functions**, each with its own shape and trade-offs. This topic is basically a reference card for the most common ones:

- **Linear**: just passes the number straight through, unchanged. Simple, but (as the next topic explains) too simple to be useful on its own in a deep network.
- **Binary Step**: this is the perceptron's harsh on/off switch from earlier — included here just for comparison.
- **Sigmoid**: the smooth S-curve from the previous topic, squashing everything into the range 0 to 1.
- **Tanh**: a close cousin of sigmoid — same general S-shape, but squashes everything into the range **-1 to 1** instead of 0 to 1 (so it's centered around zero, which turns out to matter, as the next topic will explain).
- **ReLU (Rectified Linear Unit)**: an extremely simple rule — if the number is negative, output exactly 0; if it's zero or positive, just pass it straight through unchanged. It looks like a bent line: flat at zero for all negative inputs, then a straight diagonal line going up for positive inputs.
- **Leaky ReLU**: almost identical to ReLU, but instead of completely zeroing out negative inputs, it lets a tiny fraction through (like 1%) instead of nothing — "leaking" a small signal through even on the negative side.
- **ELU (Exponential Linear Unit)**: like ReLU for positive inputs (passes through unchanged), but for negative inputs, it curves smoothly toward a fixed negative floor instead of either flattening to exactly 0 (like ReLU) or continuing in a straight line (like Leaky ReLU).
- **Softplus**: a smoothed-out version of ReLU — instead of a sharp bend at zero, it curves gently through that region.

**A quick honest check on the source material**: while double-checking this table's numbers, a few of the "range" entries in the original slide look like copy-paste mistakes from wherever the instructor sourced this table (Softplus and Leaky ReLU's ranges, specifically, don't match what those functions actually produce when you work through the math) — noted above so it's clear this was independently verified rather than blindly copied.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Sigmoid hi sirf ek "smoothing function" nahi hai — ye ek poore family ka ek member hai, jise **activation functions** kehte hai, jinme se har ek ka apna shape aur trade-offs hai. Ye topic basically sabse common ones ka ek reference card hai:

- **Linear**: bas number ko seedha bina badle pass kar deta hai. Simple hai, lekin (agla topic explain karega) ek deep network mein akele use hone ke liye bahut simple hai.
- **Binary Step**: ye perceptron ka wahi harsh on/off switch hai jo pehle dekha — sirf comparison ke liye yahan include kiya hai.
- **Sigmoid**: pichle topic wala smooth S-curve, sab kuch 0 se 1 ke range mein squash karta hai.
- **Tanh**: sigmoid ka close cousin hai — same general S-shape, lekin sab kuch **-1 se 1** ke range mein squash karta hai 0 se 1 ke bajaye (isliye ye zero ke around centered hai, jo agle topic mein important nikalta hai).
- **ReLU (Rectified Linear Unit)**: ek extremely simple rule — agar number negative hai, to output exactly 0; agar zero ya positive hai, to use seedha bina badle pass kar do. Ye ek muda hua line jaisa dikhta hai: negative inputs ke liye zero par flat, phir positive inputs ke liye ek straight diagonal line upar jaati hui.
- **Leaky ReLU**: ReLU ke lagbhag identical, lekin negative inputs ko poori tarah zero karne ke bajaye, ye ek chhota fraction (jaise 1%) pass hone deta hai kuch bhi nahi ke bajaye — negative side par bhi ek chhota signal "leak" karta hai.
- **ELU (Exponential Linear Unit)**: positive inputs ke liye ReLU jaisa hai (bina badle pass karta hai), lekin negative inputs ke liye, ye ek fixed negative floor ki taraf smoothly curve karta hai, exactly 0 par flatten hone (ReLU jaisa) ya seedhi line mein continue hone (Leaky ReLU jaisa) ke bajaye.
- **Softplus**: ReLU ka ek smoothed-out version — zero par sharp bend ke bajaye, ye us region mein gently curve karta hai.

**Source material ka ek quick honest check**: is table ke numbers double-check karte time, kuch "range" entries original slide mein copy-paste mistakes jaisi lagti hai (jahan se instructor ne ye table liya hoga) — Softplus aur Leaky ReLU ke ranges specifically, jab math kaam karte hai to wo actually jo produce hota hai usse match nahi karte — upar note kar diya hai taaki clear ho ki ye independently verify kiya gaya hai, bas copy nahi kiya.
