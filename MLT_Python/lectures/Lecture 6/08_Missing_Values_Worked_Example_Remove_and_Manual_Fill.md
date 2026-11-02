# Topic 8: Missing Values — Worked Examples (Remove vs. Manually Fill)

Source: Lecture 6, slides 19–21 (Sample forest fires dataset, Removing the data entity, Manually filling up of values).

---

## 1) Technical Explanation

**The running example dataset (slide 19)**: a sample dataset related to **forest fires**, with columns `Month, FFMC, DC, temp, RH, wind` (FFMC = Fine Fuel Moisture Code, DC = Drought Code — standard fire-weather indices; RH = Relative Humidity). Several cells contain **`NaN`** (Not a Number — the standard placeholder for a missing value in data science tools like pandas/NumPy), scattered across multiple rows and columns (e.g., missing `temp` and `wind` values in an October row; missing `FFMC` in a March row; multiple missing values in the August rows).

**Technique 1 — Removing the data entity (slide 20)**:
- Described as *"Most easiest way directly to clean the data."*
- **Explicit drawback stated**: *"this is usually discouraged as it leads to loss of data, as you are removing the data entity or feature values that can add value to data set as well."*
- **Demonstrated on the dataset**: rows containing any `NaN` are deleted entirely. Starting from 10 rows, the rows for the two `oct` entries with NaNs, the `mar` row with a NaN FFMC, both `aug` rows with NaNs, and the `sep` row with a NaN temp are all removed — leaving only **5 clean rows** (mar, oct, mar, aug, sep) out of the original 10. This concretely illustrates the drawback: **half the dataset was discarded** just to remove a handful of missing cells, most of which were in otherwise-valid rows with useful information in their other columns.

**Technique 2 — Manually filling up of values (slide 21)**:
- **Explicit drawback stated**: *"This approach is time consuming, and not recommended for huge data sets."*
- **Demonstrated on the same dataset**: each `NaN` is individually replaced with a manually chosen, plausible value (e.g., the missing October `temp` of NaN is filled with `17`; the missing March `FFMC` is filled with `91.6`; the missing August `DC` is filled with `380`; etc.) — presumably based on domain judgment, similar records, or external reference, though the lecture doesn't specify the exact reasoning for each manually chosen value (this is inherent to the technique's dependence on human judgment case-by-case).
- Result: all 10 rows are retained, with every `NaN` replaced by a specific, chosen number.

**Comparing the two techniques (synthesized from both slides)**:
| Technique | Pro | Con |
|---|---|---|
| **Remove entity** | Fast, simple | Loses potentially valuable data; can shrink dataset significantly |
| **Manually fill** | Keeps all data; can leverage domain expertise | Extremely time-consuming; impractical/unscalable for large datasets |

This sets up the motivation for the third technique — **Imputation** (Topic 9) — which aims to be more automated/scalable than manual filling, while (unlike removal) preserving the data.

---

## 2) Simple English Explanation

This section shows two of the three ways to handle missing values, worked through on a real example dataset — so you can see exactly what each technique looks like in practice, and why each has a downside.

**The example**: a table about forest fires, tracking things like the month, weather codes, temperature, humidity, and wind for various fire events. Several cells in this table are blank/missing, marked as "NaN."

**Technique 1 — Just delete the rows with missing data:**
This is the simplest possible fix — if a row has any missing value anywhere, throw the whole row away. When applied to the forest fire dataset, this drops the number of usable rows from 10 down to just **5** — literally half the data got thrown out! This shows the technique's big weakness: you lose a lot of otherwise-good data (all the other columns in those rows were perfectly fine — you're throwing away good information just because one cell was empty).

**Technique 2 — Fill in the missing values by hand:**
Instead of deleting anything, a person manually decides what number should go in each blank cell (like deciding the missing temperature was probably around 17, or the missing FFMC value was probably around 91.6). This keeps all 10 rows of data — nothing is lost. But the obvious downside: this takes a lot of time and effort, and it's simply not realistic to do this one-by-one if you have a dataset with millions of rows.

**The takeaway**: Removing rows is fast but wasteful; manually filling values keeps everything but doesn't scale. This naturally leads to wanting a third option that's both automatic *and* preserves the data — which is exactly what "imputation" (covered next) provides.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section missing values handle karne ke 2 tarike dikhata hai, ek real example dataset pe kaam karke — taaki aap dekh sako ki har technique actually kaisi dikhti hai, aur har ek mein kya kami hai.

**Example**: Forest fires ke baare mein ek table, jisme month, weather codes, temperature, humidity, aur wind jaise data hai alag-alag fire events ke liye. Is table ki kai cells khali/missing hai, "NaN" se mark ki gayi hai.

**Technique 1 — Missing data wali rows ko sidhe delete karna:**
Ye sabse simple fix hai — agar kisi row mein kahi bhi missing value hai, to puri row hata do. Forest fire dataset pe apply karne se, usable rows **10 se ghatkar sirf 5 reh gayi** — literally aadha data phenk diya gaya! Ye technique ki badi kamzori dikhata hai: aap bahut saara achha data khoo dete ho (un rows ke baaki columns bilkul theek the — sirf isliye achhi information phenk di kyunki ek cell khali thi).

**Technique 2 — Missing values ko hath se bharna:**
Kuch delete karne ke bajaye, koi insaan manually decide karta hai har khali cell mein kya number aana chahiye (jaise decide karna ki missing temperature shayad 17 ke aas-paas hoga, ya missing FFMC value shayad 91.6 ke aas-paas hoga). Isse saari 10 rows ka data bacha rehta hai — kuch bhi lost nahi hota. Lekin obvious kami: isme **bahut time aur mehnat lagti hai**, aur agar aapke paas millions rows ka dataset ho, to one-by-one aisa karna realistic hi nahi hai.

**Yaad rakhne ki baat**: Rows delete karna fast hai lekin wasteful hai (data waste ho jaata hai); manually values bharna sab kuch bacha leta hai lekin scale nahi karta (bade data ke liye practical nahi hai). Isse naturally ek teesre option ki zaroorat lagti hai jo **automatic bhi ho aur data bhi bachaye** — yehi exactly "imputation" (agla topic) karta hai.
