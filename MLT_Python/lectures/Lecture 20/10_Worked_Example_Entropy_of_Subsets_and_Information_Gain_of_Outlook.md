# Topic 10: Worked Example — Entropy of Each Outlook Subset and Information Gain of Outlook

Source: Lecture 20, slides 19–20 (entropies of S_Sunny, S_Overcast, S_Rain; then Gain(S, Outlook)). All numbers re-computed independently; one rounding discrepancy flagged. Comparison with the other attributes is an extension beyond the slides.

---

## 1) Technical Explanation

**Slide 19 — split S by Outlook** (values Sunny, Overcast, Rain). Count Yes/No inside each subset from the table in [[09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set]]:

| Subset | Days | Count | Entropy calculation | Entropy |
|---|---|---|---|---|
| **S_Sunny** | D1, D2, D8, D9, D11 | **[2+, 3−]** | −(2/5)log₂(2/5) − (3/5)log₂(3/5) = 0.5288 + 0.4422 | **0.971** |
| **S_Overcast** | D3, D7, D12, D13 | **[4+, 0−]** | −(4/4)log₂(4/4) − (0/4)log₂(0/4) = 0 − 0 (using 0·log 0 = 0) | **0** |
| **S_Rain** | D4, D5, D6, D10, D14 | **[3+, 2−]** | −(3/5)log₂(3/5) − (2/5)log₂(2/5) = 0.4422 + 0.5288 | **0.971** |

Check: 5 + 4 + 5 = 14 ✔; Yes 2+4+3 = 9 ✔; No 3+0+2 = 5 ✔. Exact values: 0.97095 for the two mixed subsets; Overcast is **pure** (all Yes) so entropy 0 → it will become a leaf.

**Slide 20 — information gain** ([[07_Information_Gain_Choosing_the_Best_Attribute]]):

Gain(S, Outlook) = Entropy(S) − Σ_{v ∈ {Sunny, Overcast, Rain}} (|S_v|/|S|) · Entropy(S_v)

= Entropy(S) − (5/14)·Entropy(S_Sunny) − (4/14)·Entropy(S_Overcast) − (5/14)·Entropy(S_Rain)

= 0.94 − (5/14)(0.971) − (4/14)(0) − (5/14)(0.971)

