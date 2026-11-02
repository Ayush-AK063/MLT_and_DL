# 00 · Seedhi Baat: Big Picture

> **Is file mein:** Hum kya bana rahe hain, kyun is tareeke se, kaun se options reject kiye aur kyun, aur end result kaisa dikhega.

---

## 1. Goal kya hai (ek line mein)

**Har lecture ke har topic ka ek aisa video jo khud ek acche teacher ki tarah padhaye:** intuition se shuru kare, imagery/analogy se samjhaye, formula dikhaye, question step-by-step solve kare, aur recap kare. Awaaz aur animation ekdam sync mein hon.

### Success ka matlab (measurable)
| Cheez | Target |
|---|---|
| Sync | Bola gaya shabd aur screen par highlight max ~100 ms ke farak mein (practically beat-level sync se hi mil jata hai) |
| Correctness | Video ka har number Python se verified ho (0 galat numbers) |
| Coverage | Lecture notes ka har topic cover ho, har worked example solve ho |
| Clarity | Ek beginner bina notes ke sirf video dekh kar topic samajh le |
| Repeatability | Naya lecture aane par same pipeline se video bane, manual kaam kam se kam ho |
| Output | 1080p (ya 1440p), 30 fps, YouTube-ready MP4 + subtitles + chapters |

---

## 2. Ek analogy se samjho: movie studio

Socho tum ek chhota animation studio chala rahe ho:

| Studio ka role | Hamari pipeline mein | Tool |
|---|---|---|
| **Writer** (kahani likhta hai) | Script generation | Claude (lecture notes se) |
| **Fact-checker** | Maths verification | Python (sympy, numpy, sklearn) |
| **Voice artist** | Narration | Local TTS (Kokoro / IndicF5 / Veena / Chatterbox) |
| **Animator** | Animation code | Manim (Claude code likhta hai) |
| **Art department** | Imagery/illustrations | Local image model (FLUX schnell / Qwen-Image) |
| **Motion graphics** | Intro, recap, quiz cards | HyperFrames (HTML+GSAP) |
| **Reviewer** | Visual QA | Vision model + tum khud |
| **Editor** | Sab jodna | ffmpeg |

Asli studio mein bhi **voice recording pehle hoti hai, animation baad mein.** Pixar aur Disney mein bhi dialogue pehle record hota hai, phir animators lip-sync aur timing usi par banate hain. Hum bhi wahi kar rahe hain.

---

## 3. Final architecture (ek diagram)

```
┌──────────────────────────────────────────────────────────────────────┐
│ INPUT: MLT_Python/lectures/Lecture N/*.md  (Technical + Simple + Hinglish)│
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
        [1] SCRIPT  ── Claude ──► script.json (scenes → beats)
                                │   har beat = narration + visual spec + latex
                                ▼
        [2] VERIFY  ── Python ──► har number check (sympy/sklearn)
                                ▼
        [3] TTS     ── local GPU ─► beat_001.wav, beat_002.wav ... + durations.json
                                ▼
        [4] ALIGN   ── stable-ts/WhisperX ─► word timestamps (captions, bookmarks)
                                ▼
        [5] ANIMATE ── Claude writes Manim code (run_time = beat duration)
                                ▼
        [6] CRITIC  ── preview render → frames → vision check → fix
                                ▼
        [7] RENDER  ── Manim 1080p30 (parallel per scene)
                                ▼
        [8] ASSEMBLE── ffmpeg: concat + loudnorm + music + subtitles + chapters
                                ▼
                     OUTPUT: topic videos + full lecture video
```

Har stage ki detail [05_Architecture_Pipeline_Folder_Structure.md](05_Architecture_Pipeline_Folder_Structure.md) mein hai.

---

## 4. Kaun se options socha aur kyun reject kiye

### ❌ Option 1: Pure AI video generation (Sora / Veo / Kling / Wan)
- **Problem:** Ye models pixels "imagine" karte hain. Equation `H(S) = 0.940` likhne ko bologe to screen par `H(5) = 0.9A0` jaisa kuch aa sakta hai.
- **Problem:** Ek clip sirf kuch seconds ka hota hai. 1 ghante ke consistent video ke liye ye kaam ka nahi.
- **Problem:** Har baar render karne par result alag aata hai (non-deterministic), isliye ek galti fix karne mein poora clip badal jata hai.
- **Kahan chalega:** Sirf decorative B-roll (jaise "data center ka shot"), aur wo bhi optional.

