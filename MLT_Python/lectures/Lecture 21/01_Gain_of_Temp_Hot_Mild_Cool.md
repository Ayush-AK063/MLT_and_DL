# Topic 1: Information Gain of the Attribute Temp (Hot, Mild, Cool)

Source: Lecture 21, slide 6 ("Attribute: Temp", handwritten calculation). All numbers independently verified.

---

## 1) Technical Explanation

**Setup (slide 6).** Value(Temp) = {Hot, Mild, Cool}; S = [9+, 5−], Entropy(S) = 0.94. The instructor circles Hot, Mild and Cool cells in the table and counts Yes/No for each ([[09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set]] from Lecture 20 has the table).

| Value | Days | Class counts | Entropy calculation | Entropy |
|---|---|---|---|---|
| **Hot** | D1, D2, D3, D13 | [2+, 2−] | −(2/4)log₂(2/4) − (2/4)log₂(2/4) | **1.0** |
| **Cool** | D5, D6, D7, D9 | [3+, 1−] | −(3/4)log₂(3/4) − (1/4)log₂(1/4) = 0.3113 + 0.5 | **0.8113** |
| **Mild** | D4, D8, D10, D11, D12, D14 | [4+, 2−] | −(4/6)log₂(4/6) − (2/6)log₂(2/6) = 0.3900 + 0.5283 | **0.918** (exact 0.9183) |

Check: 4 + 4 + 6 = 14 ✔; Yes 2+3+4 = 9 ✔; No 2+1+2 = 5 ✔.

**Gain** ([[07_Information_Gain_Choosing_the_Best_Attribute]] from Lecture 20):

Gain(S, Temp) = 0.94 − (4/14)(1) − (6/14)(0.918) − (4/14)(0.8113)
= 0.94 − 0.2857 − 0.3934 − 0.2318 = **0.029** (slide: 0.029)

With unrounded values the answer is **0.0292**. (On slide 9 the instructor lists it as 0.0289 — a small rounding variation of the same quantity.)

**Reading the result.** Temp barely reduces the uncertainty (0.94 → 0.911 bits): every temperature group is still very mixed — Hot is a perfect 50/50. Temp is a **poor** attribute.

---

## 2) Simple English Explanation

**The question we are asking.** Before we ask anything, the 14 days are a jumble: 9 "played", 5 "didn't play", mess score **0.94**. If we sort the days by **temperature**, do the piles become tidier? Let's measure.

**Step 1 — make three piles.**
- **Hot pile:** 4 days. Result: 2 played, 2 didn't.
- **Cool pile:** 4 days. Result: 3 played, 1 didn't.
- **Mild pile:** 6 days. Result: 4 played, 2 didn't.
(4 + 4 + 6 = 14, so every day is in exactly one pile.)

**Step 2 — mess score of each pile** (entropy: 0 = perfectly tidy, 1 = a 50/50 mix).
- **Hot:** exactly half and half → the worst possible mix → **1.0**.
- **Cool:** 3 of 4 played. Part for "played": 0.75 × 0.415 = 0.311. Part for "didn't": 0.25 × 2 = 0.5. Add → **0.811**.
- **Mild:** 4 of 6 played. Part for "played": 0.667 × 0.585 = 0.390. Part for "didn't": 0.333 × 1.585 = 0.528. Add → **0.918**.

**Step 3 — average the three scores, giving bigger piles more say.** Weights are pile size ÷ 14: Hot 4/14 = 0.286, Cool 0.286, Mild 6/14 = 0.429.
- Hot: 0.286 × 1.0 = 0.286
- Cool: 0.286 × 0.811 = 0.232
- Mild: 0.429 × 0.918 = 0.394
- Total = **0.911**

**Step 4 — gain = mess before − mess after** = 0.94 − 0.911 = **0.029**.

**Meaning:** sorting by temperature only cleaned things up by 0.03 out of a possible 0.94. Hot days are a perfect coin-toss; the others are only slightly better. **Temperature is a very weak first question.** (If you use the unrounded 0.9403 instead of 0.94 you get 0.0292; the teacher's 0.029 on this slide and 0.0289 on a later slide are the same number with different rounding.)

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Sawaal:** abhi 14 din ek jumble hain: 9 din khela, 5 din nahi, mess score **0.94**. Agar dino ko **temperature** se alag-alag dheriyon mein baantein, to kya dheriyan saaf-suthri hoti hain? Chalo naapte hain.

**Step 1 — teen dheriyan banao.**
- **Hot dheri:** 4 din. Natija: 2 khele, 2 nahi.
- **Cool dheri:** 4 din. Natija: 3 khele, 1 nahi.
- **Mild dheri:** 6 din. Natija: 4 khele, 2 nahi.
(4 + 4 + 6 = 14, yaani har din bas ek hi dheri mein hai.)

**Step 2 — har dheri ka mess score** (entropy: 0 = bilkul saaf, 1 = 50/50 ka mix).
- **Hot:** theek aadha-aadha → sabse kharab mix → **1.0**.
- **Cool:** 4 mein se 3 khele. "Khela" ka hissa: 0.75 × 0.415 = 0.311. "Nahi khela" ka hissa: 0.25 × 2 = 0.5. Jodo → **0.811**.
- **Mild:** 6 mein se 4 khele. "Khela" ka hissa: 0.667 × 0.585 = 0.390. "Nahi khela" ka hissa: 0.333 × 1.585 = 0.528. Jodo → **0.918**.

**Step 3 — teeno scores ka average lo, bade group ko zyada weight dekar.** Weight = dheri ka size ÷ 14: Hot 4/14 = 0.286, Cool 0.286, Mild 6/14 = 0.429.
- Hot: 0.286 × 1.0 = 0.286
- Cool: 0.286 × 0.811 = 0.232
- Mild: 0.429 × 0.918 = 0.394
- Total = **0.911**

**Step 4 — gain = pehle ka mess − baad ka mess** = 0.94 − 0.911 = **0.029**.

**Matlab:** temperature se baantne par mess sirf 0.03 kam hua (0.94 mein se). Hot din bilkul "sikka uchhalne" jaise hain, baaki bhi thode hi behtar. **Temperature pehle sawaal ke liye bahut kamzor hai.** (Agar 0.94 ki jagah exact 0.9403 lo to 0.0292 aata hai; sir ka is slide par 0.029 aur baad wali slide par 0.0289 — dono wahi number hain, bas rounding alag.)
