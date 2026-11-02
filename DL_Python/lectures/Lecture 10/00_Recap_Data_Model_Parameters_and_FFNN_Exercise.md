# Topic 0: Recap — Data/Model/Parameters Framing and the FFNN Exercise

Source: Lecture 10 (ES532: Introduction to Deep Learning), slides 2–3.

---

## 1) Technical Explanation

This lecture opens by repeating, **verbatim**, two things already covered in this repo in Lecture 9:

1. The **Data / Model / Parameters / Algorithm / Objective** framing for a feedforward network — the exact same slide, with the same $\{x_i,y_i\}_{i=1}^N$ data notation, the same composed model equation $\hat{y}_i = f(x_i) = O(W_3 g(W_2 g(W_1 x_i+b_1)+b_2)+b_3)$, the same parameter set $\theta = W_1,\dots,W_L,b_1,\dots,b_L$, "Gradient Descent with Backpropagation" as the algorithm, and the same squared-error objective — already covered in full in [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]] from Lecture 9.
2. The exact same **worked FFNN exercise** (2 inputs, two 2-neuron hidden layers, 2 outputs, sigmoid activation, all weights/biases/targets given) already solved end-to-end in [[05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN]] from Lecture 9, including the full forward-pass computation ($\hat{y}_1\approx0.7048$, $\hat{y}_2\approx0.5796$ against targets $0,1$).

Per the usual convention for recap slides that repeat earlier material word-for-word, this file just points back rather than re-deriving. **Why the instructor repeats this here**: this lecture is specifically about *gradient descent* — the algorithm named in that "Algorithm" line — so restating exactly what needs to be minimized (the loss/objective from the Data/Model/Parameters framing) and exactly what network the previous exercise's forward pass belongs to sets up the natural next question this lecture actually answers: **now that we have a prediction and a target, how do we use gradient descent to close the gap between them?**

---

## 2) Simple English Explanation

This lecture starts by showing you two things you've already seen in the previous lecture, word for word: the "Data / Model / Parameters / Algorithm / Loss" checklist for describing a learning problem, and the same tiny example network exercise you already worked through by hand (where the network's prediction came out to about 0.70 and 0.58, while the real answers should have been 0 and 1).

Since both of these are identical to what's already covered — see [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]] and [[05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN]], both from Lecture 9 — there's no need to redo them here.

**Why show them again?** This lecture is specifically about gradient descent — the very algorithm named in that checklist's "Algorithm" line. Before diving into *how* gradient descent works, it makes sense to remind you exactly *what* it's trying to minimize (the gap between a prediction and the real answer), using the same concrete example you already computed a prediction for. That sets up the natural question this lecture goes on to answer: now that we know the network is wrong by a certain amount, how do we actually use that to fix the weights?

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture do cheezein dikha kar shuru hoti hai jo tumne pichli lecture mein already dekhi hai, word for word: "Data / Model / Parameters / Algorithm / Loss" wala checklist kisi learning problem ko describe karne ke liye, aur wahi chhota sa example network exercise jo tumne hand se solve kiya tha (jahan network ki prediction lagbhag 0.70 aur 0.58 aayi thi, jabki real answers 0 aur 1 hone chahiye the).

Kyunki ye dono bilkul same hai jo already cover ho chuka hai — [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]] aur [[05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN]] dekho, dono Lecture 9 se — inhe yahan dobara karne ki zaroorat nahi.

**Inhe dobara kyun dikhaya?** Ye lecture specifically gradient descent ke baare mein hai — wahi algorithm jo us checklist ki "Algorithm" line mein naam liya gaya tha. Gradient descent *kaise* kaam karta hai wahan jaane se pehle, ye yaad dilaana samajh mein aata hai ki ye *kya* minimize karne ki koshish kar raha hai (prediction aur real answer ke beech ka gap), usi concrete example use karke jiski prediction tumne already compute ki thi. Isse ye natural sawaal set up hota hai jo ye lecture aage answer karti hai: ab jab hume pata hai ki network kitna galat hai, hum use actually weights fix karne ke liye kaise use karein?
