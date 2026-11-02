# Topic 6: Worked Examples — Euclidean Distance, Jaccard Coefficient, and Cosine Similarity

Source: Lecture 10, slides 15–23 (three worked numeric examples). All calculations below were independently re-verified.

---

## 1) Technical Explanation

### Example 1: Euclidean distance between two features (slides 15–17)

Data (10 paired observations, feature F1 = "Subjects", feature F2 = "Marks"):

| Subjects (F1) | Marks (F2) | (F1−F2) | (F1−F2)² |
|---|---|---|---|
| 2 | 6 | −4 | 16 |
| 3 | 5.5 | −2.5 | 6.25 |
| 6 | 4 | 2 | 4 |
| 7 | 2.5 | 4.5 | 20.25 |
| 8 | 3 | 5 | 25 |
| 6 | 5.5 | 0.5 | 0.25 |
| 6 | 7 | −1 | 1 |
| 7 | 6 | 1 | 1 |
| 8 | 6 | 2 | 4 |
| 9 | 7 | 2 | 4 |

Using $ d(F_1, F_2) = \sqrt{\sum_{i=1}^{n} (F_{1i} - F_{2i})^2} $:

Sum of squared differences = 16 + 6.25 + 4 + 20.25 + 25 + 0.25 + 1 + 1 + 4 + 4 = **81.75**

$ d(F_1, F_2) = \sqrt{81.75} \approx \mathbf{9.04} $

**Verification note:** the slide deck stops at the table of squared differences (slide 17) and never states the final square-rooted answer. Independently computing it: sum = 81.75, and √81.75 ≈ 9.04. This final step is added here for completeness since the slides leave it implicit.

### Example 2: Jaccard coefficient (slides 18–20)

Two binary features:
- F1 = (0, 1, 1, 0, 1, 0, 1, 0)
- F2 = (1, 1, 0, 0, 1, 0, 0, 0)

Position-by-position comparison (1-indexed):

| Position | F1 | F2 | Category |
|---|---|---|---|
| 1 | 0 | 1 | n01 |
| 2 | 1 | 1 | n11 |
| 3 | 1 | 0 | n10 |
| 4 | 0 | 0 | n00 |
| 5 | 1 | 1 | n11 |
| 6 | 0 | 0 | n00 |
| 7 | 1 | 0 | n10 |
| 8 | 0 | 0 | n00 |

Counts: n11 = 2, n10 = 2, n01 = 1, n00 = 3.

$$ \text{Jaccard Similarity} = \frac{n_{11}}{n_{01}+n_{10}+n_{11}} = \frac{2}{1+2+2} = \frac{2}{5} = 0.4 $$

$$ \text{Jaccard Distance} = 1 - 0.4 = \mathbf{0.6} $$

**Verified** — matches the slide's stated answer exactly (J = 0.4, distance = 0.6).

### Example 3: Cosine similarity (slides 21–23)

Two vectors:
- x = (2, 4, 0, 0, 2, 1, 3, 0, 0)
- y = (2, 1, 0, 0, 3, 2, 1, 0, 1)

**Dot product:**
$$ x \cdot y = (2)(2) + (4)(1) + (0)(0) + (0)(0) + (2)(3) + (1)(2) + (3)(1) + (0)(0) + (0)(1) $$
$$ = 4 + 4 + 0 + 0 + 6 + 2 + 3 + 0 + 0 = \mathbf{19} $$

**Magnitude of x:**
$$ |x| = \sqrt{2^2+4^2+0^2+0^2+2^2+1^2+3^2+0^2+0^2} = \sqrt{4+16+0+0+4+1+9+0+0} = \sqrt{34} \approx 5.83 $$

**Magnitude of y:**
$$ |y| = \sqrt{2^2+1^2+0^2+0^2+3^2+2^2+1^2+0^2+1^2} = \sqrt{4+1+0+0+9+4+1+0+1} = \sqrt{20} \approx 4.47 $$

**Cosine similarity:**
$$ \cos(x,y) = \frac{19}{5.83 \times 4.47} = \frac{19}{26.06} \approx \mathbf{0.729} $$

**Verified** — matches the slide's stated answer exactly (cos(x,y) = 0.729). A cosine of 0.729 indicates the two vectors point in a fairly similar direction (closer to 1 = identical direction than to 0 = orthogonal), meaning x and y are reasonably similar in composition even though their raw magnitudes (5.83 vs. 4.47) differ.

