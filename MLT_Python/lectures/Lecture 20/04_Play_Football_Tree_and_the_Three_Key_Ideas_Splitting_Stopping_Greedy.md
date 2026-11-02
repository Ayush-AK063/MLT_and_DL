# Topic 4: The "Play Football?" Tree and the Three Key Ideas (Splitting Criterion, Keep Splitting, Greedy Approach)

Source: Lecture 20, slide 12 ("Play Football ?" with the instructor's red handwritten annotations). Enriched with web research (greedy vs. global optimum, NP-hardness of optimal trees, dynamic programming alternatives).

---

## 1) Technical Explanation

**The tree on the slide.**

```
Weather
├─ Sunny  → Temp.
│            ├─ Hot  → No
│            ├─ Mild → Yes
│            └─ Cold → Yes
├─ Cloudy → Yes
└─ Rain   → Yes
```

Root = **Weather** (3 values). *Cloudy* and *Rain* are already decided (Yes). Only *Sunny* needs another question, **Temp.**, whose three values lead to leaves No / Yes / Yes.

**The three handwritten points.**

**① Splitting criteria — entropy / information gain.** Before building any tree we must decide *how to choose the attribute at each node*. The criteria introduced are **entropy** and **information gain** ([[06_Entropy_Measuring_Disorder_in_a_Dataset]], [[07_Information_Gain_Choosing_the_Best_Attribute]]).

**② Keep on splitting until all data points belong to the same (one) class.** This is the **stopping rule** of the basic algorithm: recurse on each subset until it is *pure* (entropy 0, all examples share one label). In the football tree, Cloudy and Rain are already pure; Sunny is split by Temp. until each Temp value is pure.

**③ Greedy approach.** At each node the algorithm picks the attribute that looks **best right now**, without looking ahead and never undoing the choice. The instructor illustrates this with a **hill-climbing picture**: a curve with several peaks, labelled *local max*, *1st best*, *Top*, *Global maximum*. A greedy climber who always steps uphill ends on the nearest peak (a **local maximum**) and may miss the **global maximum**. The note beside it reads: **greedy → "Dynamic Programming Alg."** — i.e. the alternative that can guarantee a global optimum is dynamic programming. (The name "Bhuvan" scribbled next to the hill appears to be a person used in the climbing analogy; the handwriting is not fully legible, so treat that detail as uncertain.)

**Research enrichment.**
- Finding the *smallest* decision tree consistent with the data is **NP-hard** (Hyafil & Rivest, 1976), so exact search is impractical for real data. Greedy top-down induction (ID3, C4.5, CART) is the practical compromise: fast, gives good accuracy, but **no guarantee** of the smallest or best tree.
- Greedy trees tend to grow large and overfit, which is why **pruning** is added afterwards ([[02_Tree_Structure_Terminology_and_Where_Trees_Are_Used]]).
- Newer research shows dynamic programming with branch-and-bound can find optimal (shallow) trees and sometimes beat greedy trees by a few % accuracy, but only for small depths — this matches the instructor's "dynamic programming" remark.
- Strictly, greedy tree induction is a *single top-down pass* (no iterative improvement), so "hill climbing" is an analogy for the greedy idea, not a literal description of the procedure.

**Where the three ideas show up later.** ① is topics 06–07; ② and ③ are the loop in [[08_Steps_of_the_ID3_Algorithm]].

---

## 2) Simple English Explanation

**The picture (slide 12): "Shall we play football?"** First look at the weather:
- **Cloudy** → play.
- **Rain** → play (as drawn on the slide).
- **Sunny** → ask one more question, the **temperature**: hot → don't play, mild → play, cold → play.

The tree has only two question boxes (Weather, Temp.). Cloudy and Rain are already settled, so only the Sunny branch needed another question.

**The teacher then wrote three big ideas in red.**

**① How do we choose the question? — "splitting criteria".** We use two scores called **entropy** and **information gain** (explained in the next topics). Think of them as ways of asking "which question clears up the most confusion?".

**② When do we stop? — "keep on splitting until every group has one answer".** Keep asking questions inside each group until everyone in the group has the same answer (all "play" or all "don't play"). A group like that is called **pure**.

**③ How do we build it? — the "greedy approach".** At each step pick the question that looks best *right now*; don't look ahead, and never go back and change a choice.

**The hill-climbing picture explained.** Imagine climbing a hilly landscape in thick fog. Your rule: always step uphill. You'll end up on top of some hill — but maybe a small one (a **local maximum**), while a much higher mountain (the **global maximum**) stands elsewhere and you never find it, because reaching it would have meant first going *downhill*. Greedy is the same: fast and usually good, but it can miss the very best tree. The teacher noted that **dynamic programming** is the kind of method that *can* find the true best — but it costs a lot more work. (The name "Bhuvan" scribbled near the hill drawing is hard to read; probably a person used in the story.)

**What happens in practice.** Finding the absolute smallest tree is known to be extremely hard (NP-hard), so real programs use the greedy method and then **prune** (trim) the tree. Newer research shows exact methods can win a few percent of accuracy, but only for small trees.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Picture (slide 12): "Football khelna hai ya nahi?"** Pehle weather dekho:
- **Cloudy** → khelo.
- **Rain** → khelo (jaisa slide par bana hai).
- **Sunny** → ek aur sawaal poocho, **temperature**: hot → mat khelo, mild → khelo, cold → khelo.

Tree mein sirf do sawaal wale boxes hain (Weather, Temp.). Cloudy aur Rain pehle hi tay hain, isliye sirf Sunny branch ko aur sawaal chahiye tha.

**Sir ne laal pen se teen badi baatein likhi.**

**① Sawaal kaise chunein? — "splitting criteria".** Do scores use karte hain: **entropy** aur **information gain** (agle topics mein samjhaye jayenge). Inhe aise samjho: "kaun sa sawaal sabse zyada confusion door karta hai?"

**② Kab rukein? — "tab tak split karo jab tak har group mein ek hi jawaab na ho".** Har group ke andar sawaal poochte raho jab tak group mein sabka jawaab ek jaisa na ho jaye (sab "khelo" ya sab "mat khelo"). Aise group ko **pure** kehte hain.

**③ Tree kaise banayein? — "greedy approach".** Har step par wahi sawaal chuno jo *abhi* sabse achha lag raha ho; aage ka mat socho, aur pichhla choice kabhi wapas mat badlo.

**Hill-climbing picture samjho.** Socho tum ghane kohre mein pahaadi par chadh rahe ho. Tumhara rule: hamesha upar ki taraf kadam rakho. Tum kisi pahaadi ki choti par pahunch jaoge — par ho sakta hai wo chhoti pahaadi ho (**local maximum**), jabki bahut unchi choti (**global maximum**) kahin aur hai aur tum use kabhi nahi dhundh paoge, kyunki wahan jaane ke liye pehle *neeche* utarna padta. Greedy bhi aisa hi hai: tez aur aam taur par achha, par sabse best tree miss kar sakta hai. Sir ne bataya ki **dynamic programming** wo tareeka hai jo asli best dhundh *sakta* hai — par usmein kaam bahut zyada lagta hai. (Pahaadi ke paas likha "Bhuvan" naam dhundhla hai; shayad kahani ka koi insaan.)

**Practice mein kya hota hai.** Sabse chhota tree dhundhna bahut mushkil problem hai (NP-hard), isliye real programs greedy method use karte hain aur phir tree ko **prune** (chhaant) dete hain. Naye research mein exact methods kuch percent zyada accuracy dete hain, par sirf chhote trees ke liye.
