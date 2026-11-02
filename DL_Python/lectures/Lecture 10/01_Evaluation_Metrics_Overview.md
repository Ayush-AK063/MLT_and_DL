# Topic 1: Evaluation Metrics — Classification and Regression

Source: Lecture 10 (ES532: Introduction to Deep Learning), slides 5 ("Metrics") and 25. Enriched with web research on ROC/AUC and R².

---

## 1) Technical Explanation

Until now, this course has relied purely on the **cost function value** itself (the squared error from [[04_Formalizing_the_Learning_Problem_Data_Model_Parameters]] in Lecture 9) to judge a model. This topic introduces additional **quantitative metrics** that give a more complete, more interpretable picture of model quality, split into classification metrics and regression metrics.

### Classification Metrics

These all build on four basic counts for a binary classifier: **True Positives (TP)**, **False Positives (FP)**, **True Negatives (TN)**, **False Negatives (FN)** — i.e., how many predictions of each type (correct-positive, wrong-positive, correct-negative, wrong-negative) the model made.

1. **Accuracy** $= \dfrac{\text{No. of correct predictions}}{\text{Total no. of predictions}}$ — simplest metric, but can be misleading on imbalanced datasets (e.g., 95% accuracy is trivial if 95% of the data is one class).
2. **Precision** $= \dfrac{TP}{TP+FP}$ — of everything the model *called* positive, what fraction actually was positive? High precision means few false alarms.
3. **Recall (Sensitivity)** $= \dfrac{TP}{TP+FN}$, range $(0,1)$ — of everything that *actually was* positive, what fraction did the model catch? High recall means few missed positives.
4. **F1-score** $= 2 \times \dfrac{P \times R}{P+R}$ — the **harmonic mean** of Precision and Recall, giving one combined number that penalizes a model for being lopsidedly good at one but bad at the other (a harmonic mean, unlike a simple average, is pulled down heavily by whichever of the two is smaller).
5. **ROC curve and AUC** (named on slide 5, defined here via web research since the slide gives no formula): a **ROC curve** (Receiver Operating Characteristic curve) plots the **True Positive Rate** (= Recall) against the **False Positive Rate** ($FPR = \frac{FP}{FP+TN}$) as the model's classification threshold is swept across its full range. **AUC** (Area Under the [ROC] Curve) condenses that whole curve into one number between 0 and 1: it equals the probability that the model ranks a randomly chosen true positive example higher than a randomly chosen true negative one. AUC $=0.5$ means the model is no better than random guessing; AUC $=1.0$ means perfect separation between the classes.

### Regression Metrics

Using $y_j$ for the actual value, $\hat{y}_j$ for the predicted value, and $N$ for the number of data points:

