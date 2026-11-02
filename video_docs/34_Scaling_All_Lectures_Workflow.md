# 34 · Scaling: Saare Lectures ke Liye Repeatable Workflow

> **Is file mein:** Pilot ke baad 22 MLT lectures (aur baad mein DL) ko efficiently banane ka workflow: batching, per-lecture checklist, component library ka growth, feedback loop, aur naye lecture aane par kya karna hai.

---

## 1. Scale ka hisaab (rough)

| | Value (estimate) |
|---|---|
| MLT lectures | 22 (L1–L22; L11 aur L12 ek combined folder hain) |
| Topic files (2026-10-18 count) | **~155** (`lectures/` mein 177 `.md` files, jinme 22 README hain) |
| Topics per lecture | 4–11 |
| Avg topic video | ~8–12 min (recap/short topics 3–5 min) |
| Total content | ~20–30 ghante video (estimate) |
| Frames @30fps | ~2.2–3.2 million |

> Ye scale batata hai ki **automation + reuse** zaroori hai. Har topic ko pilot jaisi care dena possible nahi; pipeline ko itna reliable banana padega ki zyadatar kaam automatic ho.

---

## 2. Per-lecture workflow (pilot ke baad)

```
Day 1 (Claude Code session):
  ├─ Saare topics ke outlines (Pass 1)  → 👤 batch review (30–60 min)
  ├─ Full scripts (Pass 2 + 3)           → validate + verify (auto)
  └─ 👤 Script spot-review (har topic ka hook + worked example)

Day 1 night (GPU batch):
  └─ normalize → TTS → audio QC → align   (saare topics)

Day 2 (Claude Code session):
  ├─ Naye components (agar lecture mein naya visual type hai)
  ├─ Scene code generation (saare topics) → static checks → previews
  └─ Critic loop (auto) → 👤 sirf flagged scenes

Day 2 night (CPU batch):
  └─ Final renders (parallel) → cards → assemble

Day 3:
  ├─ 👤 Watch-through (1.5–2×) har topic + G7 checklist
  ├─ Fixes → re-render only changed scenes
  └─ Publish (unlisted → feedback → public) + site embed
```
**Target:** Ek lecture ≈ 2–3 din (pilot ke baad, library mature hone par).

> 💰 **Budget mode (Mac) mein same flow:** Day 1 script + actions (Claude subscription ya Ollama) → `validate_actions()`; raat ko TTS (Mac); Day 2 code generation step **nahi hai** (templates), sirf previews + layout audit; raat ko render (`caffeinate -i`, 8–10 workers). Cost per lecture ≈ ₹20–50 (bijli). [42](42_Budget_Mode_Zero_Cost_Plan.md) §5.

---

## 3. Component library growth plan

Har lecture group ke naye visual needs:

(Topics `lectures/` folder ki actual files se liye gaye hain, 2026-10-18.)

| Lectures | Topics (actual notes se) | Naye components |
|---|---|---|
| L1–L3 | Course intro, What is ML, features/labels, Iris case study, AI/ML/DL hierarchy, history of AI, applications (CV, NLP, RL, robotics), supervised/unsupervised | `DatasetCard`, `ScatterPlot2D` (Iris), `HierarchyDiagram` (AI⊃ML⊃DL), `Timeline` |
| L4–L5 | RL basics, perceptron (pass/fail example, architecture, linear separability, weights/bias), logic gates OR/AND, types of data | `PerceptronDiagram` (inputs → weights → sum → step), `DecisionLine2D`, `TruthTable` |
| L6–L8 | Data preprocessing: quality, cleaning, missing values (imputation), noisy data, integration/correlation, scaling (min-max, z-score, decimal, log, MaxAbs, robust), discretization/binning, concept hierarchy | `ColumnTransform` (before/after values), `NumberLine` scaling, `BinningViz`, `MissingCellFill` |
| L9 | Classification overview, train/val/test, bias–variance, over/underfitting, decision tree intro | `SplitBar` (train/val/test), `BiasVarianceTarget` (dartboard), `FitCurves` |
| L10 | Dimensionality reduction, curse of dimensionality, feature selection (filter/wrapper/embedded), redundancy, Euclidean/Jaccard/Cosine examples, PCA/SVD/LDA intro | `DistanceViz`, `JaccardVenn`, `CosineAngle`, `DimensionGrow` (1D→2D→3D) |
| L11–12 | Feature selection worked example, PCA intuition + step-by-step + covariance/eigen worked example | `CovarianceMatrix`, `EigenArrows`, `ProjectionViz` (PCA shadow) |
| L13–L14 | Regression: simple/multiple linear (home prices), least squares (exam grades), normal equation (matrix approach) | `RegressionLine` + residuals, `MatrixOps` (XᵀX etc.) |
| L15 | Logistic regression: why line fails, sigmoid, decision boundary, multiclass, exam-pass probability | `SigmoidPlot`, `ThresholdLine` |
| L16 | KNN: idea, lazy learning, choosing K, distance metrics, movie genre + paper tissue examples, scaling | `KNNNeighbors` (circle grow, vote count) |
| L17 | Evaluation: holdout, stratified, k-fold CV, bootstrap/OOB, regression metrics, confusion matrix | `KFoldBlocks`, `ConfusionMatrix` |
| L18 | Accuracy/precision/recall/F1, retrieval Venn, man-vs-woman exercise, rates table | `MetricFormulaCard`, `PrecisionRecallVenn` |
| L19 | ROC, AUC, PR curves, 2 worked examples (trapezoid AUC 0.64), Youden J | `ROCCurve` (threshold slider), `AUCShade` (trapezoids) |
| L20–L21 | Decision trees, entropy, information gain, ID3 full worked example (PlayTennis), final tree | `TreeDiagram`, `BallBox`, `HighlightTable`, `BarCompare` ✅ (pilot) |
| L22 | Random forest, wisdom of crowd (phone + 3 friends), bootstrap, bagging, feature randomness, bagging vs boosting, sklearn digits experiment | `BootstrapSampler`, `ForestVote`, `AccuracyCompare` (82.0% vs 97.8%) |

