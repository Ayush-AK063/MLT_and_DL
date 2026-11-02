# Topic 4: Discretization by Binning — Equal-Width vs. Equal-Frequency

Source: Lecture 8, slides 20–27 (Discretization Methods, Discretization by Binning ×2, Equal-Width Example ×3, Equal-Frequency Example ×2).

All worked examples verified by independent recalculation — every number below exactly matches the lecture's stated results.

---

## 1) Technical Explanation

**Discretization Methods overview (slide 20)**: *"A basic distinction between discretization methods for classification is whether class information is used (supervised) or not (unsupervised)."* Two methods are named: **Binning** and **Clustering analysis** (clustering covered in Topic 5, [[05_Discretization_by_Clustering]]).

**Discretization by Binning (slides 21–22)**:
- Attribute values can be discretized using either **equal-width** or **equal-frequency** binning.
- **Procedure**: binning approaches first **sort** the attribute values, then **partition** them into bins.
- **Equal-width approach**: *"divides the range of the attribute into a user-specified number of intervals each having the same width."*
- **Equal-frequency (equal-depth) approach**: *"tries to put the same number of objects into each interval."*
- After bins are determined, **all values are replaced by bin labels** to discretize the attribute (alternatively, values may be replaced by bin means or medians instead of a plain label — connecting back to the bin-smoothing variants from Lecture 6's Binning topic, [[11_Binning_Method_Worked_Example]] from Lecture 6).
- **Important classification**: *"Binning does not use class information and is therefore an unsupervised discretization technique."*

---

### Worked Example 1: Equal-Width Binning

**Dataset**: 12 sorted values of a `price` attribute: `5, 10, 11, 13, 15, 35, 50, 55, 72, 89, 204, 215`.

**Step 1 — Calculate interval width**: `width = (max − min) / (number of bins) = (215 − 5) / 3 = 70`.

**Step 2 — Partition into 3 bins**, each spanning a range of width 70, starting from the minimum (5):
- Bin 1 range: `[5, 75)` → contains `5, 10, 11, 13, 15, 35, 50, 55, 72` (verified: all 9 of these values are less than 75; the next value, 89, is ≥75, so it doesn't belong here)
- Bin 2 range: `[75, 145)` → contains `89` (verified: 89 is ≥75 and <145; the next value, 204, is ≥145)
- Bin 3 range: `[145, 215]` → contains `204, 215` (verified: both are ≥145)

**Step 3 — Replace each value with its bin label**:
| price | 5 | 10 | 11 | 13 | 15 | 35 | 50 | 55 | 72 | 89 | 204 | 215 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| categorical attr. | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 3 | 3 |

**Notable consequence**: equal-width binning here produces a very **unbalanced** result — bin 1 has 9 values, bin 2 has just 1 value, and bin 3 has 2 values. This happens because the data has a couple of large outlier-like values (204, 215) that stretch the overall range, forcing most of the "normal" values into a single wide bin. This is a real limitation of equal-width binning when data is not evenly spread (skewed data).

---

### Worked Example 2: Equal-Frequency Binning

**Same dataset**: `5, 10, 11, 13, 15, 35, 50, 55, 72, 89, 204, 215` (12 values).

**Step 1 — Decide bin count and calculate items per bin**: 3 bins requested, so each bin should contain `12 / 3 = 4` values.

**Step 2 — Partition into 3 bins of 4 consecutive (sorted) values each**:
- Bin 1: `5, 10, 11, 13`
- Bin 2: `15, 35, 50, 55`
- Bin 3: `72, 89, 204, 215`

**Step 3 — Replace each value with its bin label**:
| price | 5 | 10 | 11 | 13 | 15 | 35 | 50 | 55 | 72 | 89 | 204 | 215 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| categorical attr. | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 |

**Comparison with equal-width**: notice bin 3 here contains `72, 89, 204, 215` — a much wider *range* of actual values (72 to 215) than equal-width's bin 3 (`204, 215` only) — but exactly the same *count* (4 items) as every other bin. This is the fundamental trade-off: **equal-width guarantees equal-sized ranges but unequal counts; equal-frequency guarantees equal counts but unequal-sized ranges.**

---

## 2) Simple English Explanation

**Discretization by binning** is a way to turn a list of numbers into a small set of categories by sorting the numbers and grouping them into "bins" (buckets). There are two main ways to decide how big each bin should be:

- **Equal-width binning**: split the *range* of values into equal-sized chunks (like splitting 0–100 into three 33-point-wide chunks: 0–33, 34–66, 67–100) — regardless of how many actual data points end up in each chunk.
- **Equal-frequency binning**: instead of equal-sized ranges, make sure each bin has the *same number of data points* — even if that means the ranges end up very different sizes.

**A worked example with equal-width binning**: Take these 12 sorted prices: `5, 10, 11, 13, 15, 35, 50, 55, 72, 89, 204, 215`.
- The full range is from 5 to 215, a spread of 210. Splitting that evenly into 3 bins means each bin covers a width of 70.
- Bin 1 covers 5 to 75, Bin 2 covers 75 to 145, Bin 3 covers 145 to 215.
- Counting how many actual prices fall in each: Bin 1 gets **9** prices (5 through 72), Bin 2 gets just **1** price (89), and Bin 3 gets **2** prices (204, 215).
- Notice how unbalanced this is! Because a couple of prices (204, 215) are much bigger than the rest, they stretch out the whole range, squishing almost everything else into one crowded bin.

**The same data with equal-frequency binning**: Since there are 12 prices and we want 3 bins, each bin gets exactly `12÷3 = 4` prices — no more, no less.
- Bin 1: the 4 smallest prices (`5, 10, 11, 13`)
- Bin 2: the next 4 (`15, 35, 50, 55`)
- Bin 3: the last 4 (`72, 89, 204, 215`)
- This time, every bin has the same *count*, but the actual *range* each bin covers is very different — Bin 3 spans a huge range (72 to 215) while Bin 1 spans a tiny range (5 to 13).

**The trade-off**: equal-width keeps the "size" of each range consistent but can leave you with very unbalanced bin counts (like our example). Equal-frequency keeps the counts balanced but can leave you with very unevenly-sized ranges. Which one you pick depends on what matters more for your specific analysis.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Discretization by Binning** ek tarika hai numbers ki list ko chhoti categories mein badalne ka — numbers ko sort karke unhe "bins" (buckets) mein group karke. Har bin kitna bada hona chahiye, iske 2 main tarike hai:

- **Equal-Width Binning**: values ke *range* ko equal-size chunks mein baanto (jaise 0-100 ko teen 33-point-wide chunks mein baantna: 0-33, 34-66, 67-100) — chahe har chunk mein kitne bhi actual data points aa jaayein.
- **Equal-Frequency Binning**: equal-size ranges banane ke bajaye, ye sunishchit karo ki har bin mein *same number of data points* ho — chahe iske liye ranges bahut alag sizes ki kyun na ho jaayein.

**Ek worked example Equal-Width Binning ke saath**: Ye 12 sorted prices lo: `5, 10, 11, 13, 15, 35, 50, 55, 72, 89, 204, 215`.
- Pura range 5 se 215 tak hai, spread 210 hai. Isse equally 3 bins mein baantne se har bin ki width 70 aati hai.
- Bin 1 covers 5 to 75, Bin 2 covers 75 to 145, Bin 3 covers 145 to 215.
- Ginte hai ki kitne actual prices har bin mein aate hai: Bin 1 mein **9** prices (5 se 72 tak), Bin 2 mein sirf **1** price (89), aur Bin 3 mein **2** prices (204, 215).
- Dekho kitna unbalanced hai! Kyunki kuch prices (204, 215) baaki sab se bahut bade hai, wo poore range ko stretch kar dete hai, aur almost sab kuch ek crowded bin mein squish ho jaata hai.

**Wahi data Equal-Frequency Binning ke saath**: Kyunki 12 prices hai aur humein 3 bins chahiye, har bin ko exactly `12÷3 = 4` prices milte hai — na kam, na zyada.
- Bin 1: 4 sabse chhote prices (`5, 10, 11, 13`)
- Bin 2: agle 4 (`15, 35, 50, 55`)
- Bin 3: aakhri 4 (`72, 89, 204, 215`)
- Is baar, har bin ka *count* same hai, lekin har bin ka actual *range* bahut alag hai — Bin 3 ek bada range cover karta hai (72 se 215 tak) jabki Bin 1 ek chhota range cover karta hai (5 se 13 tak).

**Trade-off**: Equal-Width har range ka "size" consistent rakhta hai lekin bahut unbalanced bin counts de sakta hai (jaise humare example mein). Equal-Frequency counts ko balanced rakhta hai lekin bahut uneven-sized ranges de sakta hai. Kaunsa choose karna hai, ye depend karta hai aapke specific analysis mein kya zyada important hai.
