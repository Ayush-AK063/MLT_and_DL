# Topic 5: The ID3 Algorithm — What It Is, Who Made It, and How It Works in One Paragraph

Source: Lecture 20, slide 13 ("Example: ID3 Algorithm" / "What is Iterative Dichotomiser3 Algorithm?"). Enriched with web research (Quinlan 1986 paper, C4.5 1993, CART 1984, ID3's limitations).

---

## 1) Technical Explanation

**Slide 13 — definitions.**
- **ID3 = Iterative Dichotomiser 3.** It builds decision trees from a given dataset. Developed in **1986** by **Ross Quinlan** (the slide's date; the standard citation is Quinlan, "Induction of Decision Trees", *Machine Learning* 1(1), 1986).
- It is a **greedy algorithm** that builds the tree by **recursively partitioning** the data into smaller and smaller subsets **until all data points in each subset belong to the same class**.
- It uses a **top-down** approach, selecting at each step the feature to split on according to **information gain**.

**The name.** *Dichotomiser* means "divider" (splitting data into groups); the "3" is usually explained as the third in Quinlan's series of programs — this is common background knowledge, **not on the slides and not verified in this session**. ID3 itself branches on *every* value of a categorical attribute, not just two (see the Outlook split with three branches, [[10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook]]).

**Properties of ID3 (from the slides + research).**

| Property | Meaning |
|---|---|
| Greedy | Picks the locally best attribute; never backtracks ([[04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy]]) |
| Top-down, recursive | Starts at the root with all data and recurses on each subset |
| Split criterion | Information gain (based on entropy) |
| Stops when | The subset is pure (one class) — or no attributes are left |
| Attribute types | **Categorical only** in the original ID3 |
| Pruning | **None** in the original ID3 → tends to overfit |

**Family tree of algorithms (research).**

| Algorithm | Year | Key difference from ID3 |
|---|---|---|
| **ID3** | 1986 (Quinlan) | Information gain, categorical, no pruning |
| **CART** | 1984 (Breiman, Friedman, Olshen, Stone) | **Gini index**, binary splits, handles regression too |
| **C4.5** | 1993 (Quinlan) | **Gain ratio**, continuous attributes, missing values, pruning |

ID3, CART and C4.5 were developed independently but share the same greedy top-down recipe. (Sources disagree slightly on some early dates; 1986 for ID3 is the one the slide uses and the one in the primary paper.)

**Flag — Gini vs. entropy.** Slide 14 says ID3 "uses a measure of impurity, such as entropy or Gini impurity". Strictly, **original ID3 uses entropy / information gain only**; Gini impurity is the criterion of **CART**. Both are impurity measures and behave similarly, so the slide's remark is loosely true of "decision-tree algorithms" in general, but not of ID3 itself ([[06_Entropy_Measuring_Disorder_in_a_Dataset]]).

---

## 2) Simple English Explanation

**What ID3 is.** ID3 is a *recipe* for building a decision tree from a table of examples. Its full name is **Iterative Dichotomiser 3**. It was created by **Ross Quinlan in 1986**. (The name part "Dichotomiser" roughly means "divider" — something that splits data into groups. The "3" is usually explained as "the third in Quinlan's series of programs"; that's background knowledge, not something on the slides.)

**The recipe in plain words.**
1. Put all the examples together at the top.
2. Pick the question (column) that splits them into the **cleanest** groups.
3. Split the examples by that question's answers.
4. Do the same thing again inside each group, and again, and again — until every group has just **one kind of answer**.

**Two words that describe the style.**
- **Greedy** — at each step it takes whatever looks best right now. It never goes back to change an earlier choice. (Like choosing the biggest slice of cake at each turn without thinking whether a different plan would have given you more overall.)
- **Top-down** — it starts with the big picture at the top and works down to small groups at the bottom.

**What it measures to pick "the cleanest" split.** It uses a score called **information gain**, which is built from **entropy** (a "messiness" number). You'll learn both in the next two topics.

**Limits of the original ID3.**
- It works only with **categories** such as Sunny/Rain/Overcast, not raw numbers like 31.5 °C.
- It never trims the tree, so it can learn the training examples *too* exactly (overfitting).
- It likes columns with lots of different values too much.

**The family it belongs to.** Two cousins appeared around the same time: **CART** (1984) and, later, Quinlan's own improved **C4.5** (1993), which fixed several of ID3's limits (numbers, missing values, trimming). All use the same greedy top-down idea.

**One mistake on the slide.** Slide 14 says ID3 uses "entropy or Gini". That's a slip: ID3 uses **entropy / information gain only**; **Gini** belongs to the CART algorithm. Both measure messiness and behave alike, so it's a small point — but good to know for exams.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**ID3 kya hai.** ID3 examples ki table se decision tree banane ki ek *recipe* hai. Iska poora naam **Iterative Dichotomiser 3** hai. Ise **Ross Quinlan ne 1986 mein** banaya. ("Dichotomiser" ka matlab lagbhag "baantne wala" — jo data ko groups mein baante. "3" ko aam taur par "Quinlan ke programs ki series mein teesra" kaha jata hai; ye background knowledge hai, slides mein nahi hai.)

**Recipe simple shabdon mein.**
1. Saare examples ek saath upar rakho.
2. Wo sawaal (column) chuno jo examples ko sabse **saaf-suthre** groups mein baante.
3. Us sawaal ke jawaabon ke hisaab se examples baant do.
4. Har group ke andar yahi kaam dobara, phir dobara karo — jab tak har group mein sirf **ek hi tarah ka jawaab** na bache.

**Iska style batane wale do shabd.**
- **Greedy** — har step par jo abhi sabse achha lage wahi leta hai. Pichhla choice kabhi wapas nahi badalta. (Jaise cake ka har baar sabse bada tukda le lena, ye soche bina ki doosra plan overall zyada de sakta tha.)
- **Top-down** — upar ke bade picture se shuru karke neeche chhote groups tak aata hai.

**"Sabse saaf" split chunne ke liye kya naapta hai.** Ek score use karta hai jise **information gain** kehte hain, jo **entropy** ("ghalat-malat" naapne ka number) se banta hai. Dono agle do topics mein seekhoge.

**Original ID3 ki limits.**
- Sirf **categories** (Sunny/Rain/Overcast) par chalta hai, 31.5 °C jaise raw numbers par nahi.
- Tree ko kabhi chhaanta nahi, isliye training examples ko *zyada hi* ratt sakta hai (overfitting).
- Bahut saari alag values wale columns ko zyada pasand karta hai.

**Kis family ka hai.** Lagbhag usi samay do cousins aaye: **CART** (1984) aur baad mein Quinlan ka khud ka behtar **C4.5** (1993), jisne ID3 ki kai limits theek ki (numbers, missing values, chhaantna). Sab same greedy top-down idea use karte hain.

**Slide ki ek galti.** Slide 14 kehti hai ID3 "entropy ya Gini" use karta hai. Ye chook hai: ID3 sirf **entropy / information gain** use karta hai; **Gini** CART algorithm ka hai. Dono ghalat-malat naapte hain aur milte-julte chalte hain, isliye chhoti baat hai — par exam ke liye jaanna achha hai.
