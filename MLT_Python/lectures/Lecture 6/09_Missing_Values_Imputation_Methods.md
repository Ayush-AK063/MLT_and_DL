# Topic 9: Missing Values — Imputation Methods (Mean, Median, Mode & Beyond)

Source: Lecture 6, slides 22–27 (Imputation methods list, Central tendency formulas, worked mean-replacement example, outlier caveat). Enriched with web research (hot deck/cold deck/nearest neighbor imputation definitions).

---

## 1) Technical Explanation

**Imputation methods listed (slide 22)**: four named approaches —
1. **Central Tendency Imputation**
2. **Hot Deck Imputation**
3. **Cold Deck Imputation**
4. **Nearest Neighbor Imputation**

Only the first is worked through in full detail in this lecture; the other three are named but not elaborated — enrichment below fills this gap.

**1) Central Tendency Imputation (slide 23)** — *"Replacing the missing value by central tendency (mean, median, mode) for a feature vector or belonging to same class of feature vector."*
- **Mean**: `x̄ = (Σ xᵢ) / N` — the arithmetic average of all available (non-missing) values for that feature.
- **Median**: the middle value when data is sorted — formula given for both cases: `md = x₍ₙ₋₁₎/₂` when N is odd, `md = ½(x_{n/2} + x_{n/2 + 1})` when N is even.
- **Mode**: *"the most frequent value corresponding to a certain feature in a given data set."*

**Worked example — Replacing Mean Value (slides 24–25)**, continuing the forest fires dataset from Topic 8:
- For each column with missing values, the **mean of that column's available values** is computed and used to fill all `NaN`s in that column.
- Demonstrated results: missing `temp` values (in Oct and Sep rows) both filled with **15.3**; missing `FFMC` values (Mar and Aug rows) filled with **90.5**; missing `DC` value (Aug row) filled with **458.3**; missing `RH` value (Aug row) filled with **58.7**; missing `wind` values (Oct and Aug rows) filled with **3.57**.
- Note: **all NaNs within the same column get the identical mean value** — this is the defining characteristic of mean imputation (it doesn't customize the fill per-row, just per-column).

**Critical limitation of mean imputation (slides 26–27)**: *"Replacing by mean value: Not a suitable method if data set has many outliers."* Illustrated with a striking example: human weights of `67, 78, 900, -56, 389, -1`. Computing the mean of this set gives **229.5** — a value that doesn't represent any realistic human weight, because the extreme/impossible outliers (`900`, `-56`, `389`, `-1`) have dragged the mean far away from where the "typical" values (`67`, `78`) actually cluster. **Resolution**: in such cases, the **median** should be used instead of the mean, since median is far more robust to outliers (it only depends on the middle-ranked value(s), not the magnitude of extreme values). Additionally: *"Mode is a good option for missing values in case of categorical variables"* — since mean/median are mathematically meaningless for nominal categorical data (recall Topic 1's feature-type taxonomy, [[01_Structured_Data_and_Types_of_Features]]), mode is the only central-tendency measure that makes sense there.

**Enrichment — the three additional imputation methods (from web research)**:

2. **Hot Deck Imputation**: replaces a missing value for a "recipient" record with an actual observed value taken from a similar "donor" record **within the same dataset**. Two common variants: *random hot deck* (donor chosen randomly from similar candidates) and *deterministic hot deck* (donor chosen via a nearest-neighbor-style distance metric). The name "hot" deck reflects that the donor data comes from the *same, currently-being-analyzed* dataset.

3. **Cold Deck Imputation**: conceptually similar to hot deck, but the donor value comes from an **external/different dataset or source** (not the dataset currently being analyzed) — hence "cold," as opposed to the "hot" (actively in-use) dataset.

4. **Nearest Neighbor Imputation**: for each record with a missing value, find the most similar complete record(s) elsewhere in the dataset (using a distance metric like Euclidean distance) and use their value(s) — often averaging the nearest neighbors' values — to fill the gap. This is more sophisticated than simple mean/median imputation because it accounts for *similarity across other features*, rather than blindly using one global statistic for the entire column.

---

## 2) Simple English Explanation

This section covers **imputation** — the smartest of the three missing-value strategies, because it fills in gaps automatically using a calculated, reasonable guess, rather than deleting data or requiring painstaking manual work.

