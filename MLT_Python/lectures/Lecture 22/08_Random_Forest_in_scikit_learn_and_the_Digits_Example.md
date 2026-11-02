# Topic 8: Random Forest in scikit-learn and the Handwritten-Digits Example

Source: Lecture 22, slides 17–19 (scikit-learn user-guide page "1.11 Ensembles: Gradient boosting, random forests, bagging, voting, stacking"; code `RandomForestClassifier().fit(X_train, y_train)`; "Identify hand written digits recognition" 8×8 image of a "4" with classes 0–9; last slide: forest photo "Random Forest — Credit: Alexander Fattal"). **The experiment numbers below were run by us** (scikit-learn digits dataset); the slides show only the code, not results.

---

## 1) Technical Explanation

**Slide 17 — ensemble methods (scikit-learn docs).** *Ensemble methods combine the predictions of several base estimators built with a given learning algorithm in order to improve generalisability / robustness over a single estimator.* The two famous examples named are **gradient-boosted trees** and **random forests**; more generally ensembles apply to any base learner via **bagging methods, model stacking, voting, or boosting (e.g. AdaBoost)**. Source: `scikit-learn.org/stable/modules/ensemble.html`.

**Slide 18 — the code.**
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
```
Three lines: import the class, create the model (defaults), train on the training data (`X_train` = feature matrix, `y_train` = labels). The displayed `RandomForestClassifier()` box is just the notebook echoing the fitted estimator. Prediction would be `model.predict(X_test)`.

**Slide 19 — the task: handwritten-digit recognition.** An **8×8 greyscale image** (64 pixel values, each pixel a feature) of a handwritten "4" is classified into one of the **10 classes 0–9** (from scikit-learn's digits dataset; the slide's source link is the `plot_digits_last_image` example). The arrow points the image to class "4".

**Verified experiment (ours).** scikit-learn digits: **1,797 images × 64 features, 10 classes**. Train/test split 75/25 (stratified, `random_state=42`).

| Model | Test accuracy |
|---|---|
| Single decision tree (fully grown) | **82.0%** (train accuracy 100% → overfit) |
| Random forest, 1 tree | 81.3% |
| Random forest, 10 trees | 94.4% |
| Random forest, 50 trees | 98.0% |
| **Random forest, default (100 trees)** | **97.8%** |
| Random forest, 200 trees | 97.6% |

- The default forest's **out-of-bag (OOB)** accuracy was **96.6%**, close to its test accuracy — OOB gives an honest estimate with no separate test set ([[05_Bagging_Bootstrap_Aggregation]]).
- Default hyper-parameters observed: `n_estimators = 100`, `max_features = "sqrt"` (√64 = 8 features per split, [[06_Feature_Randomness_Random_Subset_of_Features_per_Split]]).
- **Reading:** one deep tree overfits (100% train, 82% test); a **single** tree from the forest is similar (≈ 81%); **averaging many decorrelated trees** lifts accuracy to ~98%. Gains saturate after a few dozen trees; the small dip at 200 is random noise, not overfitting (differences of ±0.3 are a handful of test images out of 450).

**Practical hyper-parameters (general knowledge).** `n_estimators` (number of trees), `max_features`, `max_depth`/`min_samples_leaf` (control tree size), `bootstrap` (default True), `max_samples`, `oob_score`, `n_jobs` (parallelism), `random_state` (reproducibility). `model.feature_importances_` reports each feature's contribution — here, which pixels matter most.

**Typical workflow.** Load data → split train/test ([[05_k_Fold_Cross_Validation]] from Lecture 17 for more robust validation) → `fit` → `predict` → measure accuracy / confusion matrix ([[08_Confusion_Matrix_TP_TN_FP_FN]] from Lecture 17).

---

## 2) Simple English Explanation

**Slide 17 — what "ensemble" means.** The scikit-learn website (a popular Python toolbox for machine learning) explains: an **ensemble** combines the predictions of several simple models to get an answer that is more reliable than any single model. The two famous kinds are **random forests** and **gradient-boosted trees**; the same idea also works with bagging, voting, stacking and boosting in general.

**Slide 18 — the three lines of code.**
```python
from sklearn.ensemble import RandomForestClassifier   # 1) bring in the tool
model = RandomForestClassifier()                       # 2) create a forest
model.fit(X_train, y_train)                            # 3) teach it
```
- `X_train` = the table of examples (the columns/features); `y_train` = the correct answers for those examples.
- `fit` means "learn from these examples". The grey/blue box you see afterwards is just the notebook showing the trained forest.
- Afterwards you ask it for answers on new examples with `model.predict(...)`.

**Slide 19 — recognising handwritten digits.** The task: a computer must look at a tiny picture of a handwritten number and say which of the ten digits (0–9) it is. Each picture is an 8×8 grid of grey squares, so 64 numbers, one per square. The slide shows a "4" and an arrow pointing to the "4" box. (The last slide is just a photo of a forest.)

**We tried it ourselves (the slides show no results).** Using scikit-learn's built-in digits data — 1,797 pictures — and keeping a quarter aside for testing:
- **One fully-grown decision tree:** about **82%** right on the unseen pictures. (It was 100% right on the pictures it studied — a sign of overfitting.)
- **A forest of 10 trees:** about 94%.
- **A forest of 50 trees:** about 98%.
- **The default forest (100 trees):** about **98%** (97.8%).
- A forest of just **1 tree** got about 81%, similar to a single tree — it's the *crowd* that helps.
- The forest also estimated its own accuracy using the left-out pictures ("out-of-bag"): about 96.6%, close to the real test result.

**What this shows.** A crowd of different trees voting beats one big tree on the same data. After a few dozen trees the improvement levels off; small ups and downs (like 98.0 → 97.6) are just luck on a few of the 450 test pictures.

**Settings you can change (general knowledge).** Number of trees, how many columns each question may see, how deep trees may grow, how many to train in parallel, and a random seed for repeatable results. A trained forest can also tell you which pixels mattered most.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 17 — "ensemble" ka matlab.** scikit-learn website (machine learning ke liye ek mashhoor Python toolbox) samjhati hai: **ensemble** kai simple models ki predictions ko jodta hai taaki jawaab kisi bhi akele model se zyada bharosemand ho. Do mashhoor kisme **random forests** aur **gradient-boosted trees** hain; wahi idea bagging, voting, stacking aur boosting ke saath bhi chalta hai.

**Slide 18 — code ki teen line.**
```python
from sklearn.ensemble import RandomForestClassifier   # 1) tool laao
model = RandomForestClassifier()                       # 2) forest banao
model.fit(X_train, y_train)                            # 3) use sikhao
```
- `X_train` = examples ki table (columns/features); `y_train` = un examples ke sahi jawaab.
- `fit` ka matlab "in examples se seekho". Baad mein jo grey/neela box dikhta hai wo bas notebook trained forest dikha rahi hai.
- Baad mein naye examples par jawaab `model.predict(...)` se maangte hain.

**Slide 19 — haath se likhe digits pehchanna.** Kaam: computer ko haath se likhe number ki chhoti si picture dekh kar batana hai ki das digits (0–9) mein se kaun sa hai. Har picture 8×8 grey squares ki grid hai, yaani 64 numbers, har square ka ek. Slide ek "4" dikhati hai aur ek teer "4" wale box ki taraf. (Aakhri slide bas ek jungle ki photo hai.)

**Humne khud try kiya (slides mein koi results nahi).** scikit-learn ke built-in digits data (1,797 pictures) ke saath, aur ek-chauthai testing ke liye alag rakhkar:
- **Ek poora ugaya hua decision tree:** unseen pictures par lagbhag **82%** sahi. (Jin pictures se seekha unmein 100% sahi — overfitting ka sanket.)
- **10 trees ka forest:** lagbhag 94%.
- **50 trees ka forest:** lagbhag 98%.
- **Default forest (100 trees):** lagbhag **98%** (97.8%).
- Sirf **1 tree** ka forest lagbhag 81%, ek akele tree jaisa — madad *bheed* se hi hoti hai.
- Forest ne chhodi hui pictures ("out-of-bag") se apni accuracy ka andaza bhi lagaya: lagbhag 96.6%, asli test result ke kaafi paas.

**Isse kya dikhta hai.** Alag-alag trees ki bheed ka vote, usi data par ek bade tree ko hara deta hai. Kuch darjan trees ke baad sudhaar thama jata hai; chhote upar-neeche (jaise 98.0 → 97.6) 450 test pictures mein se kuch par bas kismat hai.

**Settings jo badal sakte ho (general knowledge).** Trees ki sankhya, har sawaal kitne columns dekh sake, trees kitne gehre ugein, kitne parallel train hon, aur repeatable results ke liye random seed. Trained forest ye bhi bata sakta hai ki kaun se pixels sabse zyada matter kiye.
