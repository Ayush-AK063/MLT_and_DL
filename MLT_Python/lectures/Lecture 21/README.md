# Lecture 21 — Decision Trees: Completing the ID3 Worked Example (ES514: Machine Learning Techniques)

Source PDF: `Lecture-Decision-Trees-Example.pdf` (15 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_ID3_Steps_Dataset_Entropy_and_Outlook_Gain.md](00_Recap_ID3_Steps_Dataset_Entropy_and_Outlook_Gain.md) | Slides 1–5: recap of the 4 ID3 steps, the 14-day table, Entropy(S) = 0.94 and Gain(S, Outlook) = 0.2464 — links back to Lecture 20 |
| [01_Gain_of_Temp_Hot_Mild_Cool.md](01_Gain_of_Temp_Hot_Mild_Cool.md) | Slide 6: Hot [2+,2−] = 1.0, Cool [3+,1−] = 0.8113, Mild [4+,2−] = 0.918 → Gain = 0.029 |
| [02_Gain_of_Humidity_High_Normal.md](02_Gain_of_Humidity_High_Normal.md) | Slide 7: High [3+,4−] = 0.9852, Normal [6+,1−] = 0.5916 → Gain = 0.152 |
| [03_Gain_of_Wind_and_Choosing_Outlook_as_Root.md](03_Gain_of_Wind_and_Choosing_Outlook_as_Root.md) | Slides 8–9: Wind gain 0.048 (working computed by us), scoreboard of all four gains, Outlook chosen as root |
| [04_Splitting_on_Outlook_First_Level_of_the_Tree.md](04_Splitting_on_Outlook_First_Level_of_the_Tree.md) | Slide 10: first-level tree, day-sets under Sunny/Overcast/Rain, Overcast pure → leaf |
| [05_Sunny_Subset_Gains_and_Humidity_Split.md](05_Sunny_Subset_Gains_and_Humidity_Split.md) | Slides 11–14: gains inside Sunny (Temp 0.570, Humidity 0.97, Wind 0.0192) → split on Humidity (High → No, Normal → Yes) |
| [06_Rain_Subset_and_the_Final_Decision_Tree.md](06_Rain_Subset_and_the_Final_Decision_Tree.md) | Slide 15: the finished tree; Rain-subset gains computed by us (Wind 0.971), rules, prediction example, 14/14 check |
| [07_Properties_Inductive_Bias_and_Practical_Notes_on_ID3.md](07_Properties_Inductive_Bias_and_Practical_Notes_on_ID3.md) | Research enrichment: ID3's inductive bias, overfitting, limitations, CART vs ID3 in scikit-learn |

Every slide of the 15-slide deck is accounted for (slides 12 and 14 are identical; slides 13 and 15 show tree stages). Three styles per file: Technical, Simple English, Hinglish. Text-only notes — the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **Direct continuation of Lecture 20.** Slides 1–5 repeat Lecture 20's steps/table/Outlook calculation (recap file `00_`); everything after is new. The tree preview I gave in Lecture 20 (topic 08) is **confirmed** by this lecture's slide 15.
- **Final tree:** Outlook (root) → Sunny: Humidity (High → No, Normal → Yes); Overcast → Yes; Rain: Wind (Strong → No, Weak → Yes). 3 decision nodes, 5 leaves, Temp unused; classifies all 14 training days correctly (verified).
- **Numbers verified — slide vs exact** (all differences are rounding of intermediate entropies; no ranking or tree changes):

  | Quantity | Slide | Exact |
  |---|---|---|
  | Gain(S, Outlook) | 0.2464 | 0.2467 |
  | Gain(S, Temp) | 0.029 / 0.0289 | 0.0292 |
  | Gain(S, Humidity) | 0.152 / 0.1516 | 0.1518 |
  | Gain(S, Wind) | 0.048 | 0.0481 |
  | Gain(S_sunny, Temp) | 0.570 | 0.571 |
  | Gain(S_sunny, Humidity) | 0.97 | 0.971 |
  | Gain(S_sunny, Wind) | 0.0192 | 0.0200 |
  | Entropy(S_normal humidity) | 0.5916 | 0.5917 |

  The slide also gives Temp's gain two ways (0.029 on slide 6, 0.0289 on slide 9) and Humidity's two ways (0.152 vs 0.1516).
- **Gaps in the slides (filled by us, labelled in the files):** slide 8 (Wind) shows only the table, no working; the **Rain subset has no working at all** (slide 14 re-shows the Sunny gains, slide 15 jumps to the final tree). Rain gains: Wind 0.971, Temp 0.020, Humidity 0.020.
- **Handwriting:** slide 11 — Entropy(S_hot) first written 0.97 then corrected to 0.0; Entropy(S_cool) corrected from 1.0 to 0.0.
- **Slide-15 caveat:** the bottom of the printed tree is slightly cropped (the "No" label under Strong is half-cut); the leaves read Strong → No {D6, D14}, Weak → Yes {D4, D5, D10}.
- **Research enrichment** (file 07): ID3's preference for short trees / Occam's razor, overfitting and pruning, gain-ratio fix, categorical-only limitation, ID3 vs. CART in scikit-learn (the scikit-learn points are from general knowledge, not verified in this session).
- **No off-topic content** found. Expect Lecture 22 to move on to a new topic (possibly Gini index/CART, continuous attributes or pruning — unconfirmed).
