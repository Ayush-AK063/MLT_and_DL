# 33 · Pilot Plan: L20 · Information Gain (Pehla Video)

> **Is file mein:** Pehla end-to-end video banane ka step-by-step plan: kya banana hai, kis order mein, har step ka "done" criteria, aur pilot se kya seekhna hai. Pilot ka goal sirf ek video nahi hai. Goal hai **pipeline, voice aur style ko lock karna**.

---

## 1. Pilot topic kyun ye?

**L20 · T07 "Information Gain"** (source: `lectures/Lecture 20/07_Information_Gain_Choosing_the_Best_Attribute.md` + `10_Worked_Example_...md`)

| Kyun | |
|---|---|
| Maths hai (formulas, calculation) | Manim + verify stage test hoga |
| Table data hai (PlayTennis) | `HighlightTable` component test hoga |
| Comparison hai (4 gains) | `BarCompare` test hoga |
| Strong analogy possible (mixed balls) | Intuition scene + `BallBox` |
| Slide vs exact number ka case (0.2464 vs 0.2467) | Verify + note-beat pattern test hoga |
| Pichhla topic (Entropy) se link | Recap scene test hoga |
| Length ~10–12 min | Manageable |

**Verified numbers** ([08](08_Math_Verification_Step.md)): H(S)=0.940 · Sunny 2+/3− H=0.971 · Overcast 4+/0− H=0 · Rain 3+/2− H=0.971 · remainder 0.6935 · **Gain(Outlook)=0.2467** · Humidity 0.1518 · Wind 0.0481 · Temperature 0.0292

---

## 2. Phases aur timeline (realistic)

| Phase | Kaam | Effort (rough) | Done criteria |
|---|---|---|---|
| **P0 Setup** | PC env ([29](29_Hardware_Environment_Setup_Windows_NVIDIA.md)), check_env.py green | 0.5–1 din | Saare ✅ |
| **P1 Voice** | TTS bake-off ([13](13_TTS_BakeOff_Kaise_Kare.md)), voice lock | 0.5–1 din | Winner chuna, scoring sheet bhari, params locked |
| **P2 Script** | Outline → full → critique → human OK | 2–3 ghante | script.json validated, verify 0 fail |
| **P3 Audio** | Normalize → TTS → trim → QC → durations | 1–2 ghante | durations.json, QC clean |
| **P4 Library v0** | theme, layout, HighlightTable, BarCompare, BallBox, EquationSteps, ResultBox, PauseTimer | 1 din | Component test scenes render + visual OK |
| **P5 Scenes** | 9 scenes code (pehla golden example haath se) | 1–2 din | Static checks + preview pass |
| **P6 Critic** | Audit + vision critic + fixes | 0.5 din | 0 major |
| **P7 Render+Assemble** | Final render, cards, music, chapters, SRT | 0.5 din | T07.mp4 G6/G7 pass |
| **P8 Review** | Self-watch + 2 students (TeachQuiz-lite) | 0.5 din | Feedback notes |
| **P9 Retro** | Prompts, library, docs update | 2–3 ghante | Docs + numbers updated |

**Total:** ~1–1.5 hafta (pehli baar). Baad ke topics bahut tez honge, kyunki P0, P1 aur P4 dobara nahi karne padenge.

---

## 3. Step-by-step

### P0: Setup
```powershell
python tools/check_env.py
```
Fonts install, MiKTeX on-the-fly install ON, HF token, `HF_HOME` set.

### P1: Voice lock
1. Bake-off test set ([13](13_TTS_BakeOff_Kaise_Kare.md) §2) ke 30 sentences
2. Candidates: Kokoro hf/hm, IndicF5 (patched) + apni awaaz, Indic Parler (Rohit/Divya), Veena (1–2 speakers), Chatterbox ML + apni awaaz
3. ASR CER + blind MOS + consistency test
4. **Decision record** [13](13_TTS_BakeOff_Kaise_Kare.md) §9 mein likho
5. `config.yaml` → `tts:` section lock

### P2: Script
Claude Code mein:
```text
"L20 T07 ka video script banao. video_docs/07 ke Pass 1 prompt se outline do.
 Source: lectures/Lecture 20/07_*.md aur 10_*.md. Previous topic: 06_Entropy."
```
- Outline review ([07](07_Script_Generation_Prompts_With_Claude.md) §3 checklist)
- Pass 2 + Pass 3
- `python build_video.py L20 T07 --stage verify` → 0 failures
- G1 checklist ([28](28_Quality_Assurance_Checklist.md) §2)

**Expected outline:** [07](07_Script_Generation_Prompts_With_Claude.md) §8 jaisa (9 scenes, ~11 min)

### P3: Audio
```bash
python build_video.py L20 T07 --stage normalize
python build_video.py L20 T07 --stage tts
python build_video.py L20 T07 --stage audio_qc
```
- Flagged beats suno, fix karo (rephrase/pronunciation dict)
- Total narration duration ≈ target (±20%)

### P4: Component library v0
- [19](19_Manim_Component_Library_Design.md) ka code `video/lib/components/` mein
- `tests/test_components.py` render + dekho
- Fonts sahi aa rahe hain? (Inter + Noto Devanagari)

### P5: Scenes
1. **Golden example pehle:** `s05_worked_example` (sabse complex) Claude ke saath carefully banao, har beat dekho, aur approve karo
2. Baaki 8 scenes coder prompt + golden example se
3. Har scene: static_check → `-ql -s` → `-ql` preview

### P6: Critic
- `LayoutAuditMixin` sab scenes mein
- Vision critic per scene
- Majors fix (max 2 rounds), phir human

