# Topic 4: Worked Example 1 — Building a ROC Curve from Ranked Probabilities

Source: Lecture 19, slides 12–13 ("Example": the 10-tuple table with Class, Prob, TP, FP, TPR, FPR columns, the instructor's handwritten (FPR, TPR) points and threshold notes, and the ROC plot with the "convex hull" and "Random guessing" lines). Independently re-verified; **AUC = 0.76** is computed here (the slide shades the area but doesn't state the number).

---

## 1) Technical Explanation

**The data (slide 12).** Ten test tuples, already **sorted by predicted probability** (of the positive class P), with their true class:

| Tuple | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Class | P | P | N | P | P | N | N | N | P | N |
| Prob | 0.90 | 0.80 | 0.70 | 0.60 | 0.55 | 0.54 | 0.53 | 0.51 | 0.50 | 0.40 |

There are **P = 5** positives and **N = 5** negatives. Formulas on the slide: **TPR = TP/P**, **FPR = FP/N** (TP, FP are *running totals*).

**The procedure (slide + instructor's notes).** For each row, *set the threshold equal to that row's probability* — "predict positive if prob ≥ threshold" — and count the positives (TP) and negatives (FP) at or above it. The instructor demonstrates:
- **Threshold ≥ 0.90 → positive:** only tuple 1 is predicted positive; it is really P → TP = 1, FP = 0 → **TPR = 1/5 = 0.2, FPR = 0/5 = 0** → point **(0, 0.2)**.
- **Threshold ≥ 0.80:** tuples 1–2 → TP = 2, FP = 0 → **TPR = 2/5 = 0.4**, FPR = 0 → **(0, 0.4)**.
- **Threshold ≥ 0.70:** tuples 1–3; tuple 3 is N → TP = 2, **FP = 1** → TPR = 0.4, **FPR = 1/5 = 0.2** → **(0.2, 0.4)**.

**Complete table (verified against the slide).**

| Tuple | Class | Prob | TP | FP | TPR | FPR | ROC point (FPR, TPR) |
|---|---|---|---|---|---|---|---|
| 1 | P | 0.90 | 1 | 0 | 0.2 | 0 | (0, 0.2) |
| 2 | P | 0.80 | 2 | 0 | 0.4 | 0 | (0, 0.4) |
| 3 | N | 0.70 | 2 | 1 | 0.4 | 0.2 | (0.2, 0.4) |
| 4 | P | 0.60 | 3 | 1 | 0.6 | 0.2 | (0.2, 0.6) |
| 5 | P | 0.55 | 4 | 1 | 0.8 | 0.2 | (0.2, 0.8) |
| 6 | N | 0.54 | 4 | 2 | 0.8 | 0.4 | (0.4, 0.8) |
| 7 | N | 0.53 | 4 | 3 | 0.8 | 0.6 | (0.6, 0.8) |
| 8 | N | 0.51 | 4 | 4 | 0.8 | 0.8 | (0.8, 0.8) |
| 9 | P | 0.50 | 5 | 4 | 1.0 | 0.8 | (0.8, 1.0) |
| 10 | N | 0.40 | 5 | 5 | 1.0 | 1.0 | (1.0, 1.0) |

Plus the starting point (0, 0) (threshold above every score). All values match the slide. Note the pattern from [[01_What_Is_a_ROC_Curve_and_Ranking_Instead_of_Classifying]]: a **P** row moves the curve **up** by 1/5 = 0.2; an **N** row moves it **right** by 0.2.

**Plotting (slide 13).** *ROC curve: FPR on x, TPR on y* (instructor's note). The dashed **step-wise ROC** passes (0,0) → (0,0.4) → (0.2,0.4) → (0.2,0.8) → (0.8,0.8) → (0.8,1.0) → (1,1). The straight solid line is **random guessing** (the diagonal). The slide also draws a **convex hull** (the outer solid line (0,0.4) → (0.2,0.8) → (0.8,1.0) → (1,1) — the smallest convex shape enclosing the step curve); the hull represents the best performance reachable by *mixing* two thresholds (research: ROC convex hull, Provost & Fawcett).

**AUC (the instructor shades the area under the step curve).** Using the trapezoid rule from [[02_ROC_Shapes_AUC_and_Comparing_Models]], only horizontal moves add area (vertical moves have width 0):

| Horizontal move | Width | Height (TPR) | Area |
|---|---|---|---|
| FPR 0 → 0.2 (at TPR 0.4) | 0.2 | 0.4 | 0.08 |
| FPR 0.2 → 0.4 (at TPR 0.8) | 0.2 | 0.8 | 0.16 |
| FPR 0.4 → 0.6 (at TPR 0.8) | 0.2 | 0.8 | 0.16 |
| FPR 0.6 → 0.8 (at TPR 0.8) | 0.2 | 0.8 | 0.16 |
| FPR 0.8 → 1.0 (at TPR 1.0) | 0.2 | 1.0 | 0.20 |
| **Total AUC** | | | **0.76** |

**Pair-counting check (AUC = P(random positive scored above random negative)).** Positives {0.90, 0.80, 0.60, 0.55, 0.50} vs. negatives {0.70, 0.54, 0.53, 0.51, 0.40}: each positive beats this many negatives — 0.90: 5, 0.80: 5, 0.60: 4, 0.55: 4, 0.50: 1 (only 0.40) → 5 + 5 + 4 + 4 + 1 = **19 of 25 pairs = 0.76** ✓.

**Choosing a threshold from the curve (research, our extension).** Youden's J = TPR − FPR is largest at threshold **≥ 0.55** (TPR 0.8, FPR 0.2, J = 0.6) — the point farthest above the diagonal; at that cut-off precision = 4/5 = 0.80 and recall = 0.80. Compare ≥ 0.50: TPR 1.0 but FPR 0.8.

---

## 2) Simple English Explanation

**The setup:** a model gave 10 people a "probability of being positive." We lined them up from highest to lowest and know the truth: 5 are really P (positive) and 5 are really N (negative).

**How to draw the ROC curve:** start at the bottom-left corner. Walk down the list one person at a time:
- If the person is really **P** → move **up** one step (each step = 1/5 = 0.2).
- If the person is really **N** → move **right** one step (also 0.2).

Walking down the list: P P N P P N N N P N →
up, up, right, up, up, right, right, right, up, right.

That produces the points in the table: (0,0.2), (0,0.4), (0.2,0.4), (0.2,0.6), (0.2,0.8), (0.4,0.8), (0.6,0.8), (0.8,0.8), (0.8,1.0), (1,1).

**What does each point mean?** Say the teacher uses a cut-off of 0.70 — "everyone with a score of 0.70 or more is called positive." That's tuples 1, 2, 3: 2 real positives (TPR = 2/5 = 0.4) and 1 real negative wrongly included (FPR = 1/5 = 0.2). So the point is (0.2, 0.4).

**The area under this staircase** is the AUC. Add up the areas of the strips: 0.08 + 0.16 + 0.16 + 0.16 + 0.20 = **0.76**. Another way to see it: out of 25 (positive, negative) pairs, in 19 the positive got the higher score → 19/25 = 0.76.

**Is 0.76 good?** Decent (better than guessing at 0.5, far from perfect 1.0).

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Setup:** ek model ne 10 logon ko "positive hone ki probability" di. Humne unhe highest se lowest tak line mein lagaya aur asli answer pata hai: 5 sach mein **P** (positive) hain aur 5 sach mein **N** (negative).

**ROC curve kaise banate hain:** bottom-left corner se shuru karo. List mein ek-ek karke neeche chalo:
- Agar banda asli mein **P** hai → **upar** ek step (1/5 = 0.2).
- Agar banda asli mein **N** hai → **daayein** ek step (0.2).

List: P P N P P N N N P N → up, up, right, up, up, right, right, right, up, right.

Isse table ke saare points bante hain: (0,0.2), (0,0.4), (0.2,0.4), (0.2,0.6), (0.2,0.8), (0.4,0.8), (0.6,0.8), (0.8,0.8), (0.8,1.0), (1,1).

**Har point ka matlab:** maan lo cut-off **0.70** hai — "0.70 ya usse zyada score wale sab positive." Ye tuples 1, 2, 3 hain: 2 asli positive (TPR = 2/5 = 0.4) aur 1 asli negative galti se shamil (FPR = 1/5 = 0.2). To point = (0.2, 0.4). Sir ne board par yahi likha: "Threshold ≥ 0.90 → positive, TPR = 1/5 = 0.2, FPR = 0/5 = 0", phir "≥ 0.70: TPR = 2/5 = 0.4, FPR = 1/5 = 0.2".

**Is staircase ke neeche ka area = AUC.** Strips jodo: 0.08 + 0.16 + 0.16 + 0.16 + 0.20 = **0.76**. Doosra tareeka: 25 (positive, negative) pairs mein se 19 mein positive ko zyada score mila → 19/25 = 0.76 ✅.

**Convex hull:** slide mein ek bahar wali seedhi-line wali boundary bhi hai (convex hull) — ye do thresholds ko mix karke milne wali best possible performance dikhati hai.

**0.76 accha hai?** Theek-thaak (0.5 guessing se behtar, 1.0 perfect se door). Best cut-off dhoondhna ho to Youden's J = TPR − FPR sabse bada **≥ 0.55** par hota hai (TPR 0.8, FPR 0.2).
