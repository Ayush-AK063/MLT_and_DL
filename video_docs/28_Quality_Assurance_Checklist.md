# 28 · Quality Assurance Checklist

> **Is file mein:** Har stage ke baad aur publish se pehle kya check karna hai: automatic checks, human checks, aur `qa_report.json` ka format. Is checklist ko pass kiye bina koi video publish nahi hogi.

---

## 1. QA gates (pipeline mein kahan)

```
[Script] ─G1─► [Verify] ─G2─► [TTS] ─G3─► [Code] ─G4─► [Preview+Critic] ─G5─► [Render] ─G6─► [Assemble] ─G7─► PUBLISH
```
| Gate | Kya | Kaun |
|---|---|---|
| G1 | Script review (outline + full) | 👤 Human + Claude self-critique |
| G2 | Maths verify 0 failures | 🤖 Auto |
| G3 | Audio QC (duration, silence, ASR CER) | 🤖 Auto + 👤 spot listen |
| G4 | Static code checks + `-s` render | 🤖 Auto |
| G5 | Layout audit + vision critic | 🤖 Auto + 👤 for majors |
| G6 | Final render technical checks | 🤖 Auto |
| G7 | Full watch + final checklist | 👤 Human |

---

## 2. G1: Script checklist

**Content**
- [ ] `coverage_checklist` ka har item kisi beat mein hai
- [ ] Notes ke saare worked examples cover hue
- [ ] Koi factual galti nahi (formulas, definitions)
- [ ] Slides/notes se koi mismatch ho (jaise 0.2464 vs 0.2467) to note beat hai

**Pedagogy** ([03](03_Pedagogy_Teaching_Design_Principles.md))
- [ ] Hook pehle 30 s mein
- [ ] Har symbol use se pehle define
- [ ] Har formula ke saath concrete number example
- [ ] Analogy hai, aur uski limit batayi gayi
- [ ] Pause-and-try ya predict moment hai
- [ ] Common mistake scene hai
- [ ] Recap ≤ 3 points

**Narration** ([04](04_Script_Writing_Guide_Hinglish_Narration.md))
- [ ] Har beat ≤ 45 words, har sentence ≤ ~20 words
- [ ] Narration mein raw symbols nahi
- [ ] Numbers ka ek hi style
- [ ] Tone conversational; "simply/obviously" nahi
- [ ] Total words ≈ target × 140 (±25%)

---

## 3. G2: Verify
- [ ] `verify_report.json`: 0 failures
- [ ] Har `display.latex` number kisi verify id se
- [ ] Random experiments: seed + library versions manifest mein

---

## 4. G3: Audio
**Auto** ([15](15_Audio_Post_Processing_Loudness_Music.md) §8, [13](13_TTS_BakeOff_Kaise_Kare.md) §3)
- [ ] Koi beat < 0.3 s nahi
- [ ] Truncation/repetition flags nahi
- [ ] ASR CER < threshold (ya flagged beats manually suni gayi)
- [ ] Clipping nahi

**Human (10% beats random + saare flagged)**
- [ ] Pronunciation sahi (technical terms, names)
- [ ] Awaaz consistent
- [ ] Koi ajeeb pause/emphasis nahi

---

## 5. G4: Code / actions
- [ ] **Template scenes (budget mode):** `validate_actions(script)` → `[]` ([41](41_Template_Engine_Zero_Cost_Animation.md) §5)
- [ ] **Custom scenes:** `static_check` pass ([21](21_AI_Se_Manim_Code_Generation.md) §4)
- [ ] `manim -ql -s` bina error ke

---

## 6. G5: Visual
- [ ] Layout audit: 0 OUT_OF_FRAME, 0 TEXT_OVERLAP (intentional allow-list ke alawa) ([22](22_Critic_Loop_Visual_QA.md))
- [ ] Vision critic: 0 major (full mode; budget mode mein iski jagah human preview at 2×)
- [ ] Har beat ka visual narration se match karta hai (critic MATCH check)

---

## 7. G6: Render technical (auto)
```bash
ffprobe ... → 1920x1080, 30/1 fps, yuv420p, h264; audio present
```
- [ ] Resolution/fps/pix_fmt sahi
- [ ] Scene duration ≈ Σ(beats + gaps) (±0.2 s)
- [ ] Freeze > 15 s nahi (pause-and-try chhod kar)
- [ ] Unexpected silence > 3 s nahi

---

## 8. G7: Final (publish se pehle)

### Technical
- [ ] MP4, H.264 High, yuv420p, 30 fps, 1080p (ya 1440p)
- [ ] AAC 48 kHz stereo
- [ ] Integrated loudness −14 LUFS (±1), true peak ≤ −1 dBTP
- [ ] `faststart` (moov pehle)
- [ ] Chapters embedded + YouTube description ke liye chapters text ready
- [ ] SRT ready (numbers digits mein)

### Watch-through (poora video, 1.5–2× speed theek hai)
- [ ] Shuru se end tak koi sync drift nahi (especially end ke paas check karo)
- [ ] Scene transitions smooth (koi black flash/jump nahi)
- [ ] Music narration ko dabata nahi
- [ ] Koi visual glitch nahi
- [ ] Phone par bhi text readable (ek baar phone par dekho)

### Content final
- [ ] Title, description, chapters sahi
- [ ] Thumbnail
- [ ] Credits/attributions (music, models agar license maange) description mein
- [ ] `manifest.json` complete

---

## 9. `qa_report.json` format

```json
{
  "topic": "L20/T07",
  "date": "2026-10-21",
  "gates": {
    "G1_script": {"pass": true, "reviewer": "human", "notes": "Analogy changed to cricket"},
    "G2_verify": {"pass": true, "failures": 0},
    "G3_audio": {"pass": true, "flagged_beats": ["b017"], "fixed": ["b017"]},
    "G4_code": {"pass": true, "fix_rounds": {"s05": 1}},
    "G5_visual": {"pass": true, "audit_issues": 0, "critic_major": 0, "critic_minor": 2},
    "G6_render": {"pass": true, "duration_s": 652.4},
    "G7_final": {"pass": true, "lufs": -14.1, "true_peak": -1.3, "watched_by": "human"}
  },
  "human_notes": [
    {"t": "04:12", "note": "Weighted sum wala step thoda tez hai, next time pause_after 0.8"}
  ]
}
```

`human_notes` ko next topics ke prompts improve karne ke liye use karo (feedback loop, [34](34_Scaling_All_Lectures_Workflow.md)).

---

## 10. Learner testing (optional, lekin powerful)

Code2Video ka **TeachQuiz** idea: video dekhne se pehle aur baad mein ek chhota quiz. Seekhne mein kitna farak pada, isse pata chalta hai.

Practical version:
1. 2–3 students jo topic nahi jaante
2. Video se pehle 5 sawaal (MCQ)
3. Video dekhein
4. Same 5 sawaal (order shuffle karke)
5. Score badha? Kahan confuse hue? (pucho)

Pehle 2–3 topics par karo. Isse jo seekh milegi wo baaki saare videos ko better banayegi.

👉 Agla: [29_Hardware_Environment_Setup_Windows_NVIDIA.md](29_Hardware_Environment_Setup_Windows_NVIDIA.md)