### P7: Render + assemble
```bash
python build_video.py L20 T07 --stage render --workers 8
python build_video.py L20 T07 --stage cards
python build_video.py L20 T07 --stage assemble
```
- Render time har scene ka **note karo** (section 5 ke table mein)

### P8: Review
- Khud: poora video 1×, phir specific parts
- 2 students: TeachQuiz-lite ([28](28_Quality_Assurance_Checklist.md) §10), 5 MCQs pehle/baad

### P9: Retro
Section 5 bharo, prompts/library/docs update karo.

---

## 4. Pilot ke "lock" decisions

Pilot ke end tak ye sab final hona chahiye (baad mein badalna mehenga padta hai):

| Decision | Locked value |
|---|---|
| TTS model + voice + params | |
| Script form (Roman / Devanagari-mixed) | |
| Number speaking style | |
| Resolution (1080p / 1440p) | |
| Color palette / fonts | [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md) (ya changes) |
| Intro/outro templates | |
| Music track(s) | |
| Beat gap / pause defaults | |
| Captions language | |

---

## 5. Pilot measurements (fill karo)

| Metric | Value | Notes |
|---|---|---|
| Final video duration | | |
| Narration words | | |
| Effective wpm | | |
| Beats / scenes | | |
| TTS time (total) / RTF | | |
| Claude tokens/cost (script) | | |
| Claude tokens/cost (code + fixes + critic) | | |
| Fix-loop rounds (avg per scene) | | |
| Critic majors (before → after) | | |
| Render time per scene (1080p30) | | |
| Total render time | | |
| Human time (total) | | |
| TeachQuiz-lite: before → after avg score | | |
| Top 3 problems | | |

Ye numbers [00](00_Seedhi_Baat_Big_Picture.md) §7, [26](26_Rendering_Performance_Parallel.md) §2 aur [30](30_Local_LLMs_Kab_Aur_Kaise.md) §6 ke estimates ko replace karenge.

---

## 6. Pilot success criteria

Pilot tab "pass" hai jab:
- [ ] Video G7 pass karta hai ([28](28_Quality_Assurance_Checklist.md))
- [ ] Tum khud ise "YouTube par daal sakta hoon" level ka maante ho
- [ ] 2 students ka post-quiz score badha aur unhone kaha "samajh aaya"
- [ ] Awaaz 1 ghanta sunne layak hai (honest answer)
- [ ] Ek naya topic ab ~1–2 din mein ban sakta hai (estimate)

Agar koi fail ho: root cause dhundho (voice? script? visuals?), fix karo, aur pilot ka wahi hissa dobara karo. Scale tab tak mat karo.

---

## 7. ⭐ Budget variant (MacBook, ≈ ₹0)

Same pilot, lekin bina paid API ke ([42](42_Budget_Mode_Zero_Cost_Plan.md)):

| Phase | Full mode | **Budget mode (Mac)** |
|---|---|---|
| P0 Setup | [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) | **[40](40_Mac_Apple_Silicon_Setup.md)** (Homebrew, LaTeX, Manim, MPS, Ollama, mlx-whisper) |
| P1 Voice | 5 candidates | **Kokoro, Chatterbox ML + apni awaaz, IndicF5 (agar MPS/CPU par chale)** |
| P2 Script | Claude 3 passes | Claude Code subscription (ek session) **ya** Ollama (outline → scene-by-scene, [42](42_Budget_Mode_Zero_Cost_Plan.md) §4). Beats ke saath **actions** bhi |
| P3 Audio | Same | Same (Mac par) + mlx-whisper ASR check |
| P4 Library | Components | Components + **template engine** ([41](41_Template_Engine_Zero_Cost_Animation.md)) |
| P5 Scenes | Claude code per scene | **Koi code nahi**: 3-line scene files + `validate_actions()` |
| P6 Critic | Audit + vision critic | **Audit + khud preview 2×** |
| P7 Render | 8 workers | 8–10 workers (Max) + `caffeinate -i`, charger |
| Cost | ≈ ₹500–2,500 (pilot, API) | **≈ ₹5–10 (bijli)** |

**Pilot budget-mode effort:** P4 (library + template engine) sabse bada one-time kaam hai, lekin uska code docs mein tested pada hai (19, 20, 41). Use copy karke setup karna hai. Baaki phases same hain.

**Expected scene → renderer split (L20 T07):**
| Scene | Renderer | Actions used |
|---|---|---|
| s01 hook | template | `title`, `table`, `text` |
| s02 recap | template | `balls` (9+/5−), `text` `{num:H_S}` |
| s03 intuition | template | `balls` ×3 (Sunny/Overcast/Rain), `text` |
| s04 definition | template | `math` (gain formula parts), `indicate` |
| s05 worked example | template | `table`, `highlight_rows`, `text`, `box` |
| s06 compare | template | `bars`, `crown` |
| s07 pause & try | template | `text`, `timer` |
| s08 mistake | template | `text`, `math`, `box` (WARN color) |
| s09 recap | template | `bullets`, `reveal` |

→ Is topic ke **saare scenes template se** ban sakte hain, koi custom code nahi.

---

## 8. Pilot ke baad ka order (suggestion)

1. **L20 ke baaki topics** (same lecture, same data, sabse kam naya kaam)
2. **L21** (ID3 continuation, tree components reuse honge)
3. **L22** (Random Forest, real sklearn experiment se charts)
4. Phir **L16–L19** (KNN, metrics, ROC: naye components: scatter plot, confusion matrix, ROC curve)
5. Phir **L1–L15** (shuru ke lectures)

Is order mein har naya lecture pichhle components ko reuse karta hai aur 1–2 naye add karta hai.

👉 Agla: [34_Scaling_All_Lectures_Workflow.md](34_Scaling_All_Lectures_Workflow.md)
