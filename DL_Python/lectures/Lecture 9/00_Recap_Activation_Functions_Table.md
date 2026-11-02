# Topic 0: Recap — The Activation Functions Table

Source: Lecture 9 (ES532: Introduction to Deep Learning), slide 2.

---

## 1) Technical Explanation

This lecture opens with a recap slide reproducing, **verbatim, the exact same activation-function comparison table** already covered in this repo in Lecture 8 — see [[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]] from Lecture 8, which lists the equation, derivative, and range for Linear, Binary Step, Sigmoid, Tanh, ReLU, Softplus, Leaky ReLU, and ELU, all cited to the same source (iq.opengenus.org).

Per the usual workflow for recap slides that repeat earlier material word-for-word: rather than re-explaining the table from scratch here, this file simply points back to the earlier lecture. **One thing worth re-flagging**: Lecture 8's notes already caught and documented that this table's own "Range" column has a couple of errors (Softplus's actual range is $(0,\infty)$, not the $(0,1)$ printed; Leaky ReLU's actual range is $(-\infty,\infty)$, not $(-1,1)$) — that correction, made once in Lecture 8, still applies here since it's the identical table.

**Why the instructor likely repeats it here**: this lecture goes on to build actual feedforward networks that need a choice of activation function $g$ at each hidden layer and a (possibly different) output activation function $O$ at the final layer (see [[03_Output_Layer_and_Full_Network_Function]]) — so having the full menu of options freshly in view, right before it gets used in the network equations, makes sense pedagogically.

---

## 2) Simple English Explanation

This lecture starts by showing the exact same activation-function reference table you already saw in the previous lecture (the one comparing Linear, Sigmoid, Tanh, ReLU, and a few others, side by side). Since it's word-for-word identical, there's no need to explain it all over again — see [[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]] from Lecture 8 for the full breakdown, including a couple of small mistakes we spotted in the table's numbers there.

The likely reason it's shown again here: this lecture is about to build a real, working multi-layer network, and every layer of that network needs you to pick one of these functions to use — so it makes sense to have the full menu freshly in front of you right before you start using it.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture bilkul wahi activation-function reference table dikha kar shuru hoti hai jo tumne pichli lecture mein dekhi thi (Linear, Sigmoid, Tanh, ReLU, aur kuch aur, side by side compare karti hui). Kyunki ye word-for-word identical hai, ise dobara se explain karne ki zaroorat nahi — poora breakdown ke liye [[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]] Lecture 8 mein dekho, jahan humne table ke numbers mein kuch chhoti galtiyan bhi pakdi thi.

Ise yahan dobara dikhane ki likely wajah: ye lecture ab ek real, working multi-layer network banane wali hai, aur us network ki har layer ko in functions mein se ek choose karna padta hai use karne ke liye — isliye pura menu freshly saamne rakhna samajh mein aata hai, use karna shuru karne se just pehle.
