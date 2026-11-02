# Topic 6: Decision Tree Classification and Induction

Source: Lecture 9, slides 14–16 (Decision Tree Classification, Decision Tree Induction, Decision Tree). The `buys_computer` example is the classic illustration from Han & Kamber's *Data Mining: Concepts and Techniques* textbook. Enriched with web research on ID3 and decision tree induction history.

---

## 1) Technical Explanation

**Decision Tree Classification (slide 14)** re-draws the induction/deduction diagram from [[05_General_Approach_for_Building_Classification_Model]], but now names the specific algorithm family used to learn the model: a **Tree Induction algorithm**. The training set (same 10-row `Attrib1/Attrib2/Attrib3/Class` example) is fed to a tree-induction algorithm, which produces a **Decision Tree** as the model; that tree is then applied (deduction) to the test set to fill in the unknown `Class` values.

**Decision Tree Induction — definitions (slide 15)**:
- *"Decision tree induction is the learning of decision trees (which represents discrete-valued functions) from class-labeled training tuples."* — Note "discrete-valued functions": a plain decision tree, as covered here, is used for **classification** (categorical output), matching the classification/prediction distinction from [[00_Classification_and_Prediction_Overview]] (a variant called a **regression tree** exists for continuous output, but is not covered on this slide).
- *"A decision tree is a flowchart-like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node holds a class label."*

**Worked example — the classic `buys_computer` decision tree**: This example predicts whether a customer will buy a computer (`buys_computer` = yes/no) based on attributes `age`, `student` (yes/no), and `credit_rating` (excellent/fair). Reading the tree:
- **Root node**: test on `age`.
  - `age <= 30` → go to a `student?` node.
    - `student = no` → leaf: **no**.
    - `student = yes` → leaf: **yes**.
  - `age` in `31..40` → leaf directly: **yes** (no further test needed — everyone in this age band buys a computer in this training data).
  - `age > 40` → go to a `credit_rating?` node.
    - `credit_rating = excellent` → leaf: **no**.
    - `credit_rating = fair` → leaf: **yes**.

*(This is the well-known example from Han & Kamber's textbook, widely used across data mining courses to teach tree induction; it is normally introduced together with an **information gain** calculation showing why `age` is chosen as the root-splitting attribute over `student`, `credit_rating`, or `income` — that calculation itself is not shown on this slide, but is worth knowing conceptually, see below.)*

**Decision Trees as logic (slide 16)**:
- *"Decision trees represent a disjunction of conjunctions of constraints on the attribute values of instances."*
- *"Each path from the tree root to a leaf corresponds to a conjunction of attribute tests, and the tree itself is a disjunction of these conjunctions."*
- Reading the `buys_computer` tree this way, the overall rule for `buys_computer = yes` is:
  `(age <= 30 AND student = yes) OR (age = 31..40) OR (age > 40 AND credit_rating = fair)`
  **Verification note**: the source slide's extracted text renders the first clause as `age = >=30`, which is inconsistent with the tree diagram itself (the tree's leftmost branch, leading to the `student?` subtree, is clearly labelled `<=30`). This is almost certainly a text-extraction/font artifact in the original PDF (the "≤" glyph misrendering), not an intentional change to the logic — the disjunction above has been corrected to match the actual tree structure shown in the diagram.
  - Each **path from root to a leaf labelled "yes"** is one conjunction (an AND of tests along that path).
  - The **whole tree** is the OR (disjunction) of all such yes-paths — i.e., a customer buys a computer if *any one* of these three conjunctive conditions holds.

**Why this matters conceptually**: this "disjunction of conjunctions" framing is what makes decision trees naturally interpretable — every prediction the model makes can be traced back to one specific, human-readable AND-chain of conditions, and the full model is just an OR across all such chains that lead to the same class. This interpretability is a major reason decision trees remain popular despite being individually weaker predictors than more complex methods (and is also the direct basis of **rule-based classifiers**, mentioned back in [[00_Classification_and_Prediction_Overview]], which are essentially decision trees "flattened" into an explicit list of if-then rules).

**Background not on the slide but essential context (web research)**: the classic algorithm for *how* a tree-induction algorithm actually chooses which attribute to split on at each node (i.e., why `age` was picked as the root rather than `student` or `credit_rating`) is **ID3 (Iterative Dichotomiser 3)**, invented by **Ross Quinlan in 1986** — this is very likely the specific "Tree Induction algorithm" the course will name explicitly in the next lecture, given that this example is Quinlan/Han-Kamber's canonical ID3 illustration. ID3 works top-down and greedily: at each node, it computes the **entropy** (a measure of class-label impurity/disorder, borrowed from thermodynamics/information theory) of the current subset of data, then computes the **information gain** each candidate attribute would produce if used to split that subset (information gain = reduction in entropy after the split), and picks the attribute with the highest information gain. ID3 has two well-known limitations, both later addressed by Quinlan's successor algorithm **C4.5**: it only handles discrete (categorical) attributes natively (continuous attributes like exact income need to be pre-discretized — connecting back to [[03_Discretization_Introduction_and_Income_Example]] from Lecture 8), and it has no built-in pruning step, so trees built by plain ID3 are prone to **overfitting** the training data (directly tying back to [[03_Bias_and_Variance]] and [[04_Addressing_Overfitting_and_Underfitting]] — a decision tree that is grown too deep, with a leaf for nearly every training tuple, is a textbook case of a high-variance, overfit model).

