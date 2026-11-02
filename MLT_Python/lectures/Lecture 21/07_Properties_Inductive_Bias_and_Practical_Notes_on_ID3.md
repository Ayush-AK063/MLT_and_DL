# Topic 7: What the Finished Tree Teaches Us — ID3's Bias, Limits and Practical Notes (research enrichment)

Source: Not on the slides — this topic is **research enrichment** (Mitchell, *Machine Learning*, 1997 ch. 3; lecture notes on ID3's inductive bias and Occam's razor; scikit-learn behaviour recalled from general knowledge and flagged as such) tying together Lectures 20–21.

---

## 1) Technical Explanation

**Recap of the full ID3 run on PlayTennis.**

| Step | Candidate gains | Choice |
|---|---|---|
| Root (14 days) | Outlook 0.2467, Humidity 0.1518, Wind 0.0481, Temp 0.0292 | **Outlook** |
| Sunny (5 days) | Humidity 0.971, Temp 0.571, Wind 0.020 | **Humidity** |
| Overcast (4 days) | — pure | leaf **Yes** |
| Rain (5 days) | Wind 0.971, Temp 0.020, Humidity 0.020 | **Wind** |

Result: 3 decision nodes, 5 leaves, depth 2, Temp unused ([[06_Rain_Subset_and_the_Final_Decision_Tree]]).

