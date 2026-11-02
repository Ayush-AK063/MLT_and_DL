# Topic 2: Precision and Recall — The Document-Retrieval Venn Diagram

Source: Lecture 18, slide 4 ("Precision and Recall": Venn diagram over the "Space of all documents", recall and precision formulas in words). Enriched with web research (Cranfield experiments, medical vs. retrieval vocabulary).

---

## 1) Technical Explanation

**The picture.** A rectangle = the **space of all documents**. Inside it two overlapping circles:
- the **Relevant** circle (documents that truly match the user's need),
- the **Retrieved** circle (documents the system returned),
- their **overlap** = **Relevant + Retrieved**,
- everything outside both circles = **Not Relevant + Not Retrieved**.

**Formulas (slide).**

- **recall = (Number of relevant documents retrieved) / (Total number of relevant documents)**
- **precision = (Number of relevant documents retrieved) / (Total number of documents retrieved)**

**Mapping to the confusion matrix** ([[00_Recap_Confusion_Matrix_and_the_Sick_People_Intuition]]):

| Venn region | Confusion-matrix term |
|---|---|
| Relevant + Retrieved (overlap) | **TP** |
| Retrieved but not relevant | **FP** |
| Relevant but not retrieved | **FN** |
| Not relevant + not retrieved (outside both circles) | **TN** |

Hence: relevant retrieved = TP; total retrieved = TP + FP; total relevant = TP + FN. So the slide's two formulas are exactly **precision = TP/(TP + FP)** and **recall = TP/(TP + FN)** from [[01_Classification_Metrics_Accuracy_Precision_Recall_F1]] — same idea, search-engine vocabulary. This also links to this course's opening question in Lecture 17 slide 2: *"how far down the list will a user need to look to find some/all relevant documents?"* ([[01_Why_System_Evaluation_and_Predictive_Modeling]] from Lecture 17).

**Worked example (illustrative).** A library holds 1,000 documents; 20 are relevant to a query. The system retrieves 40 documents, of which 15 are relevant.
- TP = 15, FP = 40 − 15 = 25, FN = 20 − 15 = 5, TN = 1000 − 15 − 25 − 5 = 955.
- Precision = 15/40 = **0.375**; Recall = 15/20 = **0.75**.
- Note TN = 955 is *huge* but neither formula uses it — in retrieval the vast ocean of irrelevant, unretrieved documents carries little information, which is why precision/recall (and not accuracy: (15 + 955)/1000 = 97 %) are used.

**Origin (research).** Recall and precision came out of the **Cranfield experiments** (1958–1966) led by Cyril Cleverdon at the College of Aeronautics, Cranfield, England — the first systematic evaluation of retrieval systems using a test collection of queries and known relevant documents. Later, C. J. van Rijsbergen (1979) derived the F-measure as a weighted harmonic mean of the two.

**Same ideas, medical names (research).** *Recall* = **sensitivity** = true-positive rate; *precision* = **positive predictive value (PPV)**. Medicine also tracks **specificity** (true negatives), which retrieval ignores — see [[03_Worked_Exercise_Man_vs_Woman_Photo_Classification]] and [[04_Summaries_of_the_Confusion_Matrix_Full_Table_of_Rates]].

---

## 2) Simple English Explanation

Imagine a giant pile of **all documents** in a library. You search for "dog training."
- Some documents truly match your need — the **Relevant** circle.
- Your search engine hands you a bunch — the **Retrieved** circle.
- Where the two circles overlap are the **good results you actually received**.
- Everything outside both circles was both irrelevant and (rightly) not shown.

Two questions to judge the search engine:
- **Precision:** "Of the pages it gave me, how many were actually useful?" → (useful pages given) ÷ (all pages given).
- **Recall:** "Of all the useful pages that exist, how many did it manage to give me?" → (useful pages given) ÷ (all useful pages that exist).

Example: 20 useful documents exist; the engine shows 40 pages, 15 of them useful. Precision = 15 ÷ 40 = 0.375 (lots of junk); recall = 15 ÷ 20 = 0.75 (found three-quarters of the good ones).

This is the same as the confusion matrix: "useful and shown" = TP, "junk shown" = FP, "useful but hidden" = FN.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho ek library hai jisme **saare documents** ka dher hai. Tum "dog training" search karte ho.
- Kuch documents sach mein tumhare kaam ke hain — **Relevant** circle.
- Search engine ne tumhe kuch documents diye — **Retrieved** circle.
- Jahan dono circles overlap karte hain, wo **kaam ke results jo tumhe mile** (Relevant + Retrieved) = **TP**.
- Dono circles ke bahar sab kuch: na kaam ka tha, na dikhaya gaya = **TN**.

Search engine ko judge karne ke do sawaal:
- **Precision:** "Jo pages mujhe diye gaye, unme se kitne kaam ke the?" = (kaam ke diye gaye pages) ÷ (kul diye gaye pages).
- **Recall:** "Jitne kaam ke pages exist karte hain, unme se kitne mujhe mile?" = (kaam ke diye gaye pages) ÷ (kul kaam ke pages).

Example: 20 kaam ke documents hain; engine ne 40 pages dikhaye jisme 15 kaam ke. TP = 15, FP = 25, FN = 5. Precision = 15 ÷ 40 = **0.375** (kachra zyada), Recall = 15 ÷ 20 = **0.75** (3/4 achhe pages mil gaye).

Ye wahi confusion matrix hai: "kaam ka aur dikhaya" = TP, "kachra dikhaya" = FP, "kaam ka par nahi dikhaya" = FN. Dhyaan do: yahan TN = 955 bahut bada hai par formula mein use hi nahi hota — isiliye retrieval mein accuracy (97%) bekaar hai aur precision/recall use hote hain.

History: ye idea 1958–66 ke **Cranfield experiments** (Cyril Cleverdon) se aaya. Medical mein recall ko **sensitivity** aur precision ko **PPV** kehte hain.
