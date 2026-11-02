# Topic 6: The Rain Subset and the Final Decision Tree

Source: Lecture 21, slide 15 (the finished tree, a clean printed version; its bottom edge is slightly cropped in the PDF). **The slides do not show any working for the Rain subset** — the gains below are computed by us and agree with the final tree on the slide. Numbers independently verified.

---

## 1) Technical Explanation

**The Rain subset (not worked on the slides).** S_rain = {D4, D5, D6, D10, D14} = **[3+, 2−]**, entropy **0.971**:

| Day | Temp | Humidity | Wind | PlayTennis |
|---|---|---|---|---|
| D4 | Mild | High | Weak | Yes |
| D5 | Cool | Normal | Weak | Yes |
| D6 | Cool | Normal | Strong | No |
| D10 | Mild | Normal | Weak | Yes |
| D14 | Mild | High | Strong | No |

| Attribute (inside Rain) | Subsets [Yes, No] → entropy | Gain |
|---|---|---|
| Temp | Cool [1,1] → 1.0; Mild [2,1] → 0.9183 | 0.971 − (2/5)(1.0) − (3/5)(0.9183) = **0.0200** |
| Humidity | High [1,1] → 1.0; Normal [2,1] → 0.9183 | **0.0200** |
| **Wind** | **Strong [0,2] → 0; Weak [3,0] → 0** | 0.971 − 0 − 0 = **0.971** |

**Wind** wins by a huge margin and produces two pure children:
- **Strong → No** ({D6, D14})
- **Weak → Yes** ({D4, D5, D10})

**The final tree (slide 15).**

```
Outlook                              {D1…D14} [9+,5−]
├─ Sunny    → Humidity
│              ├─ High   → No    {D1, D2, D8}
│              └─ Normal → Yes   {D9, D11}
├─ Overcast → Yes                 {D3, D7, D12, D13} [4+,0−]
└─ Rain     → Wind
               ├─ Strong → No    {D6, D14}
               └─ Weak   → Yes   {D4, D5, D10}
```

It has **3 decision nodes** (Outlook, Humidity, Wind), **5 leaves**, **depth 2**. Note that **Temp is never used** — it had the lowest gain at the root and never wins in a subset, so ID3 ignores it entirely.

**Verification on the training set.** Running all 14 days down the tree reproduces every label: **14/14 correct** (training accuracy 100%, as expected since the algorithm splits until pure).

**Rules read off the leaves.**
1. IF Outlook = Sunny AND Humidity = High THEN PlayTennis = **No**
2. IF Outlook = Sunny AND Humidity = Normal THEN **Yes**
3. IF Outlook = Overcast THEN **Yes**
4. IF Outlook = Rain AND Wind = Strong THEN **No**
5. IF Outlook = Rain AND Wind = Weak THEN **Yes**

**Predicting a new day (example).** Outlook = Sunny, Temp = Cool, Humidity = High, Wind = Strong → root says Sunny → test Humidity = High → **No**. Temp and Wind are never consulted.

**This tree = the textbook result** for this dataset (Quinlan 1986; Mitchell 1997).

---

## 2) Simple English Explanation

**The Rain box, step by step.** The slides skip this part, so the working is ours. The rainy days are D4, D5, D6, D10, D14 — 3 played, 2 didn't, mess score **0.971** (same as the sunny box). We try the three remaining questions on just these 5 days.

**Question 1 — Temperature?**
- **Cool:** D5 (yes), D6 (no) → 50/50 → score 1.0.
- **Mild:** D4 (yes), D10 (yes), D14 (no) → 2 yes, 1 no → score 0.918.
- Average mess = (2/5)×1.0 + (3/5)×0.918 = 0.4 + 0.551 = 0.951. Gain = 0.971 − 0.951 = **0.020** (useless).

**Question 2 — Humidity?**
- **High:** D4 (yes), D14 (no) → 50/50 → 1.0.
- **Normal:** D5 (yes), D6 (no), D10 (yes) → 2 yes, 1 no → 0.918.
- Same average as above → Gain = **0.020** (useless too).

