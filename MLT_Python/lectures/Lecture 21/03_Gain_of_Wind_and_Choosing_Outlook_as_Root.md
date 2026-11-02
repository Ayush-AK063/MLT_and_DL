# Topic 3: Information Gain of Wind and Choosing Outlook as the Root

Source: Lecture 21, slides 8–9 ("Attribute: Wind" — the slide shows only the table, no working; then the four gains listed). The Wind working below is **computed by us** because the slide leaves it blank. Numbers independently verified.

---

## 1) Technical Explanation

**Slide 8 — Attribute: Wind.** Only the table and the title are shown; the instructor evidently worked it out verbally. Value(Wind) = {Weak, Strong}.

| Value | Days | Class counts | Entropy |
|---|---|---|---|
| **Weak** | D1, D3, D4, D5, D8, D9, D10, D13 | [6+, 2−] | −(6/8)log₂(6/8) − (2/8)log₂(2/8) = 0.3113 + 0.5 = **0.8113** |
| **Strong** | D2, D6, D7, D11, D12, D14 | [3+, 3−] | **1.0** |

Gain(S, Wind) = 0.94 − (8/14)(0.8113) − (6/14)(1.0) = 0.94 − 0.4636 − 0.4286 = **0.048** (exact **0.0481**), matching slide 9.

**Slide 9 — the four root candidates side by side (handwritten):**

| Attribute | Slide value | Exact value |
|---|---|---|
| **Outlook** (circled) | **0.2464** | 0.2467 |
| Temp | 0.0289 | 0.0292 |
| Humidity | 0.1516 | 0.1518 |
| Wind | 0.048 | 0.0481 |

The small gaps (≤ 0.0003) are only rounding of intermediate entropies; the ranking is unaffected.

**Decision (ID3 step 3, [[08_Steps_of_the_ID3_Algorithm]] from Lecture 20).** Outlook has the highest gain, so **Outlook becomes the root node**. The ranking is Outlook > Humidity > Wind > Temp.

**Why Outlook wins.** One of its three branches (Overcast) is already perfectly pure (4 Yes, 0 No) — a big drop in entropy for free. Wind's branches are both mixed, and Temp's are the most mixed of all.

**Colour-key on slide 9.** The ticks on the table (Hot, Mild, Cool) were left over from the Temp working; the purple circle marks the winning gain 0.2464.

---

## 2) Simple English Explanation

**Wind, step by step** (the slide itself shows only the table, so this working is ours).

**Step 1 — two piles by wind.**
- **Weak wind:** 8 days → 6 played, 2 didn't.
- **Strong wind:** 6 days → 3 played, 3 didn't.
(8 + 6 = 14 ✔)

**Step 2 — mess score of each pile.**
- **Weak:** 6 of 8 played = 0.75, 2 of 8 didn't = 0.25. Parts: 0.75 × 0.415 = 0.311 and 0.25 × 2 = 0.5 → **0.811**.
- **Strong:** exactly half and half → **1.0** (the worst possible).

**Step 3 — weighted average.** Weak: 8/14 = 0.571 × 0.811 = 0.463. Strong: 6/14 = 0.429 × 1.0 = 0.429. Total = **0.892**.

**Step 4 — gain** = 0.94 − 0.892 = **0.048**. Wind helps only a tiny bit.

**The final scoreboard for the very first question** (this is the whole point of the lecture so far):

| Question | Gain (how much confusion it removes) |
|---|---|
| **Outlook** | **0.25** 🏆 |
| Humidity | 0.15 |
| Wind | 0.05 |
| Temp | 0.03 |

**Why Outlook wins.** When we split by Outlook, one of its three piles (Overcast) came out perfectly tidy — all 4 days "played". That one clean pile is a huge help. None of the other questions produce a clean pile.

**Decision.** The biggest score wins, so the first question at the top of our tree is **"What is the Outlook?"** — this is called the **root**. (The tiny differences between the slide's numbers and the exact ones — e.g. 0.2464 vs 0.2467 — come only from rounding; the order of the four scores never changes.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Wind, step by step** (slide par sirf table hai, working nahi — ye working humne nikaali hai).

**Step 1 — wind se do dheriyan.**
- **Weak wind:** 8 din → 6 khele, 2 nahi.
- **Strong wind:** 6 din → 3 khele, 3 nahi.
(8 + 6 = 14 ✔)

**Step 2 — har dheri ka mess score.**
- **Weak:** 8 mein se 6 khele = 0.75, 2 nahi = 0.25. Hisse: 0.75 × 0.415 = 0.311 aur 0.25 × 2 = 0.5 → **0.811**.
- **Strong:** theek aadha-aadha → **1.0** (sabse kharab mix).

**Step 3 — weighted average.** Weak: 8/14 = 0.571 × 0.811 = 0.463. Strong: 6/14 = 0.429 × 1.0 = 0.429. Total = **0.892**.

**Step 4 — gain** = 0.94 − 0.892 = **0.048**. Wind sirf thoda hi madad karta hai.

**Pehle sawaal ka final scoreboard** (ab tak ke lecture ka poora nichod):

| Sawaal | Gain (kitna confusion hataya) |
|---|---|
| **Outlook** | **0.25** 🏆 |
| Humidity | 0.15 |
| Wind | 0.05 |
| Temp | 0.03 |

**Outlook kyun jeeta?** Outlook se baantne par uski teen dheriyon mein se ek (Overcast) bilkul saaf nikli — chaaron din "khela". Ek saaf dheri bahut bada fayda deti hai. Baaki kisi sawaal se koi saaf dheri nahi bani.

**Decision.** Jiska score sabse bada, wahi jeetta hai, isliye tree ke sabse upar pehla sawaal hoga **"Outlook kya hai?"** — ise **root** kehte hain. (Slide ke numbers aur exact numbers mein jo chhota fark hai — jaise 0.2464 vs 0.2467 — wo sirf rounding ki wajah se hai; chaaron scores ka order kabhi nahi badalta.)
