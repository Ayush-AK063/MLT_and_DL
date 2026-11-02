# Topic 5: The Sunny Subset — Gains of Temp, Humidity, Wind and the Humidity Split

Source: Lecture 21, slides 11–14 (slide 11: S_sunny table with handwritten entropies; slide 12: typed version of the three gains; slide 13: tree with Humidity under Sunny and Rain still "?"; slide 14: the typed gains repeated, identical to slide 12). Numbers independently verified.

---

## 1) Technical Explanation

**The Sunny subset (slide 11).** S_sunny = **[2+, 3−]**, entropy **0.971**:

| Day | Temp | Humidity | Wind | PlayTennis |
|---|---|---|---|---|
| D1 | Hot | High | Weak | No |
| D2 | Hot | High | Strong | No |
| D8 | Mild | High | Weak | No |
| D9 | Cool | Normal | Weak | Yes |
| D11 | Mild | Normal | Strong | Yes |

(Outlook is dropped — constant inside this subset.)

**Gain(S_sunny, Temp).** Entropies on slide 11: S_hot = [0+, 2−] = **0.0** (the instructor first wrote 0.97 and corrected it to 0.0), S_cool = [1+, 0−] = **0.0**, S_mild = [1+, 1−] = **1.0**.
Gain = 0.971 − (2/5)(0) − (1/5)(0) − (2/5)(1.0) = 0.971 − 0.4 = **0.571** (slide: **0.570**, from the rounded 0.97 − 0.4).

**Gain(S_sunny, Humidity).** High → {D1, D2, D8} = [0+, 3−] → entropy 0; Normal → {D9, D11} = [2+, 0−] → entropy 0.
Gain = 0.971 − (3/5)(0) − (2/5)(0) = **0.971** (slide: **0.97**). **Both children are perfectly pure** — this is the maximum possible gain here, equal to the entropy of S_sunny itself.

**Gain(S_sunny, Wind).** Weak → {D1, D8, D9} = [1+, 2−] → 0.9183; Strong → {D2, D11} = [1+, 1−] → 1.0.
Gain = 0.971 − (3/5)(0.9183) − (2/5)(1.0) = 0.971 − 0.5510 − 0.4 = **0.0200** (slide: **0.0192**, from rounding 0.97 − 0.951). Tiny either way.

| Attribute (inside Sunny) | Slide | Exact |
|---|---|---|
| Temp | 0.570 | 0.571 |
| **Humidity** | **0.97** | **0.971** |
| Wind | 0.0192 | 0.0200 |

**Decision.** Humidity has by far the highest gain → the Sunny branch splits on **Humidity** (slide 13):
- **High → No** ({D1, D2, D8}) — leaf
- **Normal → Yes** ({D9, D11}) — leaf

Both subsets are pure, so this branch is finished. The tree so far: Outlook → Sunny → Humidity (High → No, Normal → Yes); Overcast → Yes; Rain → "?". Slide 13 shows exactly this, with the Rain box still unfinished.

**Note.** Humidity ranked second at the root (0.1518) and wins inside Sunny — the best attribute truly depends on the subset ([[04_Splitting_on_Outlook_First_Level_of_the_Tree]]).

---

## 2) Simple English Explanation

**Where we are.** We asked "What's the Outlook?" first. Now we look only at the **sunny days** — 5 of them: D1, D2, D8, D9, D11. Two played, three didn't, so this little group is still mixed. Its mess score is: 2/5 = 0.4 → 0.4 × 1.322 = 0.529; 3/5 = 0.6 → 0.6 × 0.737 = 0.442; total **0.971**. We now repeat the whole game on just these 5 days, using only the columns we haven't used yet: Temp, Humidity, Wind.

**Question 1 — Temperature?**
- **Hot:** D1 and D2 → both "didn't play" → perfectly tidy → score 0.
- **Cool:** only D9 → "played" → tidy → score 0.
- **Mild:** D8 ("didn't") and D11 ("played") → a 50/50 mix → score 1.0.
- Weights: Hot 2/5, Cool 1/5, Mild 2/5. Average mess = (2/5)×0 + (1/5)×0 + (2/5)×1.0 = **0.4**.
- Gain = 0.971 − 0.4 = **0.571**. Pretty good.

