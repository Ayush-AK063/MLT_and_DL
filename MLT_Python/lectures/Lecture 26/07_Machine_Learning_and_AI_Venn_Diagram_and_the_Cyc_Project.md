# Topic 7: Machine Learning and AI: The Venn Diagram, and the Cyc Project

Source: Lecture 26, slides 16–17 ("Machine Learning and AI": nested Venn diagram AI ⊃ Machine learning ⊃ Representation learning ⊃ Deep learning with examples Knowledge bases, Logistic regression, Shallow autoencoders, MLPs, from the *Deep Learning* book, Fig. 1.4; "CYC Project: The project was begun in July 1984 at MCC", with Cyc's four logos from Wikipedia). Enriched with web research (Wikipedia: Cyc, Douglas Lenat; MIT Technology Review, "Cycorp: The Cost of Common Sense", 2005; Goodfellow et al., *Deep Learning*, 2016, ch. 1).

---

## 1) Technical Explanation

### Slide 16: four nested circles, each with an example

Lecture 2's hierarchy had three circles ([[04_AI_ML_DL_Hierarchy_and_Data_Science]] from Lecture 2). The book's version adds **representation learning** between ML and DL:

**AI ⊃ Machine learning ⊃ Representation learning ⊃ Deep learning**

Each region has an example that belongs to that circle but **not** to the next one inside it:

| Region | Example on the slide | Why it sits there |
|---|---|---|
| AI but not ML | **Knowledge bases** | Intelligent behaviour from facts and rules written by humans. Nothing is learned from data. (Cyc, below.) |
| ML but not representation learning | **Logistic regression** | Learns weights from data ([[05_Worked_Example_Logistic_Regression_Exam_Pass_Probability]] from Lecture 15), but uses the features it is given. It does not learn new features. |
| Representation learning but not deep | **Shallow autoencoders** | Learn a new representation (the hidden code h) from data, but with only one hidden layer, so there is no hierarchy of simple → complex ([[04_Representation_Learning_and_Factors_of_Variation]]). |
| Deep learning | **MLPs** (multilayer perceptrons) | Several hidden layers, each a new representation built from the previous one ([[09_Deep_Learning_Model_and_the_Four_AI_Flowcharts]]). |

How to read it: "every deep-learning model is a representation-learning model; every representation-learning model is an ML model; every ML model is an AI technique", but not the other way round.

**Other examples (ours) for each ring:**
- AI, not ML: chess search programs like Deep Blue, route-finding with A* search, rule-based expert systems.
- ML, not representation learning: KNN, decision trees, random forests, linear/logistic regression, linear SVM on fixed features (Lectures 13–25).
- Representation learning, not deep: PCA ([[04_PCA_Introduction_and_Intuition]] from Lecture 11–12), shallow autoencoders, k-means used as a feature encoder (one-hot cluster membership).
- Deep learning: deep MLPs, CNNs, RNNs, Transformers.

*(The slide's graphic is a re-styled version of the book's figure; the circles and examples are the same.)*

### Slide 17: the Cyc project, the classic "knowledge base" approach

**Facts (verified):**

- **Started July 1984** at **MCC**, the Microelectronics and Computer Technology Corporation in Austin, Texas. MCC was a US industry research consortium (about 400 people) formed partly in response to Japan's Fifth Generation Computer project. Cyc was its flagship project.
- **Led by Douglas Lenat** (1950–2023). He started it after finding it frustrating to hand-code domain knowledge for his earlier AI program, EURISKO.
- **Goal:** capture human **common sense**, the millions of everyday facts that people take for granted ("water is wet", "a person can't be in two places at once"), so that a computer could reason like a human. The name comes from "en**cyc**lopedia".
- **How it works:** humans write facts and rules in a formal logic language called **CycL**. An **inference engine** then deduces new facts by logical reasoning.
- **Later history:** spun off from MCC as the company **Cycorp** (1994–95; sources differ on the exact year). A subset was released free as **OpenCyc** in 2002. Lenat died on 31 August 2023.

**The four logos** on the slide (clockwise from top-left, per Wikipedia's caption): Cyc's **Knowledge Base** (KB), its **Inference Engines** (INF), **Actionable Output** (the starburst), and **Intelligent Data Selection** (the SKSI network logo).

### Why Cyc appears in a deep-learning lecture

The *Deep Learning* book uses Cyc as the main example of the **knowledge-base approach** to AI: hard-code knowledge about the world in a formal language, then reason with logical inference rules. Its verdict: none of these projects led to a major success. People struggle to write formal rules with enough complexity to describe the world accurately.

The book's famous anecdote (citing Linde, 1992): Cyc failed to understand a story about a man named **Fred shaving in the morning**. Its inference engine found an inconsistency. It knew that people do not have electrical parts, but because Fred was holding an electric razor, it concluded that the entity "FredWhileShaving" contained electrical parts. It therefore asked whether Fred was still a person while he was shaving.

The lesson: hand-written rules break in endless unexpected ways, just like the hand-designed wheel detector of [[03_Learning_Representations_and_Why_Hand_Designed_Features_Are_Hard]]. The difficulties of hard-coded knowledge suggest that AI systems need the ability to **acquire their own knowledge by extracting patterns from raw data**. That capability is machine learning, and learning the representation too is the step deep learning takes.

| | Knowledge base (Cyc) | Machine learning / deep learning |
|---|---|---|
| Where knowledge comes from | Humans write rules | Learned from data |
| Strength | Explainable, exact logical reasoning | Handles messy, perceptual, ambiguous data |
| Weakness | Brittle; impossible to write every rule | Needs lots of data; harder to explain |

---

## 2) Simple English Explanation

**Slide 16: four circles inside each other.** In Lecture 2 we saw three: AI, then machine learning inside it, then deep learning inside that. This slide adds a new circle, **representation learning**, between machine learning and deep learning. Each ring has an example that belongs to that ring but not to the smaller ring inside it:

1. **AI only: knowledge bases.** Humans type in facts and rules, and the computer reasons with them. Nothing is learned from data. Example: a huge database of common-sense facts (Cyc, below).
2. **Machine learning, but not representation learning: logistic regression** (Lecture 15). It learns its weights from examples, but it uses exactly the features we hand it. It never invents new features.
3. **Representation learning, but not deep: shallow autoencoders.** These do invent a new, compact description of the data (Topic 4), but in only one step. There is no ladder from simple to complex.
4. **Deep learning: MLPs (multilayer perceptrons).** Many layers, each building a new description on top of the previous one.

So every deep learning model is also representation learning, also machine learning and also AI, but not the other way round. Other examples: a chess-search program is AI but not ML; KNN and decision trees are ML but don't learn features; PCA is representation learning but not deep; image-recognition networks are deep learning.

**Slide 17: the Cyc project.**
- Started in **July 1984** at **MCC** (Microelectronics and Computer Technology Corporation), a big American research group in Austin, Texas. It was led by **Douglas Lenat**.
- The dream: type all of human **common sense** into a computer, millions of facts like "water makes things wet" or "people can't be in two places at once", and let it reason like a human. The name comes from "en*cyc*lopedia".
- Facts are written in a special logic language (CycL), and a reasoning program (the "inference engine") draws conclusions from them.
- It later became a company, **Cycorp**, released a free part called **OpenCyc** in 2002, and Lenat died in 2023.
- The four logos show its parts: the knowledge base, the inference engine, actionable output, and intelligent data selection.

**Why mention Cyc here?** It is the best-known example of the "just write all the rules by hand" approach, and of why that approach struggles. The *Deep Learning* book tells a famous story: Cyc read a story about **Fred shaving in the morning** with an electric razor. Cyc knew "people don't have electrical parts". But Fred was holding something electrical, so Cyc decided "Fred-while-shaving" contained electrical parts, and asked whether Fred was still a person while shaving!

The lesson: no matter how many rules you write, real life finds a case you didn't think of. This is the same problem as the hand-made wheel detector in Topic 3. The answer is to let computers **learn from data** instead, and deep learning goes one step further by learning the features too.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 16: Chaar circles ek ke andar ek.** Lecture 2 me teen the: AI ⊃ ML ⊃ DL. Is slide (Deep Learning book, Fig 1.4) me ML aur DL ke beech ek naya circle hai: **representation learning**.

**AI ⊃ Machine learning ⊃ Representation learning ⊃ Deep learning**

Har ring ka ek example, jo us ring me hai par andar wali chhoti ring me nahi:

1. **Sirf AI (ML nahi): Knowledge bases.** Insaan facts aur rules likhta hai, computer unse reasoning karta hai. Data se kuch seekha nahi jaata. (Jaise Cyc, neeche.)
2. **ML, par representation learning nahi: Logistic regression** (Lecture 15). Weights data se seekhta hai, par jo features diye wahi use karta hai. Naye features nahi banata.
3. **Representation learning, par deep nahi: Shallow autoencoders.** Data ka naya compact representation khud banata hai (Topic 4), par sirf ek hidden layer me. Simple → complex wali seedhi nahi hai.
4. **Deep learning: MLPs** (multilayer perceptrons). Kai hidden layers, har layer pichhli ke upar naya representation.

Matlab har deep learning model representation learning bhi hai, ML bhi, AI bhi. Ulta zaroori nahi. Aur examples: chess search program = AI par ML nahi; KNN, decision tree = ML par features nahi seekhte; PCA = representation learning par deep nahi; CNN = deep learning.

**Slide 17: CYC Project.**
- **July 1984** me **MCC** (Microelectronics and Computer Technology Corporation, Austin, Texas) me shuru hua. MCC lagbhag 400 logon ka American research consortium tha, aur Cyc uska flagship project tha. Leader the **Douglas Lenat** (1950–2023), jinhone apne pichhle program EURISKO me haath se knowledge likhne ki takleef dekh ke ye shuru kiya.
- **Sapna:** insaan ka saara **common sense** (crore facts jaise "paani geela karta hai", "insaan ek time pe do jagah nahi ho sakta") computer me daal do, taaki wo insaan jaisa reasoning kare. Naam "en**cyc**lopedia" se aaya.
- Facts ek logic language **CycL** me likhe jaate hain, aur **inference engine** unse naye conclusions nikaalta hai.
- Baad me company **Cycorp** bani (1994–95), 2002 me free part **OpenCyc** release hua.
- Slide ke chaar logos (clockwise): **Knowledge Base**, **Inference Engines**, **Actionable Output**, **Intelligent Data Selection**.

**Deep learning lecture me Cyc kyun?** Ye "saare rules haath se likh do" wale approach ka sabse famous example hai, aur ye bhi ki wo approach kyun fail hota hai. Deep Learning book ki famous kahani: Cyc ko ek story di gayi jisme **Fred subah shave** kar raha hai, electric razor se. Cyc jaanta tha "insaan me electrical parts nahi hote". Par Fred ke haath me electric razor tha, to Cyc ne socha "FredWhileShaving" me electrical parts hain, aur poochha: **kya shave karte waqt Fred abhi bhi insaan hai?**

**Seekh:** kitne bhi rules likh lo, real life koi aisa case le aayegi jo socha nahi tha. Ye wahi problem hai jo Topic 3 me haath se bane wheel detector ki thi. Isliye book kehti hai ki AI ko **data se khud knowledge nikaalni** chahiye: yahi machine learning hai. Deep learning ek kadam aage jaa ke features bhi khud seekhta hai.

| | Knowledge base (Cyc) | ML / Deep learning |
|---|---|---|
| Knowledge kahan se | Insaan rules likhta hai | Data se seekha |
| Fayda | Explain kar sakte hain, exact logic | Messy data (photo, awaaz) handle karta hai |
| Nuksaan | Brittle, har rule likhna impossible | Bahut data chahiye, explain karna mushkil |