**1. Inductive bias.** ID3 searches the space of all possible trees from simple to complex, greedily. Its bias (per course notes on Mitchell's treatment) is a **preference for shorter trees**, and for trees that put **high-information-gain attributes near the root**. This is a *preference bias*, not a restriction of the hypothesis space. It echoes **Occam's razor** (prefer the simplest hypothesis that fits), although the justification is debated. Because the search is greedy ([[04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy]] from Lecture 20), the shortest tree is *not guaranteed*.

**2. Overfitting.** ID3 keeps splitting until leaves are pure, so it fits the training set perfectly (here 14/14) — including noise. On noisy data this yields large, brittle trees; remedies are **pre-pruning** (depth/min-samples limits), **post-pruning** (reduced-error pruning on validation data), and ensembles. See [[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17.

**3. Limitations of original ID3.**
- Categorical attributes only (numeric ones need threshold splits → C4.5).
- No handling of missing values.
- Information gain favours attributes with many distinct values (a "Day" ID column would get maximal gain but is useless) → **gain ratio** in C4.5 ([[05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea]] from Lecture 20).
- Small changes in data can change the root and hence the entire tree (high variance).

**4. Interpretability.** The tree reads as five if–then rules, each root-to-leaf path being one rule — an advantage over black-box models.

**5. In practice (Python).** *From general knowledge, not verified in this session:* scikit-learn's `DecisionTreeClassifier` implements **CART**, not ID3; `criterion="entropy"` uses information gain, but trees are **binary** (a 3-valued attribute like Outlook is encoded/split in two-way tests) and, by default, grown until pure, so pruning parameters (`max_depth`, `min_samples_leaf`, `ccp_alpha`) are needed to control overfitting. Categorical text values must be encoded to numbers first.

**6. Gotchas seen in these slides (all harmless).**
- Handwritten gains are rounded intermediates: Outlook 0.2464 vs exact 0.2467, Temp 0.0289 vs 0.0292, Humidity 0.1516 vs 0.1518, Sunny-Temp 0.570 vs 0.571, Sunny-Wind 0.0192 vs 0.0200.
- Slide 13 and slide 15 show the same tree; slide 15's lower edge is cropped.

---

## 2) Simple English Explanation

**What did building this tree teach us?**

**1. The tree is a short list of rules.**
- Sunny and high humidity → don't play.
- Sunny and normal humidity → play.
- Overcast → play.
- Rain and strong wind → don't play.
- Rain and weak wind → play.
Anyone can read these and check them. That's the big selling point of decision trees.

**2. ID3 likes short trees.** It tries to ask the most useful question first (Outlook), so that later branches need few questions. Temperature was never needed. This habit — preferring simple, short explanations — is related to an old idea called "Occam's razor": if a simple explanation fits the facts, prefer it.

**3. It can be *too* perfect.** Our tree gets all 14 training days right, because it keeps asking questions until each box is clean. With messy real-life data (a few wrong labels, random flukes) such a tree would memorise the flukes and then stumble on new days. This is **overfitting**. The usual cure is **pruning**: stop growing early, or grow the full tree and then trim the branches that don't really help.

**4. Greedy means "best right now".** ID3 picks the best question at each step without planning ahead. That's fast, but there might be a slightly smaller tree it never tries.

**5. Limits of basic ID3.**
- Only works with categories (Sunny/Rain), not raw numbers.
- Doesn't handle missing values.
- Overrates columns with lots of different values.
- Change a few rows of data and the top question (and so the whole tree) can change.
Later versions (C4.5, CART) fix most of these.

**6. Using it in Python (general knowledge — not checked in this session).** The popular library scikit-learn has a `DecisionTreeClassifier`. It is really the **CART** algorithm, not ID3. You can ask it to use entropy ("information gain"), but its trees are always two-way splits, and by default it grows until the boxes are pure — so you'd set limits (like a maximum depth) to avoid overfitting. Text answers like "Sunny" must first be turned into numbers.

**Small things you may notice on the slides.** The teacher's handwritten gains are slightly rounded (0.2464 instead of 0.2467, etc.). Slide 13 and slide 15 show the same tree at different stages; slide 15's bottom edge is cut off in the PDF.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Is tree ko banane se humne kya seekha?**

**1. Tree rules ki ek chhoti list hai.**
- Sunny aur high humidity → mat khelo.
- Sunny aur normal humidity → khelo.
- Overcast → khelo.
- Rain aur strong wind → mat khelo.
- Rain aur weak wind → khelo.
Koi bhi inhe padh kar check kar sakta hai. Decision trees ki sabse badi khoobi yahi hai.

**2. ID3 chhote trees pasand karta hai.** Wo sabse kaam ka sawaal pehle poochta hai (Outlook), taaki baad ki branches ko kam sawaal chahiye. Temperature ki kabhi zaroorat nahi padi. Ye aadat — simple, chhoti explanation ko pasand karna — ek purane idea "Occam's razor" se judi hai: agar simple explanation facts se match karti hai to wahi chuno.

**3. Ye *zyada hi* perfect ho sakta hai.** Hamara tree saare 14 training dino ko sahi pehchanta hai, kyunki jab tak har box saaf na ho wo sawaal poochta rehta hai. Gandle real-life data (kuch galat labels, random flukes) par aisa tree flukes ko ratt leta hai aur naye dino par ladkhadata hai. Ye **overfitting** hai. Aam ilaaj **pruning** hai: jaldi ruk jao, ya poora tree ugao aur phir wo branches kaat do jo sach mein kaam nahi aati.

**4. Greedy matlab "abhi ka best".** ID3 aage ki planning ke bina har step par best sawaal chunta hai. Ye tez hai, par ho sakta hai koi thoda chhota tree ho jo wo kabhi try na kare.

**5. Basic ID3 ki limits.**
- Sirf categories (Sunny/Rain) par chalta hai, raw numbers par nahi.
- Missing values handle nahi karta.
- Bahut saari alag values wale columns ko zyada number deta hai.
- Data ki kuch rows badlo to sabse upar ka sawaal (aur isliye poora tree) badal sakta hai.
Baad ke versions (C4.5, CART) inme se zyadatar theek karte hain.

**6. Python mein use (general knowledge — is session mein verify nahi kiya).** Mashhoor library scikit-learn mein `DecisionTreeClassifier` hota hai. Wo asal mein **CART** algorithm hai, ID3 nahi. Tum use entropy ("information gain") use karne ko keh sakte ho, par uske trees hamesha do-tarfa splits hote hain, aur by default wo tab tak ugta hai jab tak box pure na ho — isliye overfitting se bachne ke liye limits (jaise maximum depth) lagani padti hain. "Sunny" jaise text jawaabon ko pehle numbers mein badalna padta hai.

**Slides par dikhne wali chhoti baatein.** Sir ke haath se likhe gains thode rounded hain (0.2467 ki jagah 0.2464, wagairah). Slide 13 aur slide 15 same tree ko alag stages mein dikhati hain; slide 15 ka neeche ka hissa PDF mein kata hua hai.