**Question 2 — Humidity?**
- **High:** D1, D2, D8 → all three "didn't play" → score 0.
- **Normal:** D9, D11 → both "played" → score 0.
- Average mess = 0. **Both piles are perfectly clean!** Gain = 0.971 − 0 = **0.971** — you can't do better than that.

**Question 3 — Wind?**
- **Weak:** D1 (no), D8 (no), D9 (yes) → 1 yes, 2 no → score 0.918.
- **Strong:** D2 (no), D11 (yes) → 50/50 → score 1.0.
- Average mess = (3/5)×0.918 + (2/5)×1.0 = 0.551 + 0.4 = 0.951. Gain = 0.971 − 0.951 = **0.020** (almost nothing).

**Winner: Humidity.** So on sunny days the tree asks about humidity: **High → don't play** (D1, D2, D8), **Normal → play** (D9, D11). Both leaves are pure, so the sunny branch is finished.

**Three small things to know.** (1) The teacher's slide shows 0.570, 0.97 and 0.0192; the exact values are 0.571, 0.971 and 0.020 — only rounding. (2) On slide 11 he first wrote 0.97 for the Hot pile and then crossed it out and wrote 0, because both Hot days are "No". (3) Humidity was only *second best* at the very top (0.15) but is the *best* inside sunny days — the best question depends on which group you're looking at.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Hum kahan hain.** Humne pehle poocha "Outlook kya hai?" Ab sirf **sunny din** dekhte hain — 5 din: D1, D2, D8, D9, D11. 2 din khela, 3 din nahi, yaani ye chhota group abhi bhi mixed hai. Iska mess score: 2/5 = 0.4 → 0.4 × 1.322 = 0.529; 3/5 = 0.6 → 0.6 × 0.737 = 0.442; total **0.971**. Ab poora khel sirf in 5 dino par dobara khelte hain, aur sirf wahi columns use karte hain jo abhi tak nahi use hue: Temp, Humidity, Wind.

**Sawaal 1 — Temperature?**
- **Hot:** D1 aur D2 → dono "nahi khela" → bilkul saaf → score 0.
- **Cool:** sirf D9 → "khela" → saaf → score 0.
- **Mild:** D8 ("nahi") aur D11 ("haan") → 50/50 mix → score 1.0.
- Weight: Hot 2/5, Cool 1/5, Mild 2/5. Average mess = (2/5)×0 + (1/5)×0 + (2/5)×1.0 = **0.4**.
- Gain = 0.971 − 0.4 = **0.571**. Kaafi achha.

**Sawaal 2 — Humidity?**
- **High:** D1, D2, D8 → teeno "nahi khela" → score 0.
- **Normal:** D9, D11 → dono "khela" → score 0.
- Average mess = 0. **Dono dheriyan bilkul saaf!** Gain = 0.971 − 0 = **0.971** — isse behtar ho hi nahi sakta.

**Sawaal 3 — Wind?**
- **Weak:** D1 (nahi), D8 (nahi), D9 (haan) → 1 haan, 2 nahi → score 0.918.
- **Strong:** D2 (nahi), D11 (haan) → 50/50 → score 1.0.
- Average mess = (3/5)×0.918 + (2/5)×1.0 = 0.551 + 0.4 = 0.951. Gain = 0.971 − 0.951 = **0.020** (lagbhag kuch nahi).

**Winner: Humidity.** To sunny dino mein tree humidity poochta hai: **High → mat khelo** (D1, D2, D8), **Normal → khelo** (D9, D11). Dono leaves pure hain, isliye sunny wali branch poori ho gayi.

**Teen chhoti baatein.** (1) Slide par 0.570, 0.97 aur 0.0192 hai; exact values 0.571, 0.971 aur 0.020 hain — sirf rounding ka fark. (2) Slide 11 par sir ne Hot ke liye pehle 0.97 likha phir kaat kar 0 kiya, kyunki Hot ke dono din "No" hain. (3) Humidity sabse upar (root par) sirf *doosre number* par thi (0.15), par sunny dino ke andar wo *sabse best* hai — best sawaal is par depend karta hai ki tum kaun sa group dekh rahe ho.
