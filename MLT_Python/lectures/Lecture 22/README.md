# Lecture 22 — Random Forest, Bagging and Ensemble Learning (ES514: Machine Learning Techniques)

Source PDF: `Lecture_Random_Forest.pdf` (19 slides)

## Notes Index (topic-wise, in lecture order)

| File | Topic |
|---|---|
| [00_Recap_Decision_Tree_Job_Offer_and_Handwritten_Examples.md](00_Recap_Decision_Tree_Job_Offer_and_Handwritten_Examples.md) | Slides 2–3: recap of the job-offer tree (root/decision/leaf labels, Salary–Travel–Complimentary/FIKA) and the instructor's handwritten asides (features, pizza-order flow) |
| [01_What_Is_a_Random_Forest_Breiman_2001.md](01_What_Is_a_Random_Forest_Breiman_2001.md) | Slides 4–6: Breiman 2001, ensemble of trees, majority vote, the 9-tree figure (six 1s, three 0s → 1), strength vs. correlation |
| [02_Wisdom_of_the_Crowd_Choosing_a_Phone_with_Three_Friends.md](02_Wisdom_of_the_Crowd_Choosing_a_Phone_with_Three_Friends.md) | Slides 7–9: "I can't decide" analogy, three friends' trees, majority vote, binomial check (3 trees 78.4%, 11 trees 92.2%) |
| [03_Random_Forest_Overview_Three_Steps_and_Spam_Example.md](03_Random_Forest_Overview_Three_Steps_and_Spam_Example.md) | Slides 10–11: the 3 steps, the spam/ham example with 600 samples, 200 per tree, n = 40/50 trees |
| [04_Random_Sampling_with_Replacement_Bootstrap.md](04_Random_Sampling_with_Replacement_Bootstrap.md) | Slide 12: sampling with replacement on [1…6], probabilities, 63.2% distinct rows, out-of-bag rows |
| [05_Bagging_Bootstrap_Aggregation.md](05_Bagging_Bootstrap_Aggregation.md) | Slides 13–14: tree instability, bagging, Panel A/B figure, variance formula ρσ² + (1−ρ)σ²/B, OOB |
| [06_Feature_Randomness_Random_Subset_of_Features_per_Split.md](06_Feature_Randomness_Random_Subset_of_Features_per_Split.md) | Slide 15: random feature subset, decorrelation, √p rule, per-split vs per-tree flag |
| [07_Bagging_vs_Boosting_Comparison.md](07_Bagging_vs_Boosting_Comparison.md) | Slide 16: the 6-row comparison table, boosting explained, noise-row correction |
| [08_Random_Forest_in_scikit_learn_and_the_Digits_Example.md](08_Random_Forest_in_scikit_learn_and_the_Digits_Example.md) | Slides 17–19: scikit-learn ensembles page, 3-line code, digits task; our experiment (tree 82.0% vs forest 97.8%, OOB 96.6%) |
| [09_Why_Random_Forests_Work_Strengths_Limits_and_Summary.md](09_Why_Random_Forests_Work_Strengths_Limits_and_Summary.md) | Research enrichment: why it works, strengths/limits, comparison with k-NN and single trees, flag list |

Every slide of the 19-slide deck is accounted for (slides 5–6 identical except the source link; slides 7–9 are the same meme figure progressing; slide 19 is the closing forest-photo slide). Three styles per file: Technical, Simple English, Hinglish. Text-only notes — the site adds recreated SVG diagrams separately.

## Notes on this lecture

- **Natural next step after Lectures 20–21.** One greedy tree (ID3) is unstable and overfits; this lecture fixes that with bagging + feature randomness. The recap (slides 2–3) goes back to the job-offer tree of Lecture 20.
- **Lecture 22 is mostly conceptual:** only a few numbers appear (6 vs 3 votes, 600/200 samples, 40–50 trees). No numeric example in the slides needed correction, but I **verified** the ideas numerically:
  - Slide 5 grid: six 1s and three 0s → prediction 1 ✔.
  - Slide 12: 6⁶ = 46,656 equally likely samples; P([1,1,1,1,1,1]) = 2.1×10⁻⁵; expected distinct fraction 66.5% at m = 6 (simulation 66.49%), tending to 63.2%.
  - Majority vote of independent 70%-accurate voters: 1 → 70%, 3 → 78.4%, 11 → 92.2%, 101 → ≈100%.
  - sklearn digits experiment (1,797 × 64, 10 classes; 75/25 split): single tree 82.0% test (100% train); forest 1/10/50/100/200 trees = 81.3 / 94.4 / 98.0 / 97.8 / 97.6%; OOB 96.6%; default `max_features = sqrt`. **These come from our own run — the slides show only code.**
- **Flags / corrections:**
  1. **Slide 16** says bagging is "not affected by noise and outliers" — too strong; it is *more robust than boosting* (Breiman 2001 states "more robust to noise" than AdaBoost) but not immune.
  2. **Slide 15** says each *tree* picks from a random feature subset; in Breiman's algorithm a fresh subset is drawn at **each node split**.
  3. **Slide 11:** each tree gets 200 of 600 samples; a standard bootstrap sample has the *same size* as the data (600); 200 is a sub-sampling variant. Also slide 10's "corrects overfitting" is better read as "reduces variance / overfits less than a single deep tree".
  4. **Slide 5** calls the trees "simpler"; in a standard forest each tree is typically grown deep — the simplicity is per-tree data/features, not tree depth.
  5. Typos on slides: "Randomnsess", "sesitive".
- **Handwriting (hard to read, best-effort):** slide 2 (features, NeurIPS/A\*, LLM hallucination, pizza-order steps, "Safe order / Take risk"), slide 7 (OnePlus, Google Pixel, Apple, Samsung, Nokia struck out), slide 8 (best reading: Friend 1 Apple, Friend 2 Apple, Friend 3 Samsung → "Buy Apple"; the printed green/red dots on slide 9 do not map one-to-one onto these names; some other names near the friends are illegible and not transcribed), slide 11 (600 samples, 200 random samples ×3, "Mail is spam or ham", n = 40 / n = 50, Class-B). Items I could not read reliably are labelled as such inside the topic files.
- **Research enrichment:** Breiman 2001 (strength and correlation, comparison with AdaBoost, robustness to noise — confirmed via web search), bagging/variance formula, OOB estimate, boosting overview, `max_features` defaults and scikit-learn behaviour (the last items are general knowledge, flagged as such in the files).
- **Off-topic content:** none. The meme and forest-photo slides are illustrative only.
