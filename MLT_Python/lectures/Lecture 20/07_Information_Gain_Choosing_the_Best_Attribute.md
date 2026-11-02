# Topic 7: Information Gain — Choosing the Best Attribute

Source: Lecture 20, slide 15 ("Information gain", with the instructor's tick marks on the symbol definitions). Enriched with web research (information gain = mutual information; conditional entropy).

---

## 1) Technical Explanation

**Slide 15 — what it says.**
- **Information gain** assesses how much valuable information an attribute can provide. **Select the attribute with the highest information gain** — it contributes most to understanding the data. High gain ⇒ the attribute offers significant insight.
- ID3 "acts like an **investigator**": at each step it makes the choice that **maximises information gain**, aiming to **minimise uncertainty** and make well-informed decisions (which can be further enhanced by preprocessing the data).

**Formula (slide):**

IG(A, D) = H(S) − Σ_v ( |S_v| / |S| ) × H(S_v)

(The slide prints a stray closing bracket "]" after the last term; it is a typesetting slip, not part of the maths.)

**Symbols (as defined on the slide).**
- |S| = total number of instances in the dataset.
- |S_v| = number of instances for which the attribute has value **v**. (The slide says "attribute D"; the formula's first argument is called A — the same attribute. In the worked example on slide 20 the instructor writes Gain(S, Outlook).)
- H(S) = entropy of the whole dataset ([[06_Entropy_Measuring_Disorder_in_a_Dataset]]).
- H(S_v) = entropy of the subset where the attribute takes value v.

**Meaning in one line.**

Information gain = *entropy before the split* − *weighted-average entropy after the split*.

The second term, Σ (|S_v|/|S|) H(S_v), is the **conditional entropy** H(S | A): the expected disorder left after we know the attribute's value. Each subset is **weighted by its size**, so a big impure subset hurts more than a tiny one.

**Properties.**
- IG ≥ 0 always; IG = 0 means the attribute tells us nothing about the class; the largest possible IG equals H(S) (a perfect split into pure subsets).
- Information gain equals the **mutual information** between the attribute and the class label (information-theory view).
- **Known bias (research):** information gain favours attributes with many distinct values (e.g. an ID column would split into all-pure singletons and get maximum gain but be useless). C4.5 fixes this with **gain ratio** ([[05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea]]).

**Tiny sanity example (computed).** S = 4 Yes + 4 No → H = 1. An attribute splits it into {3 Yes,1 No} and {1 Yes,3 No}: each subset H = 0.8113, weights ½ and ½, so IG = 1 − 0.8113 = **0.189**. A perfect attribute splitting into {4 Yes} and {4 No} gives IG = 1 − 0 = **1.0**.

---

## 2) Simple English Explanation

**The idea.** You want to guess whether tennis will be played. Each column you could ask about (Outlook? Wind? Humidity?) helps a little. **Information gain tells you how much a question reduces your confusion** — the bigger the gain, the more useful the question.

**How to compute it — four steps.**
1. **Measure the confusion before asking** anything: that's the entropy of the whole group, H(S).
2. **Ask the question** and sort the examples into piles by the answer (one pile per possible answer).
3. **Measure the confusion inside each pile**, then take an **average that gives bigger piles more weight** (a pile with 10 examples should count more than a pile with 2). Each pile's weight is its size ÷ the total.
4. **Gain = confusion before − average confusion after.**

**The formula, read aloud.** IG(A, D) = H(S) − Σ (|S_v| / |S|) × H(S_v). In words: *entropy of everything*, minus the *sum over each answer v* of *(how many examples gave that answer ÷ total examples)* × *entropy of those examples*. Here |S| is the total number of examples, |S_v| is how many have value v, and H(S_v) is the mess score of that pile. (The slide prints a stray "]" at the end — just a typing slip.)

**The "investigator" idea.** The teacher says ID3 behaves like a detective: at every step it asks the question that clears up the most mystery. It selects the attribute with the **highest** gain, because that attribute offers the most insight.

**A tiny example.** A group of 8 days, 4 yes and 4 no, has confusion 1.0. Suppose a question splits it into {3 yes, 1 no} and {1 yes, 3 no}. Each pile has mess 0.81 and weight ½, so the average mess after = 0.81 and the gain = 1.0 − 0.81 = **0.19**. A perfect question that gave {4 yes} and {4 no} would have gain 1.0 − 0 = **1.0**.

**Handy facts.**
- Gain is never negative. Gain = 0 means the question tells you nothing.
- The biggest gain possible equals the starting entropy.
- Beware: gain likes questions with *many* different answers (like a "Day number" column that gives every day its own pile). Those piles are trivially pure but useless for new days. A later version of the algorithm, C4.5, corrects this with "gain ratio".

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Idea.** Tumhe guess karna hai ki tennis khela jayega ya nahi. Har column jiske baare mein poochh sakte ho (Outlook? Wind? Humidity?) thodi madad karta hai. **Information gain batata hai ki ek sawaal ne tumhara confusion kitna kam kiya** — gain jitna bada, sawaal utna kaam ka.

**Kaise nikalte hain — chaar steps.**
1. Kuch poochne se **pehle ka confusion** naapo: poore group ki entropy, H(S).
2. **Sawaal poocho** aur jawaab ke hisaab se examples ki dheriyan banao (har possible jawaab ke liye ek dheri).
3. **Har dheri ke andar ka confusion** naapo, phir **aisa average lo jisme bade group ko zyada weight mile** (10 examples wali dheri ka asar 2 wali se zyada hona chahiye). Har dheri ka weight = uska size ÷ total.
4. **Gain = pehle ka confusion − baad ka average confusion.**

**Formula, bol kar.** IG(A, D) = H(S) − Σ (|S_v| / |S|) × H(S_v). Shabdon mein: *sab ki entropy*, minus *har jawaab v par sum* ka *(kitne examples ne wo jawaab diya ÷ total examples)* × *un examples ki entropy*. Yahan |S| total examples hain, |S_v| wo jinki value v hai, aur H(S_v) us dheri ka mess score hai. (Slide ke ant mein ek faltu "]" chhapa hai — bas typing ki chook.)

**"Investigator" wali baat.** Sir kehte hain ID3 ek detective jaisa hai: har step par wo sawaal poochta hai jo sabse zyada mystery solve kare. Wo **sabse bade** gain wala attribute chunta hai, kyunki wahi sabse zyada insight deta hai.

**Ek chhota example.** 8 dino ka group, 4 yes aur 4 no, confusion 1.0. Maan lo ek sawaal ise {3 yes, 1 no} aur {1 yes, 3 no} mein baant deta hai. Dono dheriyon ka mess 0.81 aur weight ½, to baad ka average mess = 0.81 aur gain = 1.0 − 0.81 = **0.19**. Ek perfect sawaal jo {4 yes} aur {4 no} deta, uska gain 1.0 − 0 = **1.0** hota.

**Kaam ki baatein.**
- Gain kabhi negative nahi hota. Gain = 0 matlab sawaal kuch nahi batata.
- Sabse bada possible gain starting entropy ke barabar hota hai.
- Savdhaan: gain un sawaalon ko pasand karta hai jinke *bahut saare alag jawaab* ho (jaise "Day number" column jo har din ko apni dheri deta hai). Aisi dheriyan aasaani se pure hoti hain par naye dino ke liye bekaar. Baad ka version C4.5 ise "gain ratio" se theek karta hai.
