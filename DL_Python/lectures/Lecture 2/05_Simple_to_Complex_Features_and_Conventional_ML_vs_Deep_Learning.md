# Topic 5: Simple to Complex Features, Conventional ML vs Deep Learning, and the Representation-Learning Flowcharts

Source: Lecture 2, slides 15–20 (Simple to Complex Features; Conventional Machine Learning; Deep Learning Model; Representation learning ×3 build-ups). Figures: LeCun & Ranzato (ICML 2013 tutorial), LeCun–Bengio–Hinton, and the *Deep Learning* book.

---

## 1) Technical Explanation

**Slide 15 — Simple to complex features.** A pipeline *car image → Low-Level Feature → Mid-Level Feature → High-Level Feature → Trainable Classifier*, with grids of learned filters below each stage: low-level = oriented edge/colour detectors, mid-level = parts and textures (curves, circles, corners), high-level = object-like patterns. The features get more abstract and complex with depth.

**Slide 16 — Conventional machine learning pipeline.** *Low-level sensing → Pre-processing → Feature extraction → Feature selection → Inference (prediction, recognition)*. Beneath it: *Input (a motorbike photo) → Feature representation (e.g. SIFT, HoG) → Learning algorithm*. SIFT and HoG are classic **hand-designed** feature extractors; only the last box is learned.

**Slide 17 — Deep learning model.**

- A **feed-forward deep network, or multilayer perceptron** (MLP).
- A **mathematical function that maps input to output**.
- **Composed of simpler functions**.
- **Each layer provides a new representation**.
- Training means **learning the right representation**.

**Slides 18–20 — the four-row flowchart, built up one row at a time.** Boxes shaded blue are *learned*; unshaded ones are hand-built:

| System | Pipeline |
|---|---|
| **Rule-based system** | Input → *hand-designed program* → Output |
| **Classic machine learning** | Input → *hand-designed features* → **mapping from features** → Output |
| **Representation learning** | Input → **features** → **mapping from features** → Output |
| **Deep learning** | Input → **features** → **abstract features** → **mapping from features** → Output |

Moving down the table, more and more of the pipeline is learned; deep learning learns even the abstract features, hence "end-to-end" ([[01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features]]).

**Consistency check.** The slide's phrase "feed-forward deep network or multilayer perceptron" matches Lecture 9's feedforward networks ([[01_Feedforward_Network_Architecture_Layers_and_Notation]]) and the hierarchy of [[03_Deep_Learning_Representations_from_Simpler_Representations_and_Computational_Graphs]].

---

## 2) Simple English Explanation

Think of an assembly line that turns a photo into an answer.

- **Old machine learning:** people build the early stations by hand (using tools with names like SIFT and HoG that measure edges and shapes); only the last station — the decision-maker — learns.
- **Deep learning:** *every* station learns. The first stations spot tiny things (edges and colours), the middle ones combine them into parts (a wheel, a window), and the last ones recognise the whole thing (a car).

The four-row chart shows the progression: a rule-based program is fully hand-written; classic ML learns only the final mapping; representation learning also learns the features; deep learning learns features, then more abstract features, then the mapping.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek assembly line socho jo photo ko answer mein badalti hai.

- **Purani machine learning:** shuruaati stations insaan haath se banata hai (SIFT aur HoG jaise tools se jo edges aur shapes naapte hain); sirf aakhri station — decision lene wala — seekhta hai.
- **Deep learning:** *har* station seekhta hai. Pehle stations chhoti cheezein pakadte hain (edges aur colours), beech wale unhe jodkar parts banate hain (pahiya, window), aur aakhri stations poori cheez pehchante hain (car).

Chaar-row ka chart progression dikhata hai: rule-based program poora haath se likha hota hai; classic ML sirf aakhri mapping seekhta hai; representation learning features bhi seekhta hai; deep learning pehle features, phir aur abstract features, phir mapping seekhta hai.