- (5/14)(0.971) = 0.3468 (twice) → 0.6936
- 0.94 − 0.6936 = **0.2464** (slide's value: **0.2464**)

**⚠ Flag — rounding.** The slide's 0.2464 comes from using the *rounded* intermediate values 0.94 and 0.971. With full precision: 0.940286 − 2·(5/14)·0.970951 = **0.246750 ≈ 0.2467** (the textbook figure is 0.247). The difference (0.0003) is only rounding and changes nothing, but if you are asked for the answer to 3–4 decimals, compute with unrounded entropies. Note also the order of terms on the slide is Sunny, Overcast, Rain with weights 5/14, 4/14, 5/14 — matching the counts above.

**Interpretation.** Splitting by Outlook reduces the uncertainty from 0.94 bits to the weighted average 0.694 bits, i.e. gains **0.2467 bits**. The Overcast branch is already perfect, which is the main reason Outlook scores well.

**Extension — the other attributes (not on the slides; computed with the same method).**

| Attribute | Subsets [Yes, No] → entropy | Weighted entropy after split | Gain |
|---|---|---|---|
| **Outlook** | Sunny [2,3]→0.971; Overcast [4,0]→0; Rain [3,2]→0.971 | 0.6935 | **0.2467** |
| Temp | Hot [2,2]→1.0; Mild [4,2]→0.9183; Cool [3,1]→0.8113 | 0.9111 | 0.0292 |
| Humidity | High [3,4]→0.9852; Normal [6,1]→0.5917 | 0.7885 | 0.1518 |
| Wind | Weak [6,2]→0.8113; Strong [3,3]→1.0 | 0.8922 | 0.0481 |

**Outlook has the largest gain → it becomes the root of the tree**, exactly the ID3 step 3 ([[08_Steps_of_the_ID3_Algorithm]]). The slides end here; the rest of the tree (Overcast → Yes; Sunny → Humidity; Rain → Wind) is previewed in topic 08.

---

## 2) Simple English Explanation

**The question.** If our very first question is "What's the outlook?", how much tidier do the 14 days become?

**Step 1 — sort the 14 days into three piles by outlook.**
- **Sunny pile (5 days: D1, D2, D8, D9, D11):** 2 played, 3 didn't.
- **Overcast pile (4 days: D3, D7, D12, D13):** all 4 played.
- **Rain pile (5 days: D4, D5, D6, D10, D14):** 3 played, 2 didn't.
(5 + 4 + 5 = 14 ✔, and 2 + 4 + 3 = 9 played ✔)

**Step 2 — the mess score of each pile.**
- **Sunny:** shares are 2/5 = 0.4 and 3/5 = 0.6. Parts: 0.4 × 1.322 = 0.529 and 0.6 × 0.737 = 0.442. Add → **0.971**.
- **Overcast:** share of "played" is 4/4 = 1 and of "didn't" is 0. Nothing is mixed, so the score is **0**. (The "0 × log 0" part is counted as 0 by agreement.)
- **Rain:** shares are 3/5 = 0.6 and 2/5 = 0.4 — the same two numbers as Sunny, just swapped → **0.971**.

**Step 3 — average the three scores, giving bigger piles more say.** Each pile's weight is its size ÷ 14:
- Sunny: (5/14) × 0.971 = 0.357 × 0.971 = **0.347**
- Overcast: (4/14) × 0 = **0**
- Rain: (5/14) × 0.971 = **0.347**
- Total (the mess *after* asking about outlook) = **0.694**.

**Step 4 — gain = mess before − mess after.** Before we asked anything the mess was 0.94. After: 0.694. Gain = 0.94 − 0.694 = **0.2464** (the teacher's number on slide 20). With every number kept at full precision the answer is **0.2467** — only a rounding difference, nothing wrong. If an exam wants 4 decimals, use the unrounded entropies.

**What the gain means.** Asking about the outlook removes about a quarter of the confusion. A big reason is the Overcast pile: it is completely clean, so on overcast days we can already say "play" with certainty.

**Is Outlook the best first question? (extension — not on the slides.)** Same method for the other columns:
| Column | Mess after the split | Gain |
|---|---|---|
| **Outlook** | 0.694 | **0.2467** |
| Humidity | 0.789 | 0.1518 |
| Wind | 0.892 | 0.0481 |
| Temp | 0.911 | 0.0292 |

Outlook has the biggest gain, so ID3 picks it as the top question (the root). Lecture 21 does exactly this calculation for the other three columns.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal.** Agar hamara pehla sawaal "Outlook kya hai?" ho, to 14 din kitne zyada saaf-suthre ho jaate hain?

**Step 1 — 14 dino ko outlook ke hisaab se teen dheriyon mein baanto.**
- **Sunny dheri (5 din: D1, D2, D8, D9, D11):** 2 khele, 3 nahi.
- **Overcast dheri (4 din: D3, D7, D12, D13):** chaaron khele.
- **Rain dheri (5 din: D4, D5, D6, D10, D14):** 3 khele, 2 nahi.
(5 + 4 + 5 = 14 ✔, aur 2 + 4 + 3 = 9 khele ✔)

**Step 2 — har dheri ka mess score.**
- **Sunny:** hisse 2/5 = 0.4 aur 3/5 = 0.6. Parts: 0.4 × 1.322 = 0.529 aur 0.6 × 0.737 = 0.442. Jodo → **0.971**.
- **Overcast:** "khela" ka hissa 4/4 = 1 aur "nahi khela" ka 0. Kuch mixed hai hi nahi, isliye score **0**. ("0 × log 0" ko sahmati se 0 maana jata hai.)
- **Rain:** hisse 3/5 = 0.6 aur 2/5 = 0.4 — Sunny wale hi do numbers, bas ulte → **0.971**.

**Step 3 — teeno scores ka average, bade group ko zyada weight dekar.** Har dheri ka weight = uska size ÷ 14:
- Sunny: (5/14) × 0.971 = 0.357 × 0.971 = **0.347**
- Overcast: (4/14) × 0 = **0**
- Rain: (5/14) × 0.971 = **0.347**
- Total (outlook poochne ke *baad* ka mess) = **0.694**.

**Step 4 — gain = pehle ka mess − baad ka mess.** Kuch poochne se pehle mess 0.94 tha. Baad mein: 0.694. Gain = 0.94 − 0.694 = **0.2464** (slide 20 par sir ka number). Agar har number poori precision mein rakho to **0.2467** aata hai — sirf rounding ka fark, kuch galat nahi. Agar exam mein 4 decimal chahiye to unrounded entropy se hi nikalna.

**Gain ka matlab.** Outlook poochne se lagbhag ek-chauthai confusion hat jaata hai. Iski badi wajah Overcast dheri hai: wo bilkul saaf hai, isliye overcast dino mein hum pakke se keh sakte hain "khelo".

**Kya Outlook sabse best pehla sawaal hai? (extension — slides mein nahi.)** Baaki columns ke liye wahi tareeka:
| Column | Split ke baad mess | Gain |
|---|---|---|
| **Outlook** | 0.694 | **0.2467** |
| Humidity | 0.789 | 0.1518 |
| Wind | 0.892 | 0.0481 |
| Temp | 0.911 | 0.0292 |

Outlook ka gain sabse bada hai, isliye ID3 use sabse upar (root) rakhta hai. Lecture 21 mein sir baaki teen columns ke liye yahi calculation karte hain.
