# Topic 2: Tree Structure, Key Terms and Where Decision Trees Are Used

Source: Lecture 20, slides 4–5 ("Decision Tree" bullet list, "Example"). Enriched with web research (pruning, regression trees).

---

## 1) Technical Explanation

**Slide 4 — the lecture's roadmap.** A decision tree is a machine-learning algorithm used for **both classification and regression**. The slide lists six concepts:

1. **Tree structure**
2. **Decision nodes**
3. **Leaf nodes**
4. **Splitting**
5. **Entropy and information gain**
6. **Pruning**

**Definitions.**

| Term | Meaning |
|---|---|
| **Root node** | The topmost decision node; the first question asked, applied to the whole training set. |
| **Decision (internal) node** | A node that tests one attribute and branches into children, one per outcome/value. |
| **Branch / edge** | One outcome of a test (e.g. Outlook = Sunny). |
| **Leaf (terminal) node** | A node with no children; it holds the final prediction (a class label for classification, a number for regression). |
| **Splitting** | Dividing the set of examples at a node into subsets according to the test's outcome. |
| **Entropy / information gain** | The numbers used to decide *which* attribute to split on (topics 06–07). |
| **Pruning** | Cutting back branches that do not generalise (not worked out in this lecture's slides — see below). |
| **Depth** | Length of the longest root-to-leaf path. |

**Classification vs. regression trees.** If the target is a category (spam / not spam) the leaf stores the majority class; if the target is a number (house price) the leaf stores the average of the training targets in that leaf. ID3, which this lecture develops, builds *classification* trees on categorical attributes.

**Slide 5 — typical uses.** Predicting an email as **spam / not spam**; whether a **tumor is cancerous**; whether a **loan is a good or bad credit risk** — each based on the relevant factors.

**Slide 5 — the training workflow.**
1. Build the model from **observed (training) data**.
2. Use a **validation set** to verify and improve the model.
3. For a **new set of predictor variables**, run the example down the tree to get the category (yes/no, spam/not spam).

**Pruning (enrichment — the slide only names it).** A tree grown until every leaf is pure will memorise noise (overfitting, see [[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17). *Pre-pruning* stops growth early (max depth, minimum samples per leaf, minimum gain); *post-pruning* grows the full tree and then removes subtrees that do not improve accuracy on validation data (e.g. reduced-error pruning). Research also notes that finding the *smallest* possible tree is NP-hard (Hyafil & Rivest, 1976), which is why greedy construction plus pruning is used in practice ([[04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy]]).

---

## 2) Simple English Explanation

**The lecture's roadmap (slide 4).** A decision tree is a learning method that can answer *category* questions (spam or not spam?) and *number* questions (what will the price be?). The teacher lists six ideas we will meet: the tree's **structure**, **decision nodes**, **leaf nodes**, **splitting**, **entropy and information gain**, and **pruning**.

**The vocabulary, using one picture in your head — an upside-down tree:**
- **Root** — the very first question, at the top. It looks at *all* the examples.
- **Decision node** (also called internal node) — any other question box. It asks about one feature and has one arrow for each possible answer.
- **Branch / edge** — one answer to a question (e.g. "Outlook = Sunny").
- **Leaf** — a box with no arrows leaving it. It holds the final answer: a *category* (spam) or a *number* (average price).
- **Splitting** — sorting the examples into smaller piles according to the answer.
- **Depth** — how many questions deep the longest path goes.
- **Entropy / information gain** — scores that tell us which question to ask. (Next topics.)
- **Pruning** — trimming off useless twigs.

**Where trees are used (slide 5).** Is this email spam? Is this tumour cancerous? Is this loan applicant a good or bad credit risk? In each case the tree looks at the relevant facts (words in the email, test results, income and past loans) and walks down to an answer.

**How the whole process works (slide 5).**
1. Build the tree from **training data** — examples where the right answer is already known.
2. Use a separate **validation set** to check how well it does and to improve it.
3. For a brand-new case, follow the questions from the top to a leaf. The leaf's answer is the prediction.

**Why pruning matters (not worked out on the slides).** If you keep splitting until every pile is perfectly pure, the tree starts memorising random quirks of the training data, like a student who memorises last year's exam paper but can't solve new questions (**overfitting**). Two cures: *stop early* (limit how deep it can grow), or *grow fully, then trim* the branches that don't help on validation data. Finding the very smallest tree is a famously hard problem, so in practice we grow quickly and trim afterwards.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Lecture ka roadmap (slide 4).** Decision tree ek learning method hai jo *category* wale sawaal (spam hai ya nahi?) aur *number* wale sawaal (price kitna hoga?) dono ka jawaab de sakta hai. Sir ne chhe cheezein likhi hain jo hum dekhenge: tree ka **structure**, **decision nodes**, **leaf nodes**, **splitting**, **entropy aur information gain**, aur **pruning**.

**Vocabulary — ek ulte tree ki tasveer dimaag mein rakho:**
- **Root** — sabse upar ka pehla sawaal. Ye *saare* examples ko dekhta hai.
- **Decision node** (internal node bhi kehte hain) — baaki saare sawaal ke boxes. Ye ek feature ke baare mein poochta hai aur har possible jawaab ke liye ek teer hota hai.
- **Branch / edge** — ek sawaal ka ek jawaab (jaise "Outlook = Sunny").
- **Leaf** — wo box jisme se koi teer bahar nahi nikalta. Isme final jawaab hota hai: *category* (spam) ya *number* (average price).
- **Splitting** — examples ko jawaab ke hisaab se chhoti dheriyon mein baantna.
- **Depth** — sabse lambe raaste mein kitne sawaal hain.
- **Entropy / information gain** — wo scores jo batate hain kaun sa sawaal poochna hai. (Agle topics mein.)
- **Pruning** — faltu daaliyan kaatna.

**Trees kahan use hote hain (slide 5).** Ye email spam hai? Ye tumor cancerous hai? Ye loan lene wala good ya bad credit risk hai? Har case mein tree zaroori facts dekhta hai (email ke words, test results, income aur purane loans) aur chalte-chalte ek jawaab tak pahunchta hai.

**Poora process kaise chalta hai (slide 5).**
1. **Training data** se tree banao — wo examples jinka sahi jawaab pehle se pata hai.
2. Ek alag **validation set** se check karo ki kitna achha kaam kar raha hai aur improve karo.
3. Bilkul naye case ke liye upar se leaf tak sawaal follow karo. Leaf ka jawaab hi prediction hai.

**Pruning kyun zaroori hai (slides mein nahi samjhaya).** Agar tum tab tak split karte raho jab tak har dheri bilkul pure na ho jaye, to tree training data ki random ajeeb baatein ratt leta hai — us student ki tarah jo pichhle saal ka paper ratt leta hai par naye sawaal nahi hal kar paata (**overfitting**). Do ilaaj: *jaldi ruk jao* (tree ko zyada gehra mat badhne do), ya *poora ugao phir kaato* jo branches validation data par kaam nahi aati. Sabse chhota tree dhundhna famous mushkil problem hai, isliye practice mein jaldi ugate hain aur baad mein chhaantte hain.