**Central Tendency Imputation — the most common approach**: fill in a missing value using a summary statistic calculated from the other, known values in that same column:
- **Mean** — the average.
- **Median** — the middle value when everything is sorted.
- **Mode** — the value that shows up most often.

**Worked example**: In the forest fires dataset, every missing "temp" value got replaced with **15.3** (the average temperature calculated from all the temperatures that *were* recorded), every missing "wind" value got replaced with **3.57**, and so on for each column — one calculated number per column, used to fill every gap in that column.

**A crucial warning about using the mean**: the mean can be badly misleading if your data has **outliers** (extreme, unusual values). The lecture gives a great example: imagine a list of human weights: 67, 78, 900, -56, 389, -1. Some of these numbers are obviously wrong (nobody weighs -56 kg or 900 kg!) — but if you naively calculate the average of this list anyway, you get **229.5**, which isn't close to a realistic human weight at all. The extreme, wrong values dragged the average way off. **The fix**: use the **median** instead when your data has outliers — it's much more resistant to being thrown off by a few crazy values. And for categorical data (like "account type"), you can't calculate a mean or median at all — you use the **mode** (the most common category) instead.

**Three other, more advanced imputation methods** (briefly listed in the lecture without much detail, explained here):
- **Hot Deck Imputation** — find a similar-looking record already in your dataset, and copy its value over to fill the gap.
- **Cold Deck Imputation** — same idea, but the "donor" value comes from a different, outside dataset, rather than the one you're currently working with.
- **Nearest Neighbor Imputation** — look for the records most similar to the one with the missing value (based on all its other features), and use their values to make a smart guess for the missing one — generally more accurate than just using one flat average for the whole column.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section **Imputation** cover karta hai — teeno missing-value strategies mein sabse smart approach, kyunki ye gaps ko automatically ek calculated, reasonable guess se bharta hai, na ki data delete karta hai ya bahut zyada manual mehnat maangta hai.

**Central Tendency Imputation — sabse common approach:**
Missing value ko us column ke baaki (known) values se calculate ki gayi ek summary statistic se bharna:
- **Mean (Average)** — sab values ka average
- **Median (Beech ki value)** — sab values ko sort karke jo beech mein aaye
- **Mode (Sabse common value)** — jo value sabse zyada baar aaye

**Worked Example**: Forest fires dataset mein, har missing "temp" value ko **15.3** se replace kiya gaya (jo saare available temperatures ka average hai), har missing "wind" value ko **3.57** se replace kiya gaya, aur waise hi har column ke liye — **ek calculated number per column**, jo us column ke saare gaps bharta hai.

**Mean use karte waqt ek zaroori warning:**
Mean bahut misleading ho sakta hai agar data mein **outliers** (extreme, ajeeb values) ho. Lecture ek achha example deta hai: socho insaanon ke weight ki ek list hai: 67, 78, 900, -56, 389, -1. Inme se kuch numbers obviously galat hai (koi -56 kg ya 900 kg weigh nahi karta!) — lekin agar aap seedha is list ka average nikaal do, to milta hai **229.5**, jo kisi bhi realistic human weight ke aas-paas nahi hai. In extreme, galat values ne average ko bahut door khinch diya.

**Fix**: Jab data mein outliers ho, to **median** use karo instead of mean — ye kuch crazy values se distract hone mein bahut zyada resistant hai. Aur categorical data (jaise "account type") ke liye, aap mean ya median calculate hi nahi kar sakte — waha **mode** (sabse common category) use karte hai.

**3 aur advanced imputation methods** (lecture mein bas naam liya gaya, yaha explain kiya):
- **Hot Deck Imputation** — aapke apne dataset mein hi ek similar-dikhne wala record dhoondho, aur uski value copy karke gap bharo.
- **Cold Deck Imputation** — same idea, lekin "donor" value ek doosre, alag/external dataset se aati hai, na ki jis dataset pe aap kaam kar rahe ho.
- **Nearest Neighbor Imputation** — un records ko dhoondho jo missing-value wale record se sabse zyada similar hai (baaki sabhi features ke aadhar par), aur unki values use karke missing value ka smart guess lagao — generally sirf ek flat average use karne se zyada accurate hota hai.
