# Lecture 5 — McCulloch–Pitts Neuron and Thresholding Logic (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 05 McCulloch Pitts Neuron and Thresholding logic.pdf` — 30 slides, read in full (the deck is almost entirely figures and handwritten annotations, so every slide was read visually).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [01_McCulloch_Pitts_Neuron_Model_Aggregation_g_and_Decision_f.md](01_McCulloch_Pitts_Neuron_Model_Aggregation_g_and_Decision_f.md) | The 1943 neuron model: binary inputs, aggregation g, decision f; the "rain" and "comedy show" examples |
| [02_Excitatory_and_Inhibitory_Inputs_and_the_Threshold_Rule.md](02_Excitatory_and_Inhibitory_Inputs_and_the_Threshold_Rule.md) | Excitatory vs inhibitory inputs, g(x) = Σxᵢ, y = 1 iff g(x) ≥ θ, "θ > nw − p" |
| [03_Implementing_Boolean_Functions_AND_OR_NOR_NOT_with_MP_Units.md](03_Implementing_Boolean_Functions_AND_OR_NOR_NOT_with_MP_Units.md) | AND (θ=3), OR (θ=1), NOR (θ=0), NOT (θ=0), all truth tables checked |
| [04_Geometric_Interpretation_of_an_MP_Unit_Lines_and_Planes.md](04_Geometric_Interpretation_of_an_MP_Unit_Lines_and_Planes.md) | OR/AND/tautology as lines; the 3-input cube and plane |
| [05_Linear_Separability_of_Boolean_Functions.md](05_Linear_Separability_of_Boolean_Functions.md) | One MP unit ⇔ linearly separable Boolean functions |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Verified:** all gate truth tables (3-input AND/OR, 2-input NOR, NOT) were recomputed by script. The background claim "14 of the 16 two-input Boolean functions (and 104 of the 256 three-input ones) are linearly separable" was confirmed by brute-force search.
- **Interpretation flagged:** the slide's handwritten "θ > nw − p" is not explained on the slide; topic 02 gives the reading (one inhibitory input vetoes all n excitatory ones).
- **Subtle point noted:** MP units use f = 1 iff g(x) ≥ θ, so boundary points count as ON; Lecture 3's perceptron uses a strict >. Equivalent on binary inputs (topic 04).
- **Slide counters skip** a few numbers (e.g. 140, 146, 147) — the PDF flows continuously and no content is missing.
- **Background (not on slides):** the 1943 paper title, universality of NOR/NAND, and the count of separable Boolean functions are labelled as such in the files.
- Lecture 3's [[07_Linear_Separability_and_the_OR_Problem]] and Lecture 4's AND-learning example are the learning-based counterparts of this lecture's hand-chosen thresholds.
- XOR is left open here; it is resolved in Lectures 6 and 7.
