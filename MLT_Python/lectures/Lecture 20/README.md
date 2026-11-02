# Lecture 20 — Decision Trees and the ID3 Algorithm (ES514: Machine Learning Techniques)

Source PDF: `Lecture-Decision-Trees.pdf` (20 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [01_Job_Offer_Example_and_What_Is_a_Decision_Tree.md](01_Job_Offer_Example_and_What_Is_a_Decision_Tree.md) | Job-offer motivating example (slide 2), definition of a decision tree (nodes = choices, edges = rules), history (CART 1984, ID3 1986, C4.5 1993) |
| [02_Tree_Structure_Terminology_and_Where_Trees_Are_Used.md](02_Tree_Structure_Terminology_and_Where_Trees_Are_Used.md) | Slide-4 roadmap (root, decision/leaf nodes, splitting, entropy & gain, pruning), classification vs. regression, spam/tumor/loan uses, training → validation → prediction workflow, pruning explained |
| [03_Worked_Tree_Will_Vaibhav_Suryavanshi_Play_Cricket.md](03_Worked_Tree_Will_Vaibhav_Suryavanshi_Play_Cricket.md) | The 6-slide progressive cricket tree: 5 decision nodes, 6 leaves, depth 4, branch-by-branch reveal table, if–then rules |
| [04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy.md](04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy.md) | "Play Football?" tree + the three handwritten ideas: splitting criteria (entropy/info gain), keep splitting until pure, greedy approach (hill-climbing, local vs. global maximum, dynamic programming) |
| [05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea.md](05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea.md) | What ID3 is (Quinlan, 1986), greedy + top-down + recursive, properties, ID3 vs. CART vs. C4.5 |
| [06_Entropy_Measuring_Disorder_in_a_Dataset.md](06_Entropy_Measuring_Disorder_in_a_Dataset.md) | Entropy formula, range 0–1 (log₂k max), reference-value table, Shannon intuition, H(9,5) = 0.9403, Gini comparison |
| [07_Information_Gain_Choosing_the_Best_Attribute.md](07_Information_Gain_Choosing_the_Best_Attribute.md) | IG formula, weighted conditional entropy, "investigator" idea, properties, bias towards many-valued attributes |
| [08_Steps_of_the_ID3_Algorithm.md](08_Steps_of_the_ID3_Algorithm.md) | The 4 steps, full pseudocode, stopping conditions, plus a verified preview of the complete PlayTennis tree |
| [09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set.md](09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set.md) | The 14-day table, counts 9 Yes / 5 No, Entropy(S) = 0.94 |
| [10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook.md](10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook.md) | Entropy of Sunny [2+,3−], Overcast [4+,0−], Rain [3+,2−]; Gain(S, Outlook) = 0.2464 (exact 0.2467); gains of all four attributes |

Every slide of the 20-slide deck is accounted for (slides 6–11 are one figure revealed progressively; slide 1 is the title slide). Each file explains its topic in **three styles**: Technical, Simple English, and Hinglish. Text-only notes — the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **New algorithm family.** After the lazy, distance-based k-NN (Lecture 16) and the evaluation lectures (17–19), this starts *tree-based* learning. No recap slides, so no `00_` file.
- **The slides stop mid-example.** Information gain is computed only for Outlook (0.2464). The other attributes' gains and the finished tree are *not* in this PDF — expect them in Lecture 21. I computed them independently as a clearly labelled preview ([[08_Steps_of_the_ID3_Algorithm]], [[10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook]]): Outlook 0.2467, Humidity 0.1518, Wind 0.0481, Temp 0.0292.
- **Numeric verification.**
  - Entropy(S) for [9+, 5−] = 0.940286 → slide's 0.94 ✔.
  - Entropy of [2+,3−] and [3+,2−] = 0.970951 → slide's 0.971 ✔; [4+,0−] = 0 ✔.
  - **Rounding flag:** slide's Gain(S, Outlook) = **0.2464** is from rounded intermediates (0.94, 0.971). Exact value = **0.2467** (textbook ≈ 0.247). Immaterial, but worth knowing for exam answers.
- **Correction flagged:** slide 14 says ID3 uses "entropy or Gini impurity". Original ID3 uses **entropy/information gain only**; Gini is the splitting criterion of **CART** (Breiman et al., 1984).
- **Slide quirks (harmless):** slide 15's formula has a stray closing "]"; the symbol list calls the attribute "D" while the formula uses "A".
- **Handwriting (slide 12):** transcribed as ① splitting criteria: entropy / info. gain, ② keep on splitting until all data points belong to same/one class, ③ greedy approach (hill climbing, local max vs. global maximum, "Top", "1st best", → dynamic programming alg.). The name "Bhuvan" beside the hill sketch is not fully legible; likely a person in the climbing analogy — uncertain.
- **Cricket example (slides 6–11):** the instructor's own illustrative tree (not learned from data, no entropy values); it shows tree *shape* before ID3 shows how to *learn* one.
- **Pruning** is named on slide 4 but **not developed** in any slide of this lecture; explained from research in [[02_Tree_Structure_Terminology_and_Where_Trees_Are_Used]].
- **Research enrichment** for: Quinlan's ID3 (1986) / C4.5 (1993) / CART (1984), Shannon entropy and bits, information gain as mutual information, gain-ratio fix for many-valued attributes, greedy vs. global optimality (NP-hardness of optimal trees, Hyafil & Rivest 1976), pre- vs. post-pruning.
- **No off-topic content** found — every slide belongs to decision trees.
