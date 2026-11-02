# Topic 0: Recap Note: Traditional Programming vs ML/DL and the AI Hierarchy (Slides 1–4)

Source: Lecture 26, slides 1–4 (title slide "Deep Learning / Representation Learning"; "Traditional Programming vs ML/DL" ×2; "AI Hierarchy"). Slides 2–4 repeat Lecture 2, slides 19–20 and 30, almost word for word, so this file is a short recap that links back instead of re-explaining from scratch.

---

## 1) Technical Explanation

### Slide 1: the title

The deck is titled **"Deep Learning — Representation Learning"**. Every content slide carries the footer **"ES532: Deep Learning"** and page numbers 34–55. This tells us the slides were taken from a larger Deep Learning deck (its slides 1–33 are not included). The user confirmed that this lecture belongs to the MLT course as Lecture 26. It is the bridge from classical ML (Lectures 1–25) to deep learning.

The single idea the whole lecture builds towards is in the subtitle: **deep learning is a way of doing representation learning**. The computer learns not only the mapping from features to the answer, but also the features themselves.

### Slides 2–3: Traditional programming vs machine learning

Already covered in full in [[00_Traditional_Programming_vs_Machine_Learning]] from Lecture 2. In short:

| Paradigm | Inputs to the computer | What comes out |
|---|---|---|
| Traditional programming | Data + Program (hand-written rules) | Output |
| Machine learning | Data + Output (labelled examples) | Program (the learned model f(x) ≈ y) |

Slide 2 shows only the first row. Slide 3 adds the second row as an animation step.

### Slide 4: AI hierarchy

Already covered in [[04_AI_ML_DL_Hierarchy_and_Data_Science]] from Lecture 2:

**Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning**

### Why the recap is here

This lecture refines both pictures:

- The ML row in slides 2–3 still assumes a human decides **which features** the computer sees. Slides 7–11 show that this choice is the hard part, and slide 23 splits "Program" into hand-designed vs learned pieces ([[09_Deep_Learning_Model_and_the_Four_AI_Flowcharts]]).
- The three-circle hierarchy of slide 4 gets a fourth circle, **representation learning**, between ML and DL on slide 16 ([[07_Machine_Learning_and_AI_Venn_Diagram_and_the_Cyc_Project]]).

---

## 2) Simple English Explanation

The first slide just names the topic: **Deep Learning, also called Representation Learning**. The small print on each slide says "ES532: Deep Learning", which means these slides were borrowed from a Deep Learning course deck. In our MLT course this is Lecture 26, the first step from ordinary machine learning into deep learning.

Slides 2 to 4 are pictures you have already seen in Lecture 2:

- **Normal programming:** you give the computer the data and the rules, and it gives you the answer. For example, you tell it "tax = 10% of price" and give it a price.
- **Machine learning:** you give the computer the data and the correct answers, and it works out the rule by itself.
- **The family tree:** AI is the big circle. Machine learning sits inside AI. Deep learning sits inside machine learning.

Full explanations are in Lecture 2 ([[00_Traditional_Programming_vs_Machine_Learning]] and [[04_AI_ML_DL_Hierarchy_and_Data_Science]]).

Why repeat them? Because this lecture adds something new to both pictures. In normal machine learning a human still has to decide *what to measure* about the data (the "features"). Deep learning lets the computer decide that too. And the family tree gets a new circle in the middle called **representation learning**.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Pehli slide sirf topic ka naam batati hai: **Deep Learning, yaani Representation Learning**. Har slide ke neeche chhota sa "ES532: Deep Learning" likha hai, aur page numbers 34 se 55 tak hain. Matlab ye slides kisi bade Deep Learning deck se li gayi hain (pehle 33 slides isme nahi hain). Hamare MLT course me ye Lecture 26 hai, jahan se hum normal machine learning se deep learning ki taraf jaa rahe hain.

Slides 2 se 4 wahi diagrams hain jo Lecture 2 me aa chuke hain:

- **Traditional programming:** Computer ko data + rules (program) do, wo output deta hai. Jaise "tax = price ka 10%" rule likh diya, price diya, answer mil gaya.
- **Machine learning:** Computer ko data + sahi answers (output) do, wo khud rule (program/model) dhoondh leta hai.
- **AI hierarchy:** AI sabse bada circle hai, uske andar Machine Learning, aur uske andar Deep Learning.

Poori detail Lecture 2 me hai: [[00_Traditional_Programming_vs_Machine_Learning]] aur [[04_AI_ML_DL_Hierarchy_and_Data_Science]].

Ye recap yahan kyun hai? Kyunki ye lecture dono diagrams ko aage badhata hai:

- Normal ML me bhi ek insaan ko decide karna padta hai ki data ke **kaun se features** (kya-kya measure karna hai) computer ko dene hain. Ye kaam hi sabse mushkil hota hai (slides 7–11). Deep learning me computer features bhi khud seekh leta hai (slide 23).
- AI ⊃ ML ⊃ DL wale diagram me ek naya circle judta hai, **representation learning**, jo ML aur DL ke beech me aata hai (slide 16).
