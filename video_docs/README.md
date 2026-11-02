# 🎬 Video Docs: AI-Generated Lecture Videos (MLT & DL)

> **Ye folder kya hai?**
> Har MLT (aur baad mein DL) lecture ka ek **detailed, animated, narrated video** banane ka poora plan aur manual.
> Isme har cheez likhi hai: concept, tools, install steps, code, prompts, checklists, galtiyan aur unke fix.
> Docs **Hinglish** mein hain (technical words English mein hi rakhe hain), taaki padhna aasaan rahe.

**Last verified:** 2026-10-18
- Facts official docs, GitHub READMEs, Hugging Face model cards, PyPI aur arXiv se check kiye
- manim-voiceover v0.4.0 ka **source code padha**
- Docs ka zyadatar Python/Manim/ffmpeg code **actually chala kar test kiya** (manim 0.22.0, ffmpeg 8.1.2), aur testing mein mile **14 bugs fix kiye**
- Kya test hua, kya nahi, aur kya abhi bhi tumhe check karna hai: [39_Verification_Log.md](39_Verification_Log.md)

---

## 💰 Default: Budget mode (MacBook, lagbhag ₹0)

Docs ka **recommended mode** ab **budget mode** hai: poori pipeline MacBook (Apple Silicon, jaise 40-core GPU + 64 GB) par, bina paid API ke.
- Animation: **template engine** ([41](41_Template_Engine_Zero_Cost_Animation.md)). Har video ke liye AI-code nahi, sirf JSON "actions"
- Script: Claude subscription (jo already hai) ya local LLM (Ollama)
- TTS / Whisper / render: sab Mac par local
- **Kharcha: ≈ ₹2–5 per topic video (sirf bijli)**

Shuru karo: [42_Budget_Mode_Zero_Cost_Plan.md](42_Budget_Mode_Zero_Cost_Plan.md) → [40_Mac_Apple_Silicon_Setup.md](40_Mac_Apple_Silicon_Setup.md) → [41_Template_Engine_Zero_Cost_Animation.md](41_Template_Engine_Zero_Cost_Animation.md)

> Docs mein jahan "Claude API / vision critic / NVIDIA" likha hai, wo **full mode** hai (optional, paid). Budget mode mein unki jagah kya use karna hai, wo [42](42_Budget_Mode_Zero_Cost_Plan.md) §3 ki table mein hai.

---

## ⚡ 30 second mein poora idea

```
Lecture notes (.md)  ──►  Script JSON (scene → beats)  ──►  Har beat ka audio (local TTS)
                                                                   │  (duration naapo)
                                                                   ▼
   Final MP4  ◄──  ffmpeg stitch  ◄──  Manim render  ◄──  Animation code (run_time = audio duration)
```

1. **Audio pehle, video baad mein.** Har beat (1–3 sentence) ka audio banao, uski length naapo, aur animation ko utna hi lamba banao. Is tarah sync perfect rehta hai.
2. **Maths ke liye code se animation (Manim).** AI video models (Sora/Veo/Wan) equations aur numbers bigaad dete hain, isliye unhe main content mein use nahi karna.
3. **Topic-wise chapters (8–20 min).** Inhe jod kar 1–2 ghante ka full lecture video banta hai.

---

## 📚 Reading order (kaun si file kab padhni hai)

### Part A: Samjho (concepts, sabse pehle padho)
| # | File | Kya milega |
|---|---|---|
| 00 | [00_Seedhi_Baat_Big_Picture.md](00_Seedhi_Baat_Big_Picture.md) | Poora project ek nazar mein, kya ban raha hai, kyun aise |
| 01 | [01_Video_Basics_Frames_FPS_Codecs_Audio.md](01_Video_Basics_Frames_FPS_Codecs_Audio.md) | Frame, FPS, resolution, codec, bitrate, sample rate, LUFS: zero se |
| 02 | [02_Sync_Ka_Science_Audio_First_Timeline.md](02_Sync_Ka_Science_Audio_First_Timeline.md) | Audio-video sync kaise kaam karta hai (maths ke saath) |
| 03 | [03_Pedagogy_Teaching_Design_Principles.md](03_Pedagogy_Teaching_Design_Principles.md) | Accha padhane wala video kaise banta hai (Mayer principles, 3Blue1Brown style) |
| 04 | [04_Script_Writing_Guide_Hinglish_Narration.md](04_Script_Writing_Guide_Hinglish_Narration.md) | Narration script kaise likhein (Hinglish rules, pacing, examples) |

