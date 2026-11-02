# Topic 1: Linear Regression vs. Classification, and Classification Types

Source: Lecture 15, slides 1–6 (title slide recap of y=mx+c, Linear Regression vs. Classification, "Logistic regression is one of the techniques used for classification," Classification Types).

---

## 1) Technical Explanation

**Opening recap (slide 1).** The title slide restates the familiar straight-line vocabulary one more time before extending it: **y = mx + c**, where y is the **target variable**, x is the **input/output (I/P) feature**, m is the **slope**, and c is the **intercept**. It also restates the general multiple-regression form **y = m₁x₁ + m₂x₂ + … + mₙxₙ + c** from [[01_Multiple_Linear_Regression_Definition_and_General_Form]] in Lecture 14. This sets up the contrast the lecture is about to draw: everything up to this point (Lectures 13–14) predicted a **number**. This lecture is about predicting a **category** instead.

**Linear Regression vs. Classification (slides 2–3).** The slide draws a direct, explicit contrast between two families of supervised learning problems:

| | **Linear Regression** | **Classification** |
|---|---|---|
| Example problems | Home prices, weather, stock price | Is an email spam or not? Will a customer buy life insurance? Which party will a person vote for (BJP / Congress / Independent)? |
| Predicted value | **Continuous** | **Categorical** |

This is the single most important distinction in this lecture: a linear regression model outputs *any real number* (₹550,000, or 23.6°C, or ₹1,842.17) — there's no natural upper or lower bound, and "in-between" answers make sense. A classification model outputs *one label from a fixed, finite set of categories* (Yes/No, or BJP/Congress/Independent) — there is no meaningful "in-between" a Yes and a No.

**Where logistic regression fits (slide 4).** The slide states this plainly: **"Logistic regression is one of the techniques used for classification."** This is worth pausing on, because the name is actively misleading — despite having "regression" in its name (and despite being built, as this lecture will show, directly on top of the linear regression equation), logistic regression is a **classification** algorithm, not a regression algorithm in the "predict a continuous number" sense. (This exact point was flagged as research enrichment already in [[04_Types_of_Regression_Models_Overview]] from Lecture 13; this lecture now builds the full mechanism behind that one-line definition.)

**Classification Types (slides 5–6).** Two sub-categories of classification are introduced, distinguished purely by how many possible output labels exist:

- **Binary Classification** — exactly **two** possible outcomes. Example: "Will customer buy life insurance?" → Yes / No.
- **Multiclass Classification** — **three or more** possible outcomes. Example: "Which party is a person going to vote for?" → BJP / Congress / Independent.

This lecture's main worked example (covered in [[02_Why_a_Straight_Line_Fails_for_Classification_Worked_Example]] and [[03_The_Sigmoid_Function_and_Decision_Boundary]]) is a binary classification problem. Multiclass classification is introduced conceptually later in the lecture (see [[04_Multiclass_Classification_and_Handwritten_Digit_Recognition]]) via a handwritten-digit-recognition example (10 possible output classes: the digits 0–9).

---

## 2) Simple English Explanation

Everything you've learned in the last two lectures — predicting house prices, predicting plant weight — has one thing in common: the answer is always **a number**, and that number could theoretically be anything: ₹550,000 or ₹550,001 or ₹550,001.37, it doesn't matter, any number is a valid answer. This is called **Linear Regression**, and the slide gives more examples of this pattern: predicting weather, predicting stock prices — all of these give you back a number that can be anything on a continuous scale.

This lecture introduces a totally different kind of question: instead of "how much/how many," it's "which one, out of a short fixed list." Examples from the slide:
- Is this email spam, or not spam?
- Will this customer buy life insurance — yes or no?
- Which political party will this person vote for — BJP, Congress, or Independent?

Notice: you can't answer "will they buy insurance?" with "₹0.37 of insurance" — the answer has to be exactly "Yes" or exactly "No," nothing in between makes sense. This kind of problem — picking one label out of a fixed set of categories — is called **Classification**.

**Logistic Regression, despite its confusing name, is actually a classification tool, not a "predict-a-number" tool.** The name has "regression" in it purely because of how it's built internally (you'll see in the next topics that it literally starts from the same straight-line formula as regular regression) — but what it actually outputs at the end is a category (like Yes/No), not a number.

**Two types of classification, based on how many categories you're choosing between:**
- **Binary Classification**: exactly 2 choices. "Will they buy insurance?" → Yes or No. This is the type worked through in detail in this lecture.
- **Multiclass Classification**: 3 or more choices. "Which party will they vote for?" → BJP, Congress, or Independent (3 choices). This lecture also briefly shows a bigger example later: recognizing a handwritten digit, where there are 10 possible answers (0 through 9).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Pichle do lectures mein jo bhi seekha — ghar ki price predict karna, plant ka weight predict karna — sabme ek common cheez hai: answer hamesha **ek number** hota hai, aur wo number theoretically kuch bhi ho sakta hai: ₹550,000 ya ₹550,001 ya ₹550,001.37, farak nahi padta, koi bhi number valid answer hai. Isko **Linear Regression** bolte hain, aur slide isi pattern ke aur examples deti hai: weather predict karna, stock price predict karna — yeh sab ek continuous scale pe koi bhi number wapas dete hain.

Yeh lecture ek bilkul alag tarah ka sawaal introduce karti hai: "kitna/kitne" ki jagah, "konsa ek, ek short fixed list mein se." Slide ke examples:
- Yeh email spam hai, ya nahi?
- Kya yeh customer life insurance kharidega — haan ya na?
- Yeh insaan kis political party ko vote karega — BJP, Congress, ya Independent?

Notice karo: "kya wo insurance kharidenge?" ka jawab "₹0.37 ka insurance" nahi ho sakta — answer bilkul "Haan" ya bilkul "Na" hona chahiye, beech mein kuch nahi. Is tarah ke problem — ek fixed set of categories mein se ek label choose karna — usko **Classification** bolte hain.

**Logistic Regression, uske confusing naam ke bawajood, actually ek classification tool hai, "number predict karo" wala tool nahi.** Naam mein "regression" isliye hai kyunki yeh andar se kaise banaya gaya hai (agle topics mein dikhega ki yeh literally wahi straight-line formula se shuru hota hai jo regular regression mein tha) — lekin end mein yeh jo output deta hai wo ek category hai (jaise Yes/No), number nahi.

**Classification ke do types hain, kitne categories mein se choose kar rahe ho uske hisaab se:**
- **Binary Classification**: bilkul 2 choices. "Kya wo insurance kharidenge?" → Haan ya Na. Yehi type is lecture mein detail mein worked through hai.
- **Multiclass Classification**: 3 ya zyada choices. "Kis party ko vote karenge?" → BJP, Congress, ya Independent (3 choices). Yeh lecture aage ek aur bada example bhi briefly dikhati hai: handwritten digit ko recognize karna, jahan 10 possible answers hain (0 se 9 tak).
