# Topic 8: SVM in scikit-learn: Code, Scaling, Tuning and Multiclass

Source: Research enrichment, not on the slides. It puts slides 3–19 into practice. References: scikit-learn `SVC` documentation (v1.9.1, run locally) and the "RBF SVM parameters" example. Every output below is from our own runs.

---

## 1) Technical Explanation

### (a) The 8-point example from Topic 3

```python
import numpy as np
from sklearn.svm import SVC

X = np.array([[3,1],[3,-1],[6,1],[6,-1],[1,0],[0,1],[0,-1],[-1,0]])
y = np.array([ 1, 1, 1, 1, -1, -1, -1, -1])

svm = SVC(kernel="linear", C=1e6)        # huge C ≈ hard margin
svm.fit(X, y)
print(svm.coef_, svm.intercept_)         # ≈ [[1. 0.]] ≈ [-2.]   -> hyperplane x1 = 2 (1.0005, -2.0011: C is huge, not infinite)
print(svm.support_vectors_)              # [[1,0],[3,1],[3,-1]]
print(svm.dual_coef_)                    # ≈ [[-0.5, 0.25, 0.25]]  (alpha_i * y_i)
print(svm.decision_function([[2.5, 0]])) # ≈ [0.5]  -> positive side, 0.5/||w|| = 0.5 from the line
print(svm.predict([[2.5, 0]]))           # [1]
```

These outputs match the hand derivation in [[03_Support_Vectors_Margin_Hard_and_Soft_Margin]]. `coef_` (that is, w) exists only for the linear kernel. With RBF the model is Σ αᵢyᵢK(xᵢ, x) + b, and there is no explicit w.

### (b) A real dataset: breast cancer (slide 22, "Cancer Detection")

The Wisconsin breast-cancer data has 569 tumours, 30 numeric features, and 212 malignant vs 357 benign cases. We used a stratified 75/25 split.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

model = make_pipeline(StandardScaler(), SVC(kernel="rbf"))   # scale INSIDE the pipeline
model.fit(Xtr, ytr)
print(model.score(Xte, yte))
```

| Model | Test accuracy |
|---|---|
| `SVC()` (RBF) on **raw, unscaled** features | 0.923 |
| `StandardScaler` + `SVC()` (RBF) | **0.979**, with 96 support vectors (50 + 46) out of 426 training points |
| `StandardScaler` + `SVC(kernel='linear')` | 0.986 |
| Grid search (5-fold CV) over C ∈ {0.1, 1, 10, 100} and γ ∈ {'scale', 0.001, 0.01, 0.1, 1} | best C = 10, γ = 0.001; CV score 0.977; test 0.979 |

Three lessons:
1. **Scaling** adds about 5.6 percentage points here.
2. A **linear** kernel is already excellent on this data, so try the simple kernel first.
3. **Tune C and γ** with cross-validation ([[05_k_Fold_Cross_Validation]] from Lecture 17).

Put the scaler inside the pipeline. That way it is fit only on training folds, and no test information leaks into training.

```python
grid = GridSearchCV(make_pipeline(StandardScaler(), SVC()),
                    {"svc__C": [0.1, 1, 10, 100], "svc__gamma": ["scale", 0.001, 0.01, 0.1, 1]},
                    cv=5).fit(Xtr, ytr)
