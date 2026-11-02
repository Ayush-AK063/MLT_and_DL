# Topic 0: Recap — What Gradient Descent Is, and Its Three Types

Source: Lecture 11 (ES532: Introduction to Deep Learning), slides 2 and 4.

---

## 1) Technical Explanation

This lecture opens by repeating, **verbatim**, two slides already covered in this repo in Lecture 10:

1. The **definition of Gradient Descent** — an optimization technique/algorithm, mostly used in supervised ML and deep learning, called a "first-order optimization algorithm" because it only uses first-derivative (slope) information, and the literal breakdown of the name ("gradient" = slope, "descent" = movement to a lower point) — already covered in full in [[05_Loss_Function_and_the_Meaning_of_Gradient_Descent]] from Lecture 10.
2. The **three types of gradient descent** — Batch (entire dataset), Stochastic (1 data point), Mini-Batch (small batch) — framed around the goal $\min_\theta J(\theta)$ where $\theta$ is the parameter set — already covered, with the same cross-reference back to Lecture 0's [[02_Batch_Stochastic_and_MiniBatch_Gradient_Descent]], in [[06_Types_of_Gradient_Descent_Revisited]] from Lecture 10.

Per the usual convention, this file just links back rather than re-deriving identical content a third time across three lectures. **Why the repetition makes sense pedagogically**: this lecture's actual new content — starting with [[02_SGD_BGD_and_MBGD_Compared_in_Detail]] — goes substantially *deeper* into the same three types than either Lecture 0 or Lecture 10 did (practical trade-offs, when to use which, pseudocode, worked memory-sizing examples), so restating the basic definitions and names one more time before diving into that depth is a reasonable way to make sure nothing is assumed.

---

## 2) Simple English Explanation

This lecture starts with two slides you've already seen twice now (once in Lecture 0, once in Lecture 10): what gradient descent literally means (follow the slope downhill), and the three ways of deciding how much data to look at per update step (batch, stochastic, mini-batch).

Since this is identical to what's already covered — see [[05_Loss_Function_and_the_Meaning_of_Gradient_Descent]] and [[06_Types_of_Gradient_Descent_Revisited]], both from Lecture 10 — there's no need to go through it a third time here.

**Why show it again?** This lecture is about to go much deeper into these same three types than the last two lectures did — real trade-offs, pseudocode, and worked examples with actual numbers — so it makes sense to briefly remind you of the basics one more time before diving into that depth.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture do slides se shuru hoti hai jo tumne ab do baar dekh liya hai (ek baar Lecture 0 mein, ek baar Lecture 10 mein): gradient descent ka literally kya matlab hai (slope ko neeche follow karo), aur teen tarike decide karne ke ki har update step mein kitna data dekhna hai (batch, stochastic, mini-batch).

Kyunki ye bilkul wahi hai jo already cover ho chuka hai — [[05_Loss_Function_and_the_Meaning_of_Gradient_Descent]] aur [[06_Types_of_Gradient_Descent_Revisited]] dekho, dono Lecture 10 se — isse yahan teesri baar karne ki zaroorat nahi.

**Ise dobara kyun dikhaya?** Ye lecture in teeno types mein pichli do lectures se bahut zyada depth mein jaane wali hai — real trade-offs, pseudocode, aur real numbers wale worked examples — isliye us depth mein jaane se pehle basics ek aur baar briefly yaad dilaana samajh mein aata hai.