---

## 2) Simple English Explanation

**Example 1 (Euclidean distance):** You have 10 pairs of numbers (subjects marks vs. another marks column). For each pair, find the difference, square it (this makes negative differences positive and emphasizes larger gaps), add up all 10 squared differences (you get 81.75), then take the square root of that total. The result, about 9.04, is a single number summarizing "how far apart" these two columns of numbers are overall — the smaller this number, the more similar/redundant the two columns are.

**Example 2 (Jaccard coefficient):** You have two lists of 0s and 1s (like two people's "did you like this movie" surveys across 8 movies, where 1 = liked). You count: in how many movies did *both* people say 1 (liked)? That's 2. Then you count all the movies where *at least one* person said 1 (liked) — ignoring movies where both said 0 (didn't like), because "we both didn't like it" isn't very informative agreement. That total is 5 (2 both-liked + 2 only-one-liked + 1 only-other-liked). Jaccard similarity = 2/5 = 0.4, meaning they agree on 40% of the movies they collectively liked. Jaccard *distance* (how different they are) = 1 − 0.4 = 0.6.

**Example 3 (Cosine similarity):** You have two lists of numbers (like word-counts of two documents across 9 words). Instead of measuring "distance" directly, cosine similarity measures the angle between the two lists when treated as arrows (vectors) in space. You compute: the "dot product" (multiply matching positions and add them all up = 19), then each vector's own "length" (using the Pythagorean-style formula: square each number, add them, square root — giving 5.83 and 4.47). Divide the dot product by the product of the two lengths: 19 / (5.83 × 4.47) ≈ 0.729. A value close to 1 means the two documents talk about very similar things in similar proportions, even if one document is much longer than the other.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Example 1 (Euclidean distance):** Tumhare paas 10 pairs of numbers hain (jaise subjects marks vs kisi aur marks column). Har pair ke liye difference nikaalo, use square karo (isse negative differences positive ho jaate hain aur bade gaps zyada emphasize hote hain), saare 10 squared differences ko add karo (total milta hai 81.75), phir us total ka square root nikaalo. Result, lagbhag 9.04, ek single number hai jo batata hai "ye do columns overall kitni door hain ek doosre se" — ye number jitna chhota hoga, dono columns utne zyada similar/redundant honge.

**Example 2 (Jaccard coefficient):** Tumhare paas 0 aur 1 ki do lists hain (jaise do logon ka "kya tumhe ye movie pasand aayi" survey 8 movies ke liye, jahan 1 = pasand aayi). Tum count karte ho: kitni movies mein *dono* ne 1 bola (pasand aayi)? Ye 2 hai. Phir tum count karte ho un saari movies ko jahan *kam se kam ek* ne 1 bola (pasand aayi) — un movies ko ignore karte hue jahan dono ne 0 bola (pasand nahi aayi), kyunki "dono ko pasand nahi aayi" bahut informative agreement nahi hai. Ye total 5 hai (2 dono-ko-pasand + 2 sirf-ek-ko-pasand + 1 doosre-ko-pasand). Jaccard similarity = 2/5 = 0.4, matlab wo apni collectively pasand ki hui movies mein se 40% pe agree karte hain. Jaccard *distance* (kitne alag hain) = 1 − 0.4 = 0.6.

**Example 3 (Cosine similarity):** Tumhare paas numbers ki do lists hain (jaise do documents ke 9 words ke word-counts). "Distance" seedhe measure karne ke bajaye, cosine similarity un do lists ke beech ka angle measure karta hai jab unhe arrows (vectors) samjha jaaye space mein. Tum calculate karte ho: "dot product" (matching positions ko multiply karke sab add karo = 19), phir har vector ki apni "length" (Pythagoras jaisa formula use karke: har number ko square karo, add karo, square root nikaalo — 5.83 aur 4.47 milta hai). Dot product ko dono lengths ke product se divide karo: 19 / (5.83 × 4.47) ≈ 0.729. Jo value 1 ke kareeb ho, uska matlab hai dono documents bahut similar cheezon ke baare mein similar proportion mein baat kar rahe hain, chahe ek document doosre se bahut zyada lamba kyun na ho.
