# Topic 8: The Steps of the ID3 Algorithm

Source: Lecture 20, slide 16 ("Steps of ID3 Algorithm"). Enriched with a pseudocode expansion, stopping conditions and a preview of the full tree for the lecture's dataset (computed independently; not on the slides).

---

## 1) Technical Explanation

**The four steps (slide 16).**
1. **Determine the entropy of the overall dataset** using the class distribution.
2. **For each feature:** calculate the entropy for each of its categorical values, then assess the information gain for the feature.
3. **Choose the feature that gives the highest information gain.**
4. **Iteratively apply all the above steps** (on each resulting subset) to build the tree structure.

**Pseudocode (expanded).**

```
ID3(S, Attributes):
    create a node
    if all examples in S have the same class:      # pure
        return leaf(that class)
    if Attributes is empty:                         # nothing left to ask
        return leaf(majority class of S)
    for each attribute A in Attributes:
        compute IG(S, A) = H(S) − Σ_v (|S_v|/|S|)·H(S_v)
    A_best = attribute with the largest IG
    node.test = A_best
    for each value v of A_best:
        S_v = examples in S with A_best = v
        if S_v is empty: add leaf(majority class of S)
        else:            add branch v → ID3(S_v, Attributes − {A_best})
    return node
```

**Key points.**
- Each attribute is used **at most once along a path** (it is removed from the list after use) — because the subsets below already all share that attribute's value.
- Gains are **recomputed inside every subset**; the best attribute at the root need not be best lower down.
- Stopping rule: pure subset (slide 12's "keep on splitting until all data points belong to the same class", [[04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy]]), or no attributes left, or an empty subset.
- It is **greedy**: no backtracking, so the final tree is not guaranteed to be the smallest.

**Preview — where the lecture's example leads (computed here; slides stop at the Outlook gain).** For the 14-day PlayTennis table ([[09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set]]):

| Attribute | Information gain |
|---|---|
| **Outlook** | **0.2467** (highest → root) |
| Humidity | 0.1518 |
| Wind | 0.0481 |
| Temp | 0.0292 |

Outlook = Overcast is pure (4 Yes) → leaf **Yes**. Recursing on the two impure subsets (5 days each): Sunny → best attribute **Humidity** (gain 0.971, splits into pure subsets: High → No, Normal → Yes); Rain → best attribute **Wind** (gain 0.971: Weak → Yes, Strong → No). Resulting tree:

```
Outlook
├─ Sunny    → Humidity ─ High → No ; Normal → Yes
├─ Overcast → Yes
└─ Rain     → Wind     ─ Weak → Yes ; Strong → No
```

(Expect the next lecture to continue the instructor's own working; this preview is for orientation and was verified by direct computation.)

---

## 2) Simple English Explanation

**The four-step recipe for growing the tree (slide 16).**
1. **Measure the mess of the whole table.** (Entropy of everything — for our tennis table 0.94.)
2. **Test every column.** For each column (Outlook, Temp, Humidity, Wind): sort the days by that column's answers, measure the mess of each pile, and work out the gain.
3. **Pick the winner.** The column with the **biggest gain** becomes the next question in the tree.
4. **Repeat.** Inside each pile, do steps 1–3 again with the *remaining* columns, and keep going.

**When do we stop growing a branch?**
- When the pile is **pure** (everyone has the same answer) → write that answer and stop.
- When there are **no columns left** to ask about → write down the most common answer in the pile.
- When a pile turns out to be **empty** → use the most common answer from the parent group.

**Rules of the game.**
- Each column is used **at most once on any path** from top to bottom (after you've asked "Outlook?", everybody in a pile has the same outlook, so asking again is pointless).
- Gains are **recalculated inside every pile**. The best question at the top need not be the best question further down.
- It is **greedy**: it never goes back and changes an earlier choice, so it isn't guaranteed to find the smallest possible tree.

**Preview: where our tennis example ends up (not on the slides — we worked it out).**
- At the top, the gains are: **Outlook 0.2467** (winner), Humidity 0.1518, Wind 0.0481, Temp 0.0292.
- **Overcast** days are all "play" → pure → leaf **Yes**.
- For **Sunny** days the best next question is **Humidity** (high → no, normal → yes).
- For **Rain** days the best next question is **Wind** (weak → yes, strong → no).

That gives a tree with 3 questions and 5 answers, and **temperature isn't needed at all**. (The next lecture does exactly this calculation on its slides.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Tree ugaane ki chaar-step recipe (slide 16).**
1. **Poori table ka mess naapo.** (Sab ki entropy — hamari tennis table ke liye 0.94.)
2. **Har column test karo.** Har column (Outlook, Temp, Humidity, Wind) ke liye: dino ko us column ke jawaabon se baanto, har dheri ka mess naapo aur gain nikalo.
3. **Winner chuno.** Jis column ka **gain sabse bada** ho wo tree ka agla sawaal banta hai.
4. **Dohraao.** Har dheri ke andar *bache hue* columns ke saath step 1–3 phir se karo, aur chalte raho.

**Branch ugana kab band karein?**
- Jab dheri **pure** ho (sab ka jawaab same) → wo jawaab likho aur ruk jao.
- Jab poochne ke liye **koi column na bache** → dheri ka sabse common jawaab likh do.
- Jab dheri **khaali** nikle → parent group ka sabse common jawaab use karo.

**Khel ke niyam.**
- Har column upar se neeche ke kisi bhi raaste par **zyada se zyada ek baar** use hota hai ("Outlook?" poochne ke baad ek dheri ke sabka outlook same hai, dobara poochna bekaar).
- Gains **har dheri ke andar dobara** nikalte hain. Upar ka best sawaal neeche ka best ho, zaroori nahi.
- Ye **greedy** hai: pichhla choice kabhi wapas nahi badalta, isliye sabse chhota tree milna guaranteed nahi.

**Preview: hamara tennis example kahan khatam hota hai (slides mein nahi — humne nikaala).**
- Sabse upar gains: **Outlook 0.2467** (winner), Humidity 0.1518, Wind 0.0481, Temp 0.0292.
- **Overcast** din sab "khelo" → pure → leaf **Yes**.
- **Sunny** dino ke liye agla best sawaal **Humidity** (high → nahi, normal → haan).
- **Rain** dino ke liye agla best sawaal **Wind** (weak → haan, strong → nahi).

Natija: 3 sawaal aur 5 jawaab wala tree, aur **temperature ki zaroorat hi nahi**. (Agla lecture isi calculation ko slides par karta hai.)
