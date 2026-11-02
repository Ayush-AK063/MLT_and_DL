# Lecture 6 — Network of Perceptrons: Multilayer Perceptrons (MLPs) (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 06 Multilayer Perceptron.pdf` — 36 slides, read in full (mostly figures and handwritten annotations, read visually).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_McCulloch_Pitts_Neuron_and_Linear_Separability.md](00_Recap_McCulloch_Pitts_Neuron_and_Linear_Separability.md) | Recap of Lecture 5: the MP neuron, threshold rule, linear separability |
| [01_Implementing_AND_with_an_MP_Neuron_and_Deriving_the_Threshold.md](01_Implementing_AND_with_an_MP_Neuron_and_Deriving_the_Threshold.md) | AND by hand (w = 1,1; θ = 2); "no training algorithm"; the θ > nw − p flag |
| [02_Network_of_Perceptrons_MLP_Introduction.md](02_Network_of_Perceptrons_MLP_Introduction.md) | The 2-input, 4-perceptron network: ±1 weights, bias −2, one-hot hidden layer |
| [03_Terminology_Input_Hidden_and_Output_Layers_and_Layer_Weights.md](03_Terminology_Input_Hidden_and_Output_Layers_and_Layer_Weights.md) | Input / hidden / output layers, h₁–h₄, layer 1 and layer 2 weights |
| [04_Claim_Any_Boolean_Function_Using_One_Hidden_Layer_of_Perceptrons.md](04_Claim_Any_Boolean_Function_Using_One_Hidden_Layer_of_Perceptrons.md) | The "any Boolean function" claim, XOR, and its limits |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Recap (slides 2–5)** repeats Lecture 5 and a textbook-style MP-neuron slide; written as `00_` with links back, not re-derived.
- **Verified:** the AND derivation (w = 1,1; θ = 2); the hidden-layer table (exactly one unit fires per input); and the claim itself — with output weights from {0,1}⁴ and threshold 1, **all 16** two-input Boolean functions (including XOR) are realised.
- **Flag — θ > nw − p:** applied literally to AND it would give θ > 2 (never fires). The instructor's own working uses ≥ and gets θ = 2; the veto condition is irrelevant when there are no inhibitory inputs. Explained in topic 01.
- **Flag — OR slide (8) is title-only** in this deck; its answer (θ = 1) comes from Lecture 5.
- **Flag — layer counting:** the deck calls the network "3 layers" (input counted); other books say 2-layer. Noted in topic 03.
- **Inferred, not on slides:** the output neuron's threshold/activation is not specified on the slides; topic 04 picks "output 1 iff Σ wᵢhᵢ ≥ 1" for the illustration and says so. The hidden-weight table is read from the figure (edge colours) and confirmed by the handwritten arithmetic on slide 32.
- **Background (labelled):** the 2ⁿ hidden-units cost and the pointer to the Universal Approximation Theorem.
- XOR is posed on the last content slide ("XOR function?") and solved fully in Lecture 7.