### ❌ Option 2: Slides + voiceover (PowerPoint style)
- Aasaan hai, lekin boring lagta hai. Static slides se "aha moment" nahi aata.
- Research (Paper2Video) ne slides + talking head try kiya hai, lekin maths ke liye animation zyada samjhati hai.

### ❌ Option 3: Ek single 2-ghante ka TTS + ek single render
- TTS models lambe text par drift karte hain (awaaz badalti hai, words skip hote hain).
- Ek galti par sab dobara banana padta hai.
- Render crash hua to ghanton ka kaam gaya.

### ✅ Option chosen: Code-driven animation + audio-first + chunked pipeline
- **Deterministic:** Same code se har baar same video banta hai.
- **Correct:** Text/equations LaTeX se render hote hain, isliye hamesha sahi.
- **Editable:** Ek beat badlo to sirf wahi regenerate hota hai.
- **Research-backed:** Code2Video aur TheoremExplainAgent dono yahi approach (LLM → Manim code) use karte hain ([36](36_Research_Papers_And_Prior_Art.md)).

---

## 5a. ⭐ Budget mode (MacBook, ≈ ₹0) — recommended default

Tumhare paas Apple Silicon MacBook (40-core GPU, 64 GB unified memory) hai, aur paisa kam se kam lagana hai. Isliye default plan ye hai:

| Layer | Budget mode choice | Kyun |
|---|---|---|
| Script | Claude **subscription** (Claude Code) ya **Ollama** local LLM | Extra paisa nahi |
| Animation | **Template engine** ([41](41_Template_Engine_Zero_Cost_Animation.md)): JSON actions → tested Manim components | Har video ke liye AI-code nahi; reliable + free |
| QA | `validate_actions()` + layout audit + khud 2× dekhna | Paid vision critic ki zaroorat nahi |
| TTS | Kokoro / Chatterbox ML / IndicF5 Mac par (MPS) | Local, free |
| Timing | mlx-whisper (Apple MLX) | Fast on Mac |
| Render + assembly | Manim + ffmpeg (Mac) | Free |

**Kharcha: ≈ ₹2–5 per topic video (bijli).** Detail: [42](42_Budget_Mode_Zero_Cost_Plan.md), setup: [40](40_Mac_Apple_Silicon_Setup.md).

Neeche ki table (5) **full mode** hai (paid API + NVIDIA PC). Wo ab optional hai.

---

## 5. Tools ka final stack: full mode (optional)

| Layer | Primary choice | Backup | Kyun |
|---|---|---|---|
| Script + code | **Claude (Claude Code)** | Local LLM (Qwen-Coder class) | Code2Video ke README ke hisaab se best Manim code Claude-4-Opus se aaya tha; local models abhi peeche hain |
| Animation | **Manim Community v0.22** | Manim + HyperFrames | Maths ke liye industry standard (3Blue1Brown style) |
| Sync | **manim-voiceover v0.4** (custom local service) | Apna simple wrapper | Audio duration automatically animation ko milti hai |
| TTS (Hinglish) | **Bake-off se decide**: IndicF5 (patched) / Veena / Indic Parler / Kokoro-hi | Gemini TTS (cloud) | Hinglish quality model-dependent hai, test karna zaroori hai |
| TTS (English) | **Kokoro** (`af_heart`) | Chatterbox | Fast, Apache-2.0, high quality |
| Voice cloning | **Chatterbox Multilingual V3** (Hindi supported) | IndicF5 (reference audio leta hai) | MIT license |
| Word timing | **stable-ts align** (known text) | WhisperX | Known script ke saath forced alignment zyada accurate hai |
| Imagery | **FLUX.1 schnell** / **Qwen-Image** (Apache-2.0) | SDXL | Commercial-safe licenses |
| Motion cards | **HyperFrames** (Apache-2.0) | Remotion (4+ employees par paid) | Free, agent-friendly |
| Assembly | **ffmpeg** | – | Standard, scriptable |

---

## 6. Ek topic video ka andar se structure

