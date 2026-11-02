# Topic 4: Labeled vs Unlabeled Data (and Supervised vs Unsupervised Learning)

Source: Lecture 1, slide 12 ("Observation Labels"). Enriched with web research (GeeksforGeeks, Toloka).

---

## 1) Technical Explanation

Datasets are categorized based on whether the target/label is observed:

- **Labeled data**: each sample's target value `y` is known and recorded (e.g., a flower row where `Species = Setosa` is filled in). Producing labeled data typically requires manual annotation effort (human experts assigning the correct category/value), which makes it costlier and scarcer than unlabeled data.
- **Unlabeled data**: the target value is missing/unknown (denoted `?` in the lecture's example table). Unlabeled data is abundant and cheap to collect (e.g., raw sensor readings, unannotated images) since it requires no manual annotation.

This distinction directly maps to the two dominant paradigms of machine learning:

| Paradigm | Data used | Goal |
|---|---|---|
| **Supervised Learning** | Labeled data (x, y pairs) | Learn a mapping f(x) → y to predict labels for new, unseen data. Includes **classification** (discrete target, e.g., species) and **regression** (continuous target, e.g., price). |
| **Unsupervised Learning** | Unlabeled data (only x) | Discover hidden structure without predefined answers — e.g., **clustering** (grouping similar points), **dimensionality reduction** (e.g., PCA, mentioned later in the course syllabus), **anomaly detection**. |

In the Iris example: rows with a known species (Setosa/Versicolor/Virginica) are the labeled training set; rows marked "?" simulate new flowers whose species we don't yet know — the supervised model trained on labeled data is used to predict labels for these unlabeled rows.

There's also a middle ground, **semi-supervised learning**, which uses a small amount of labeled data together with a large amount of unlabeled data — useful because labeling is expensive but raw data is plentiful. This isn't explicitly named in the slide but follows directly from the labeled/unlabeled distinction shown.

---

## 2) Simple English Explanation

Think of a table where one column shows the "correct answer" for each row.

- **Labeled data** = rows where we already know and have written down the correct answer. Example: a photo of a flower where someone already wrote "this is a Setosa" next to it.
- **Unlabeled data** = rows where we don't know the answer yet — it's blank or marked with a question mark. Example: a new flower photo nobody has identified yet.

Why does this matter? Because it decides *how* a machine learning model can be trained:
- If you have labeled data (question + correct answer pairs), you can train the model like a student with an answer key — this is called **supervised learning**.
- If you only have unlabeled data (no answer key at all), the model has to find patterns on its own, like grouping similar things together without being told what the groups mean — this is called **unsupervised learning**.

Getting labeled data usually takes more effort (someone — a person — has to look at each example and label it correctly), while unlabeled data is often lying around for free (raw photos, sensor logs, text, etc.).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho ek table hai jisme har row ek flower hai, aur last column mein uska "sahi jawaab" (species) likha hai.

**Labeled Data kya hai?**
Jin rows mein "sahi jawaab" pehle se pata hai aur likha hua hai — unhe **labeled data** kehte hai. Jaise: "Ye flower Setosa hai" — ye already kisi ne check karke bata diya.

**Unlabeled Data kya hai?**
Jin rows mein jawaab pata nahi hai — matlab "?" laga hai — unhe **unlabeled data** kehte hai. Jaise: ek naya flower mila hai lekin abhi tak kisi ne uski species confirm nahi ki.

**Ye kyun important hai?**
Kyunki iske hisaab se decide hota hai ki ML model kis tarah train karenge:

1. **Supervised Learning** (Labeled data use karte hai):
   - Jaise ek student ko answer-key ke saath practice questions diye jaayein — student sawaal aur sahi jawaab dono dekhta hai, aur pattern seekhta hai.
   - Example: Iris dataset mein flowers jinki species pehle se pata hai, unse model seekhta hai.
   - Isme 2 type hote hai: **Classification** (category guess karna, jaise "kaunsi species") aur **Regression** (number predict karna, jaise "price kitna hoga")

2. **Unsupervised Learning** (Unlabeled data use karte hai):
   - Jaise ek student ko sirf sawaal diye jaayein, answer-key na ho — student khud similar cheezon ko group karne ki koshish karta hai.
   - Example: Bina species bataye, sirf measurements dekh kar flowers ko groups mein baantna (jaise similar flowers ek saath rakhna) — isko **clustering** kehte hai.

**Labeled data banana mehnga kyun hai?**
Kisi insaan ko baith kar har example dekh kar sahi answer likhna padta hai — isliye labeled data **kam hota hai aur mehnga hota hai**. Lekin unlabeled data (raw photos, sensor data) **bahut zyada aur free mein milta hai** kyunki usme label lagane ki mehnat nahi lagi.

**Yaad rakhne ka tarika**: 
- Labeled = "Answer-key ke saath" → Supervised Learning
- Unlabeled = "Answer-key ke bina" → Unsupervised Learning
