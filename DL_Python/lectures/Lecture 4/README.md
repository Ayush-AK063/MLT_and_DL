# Lecture 4 — Perceptron Learning Algorithm (ES532: Introduction to Deep Learning)

Source PDF: `Lecture-4 Perceptron Learning.pdf` — 16 slides, read in full (several slides are images with handwritten working, so they were read visually).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Exercise_Linear_Separability_and_Designing_a_Perceptron.md](00_Recap_Exercise_Linear_Separability_and_Designing_a_Perceptron.md) | Opening exercise: separable? design a perceptron (x₁ − x₂ − 1.5 = 0) |
| [01_Perceptron_Learning_Model_McCulloch_Pitts_plus_Hebbian_Learning.md](01_Perceptron_Learning_Model_McCulloch_Pitts_plus_Hebbian_Learning.md) | The model: McCulloch–Pitts neuron + Hebbian weight adjustment; 4 parts |
| [02_Perceptron_Learning_Algorithm_Steps_and_Update_Rule.md](02_Perceptron_Learning_Algorithm_Steps_and_Update_Rule.md) | The algorithm and Δwᵢ = α·e·xᵢ |
| [03_Worked_Example_Boolean_AND_Perceptron_Learning_Epoch_by_Epoch.md](03_Worked_Example_Boolean_AND_Perceptron_Learning_Epoch_by_Epoch.md) | Learning AND over 4 epochs, every row tabulated |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Verified:** the exercise's separating perceptron was checked on all 7 points; the full AND-learning run (Epochs 1–4) was recomputed by script and matches the instructor's handwritten Epoch 1–2 working exactly.
- **Completed:** the Epoch 3 and Epoch 4 tables are blank templates on the slides (Epoch 3 shows only the starting weights 0.5, 0.2). They are filled in here by running the same algorithm — noted explicitly in the file.
- **Flag — missing step 5:** the algorithm slide numbers its steps 1, 2, 3, 4, 6. Treated as a numbering slip.
- **Flag — θ is never updated:** the slide's update rule changes only the weights; the worked example keeps θ = 0.4. Many textbooks also update the bias; noted in topic 02.
- **Flag — two threshold conventions:** this lecture uses Y = 1 if Σxᵢwᵢ ≥ θ; Lecture 3 uses w·x + b > 0 (b = −θ).
- **Background added (not on slides):** Hebb's rule (1949) and the perceptron convergence theorem (Novikoff, 1962), each labelled as background.
- Slides 4 and 7 repeat earlier material (Cornell/1960 line; the annotated perceptron diagram) — linked back to Lecture 3, not re-explained.
- This lecture links forward to Lecture 5 (McCulloch–Pitts neuron) for the neuron model that learning builds on.
