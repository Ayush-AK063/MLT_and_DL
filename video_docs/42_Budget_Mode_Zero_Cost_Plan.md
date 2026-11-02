# 42 · Budget Mode: Lagbhag ₹0 Mein Videos

> **Is file mein:** Poori pipeline ko **bina kisi paid API ke**, sirf MacBook aur free tools se chalane ka plan: har stage par kya use karna hai, kya chhodna hai, cost ka hisaab, local LLM ke prompts, workflow, aur quality kaise bachayein. Ye docs ka **recommended default mode** hai, kyunki tum laptop par pehle hi kaafi kharcha kar chuke ho.

---

## 1. Seedhi baat

| | Full mode (pehle ka plan) | **Budget mode** |
|---|---|---|
| Script | Claude API (3 passes) | Claude **subscription** (jo already hai) ya local LLM |
| Animation code | Claude API har scene ka code likhta hai | **Template engine** ([41](41_Template_Engine_Zero_Cost_Animation.md)), JSON actions se, koi naya code nahi |
| Visual critic | Claude vision (har frame image) | **Layout audit (free code)** ([22](22_Critic_Loop_Visual_QA.md) §3) + tum 2× speed par dekho |
| TTS | Local | Local (Mac par) |
| Alignment | Local | Local (mlx-whisper) |
| Images | Local | Optional (Draw Things, free), shuru mein skip |
| Music | YouTube Audio Library | Same |
| **Kharcha per topic video** | ≈ ₹300–1,300 (API) | **≈ ₹2–5 (sirf bijli)** |

---

## 2. Cost ka hisaab (budget mode)

| Item | Cost | Note |
|---|---|---|
| Software (Manim, ffmpeg, TTS models, Ollama, mlx) | ₹0 | Open-source / free |
| Claude | ₹0 extra | Agar subscription already hai (Claude Code isi se chal raha hai). Na ho to local LLM |
| Local LLM | ₹0 | Ollama + Qwen3 30B-class (64 GB Mac) |
| Bijli | ~₹2–5 per topic | Mac full load ~40–140 W (chip par depend); ek topic ka ~1–2 ghanta compute ≈ 0.05–0.3 unit; ₹8–10/unit maan kar. Safe side ke liye ₹2–5 likha |
| Music | ₹0 | YouTube Audio Library |
| YouTube hosting | ₹0 | |
| **Ek topic** | **≈ ₹2–5** | |
| **Ek lecture (8–10 topics)** | **≈ ₹20–50** | |
| **Poora MLT course (~155 topics)** | **≈ ₹300–800** | |

> Ye estimates hain. Pilot mein asli bijli/time naapo ([33](33_Pilot_Plan_L20_Entropy_Information_Gain.md) §5).

**Asli "cost" time hai:** Pehle 1–2 topics mein library aur templates banane mein zyada time lagega. Uske baad har topic mein sirf script review, JSON check aur final watch karna hai.

---

## 3. Har stage: budget mode mein kya use karein

| # | Stage | Budget choice | Detail |
|---|---|---|---|
| 1 | Script + actions | Claude Code (subscription) **ya** Ollama `qwen3` 30B-class | Section 4 |
| 2 | Verify numbers | Python (free) | [08](08_Math_Verification_Step.md) |
| 3 | Normalize text | Python (free) | [14](14_Pronunciation_Text_Normalization.md) |
| 4 | TTS | Kokoro (fastest) / Chatterbox ML (Hindi + apni awaaz) / IndicF5 (test) | [40](40_Mac_Apple_Silicon_Setup.md) §5, bake-off [13](13_TTS_BakeOff_Kaise_Kare.md) |
| 5 | Audio QC | ffmpeg + mlx-whisper (CER check) | [15](15_Audio_Post_Processing_Loudness_Music.md), [40](40_Mac_Apple_Silicon_Setup.md) §6 |
| 6 | Word timing | mlx-whisper `word_timestamps=True` (sirf bookmark wale beats) ya sub-beats | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| 7 | Animation | **TemplateScene** (actions JSON) | [41](41_Template_Engine_Zero_Cost_Animation.md) |
| 8 | Check | `validate_actions()` + `LayoutAuditMixin` + preview 2× | [41](41_Template_Engine_Zero_Cost_Animation.md) §5, [22](22_Critic_Loop_Visual_QA.md) §3 |
| 9 | Render | Manim `-qh --fps 30`, 8–10 workers (Max) | [26](26_Rendering_Performance_Parallel.md), [40](40_Mac_Apple_Silicon_Setup.md) §3 |
| 10 | Cards | **Skip HyperFrames shuru mein**: intro/recap bhi template se (`title`, `bullets`, `reveal`). Baad mein chaho to HyperFrames (free, Node) | [24](24_HyperFrames_Intro_Recap_Quiz.md) |
| 11 | Assemble | ffmpeg | [27](27_FFmpeg_Final_Assembly.md) |
| 12 | Publish | YouTube + site embed | [32](32_Publishing_YouTube.md) |

