# Lecture 7 — XOR Implementation Example (ES532: Introduction to Deep Learning)

Source PDF: `Lecture 07 XOR Implementation Example.pdf` — 25 slides, read in full (figures and tables, read visually).

## Notes Index (topic-wise)

| File | Topic |
|---|---|
| [01_XOR_with_a_Hidden_Layer_The_Table_and_the_Four_Inequalities.md](01_XOR_with_a_Hidden_Layer_The_Table_and_the_Four_Inequalities.md) | XOR on the 4-hidden-unit network; w₁ < w₀, w₂ ≥ w₀, w₃ ≥ w₀, w₄ < w₀ |
| [02_The_Remaining_15_Boolean_Functions_and_the_Three_Input_Case.md](02_The_Remaining_15_Boolean_Functions_and_the_Three_Input_Case.md) | All 16 two-input functions; 3 inputs → 8 hidden units, bias −3 |
| [03_Theorem_Any_Boolean_Function_with_2_to_the_n_Hidden_Perceptrons.md](03_Theorem_Any_Boolean_Function_with_2_to_the_n_Hidden_Perceptrons.md) | The 2ⁿ-hidden-unit theorem, informal proof, and the exponential catch |
| [04_Why_Boolean_Functions_Matter_Movie_Example_and_MLP_Terminology.md](04_Why_Boolean_Functions_Matter_Movie_Example_and_MLP_Terminology.md) | Link to the movie-liking problem; the name "MLP" and single-hidden-layer representation power |

Each file explains the topic in **three styles**: Technical, Simple English, and Hinglish.

## Notes on this lecture

- **Slide 1 is an admin announcement:** *Quiz 1 is scheduled for Tuesday, 25/08/2026, at 10:00 AM.* No academic content; recorded here only.
- **Continues Lecture 6** directly (same network, same ±1 convention; slide counter 197 follows 196) — no separate recap file, links back instead.
- **Verified:** the XOR inequalities with a concrete solution (w = (0,1,1,0), w₀ = 1); for n = 2 and n = 3, exactly one hidden unit fires per input and **all 16 / all 256** Boolean functions are realised by the construction.
- **Flag — "more than 3 inputs" / "more than n inputs":** the titles of slides 12 and 14 say "more than", but the content treats exactly 3 and n inputs. Read as wording slips.
- **Flag — scope of the movie argument:** the theorem is for Boolean inputs, and fitting past data ≠ generalising; both cautions are added (labelled as not on the slide).
- **Typos on slides 21–22** ("prrof", "givne", "or past") noted, harmless.
- **Background (labelled):** exponential growth table (2ⁿ), depth vs width remark.