Example: **L20 · Information Gain** (~10–12 min)

```
00:00  Hook          "14 din ka data hai. Kaunsa sawaal pehle poochein ki tennis ka faisla jaldi ho?"
00:30  Recap         Entropy kya thi (10 sec visual reminder)
01:00  Intuition     "Kamra saaf karna" analogy → mixed dabba vs sorted dabba
02:30  Definition    Gain(S,A) = H(S) − Σ |Sv|/|S| · H(Sv)   (term by term build)
04:00  Worked ex.    Outlook split: Sunny(2+,3−) Overcast(4+,0−) Rain(3+,2−)
                     → har entropy calculate, weighted sum, gain = 0.2467
07:00  Compare       Humidity 0.1518, Wind 0.0481, Temperature 0.0292 → bar chart race
08:30  Pause & try   "Wind ka gain khud nikalo" → 5 sec pause → solution
09:30  Galti         "Weighted average bhoolna" common mistake
10:30  Recap         3 bullet points + next topic teaser
```

---

## 7a. Kitna paisa lagega

| Mode | Per topic video (~10 min) | Poora course (~155 topics) |
|---|---|---|
| **Budget (Mac, local)** | **≈ ₹2–5** (bijli) | **≈ ₹300–800** |
| Full (Claude API Opus 5.5 + critic) | ≈ ₹450–1,300 | ≈ ₹70,000–2 lakh |
| Full (Claude API Sonnet 5.5) | ≈ ₹250–650 | ≈ ₹40,000–1 lakh |

(API estimates: ~4–5 lakh input + ~2 lakh output tokens per topic; Opus 5.5 $4/$20 per MTok, Sonnet 5.5 $2/$10; ~₹88/$. Pilot mein naapna hai.)

## 7. Kitna time/compute lagega (rough estimates)

> ⚠️ Ye estimates hain, measured numbers nahi. Pilot ke baad asli numbers [33](33_Pilot_Plan_L20_Entropy_Information_Gain.md) mein update karne hain.

| Stage | 10-min topic ke liye rough | Kahan chalega |
|---|---|---|
| Script generation | 5–15 min (incl. review) | Claude |
| Maths verify | 2–5 min | CPU |
| TTS (~1500 words) | Kokoro: seconds se kuch minute tak; 3B models (Veena): zyada | GPU |
| Manim code gen + fix loop | 20–60 min (pehle topics mein zyada, library banne ke baad kam) | Claude |
| Render 1080p30 | Scene complexity par depend; ~10 min video = 18,000 frames | CPU (Cairo) |
| Assembly | Minutes | CPU |

**Frames ki ginti:** 1 ghanta × 3600 sec × 30 fps = **108,000 frames**. Isliye parallel render aur caching zaroori hai ([26](26_Rendering_Performance_Parallel.md)).

---

## 8. Sabse badi risks aur unka plan

| Risk | Asar | Plan |
|---|---|---|
| Hinglish TTS robotic lage | Poore video ki quality giregi | Bake-off ([13](13_TTS_BakeOff_Kaise_Kare.md)) + pronunciation dictionary ([14](14_Pronunciation_Text_Normalization.md)) + voice clone option |
| AI ka Manim code layout bigaade (overlap) | Ganda video | Component library ([19](19_Manim_Component_Library_Design.md)) + critic loop ([22](22_Critic_Loop_Visual_QA.md)) |
| Galat number | Galat padhai | Verify step ([08](08_Math_Verification_Step.md)), numbers script JSON se hi aate hain |
| Bahut lamba/boring | Log chhod denge | Chapters, pause-and-try, imagery, pacing rules ([03](03_Pedagogy_Teaching_Design_Principles.md)) |
| License issue (commercial) | Legal problem | [38](38_Licenses_Legal_Ethics.md) ki table follow karo |

---

## 9. Agla kadam

👉 [01_Video_Basics_Frames_FPS_Codecs_Audio.md](01_Video_Basics_Frames_FPS_Codecs_Audio.md) — video ki basic terms samjho
👉 Ya seedha [33_Pilot_Plan_L20_Entropy_Information_Gain.md](33_Pilot_Plan_L20_Entropy_Information_Gain.md) — pilot plan