---

## 2) Simple English Explanation

A **decision tree** is exactly what it sounds like: a flowchart of yes/no (or multiple-choice) questions that ends in an answer. You start at the top (the "root"), answer a question about one of your attributes, follow the matching branch down, and either land on another question or on a final answer (a "leaf").

**The classic example on the slide**: predicting whether someone will buy a computer.
- First question: **How old are they?**
  - **30 or younger** → ask a follow-up: **Are they a student?**
    - No → prediction: **won't buy**.
    - Yes → prediction: **will buy**.
  - **31 to 40** → no more questions needed, prediction: **will buy** (in this particular training data, everyone in this age range bought one).
  - **Over 40** → ask a follow-up: **Is their credit rating excellent or fair?**
    - Excellent → prediction: **won't buy**.
    - Fair → prediction: **will buy**.

This tree was itself learned automatically from a training set of past customers — the algorithm looked at the data and figured out on its own that "age" was the single most useful first question to ask (it splits the customers into the most "pure" groups compared to starting with any other question), then repeated the process within each branch.

**Why "disjunction of conjunctions" (in plain terms)**: every route from the top of the tree down to a "will buy: yes" answer is one specific combination of conditions joined by AND — like "age is 30-or-under AND is a student." The whole tree, as a rule for "who buys a computer," is really just: "this combination OR that combination OR that other combination" — i.e., someone buys a computer if they match *any one* of the yes-paths through the tree. This is why decision trees are so easy to explain to a non-technical person — you can literally read off the plain-English rule for any prediction.

*(One thing this note double-checked: the text pulled from the original PDF for the combined rule had a small typo — it said "age >= 30" where it should say "age <= 30" to match the actual tree picture. This has been corrected here.)*

**Where this tree actually comes from**: an algorithm called **ID3**, invented by Ross Quinlan in 1986, is the classic method for automatically building trees like this — it works by always picking, at each step, whichever question does the best job of separating "yes" customers from "no" customers (measured using a concept called "information gain"). One weakness of plain ID3: if you let it keep asking questions forever, it can end up creating a super-specific question for almost every individual customer in the training data — which is a textbook case of overfitting (see [[03_Bias_and_Variance]]).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek **decision tree** bilkul waisa hi hai jaisa naam se lagta hai: yes/no (ya multiple-choice) sawaalon ka ek flowchart jo ek answer pe khatam hota hai. Tum top se (the "root") start karte ho, apne attributes mein se ek ke baare mein sawaal ka jawab dete ho, matching branch follow karte hue neeche jaate ho, aur ya to ek aur sawaal pe pahunchte ho ya ek final answer (a "leaf") pe.

**Slide ka classic example**: predict karna ki koi computer khareedega ya nahi.
- Pehla sawaal: **Unki age kya hai?**
  - **30 ya usse kam** → ek follow-up poocho: **Kya wo student hai?**
    - Nahi → prediction: **nahi khareedega**.
    - Haan → prediction: **khareedega**.
  - **31 se 40 ke beech** → koi aur sawaal nahi chahiye, prediction: **khareedega** (is particular training data mein, is age range ke sab logon ne khareeda tha).
  - **40 se zyada** → ek follow-up poocho: **Unka credit rating excellent hai ya fair?**
    - Excellent → prediction: **nahi khareedega**.
    - Fair → prediction: **khareedega**.

Ye tree khud automatically seekha gaya tha purane customers ke ek training set se — algorithm ne data dekha aur khud figure out kiya ki "age" sabse pehle poochne ke liye sabse useful sawaal hai (ye customers ko sabse "pure" groups mein baant deta hai kisi bhi aur sawaal se start karne ke comparison mein), fir har branch ke andar wahi process repeat kiya.

**"Disjunction of conjunctions" ka matlab (simple bhasha mein)**: tree ke top se "khareedega: yes" answer tak ki har route ek specific combination of conditions hai jo AND se judi hui hai — jaise "age 30-ya-kam AND student hai." Poora tree, "kaun computer khareedta hai" ke liye ek rule ke roop mein, actually bas ye hai: "ye combination YA wo combination YA wo dusra combination" — matlab koi computer khareedta hai agar wo tree ke in yes-paths mein se *kisi bhi ek* se match kare. Isi liye decision trees ko ek non-technical insaan ko samjhana itna easy hai — tum literally kisi bhi prediction ka plain-English rule padh sakte ho.

*(Ek cheez jo is note mein double-check ki gayi: original PDF se nikale gaye text mein combined rule mein ek chhoti si typo thi — usme "age >= 30" likha tha jabki asli tree picture ke hisaab se "age <= 30" hona chahiye. Isse yahaan correct kar diya gaya hai.)*

**Ye tree asal mein kahan se aata hai**: ek algorithm jiska naam **ID3** hai, jise Ross Quinlan ne 1986 mein banaya tha, aise trees automatically banane ka classic method hai — ye har step pe wahi sawaal choose karta hai jo "yes" customers ko "no" customers se sabse achhe tarike se alag karta hai (ise "information gain" naam ke concept se measure kiya jaata hai). Plain ID3 ki ek weakness: agar usse hamesha sawaal poochne do, to wo training data ke almost har individual customer ke liye ek super-specific sawaal bana sakta hai — jo overfitting ka ek textbook case hai (dekho [[03_Bias_and_Variance]]).