**Rule:** Naya component tab banao jab **2+ topics** mein use hoga. One-off visual scene code mein hi theek hai.

**Budget mode mein:** Har naya component ek **template action** bhi banta hai ([41](41_Template_Engine_Zero_Cost_Animation.md) §8), taaki agle lectures mein wo visual bina code ke JSON se use ho sake. Target: har lecture ke saath template coverage badhe, aur custom-code scenes 10–20% se neeche rahein.

---

## 4. Feedback loop (har lecture ke baad)

```
qa_report.json (human_notes, critic issues, fix rounds)
        │
        ▼  monthly / per-lecture retro
   ├─ Script prompt update (jo galtiyan baar-baar aayi)
   ├─ Coder prompt update + golden examples refresh
   ├─ pronunciation.yaml mein naye words
   ├─ Component bugs fix + visual tests
   └─ video_docs update (ye folder!)
```
Prompt versions ko `prompts/` mein version header ke saath rakho, aur har video ke `manifest.json` mein version likho, taaki pata rahe kaun sa video kis version se bana.

---

## 5. Naya lecture aane par (MLT ya DL)

Abhi workflow hai: naya lecture PDF → notes (3 styles) → site + chatbot rebuild. Video ke liye isme ek step aur add hota hai:

```
1. Lecture PDF → lecture notes (existing workflow, MLT_Python/CLAUDE.md)
2. build_site.py + build_chat_data.py (existing)
3. NEW: python build_video.py L{N} --all  (script → ... → assemble)
4. Publish + site par video_id add + rebuild
```

### DL_Python ke liye
- Same pipeline, alag `out/` aur alag playlist
- DL ke liye naye components: neural network diagrams (`NeuralNetDiagram`: layers, weights, forward pass animation), `ActivationPlot`, `LossLandscape`, `ConvFilterViz`, `AttentionMatrix`
- Shared library (`video/lib/`) ko ek common jagah rakhne ka plan karo (jaise `MLT_&_DL/video_core/`), taaki MLT aur DL dono use kar sakein

---

## 6. Batch commands

```bash
# Ek lecture ke saare topics ke outlines (Claude Code session ke andar interactive better hai)
python build_video.py L21 --stage script --pass outline

# Raat ka GPU batch
python build_video.py L21 --stage normalize,tts,audio_qc,align

# CPU batch
python build_video.py L21 --stage render,cards,assemble --workers 10

# Report
python build_video.py L21 --report        # saare topics ka QA status table
```

### Status dashboard (simple)
`out/STATUS.md` auto-generate karo:
```
| Lecture | Topic | Script | Verify | TTS | Code | Critic | Render | Final | Published |
|---|---|---|---|---|---|---|---|---|---|
| L20 | T07 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| L20 | T08 | ✅ | ✅ | ✅ | ⏳ | | | | |
```

---

## 7. Quality drift se bachna

Scale par quality dheere-dheere girti hai ("ek aur bina dekhe chala do"). Iske against:
- **G7 human watch kabhi skip mat karo** (1.5–2× speed par bhi chalega)
- Har 5th video par TeachQuiz-lite
- Comments/feedback (YouTube) padho aur common confusion points ko notes mein daalo
- Pehle 3 videos ko har 2 mahine baad dobara dekho: kya ab bhi achhe lagte hain? Agar style improve hua hai to unhe re-render karna cheap hai (pipeline wahi hai)

---

## 8. Re-render ki aasaani (pipeline ka bada fayda)

Kyunki sab kuch code + data hai:
- **Galti mili** (jaise galat number) → `script.json` fix → sirf affected beats ka TTS + scenes re-render
- **Voice upgrade** (better TTS aaya) → TTS stage dobara, render dobara, script same
- **Style change** → theme.py change → re-render (script/audio same)
- **Language add** (English version) → script translate + English TTS → same scenes (narration text alag)

Ye "living videos" ka concept hai: video ek baar ban kar khatam nahi hota, aur improve hota reh sakta hai.

👉 Agla: [35_Troubleshooting_FAQ.md](35_Troubleshooting_FAQ.md)
