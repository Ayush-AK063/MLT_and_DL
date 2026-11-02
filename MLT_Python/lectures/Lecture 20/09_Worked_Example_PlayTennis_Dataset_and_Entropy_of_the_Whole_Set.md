# Topic 9: Worked Example — The PlayTennis Dataset and the Entropy of the Whole Set

Source: Lecture 20, slides 17–18 ("Example: ID3 Algorithm" — 14-row table with handwritten Yes/No counts, then the entropy of S). All numbers independently verified.

---

## 1) Technical Explanation

**The dataset (slide 17).** 14 days, 4 categorical attributes, 1 target:

| Day | Outlook | Temp | Humidity | Wind | PlayTennis |
|---|---|---|---|---|---|
| D1 | Sunny | Hot | High | Weak | No |
| D2 | Sunny | Hot | High | Strong | No |
| D3 | Overcast | Hot | High | Weak | Yes |
| D4 | Rain | Mild | High | Weak | Yes |
| D5 | Rain | Cool | Normal | Weak | Yes |
| D6 | Rain | Cool | Normal | Strong | No |
| D7 | Overcast | Cool | Normal | Strong | Yes |
| D8 | Sunny | Mild | High | Weak | No |
| D9 | Sunny | Cool | Normal | Weak | Yes |
| D10 | Rain | Mild | Normal | Weak | Yes |
| D11 | Sunny | Mild | Normal | Strong | Yes |
| D12 | Overcast | Mild | High | Strong | Yes |
| D13 | Overcast | Hot | Normal | Weak | Yes |
| D14 | Rain | Mild | High | Strong | No |

(This is the classic table from Quinlan 1986 and Tom Mitchell's *Machine Learning* textbook.)

**Handwritten counts (slide 17).** Yes → **9**, No → **5**, Total → **14**. Verified by counting: Yes on D3, D4, D5, D7, D9, D10, D11, D12, D13 (9); No on D1, D2, D6, D8, D14 (5).

**Step 1 of ID3 ([[08_Steps_of_the_ID3_Algorithm]]): entropy of the whole set (slide 18).**

- Target attribute: PlayTennis. Attribute under study: **Outlook**, values(Outlook) = {Sunny, Overcast, Rain}.
- S = **[9+, 5−]**.

Entropy(S) = −(9/14) log₂(9/14) − (5/14) log₂(5/14)

- 9/14 = 0.642857; log₂ = −0.637430; term = 0.409776
- 5/14 = 0.357143; log₂ = −1.485427; term = 0.530505
- **Entropy(S) = 0.940286 ≈ 0.94** ✔ (slide: 0.94)

Because 0.94 is near the 2-class maximum (1.0), the dataset is quite mixed; no-one-question yet predicts well. The remaining steps measure how much each attribute reduces this 0.94 ([[10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook]]).

**Formula recap** ([[06_Entropy_Measuring_Disorder_in_a_Dataset]]): H(S) = Σ −P_i log₂ P_i with P_yes = 9/14, P_no = 5/14.

---

## 2) Simple English Explanation

**What the table is.** Each row is one day. For every day someone wrote down the weather (Outlook), how hot it was (Temp), how damp the air was (Humidity), how windy (Wind) — and the answer we care about: **did we play tennis that day?** The goal is to learn a set of questions that predicts the last column from the first four.

**Job 1 — count the answers.** Go down the PlayTennis column:
- "Yes" on D3, D4, D5, D7, D9, D10, D11, D12, D13 → **9 days**.
- "No" on D1, D2, D6, D8, D14 → **5 days**.
- 9 + 5 = **14** days in total. (The teacher wrote exactly this on slide 17: Yes → 9, No → 5, Total → 14.)

We write this as **S = [9+, 5−]** — "9 positives, 5 negatives".

**Job 2 — how mixed up is this? (entropy)**
Think of entropy as a "mess score": 0 means everything is the same answer, 1 means a perfect 50/50 mix (for yes/no problems).
1. Share of "Yes" days: 9 ÷ 14 = **0.643**. Share of "No" days: 5 ÷ 14 = **0.357**.
2. For each share, multiply the share by a special number (log base 2 of the share, made positive): 
   - Yes part: 0.643 × 0.637 = **0.410**
   - No part: 0.357 × 1.485 = **0.531**
3. Add the two parts: 0.410 + 0.531 = **0.94**.

**What 0.94 tells us.** It is very close to the maximum of 1. That means the table is almost a coin-toss: if you had to guess "play or not" with no extra information you would be wrong a lot. The rest of ID3 is a hunt for questions (Outlook? Wind? …) that push this number down towards 0.

**Why the teacher circled "Outlook" on slide 18.** He is about to test Outlook as the first question. Its possible answers are {Sunny, Overcast, Rain}. For that test we first need this starting mess score, 0.94, to compare against.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Table kya hai.** Har row ek din hai. Har din ke liye kisi ne likha: mausam (Outlook), kitni garmi (Temp), hawa mein kitni nami (Humidity), kitni hawa (Wind) — aur wo jawaab jo humein chahiye: **us din tennis khela ya nahi?** Goal hai aise sawaal seekhna jo pehle chaar columns se aakhri column ka jawaab bata sakein.

**Kaam 1 — jawaab gino.** PlayTennis column mein neeche jao:
- "Yes" D3, D4, D5, D7, D9, D10, D11, D12, D13 par → **9 din**.
- "No" D1, D2, D6, D8, D14 par → **5 din**.
- 9 + 5 = **14** din total. (Sir ne slide 17 par yahi likha: Yes → 9, No → 5, Total → 14.)

Ise hum likhte hain **S = [9+, 5−]** — "9 positive, 5 negative".

**Kaam 2 — ye kitna mixed hai? (entropy)**
Entropy ko "mess score" samjho: 0 matlab sab ka jawaab ek hi, 1 matlab perfect 50/50 mix (yes/no wale problems ke liye).
1. "Yes" din ka hissa: 9 ÷ 14 = **0.643**. "No" din ka hissa: 5 ÷ 14 = **0.357**.
2. Har hisse ko ek khaas number (hisse ka log base 2, positive bana kar) se guna karo:
   - Yes wala hissa: 0.643 × 0.637 = **0.410**
   - No wala hissa: 0.357 × 1.485 = **0.531**
3. Dono jodo: 0.410 + 0.531 = **0.94**.

**0.94 ka matlab.** Ye maximum 1 ke bahut paas hai. Yaani table lagbhag sikka-uchhalne jaisa hai: agar koi extra jaankari na ho aur "khelna hai ya nahi" guess karna pade to bahut baar galat honge. ID3 ka baaki kaam aise sawaal dhundhna hai (Outlook? Wind? …) jo is number ko 0 ki taraf neeche laayein.

**Sir ne slide 18 par "Outlook" ko circle kyun kiya.** Wo Outlook ko pehle sawaal ke roop mein test karne wale hain. Uske possible jawaab {Sunny, Overcast, Rain} hain. Is test ke liye pehle ye starting mess score 0.94 chahiye taaki compare kar sakein.
