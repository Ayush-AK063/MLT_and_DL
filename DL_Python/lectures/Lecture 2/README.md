# Lecture 2 — Representation Learning (ES532: Introduction to Deep Learning)

Source PDF: `Lecture-2 Representation Learning.pdf` — 46 slides, read in full (text plus every figure slide).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_Issue_and_Choice_of_Representation.md](00_Recap_Issue_and_Choice_of_Representation.md) | Recap of Lecture 1's last two slides (representation matters; Cartesian vs polar) |
| [01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features.md](01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features.md) | Pattern recognition vs end-to-end learning; why hand-designed features fail ("identify a car") |
| [02_Representation_Learning_and_Factors_of_Variation.md](02_Representation_Learning_and_Factors_of_Variation.md) | Why learned representations win; separating factors of variation |
| [03_Deep_Learning_Representations_from_Simpler_Representations_and_Computational_Graphs.md](03_Deep_Learning_Representations_from_Simpler_Representations_and_Computational_Graphs.md) | Layered features (pixels→edges→parts→object); computational graphs and depth |
| [04_ML_and_AI_Venn_Diagram_and_the_Cyc_Project.md](04_ML_and_AI_Venn_Diagram_and_the_Cyc_Project.md) | The AI / ML / representation learning / DL Venn diagram; the Cyc knowledge base |
| [05_Simple_to_Complex_Features_and_Conventional_ML_vs_Deep_Learning.md](05_Simple_to_Complex_Features_and_Conventional_ML_vs_Deep_Learning.md) | Low→high-level features; conventional-ML pipeline; the 4-row rule-based→DL flowchart |
| [06_Content_Organization_and_History_of_Deep_Learning.md](06_Content_Organization_and_History_of_Deep_Learning.md) | The book's chapter map; cybernetics → connectionism → deep learning |
| [07_Historical_Trends_Growing_Datasets_Connections_and_Neurons.md](07_Historical_Trends_Growing_Datasets_Connections_and_Neurons.md) | Growing datasets, MNIST, connections per neuron, neuron counts |
| [08_Solving_Object_Recognition_AlexNet_and_When_Not_to_Use_Deep_Learning.md](08_Solving_Object_Recognition_AlexNet_and_When_Not_to_Use_Deep_Learning.md) | AlexNet's 2012 ImageNet win; when not to use DL |
| [09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications.md](09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications.md) | The perceptron: pass/fail example, weights, bias, linear boundary, applications |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Opens with a repeat of Lecture 1's last two slides** (slides 2–3); written up once in Lecture 1 ([[08_Issue_and_Choice_of_Representation]]) and linked from `00_`.
- **Most figures come from the *Deep Learning* book** (Goodfellow, Bengio, Courville), credited on the slides. Values read off charts (datasets, connections, neurons, ILSVRC error) are approximate and flagged as such in the notes.
- **Web research added:** Cyc's history and size (topic 04), AlexNet's 15.3% vs 26.2% top-5 error (topic 08), and the 2006 deep-belief-network turning point (topic 06).
- **Slide 24** (Growing Datasets) has no figure in the PDF — it is the build-up before slide 25's chart.
- **Slide 30's handwritten-style notes** about when not to use neural nets are terse and one bullet is ambiguous; interpretation is flagged in topic 08.
- **Perceptron slides (31–45) are reused in Lecture 3.** They are written up here in full; Lecture 3's recap links back rather than repeating them.
- **Only worked numbers:** the pass/fail arithmetic in topic 09 is an invented illustration (the slides give no numbers) and was checked by hand (0.24 → Pass, −0.06 → Fail).
- Slide 29/30 chart and several figure slides carry the counter numbers of the longer master deck (37–82).
