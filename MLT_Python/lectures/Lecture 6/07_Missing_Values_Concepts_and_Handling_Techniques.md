# Topic 7: Missing Values — Concepts & Handling Techniques Overview

Source: Lecture 6, slides 17–18 (Missing Values, Missing Values Contd.).

---

## 1) Technical Explanation

**Definition**: *"Missing values: data values are not available."* Formally, this means many data entities have **no recorded value** corresponding to a particular feature. **Example given**: BMI value missing for some persons in a diabetes dataset.

**Probable reasons for missing values** — four causes listed:
1. **Faulty measuring equipment** — the sensor/instrument malfunctioned or failed to record.
2. **Reluctance of person to share certain detail** — in survey/self-reported data, respondents may deliberately skip sensitive questions (e.g., income, health conditions).
3. **Negligence on part of data entry operator** — human error during manual data entry.
4. **Feature unimportance at time of data collection** — a feature that seemed irrelevant when data was originally gathered wasn't recorded, but later turns out to be useful for a new analysis.

**Missing data handling techniques — three broad approaches**:
1. **Removing the data entity** — deleting the row (or column) containing missing data (detailed with a worked example in Topic 8).
2. **Manually filling the values** — a human fills in the gaps based on domain knowledge or lookup (also detailed in Topic 8).
3. **Imputation** — *"process used to determine and assign replacement values for missing, invalid, or inconsistent data"* — an automated/algorithmic approach (detailed extensively in Topic 9).

**Key guiding principle stated in the lecture**: *"Technique selection is specific to user's preference, dataset or feature type or problem set"* — there is **no single universally correct method**; the right choice of missing-data handling technique depends on context (how much data is missing, what type of feature it is, what the downstream task requires, computational constraints, etc.).

---

## 2) Simple English Explanation

This section explains what "missing values" actually are, why they happen, and gives a first overview of the three main ways to deal with them.

**What are missing values?** Simply put, some rows in your dataset just don't have a value recorded for a particular column. For example, in a medical dataset tracking diabetes, some people's BMI (Body Mass Index) field might just be blank — nobody recorded it for them.

**Why does this happen? Four common reasons:**
1. **Broken equipment** — the machine measuring something failed and didn't record a value.
2. **People not wanting to share something** — if you're filling out a survey, you might skip a question you consider too personal (like your income).
3. **Human mistakes during data entry** — someone typing the data in just missed a field by accident.
4. **The feature didn't seem important at the time** — maybe nobody thought to record something when the data was first collected, but now, for a new analysis, that missing piece turns out to matter.

**Three main ways to handle missing values:**
1. **Remove the row entirely** — just delete any record that has missing data.
2. **Fill it in by hand** — a person manually decides what the missing value should probably be, based on other information they know.
3. **Imputation** — use an automated method/formula to calculate and fill in a reasonable replacement value.

**Important rule of thumb**: there's no single "always correct" way to handle missing data. The best choice depends on your specific situation — what kind of data it is, how much is missing, and what you're trying to do with it.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section batata hai **"missing values" actually kya hai**, ye kyun hoti hai, aur inhe handle karne ke 3 main tarikon ka overview deta hai.

**Missing Values kya hai?**
Simple bhasha mein, aapke dataset ki kuch rows mein kisi particular column ki value **record hi nahi hui**. Jaise, ek diabetes dataset mein kuch logon ka BMI (Body Mass Index) field khali ho sakta hai — kisi ne unke liye ye record nahi kiya.

**Ye kyun hota hai? 4 common reasons:**
1. **Kharab equipment** — measuring machine fail ho gayi aur value record nahi hui.
2. **Log kuch share nahi karna chahte** — agar aap survey bhar rahe ho, to shayad koi bahut personal sawaal (jaise income) skip kar do.
3. **Data entry mein human mistake** — kisi ne data type karte waqt galti se field miss kar diya.
4. **Us waqt wo feature important nahi lagi** — shayad data collect karte waqt kisi ne socha hi nahi ki wo cheez record karni chahiye, lekin ab, nayi analysis ke liye, wo missing piece important nikal aaya.

**Missing values handle karne ke 3 main tarike:**
1. **Poori row hata dena** — jis record mein missing data hai, use bas delete kar do.
2. **Hath se bhar dena** — koi insaan manually decide karta hai missing value kya honi chahiye, apni jaankari ke aadhar pe.
3. **Imputation** — koi automated method/formula use karke ek reasonable replacement value calculate karke bhar dena.

**Important rule (yaad rakho)**: Missing data handle karne ka koi **"hamesha sahi" tarika nahi hai**. Best choice aapki specific situation pe depend karti hai — data kis type ka hai, kitna missing hai, aur aap uske saath kya karna chahte ho.
