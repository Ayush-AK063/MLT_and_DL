# Lecture 0 — An Overview of Gradient Descent Optimization Algorithms

Source PDF: `Overview of GD Optimization Algorithms.pdf` — this is Sebastian Ruder's widely-cited paper "An overview of gradient descent optimization algorithms" (arXiv:1609.04747; originally a blog post, 19 Jan 2016; this version updated 15 Jun 2017), read here in full (all 14 pages, including references).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [01_What_Is_Gradient_Descent_and_the_Learning_Rate.md](01_What_Is_Gradient_Descent_and_the_Learning_Rate.md) | What gradient descent is, the update rule, and why the learning rate is so critical |
| [02_Batch_Stochastic_and_MiniBatch_Gradient_Descent.md](02_Batch_Stochastic_and_MiniBatch_Gradient_Descent.md) | The three GD variants — batch, stochastic (SGD), and mini-batch |
| [03_Challenges_in_Gradient_Descent_Optimization.md](03_Challenges_in_Gradient_Descent_Optimization.md) | Learning-rate tuning, fixed schedules, per-parameter rates, and saddle points |
| [04_Momentum.md](04_Momentum.md) | Momentum — the "heavy ball" fix for ravines, from Polyak (1964) |
| [05_Nesterov_Accelerated_Gradient.md](05_Nesterov_Accelerated_Gradient.md) | NAG — giving momentum a "look-ahead" |
| [06_Adagrad.md](06_Adagrad.md) | Adagrad — per-parameter adaptive learning rates for sparse data |
| [07_Adadelta.md](07_Adadelta.md) | Adadelta — fixing Adagrad's ever-shrinking learning rate |
| [08_RMSprop.md](08_RMSprop.md) | RMSprop — Hinton's unpublished-but-ubiquitous fix for the same problem |
| [09_Adam.md](09_Adam.md) | Adam — combining RMSprop-style scaling with momentum, plus bias correction |
| [10_AdaMax_and_Nadam.md](10_AdaMax_and_Nadam.md) | AdaMax (the ℓ∞ variant of Adam) and Nadam (Adam + NAG) |
| [11_Visualizing_Optimizers_and_Which_One_to_Use.md](11_Visualizing_Optimizers_and_Which_One_to_Use.md) | How the algorithms actually behave on tricky surfaces, and the paper's own recommendation |
| [12_Parallelizing_and_Distributing_SGD.md](12_Parallelizing_and_Distributing_SGD.md) | Hogwild!, Downpour SGD, TensorFlow, EASGD, and other ways to run SGD across many machines |
| [13_Additional_Strategies_Shuffling_BatchNorm_EarlyStopping_GradientNoise.md](13_Additional_Strategies_Shuffling_BatchNorm_EarlyStopping_GradientNoise.md) | Shuffling/curriculum learning, batch normalization, early stopping, gradient noise |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- This is a **standalone reference paper** (originally filed as "Lecture 1" on 2026-09-20; renamed **Lecture 0** on 2026-10-05 once the real course Lecture 1 "Introduction to Deep Learning" arrived), so it has no recap file (`00_`) and no slide deck behind it.
- The source is a **research paper**, not a slide deck — so instead of "slide numbers," topic files cite the paper's own section numbers (e.g. "Section 4.1"). The paper's own numbered equations are reproduced in full in every topic's Technical section.
- **No worked numeric examples** appear in the source paper — it's a pure derivation-and-intuition overview, not a worked-problem lecture — so there was nothing to numerically re-verify here (unlike some MLT_Python lectures, which had worked examples to check by hand).
- **Web research added throughout**, per the usual workflow: the historical origin of Momentum (Polyak, 1964) and Nesterov's method (1983), Adam's real-world successor AdamW and *why* it was needed, and the ongoing research debate about *why* batch normalization actually works (the paper's own "internal covariate shift" explanation has since been seriously challenged by later research). Each of these is called out explicitly inside the relevant topic file so it's clear what came from the paper itself versus what was added.
- **Images**: the source paper has several genuine figures (SGD's noisy loss curve, the momentum ravine contours, the Nesterov look-ahead vectors, and the Beale-function/saddle-point optimizer-path comparisons). Per the usual convention, the `.md` notes stay text-only, but all of these have been recreated as hand-drawn, theme-aware inline SVGs in `site/diagrams.js` and will render automatically on the site under the matching topic (02, 04, 05, and 11).
- Course code/instructor for this Deep Learning course are still placeholders in `CLAUDE.md`/the site — update those once a lecture PDF confirms them (this first PDF was a standalone reference paper, not a slide deck with course branding on it).
