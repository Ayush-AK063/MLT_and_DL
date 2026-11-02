# Topic 4: Data Quality — The Six Dimensions

Source: Lecture 6, slide 11 (Data Quality).

---

## 1) Technical Explanation

**Definition**: *"Data have quality if they satisfy the requirements of the intended use."* This is a crucial, use-case-relative definition — data quality isn't an absolute, fixed property; it depends on what the data is being used *for*. Data that's "high quality" for one purpose might be inadequate for another.

**Measures for data quality — a multidimensional view**, six dimensions:

1. **Accuracy**: whether the data is *correct or wrong, accurate or not* — i.e., does the recorded value genuinely reflect the true value in the real world?
2. **Completeness**: whether data is *not recorded, unavailable, ...* — this directly maps to the "incomplete" data problem from Topic 2 ([[02_Data_Preprocessing_Overview_and_Need]]).
3. **Consistency**: whether *some [data] modified but some not, dangling, ...* — i.e., are related pieces of data kept in sync with each other, or do inconsistencies/orphaned references ("dangling" data) exist? Maps to the "inconsistent" data problem from Topic 2.
4. **Timeliness**: whether data is *updated in a timely* manner — stale/outdated data can be a quality problem even if it was accurate when originally recorded.
5. **Believability**: *how trustable the data are* — i.e., independent of technical accuracy, how much confidence can a user reasonably place in this data source? (e.g., data from an unreliable or unverified source may be technically well-formatted but still not believable.)
6. **Interpretability**: *how easily the data can be understood* — even accurate, complete, consistent, timely, and believable data is low-quality in practice if users/systems can't make sense of it (e.g., poorly documented codes, cryptic abbreviations, ambiguous units).

**How this connects to the rest of the lecture**: this six-dimensional framework is a more formal, comprehensive lens than the simple "incomplete/noisy/inconsistent" categorization from Topic 2 — it shows that data cleaning (which addresses accuracy, completeness, consistency) is necessary but not *sufficient* for full data quality; timeliness, believability, and interpretability are quality concerns that go beyond what pure "cleaning" techniques (missing value imputation, noise smoothing) can fix.

---

## 2) Simple English Explanation

This section asks a deeper question: what does it even mean for data to be "good quality"?

**The core idea**: data has quality if it's good enough to actually do the job you need it to do. This means quality isn't a fixed, universal thing — data that's perfectly fine for one purpose might not be good enough for a different purpose.

**Six specific things to check to judge data quality:**

1. **Accuracy** — Is the data actually correct? Does it match reality?
2. **Completeness** — Is anything missing? Are there gaps where information should be but isn't?
3. **Consistency** — Do different parts of the data agree with each other, or do they contradict each other?
4. **Timeliness** — Is the data up to date, or is it stale/outdated?
5. **Believability** — Can you actually trust this data? Does it come from a reliable source?
6. **Interpretability** — Can people (or systems) actually understand and make sense of this data, or is it confusing/unclear?

**Why this matters**: even if you fix all the obvious problems (missing values, weird numbers, contradictions), your data might still have quality issues — like being outdated, coming from an unreliable source, or being written in a confusing way that nobody can properly interpret. Good data quality is bigger than just "cleaning" — it's a broader set of considerations.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section ek deeper sawaal poochta hai: **data "achhi quality" ka kab hota hai?**

**Core idea**: Data mein quality tab hoti hai jab wo aapke intended kaam ke liye kaafi achha ho. Matlab quality koi fixed, universal cheez nahi hai — jo data ek kaam ke liye perfect hai, wo doosre kaam ke liye achha na ho sakta hai.

**Data quality judge karne ke liye 6 specific cheezein check karo:**

1. **Accuracy (Sahi hona)** — Kya data actually sahi hai? Kya wo real duniya se match karta hai?
2. **Completeness (Poora hona)** — Kuch missing to nahi hai? Aisi jagah gaps to nahi hai jaha information honi chahiye thi lekin nahi hai?
3. **Consistency (Aapas mein match hona)** — Kya data ke alag-alag hisse aapas mein match karte hai, ya ek doosre se contradict karte hai?
4. **Timeliness (Time pe hona)** — Kya data updated (naya) hai, ya wo purana/stale ho chuka hai?
5. **Believability (Trust karne layak hona)** — Kya aap is data pe bharosa kar sakte ho? Kya ye reliable source se aaya hai?
6. **Interpretability (Samajhne layak hona)** — Kya log (ya systems) is data ko sahi tarike se samajh sakte hai, ya ye confusing/unclear hai?

**Ye kyun important hai?**
Chahe aap sare obvious problems fix kar do (missing values, ajeeb numbers, contradictions), phir bhi data mein quality issues ho sakte hai — jaise data purana hona, unreliable source se aana, ya itni confusing tarike se likha hona ki koi samajh hi na paye. **Achhi data quality sirf "cleaning" se bahut bada concept hai — ye ek broader set of considerations hai.**
