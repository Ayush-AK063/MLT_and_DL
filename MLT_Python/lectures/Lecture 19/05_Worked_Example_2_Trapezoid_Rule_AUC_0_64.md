# Topic 5: Worked Example 2 — Computing AUC by the Trapezoid Rule (AUC = 0.64)

Source: Lecture 19, slides 14–15 ("Example 2": a second 10-tuple table, the instructor's hand-computation of the area using Area = (x₂ − x₁)(y₁ + y₂)/2, "AUC = 0.64" circled, and the resulting ROC plot). Independently re-verified — the instructor's 0.64 is correct.

---

## 1) Technical Explanation

**The data (slide 14).** Ten tuples sorted by probability; **P = 5** positives, **N = 5** negatives:

| Tuple | Class | Prob | TP | FP | TPR | FPR |
|---|---|---|---|---|---|---|
| 1 | P | 0.95 | 1 | 0 | 0.2 | 0 |
| 2 | N | 0.85 | 1 | 1 | 0.2 | 0.2 |
| 3 | P | 0.78 | 2 | 1 | 0.4 | 0.2 |
| 4 | P | 0.66 | 3 | 1 | 0.6 | 0.2 |
| 5 | N | 0.60 | 3 | 2 | 0.6 | 0.4 |
| 6 | P | 0.55 | 4 | 2 | 0.8 | 0.4 |
| 7 | N | 0.53 | 4 | 3 | 0.8 | 0.6 |
| 8 | N | 0.52 | 4 | 4 | 0.8 | 0.8 |
| 9 | N | 0.51 | 4 | 5 | 0.8 | 1.0 |
| 10 | P | 0.40 | 5 | 5 | 1.0 | 1.0 |

(TP, FP running totals; TPR = TP/5, FPR = FP/5. The instructor circles tuples 2 and 3 — the place where the curve first moves right and then up.) Every value matches the slide on re-computation. Method as in [[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]].

**ROC points (FPR, TPR):** (0, 0) → (0, 0.2) → (0.2, 0.2) → (0.2, 0.4) → (0.2, 0.6) → (0.4, 0.6) → (0.4, 0.8) → (0.6, 0.8) → (0.8, 0.8) → (1.0, 0.8) → (1.0, 1.0). This is the step curve drawn in the MATLAB-style plot on slide 15 (red staircase, black diagonal = random).

**Computing the area (slide 14).** Instructor lists the first points "(x, y) = (0, 0.2), (0.2, 0.2)" and writes the strip formula **Area = (x₂ − x₁)(y₁ + y₂)/2**. For the first strip: Area₁ = (0.2 − 0)(0.2 + 0.2)/2 = **0.04**. Continue for every consecutive pair of points (only moves with a positive horizontal width add area):

| From → To | x₂ − x₁ | y₁ + y₂ | Area |
|---|---|---|---|
| (0, 0.2) → (0.2, 0.2) | 0.2 | 0.4 | 0.2 × 0.4/2 = **0.04** |
| (0.2, 0.6) → (0.4, 0.6) | 0.2 | 1.2 | 0.2 × 1.2/2 = **0.12** |
| (0.4, 0.8) → (0.6, 0.8) | 0.2 | 1.6 | 0.2 × 1.6/2 = **0.16** |
| (0.6, 0.8) → (0.8, 0.8) | 0.2 | 1.6 | **0.16** |
| (0.8, 0.8) → (1.0, 0.8) | 0.2 | 1.6 | **0.16** |
| vertical moves (e.g. (0,0)→(0,0.2), (0.2,0.2)→(0.2,0.6), (0.4,0.6)→(0.4,0.8), (1,0.8)→(1,1)) | 0 | — | 0 |
| **Total** | | | **0.04 + 0.12 + 0.16 + 0.16 + 0.16 = 0.64** |

**AUC = 0.64 ✓** (circled by the instructor).

**Pair-counting check.** Positives {0.95, 0.78, 0.66, 0.55, 0.40}, negatives {0.85, 0.60, 0.53, 0.52, 0.51}. Negatives each positive outranks: 0.95 → 5; 0.78 → 4; 0.66 → 4; 0.55 → 3; 0.40 → 0. Total = 5 + 4 + 4 + 3 + 0 = **16 of 25 pairs = 0.64** ✓ — matching AUC = P(random positive ranked above random negative) ([[02_ROC_Shapes_AUC_and_Comparing_Models]]).

**Interpretation.** AUC 0.64 is only modestly above the 0.50 of random guessing — compare Example 1's 0.76 ([[04_Worked_Example_1_Building_a_ROC_Curve_and_AUC]]). The model's weakness is visible in the ranking: the high-scoring negative (tuple 2, 0.85) outranks three positives and the lowest-scoring tuple (0.40) is actually a positive; the curve even touches the diagonal at (0.2, 0.2) and (0.8, 0.8). **Example 1 is therefore the better model** on this data.

**How the area is computed in practice.** Libraries (e.g. scikit-learn's `roc_auc_score`) use exactly this trapezoid sum — or equivalently the pair-ranking count — over the sorted scores; tied scores need the diagonal trapezoid, which the formula handles automatically.

---

## 2) Simple English Explanation

**Same recipe as Example 1:** line up 10 tuples by score. Real positives (P) move the curve **up** 0.2; real negatives (N) move it **right** 0.2.

Order: P N P P N P N N N P → up, right, up, up, right, up, right, right, right, up.

**Finding the area under the staircase.** Only the **right** moves add area (an up move has no width). For each right move: area = width × average height. Width is always 0.2 here:
1. First right move at height 0.2 → 0.2 × 0.2 = **0.04**
2. Second right move at height 0.6 → 0.2 × 0.6 = **0.12**
3. Right moves at height 0.8 (three of them) → 0.2 × 0.8 = 0.16 each → **0.48**

Total area = 0.04 + 0.12 + 0.48 = **0.64**. That's the **AUC = 0.64** the teacher circled.

**Does 0.64 mean good?** It's a bit better than a coin flip (0.5) but not great. Check by pairs: out of 25 (positive, negative) pairs, the positive had the higher score in 16 → 16/25 = 0.64.

Why so-so? A negative person scored 0.85 — higher than three real positives — and one real positive got the lowest score (0.40).

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Recipe wahi hai jo Example 1 mein tha:** 10 tuples ko score se line mein lagao. Asli positive (P) par curve **0.2 upar** jaata hai; asli negative (N) par **0.2 daayein**.

Order: P N P P N P N N N P → up, right, up, up, right, up, right, right, right, up.

**Area nikaalna.** Sirf **right** moves area add karte hain (upar wale move ki width 0 hoti hai). Har right move ka area = width × average height; width yahan hamesha 0.2 hai:
1. Pehla right move height 0.2 par → 0.2 × 0.2 = **0.04** (sir ka Area₁: (0.2 − 0)(0.2 + 0.2)/2 = 0.04)
2. Doosra right move height 0.6 par → 0.2 × 0.6 = **0.12**
3. Teen right moves height 0.8 par → har ek 0.2 × 0.8 = 0.16, total **0.48**

Kul area = 0.04 + 0.12 + 0.48 = **0.64** ✅ — yahi sir ne circle kiya hai: **AUC = 0.64**.

**Ye accha hai?** Sikke uchhalne (0.5) se thoda behtar, par zyada accha nahi. Pairs se check: 25 (positive, negative) pairs mein se 16 mein positive ka score zyada tha → 16/25 = 0.64.

Kamzori kyun? Ek negative ko 0.85 score mila jo teen asli positives se zyada hai, aur ek asli positive ko sabse kam score (0.40) mila. Example 1 (AUC 0.76) is data par behtar model tha.
