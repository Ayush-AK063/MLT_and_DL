# Topic 6: Entropy — Measuring Disorder in a Dataset

Source: Lecture 20, slide 14 ("Entropy"). Enriched with web research (Shannon 1948, bits, coin examples) and independently verified numbers.

---

## 1) Technical Explanation

**Slide 14 — what it says.**
- ID3 uses a **measure of impurity** (the slide names entropy or Gini impurity) to compute the information gain of each attribute. **Entropy is a measure of disorder in a dataset.**
- **High entropy**: data points are *evenly distributed* across the categories (very mixed). **Low entropy**: data points are *concentrated* in one or a few categories (nearly pure).

**Formula (slide):**

H(S) = Σ − ( P_i · log₂ P_i )

where **P_i** = fraction of the sample in the node that belongs to class i, **S** = the current dataset, **i** ranges over the set of classes in S. Write it fully for two classes (Yes/No):

H(S) = − p₊ log₂ p₊ − p₋ log₂ p₋

**Conventions.** log₂ means answers are in **bits** (Shannon, *A Mathematical Theory of Communication*, 1948). By convention **0 · log₂ 0 = 0** (the limit as p → 0). Since 0 ≤ p ≤ 1, log₂ p ≤ 0, so the leading minus makes entropy ≥ 0.

**Range.**
- **Minimum 0**: all examples in one class (pure node).
- **Maximum for two classes = 1 bit**: a 50/50 split. For *k* equally likely classes the maximum is **log₂ k** (3 classes → 1.585, 4 classes → 2).

**Verified reference values (computed).**

| Class mix (Yes, No) | p₊ | Entropy (bits) |
|---|---|---|
| (7, 0) or (0, 7) | 1 or 0 | **0** |
| (9, 1) | 0.9 | 0.469 |
| (9, 5) — the PlayTennis dataset | 0.643 | **0.9403** |
| (3, 2) or (2, 3) | 0.6 / 0.4 | **0.9710** |
| (4, 2) | 0.667 | 0.9183 |
| (3, 1) | 0.75 | 0.8113 |
| (1, 1) | 0.5 | **1.0** |

**Intuition (research).** Entropy is the *average surprise*. A fair coin (50/50) is maximally unpredictable → 1 bit. A coin that lands heads 90% of the time is more predictable → 0.469 bits. In a decision tree we want leaves where the answer is nearly certain, i.e. **low entropy**.

**Worked calculation of H(S) = H(9 Yes, 5 No).**
- −(9/14) log₂(9/14) = −0.6429 × (−0.6374) = 0.4098
- −(5/14) log₂(5/14) = −0.3571 × (−1.4854) = 0.5305
- Sum = **0.9403 ≈ 0.94** (the value the instructor writes on slide 18, [[09_Worked_Example_PlayTennis_Dataset_and_Entropy_of_the_Whole_Set]]).

**Entropy vs. Gini (so the slide's "or Gini" makes sense).** Gini impurity = 1 − Σ P_i². For (9, 5): 1 − (0.643² + 0.357²) = **0.459**. Gini is used by **CART**, entropy by **ID3/C4.5** ([[05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea]]).

---

## 2) Simple English Explanation

**Entropy = "how mixed-up is this group?"** Picture baskets of fruit:
- A basket with **only apples** → perfectly tidy → entropy **0**.
- A basket with **half apples, half oranges** → as mixed as it can possibly be → entropy **1** (for two kinds of fruit).
- A basket with **9 apples and 1 orange** → almost tidy → entropy about **0.47**.
- With **more than two kinds** the maximum is bigger: 3 equally likely kinds → 1.58, 4 kinds → 2.

**The slide's formula in words.** For each kind of thing in the group, take its **share** (the fraction of the group), multiply that share by log base 2 of the share, add these up, and flip the sign: **H(S) = Σ − (share × log₂ share)**. Here S is the group we're looking at. (By agreement, an empty share counts as 0.) You don't have to love the formula — the idea is the scale: **tidy → 0, completely mixed → maximum**.

**Why the minus sign?** Shares are between 0 and 1, so their logs are negative; the minus sign turns the answer positive.

**Quick reference — yes/no groups**
| Group (Yes, No) | Entropy |
|---|---|
| (7, 0) — all the same | **0** |
| (9, 1) | 0.47 |
| (4, 2) | 0.92 |
| (3, 1) | 0.81 |
| (3, 2) | **0.971** |
| (9, 5) — our tennis table | **0.94** |
| (1, 1) — a perfect coin toss | **1.0** |

**Our tennis table, worked out.** 9 "Yes" and 5 "No" out of 14 days.
- Yes share 9/14 = 0.643 → 0.643 × 0.637 = 0.410
- No share 5/14 = 0.357 → 0.357 × 1.485 = 0.531
- Add: **0.94**. Very close to the maximum 1, so the table is very mixed.

**Why we care.** Building a tree means asking questions that make the groups *tidier* (entropy falling towards 0). Entropy is the thermometer for that.

**About the "or Gini" on the slide.** Gini impurity is a similar messiness score (for our table: 0.459). It belongs to the CART algorithm; ID3 uses entropy.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Entropy = "ye group kitna mixed-up hai?"** Fal ki tokriyon ki tasveer socho:
- **Sirf seb** wali tokri → bilkul saaf → entropy **0**.
- **Aadhe seb, aadhe santre** → jitna mixed ho sakta hai utna → entropy **1** (do tarah ke fal ke liye).
- **9 seb aur 1 santra** → lagbhag saaf → entropy lagbhag **0.47**.
- **Do se zyada tarah** ke fal ho to maximum bada hota hai: 3 barabar tarah → 1.58, 4 tarah → 2.

**Slide ka formula shabdon mein.** Group ki har cheez ka **hissa** (group ka fraction) lo, us hisse ko hisse ke log base 2 se guna karo, sab jodo aur sign ulta kar do: **H(S) = Σ − (hissa × log₂ hissa)**. Yahan S wo group hai jise dekh rahe hain. (Sahmati se khaali hissa 0 maana jata hai.) Formula ratna zaroori nahi — asli baat scale hai: **saaf → 0, poora mixed → maximum**.

**Minus sign kyun?** Hisse 0 aur 1 ke beech hote hain, isliye unka log negative aata hai; minus laga kar jawaab positive ho jata hai.

**Quick reference — yes/no groups**
| Group (Yes, No) | Entropy |
|---|---|
| (7, 0) — sab same | **0** |
| (9, 1) | 0.47 |
| (4, 2) | 0.92 |
| (3, 1) | 0.81 |
| (3, 2) | **0.971** |
| (9, 5) — hamari tennis table | **0.94** |
| (1, 1) — bilkul sikka-uchhalna | **1.0** |

**Hamari tennis table, hal karke.** 14 dino mein 9 "Yes" aur 5 "No".
- Yes ka hissa 9/14 = 0.643 → 0.643 × 0.637 = 0.410
- No ka hissa 5/14 = 0.357 → 0.357 × 1.485 = 0.531
- Jodo: **0.94**. Maximum 1 ke bahut paas, yaani table bahut mixed hai.

**Hume kyun parwah hai.** Tree banane ka matlab hai aise sawaal poochna jo groups ko *zyada saaf* karein (entropy 0 ki taraf girna). Entropy us ka thermometer hai.

**Slide par "ya Gini" ke baare mein.** Gini impurity bhi milta-julta ghalat-malat score hai (hamari table ke liye: 0.459). Wo CART algorithm ka hai; ID3 entropy use karta hai.