print(grid.best_params_, grid.score(Xte, yte))
```

### (c) Multiclass: handwritten digits (slide 22, "Hand Written Detection")

On the digits data (1,797 images of 8×8 pixels, classes 0–9, 75/25 split), `SVC()` gives **99.1%** test accuracy, using 619 support vectors out of 1,347 training images. For comparison, the best random forest in Lecture 22 got 98.0% on the same dataset ([[08_Random_Forest_in_scikit_learn_and_the_Digits_Example]] from Lecture 22). The splits differ, so compare loosely.

An SVM is inherently **binary**. scikit-learn's `SVC` handles K classes by **one-vs-one**:
- It trains K(K−1)/2 binary SVMs, one per pair of classes. For 10 digits that is 10·9/2 = **45** classifiers. Our run confirmed a 45-column decision function with `decision_function_shape='ovo'`.
- Prediction is by majority vote over the 45 classifiers.
- By default the decision values are reported in one-vs-rest shape (10 columns).
- `LinearSVC` uses one-vs-rest instead: K classifiers, each "class k vs all others".

### (d) Key parameters of `SVC` (defaults in scikit-learn 1.9.1)

| Parameter | Default | Meaning |
|---|---|---|
| `kernel` | `'rbf'` | `'linear'`, `'poly'`, `'rbf'`, `'sigmoid'`, or a custom function ([[06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick]]) |
| `C` | 1.0 | penalty on margin violations. Large C → narrow margin and less regularization ([[05_Gamma_and_Regularization_C]]) |
| `gamma` | `'scale'` = 1/(n_features · X.var()) | reach of each point for rbf/poly/sigmoid |
| `degree`, `coef0` | 3, 0.0 | the d and r of the polynomial kernel (γ x·z + r)^d |
| `class_weight` | None | `'balanced'` raises C for rare classes (useful for imbalanced data, Lecture 18) |
| `probability` | off | turn on Platt-scaled probabilities, at a slower speed |

**Related estimators:**
- `LinearSVC`: fast linear SVM for large n.
- `SVR`: regression ("SVMs … for classification and regression", slide 3).
- `OneClassSVM`: novelty and outlier detection.

### (e) SVM vs earlier classifiers in this course

| | k-NN (L16) | Decision tree / Random forest (L20–22) | SVM (L24) |
|---|---|---|---|
| Boundary | local, by neighbours | axis-aligned splits / their average | maximum-margin hyperplane (curved via kernels) |
| Training | none (lazy) | greedy splits / bagging | convex QP, global optimum |
| Needs scaling? | yes | no | **yes** |
| Main knobs | k, distance metric | depth, n_estimators, max_features | kernel, C, γ |
| Stores at prediction | all training points | trees | support vectors only |

---

## 2) Simple English Explanation

**Using SVM in Python takes only a few lines:**
1. Create the model: `SVC(kernel="rbf")` (or `"linear"`, `"poly"`).
2. Train it: `model.fit(X_train, y_train)`.
3. Predict: `model.predict(X_new)`. Or check accuracy: `model.score(X_test, y_test)`.

**Our small example from Topic 3.**
- Python found the dividing line x₁ = 2 with support vectors (1,0), (3,1) and (3,−1), exactly what we worked out by hand.
- For a new point (2.5, 0) it says "+1". The point is 0.5 units on the plus side of the line.

**A real medical test: breast-cancer data** (569 tumours, 30 measurements each).
- Without scaling the features: **92.3%** correct.
- With scaling: **97.9%**. Scaling matters a lot for SVM, because measurements come in very different units.
- A simple straight-line (linear) SVM did even better: **98.6%**. Always try the simple option first.
- Letting the computer try 20 combinations of C and gamma with cross-validation picked C = 10 and gamma = 0.001, which also gave 97.9%.
- Put the scaler and the SVM into one "pipeline" so the scaler only ever learns from training data, never from the test data.

**Handwritten digits (0–9).**
- SVM scored **99.1%**, slightly better than the random forest of Lecture 22 (98.0%), though on a different random split.
- An SVM can only separate **two** classes at a time. For 10 digits, Python quietly trains **45 mini-SVMs**, one for every pair (0 vs 1, 0 vs 2, …, 8 vs 9), and lets them vote.

**The main settings:**
- **kernel**: the shape of boundary (straight, polynomial, RBF).
- **C**: how strict about training mistakes.
- **gamma**: how far each point's influence reaches.
- Defaults are RBF, C = 1 and gamma = "scale".
- Related tools:
  - **LinearSVC**: fast, for huge data.
  - **SVR**: predicts numbers instead of classes.
  - **OneClassSVM**: finds unusual points.

**How SVM compares with earlier methods:**
- **k-NN** remembers every training point and asks the neighbours.
- **Trees and forests** ask yes/no questions about features.
- **SVM** draws the widest possible road between the classes and remembers only the points on the road's edges. Like k-NN, it needs scaled features. Trees don't.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Python mein SVM sirf 3 lines ka kaam hai:**
1. Model banao: `SVC(kernel="rbf")` (ya `"linear"`, `"poly"`).
2. Train karo: `model.fit(X_train, y_train)`.
3. Predict karo: `model.predict(X_new)`, ya accuracy dekho: `model.score(X_test, y_test)`.

**Topic 3 wala chhota example.**
- `SVC(kernel="linear", C=1e6)` ne diya:
  - `coef_` = [1, 0] aur `intercept_` = −2, yaani line **x₁ = 2**.
  - Support vectors (1,0), (3,1), (3,−1). Bilkul humare haath wale jawaab jaisa.
- Naya point (2.5, 0): decision value **+0.5**, to prediction **+1**. Line se 0.5 unit plus side pe.
- `coef_` (w) sirf linear kernel mein milta hai. RBF mein model Σ αᵢyᵢK(xᵢ, x) + b hota hai, alag se w nahi hota.

**Real medical data: breast cancer** (569 tumours, 30 measurements, slide 22 ka "Cancer Detection").
- Bina scaling RBF SVM: **92.3%**.
- `StandardScaler` + RBF SVM: **97.9%**. Sirf scaling se ~5.6% ka fayda! Support vectors sirf 96 (426 mein se).
- Scaling + **linear** SVM: **98.6%**. Simple option pehle try karo.
- GridSearchCV (5-fold) ne C ∈ {0.1, 1, 10, 100} aur γ ∈ {scale, 0.001, 0.01, 0.1, 1} mein se best **C = 10, γ = 0.001** chuna. Test pe 97.9%.
- Scaler ko SVM ke saath **pipeline** mein daalo, taaki scaler sirf training data se seekhe aur test data ki jaankari leak na ho.

**Handwritten digits (0–9), slide 22 ka "Hand Written Detection".**
- SVM ne **99.1%** score kiya. Lecture 22 ka random forest 98.0% tha (split alag tha, isliye roughly compare karo).
- SVM ek baar mein sirf **do classes** alag kar sakta hai. 10 digits ke liye scikit-learn chupchaap **45 chhote SVMs** banata hai: har jodi ke liye ek (0 vs 1, 0 vs 2, …, 8 vs 9), kyunki 10×9/2 = 45. Phir voting hoti hai. Ise **one-vs-one** kehte hain.
- `LinearSVC` **one-vs-rest** use karta hai: har class vs baaki sab, yaani 10 classifiers.

**Main settings (defaults):**
- `kernel='rbf'`: boundary ki shape.
- `C=1.0`: galtiyon pe kitni sakhti. Bada C = patla margin = kam regularization.
- `gamma='scale'`: har point ka asar kitni door tak.
- `degree=3`: polynomial kernel ki degree.
- `class_weight='balanced'`: chhoti class ko zyada weight (imbalanced data ke liye, Lecture 18).
- `probability=True`: probability chahiye to on karo (slow).
- Aur tools:
  - **LinearSVC**: bade data ke liye tez.
  - **SVR**: numbers predict karne ke liye (slide 3 ka "regression").
  - **OneClassSVM**: anokhe (outlier) points dhoondhne ke liye.

**Pichhle classifiers se tulna:**
- **k-NN (L16)**: saare training points yaad rakhta hai aur padosiyon se poochta hai. Scaling chahiye.
- **Tree / Forest (L20–22)**: features pe haan/na sawaal poochta hai. Scaling nahi chahiye.
- **SVM (L24)**: classes ke beech sabse chaudi sadak banata hai aur sirf kinare wale points (support vectors) yaad rakhta hai. Training convex hai, to ek hi best answer. k-NN ki tarah **scaling chahiye**. Knobs: kernel, C, γ.
