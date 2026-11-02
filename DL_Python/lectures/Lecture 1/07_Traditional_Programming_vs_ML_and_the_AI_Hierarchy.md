# Topic 7: Traditional Programming vs ML/DL, and the AI Hierarchy

Source: Lecture 1, slides 33–35 (Traditional Programming vs ML/DL ×2; AI Hierarchy).

---

## 1) Technical Explanation

**Traditional programming (slide 33).** A computer takes **Data** and a **Program** (hand-written rules) and produces an **Output**:

Data + Program → Computer → Output

**Machine learning (slide 34).** The roles are reversed. The computer takes **Data** and the desired **Output** and produces the **Program**:

Data + Output → Computer → Program

The "program" that comes out is the *trained model* (for neural networks: the learned weights). It is then used like a normal program on new data. This is why ML suits Category-B problems ([[02_Problem_Space_Easy_for_Humans_vs_Easy_for_Computers]]): when we cannot write the rules, we instead supply examples of inputs and correct outputs and let the machine infer the rules. The same slide appears in the sister ML course — see `00_Traditional_Programming_vs_Machine_Learning` in MLT_Python's Lecture 2 for a fuller treatment.

**AI hierarchy (slide 35).** Three nested ellipses:

Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning

Deep learning is a *subset of* machine learning, which is a *subset of* AI. (Not all AI is ML — e.g. hand-coded rule systems such as the Cyc project of [[04_ML_and_AI_Venn_Diagram_and_the_Cyc_Project]] in Lecture 2 are AI without learning.)

---

## 2) Simple English Explanation

- **Old way of programming:** you write the recipe (the program), give it ingredients (data), and get a dish (output).
- **Machine learning:** you hand over the ingredients *and a picture of the finished dish* many times, and the computer works out the **recipe** for you.

And a family tree: **AI** is the big idea of smart machines. **Machine learning** is the part of AI where machines learn from data. **Deep learning** is the part of machine learning that uses many-layered neural networks.

---

## 3) Hinglish Explanation (Beginner-Friendly)

- **Purana programming:** aap recipe (program) likhte ho, ingredients (data) dete ho, aur dish (output) milti hai.
- **Machine learning:** aap ingredients *aur taiyaar dish ki photo* kai baar de dete ho, aur computer khud **recipe** nikaal leta hai.

Aur ek family tree: **AI** smart machines ka bada idea hai. **Machine learning** AI ka wo hissa hai jahan machines data se seekhti hain. **Deep learning** machine learning ka wo hissa hai jo bahut saari layers wale neural networks use karta hai.
