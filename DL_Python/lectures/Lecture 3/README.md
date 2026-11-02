# Lecture 3 — Single Layer Perceptron (ES532: Introduction to Deep Learning)

Source PDF: `Lecture-3 Single Layer Perceptron.pdf` — 34 slides (title slide reads "Perceptron"), read in full including all handwritten-annotation slides (the PDF has almost no extractable text, so every slide was read as an image).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Can_You_See_Mistakes_in_the_Network.md](00_Can_You_See_Mistakes_in_the_Network.md) | Opening hook: networks are hard to inspect; backward information flow |
| [01_Recap_Perceptron_Introduction_and_Perceptron_Rule.md](01_Recap_Perceptron_Introduction_and_Perceptron_Rule.md) | Repeated perceptron slides (linked to Lecture 2) + squat example, clean diagrams, the Perceptron rule |
| [02_History_of_the_Perceptron_and_the_Biological_Neuron.md](02_History_of_the_Perceptron_and_the_Biological_Neuron.md) | Rosenblatt, Cornell, 1957–60; neuron analogy; Minsky & Papert |
| [03_The_Perceptron_Function.md](03_The_Perceptron_Function.md) | f(x) = 1 if w·x + b > 0 else 0; meaning of w, b, x, m |
| [04_Iris_Dataset_Features_Targets_and_Problem_Types.md](04_Iris_Dataset_Features_Targets_and_Problem_Types.md) | The Iris dataset, features vs target |
| [05_Regression_vs_Classification_Linear_and_Non_Linear.md](05_Regression_vs_Classification_Linear_and_Non_Linear.md) | Regression vs classification, linear vs non-linear |
| [06_A_Simple_Artificial_Neural_Network_Model.md](06_A_Simple_Artificial_Neural_Network_Model.md) | A small fully-connected network with bias unit |
| [07_Linear_Separability_and_the_OR_Problem.md](07_Linear_Separability_and_the_OR_Problem.md) | Linear separability; OR built as a perceptron (verified) |
| [08_Linear_Non_Separability_XOR_and_Hyperplanes.md](08_Linear_Non_Separability_XOR_and_Hyperplanes.md) | XOR cannot be solved by one perceptron; hyperplanes in n-D |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Overlap with Lecture 2:** slides 4 and 6–14 are the same perceptron slides that close Lecture 2 (the slide counter even continues from it). They are written up once, in Lecture 2's topic 09, and `01_` here links back and covers only what's new (squat example, clean diagrams, Perceptron rule).
- **Verified:** the OR perceptron (w = 1, 1; b = −0.3) was checked on all four input pairs; the XOR impossibility was proven algebraically; NAND and NOR perceptrons were checked on all four inputs.
- **Flag — slide 32's "NAND, NOR problems":** NAND and NOR *are* linearly separable, so they are not examples of non-separability; noted in topic 08.
- **Flag — dates:** the slide says the perceptron was "built at Cornell, 1960"; web sources give 1957 (design/simulation) and 1958 (public demonstration of the Mark I). Both are noted in topic 02.
- **Flag — unverified claim:** slide 3's "10 times more backward than forward connections in the human brain" is reported as stated, not checked.
- **Slide 2 and slide 4** have no content in the PDF (title-only/blank figure).
- Perceptron *learning* (how the weights are updated) is deliberately left to Lecture 4.
- Web research added: Rosenblatt/Mark I/Minsky–Papert context, Fisher's Iris paper and the setosa-separability fact.
