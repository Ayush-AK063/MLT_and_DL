# Topic 2: History of the Perceptron and the Biological-Neuron Analogy

Source: Lecture 3, slides 18–19 (History of basic model; Perceptron — biological neuron vs Rosenblatt's 1957 perceptron). Enriched with web research (Rosenblatt, Mark I Perceptron, Minsky & Papert 1969).

---

## 1) Technical Explanation

**Slide 18 — "History of basic model".**

- *The first learning machine: the Perceptron — built at Cornell, 1960.*
- The perceptron was a **linear classifier on top of a simple feature extractor**.
- "Most of the practical applications of ML today use glorified linear classifiers or glorified template matching." (This remark is well known from Yann LeCun's talks; the slide does not attribute it.)
- **Significant effort is required for identifying relevant features** — the hand-design problem of [[01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features]] in Lecture 2.
- It typically solves **y = sign( Σᵢ₌₁ᴺ (wᵢ · fᵢ(X) + b) )**, where fᵢ(X) are hand-made features of the input X. The small diagram shows inputs x₁, x₂ and a bias unit b (value 1) with weights, a Σ node, a step function and a 0/1 output.

**Slide 19 — the analogy.** *A perceptron is a neural network unit (an artificial neuron) that does certain computations to detect features or business intelligence in the input data.* Fig. 1 shows a **biological neuron** (dendrites receive input signals, the cell nucleus, the axon with its myelin sheath carries the output to axon terminals); Fig. 2 shows **Rosenblatt's original 1957 perceptron** (a figure credited to Minsky & Papert's *Perceptrons*, 1969, with Frank Rosenblatt, 1928–1971, pictured) and the **simplified model** with inputs weighted w₁, w₂, w₃ feeding a single unit. The mapping: dendrites ↔ inputs, synaptic strength ↔ weights, cell body ↔ sum + threshold, axon ↔ output.

**Web-research context.**

- Rosenblatt, at the **Cornell Aeronautical Laboratory**, simulated the perceptron on an IBM 704 in **1957**; it was publicly demonstrated on **7 July 1958**, and the **Mark I Perceptron** machine was built as a pattern classifier. The press (New York Times, 1958) hailed an "electronic brain that teaches itself". (The slide dates the machine to 1960; sources vary by which milestone — design, demo or hardware — is counted. Both dates are given so neither is lost.)
- In **1969** Minsky and Papert's *Perceptrons* analysed what single-layer perceptrons cannot compute — notably XOR — which chilled funding for neural-network research for years. This limit is the subject of [[08_Linear_Non_Separability_XOR_and_Hyperplanes]] here and of Lecture 7 (XOR implementation with a network).

**Caution.** The biological analogy is loose: a real neuron is far more complex than a weighted sum and threshold.

---

## 2) Simple English Explanation

The perceptron is the oldest "learning machine". Frank Rosenblatt designed it in 1957 at Cornell, and a physical machine was shown to the public soon after (the slide says 1960). It works as a **straight-line decision-maker sitting on top of hand-chosen clues**. Its formula in words: "multiply each clue by its weight, add them with a bias, and take the sign (positive or negative)".

The pictures compare it to a **brain cell**: a real neuron collects signals through its branches (dendrites), decides in its body, and sends an output down its long tail (axon). A perceptron copies this in a very simplified way: inputs, weights, a sum and a yes/no output.

Weakness: someone still has to choose good clues by hand, and one perceptron can only draw a straight line — Minsky and Papert showed in 1969 that it cannot solve some simple problems like XOR.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Perceptron sabse purani "learning machine" hai. Frank Rosenblatt ne ise 1957 mein Cornell mein design kiya, aur uske kuch samay baad ek physical machine logon ko dikhayi gayi (slide 1960 kehti hai). Ye **haath se chune gaye clues ke upar baitha ek seedhi-line decision-maker** hai. Iska formula shabdon mein: "har clue ko uske weight se multiply karo, bias ke saath jodo, aur sign (positive ya negative) lo".

Pictures ise **dimaag ke cell** se compare karti hain: asli neuron apni shakhaon (dendrites) se signals ikatthe karta hai, apne body mein decide karta hai, aur lambi poonchh (axon) se output bhejta hai. Perceptron isko bahut simple tareeke se copy karta hai: inputs, weights, ek sum aur haan/naa output.

Kamzori: abhi bhi kisi ko haath se achhe clues chunne padte hain, aur ek perceptron sirf seedhi line kheench sakta hai — Minsky aur Papert ne 1969 mein dikhaya ki wo XOR jaisi kuch simple problems solve nahi kar sakta.