**Question 3 — Wind?**
- **Strong:** D6 (no), D14 (no) → both "didn't play" → score 0.
- **Weak:** D4, D5, D10 → all three "played" → score 0.
- Average mess = 0, **both piles perfectly clean** → Gain = **0.971**. A clear winner.

**So on rainy days the tree asks about wind:** strong wind → **don't play**, weak wind → **play**.

**The whole finished tree, in plain words.**
1. Look at the **outlook**.
2. **Sunny →** look at **humidity**: high → no, normal → yes.
3. **Overcast →** always **yes**.
4. **Rain →** look at **wind**: strong → no, weak → yes.

**Facts about this tree.** It has 3 question boxes (Outlook, Humidity, Wind), 5 answer boxes, and it never asked about temperature at all. We checked it against all 14 days and it gets **every one right** (14 out of 14).

**Try it on a new day.** Outlook = Sunny, Temp = Cool, Humidity = High, Wind = Strong. Start at the top: Sunny → ask humidity → High → **No**. We never even looked at the temperature or the wind.

**About the slides.** Slide 14 just repeats the sunny numbers and slide 15 jumps straight to the finished tree, so the rain working above is ours (it matches the tree on slide 15). The bottom edge of slide 15 is slightly cut off in the PDF; the leaves are Strong → No (D6, D14) and Weak → Yes (D4, D5, D10).

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Rain wala dibba, step by step.** Slides ye hissa skip kar deti hain, isliye ye working humari hai. Barish ke din D4, D5, D6, D10, D14 hain — 3 khele, 2 nahi, mess score **0.971** (sunny dibbe jaisa hi). Ab bache hue teeno sawaal sirf in 5 dino par try karte hain.

**Sawaal 1 — Temperature?**
- **Cool:** D5 (haan), D6 (nahi) → 50/50 → score 1.0.
- **Mild:** D4 (haan), D10 (haan), D14 (nahi) → 2 haan, 1 nahi → score 0.918.
- Average mess = (2/5)×1.0 + (3/5)×0.918 = 0.4 + 0.551 = 0.951. Gain = 0.971 − 0.951 = **0.020** (bekaar).

**Sawaal 2 — Humidity?**
- **High:** D4 (haan), D14 (nahi) → 50/50 → 1.0.
- **Normal:** D5 (haan), D6 (nahi), D10 (haan) → 2 haan, 1 nahi → 0.918.
- Average wahi upar wala → Gain = **0.020** (ye bhi bekaar).

**Sawaal 3 — Wind?**
- **Strong:** D6 (nahi), D14 (nahi) → dono "nahi khela" → score 0.
- **Weak:** D4, D5, D10 → teeno "khela" → score 0.
- Average mess = 0, **dono dheriyan bilkul saaf** → Gain = **0.971**. Saaf winner.

**To barish ke dino mein tree wind poochta hai:** tez hawa → **mat khelo**, halki hawa → **khelo**.

**Poora finished tree, simple shabdon mein.**
1. Pehle **outlook** dekho.
2. **Sunny →** **humidity** dekho: high → nahi, normal → haan.
3. **Overcast →** hamesha **haan**.
4. **Rain →** **wind** dekho: strong → nahi, weak → haan.

**Is tree ke baare mein.** Isme 3 sawaal wale boxes (Outlook, Humidity, Wind) aur 5 jawaab wale boxes hain, aur temperature kabhi poocha hi nahi gaya. Humne ise saare 14 dino par check kiya aur ye **har ek sahi** pehchanta hai (14 mein se 14).

**Naye din par try karo.** Outlook = Sunny, Temp = Cool, Humidity = High, Wind = Strong. Upar se shuru: Sunny → humidity poocho → High → **No**. Temperature ya wind ko dekhne ki zaroorat hi nahi padi.

**Slides ke baare mein.** Slide 14 sirf sunny wale numbers dobara dikhati hai aur slide 15 seedha finished tree hai, isliye upar ki rain working humari hai (ye slide 15 ke tree se match karti hai). Slide 15 ka neeche ka hissa PDF mein thoda kata hua hai; leaves hain Strong → No (D6, D14) aur Weak → Yes (D4, D5, D10).