### Kya chhod rahe hain (aur kyun theek hai)
| Chhoda | Kyun theek hai | Kab wapas laana |
|---|---|---|
| Claude vision critic | Layout audit overlaps/out-of-frame pakad leta hai; templates already tested hain; tum khud dekh hi rahe ho | Kabhi zaroorat lage to subscription mein frames dikha do |
| AI-generated per-scene code | Templates zyada reliable aur free hain | Sirf complex one-off visuals (~10–20% scenes) ke liye |
| AI images | Analogy `balls`/`tree`/text se bhi samjhayi ja sakti hai | Jab channel set ho jaye, Draw Things se |
| Talking head | Research ke hisaab se zaroori nahi ([31](31_Avatar_Talking_Head_Optional.md)) | – |
| Veena | Mac par official 4-bit setup nahi chalta | NVIDIA machine mile tab |

---

## 4. Script + actions: do free raaste

### Raasta A: Claude Code subscription (best quality, ₹0 extra)
Isi tarah jaise lecture notes banwate ho:
```text
"L20 T07 ka video script.json banao, video_docs/07 (Pass 1 outline) aur 41 (actions) ke hisaab se.
 Har beat mein narration + actions do. Numbers sirf {num:id}. Source: lectures/Lecture 20/07_*.md, 10_*.md"
```
- Ek session mein ek topic. Subscription ki usage limit ka dhyan rakho
- Script ke saath hi actions bhi ban jaate hain, alag "code generation" step nahi hai

### Raasta B: Local LLM (Ollama), poori tarah free
Lecture notes already Claude ne detail mein bana diye hain (Technical + Simple + Hinglish). Isliye local model ka kaam mostly **restructure** karna hai, naya content sochna nahi.

**Do-step (chhote steps local model ke liye aasaan hain):**

**Step 1: Outline (scenes + coverage)**
```markdown
Tum ek ML teacher ho. Neeche lecture notes hain. Inse ek video OUTLINE banao.
Scenes is order mein: hook, recap, intuition, definition, worked_example, compare, pause_and_try,
common_mistake, recap_summary. Har scene ke liye: id, type, title, 1 line purpose, kaun se points cover honge.
Sirf JSON do: {"scenes":[...], "coverage_checklist":[...]}
<notes>{{NOTES}}</notes>
```

**Step 2: Har scene ke beats + actions (scene-by-scene, ek call per scene)**
```markdown
Is scene ke liye beats likho. Har beat: {"id","narration","actions"}.
Narration: Roman Hinglish, 1-3 chhote sentences, max 45 words, numbers English words mein
("zero point nine four zero"), koi symbol nahi.
Actions: SIRF is list se: {{ACTION_REFERENCE}}
Numbers ke liye {num:id} use karo; available verify ids: {{VERIFY_IDS_WITH_DISPLAY}}
Data tables: {{DATA_BLOCK_NAMES}}
Scene: {{SCENE_OUTLINE_ITEM}}
Notes ka relevant hissa: {{NOTES_SECTION}}
Sirf JSON array do.
```