### Part B: Design (architecture)
| # | File | Kya milega |
|---|---|---|
| 05 | [05_Architecture_Pipeline_Folder_Structure.md](05_Architecture_Pipeline_Folder_Structure.md) | Poori pipeline, har stage, folder layout, caching |
| 06 | [06_Script_JSON_Schema_Reference.md](06_Script_JSON_Schema_Reference.md) | Script JSON ka har field, full example |
| 07 | [07_Script_Generation_Prompts_With_Claude.md](07_Script_Generation_Prompts_With_Claude.md) | Claude ko script banane ke liye exact prompts |
| 08 | [08_Math_Verification_Step.md](08_Math_Verification_Step.md) | Har number Python se verify karna |

### Part C: Audio (TTS → clean audio → timestamps)
| # | File | Kya milega |
|---|---|---|
| 09 | [09_TTS_Model_Selection_Guide.md](09_TTS_Model_Selection_Guide.md) | Kaun sa TTS model kyun, comparison table |
| 10 | [10_TTS_Setup_Kokoro.md](10_TTS_Setup_Kokoro.md) | Kokoro install aur code |
| 11 | [11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) | Hindi/Hinglish models ka setup |
| 12 | [12_TTS_Setup_Chatterbox_Voice_Cloning.md](12_TTS_Setup_Chatterbox_Voice_Cloning.md) | Apni awaaz clone karna |
| 13 | [13_TTS_BakeOff_Kaise_Kare.md](13_TTS_BakeOff_Kaise_Kare.md) | Models ko apne sentences par test karna (scoring sheet) |
| 14 | [14_Pronunciation_Text_Normalization.md](14_Pronunciation_Text_Normalization.md) | "AUC", "σ", "0.940" sahi kaise bulwayein |
| 15 | [15_Audio_Post_Processing_Loudness_Music.md](15_Audio_Post_Processing_Loudness_Music.md) | Loudness, silence, background music, ducking |
| 16 | [16_Word_Timestamps_Forced_Alignment_Captions.md](16_Word_Timestamps_Forced_Alignment_Captions.md) | Word-level timing, subtitles (SRT/VTT) |

### Part D: Visuals (animation)
| # | File | Kya milega |
|---|---|---|
| 17 | [17_Manim_Basics_Install_Concepts.md](17_Manim_Basics_Install_Concepts.md) | Manim zero se: install, Scene, Mobject, animations, LaTeX |
| 18 | [18_Manim_Voiceover_Sync_Custom_Local_TTS.md](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) | manim-voiceover, local TTS ka custom service, bookmarks |
| 19 | [19_Manim_Component_Library_Design.md](19_Manim_Component_Library_Design.md) | Reusable components (EquationSteps, TreeDiagram, ...) |
| 20 | [20_Visual_Style_Guide_Colors_Fonts_Layout.md](20_Visual_Style_Guide_Colors_Fonts_Layout.md) | Colors, fonts, layout grid, safe zones |
| 21 | [21_AI_Se_Manim_Code_Generation.md](21_AI_Se_Manim_Code_Generation.md) | Claude se Manim code likhwana, error-fix loop |
| 22 | [22_Critic_Loop_Visual_QA.md](22_Critic_Loop_Visual_QA.md) | Rendered frames dekh kar layout galtiyan pakadna |
| 23 | [23_Imagery_Local_Image_Generation.md](23_Imagery_Local_Image_Generation.md) | Analogy/imagery ke liye local image models |
| 24 | [24_HyperFrames_Intro_Recap_Quiz.md](24_HyperFrames_Intro_Recap_Quiz.md) | HTML+GSAP se intro, recap, quiz screens |
| 25 | [25_Remotion_Alternative.md](25_Remotion_Alternative.md) | Remotion kab use karein, license |

### Part E: Render, assemble, publish
| # | File | Kya milega |
|---|---|---|
| 26 | [26_Rendering_Performance_Parallel.md](26_Rendering_Performance_Parallel.md) | Render settings, parallel render, time estimates |
| 27 | [27_FFmpeg_Final_Assembly.md](27_FFmpeg_Final_Assembly.md) | Clips jodna, audio mix, subtitles, chapters, final encode |
| 28 | [28_Quality_Assurance_Checklist.md](28_Quality_Assurance_Checklist.md) | Publish se pehle har check |
| 32 | [32_Publishing_YouTube.md](32_Publishing_YouTube.md) | YouTube upload settings, chapters, thumbnail |

