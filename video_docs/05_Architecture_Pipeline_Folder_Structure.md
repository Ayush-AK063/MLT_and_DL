# 05 · Architecture: Pipeline, Stages, Folder Structure

> **Is file mein:** Poori pipeline ka technical design: har stage ka input/output, folder layout, caching (kya dobara banana padega aur kya nahi), commands, aur failure handling.

---

## 1. Design principles

| Principle | Matlab |
|---|---|
| **Single source of truth** | `script.json` hi sab kuch decide karta hai: narration, visuals, numbers. Code, audio, captions sab isi se bante hain |
| **Stage isolation** | Har stage ka output disk par file hai. Koi bhi stage dobara chala sakte ho bina baaki ko chhede |
| **Content-hash caching** | Beat ka text nahi badla to audio dobara nahi banega. Scene code nahi badla to render dobara nahi hoga |
| **Fail loudly** | Koi number verify nahi hua ya audio duration 0 hai to pipeline wahin ruk jaaye, aage galat video na bane |
| **Human checkpoints** | Script, voice aur pehla preview: in teeno par insaan approve kare |
| **Idempotent** | Same command do baar chalao to same result aaye |

---

## 2. Stages (input → output)

| # | Stage | Input | Output | Tool | Kahan chalega |
|---|---|---|---|---|---|
| 1 | **Script** | `lectures/Lecture N/0X_*.md` | `script.json` | Claude | Claude Code |
| 2 | **Verify** | `script.json` (`verify` blocks) | `verify_report.json` (pass/fail) | Python + sympy/numpy/sklearn | CPU |
| 3 | **Normalize** | narration text | `tts_text` (spoken form, transliterated) | Rule-based Python + dictionary | CPU |
| 4 | **TTS** | `tts_text` per beat | `audio/beat_XXX.wav` + `durations.json` | Kokoro / IndicF5 / Veena / Chatterbox | GPU |
| 5 | **Audio QC** | wav files | trimmed, normalized wavs + QC report | ffmpeg / pydub + ASR check | CPU/GPU |
| 6 | **Align** | wav + text | `words/beat_XXX.json` (word timestamps) | stable-ts / WhisperX | GPU |
| 7 | **Scene code** | `script.json` + durations + component library | `scenes/sceneXX.py` | **Budget:** template engine (3-line scene files, auto-generated; doc 41) · **Full:** Claude (Coder) | Local / Claude Code |
| 8 | **Preview + Critic** | scene code | low-res mp4 + keyframe PNGs + issues list | Manim `-ql` + vision model | CPU + Claude |
| 9 | **Final render** | approved scene code | `renders/sceneXX.mp4` (1080p30, no audio or with audio) | Manim `-qh --fps 30` | CPU (parallel) |
| 10 | **Cards** | intro/recap/quiz data | `cards/*.mp4` | HyperFrames | CPU (headless Chrome) |
| 11 | **Assemble** | renders + audio + cards + music | `topic_XX.mp4` + `.srt` + chapters | ffmpeg | CPU |
| 12 | **Full lecture** | all topic videos | `Lecture_N_full.mp4` + chapters.txt | ffmpeg | CPU |
| 13 | **QA** | final mp4 | QA report | scripts + human | – |

---

## 3. Folder structure (proposed)

Pipeline code `MLT_Python/video/` mein rahega (jaise `build_site.py` aur `build_chat_data.py` hain, waise hi `build_video.py`).

