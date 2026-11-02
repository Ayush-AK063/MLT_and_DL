# Lecture 9 — Feedforward Neural Networks (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 09 FFNN.pdf` — Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Read in full (all 16 slides).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Activation_Functions_Table.md](00_Recap_Activation_Functions_Table.md) | Recap: the same activation-function table from Lecture 8, linked back rather than re-derived |
| [01_Feedforward_Network_Architecture_Layers_and_Notation.md](01_Feedforward_Network_Architecture_Layers_and_Notation.md) | Layers, pre-activation vs. activation, 0-to-L numbering, weight/bias dimensions |
| [02_PreActivation_and_Activation_Equations.md](02_PreActivation_and_Activation_Equations.md) | The $a_i = b_i + W_i h_{i-1}$ and $h_i = g(a_i)$ equations, with a worked matrix illustration |
| [03_Output_Layer_and_Full_Network_Function.md](03_Output_Layer_and_Full_Network_Function.md) | The output activation function $O$ (softmax for classification, linear for regression) |
| [04_Formalizing_the_Learning_Problem_Data_Model_Parameters.md](04_Formalizing_the_Learning_Problem_Data_Model_Parameters.md) | Data/Model/Parameters/Algorithm/Loss framing, the full composed network equation, loss vs. cost |
| [05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN.md](05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN.md) | The slide's own unsolved exercise, worked and verified by hand end to end |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- **Recap handled per convention**: slide 2 repeats Lecture 8's activation-function table verbatim — rather than re-deriving it, [[00_Recap_Activation_Functions_Table]] just links back to Lecture 8's [[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]] (which already flagged and fixed the table's own range errors).
- **Worked example added, not just transcribed**: slide 16 poses a fully-specified toy feedforward network (2 inputs, two 2-neuron hidden layers, 2 outputs, all weights/biases/targets given, sigmoid activation) as an unsolved "Exercise" — the source PDF gives no answer. [[05_Worked_Exercise_Forward_Pass_Through_a_Sample_FFNN]] computes the complete forward pass by hand (verified numerically): $\hat{y}_1 \approx 0.7048$, $\hat{y}_2 \approx 0.5796$ against targets $(0, 1)$. The backward pass (adjusting the weights via backpropagation) is explicitly left open, since that algorithm is introduced in a later lecture not yet in this repo — noted so this isn't mistaken for a finished/abandoned calculation.
- **Cross-references to Lecture 8**: this lecture builds directly on Lecture 8's sigmoid neuron and activation-function material — see the `[[...]] from Lecture 8` links inside topics 00 and 03.
- **Web research added**: the Universal Approximation Theorem (Cybenko 1989; Hornik, Stinchcombe & White 1989) is introduced in [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]] as the theoretical justification for why this layered architecture can represent the "arbitrary functions" Lecture 8 opened with — and the softmax function's actual formula (named but not defined on the slide) is given in full in [[03_Output_Layer_and_Full_Network_Function]].
- No anomalies or out-of-place content flagged in this lecture — it's a tightly-scoped, self-contained build-up from "what is a layer" to "here's a network you can hand-compute."
