# Lecture 8 — Sigmoid Neuron (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 8 Sigmoid Neuron.pdf` — Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Read in full (all 25 slides).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [00_Recap_From_Boolean_to_Arbitrary_Functions.md](00_Recap_From_Boolean_to_Arbitrary_Functions.md) | Recap: moving from Boolean functions to arbitrary real-valued functions, the oil-mining motivating example |
| [01_Why_Perceptron_Thresholding_Is_Too_Harsh.md](01_Why_Perceptron_Thresholding_Is_Too_Harsh.md) | The movie-critics-rating example showing the perceptron's harsh, discontinuous step-function decision |
| [02_The_Sigmoid_Logistic_Function.md](02_The_Sigmoid_Logistic_Function.md) | Introducing the sigmoid/logistic function, its formula, and its probability interpretation |
| [03_Perceptron_vs_Sigmoid_Neuron_and_Differentiability.md](03_Perceptron_vs_Sigmoid_Neuron_and_Differentiability.md) | Side-by-side comparison, and why differentiability is what makes gradient-based training possible |
| [04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU.md](04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU.md) | The wider activation-function family — Tanh, ReLU, Leaky ReLU, ELU, Softplus — equations, derivatives, ranges |
| [05_Advantages_and_Disadvantages_of_Activation_Functions.md](05_Advantages_and_Disadvantages_of_Activation_Functions.md) | Trade-offs of each activation function — vanishing gradients, dying ReLU, zero-centering |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish — so it's usable whether you want precise terminology or a beginner-friendly walkthrough with zero prior Python/DL knowledge.

## Notes on this lecture

- **Course confirmed**: this PDF revealed the course details that were placeholders in `CLAUDE.md`/the site — **ES532: Introduction to Deep Learning**, ABV-IIITM Gwalior, instructor **Dr. Yashwant Singh Patel** (same instructor and institute as the sibling `MLT_Python` project's ES514 course). `CLAUDE.md` and `site/index.html` have been updated accordingly; `site/netlify/functions/chat.js` was **left untouched** per the user's explicit instruction not to update the (currently disabled) chatbot right now.
- **Out-of-order lecture**: this is Lecture **8** in the actual course, added first because it's what the user had on hand — Lectures 1–7 don't exist in this repo yet and will be added later, under their own numbers, when supplied.
- **`00_` recap file convention applied**: slides 2–5 open with a "Till Now" recap (moving from Boolean functions to arbitrary real-valued functions) referencing earlier course content this repo doesn't have yet (perceptrons, logic gates, Boolean functions) — rather than reconstructing that missing material from scratch, the recap file summarizes only what these specific slides actually say and re-derive, and does not invent citations to files that don't exist yet. Once Lectures 1–7 are added, this recap file is a natural candidate to gain proper `[[cross-reference]]` links back to them.
- **Worked example verified**: the movie-critics-rating example (0.49 → dislike, 0.51 → like, threshold 0.5) was double-checked against the slide's own stated threshold and both given rating values — the arithmetic is trivial (just a greater-than/less-than comparison) but the point it illustrates (a razor-thin input difference producing a maximally different output) was confirmed to be exactly what the slide claims.
- **A genuine flag on the source material**: the activation-function comparison table (slides 23–24, credited by the slide to an external site) has a few "Range" column entries that don't check out mathematically once independently recomputed — Softplus's actual range is $(0,\infty)$, not the $(0,1)$ printed on the slide (which looks like it was copy-pasted from the Sigmoid row just above it), and Leaky ReLU's actual range is $(-\infty,\infty)$, not $(-1,1)$. This is called out explicitly inside [[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]] rather than silently reproduced, per the usual "flag, don't silently absorb" rule.
- **Web research added**: the historical origin of the vanishing gradient problem (Hochreiter, 1991) and of ReLU (Nair & Hinton, 2010), both cited inside [[05_Advantages_and_Disadvantages_of_Activation_Functions]] to explain *why* these specific activation functions matter beyond what the slide's own bullet points say.
