# Topic 1: Classification — A Two-Step Process

Source: Lecture 9, slide 2 (Classification - A Two-Step Process).

---

## 1) Technical Explanation

Building and using a classifier is formally split into two distinct steps: **Model Construction** and **Model Usage**.

**Step 1 — Model Construction**: describing a set of predetermined classes.
- Every **tuple/sample** (a single row/record of data) in the dataset is assumed to already belong to one predefined class, and this is determined by a special attribute called the **class label attribute**.
- The set of tuples used for model construction is called the **training set**.
- The resulting model can be represented in several forms: **classification rules** (if-then statements), **decision trees** (see [[06_Decision_Tree_Classification_and_Induction]]), or **mathematical formulae** (e.g., the weights of a linear/logistic model).

**Step 2 — Model Usage**: applying the constructed model to classify future or unknown objects.
- Before deploying the model, its **accuracy must be estimated**:
  - A separate labelled dataset (the **test set**) is used. The model's predicted label for each test tuple is compared against that tuple's *known, true* label.
  - **Accuracy rate** = the percentage of test-set samples the model classifies correctly.
  - Critically, **the test set must be independent of the training set** — if the same data used to build the model is also used to evaluate it, the estimated accuracy will be misleadingly high. This failure mode is called **overfitting** (the model has essentially "memorized" the training data rather than learned a generalizable pattern — see the deeper treatment in [[03_Bias_and_Variance]] and [[04_Addressing_Overfitting_and_Underfitting]]).
- **If the accuracy is acceptable**, the model is then used to classify genuinely new data whose true labels are unknown.

This two-step framework — construct on a training set, validate on an independent test set, then deploy — is the foundational workflow for *every* supervised classification algorithm covered later in the course (decision trees, Bayesian classifiers, k-NN, SVMs, etc.). It is also the conceptual seed for the more refined **train / validation / test** three-way split covered next ([[02_Training_Validation_and_Test_Sets]]), where a third partition (validation) is introduced specifically to tune the model without contaminating the final, one-time test evaluation.

---

## 2) Simple English Explanation

Making a classifier that actually works involves two separate stages — think of it like studying for an exam and then taking the exam.

**Stage 1 — Building the model (studying)**:
- You start with a bunch of examples where you already know the correct answer (the "class label") — like flashcards with the answer written on the back.
- This set of examples is called the **training set** — it's what the model learns from.
- After learning, the model can express what it learned as a set of simple rules, a decision tree (a flowchart of yes/no questions), or a mathematical formula.

**Stage 2 — Using the model (taking the exam)**:
- Before you trust the model with real, unknown cases, you need to check how good it actually is.
- You do this with a **test set** — a different batch of examples (that the model has never seen before) where you *do* know the right answers, but you hide them from the model and see how many it gets right.
- **Accuracy** = what percentage of the test set the model got right.
- Very important rule: **never test the model on the same data it trained on** — that's like grading a student using the exact same questions they memorized answers for. It would look like the student (model) is a genius, but they'd fail on any new question. This trap is called **overfitting**.
- If the accuracy on this fair test looks good enough, only *then* do you let the model loose on brand-new, real-world data where nobody knows the answer yet.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek achha classifier banane mein 2 alag stages hote hai — jaise exam ki taiyari karna aur fir exam dena.

**Stage 1 — Model banana (padhai karna)**:
- Tumhare paas kuch examples hai jinka sahi jawab pehle se pata hai (unka "class label") — jaise flashcards jinke peeche jawab likha hota hai.
- Ye examples ka set **training set** kehlata hai — isi se model seekhta hai.
- Seekhne ke baad, model apni learning ko simple rules, ek decision tree (yes/no sawaalon ka flowchart), ya ek mathematical formula ke roop mein express kar sakta hai.

**Stage 2 — Model use karna (exam dena)**:
- Model ko real, unknown cases par bharosa karne se pehle, check karna padta hai ki wo actually kitna achha hai.
- Iske liye ek **test set** use karte hai — ek alag batch of examples (jo model ne kabhi nahi dekhe), jinke sahi jawab humein pata hai lekin model se chhupaye jaate hai, aur dekhte hai model kitne sahi karta hai.
- **Accuracy** = test set ka kitna percentage model ne sahi kiya.
- Bahut important rule: **model ko kabhi bhi wahi data pe test mat karo jispe usne training ki thi** — ye aisa hai jaise ek student ko usi exact question paper se grade karna jo usne ratta maara tha. Isse lagega ki student (model) genius hai, lekin koi bhi naya sawaal aane par fail ho jayega. Is trap ko **overfitting** kehte hai.
- Agar is fair test mein accuracy achhi lage, tabhi model ko real-world ke bilkul naye data par chhoda jaata hai jahan kisi ko jawab pata nahi hai.
