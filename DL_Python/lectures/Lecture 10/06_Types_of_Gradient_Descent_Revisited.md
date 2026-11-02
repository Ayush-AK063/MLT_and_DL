# Topic 6: The Types of Gradient Descent, Revisited

Source: Lecture 10 (ES532: Introduction to Deep Learning), slide 23 (numbered 26 in the printed corner).

---

## 1) Technical Explanation

This slide states the formal optimization goal — $\min_\theta J(\theta)$, where $\theta$ represents the parameters (weights and biases) — and then names the same **three variants of gradient descent** already covered in full depth in this repo's Lecture 0, [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]]:

1. **Batch Gradient Descent**: uses the **entire dataset** to compute each weight update.
2. **Stochastic Gradient Descent (SGD)**: uses **1 data point at a time**.
3. **Mini-Batch Gradient Descent**: uses a **small batch of data** at a time.

These are exactly the same three variants, same trade-offs (accuracy vs. speed per update, memory constraints, ability to do online learning), already explained with formulas and code sketches in Lecture 0's topic 02 — this slide is a compact, one-line-per-variant restatement rather than new material, so rather than re-deriving the trade-offs here again, this note points back to that fuller treatment.

**What's new here, worth calling out**: this slide explicitly frames the choice of gradient descent variant as a sub-decision *within* the broader optimization goal $\min_\theta J(\theta)$ — i.e., "which subset of the data do I use to estimate the gradient of $J$ at each step" is a separate design choice from "how do I use that gradient once I have it" (the subject of momentum, Adam, and the other algorithms from Lecture 0's [[04_Momentum]] onward). Both kinds of choices apply simultaneously in practice — e.g., "mini-batch gradient descent with the Adam optimizer" is a complete, specific training recipe combining one choice from each category.

---

## 2) Simple English Explanation

This slide restates something you've already learned in detail back in Lecture 0: there are three ways to decide **how much data to look at** before making one weight-update step.

1. **Batch**: look at *everything* before each update.
2. **Stochastic (SGD)**: look at just *one* example before each update.
3. **Mini-batch**: look at a *small handful* of examples before each update.

If any of these need a refresher on the actual trade-offs (why you'd pick one over another), see [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]] from Lecture 0 — this slide doesn't add anything new to that explanation, it's just a quick reminder, framed alongside the formal goal of "minimize the loss function $J(\theta)$ over the parameters $\theta$."

**One thing worth noticing, though**: "how much data to look at per step" (batch vs. SGD vs. mini-batch) is a completely separate decision from "what to actually *do* with the gradient once you've computed it" (plain updates, momentum, Adam, etc. — also from Lecture 0). In real training, you pick one option from each category at the same time — for example, "mini-batch gradient descent, using the Adam optimizer" is a common, complete combination of both choices.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye slide wo cheez dobara batati hai jo tumne Lecture 0 mein detail mein already seekhi thi: teen tarike hai decide karne ke ki har weight-update step lene se pehle **kitna data dekhna hai**.

1. **Batch**: har update se pehle *sab kuch* dekho.
2. **Stochastic (SGD)**: har update se pehle sirf *ek* example dekho.
3. **Mini-batch**: har update se pehle examples ka ek *chhota handful* dekho.

Agar inme se kisi ke actual trade-offs (kyun ek dusre se better hai) ka refresher chahiye, to [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]] Lecture 0 se dekho — ye slide us explanation mein kuch naya add nahi karti, ye bas ek quick reminder hai, formal goal "loss function $J(\theta)$ ko parameters $\theta$ ke upar minimize karo" ke saath framed.

**Ek baat jo notice karne layak hai though**: "har step ke liye kitna data dekhna hai" (batch vs. SGD vs. mini-batch) ek bilkul alag decision hai "gradient compute karne ke baad actually usse *kya* karna hai" se (plain updates, momentum, Adam, etc. — Lecture 0 se bhi). Real training mein, tum ek option har category se ek saath choose karte ho — jaise, "mini-batch gradient descent, Adam optimizer use karke" dono choices ka ek common, complete combination hai.