```
MLT_Python/
├── lectures/                         ← SOURCE (already exists)
│   └── Lecture 20/
│       ├── 06_Entropy_Measuring_Disorder_in_a_Dataset.md
│       └── 07_Information_Gain_Choosing_the_Best_Attribute.md
│
├── build_video.py                    ← main CLI (stage runner)
│
└── video/
    ├── config.yaml                   ← global settings (voice, fps, resolution, colors)
    ├── pronunciation.yaml            ← word → spoken form dictionary
    ├── lib/                          ← reusable code
    │   ├── components/               ← Manim component library
    │   │   ├── __init__.py
    │   │   ├── theme.py              ← colors, fonts, sizes
    │   │   ├── equation_steps.py
    │   │   ├── highlight_table.py
    │   │   ├── tree_diagram.py
    │   │   ├── bar_compare.py
    │   │   ├── confusion_matrix.py
    │   │   ├── plot2d.py
    │   │   ├── analogy_card.py
    │   │   └── pause_timer.py
    │   ├── tts/                      ← TTS backends (same interface)
    │   │   ├── base.py
    │   │   ├── kokoro_backend.py
    │   │   ├── indicf5_backend.py
    │   │   ├── veena_backend.py
    │   │   └── chatterbox_backend.py
    │   ├── voiceover_service.py      ← manim-voiceover custom SpeechService (PrebakedService)
    │   ├── scene_base.py             ← LessonScene (doc 18 §6)
    │   ├── template_engine.py        ← ⭐ actions JSON → animation (doc 41, budget mode)
    │   ├── layout_audit.py           ← LayoutAuditMixin (doc 22)
    │   ├── normalize.py              ← text normalization + transliteration
    │   ├── align.py                  ← word timestamps
    │   ├── verify.py                 ← math verification runner
    │   ├── critic.py                 ← frame extraction + vision check
    │   └── assemble.py               ← ffmpeg wrappers
    ├── prompts/                      ← Claude prompts (versioned)
    │   ├── script_prompt.md
    │   ├── coder_prompt.md
    │   └── critic_prompt.md
    ├── assets/
    │   ├── music/                    ← royalty-free background music
    │   ├── images/                   ← generated illustrations (per lecture)
    │   ├── fonts/
    │   └── voice_refs/               ← voice cloning reference clips (consent ke saath)
    ├── cards/                        ← HyperFrames project (intro/recap/quiz templates)
    └── out/                          ← GENERATED (git ignore)
        └── L20/
            └── T07_information_gain/
                ├── script.json
                ├── verify_report.json
                ├── audio/
                │   ├── b001.wav
                │   ├── b002.wav
                │   └── durations.json
                ├── words/
                │   └── b001.json
                ├── scenes/
                │   ├── s01_hook.py
                │   └── s05_worked_example.py
                ├── preview/
                │   ├── s05.mp4
                │   └── s05_frames/
                ├── renders/
                │   └── s05.mp4
                ├── cards/
                ├── T07.mp4             ← final topic video
                ├── T07.srt
                ├── T07_chapters.txt
                └── qa_report.json
```

### Naming conventions
| Cheez | Format | Example |
|---|---|---|
| Lecture id | `L{n}` | `L20` |
| Topic id | `T{nn}_{slug}` | `T07_information_gain` |
| Scene id | `s{nn}_{type}` | `s05_worked_example` |
| Beat id | `b{nnn}` (topic mein global) | `b042` |
| Bookmark | `[A-Za-z0-9_]+` (sirf word characters, manim-voiceover regex `\w*` hai) | `E`, `gain_box` |

---

## 4. CLI design (`build_video.py`)

```bash
# Ek topic, saare stages
python build_video.py L20 T07 --all

# Sirf ek stage
python build_video.py L20 T07 --stage tts
python build_video.py L20 T07 --stage render --scene s05

# Preview (low quality, fast)
python build_video.py L20 T07 --stage preview

# Poora lecture
python build_video.py L20 --all

# Force regenerate (cache ignore)
python build_video.py L20 T07 --stage tts --force
```

### Stage runner ka pseudo-code
```python
STAGES = ["script", "verify", "normalize", "tts", "audio_qc", "align",
          "code", "preview", "critic", "render", "cards", "assemble", "qa"]

def run(lecture, topic, stages, force=False):
    ctx = load_context(lecture, topic)          # paths, config, script.json (agar hai)
    for stage in stages:
        if not force and is_up_to_date(stage, ctx):
            log(f"skip {stage} (cache hit)")
            continue
        result = STAGE_FUNCS[stage](ctx)
        if not result.ok:
            raise SystemExit(f"{stage} FAILED: {result.reason}")   # fail loudly
        save_stage_hash(stage, ctx)
```

---

## 5. Caching: kya kab dobara banega

Har artifact ke saath uske inputs ka **hash** store karo. Inputs badle tabhi rebuild karo.

| Artifact | Hash inputs | Kab rebuild |
|---|---|---|
| `audio/bXXX.wav` | `tts_text` + voice id + model id + model params (speed, temperature) | Narration ya voice badli |
| `words/bXXX.json` | wav hash + text | Audio badla |
| `scenes/sXX.py` | scene ka JSON + durations + component library version | Script/duration badli |
| `renders/sXX.mp4` | scene .py hash + assets hash + render settings | Code badla |
| `T07.mp4` | sab renders + audio + music + settings | Kuch bhi upar badla |

> manim-voiceover khud bhi cache rakhta hai: `media/voiceovers/cache.json` mein `input_data` match karke purani audio reuse karta hai. Hamara custom service `input_data` mein voice/model/params daalega, taaki voice badalne par cache invalid ho ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)).

> Manim ka apna partial-movie cache bhi hai (har `play()` call ka hash). Code thoda badla to sirf badle hue animations re-render hote hain. `--disable_caching` sirf debugging mein use karo.

---

## 6. Do architecture options: audio kahan banega?

### Option A: TTS Manim ke andar (manim-voiceover) ✅ Recommended for start
```
Scene code → self.voiceover(text) → custom service → local TTS → wav → add_sound
```
- **Pro:** Simple, sync automatic, Manim khud audio + video ek file mein deta hai
- **Con:** Render ke waqt TTS model load hota hai (GPU), aur parallel renders mein har process model load karega

