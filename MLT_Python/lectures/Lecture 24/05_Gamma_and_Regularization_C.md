# Topic 5: The Two Knobs: Gamma (γ) and Regularization (C)

Source: Lecture 24, slides 12–14:
- Slide 12: "Gamma & Regularization", with the handwritten note "Regularization → controls the trade-off between the model simplicity / training accuracy & overfitting".
- Slide 13: "High Gamma" vs "Low Gamma" scatter plots, handwritten "(non-linear kernels)".
- Slide 14: "High Regularization (C)" vs "Low Regularization (C)".

Enriched with the scikit-learn documentation ("RBF SVM parameters") and our own experiments on the two-moons dataset.

---

## 1) Technical Explanation

### Slide 12: why these knobs exist

The instructor's note says regularization "controls the trade-off between model simplicity, training accuracy and overfitting". An SVM with kernels can draw almost any boundary. **γ** and **C** decide how hard it tries to fit every training point. That is the bias–variance trade-off from [[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17.

### Gamma (γ): reach of each training point (slide 13)

γ belongs to the non-linear kernels, which is the handwritten note on slide 13. It matters most for the **RBF (Gaussian) kernel**:

  **K(x, z) = exp(−γ ‖x − z‖²)**

K measures the similarity between x and z. It is 1 when x = z and decays towards 0 with distance. **γ sets how fast it decays.** scikit-learn's docs put it this way: γ "defines how far the influence of a single training example reaches, with low values meaning 'far' and high values meaning 'close'". You can think of γ as the inverse of the radius of influence of each support vector.

**Numbers (our computation).** Kernel value K for points at distance d:

| γ | d = 0.5 | d = 1 | d = 2 | d = 3 |
|---|---|---|---|---|
| 0.1 | 0.975 | 0.905 | 0.670 | 0.407 |
| 1 | 0.779 | 0.368 | 0.018 | 0.0001 |
| 10 | 0.082 | ≈ 0 | 0 | 0 |

For example, x = (1, 2) and z = (3, 4) have ‖x − z‖² = 8. With γ = 0.5, K = e⁻⁴ = **0.0183**. With γ = 0.1, K = e^−0.8 = 0.449.

**Slide 13's picture.**
- **High γ:** only points **close** to the boundary influence it. The dashed lines in the figure are drawn only from nearby points. The boundary becomes **curvy** and wraps tightly around individual points. Training fit is high, but there is a risk of **overfitting**.
- **Low γ:** **far-away** points also have influence (dashed lines from many points). The boundary is **smooth, nearly straight**. Too low a γ **underfits** and behaves almost like a linear SVM.

### C: penalty on violations (slide 14)

C is the weight on the slack term in ½‖w‖² + C Σ ξᵢ ([[04_Choosing_the_Best_Hyperplane_Good_vs_Bad_Margin]]). scikit-learn's docs: C "trades off correct classification of training examples against maximization of the decision function's margin. A lower C will encourage a larger margin, therefore a simpler decision function, at the cost of training accuracy."

- **Large C:** violations are expensive. The model tries to classify every training point correctly, giving a narrow margin and a **wiggly** boundary (slide 14, left).
- **Small C:** violations are cheap. The model prefers a wide margin and a **simple, straight-ish** boundary and tolerates some errors (slide 14, right).

**⚠ Naming caution.** Slide 14 labels the wiggly plot "High Regularization (C)" and the straight plot "Low Regularization (C)". Read these as "**high C value**" and "**low C value**". In standard terminology C is the **inverse** of regularization strength: large C means *weak* regularization, so the model fits the data closely. Small C means *strong* regularization, so the model is simpler. The pictures are correct. Only the word "regularization" in the labels is ambiguous.

### Experiment (our own; two-moons data, 300 points, noise 0.3, 70/30 split, RBF kernel)

**Effect of γ (C = 1):**

| γ | 0.01 | 0.1 | 1 | **10** | 100 |
|---|---|---|---|---|---|
| Train accuracy | 0.829 | 0.848 | 0.933 | 0.957 | **0.990** |
| Test accuracy | 0.767 | 0.789 | 0.911 | **0.933** | 0.889 |
| # support vectors | 145 | 95 | 66 | 102 | 194 |

- Very small γ underfits: both accuracies are low and the boundary is nearly linear.
- Very large γ overfits: train accuracy rises to 99% while test accuracy falls to 88.9%, and almost every point becomes a support vector.

**Effect of C (γ = 1):**

| C | 0.01 | 0.1 | 1 | 10 | 100 | 1000 |
|---|---|---|---|---|---|---|
| Train accuracy | 0.519 | 0.900 | 0.933 | 0.948 | 0.952 | 0.952 |
| Test accuracy | 0.456 | 0.833 | 0.911 | 0.922 | 0.911 | 0.922 |
| # support vectors | 202 | 126 | 66 | 48 | 45 | 40 |

- Tiny C underfits badly: the margin is so wide that nearly every point is inside it.
- As C grows the margin narrows. Fewer points are support vectors, and training accuracy climbs.

**Tuning in practice.** Search over a log-scale grid, e.g. C ∈ {0.1, 1, 10, 100} and γ ∈ {0.001, …, 10}, using **cross-validation** ([[05_k_Fold_Cross_Validation]] from Lecture 17). scikit-learn's defaults are C = 1.0 and `gamma='scale'` = 1/(n_features × Var(X)). **Always scale the features first**, because ‖x − z‖ depends on units.

---

## 2) Simple English Explanation

**Slide 12: two dials.** An SVM with curved boundaries could bend itself around every single training point. That would look perfect on the training data but fail on new data (overfitting). The teacher's note says these settings "control the trade-off between keeping the model simple and getting training points right". There are two dials: **gamma** and **C**.

