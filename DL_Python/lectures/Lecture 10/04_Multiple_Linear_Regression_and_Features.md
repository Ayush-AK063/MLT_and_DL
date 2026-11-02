# Topic 4: Multiple Linear Regression — Adding More Features

Source: Lecture 10 (ES532: Introduction to Deep Learning), slides 13–18.

---

## 1) Technical Explanation

[[02_Simple_Linear_Regression_Intuition_Home_Price_Example]] and [[03_Simple_Linear_Regression_Worked_Example_Verified]] predicted price from a single input, area. This topic extends the same dataset with **two more columns** — bedrooms and age (of the house) — and asks the natural next question: what if price depends on *multiple* factors at once?

| area | bedrooms | age | price |
|---|---|---|---|
| 2600 | 3 | 20 | 550000 |
| 3000 | 4 | 15 | 565000 |
| 3200 | *(blank)* | 18 | 610000 |
| 3600 | 3 | 30 | 595000 |
| 4000 | 5 | 8 | 760000 |

**An anomaly worth flagging**: the third row's `bedrooms` value is **missing** in the source slide (left blank in the table) — this is presumably intentional, since datasets with a deliberately missing value like this are commonly used in introductory ML tutorials specifically to set up a later discussion of missing-data handling (imputation, dropping the row, etc. — the same kind of "missing values" topic already covered in depth in the sibling `MLT_Python` project, e.g. its Lecture 6). The slides here don't address it explicitly, so it's flagged rather than silently worked around; if a later DL lecture revisits this exact dataset to demonstrate missing-value handling, this note should be updated to point to it.

**The model form generalizes** from a single-slope line to a **weighted sum of multiple features**, each with its own coefficient:

$$\text{price} = m_1 \times \text{area} + m_2 \times \text{bedrooms} + m_3 \times \text{age} + b$$

or, in fully generic variable notation:

$$y = m_1 x_1 + m_2 x_2 + m_3 x_3 + b$$

**Terminology, as labeled directly on the slides**:
- $y$ (price) is the **dependent variable** — the thing being predicted.
- $x_1, x_2, x_3$ (area, bedrooms, age) are the **independent variables**, also called **features** — the inputs the prediction is based on.
- $m_1, m_2, m_3$ are the **coefficients** — one per feature, each measuring how much $y$ changes per unit change in that specific feature, holding the others fixed.
- $b$ remains the intercept, same role as in simple linear regression.

**The posed exercise**: given this table, predict the price of a home with (a) 3000 sq ft, 3 bedrooms, 40 years old, and (b) 2500 sq ft, 4 bedrooms, 5 years old. **This is left unsolved in the source slides**, and — unlike the single-feature case in [[03_Simple_Linear_Regression_Worked_Example_Verified]] — it is **not solved here either**: fitting a reliable 3-feature regression by hand from only 5 data points (one of which has a missing feature) would require either discarding the incomplete row (leaving just 4 points to fit 4 unknowns $m_1,m_2,m_3,b$, an exact-fit rather than a genuine best-fit situation with no error left to check) or an imputation strategy the slides don't specify — either choice would be inventing information the source material doesn't provide, rather than the kind of independent verification done elsewhere in these notes. This is flagged as an open exercise rather than answered with a fabricated number.

**Connection forward**: this same "weighted sum of features plus bias" structure is exactly what a single neuron's pre-activation, $a_i(x) = b_i + W_i h_{i-1}(x)$ from [[02_PreActivation_and_Activation_Equations]] in Lecture 9, computes — multiple linear regression is, in effect, a single linear neuron with no activation function (or a linear one) applied at all.

---

## 2) Simple English Explanation

So far the house-price example only used one piece of information (area) to predict price. This topic asks: what if we use *several* pieces of information at once — area, number of bedrooms, and age of the house?

**A quick honest note on the data itself**: one of the five houses in this table is missing its "bedrooms" value entirely — it's just left blank. The slides don't explain why or what to do about it, so this is flagged here rather than quietly ignored or guessed at. (This is a very common thing to see in real datasets, and a whole separate topic — missing value handling — exists specifically to deal with it; the sibling MLT_Python project's own Lecture 6 covers that in depth.)

**The model, extended**: instead of one slope times one input plus a bias, you now have *three* slopes, one for each input, all added together, plus a bias:

$$\text{price} = m_1 \times \text{area} + m_2 \times \text{bedrooms} + m_3 \times \text{age} + b$$

Each input (area, bedrooms, age) is called a **feature**, and each has its own personal coefficient ($m_1$, $m_2$, $m_3$) that says how much that specific feature pushes the price up or down, independent of the other features.

**The exercise the slides pose but don't answer**: predict the price for a couple of new houses with specific area/bedroom/age combinations. This note doesn't invent an answer for that either — with only 5 data points, one of them missing a value, there isn't enough clean information here to responsibly fit all four unknowns ($m_1$, $m_2$, $m_3$, $b$) by hand without just making something up. So this is left as an open question rather than a guessed-at number.

**Where this connects to the bigger picture**: this "add up several inputs, each with its own weight, plus a bias" formula is *exactly* the same computation a single neuron does inside a neural network (see the pre-activation formula from Lecture 9). Multiple linear regression is, in a real sense, the simplest possible neural network — just one neuron, with no squashing function applied at all.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab tak house-price example mein price predict karne ke liye sirf ek piece of information (area) use hua tha. Ye topic puchta hai: agar hum *kayi* pieces of information ek saath use karein — area, bedrooms ki sankhya, aur ghar ki age?

**Data par ek quick honest note**: is table ke paanch gharon mein se ek ka "bedrooms" value bilkul missing hai — bas blank chhod diya gaya hai. Slides ye explain nahi karti ki kyun ya iske baare mein kya karna hai, isliye ise yahan flag kiya ja raha hai chupchaap ignore ya guess karne ke bajaye. (Ye real datasets mein bahut common baat hai, aur ek poora alag topic — missing value handling — specifically isse deal karne ke liye exist karta hai; sibling MLT_Python project ki apni Lecture 6 mein ye depth mein cover kiya hai.)

**Model, extended**: ek slope ek input times plus ek bias ke bajaye, ab tumhare paas *teen* slopes hai, har input ke liye ek, sab add ho rahe hai, plus ek bias:

$$\text{price} = m_1 \times \text{area} + m_2 \times \text{bedrooms} + m_3 \times \text{age} + b$$

Har input (area, bedrooms, age) ko **feature** kehte hai, aur har ek ka apna personal coefficient hai ($m_1$, $m_2$, $m_3$) jo batata hai ki wo specific feature price ko kitna upar ya neeche push karta hai, doosre features se independent.

**Exercise jo slides puchti hai lekin answer nahi deti**: kuch naye gharon ke liye price predict karo, specific area/bedroom/age combinations ke saath. Ye note bhi iska answer invent nahi karta — sirf 5 data points ke saath, jinme se ek ka value missing hai, yahan itna clean information nahi hai ki hand se saare 4 unknowns ($m_1$, $m_2$, $m_3$, $b$) ko responsibly fit kiya ja sake bina kuch banaye. Isliye ise ek open question ki tarah chhoda ja raha hai, ek guessed-at number ke bajaye.

**Ye bade picture se kaise connect hota hai**: ye "kayi inputs add karo, har ek apne weight ke saath, plus ek bias" wala formula *exactly* wahi computation hai jo ek single neuron neural network ke andar karta hai (Lecture 9 ka pre-activation formula dekho). Multiple linear regression, ek real sense mein, sabse simple possible neural network hai — bas ek neuron, koi squashing function apply kiye bina.
