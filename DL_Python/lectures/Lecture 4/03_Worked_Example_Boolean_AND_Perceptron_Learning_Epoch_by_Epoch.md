# Topic 3: Worked Example — Learning the Boolean AND Function, Epoch by Epoch

Source: Lecture 4, slides 10–16 (Example: Perceptron Algorithm for Boolean AND Function — set-up ×2, then Epoch 1, 2, 3, 4 tables). Slides 12–13 carry the instructor's handwritten working; the Epoch 3 and Epoch 4 tables (slides 14–15) are **blank templates** on the slides and are completed here.

---

## 1) Technical Explanation

**Set-up (slides 10–11).** Represent Boolean **AND** with a perceptron:

- initial weights **w₁ = 0.3, w₂ = −0.2**, learning rate **α = 0.2**, threshold/bias **θ = 0.4**;
- activation = **step function**: output 1 if f(x) ≥ 0, else 0, applied to **(x₁w₁ + x₂w₂) − θ**;
- training data (desired outputs Y_des): (0,0)→0, (0,1)→0, (1,0)→0, (1,1)→1. Update the weights until the function gives the desired output.

Update rule (from [[02_Perceptron_Learning_Algorithm_Steps_and_Update_Rule]]): e = Y_des − Y_est, Δwᵢ = α·e·xᵢ, wᵢ ← wᵢ + Δwᵢ. θ is not changed.