### Part F: Setup, operations, reference
| # | File | Kya milega |
|---|---|---|
| 29 | [29_Hardware_Environment_Setup_Windows_NVIDIA.md](29_Hardware_Environment_Setup_Windows_NVIDIA.md) | High-end PC setup (CUDA, Python, LaTeX, Node) |
| 30 | [30_Local_LLMs_Kab_Aur_Kaise.md](30_Local_LLMs_Kab_Aur_Kaise.md) | Local LLM kab use karein, kab Claude |
| 31 | [31_Avatar_Talking_Head_Optional.md](31_Avatar_Talking_Head_Optional.md) | Talking head (optional) |
| 33 | [33_Pilot_Plan_L20_Entropy_Information_Gain.md](33_Pilot_Plan_L20_Entropy_Information_Gain.md) | **Pehla pilot video, step by step** |
| 34 | [34_Scaling_All_Lectures_Workflow.md](34_Scaling_All_Lectures_Workflow.md) | 22 lectures ke liye repeatable workflow |
| 35 | [35_Troubleshooting_FAQ.md](35_Troubleshooting_FAQ.md) | Common errors aur fixes |
| 36 | [36_Research_Papers_And_Prior_Art.md](36_Research_Papers_And_Prior_Art.md) | Code2Video, TheoremExplainAgent, Paper2Video: inse kya seekhna hai |
| 37 | [37_Glossary_A_to_Z.md](37_Glossary_A_to_Z.md) | Har technical shabd ka matlab |
| 38 | [38_Licenses_Legal_Ethics.md](38_Licenses_Legal_Ethics.md) | Kaun sa tool commercial use mein chalega, voice consent |
| 39 | [39_Verification_Log.md](39_Verification_Log.md) | Kya verify kiya, kis source se, kya correct kiya |

### Part G: Mac + Budget mode (⭐ recommended)
| # | File | Kya milega |
|---|---|---|
| 40 | [40_Mac_Apple_Silicon_Setup.md](40_Mac_Apple_Silicon_Setup.md) | MacBook par poora setup: LaTeX, Manim, MPS, Mac par TTS, mlx-whisper, Ollama, Draw Things, memory planning |
| 41 | [41_Template_Engine_Zero_Cost_Animation.md](41_Template_Engine_Zero_Cost_Animation.md) | JSON actions se animation (tested engine code + action reference + validator) |
| 42 | [42_Budget_Mode_Zero_Cost_Plan.md](42_Budget_Mode_Zero_Cost_Plan.md) | ₹0 workflow: har stage ka free option, cost table, local LLM prompts |

---

## 🧭 "Main abhi kya karun?" (quick start)

### Budget mode (MacBook) ⭐
1. [00](00_Seedhi_Baat_Big_Picture.md) aur [02](02_Sync_Ka_Science_Audio_First_Timeline.md) padho, isse mental model ban jayega.
2. [42](42_Budget_Mode_Zero_Cost_Plan.md) padho: ₹0 wala plan.
3. [40](40_Mac_Apple_Silicon_Setup.md) follow karke Mac setup karo.
4. [13](13_TTS_BakeOff_Kaise_Kare.md) se voice choose karo (Mac par chalne wale models ke saath).
5. [33](33_Pilot_Plan_L20_Entropy_Information_Gain.md) ka **budget variant** (§7) follow karke pilot banao.
6. Phir [34](34_Scaling_All_Lectures_Workflow.md) se baaki lectures.

### Full mode (NVIDIA PC + paid API, optional)
1. [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) se PC setup karo.
2. [13](13_TTS_BakeOff_Kaise_Kare.md) → [33](33_Pilot_Plan_L20_Entropy_Information_Gain.md) → [34](34_Scaling_All_Lectures_Workflow.md).

---

## 🔑 Teen rules jo kabhi nahi todne

| Rule | Kyun |
|---|---|
| **Audio duration hi master clock hai** | Video ko audio par fit karo, audio ko kabhi stretch mat karo ([02](02_Sync_Ka_Science_Audio_First_Timeline.md)) |
| **Har number Python se verify** | Galat number wala educational video nuksaan karta hai ([08](08_Math_Verification_Step.md)) |
| **Screen par text sirf code se** | AI image/video models text bigaadte hain ([23](23_Imagery_Local_Image_Generation.md)) |

---

## 🗂️ Ye docs project mein kahan fit hote hain

```
MLT_&_DL/
├── MLT_Python/
│   ├── lectures/          ← video ka SOURCE (har topic ki .md, 3 styles)
│   ├── site/              ← existing website
│   └── video/             ← (pilot ke time banega) pipeline code + outputs (template engine bhi yahin)
├── DL_Python/             ← baad mein same pipeline
└── video_docs/            ← 📍 tum yahan ho (ye manual)
```
