# Topic 2: The Perceptron Learning Algorithm — Steps and the Weight-Update Rule

Source: Lecture 4, slides 8–9 (Perceptron Learning Algorithm — text slide; the block diagram).

---

## 1) Technical Explanation

The slide states the algorithm in words. Reproduced faithfully:

**Initialisation.** Set the initial weights w₁, w₂, …, wₙ and the bias (threshold) θ to random values in the range **[−0.5, 0.5]**.

**For each epoch** (one pass over the training data), for each training sample:

1. **Compute the weighted sum** by multiplying the inputs by the weights and adding the products.
2. **Apply the activation function** to the weighted sum:

   Y = Step( (x₁w₁ + x₂w₂) − θ )

3. If the sum is above the threshold, output **positive** (1); otherwise **negative** (0).
4. **Calculate the error:** e(t) = Y_desired − Y_estimated.
6. **Update the weights if there is an error:**

   Δwᵢ = α × e(t) × xᵢ
   wᵢ = wᵢ + Δwᵢ

   where xᵢ is the input value, e(t) the error at step t, **α the learning rate**, and Δwᵢ the amount added to wᵢ.

**Flag — missing step 5.** The slide numbers its steps 1, 2, 3, 4, **6** — there is no step 5. Nothing appears to be missing from the logic (the text flows directly from computing the error to updating the weights); it is a numbering slip. Likewise the slide gives the update for the **weights only**; the threshold θ is not updated in the worked example that follows ([[03_Worked_Example_Boolean_AND_Perceptron_Learning_Epoch_by_Epoch]] keeps θ = 0.4 throughout). In the more common textbook form the bias is treated as a weight on a constant input 1 and *is* updated by the same rule (Δb = α·e); the slide does not do that.

**How to read the update rule.**

| Situation | e = Y_desired − Y_est | Effect on wᵢ (xᵢ > 0) |
|---|---|---|
| Correct output | 0 | no change |
| Output 0 but should be 1 (too low) | +1 | wᵢ **increases** by α·xᵢ → sum goes up |
| Output 1 but should be 0 (too high) | −1 | wᵢ **decreases** by α·xᵢ → sum goes down |

Inputs that are 0 contribute nothing (Δwᵢ = α·e·0 = 0), so only the weights of *active* inputs move — the Hebbian flavour noted in [[01_Perceptron_Learning_Model_McCulloch_Pitts_plus_Hebbian_Learning]]. The learning rate α scales how big each correction is (too large can overshoot, too small learns slowly — the same trade-off met again with gradient descent in Lecture 0, [[01_What_Is_Gradient_Descent_and_the_Learning_Rate]]).

**Convergence (background, not on the slide).** The *perceptron convergence theorem* (Novikoff, 1962) states that if the training data are linearly separable, this rule finds a separating set of weights in a finite number of updates. If the data are not linearly separable (e.g. XOR, [[08_Linear_Non_Separability_XOR_and_Hyperplanes]]), the weights never settle and the algorithm cycles forever — in practice a maximum epoch count is used.

---

## 2) Simple English Explanation

How the perceptron teaches itself:

1. **Start with random guesses** for the weights and the threshold (small numbers between −0.5 and 0.5).
2. Go through the examples **one at a time**. For each: multiply inputs by weights, add up, subtract the threshold, and decide — 1 if the result is zero or more, 0 if not.
3. Compare with the **correct answer**: error = correct − guess.
4. If the error is not zero, **fix the weights**: add (learning rate × error × input) to each weight.
5. One full pass through all examples is an **epoch**. Repeat epochs until a whole pass has no errors.

*Intuition:* if the perceptron said "no" but should have said "yes", it raises the weights of the inputs that were on, so next time the total is bigger. If it said "yes" but should have said "no", it lowers them. The learning rate says how big a step to take.

(Small note: the slide's list jumps from step 4 to step 6 — just a numbering slip.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

Perceptron khud ko kaise sikhata hai:

1. **Random guesses se shuru karo** weights aur threshold ke liye (−0.5 aur 0.5 ke beech chhote numbers).
2. Examples ko **ek-ek karke** dekho. Har ek ke liye: inputs ko weights se multiply karo, jodo, threshold ghatao, aur decide karo — agar result zero ya usse zyada ho to 1, warna 0.
3. **Sahi jawab** se compare karo: error = sahi − guess.
4. Agar error zero nahi hai, to **weights theek karo**: har weight mein (learning rate × error × input) jodo.
5. Saare examples par ek poora pass ek **epoch** hai. Epochs tab tak dohrao jab tak ek poore pass mein koi error na aaye.

*Intuition:* agar perceptron ne "naa" bola par "haan" hona chahiye tha, to wo un inputs ke weights badhata hai jo on the, taaki agli baar total bada ho. Agar usne "haan" bola par "naa" hona chahiye tha, to weights ghatata hai. Learning rate batata hai ki kitna bada kadam lena hai.

(Chhoti baat: slide ki list step 4 se seedhe step 6 par chali jaati hai — bas numbering ki chook hai.)