**Epoch 1 (slide 12, instructor's working).** Start w = (0.3, −0.2).

| x₁ | x₂ | Y_des | (x₁w₁ + x₂w₂) − 0.4 | Y_est | Error | w₁ | w₂ | Status |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 − 0.4 = −0.4 | 0 | 0 | 0.3 | −0.2 | no change |
| 0 | 1 | 0 | −0.2 − 0.4 = −0.6 | 0 | 0 | 0.3 | −0.2 | no change |
| 1 | 0 | 0 | 0.3 − 0.4 = −0.1 | 0 | 0 | 0.3 | −0.2 | no change |
| 1 | 1 | 1 | 0.3 − 0.2 − 0.4 = −0.3 | 0 | **+1** | **0.5** | **0.0** | change |

Update for (1,1): Δw₁ = 0.2 × 1 × 1 = 0.2 → w₁ = 0.3 + 0.2 = 0.5; Δw₂ = 0.2 × 1 × 1 = 0.2 → w₂ = −0.2 + 0.2 = 0. (Matches the slide.)

**Epoch 2 (slide 13).** Start w = (0.5, 0).

| x₁ | x₂ | Y_des | sum − 0.4 | Y_est | Error | w₁ | w₂ | Status |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | −0.4 | 0 | 0 | 0.5 | 0 | no change |
| 0 | 1 | 0 | 0 − 0.4 = −0.4 | 0 | 0 | 0.5 | 0 | no change |
| 1 | 0 | 0 | 0.5 − 0.4 = **0.1** | **1** | **−1** | **0.3** | 0 | change |
| 1 | 1 | 1 | 0.3 + 0 − 0.4 = −0.1 | 0 | **+1** | **0.5** | **0.2** | change |

Updates: for (1,0): Δw₁ = 0.2 × (−1) × 1 = −0.2 → w₁ = 0.5 − 0.2 = 0.3, Δw₂ = 0.2 × (−1) × 0 = 0 → w₂ = 0. For (1,1): Δw₁ = Δw₂ = 0.2 → w = (0.5, 0.2). The slide's own handwriting notes the weights carried into epoch 3 are **w₁ = 0.5, w₂ = 0.2**. (Matches.)

**Epoch 3 (slide 14 gives only the starting weights 0.5, 0.2; completed here).**

| x₁ | x₂ | Y_des | sum − 0.4 | Y_est | Error | w₁ | w₂ | Status |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | −0.4 | 0 | 0 | 0.5 | 0.2 | no change |
| 0 | 1 | 0 | 0.2 − 0.4 = −0.2 | 0 | 0 | 0.5 | 0.2 | no change |
| 1 | 0 | 0 | 0.5 − 0.4 = 0.1 | 1 | −1 | **0.3** | 0.2 | change |
| 1 | 1 | 1 | 0.3 + 0.2 − 0.4 = 0.1 | 1 | 0 | 0.3 | 0.2 | no change |

**Epoch 4 (slide 15 blank; completed here).** Start w = (0.3, 0.2).

| x₁ | x₂ | Y_des | sum − 0.4 | Y_est | Error | w₁ | w₂ | Status |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | −0.4 | 0 | 0 | 0.3 | 0.2 | no change |
| 0 | 1 | 0 | 0.2 − 0.4 = −0.2 | 0 | 0 | 0.3 | 0.2 | no change |
| 1 | 0 | 0 | 0.3 − 0.4 = −0.1 | 0 | 0 | 0.3 | 0.2 | no change |
| 1 | 1 | 1 | 0.3 + 0.2 − 0.4 = 0.1 | 1 | 0 | 0.3 | 0.2 | no change |

**Converged.** A complete epoch with **no errors** means training is finished. Final perceptron: **w₁ = 0.3, w₂ = 0.2, θ = 0.4**, i.e. output 1 iff 0.3x₁ + 0.2x₂ ≥ 0.4. Only (1,1) gives 0.5 ≥ 0.4; the other inputs give 0, 0.2, 0.3 — all below 0.4. ✓

**Verification note.** Every row of the tables (including the slide's handwritten Epochs 1 and 2) was recomputed by a small script; all values match, and Epochs 3–4 are the continuation of the same algorithm. The stopping rule ("a full epoch without any error") is the standard criterion; the slides do not state it explicitly.

**Geometry.** The final boundary 0.3x₁ + 0.2x₂ = 0.4 is a line passing between (1,1) and the other three corners — exactly the picture of a linearly separable problem from [[07_Linear_Separability_and_the_OR_Problem]] in Lecture 3, but found by **learning** instead of by hand. Notice also that a different starting point or order of samples would give a *different* but equally valid line — the solution is not unique.

---

## 2) Simple English Explanation

**Goal:** teach a perceptron the AND rule — output 1 only when **both** inputs are 1.

**Starting guess:** weight 1 = 0.3, weight 2 = −0.2, threshold 0.4, learning rate 0.2.

**How a single check works:** multiply, add, subtract 0.4; if the result is 0 or more, say 1, otherwise say 0.

**Epoch 1** (go through all four cases): the first three cases are answered correctly (0, 0, 0). The fourth (1,1) should be 1 but the perceptron says 0 — a mistake. So raise both weights by 0.2 × 1 × 1 = 0.2: weights become 0.5 and 0.0.

**Epoch 2:** now (1,0) wrongly gives 1 (0.5 − 0.4 = 0.1 ≥ 0). Lower weight 1 by 0.2 → 0.3. Then (1,1) gives 0.3 + 0 − 0.4 = −0.1, wrongly 0, so raise both by 0.2 → weights 0.5 and 0.2.

**Epoch 3:** (1,0) again wrongly gives 1 (0.1) → lower weight 1 to 0.3. Everything else is fine. Weights 0.3 and 0.2.

**Epoch 4:** all four cases are now right (0, 0, 0, 1). No mistakes means we **stop**. Final: weights 0.3 and 0.2, threshold 0.4. Check: only (1,1) reaches 0.3 + 0.2 = 0.5 ≥ 0.4.

(The slide gives the empty tables for epochs 3 and 4; the numbers above fill them in.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Goal:** perceptron ko AND ka rule sikhana — output 1 sirf tab jab **dono** inputs 1 hon.

**Shuruaati guess:** weight 1 = 0.3, weight 2 = −0.2, threshold 0.4, learning rate 0.2.

**Ek check kaise hota hai:** multiply karo, jodo, 0.4 ghatao; agar result 0 ya usse zyada ho to 1 bolo, warna 0.

**Epoch 1** (chaaron cases dekho): pehle teen cases sahi nikle (0, 0, 0). Chauthe (1,1) ka jawab 1 hona chahiye par perceptron 0 bolta hai — galti. To dono weights ko 0.2 × 1 × 1 = 0.2 se badhao: weights 0.5 aur 0.0 ho gaye.

**Epoch 2:** ab (1,0) galti se 1 deta hai (0.5 − 0.4 = 0.1 ≥ 0). Weight 1 ko 0.2 se ghatao → 0.3. Phir (1,1) ka 0.3 + 0 − 0.4 = −0.1 aata hai, galti se 0, to dono ko 0.2 se badhao → weights 0.5 aur 0.2.

**Epoch 3:** (1,0) phir galti se 1 deta hai (0.1) → weight 1 ghatakar 0.3. Baaki sab theek. Weights 0.3 aur 0.2.

**Epoch 4:** ab chaaron cases sahi hain (0, 0, 0, 1). Koi galti nahi matlab **ruk jao**. Final: weights 0.3 aur 0.2, threshold 0.4. Check: sirf (1,1) ka 0.3 + 0.2 = 0.5 ≥ 0.4 hota hai.

(Slide mein epoch 3 aur 4 ke tables khaali hain; upar ke numbers unhe bharte hain.)
