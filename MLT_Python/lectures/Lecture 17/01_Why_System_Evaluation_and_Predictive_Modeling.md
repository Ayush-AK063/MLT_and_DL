# Topic 1: Why Evaluate a Model? Predictive Modeling and Performance Evaluation

Source: Lecture 17, slides 1–4 ("Why System Evaluation?", "Regression / classification models", "Performance evaluation"). Enriched with web research (generalization, why training-set performance is optimistic).

---

## 1) Technical Explanation

**Why system evaluation? (slide 2).** There are many models/algorithms/systems — *which one is the best?* The slide asks the same question for each **component** of a system:
- the **similarity function** (cosine, correlation, …) — compare [[04_Distance_Metrics]] from Lecture 16;
- **term selection** (stop-word removal, stemming, …) and **term weighting** (TF, TF-IDF, …) — text-retrieval examples;
- and, for retrieval: *how far down the list will a user need to look to find some/all relevant documents?*

So evaluation is how we **compare choices** objectively instead of by intuition.

**Predictive modeling / supervised learning (slide 3).** *A model is a specification of the mathematical/probabilistic relationships that exist between different variables.* The goal is usually to use **existing data** to develop models that predict outcomes for **new data**. The slide's examples:

| Prediction task | Output type |
|---|---|
| Is an email spam or not? | Nominal (category, no order) → **classification** |
| Is a credit-card transaction fraudulent? | Nominal → classification |
| Which advertisement will a shopper most likely click? | Nominal → classification |
| Which football team will win the Super Bowl? | Nominal → classification |
| Predict the stock price of a company | Continuous → **regression** |
| Predict the number of buyers of a product | Continuous → regression |
| Predict user ratings of a new movie | Continuous/ordinal → regression |
| Predict the grade of a disease | Ordinal → regression/ordinal classification |

The slide's side annotations label the target types: **Nominal** (categorical with no particular order) vs. **Continuous / ordinal**. This is the same regression-vs-classification split from [[01_Linear_Regression_vs_Classification_and_Types]] from Lecture 15.

**Performance evaluation (slide 4).** *How predictive is the model we learned?*
- **Regression:** usually **R²** or **MSE** ([[07_Performance_Metrics_Overview_and_Regression_Metrics]]).
- **Classification:** *many options*; **accuracy can be used, with caution** ([[08_Confusion_Matrix_TP_TN_FP_FN]]).
- **Key warning:** *performance on the training data (data used to build models) is **not** a good indicator of performance on future data.*
- Q: Why? A: *Because new data will probably not be exactly the same as the training data!*

**Why training performance is misleading (explained).** A model can **memorize** its training examples — a 1-NN classifier ([[01_Nearest_Neighbor_Idea_and_Basic_Rule]] from Lecture 16) scores 100 % on its own training data because every point is its own nearest neighbor, yet may do poorly on new points. What we truly care about is **generalization error**: performance on unseen data. All the techniques in this lecture (train/test split, validation set, cross-validation, bootstrap) are ways to *estimate generalization performance honestly* — see [[02_Overfitting_vs_Underfitting_Bias_and_Variance]] for the underlying reason.

---

## 2) Simple English Explanation

Suppose you have several different models (or settings) and must pick one. You need a fair **scorecard** — that's "evaluation."

**Prediction tasks come in two flavours:**
- Predicting a **category** (spam / not spam, fraud / not fraud, which team wins): this is **classification**.
- Predicting a **number** (a stock price, how many people will buy, a movie rating): this is **regression**.

For numbers we usually score with **R² or MSE**; for categories there are many scores, and "accuracy" (percentage correct) is the simplest — but use it carefully.

**The big rule: never grade a model using the same questions it studied from.** Imagine a student who memorizes last year's exam answers. Ask the same questions again and they score 100 % — but that doesn't prove they understood anything. Real life brings *new* questions that are never exactly like the old ones. So we must test on data the model has **not seen** before.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Maan lo tumhare paas kai models hain aur ek chunna hai. Iske liye ek **fair scorecard** chahiye — isi ko "evaluation" kehte hain. Slide 2 yahi sawaal puchhti hai: "kaun sa model/algorithm/component sabse best hai?" (jaise similarity function cosine ya correlation, ya text mein stemming/TF-IDF).

**Prediction ke do tarah ke kaam:**
- **Category** predict karna (spam hai ya nahi, fraud hai ya nahi, kaun si team jeetegi) = **classification**. Ye "nominal" data hai (categories mein koi order nahi).
- **Number** predict karna (stock price, kitne log kharidenge, movie rating) = **regression**. Ye "continuous / ordinal" data hai.

Numbers ke liye aam taur par **R² ya MSE** use hota hai; categories ke liye bahut options hain, aur sabse simple **accuracy** (kitne % sahi) hai — par isse **dhyaan se** use karna hai.

**Sabse badi baat:** model ko usi data par kabhi mat parkho jisse usne seekha hai. Socho ek student ne pichle saal ke paper ke answers ratt liye. Wahi sawaal dobara aaye to 100% marks, par isse ye saabit nahi hota ki usne samjha. Asli zindagi mein **naye** sawaal aate hain jo purane se bilkul same nahi hote. Isliye hum model ko aise data par test karte hain jo usne pehle **kabhi dekha hi nahi**. (Jaise 1-NN apne training data par hamesha 100% deta hai, kyunki har point ka sabse paas wala neighbor wo khud hota hai — par naye data par fail ho sakta hai.)