**Step 3: Validate + fix loop (automatic)**
```python
issues = validate_actions(script) + schema_and_narration_checks(script)   # doc 06 §8, doc 14 §7
if issues:
    fixed = local_llm(f"Ye JSON hai aur ye errors hain. Sirf errors fix karke poora JSON do.\n{json.dumps(scene)}\n{issues}")
```

**Verify block kaun banayega?** Numbers ka verify block **Python se banao, LLM se nahi:** `verify.py` helpers se values compute karke `display`/`spoken` khud generate ho jaate hain. LLM ko sirf ids aur display strings diye jaate hain. Isse local LLM ki maths galti ka risk khatam ho jaata hai.

### Local model settings
- JSON ke liye temperature 0.2–0.3
- Ollama `format: "json"` option (agar available ho) se valid JSON milta hai
- Ek call mein ek scene, kyunki chhota context = kam galtiyan

---

## 5. Budget workflow (ek topic)

```
Din 1 (2–3 ghante tumhara time):
  1. Script + actions (Claude Code ya local LLM)            ~30–60 min (review incl.)
  2. python build_video.py L20 T07 --stage verify,validate  ~1 min
  3. --stage normalize,tts,audio_qc                           ~10–30 min (Mac, automatic)
     → flagged beats suno, fix
  4. --stage preview  (manim -ql, saare scenes)               ~10–20 min automatic
     → 2× speed dekho + layout audit report
  5. JSON tweaks → dobara preview (sirf badle scenes)

Raat:
  6. caffeinate -i python build_video.py L20 T07 --stage render,assemble --workers 8

Din 2 (30–45 min):
  7. Final watch (1.5–2×) + G7 checklist ([28])
  8. Publish (unlisted → public) + site embed
```

---

## 6. Quality kaise bachayein (budget mein bhi)

| Risk | Budget fix |
|---|---|
| Local LLM ki script kamzor | Notes already detailed hain; outline review khud karo (5 min); zaroorat ho to sirf script Claude subscription se |
| Galat number | Verify block Python se; actions mein sirf `{num:id}` |
| Layout galti | Tested components + layout audit + preview |
| Robotic awaaz | Bake-off ([13](13_TTS_BakeOff_Kaise_Kare.md)) + pronunciation dict + apni awaaz clone (Chatterbox) |
| Boring visuals | Template library dheere-dheere badhao (har lecture mein 1–2 naye actions) |

---

## 7. One-time setup checklist (Mac, budget mode)

- [ ] [40](40_Mac_Apple_Silicon_Setup.md) §1–4: Homebrew tools, LaTeX, Python + Manim, PyTorch MPS
- [ ] Fonts install
- [ ] Ollama + `qwen3-coder:30b` (ya general 30B-class instruct) pull (64 GB Mac)
- [ ] TTS envs: Kokoro + Chatterbox (+ IndicF5 test)
- [ ] mlx-whisper
- [ ] Component library + template engine files ([19](19_Manim_Component_Library_Design.md), [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md), [41](41_Template_Engine_Zero_Cost_Animation.md))
- [ ] Bake-off → voice lock
- [ ] Music tracks (YouTube Audio Library) + license notes

**Disk space plan:** Ollama model ~19 GB + TTS models (kuch GB) + MacTeX (kai GB, ya BasicTeX chhota) + renders. 50–80 GB free rakho, ya models external SSD par rakho ([40](40_Mac_Apple_Silicon_Setup.md) §12).

---

## 8. Agar kabhi thoda paisa lagana pade (optional upgrades, priority order)

1. **Kuch nahi**: budget mode poori tarah kaam karta hai
2. Agar local Hinglish TTS pasand na aaye: cloud TTS (Gemini/ElevenLabs) sirf final narration ke liye. Cost per video characters ke hisaab se lagega; pehle free tier/trial check karo
3. Agar script quality local LLM se kam lage: sirf script ke liye Claude (subscription limit ya API Sonnet), animation phir bhi templates se

👉 Wapas: [README.md](README.md)
