# Topic 6: The Bootstrap and Out-of-Bag Validation

Source: Lecture 17, slide 16 ("The bootstrap", with the instructor's "{Out of bag validation}" note, the iteration sketches and the figure comparing hold-out, K-fold and bootstrap resampling). Enriched with web research (the 63.2 % / 36.8 % result, the .632 bootstrap estimator).

---

## 1) Technical Explanation

**Cross-validation vs. bootstrap (slide 16).**
- **CV uses sampling *without replacement*:** an instance, once selected, **cannot be selected again** for a particular training/test set.
- **The bootstrap uses sampling *with replacement* to form the training set:**
  1. **Sample a dataset of n instances n times, with replacement,** to form a new dataset of **n** instances.
  2. Use this data as the **training set**.
  3. Use the instances from the original dataset that **don't occur** in the new training set for **testing**.

The instructor adds **"{Out of bag validation}"** — those left-out test instances are called the **out-of-bag (OOB)** sample. His board sketch (Ist Iteration, I₂, I₃ …) shows repeating this over several iterations with different resamples.

**The slide's figure** (bottom right) contrasts three schemes: **Hold-out validation** (Data → Training + Validation), **K-fold cross validation** (Data cut into 1, 2, 3, …, K; one is the validation set each round) and **Bootstrap resampling** (a Data bar with a few coloured instances picked, and a "Resampled dataset" bar where those same coloured instances appear **more than once**).

**Mini-example (illustrative).** Original data = {a, b, c, d, e}. Draw 5 times with replacement, e.g. **b, d, b, e, a** → training set {b, b, d, e, a} (b twice); out-of-bag test set = {c} (never drawn).

**How many instances end up out-of-bag? (verified calculation + research).** In one draw, an instance is *not* picked with probability (1 − 1/n). Over n independent draws it is never picked with probability

(1 − 1/n)ⁿ → **e⁻¹ ≈ 0.368** as n grows.

Verified numerically: n = 5 → 0.328; n = 10 → 0.349; n = 100 → 0.366; n = 1000 → 0.3677. So a bootstrap training set contains on average only **≈ 63.2 % distinct** original instances (1 − 0.368), and ≈ **36.8 %** of the data is out-of-bag and usable for testing.

**Because training uses only ≈ 63 % unique data**, the OOB error is a bit *pessimistic*; the **.632 bootstrap** estimator (Efron) corrects by blending: Error ≈ 0.632 × (OOB error) + 0.368 × (training/resubstitution error). Repeating the bootstrap (b = 100s of times) and averaging gives a stable estimate. Bootstrap is especially useful for **very small datasets** and underlies **bagging / random forests**, where each tree's OOB samples give a free validation score.

| | k-fold CV | Bootstrap |
|---|---|---|
| Sampling | without replacement | **with replacement** |
| Training set size | (k−1)/k of data | n draws → ≈ 63.2 % unique |
| Test instances | each instance tested once | out-of-bag ≈ 36.8 % per round |
| Typical use | standard accuracy/model-selection | very small data, ensembles |

See also [[05_k_Fold_Cross_Validation]].

---

## 2) Simple English Explanation

Another way to get "study pile" and "exam pile" from a small dataset is the **bootstrap**.

**Idea:** imagine your data are names written on slips in a bag. To make a study pile of the same size as your data, **pull a slip, write its name down, and put it back** — then repeat until you've pulled as many times as there are slips. Because you put each slip back, the same name can show up **several times**, and some names never show up.

- The **study pile** = everything you pulled (with repeats).
- The **exam pile** = the names that **never got pulled** (called **out of bag**).

Example: names {a, b, c, d, e}; pulls give b, d, b, e, a → study with {b, b, d, e, a}; exam on {c}.

**Fun fact:** with a large dataset, about **63 %** of the different names get picked at least once and about **37 %** are left out — that's the exam pile. (The math: the chance a name is never picked is about 1/e ≈ 0.368.)

Cross-validation never repeats an example in a pile; the bootstrap does — that's the key difference.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Chhote data se "study pile" aur "exam pile" banane ka ek aur tareeka hai — **bootstrap**.

**Idea:** socho tumhare data ke naam parchiyon par likhe hain aur ek thaile mein hain. Training set banane ke liye: **ek parchi nikalo, naam likho, aur parchi wapas thaile mein daal do** — ye utni baar karo jitni parchiyan hain (n baar). Kyunki parchi wapas daal rahe ho, ek hi naam **kai baar** aa sakta hai aur kuch naam kabhi nahi aate.

- **Training set** = jo bhi nikla (repeats ke saath).
- **Test set** = jo naam **kabhi nahi nikle** — isse **out-of-bag (OOB)** kehte hain (sir ne "Out of bag validation" likha hai).

Example: data {a, b, c, d, e}; nikle b, d, b, e, a → training {b, b, d, e, a}; test {c}.

**Interesting fact:** bade data mein lagbhag **63%** alag-alag examples kam se kam ek baar chun jate hain aur lagbhag **37%** bach jate hain (wahi test set). Math: kisi naam ke kabhi na chunne ki probability (1 − 1/n)ⁿ ≈ 1/e ≈ 0.368 hoti hai (hamne n = 5, 10, 100, 1000 par check kiya: 0.328, 0.349, 0.366, 0.368).

**Cross-validation vs bootstrap:** CV mein koi example ek pile mein repeat nahi hota (**without replacement**); bootstrap mein hota hai (**with replacement**) — yahi asli farak hai.
