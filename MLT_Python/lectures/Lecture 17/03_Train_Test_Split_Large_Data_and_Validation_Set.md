# Topic 3: Evaluation on Large Data — Train/Test Split, the Three Steps, and the Validation Set

Source: Lecture 17, slides 6–10 ("Evaluation on LARGE data", "Model Evaluation Step 1/2/3" diagrams, "A note on parameter tuning"). Enriched with web research (data leakage, train/validation/test roles).

---

## 1) Technical Explanation

**Large data (slide 6).** If **many (thousands) of examples** are available, *a simple evaluation is sufficient*:
- **Randomly split** the data into training and test sets (e.g. **2/3 for train, 1/3 for test**).
- For classification, make sure training and testing have a **similar distribution of class labels**.
- **Build** a model using the train set and **evaluate** it using the test set.

**The three-step picture (slides 7–9).** The diagrams use a database cylinder ("Data"), a table of **Results Known** (the true answers, e.g. 0, 3, 2, 5, 1, …) and a "THE PAST" label (all this data comes from past, already-labelled cases):

1. **Step 1 – Split** the data into a **Training set** and a **Testing set**.
2. **Step 2 – Build a model** on the training set (the "Model Builder" box produces a model, drawn as a small decision tree).
3. **Step 3 – Evaluate on the test set:** the model produces **Predictions** (the blue column, e.g. 3, 4, 1, 2) for the held-out test cases; these are compared with the known results ("Evaluate" arrow) to compute the performance score.

The test set plays the role of **"the future"** — it must act like data the model has never seen.

**A note on parameter tuning (slide 10).**
- *It is important that the test data is **not used in any way** to build the model.*
- Some learning schemes work in **two stages**: Stage 1 builds the basic structure; Stage 2 **optimizes parameter settings** (for k-NN: the value of k and the distance metric — [[03_Issues_and_Choosing_the_Value_of_K]] from Lecture 16).
- *The test data can't be used for parameter tuning!* If you tune on the test set, the test score becomes an optimistic, "leaked" estimate.
- **Proper procedure uses three sets:**

| Set | Used for |
|---|---|
| **Training data** | fit the model's parameters/structure |
| **Validation data** | **optimize hyper-parameters** (choose k, pick between models) |
| **Test data** | final, one-time, unbiased estimate of performance |

**Worked example (illustrative).** 9,000 labelled emails: take 6,000 train / 1,500 validation / 1,500 test. Train k-NN with k = 1, 3, 5, 7 on the 6,000; pick the k with the best accuracy on the 1,500 validation emails (say k = 5); finally report the accuracy of that chosen model **once** on the 1,500 test emails. The 2/3–1/3 split of slide 6 corresponds to 6,000/3,000 if no validation set is needed.

**After tuning:** it is common to retrain the final chosen model on train + validation data before real-world use; the test estimate then refers to that procedure.

---

## 2) Simple English Explanation

If you have **lots of data** (thousands of examples), evaluation is easy:

1. **Shuffle and split** your examples: roughly **two-thirds to learn from** (training set), **one-third to be quizzed on** (test set). Make sure both piles have a similar mix of answers (for example, similar numbers of spam and non-spam).
2. **Teach** the model using only the training pile.
3. **Quiz** it on the test pile: let it guess, then compare its guesses with the real answers (you already know them).

The test pile pretends to be "the future."

**Important rule:** the test pile must stay **hidden** until the very end — you may not peek at it while designing the model. Many models have **settings you adjust** (like how many neighbors, k). If you adjust those settings by checking the test score, you are cheating: you've indirectly studied the exam.

So use **three piles**:
- **Training** – learn from it.
- **Validation** – use it to choose the best settings.
- **Test** – use it **once**, at the very end, for the honest final score.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Agar tumhare paas **bahut saara data** hai (hazaaron examples), to evaluation aasaan hai:

1. Data ko **shuffle karke do hisson mein baanto**: lagbhag **2/3 seekhne ke liye (training set)** aur **1/3 test ke liye (test set)**. Dhyaan rakho dono hisson mein classes ka mix similar ho (jaise spam aur non-spam dono ka ek jaisa ratio).
2. Model ko **sirf training set** se train karo.
3. **Test set par quiz lo**: model se prediction karwao aur uski guesses ko asli answers ("Results Known") se compare karo.

Slide 7–9 ke diagrams yahi 3 steps dikhate hain: Data → split → Model Builder → predictions → evaluate. Test set "future" ka kaam karta hai.

**Sabse zaroori rule:** test data ko model banane mein **kisi bhi tarah use mat karo.** Bahut se models mein **settings** hoti hain (jaise k-NN mein k). Agar tum test score dekh kar settings badalte ho, to ye cheating hai — jaise exam ke paper ko pehle se dekh liya.

Isliye **teen sets** use karte hain:
- **Training** – isse model seekhta hai.
- **Validation** – isse best settings (jaise k) chunte hain.
- **Test** – sabse end mein **sirf ek baar** use hota hai, honest final score ke liye.

Example: 9,000 emails → 6,000 train, 1,500 validation, 1,500 test. Validation par k = 1,3,5,7 try karo, jo best ho (maan lo k=5) use rakho, aur phir test set par ek baar score nikaalo.