**Fix:** Stage 4 mein saari audio **pehle hi** generate kar lo (batch, GPU par). Custom service sirf **cache se file uthaye**, render ke waqt TTS model chalane ki zaroorat hi na pade. Ye "pre-baked audio" pattern hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md), section 5).

### Option B: Pure timeline (Manim silent + ffmpeg audio)
```
durations.json → scene code (run_time hardcoded) → silent mp4 → ffmpeg mein audio overlay
```
- **Pro:** Render aur TTS poori tarah alag; audio ek baar poori timeline par mix hota hai (AAC priming issue nahi aata)
- **Con:** Timing ka hisaab khud rakhna padta hai

**Hamara hybrid:** Option A ke saath pre-baked audio. Manim scene ki mp4 mein audio already hota hai. Final assembly mein hum **har scene ka audio WAV mein extract karke, poori timeline ka audio ek baar AAC mein encode** karenge ([27](27_FFmpeg_Final_Assembly.md)).

---

## 7. Data flow ek beat ke liye (end-to-end)

```
script.json:
  { "id":"b042", "narration":"Entropy aati hai zero point nine four zero.",
    "display":{"latex":"H(S)=0.940"}, "visual":"result box appears around 0.940" }
        │
        ▼ normalize.py
  tts_text = "Entropy aati hai zero point nine four zero."
        │
        ▼ kokoro/indicf5 backend
  audio/b042.wav  (3.21 s)  → durations.json["b042"] = 3.21
        │
        ▼ align.py
  words/b042.json  [{"w":"Entropy","s":0.05,"e":0.61}, ...]
        │
        ▼ coder (Claude) writes scene code
  with self.voiceover(text=B["b042"].narration) as t:
      self.play(Create(SurroundingRectangle(result)), run_time=min(1.0, t.duration))
        │
        ▼ manim render → custom service cache hit → add_sound(b042.wav)
  renders/s05.mp4 (audio + video, sync)
```

---

## 8. Config file (`video/config.yaml`) example

```yaml
video:
  width: 1920
  height: 1080
  fps: 30
  background: "#0F1117"

audio:
  sample_rate_final: 48000
  loudness_lufs: -14
  true_peak_db: -1.0
  beat_gap_s: 0.25
  music_volume_db: -28        # narration ke neeche
  ducking: true

tts:
  backend: indicf5            # kokoro | indicf5 | veena | chatterbox | parler
  voice: "voice_refs/saurabh_ref.wav"
  voice_ref_text: "..."       # IndicF5/F5 ko reference ka transcript chahiye
  lang: hi
  speed: 1.0
  script_form: roman          # roman | devanagari_mixed

align:
  engine: stable_ts           # stable_ts | whisperx | none
  model: medium

render:
  preview_quality: l          # -ql
  final_quality: h            # -qh + --fps 30
  renderer: cairo
  parallel_scenes: 6

mode: budget                  # budget | full   (doc 42)

llm:
  script_model: claude_subscription   # claude_subscription | ollama:qwen3-coder:30b | claude_api
  coder_model: none                   # budget mode: template engine (koi code-gen nahi)
  critic_model: none                  # budget mode: layout audit + human; full: claude vision
```

---

## 9. Failure handling

| Failure | Detection | Action |
|---|---|---|
| Verify fail (number mismatch) | `verify_report.json` mein `fail` | Pipeline STOP, script fix karo |
| TTS empty/silent audio | duration < 0.3 s ya RMS bahut kam | Retry (different seed), phir flag |
| TTS ne words skip kiye | ASR back-transcription se CER > threshold ([13](13_TTS_BakeOff_Kaise_Kare.md)) | Retry, phir sentence rephrase |
| Manim code crash | Non-zero exit + traceback | Traceback Claude ko do, fix (max 3 tries), phir human |
| Layout overlap | Critic report | Fix loop ([22](22_Critic_Loop_Visual_QA.md)) |
| Render crash mid-way | Partial file | Manim partial-movie cache se resume |
| Duration mismatch (video vs audio) | ffprobe compare | Assembly mein flag |

---

## 10. Versioning

- `video/` folder ko **git** mein rakho (out/ ko `.gitignore` karo)
- Prompts versioned rakho (`prompts/script_prompt.md` mein version header)
- Har final video ke saath `manifest.json`: kaun sa model, voice, prompt version, component library version, aur date

```json
{
  "topic": "L20/T07",
  "built": "2026-10-20",
  "tts": {"backend": "indicf5", "voice": "saurabh_ref", "patch": "harrrshall-v2.1"},
  "manim": "0.22.0",
  "manim_voiceover": "0.4.0",
  "prompt_versions": {"script": "v3", "coder": "v5"},
  "components": "v1.2"
}
```

👉 Agla: [06_Script_JSON_Schema_Reference.md](06_Script_JSON_Schema_Reference.md)