1. **MAE (Mean Absolute Error)** $= \dfrac{1}{N}\sum_{j=1}^{N} |y_j - \hat{y}_j|$ — average absolute size of the error, in the same units as the target.
2. **MSE (Mean Squared Error)** $= \dfrac{1}{N}\sum_{j=1}^{N} (y_j - \hat{y}_j)^2$ — the same squared-error idea from the cost function in Lecture 9, just explicitly averaged and named as an evaluation metric here. Squaring penalizes large errors disproportionately more than small ones, compared to MAE.
3. **RMSE (Root Mean Squared Error)** $= \sqrt{\dfrac{1}{N}\sum_{j=1}^{N}(y_j-\hat{y}_j)^2} = \sqrt{\text{MSE}}$ — taking the square root brings the error back into the same units as the original target (MSE's units are "target units squared," which is hard to interpret directly).
4. **R² (coefficient of determination)** $= 1 - \dfrac{\sum_{j=1}^N (y_j-\hat{y}_j)^2}{\sum_{j=1}^N (y_j-\bar{y})^2}$, where $\bar{y}$ is the mean of the actual values. R² measures **what fraction of the variance in the target the model explains**, relative to a naive baseline that always predicts the mean $\bar{y}$. The slide's own annotation notes "closer to 1 [is better]": R²$=1$ means the model perfectly explains all variation in the target; R²$=0$ means the model does no better than always guessing the average; R² can even go negative if the model is worse than that naive baseline (via web research: a genuinely important caveat — a high R² is not automatically "good," since it can be inflated by overfitting or misleading depending on the data and transformations used, so it should be read alongside other diagnostics, not in isolation).

---

## 2) Simple English Explanation

So far, the only way this course has judged "is the model good?" is by looking at the raw cost function number. This topic introduces a fuller toolkit of ways to measure model quality — one set for classification problems (predicting a category), one set for regression problems (predicting a number).

**For classification**, everything builds on counting four outcomes: did the model correctly say "yes" (true positive), wrongly say "yes" (false positive), correctly say "no" (true negative), or wrongly say "no" (false negative)?
- **Accuracy**: what fraction of all predictions were correct overall. Simple, but can lie to you — if 95 out of 100 patients don't have a disease, a model that just always says "no disease" gets 95% accuracy while being completely useless.
- **Precision**: of everything the model flagged as positive, how much of that was actually correct? (Are its "yes" answers trustworthy?)
- **Recall**: of everything that was actually positive, how much did the model actually catch? (Did it miss a lot of real cases?)
- **F1-score**: one number that combines precision and recall, punishing a model that's great at one but terrible at the other.
- **ROC/AUC**: a way of measuring how well the model separates the two classes overall, across every possible "how confident do I need to be before I say yes" cutoff — summarized as one number (AUC) where 0.5 = no better than a coin flip, and 1.0 = perfect.

**For regression**, everything is about how far off the predicted number is from the real number:
- **MAE**: on average, how far off are the predictions (in plain, easy-to-understand units)?
- **MSE**: same idea, but squares each error first — so one big miss counts a lot more than several small misses.
- **RMSE**: MSE's square root — brings the error back into normal, easy-to-read units.
- **R²**: roughly, "what fraction of the pattern in the data did my model actually capture?" 1.0 means it captured everything perfectly; 0 means it's no better than just always guessing the average value; it can even go negative if it's doing *worse* than that. A high R² sounds great, but it's worth knowing it's not an automatic guarantee of a genuinely good model — it can be misleadingly high in some situations, so experienced practitioners check it alongside other metrics rather than trusting it blindly.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab tak, is course ne "model achha hai ya nahi" judge karne ka sirf ek tarika use kiya hai — raw cost function number dekh kar. Ye topic model quality measure karne ka ek fuller toolkit deta hai — ek set classification problems ke liye (category predict karna), ek set regression problems ke liye (ek number predict karna).

**Classification ke liye**, sab kuch 4 outcomes count karne par based hai: model ne sahi se "haan" bola (true positive), galat se "haan" bola (false positive), sahi se "na" bola (true negative), ya galat se "na" bola (false negative)?
- **Accuracy**: total predictions mein se kitna fraction sahi tha. Simple hai, lekin jhooth bol sakta hai — agar 100 mein se 95 patients ko disease nahi hai, to ek model jo bas hamesha "no disease" bolta hai use 95% accuracy mil jaayegi, jabki wo bilkul useless hai.
- **Precision**: model ne jo bhi positive flag kiya, usme se kitna actually correct tha? (Uske "haan" answers trustworthy hai kya?)
- **Recall**: jo actually positive tha, usme se model ne kitna actually pakda? (Kya usne bahut saare real cases miss kiye?)
- **F1-score**: ek number jo precision aur recall ko combine karta hai, ek model ko punish karta hai jo ek mein achha aur doosre mein bura hai.
- **ROC/AUC**: ye measure karne ka tarika ki model dono classes ko overall kitna achhe se separate karta hai, har possible "kitna confident hona chahiye bolne se pehle 'haan'" cutoff ke across — ek number (AUC) mein summarize kiya jaata hai jahan 0.5 = coin flip se behtar nahi, aur 1.0 = perfect.

**Regression ke liye**, sab kuch iske baare mein hai ki predicted number real number se kitna door hai:
- **MAE**: average mein, predictions kitni door hai (simple, easy-to-understand units mein)?
- **MSE**: same idea, lekin har error ko pehle square karta hai — isliye ek bada miss kai chhote misses se zyada count hota hai.
- **RMSE**: MSE ka square root — error ko wapas normal, easy-to-read units mein le aata hai.
- **R²**: roughly, "mere model ne data ke pattern ka kitna fraction actually capture kiya?" 1.0 ka matlab hai usne sab kuch perfectly capture kiya; 0 ka matlab hai wo hamesha average value guess karne se behtar nahi; ye negative bhi ho sakta hai agar wo us se *bura* kaam kar raha ho. Ek high R² sunne mein achha lagta hai, lekin jaanna zaroori hai ki ye automatically genuinely achhe model ki guarantee nahi hai — ye kuch situations mein misleadingly high ho sakta hai, isliye experienced practitioners ise doosre metrics ke saath check karte hai, blindly trust nahi karte.
