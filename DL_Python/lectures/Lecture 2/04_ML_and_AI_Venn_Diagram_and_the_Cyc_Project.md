# Topic 4: Machine Learning and AI — The Venn Diagram, and the Cyc Project

Source: Lecture 2, slides 13–14 (Machine Learning and AI; CYC Project). Figure from the *Deep Learning* book; Cyc slide sourced from Wikipedia. Enriched with web research (Cyc's history and size).

---

## 1) Technical Explanation

**Slide 13 — the book's Venn diagram.** Nested sets, outermost first, each with a representative example:

| Set | Example shown |
|---|---|
| **AI** (outermost) | **Knowledge bases** |
| **Machine learning** | **Logistic regression** |
| **Representation learning** | **Shallow autoencoders** |
| **Deep learning** (innermost) | **MLPs** (multilayer perceptrons) |

This refines Lecture 1's three-ring picture ([[07_Traditional_Programming_vs_ML_and_the_AI_Hierarchy]]) by adding a fourth ring, *representation learning*, between ML and DL: some representation-learning methods (shallow autoencoders) are not deep, while deep learning is the representation-learning approach built from many layers. Knowledge bases sit in AI *outside* ML because they are not learned from data.

**Slide 14 — the Cyc project: a knowledge-base AI.** Four logos: Cyc's *Knowledge Base*, *Inference Engines*, *Actionable Output*, *Intelligent Data Selection*. The slide says the project "was begun in July 1984 at MCC".

Web research adds: Cyc was started by **Douglas Lenat** in 1984 at MCC (Microelectronics and Computer Technology Corporation), where he stayed until 1994, after he found it difficult to hand-code domain-specific knowledge for his earlier project EURISKO. Cyc is a knowledge base of **hand-coded "common-sense" facts** plus an **inference engine** that deduces new facts from them, written in the logic-based language **CycL**. It was spun out of MCC in 1994 as **Cycorp**. As of 2012 the full knowledge base held roughly 500,000 concepts and 5 million assertions.

**Why the lecture shows it.** Cyc is the standard example of the *knowledge-base* approach: people type the facts and rules in. That is the opposite of learning, and it illustrates the lesson of [[01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features]] — hand-coding world knowledge is slow, expensive and never finished. (The slide itself only names the project; the "why" is the standard textbook framing of this figure.)

---

## 2) Simple English Explanation

Imagine four circles, one inside another:

- Biggest: **AI** — any way of making computers act smart. Example: a **knowledge base**, a giant list of facts typed in by people.
- Inside it: **machine learning** — AI that learns from data. Example: logistic regression.
- Inside that: **representation learning** — ML that also learns *what to look at*. Example: a small autoencoder.
- Smallest: **deep learning** — representation learning with many layers. Example: a multilayer perceptron.

**Cyc** is the famous example from the biggest circle only. Starting in 1984, a team spent decades typing in everyday common sense ("water is wet", "people die", …) plus rules to reason with it. It shows how slow it is to teach a computer by writing everything by hand — one reason learning from data became so attractive.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Chaar circles socho, ek doosre ke andar:

- Sabse bada: **AI** — computer ko smart banane ka koi bhi tareeka. Example: **knowledge base**, logon ke type kiye hue facts ki badi list.
- Uske andar: **machine learning** — AI jo data se seekhta hai. Example: logistic regression.
- Uske andar: **representation learning** — ML jo ye bhi seekhta hai ki *kya dekhna hai*. Example: chhota autoencoder.
- Sabse chhota: **deep learning** — bahut saari layers wali representation learning. Example: multilayer perceptron.

**Cyc** sirf sabse bade circle ka famous example hai. 1984 se ek team ne kai saal tak rozmarra ka common sense ("paani geela hota hai", "log marte hain", …) aur usse reason karne ke rules haath se type kiye. Ye dikhata hai ki sab kuch haath se likhkar computer ko sikhana kitna dheema hai — data se seekhna isiliye itna attractive laga.