**Gamma: how far each point's "voice" carries (slide 13).**
- Imagine every training point is a lamp. Gamma decides the lamp's reach.
- **High gamma = small lamps.** Each point only lights up its immediate neighbourhood, so only points near the border matter. The border becomes very **curvy**, hugging individual points. That is great on training data and risky on new data.
- **Low gamma = big floodlights.** Every point influences a wide area, even far-away ones. The border becomes **smooth and almost straight**. Too low, and it can't capture any real curve.
- Numbers: with gamma = 1, two points 1 unit apart have similarity 0.37, and 2 units apart only 0.02. With gamma = 10, even points 1 unit apart have essentially zero similarity, so influence is very local.
- The teacher noted "(non-linear kernels)": gamma only matters when we use curved (kernel) boundaries.

**C: how strict the teacher is about mistakes (slide 14).**
- **High C = strict teacher.** Every training mistake is heavily punished, so the boundary twists to get every point right. The margin becomes narrow and the border wiggly.
- **Low C = relaxed teacher.** A few mistakes are fine if the boundary stays simple with a wide margin.
- **Careful with the slide's wording:** "High Regularization (C)" on the slide really means "a **high value of C**". In standard ML language, a high C actually means *less* regularization (less pressure to stay simple). The pictures are right; just read the labels as "high C" and "low C".

**Our experiment (moon-shaped data with noise):**
- **Gamma from tiny to huge:**
  - Test accuracy went 77% → 79% → 91% → **93%** → 89%.
  - At gamma = 100, training accuracy hit 99% but test accuracy dropped: classic overfitting.
  - At gamma = 0.01, both were low: underfitting.
- **C from tiny to huge:**
  - At C = 0.01 the model was useless (46% test), because it barely cared about mistakes.
  - From C = 1 upward it settled around 91–92%.
- **Lesson:** try several values of both dials and pick the best using cross-validation (Lecture 17). Always scale your features first.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 12: do dials (knobs).** Curved boundary wala SVM har training point ke around mud sakta hai. Training pe perfect dikhega, par naye data pe fail hoga (overfitting). Teacher ka note: regularization "**model ki simplicity aur training accuracy / overfitting ke beech ka balance control karta hai**". Do dials hain: **gamma (γ)** aur **C**.

**Gamma: har point ki "awaaz" kitni door tak jaati hai (slide 13).**
- RBF kernel ka formula: **K(x, z) = exp(−γ‖x − z‖²)**. Ye do points ki similarity hai: same point pe 1, door jaane pe 0 ki taraf.
- Socho har training point ek lamp hai, aur gamma uski roshni ki range hai.
- **High gamma = chhote lamp.** Har point sirf apne aas-paas ko roshan karta hai, isliye sirf border ke paas wale points matter karte hain (slide pe dashed lines sirf paas wale points se hain). Boundary bahut **ghumaavdaar** ban jaati hai aur har point se chipak jaati hai. Training pe badhiya, naye data pe risky (overfitting).
- **Low gamma = bade floodlight.** Door ke points bhi asar daalte hain. Boundary **smooth, lagbhag seedhi** hoti hai. Bahut kam gamma ho to curve pakad hi nahi paata (underfitting).
- Numbers:
  - γ = 1 pe 1 unit door ke points ki similarity 0.37, aur 2 unit door ki sirf 0.018.
  - γ = 10 pe 1 unit door bhi ≈ 0, yaani asar bahut local.
  - Example: (1,2) aur (3,4) ke beech ‖x − z‖² = 8. γ = 0.5 pe K = e⁻⁴ = **0.0183**.
- Teacher ne likha "(non-linear kernels)": gamma sirf curved (RBF/poly) kernels mein matter karta hai. Linear SVM mein gamma hota hi nahi.

**C: galtiyon pe kitni sakhti (slide 14).**
- Formula ½‖w‖² + C Σξ mein C galtiyon (slack) ka jurmana hai.
- **High C = sakht teacher.** Har training galti pe bhaari saza, isliye boundary mud-mud ke har point sahi karti hai. Margin patla, border wiggly.
- **Low C = relaxed teacher.** Thodi galtiyan chalegi, bas boundary simple aur margin chauda rahe.
- ⚠ **Slide ke words pe dhyan do:** "High Regularization (C)" ka matlab hai "**C ki value high**". Standard ML language mein high C = *kam* regularization hai (simple rehne ka dabaav kam), kyunki C regularization ka ulta (inverse) hai. Pictures sahi hain, bas labels ko "high C" aur "low C" padho.

**Humara experiment (noisy moon-shaped data, RBF kernel):**
- **Gamma badhaya (C = 1):**
  - Test accuracy: 0.01 → 76.7%, 0.1 → 78.9%, 1 → 91.1%, **10 → 93.3%**, 100 → 88.9%.
  - γ = 100 pe training 99% par test gir gaya: overfitting. Support vectors bhi 194 ho gaye, lagbhag har point.
  - γ = 0.01 pe dono kam: underfitting.
- **C badhaya (γ = 1):**
  - C = 0.01 pe model bekaar tha (test 45.6%), kyunki galtiyon ki parwaah hi nahi.
  - C = 1 se upar ~91–92% pe tik gaya. C badhne se support vectors kam hote gaye (202 → 40), kyunki margin patla hota gaya.
- **Seekh:**
  - Dono dials ki kai values try karo (jaise C = 0.1, 1, 10, 100 aur γ = 0.001 … 10) aur **cross-validation** (Lecture 17) se best chuno.
  - scikit-learn ke defaults: C = 1, gamma = 'scale'.
  - Features ko pehle **scale** zaroor karo, kyunki distance units pe depend karta hai.
