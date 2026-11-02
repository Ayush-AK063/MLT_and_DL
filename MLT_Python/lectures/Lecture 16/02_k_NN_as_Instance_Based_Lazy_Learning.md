# Topic 2: k-NN as an Instance-Based (Memory-Based, "Lazy") Learner

Source: Lecture 16, slides 8–10 (K-Nearest Neighbor — Introduction, Contd. with the Iris-style decision-region figure, classification vs. regression output). Enriched with web research (eager vs. lazy learning, k-NN regression).

---

## 1) Technical Explanation

**Definition (slide 8).** *K-Nearest Neighbor (K-NN) is an **instance-based (memory-based) supervised** algorithm.*

- **Supervised** — it needs a training set of examples with known labels (see [[04_Labeled_vs_Unlabeled_Data]] from Lecture 1).
- **Instance-based learning** — *"a family of learning algorithms that, instead of performing explicit generalization (in the training phase), compare new problem instances with instances seen in training, which have been stored in memory."* It *"constructs hypotheses directly from the training instances themselves."*
- **Lazy** — *"The computation is postponed until a new instance is observed, these algorithms are sometimes referred to as 'lazy.'"*

**Eager vs. lazy (research).** Most models in this course so far are **eager learners**: [[05_Worked_Example_Logistic_Regression_Exam_Pass_Probability]] from Lecture 15 or [[03_Matrix_Approach_Normal_Equation_Worked_Solution]] from Lecture 14 do all the hard work during *training* (compute coefficients/weights), after which prediction is a quick formula and the training data can be discarded. k-NN is the opposite:

| | Eager (regression, logistic regression, neural nets) | Lazy (k-NN) |
|---|---|---|
| Training phase | Expensive: fit parameters | **Almost nothing** — just store the data |
| Prediction phase | Cheap: evaluate formula | **Expensive**: compare against stored data |
| Needs training data at prediction time? | No | **Yes, all of it** |
| Learned model | Parameters (m, c, weights) | The dataset itself |

**Core assumption (slide 9).** *"K-NN is based on the fact that similar objects lie in close proximity to each other in the feature space."* The slide's figure is a scatter plot of the Iris-style data (sepal length vs. sepal width, three clusters) with the plane painted in three colour regions (red / green / blue): *"objects of the same class lie quite close to each other and hence a new test case can be compared with k closest training examples."* The painted regions are the **decision regions** — wherever a new point lands, k-NN would give it that region's colour. Their boundary is jagged and irregular (not a straight line like logistic regression's), because k-NN makes no assumption about the *shape* of the boundary — it is a **non-parametric** method. Compare with the same Iris data in [[03_Iris_Dataset_Case_Study]] from Lecture 1.

**Two uses (slide 10).** The slide states k-NN is used for **both classification and regression**, and the output depends on which:

1. **k-NN classification** — *the output is a class membership. An object is classified by a **plurality vote** of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.*
2. **k-NN regression** — *the output is the property value for the object. This value is the **average** of the values of the k nearest neighbors.*

Note "plurality" ≠ "majority": with 3+ classes the winner only needs the *most* votes, not more than half (e.g. 4 neighbors voting A, A, B, C → A wins with 2 of 4, a plurality but not a majority). Tied pluralities still need a tie-break rule.

**Tiny regression example (illustrative).** If k = 3 and the three nearest houses sold for ₹50 L, ₹60 L, ₹55 L, then k-NN regression predicts (50+60+55)/3 = **₹55 L**.

**Why "no training" is a double-edged sword.** There is no model-fitting step to go wrong, and new data can be added instantly (just append it). But every prediction scans the stored data, so speed and memory grow with dataset size — see [[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]].

---

## 2) Simple English Explanation

Most machine-learning methods **study** first and then **take the exam**: they spend time learning a rule from the data, then throw the data away and just apply the rule. k-NN is different — it never really "studies." It just **keeps all the examples in a notebook**. When a question comes, it flips through the notebook, finds the most similar past examples, and copies their answer. That's why it's called:

- **Instance-based / memory-based** — it works directly from remembered examples ("instances").
- **Lazy** — it does no work until someone actually asks a question.

It is also **supervised**, because every example in the notebook must already come with its correct answer.

The idea behind it: **things that are similar sit close together.** On a graph of flowers, all roses cluster in one corner, all tulips in another. A new flower landing near the roses is most likely a rose. The coloured picture on the slide shows exactly this — the graph is painted with the colour of whichever group a new point would be placed into.

k-NN can answer two kinds of questions:
- **"Which category?"** (classification) — the neighbors **vote**. Most votes wins.
- **"What number?"** (regression) — take the **average** of the neighbors' numbers. If the 3 nearest houses cost 50, 60 and 55 lakh, guess 55 lakh.

The price you pay for being lazy: every question makes it look through the whole notebook, so it gets slow when the notebook is huge.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Zyada tar ML methods pehle **padhai** karte hain (data se ek rule/formula seekhte hain) aur phir exam mein sirf wo rule laga dete hain, data ko fenk dete hain. **k-NN aisa nahi karta.** Ye bas saare examples ek **copy mein likh kar rakh leta hai**. Jab koi naya sawaal aata hai tab copy kholta hai, sabse milte-julte purane examples dhoondhta hai aur unka answer copy kar deta hai. Isiliye isse kehte hain:

- **Instance-based / memory-based** — ye seedha yaad rakhe hue examples (instances) se kaam karta hai.
- **Lazy (aalsi)** — jab tak koi naya point na aaye, ye koi computation nahi karta; sab kaam baad mein (prediction ke time) hota hai.

Ye **supervised** bhi hai, kyunki har stored example ke saath uska sahi answer (label) hona zaroori hai.

Basic soch: **similar cheezein feature space mein ek-dusre ke paas hoti hain.** Slide 9 ke graph mein teen colour ke region hain — ek naya point jis region mein girega, k-NN use usi colour (class) ka bata dega. Iska boundary tedha-medha hota hai, seedhi line nahi, kyunki k-NN koi fixed shape assume nahi karta (isse **non-parametric** kehte hain).

k-NN do kaam kar sakta hai:
- **Classification (kaunsi category?)** — neighbors **vote** karte hain, jiske zyada vote wo jeeta.
- **Regression (kitni value?)** — neighbors ki values ka **average** lete hain. Maan lo 3 sabse paas ke ghar 50, 60, 55 lakh mein bike, to prediction = (50+60+55)/3 = **55 lakh**.

Slide mein "plurality vote" likha hai — matlab jiske **sabse zyada** vote ho (zaroori nahi 50% se zyada ho). Jaise 4 neighbors mein A, A, B, C aaye to A jeetega (2 vote), bhale majority nahi hai.

Kimat kya hai? Lazy hone ki wajah se har prediction pe poora data scan karna padta hai, isliye data bahut bada ho to k-NN **slow** ho jata hai.
