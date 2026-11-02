# Topic 2: Features, Target, and Labels

Source: Lecture 1 — Iris Dataset slides (slides 10–12)

---

## 1) Technical Explanation

In a supervised machine learning dataset, each **sample / instance / observation** (a single row of data, e.g., one flower) is described by two categories of variables:

- **Features (x)**: the independent/input variables — measurable properties (attributes, dimensions) that describe the object. In the Iris dataset: `Sepal.Length`, `Sepal.Width`, `Petal.Length`, `Petal.Width`.
- **Target (y)**: the dependent/output variable — the value the model is trying to predict. In the Iris dataset: `Species` (Setosa, Versicolor, Virginica).

When the target column is filled in (observed), the corresponding value is called a **label**. Formally:
- **Labeled data**: samples where the target `y` is known/observed.
- **Unlabeled data**: samples where the target `y` is unknown (marked `?`).

The dataset is structured as a matrix: rows = samples, columns = features (+ one target/label column). The core assumption of supervised ML is that there exists **some relationship f such that y ≈ f(x)** — i.e., features determine (or strongly correlate with) the target — and the learning algorithm's job is to approximate this function `f` from the labeled data, so it can later predict `y` for new, unlabeled `x`.

Analogous terms used interchangeably across ML literature: target = label = response variable = dependent variable = ground truth. Features = attributes = predictors = independent variables = input variables.

---

## 2) Simple English Explanation

Imagine a spreadsheet (table) about flowers. Each row is one flower. Each column is a piece of information about that flower.

- The columns that describe the flower's measurements (like the length of its petal) are called **features** — these are the "clues" the computer looks at.
- The column that tells you what species the flower actually is (Setosa, Versicolor, or Virginica) is called the **target** — this is the "answer" the computer is trying to guess.
- When we already know the answer for a row (we know the species), we call that a **label**. So "label" and "target value" mean basically the same thing — the label is just the specific value written in the target column for that row.
- Sometimes we don't know the answer yet (maybe nobody identified the species of that particular flower) — those rows are called **unlabeled data**, marked with a "?" in the target column.

**Simple analogy**: If you're guessing someone's job based on their clothes, height, and the tools they carry — those are the *features*. Their actual job (doctor, chef, engineer) is the *target/label* you're trying to predict.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho ek Excel sheet hai jisme 150 flowers (phoolon) ki information hai. Har row ek flower hai. Har column ek jaankari hai us flower ke baare mein.

**Features kya hote hai?**
Features matlab wo **measurements/properties jo hum flower ko dekh kar naap sakte hai** — jaise:
- Sepal Length (bahar wali patti ki lambai)
- Sepal Width (bahar wali patti ki chaudai)
- Petal Length (andar wali petal ki lambai)
- Petal Width (andar wali petal ki chaudai)

Ye sab "clues" hai jinse computer guess karega ki flower kaunsi type ka hai.

**Target kya hota hai?**
Target matlab wo **cheez jo humein predict/guess karni hai** — is dataset mein target hai "Species" (yaani flower kaunsi kism ka hai: Setosa, Versicolor, ya Virginica). Isko humesha `y` letter se represent karte hai, aur features ko `x` se.

**Label kya hota hai?**
Jab kisi row ka target/answer humein pehle se pata hai (kisi expert ne bata diya "ye Setosa hai"), to us value ko **label** kehte hai. Matlab **label = target ka actual pata hua answer**.

**Labeled vs Unlabeled data (chhota preview)**:
- **Labeled data**: jinme species pehle se pata hai (jaise "Setosa", "Versicolor")
- **Unlabeled data**: jinme species pata nahi hai, table mein "?" laga hota hai

**Yaad rakhne ka easy tarika**:
- Features = Sawaal ke clues (jo hum dekh sakte hai)
- Target/Label = Sahi jawaab (jo hume predict karna hai)

Jaise agar aap kisi insaan ko dekh kar uska profession guess kar rahe ho — uske kapde, uske paas ka saaman, uski height — ye sab **features** hai. Uska actual profession (doctor/engineer/chef) jo aap guess kar rahe ho, wo hai **target/label**.
