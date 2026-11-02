# Topic 6: A Simple Artificial Neural Network (Network of Perceptron-Style Units)

Source: Lecture 3, slide 29 (Artificial Neural Network — "A simple model").

---

## 1) Technical Explanation

The slide has one figure and the caption "A simple model": a small **feed-forward network** drawn left to right.

- **Inputs:** x₁, x₂ and a **bias unit b** whose value is fixed at 1 (the "1" labels on its edges).
- **Middle layer:** **three units**, each receiving **every** input through its own weight (each edge is labelled with a w and subscripts on the slide; the exact index convention is not explained), so the inputs are *fully connected* to this layer.
- **Output layer:** **two outputs, out₁ and out₀**, each fed by all three hidden units.

This is the picture of "perceptrons joined into a network": each unit computes a weighted sum plus bias and an activation, exactly as in [[03_The_Perceptron_Function]], and its output becomes the input of the next layer. The bias is drawn as an extra input fixed at 1 — the same trick as the "1 with weight w₀" in [[01_Recap_Perceptron_Introduction_and_Perceptron_Rule]].

Why join units? A single perceptron only draws one straight line ([[07_Linear_Separability_and_the_OR_Problem]]); layers of units can build curved boundaries, the solution to XOR ([[08_Linear_Non_Separability_XOR_and_Hyperplanes]]; implemented in Lecture 7) and the multilayer perceptrons of Lecture 6. The formal notation for such networks is developed in Lecture 9 ([[01_Feedforward_Network_Architecture_Layers_and_Notation]]).

---

## 2) Simple English Explanation

The picture shows a tiny "brain": two inputs on the left (plus a constant "1" that carries the bias), a middle row of three small decision-makers, and two outputs on the right. Every input is connected to every middle unit, and every middle unit to both outputs; each line carries a weight (importance number). Each unit does what a perceptron does — multiply, add, decide — and passes the result forward.

Joining several simple units like this lets the network do things one unit alone cannot.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Picture ek chhota sa "dimaag" dikhati hai: left mein do inputs (aur ek constant "1" jo bias carry karta hai), beech mein teen chhote decision-makers ki ek row, aur right mein do outputs. Har input har beech wale unit se juda hai, aur har beech wala unit dono outputs se; har line par ek weight (importance number) hai. Har unit wahi karta hai jo perceptron karta hai — multiply, add, decide — aur result aage bhej deta hai.

Aise kai simple units ko jodne se network wo kaam kar sakta hai jo akela ek unit nahi kar sakta.
