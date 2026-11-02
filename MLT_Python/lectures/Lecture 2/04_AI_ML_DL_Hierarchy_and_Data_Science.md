# Topic 4: AI, ML, DL Hierarchy and Relationship with Data Science

Source: Lecture 2, slides 30–31 ("AI Hierarchy"). Enriched with web research (IBM).

---

## 1) Technical Explanation

The lecture presents the standard **nested-set relationship** among four related-but-distinct fields, shown as concentric ovals/circles:

`Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning`

- **Artificial Intelligence (AI)** — the broadest field: the general pursuit of building programs/machines capable of tasks that would normally require human intelligence (reasoning, perception, decision-making, language, learning). AI includes many approaches beyond learning from data — e.g., rule-based expert systems, search algorithms, logic-based planning — not all of which involve "learning" at all.
- **Machine Learning (ML)** — a *subset* of AI specifically concerned with algorithms that improve their performance on a task by learning patterns from data, rather than being explicitly programmed with fixed rules (as covered in Topic 0 of this lecture). Not all AI is ML — but all ML is AI.
- **Deep Learning (DL)** — a *subset* of ML that uses **multi-layered artificial neural networks** ("deep" = many hidden layers) to automatically learn hierarchical feature representations directly from raw data (pixels, audio waveforms, raw text), reducing the need for manual feature engineering that older ML techniques (e.g., linear regression, decision trees) typically require.

The second diagram in the lecture (slide 31) extends this hierarchy with a fourth, adjacent field:
- **Data Science** — overlaps with AI/ML/DL but is broader in scope. It combines mathematics & statistics, programming skills (Python, R, etc.), and domain expertise to extract meaningful insights from data — via exploratory data analysis and predictive analytics. Data Science *uses* AI/ML/DL as tools, but also includes non-ML activities like data cleaning, visualization, and statistical inference.

**Practical implication for this course**: ES514 sits mainly inside the "Machine Learning" and "Deep Learning" circles — you'll study classical ML algorithms (KNN, decision trees, SVM, etc.) as well as neural-network-based Deep Learning methods (CNNs, RNNs, GANs) later in the syllabus.

---

## 2) Simple English Explanation

Think of these four fields as a set of Russian nesting dolls (matryoshka dolls) — each one fits inside a bigger one.

- The biggest doll is **Artificial Intelligence (AI)** — this is the whole idea of making machines act smart in any way at all (this includes very old techniques too, like simple if-then rule systems that have nothing to do with "learning").
- Inside AI is a smaller doll called **Machine Learning (ML)** — this is specifically about machines that get smart by learning from examples/data, instead of being told exact rules.
- Inside ML is an even smaller doll called **Deep Learning (DL)** — this is a special, more powerful kind of machine learning that uses layered "neural networks" (inspired loosely by the brain) and works especially well with huge amounts of data like images, audio, and text.

There's also a related field, **Data Science**, which overlaps with all three. Data scientists use AI/ML/DL as tools, but they also do a lot of other work — cleaning messy data, making charts, and using statistics — to find useful insights and make predictions from large datasets.

So: AI is the big goal, ML is one major way of achieving it (learning from data), and DL is the most powerful modern branch of ML (using deep neural networks).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye 4 fields ko samajhne ka sabse aasan tarika hai — **matryoshka (Russian) gudiya** jaisa socho, jisme ek chhoti gudiya dusri badi gudiya ke andar fit hoti hai.

**Sabse badi gudiya — Artificial Intelligence (AI):**
Ye sabse bada concept hai — machine ko kisi bhi tarah se "smart" banane ki koshish. Isme purane tarike bhi aate hai jaise simple "agar-to" (if-then) rule-based systems, jinka "seekhne" se koi lena-dena nahi hota.

**Uske andar — Machine Learning (ML):**
Ye AI ka ek hissa (subset) hai, jisme machine **data se seekh kar** smart banti hai — na ki hardcoded rules se. (Ye Topic 0 mein humne detail mein padha hai.)

**Uske bhi andar — Deep Learning (DL):**
Ye ML ka ek aur khaas hissa hai jo **Neural Networks** (layers mein bane hue, dimaag se inspired systems) use karta hai. DL khaaskar bahut zyada data (jaise images, audio, text) ke saath bahut achha kaam karta hai, aur khud hi important patterns (features) dhoondh leta hai — insaan ko manually batana nahi padta.

**Zanjeer (chain) yaad rakho:**
```
AI (sabse bada) > ML (uske andar) > DL (sabse andar)
```
Matlab: **Har DL, ML hai. Har ML, AI hai. Lekin har AI, ML nahi hai.**

**Data Science kya hai?**
Ye ek related field hai jo AI/ML/DL se overlap karti hai. Data Scientists in teeno ka use karte hai, lekin unka kaam usse zyada bada hai — jaise:
- **Maths & Statistics** use karna
- **Programming (Python, R)** karna
- **Domain Knowledge** (us field ki jaankari) use karna
Data Science ka goal hai data se **insights nikalna** (exploratory data analysis) aur **future predict karna** (predictive analytics).

**Is course (ES514) ka connection**: Ye course mostly **ML aur DL** ke andar aata hai — pehle classical ML algorithms (KNN, Decision Tree, SVM) padhenge, fir baad mein Deep Learning (CNN, RNN, GAN jaise neural networks) padhenge.
