# Topic 4: Splitting on Outlook — The First Level of the Tree

Source: Lecture 21, slide 10 (hand-drawn tree with the Outlook root, branches Sunny / Overcast / Rain, and the day-sets under each).

---

## 1) Technical Explanation

**What the slide draws.** Root node **Outlook** holding the whole dataset **{D1, D2, …, D14}, [9+, 5−]**, with three branches:

| Branch | Days in the subset | Class counts | Status |
|---|---|---|---|
| **Sunny** | {D1, D2, D8, D9, D11} | [2+, 3−] | impure → "?" (needs another split) |
| **Overcast** | {D3, D7, D12, D13} | [4+, 0−] | pure → leaf **Yes** |
| **Rain** | {D4, D5, D6, D10, D14} | [3+, 2−] | impure → "?" (needs another split) |

**How the subsets are formed.** "Splitting" ([[02_Tree_Structure_Terminology_and_Where_Trees_Are_Used]] from Lecture 20) sends every row down the branch matching its Outlook value; the subset sizes 5 + 4 + 5 = 14 add back to the whole set, and the Yes/No counts add back to [9+, 5−].

**Applying the stopping rule** ([[04_Play_Football_Tree_and_the_Three_Key_Ideas_Splitting_Stopping_Greedy]] from Lecture 20: "keep on splitting until all data points belong to the same class"):
- Overcast is **pure** (entropy 0) → stop; the leaf predicts **Yes**.
- Sunny and Rain are impure (entropy 0.971 each) → recurse: run ID3 again on each subset, **using only the remaining attributes {Temp, Humidity, Wind}** — Outlook is not reused on a path because it is constant inside each subset.

The "?" boxes on the slide are exactly these two unfinished nodes; the next topics fill them ([[05_Sunny_Subset_Gains_and_Humidity_Split]] and [[06_Rain_Subset_and_the_Final_Decision_Tree]]).

**Important:** the best attribute can differ per subset — the gains must be **recomputed on each subset**, not reused from the root.

---

## 2) Simple English Explanation

**Where we are.** The scoreboard said Outlook is the best first question, so the top of our tree is "What is the Outlook?" Now we actually *use* that question: every one of the 14 days walks down the arrow that matches its outlook. The teacher draws this on slide 10, writing the list of day numbers next to each box.

**The three boxes after the split.**
- **Sunny box — 5 days (D1, D2, D8, D9, D11).** 2 played, 3 didn't. Still a mix, so the teacher draws a "?" — we need another question here.
- **Overcast box — 4 days (D3, D7, D12, D13).** All 4 played. This one is **perfectly clean**, so we're done: write **"Yes"**.
- **Rain box — 5 days (D4, D5, D6, D10, D14).** 3 played, 2 didn't. Still a mix, so another "?".

**A good habit: check your counts.** 5 + 4 + 5 = 14 days (nobody lost or doubled), and 2 + 4 + 3 = 9 "played", 3 + 0 + 2 = 5 "didn't" (matches the starting [9+, 5−]).

**What do the two "?" boxes mean?** They are the unfinished parts of the tree. For each one we repeat the same game — measure the mess, test the columns, pick the best — but with two differences:
1. We only use the days in that box (5 days each).
2. We can only use the columns not yet used on that path: **Temp, Humidity, Wind**. We don't ask "Outlook?" again, because everybody in a box already has the same outlook.

**One more important point.** The scores must be **recomputed inside each box**. The scoreboard from the top (Outlook best, then Humidity, Wind, Temp) was for all 14 days. Inside the sunny box the order will turn out to be different.

**Rule of thumb for stopping:** a box that is pure (all the same answer) becomes a leaf; a box that is still mixed gets another question.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Hum kahan hain.** Scoreboard ne bataya ki Outlook sabse achha pehla sawaal hai, isliye tree ke sabse upar "Outlook kya hai?" hai. Ab hum us sawaal ko *use* karte hain: 14 mein se har din apne outlook wale teer par neeche jata hai. Sir ye slide 10 par banate hain aur har box ke paas day numbers ki list likhte hain.

**Split ke baad teen box.**
- **Sunny box — 5 din (D1, D2, D8, D9, D11).** 2 khele, 3 nahi. Abhi bhi mix hai, isliye sir "?" banate hain — yahan aur sawaal chahiye.
- **Overcast box — 4 din (D3, D7, D12, D13).** Chaaron khele. Ye **bilkul saaf** hai, isliye kaam khatam: **"Yes"** likh do.
- **Rain box — 5 din (D4, D5, D6, D10, D14).** 3 khele, 2 nahi. Abhi mix hai, isliye ek aur "?".

**Achhi aadat: apni ginti check karo.** 5 + 4 + 5 = 14 din (koi gum ya double nahi hua), aur 2 + 4 + 3 = 9 "khela", 3 + 0 + 2 = 5 "nahi khela" (shuruaati [9+, 5−] se match).

**Do "?" boxes ka matlab kya hai?** Ye tree ke adhoore hisse hain. Har ek ke liye wahi khel dobara — mess naapo, columns test karo, best chuno — par do farak ke saath:
1. Sirf us box ke din use karte hain (har box mein 5 din).
2. Sirf wahi columns use kar sakte hain jo is raaste par abhi use nahi hue: **Temp, Humidity, Wind**. "Outlook?" dobara nahi poochte, kyunki box ke sabhi dino ka outlook pehle se same hai.

**Ek aur zaroori baat.** Scores **har box ke andar dobara** nikalne padte hain. Upar wala scoreboard (Outlook best, phir Humidity, Wind, Temp) saare 14 dino ke liye tha. Sunny box ke andar order alag nikalega.

**Rukne ka rule:** jo box pure hai (sab ka jawaab same) wo leaf ban jata hai; jo abhi mixed hai usse aur sawaal milta hai.
