# Topic 2: Information Gain of the Attribute Humidity (High, Normal)

Source: Lecture 21, slide 7 ("Attribute: Humidity", handwritten). All numbers independently verified.

---

## 1) Technical Explanation

**Setup (slide 7).** Value(Humidity) = {High, Normal}; Entropy(S) = 0.94.

| Value | Days | Class counts | Entropy |
|---|---|---|---|
| **High** | D1, D2, D3, D4, D8, D12, D14 | [3+, 4−] | −(3/7)log₂(3/7) − (4/7)log₂(4/7) = 0.5239 + 0.4613 = **0.9852** |
| **Normal** | D5, D6, D7, D9, D10, D11, D13 | [6+, 1−] | −(6/7)log₂(6/7) − (1/7)log₂(1/7) = 0.1906 + 0.4011 = **0.5917** (slide writes 0.5916 — truncation) |

Check: 7 + 7 = 14 ✔; Yes 3 + 6 = 9 ✔; No 4 + 1 = 5 ✔.

**Gain:**

Gain(S, Humidity) = 0.94 − (7/14)(0.9852) − (7/14)(0.5916)
= 0.94 − 0.4926 − 0.2958 = **0.152** (slide: 0.152)

Exact: **0.1518**. (Slide 9 lists 0.1516 — again rounding of intermediates.)

**Reading the result.** Normal humidity is mostly "Yes" (6 of 7), so splitting on Humidity helps noticeably — about five times the gain of Temp — but High humidity is still mixed (3 vs 4). Humidity is a **decent** attribute, but weaker than Outlook ([[03_Gain_of_Wind_and_Choosing_Outlook_as_Root]]). Humidity will matter more later: inside the Sunny subset it becomes a perfect splitter ([[05_Sunny_Subset_Gains_and_Humidity_Split]]).

---

## 2) Simple English Explanation

**The question.** Same 14 days (9 played, 5 didn't, mess score 0.94). Now split them by **humidity** — either High or Normal. Does that tidy things up?

**Step 1 — two piles.**
- **High humidity pile:** 7 days → 3 played, 4 didn't.
- **Normal humidity pile:** 7 days → 6 played, 1 didn't.
(7 + 7 = 14 ✔)

**Step 2 — mess score of each pile.**
- **High:** 3 of 7 played (0.429) and 4 of 7 didn't (0.571). Parts: 0.429 × 1.222 = 0.524 and 0.571 × 0.807 = 0.461. Add → **0.985**. That is almost the worst possible (1.0) — the High pile is still nearly a coin-toss.
- **Normal:** 6 of 7 played (0.857) and 1 of 7 didn't (0.143). Parts: 0.857 × 0.222 = 0.191 and 0.143 × 2.807 = 0.401. Add → **0.592**. Much tidier — most Normal-humidity days were "play" days.

**Step 3 — weighted average.** Both piles have 7 of the 14 days, so each counts for half: 0.5 × 0.985 = 0.493 and 0.5 × 0.592 = 0.296 → total **0.789**.

**Step 4 — gain** = 0.94 − 0.789 = **0.152** (about 0.15).

**Meaning:** humidity removes about five times as much confusion as temperature did (0.15 vs 0.03). It is a decent question, but not the best — Outlook will beat it. Remember Humidity though; it comes back later as the perfect question for sunny days.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal.** Wahi 14 din (9 khele, 5 nahi, mess score 0.94). Ab inhe **humidity** se baanto — High ya Normal. Kya isse cheezein saaf hoti hain?

**Step 1 — do dheriyan.**
- **High humidity dheri:** 7 din → 3 khele, 4 nahi.
- **Normal humidity dheri:** 7 din → 6 khele, 1 nahi.
(7 + 7 = 14 ✔)

**Step 2 — har dheri ka mess score.**
- **High:** 7 mein se 3 khele (0.429) aur 4 nahi (0.571). Hisse: 0.429 × 1.222 = 0.524 aur 0.571 × 0.807 = 0.461. Jodo → **0.985**. Ye lagbhag sabse kharab (1.0) hai — High wali dheri abhi bhi sikka-uchhalne jaisi hai.
- **Normal:** 7 mein se 6 khele (0.857) aur 1 nahi (0.143). Hisse: 0.857 × 0.222 = 0.191 aur 0.143 × 2.807 = 0.401. Jodo → **0.592**. Kaafi saaf — Normal humidity wale zyada tar din "khelne" wale the.

**Step 3 — weighted average.** Dono dheriyon mein 14 mein se 7-7 din hain, isliye har ek ka aadha weight: 0.5 × 0.985 = 0.493 aur 0.5 × 0.592 = 0.296 → total **0.789**.

**Step 4 — gain** = 0.94 − 0.789 = **0.152** (lagbhag 0.15).

**Matlab:** humidity ne temperature se lagbhag paanch guna zyada confusion hataya (0.15 vs 0.03). Achha sawaal hai, par best nahi — Outlook isse jeet jayega. Humidity ko yaad rakhna; baad mein sunny dino ke liye ye perfect sawaal banega.
