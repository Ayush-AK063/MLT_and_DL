# 35 · Troubleshooting & FAQ

> **Is file mein:** Common errors (install, Manim, LaTeX, manim-voiceover, TTS, ffmpeg, sync) aur unke fixes. Kai errors humne docs ke code test karte waqt **khud dekhe** hain, aur unhe ✅ "seen in testing" mark kiya hai.

---

## 1. Installation

| Error | Cause | Fix |
|---|---|---|
| `pycairo` build failed / "Dependency cairo not found" ✅ seen | macOS/Linux par cairo system library nahi hai | macOS: `brew install cairo pkg-config`; Ubuntu: `sudo apt install libcairo2-dev libpango1.0-dev` |
| "Microsoft Visual C++ 14.0 or greater is required" | Windows par compile tools nahi | Visual Studio Build Tools, "Desktop development with C++" |
| `manim: command not found` | venv activate nahi | `uv run manim ...` ya venv activate karo |
| Python version error (manim-voiceover) | v0.4.0 ko Python ≥ 3.11 chahiye | `uv python install 3.12` |
| "SoX could not be found!" warning ✅ seen | `sox` Python package SoX binary dhundhta hai | Ignore (agar `global_speed` use nahi), ya SoX install karke PATH mein daalo |

---

## 2. LaTeX (MathTex)

| Error | Cause | Fix |
|---|---|---|
| `LaTeX Error: File 'standalone.cls' not found` ✅ seen | Minimal TeX install (BasicTeX/TinyTeX) mein package nahi | MiKTeX: on-the-fly install ON; TeX Live: `tlmgr install standalone preview` (user mode: `tlmgr --usermode install ...`) |
| `FileNotFoundError: 'dvisvgm'` ✅ seen | dvisvgm installed nahi (BasicTeX mein nahi aata) | MiKTeX/TeX Live full mein hota hai; Ubuntu: `sudo apt install dvisvgm`; TeX Live: `tlmgr install dvisvgm` (admin) |
| `latex error converting to dvi` | Formula mein syntax error, ya missing package | `media/Tex/<hash>.log` kholo, `!` wali line dekho |
| Hindi text MathTex mein toot gaya | Default LaTeX template Devanagari support nahi karta | Hindi ke liye `Text()` use karo |
| `\f`/`\t` ajeeb characters | Non-raw string | `r"..."` raw strings |

---

## 3. Manim

| Error | Cause | Fix |
|---|---|---|
| `ImportError: cannot import name 'ShowCreation'` | 3b1b manimgl API | ManimCE: `Create` |
| `NameError: TextMobject` | Purana API | `Text` / `Tex` |
| Video 60 fps aa raha hai | `-qh` default 60 | `-qh --fps 30` |
| Font fallback / layout alag | Font installed nahi | Inter / Noto Sans Devanagari install karo ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) |
| Text overlap / frame ke bahar ✅ seen | Fixed widths, manual coordinates | Components + `place()` + `LayoutAuditMixin` ([22](22_Critic_Loop_Visual_QA.md)) |
| Render bahut slow | 1080p60, complex updaters | 30 fps, preview `-ql`, updaters kam, parallel scenes ([26](26_Rendering_Performance_Parallel.md)) |
| Code change ke baad purana output | Cache | Normal (partial cache); doubt ho to `--disable_caching` |
| `-n` se render kiya, voiceover timing galat | Voiceover tracker scene start se time count karta hai | Lambe scene ko script level par todo |

---

## 4. manim-voiceover

| Error | Cause | Fix |
|---|---|---|
| `ValueError: Invalid voiceover cache entry` / `ValidationError ... VoiceoverCacheEntryModel` ✅ seen | v0.4.0 strict pydantic validation: `input_data` mein `input_text` (str) missing, ya galat types | `input_data = {"input_text": ..., "service": ..., ...}`; word boundary fields int/str ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) §3) |
| "Word boundaries are required for timing with bookmarks" ✅ seen | Na transcription model, na `word_boundaries` key | `transcription_model="base"`, ya apni alignment, ya `word_boundaries = []` (linear fallback) |
| "Word boundaries ... insufficient. Using fallback" warning ✅ seen | Empty/1-entry boundaries | Expected (fallback); precise chahiye to alignment do |
| "There is no <bookmark mark='x' />" | Mark naam galat, ya hyphen jaise characters | Sirf `[A-Za-z0-9_]`; narration aur code mein same naam |
| Bookmark tag audio mein bola gaya / text mein dikha | Invalid mark name ki wajah se regex match nahi hua | Same as above |
| Audio duration error (mutagen) | `.flac`/`.ogg` diya; library sirf wav/mp3 padhti hai | WAV ya MP3 |
| `FileNotFoundError` audio | `original_audio` absolute path diya, ya file cache_dir mein nahi | Sirf filename return karo, file `cache_dir` mein rakho |
| Voice badli, phir bhi purani audio | Cache key same | `input_data` mein voice/model/params daalo, ya `media/voiceovers/` saaf karo |
| "You need to call init_voiceover()..." | `set_speech_service` call nahi hua | `construct`/`setup` ke shuru mein call karo |

---

## 5. TTS

| Problem | Cause | Fix |
|---|---|---|
| IndicF5: Roman text par audio kat gaya / silent | UTF-8 byte-count duration bug | harrrshall patch ya Devanagari transliteration ([11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md)) |
| IndicF5 awaaz ajeeb | `ref_text` reference audio se match nahi | Exact transcript |
| Model download 401/403 | Gated model, terms accept nahi ki | HF page par accept + `huggingface-cli login` |
| CUDA out of memory | Model + doosre GPU kaam | Ek model ek time par; 4-bit (Veena); doosre GPU processes band |
| `torch.cuda.is_available() == False` | CPU-only torch install | pytorch.org se CUDA build |
| Words repeat/skip (Veena/autoregressive) | Sampling | Seed fix, temperature kam, beat chhota, ASR check + retry |
| Har beat mein awaaz alag | Random sampling / reference | Same seed, same ref, lower expressiveness |
| Numbers galat bole | Normalization nahi hua | [14](14_Pronunciation_Text_Normalization.md) pipeline; validator |
| Technical term galat | Dictionary mein nahi | `pronunciation.yaml` mein add |

---

## 6. ffmpeg / assembly

| Problem | Cause | Fix |
|---|---|---|
| loudnorm JSON parse fail ✅ seen | ffmpeg 8.x JSON ke baad bhi lines print karta hai | Aakhri `{...}` block lo ([15](15_Audio_Post_Processing_Loudness_Music.md) §4) |
| Final audio 192 kHz ✅ seen | loudnorm internally 192 kHz upsample karta hai | Output par `-ar 48000` |
| Concat ke baad glitch/freeze | Clips ke formats alag | Normalize step ([27](27_FFmpeg_Final_Assembly.md) §2) |
| Lambe video mein dheere-dheere sync drift | AAC clips ka copy-concat (priming), ya frames ko alag-alag round karna | Audio WAV mein concat + ek baar encode; cumulative time se frames ([02](02_Sync_Ka_Science_Audio_First_Timeline.md)) |
| Video QuickTime/phone par nahi chalta | `yuv444p` | `-pix_fmt yuv420p` |
| YouTube processing slow / streaming late start | moov atom end mein | `-movflags +faststart` |
| `subtitles=` filter path error (Windows) | Colon/backslash escaping | Relative path, simple naam |
| "Non-monotonous DTS" warnings | Timestamps mismatch in concat | Normalize + re-encode |

---

## 7. Sync issues (diagnosis)

| Symptom | Likely cause | Check |
|---|---|---|
| Shuru se hi offset | Audio trim ke pehle duration li | Durations trimmed files se? |
| Offset badhta jaata hai | AAC concat ya frame rounding | Section 6 |
| Ek beat mein animation late | Bookmark timing (fallback linear) | Word alignment do, ya sub-beats |
| Animation khatam, narration chal raha | Normal (voiceover block baaki time wait karta hai) | Agar lamba gap hai to visual add karo |
| Narration khatam, animation chal raha | `run_time` > `t.duration` | `min(x, t.duration)` |

---

## 7a. 🍎 Mac-specific

| Problem | Cause | Fix |
|---|---|---|
| `tlmgr --usermode install dvisvgm` → "package dvisvgm is not relocatable" ✅ seen | dvisvgm binary package hai; user mode mein install nahi hota | `sudo tlmgr install dvisvgm` (BasicTeX) ya MacTeX full |
| `brew install dvisvgm` poora TeX Live + Java download karne laga ✅ seen | Homebrew formula ki heavy dependencies | Rok do; TeX ka apna dvisvgm (tlmgr) use karo |
| `pycairo` build fail ✅ seen | cairo nahi hai | `brew install cairo pkg-config` |
| PyTorch: "operator not implemented for MPS" | Kuch ops MPS par nahi hain | `export PYTORCH_ENABLE_MPS_FALLBACK=1` |
| Chatterbox load error (CUDA device) | Weights CUDA par save hue hain | `torch.load` ko `map_location=torch.device("mps")` patch (official `example_for_mac.py`) |
| Veena `bitsandbytes` error | bnb 4-bit NVIDIA-only | Quantization hata kar fp16/bf16 + `mps` (64 GB) ya skip |
| Sab bahut slow, Mac garam, swap badha | LLM + TTS + render ek saath | Ek phase ek time ([40](40_Mac_Apple_Silicon_Setup.md) §9); `ollama stop <model>` |
| Raat ko render ruk gaya | Mac so gaya | `caffeinate -i <command>`, charger lagao |
| Ollama model download se disk full | Models bade (30B ≈ 19 GB) | Purane models `ollama rm`; external SSD |
| `validate_actions` errors | JSON actions galat | Errors LLM ko wapas do ya haath se fix ([41](41_Template_Engine_Zero_Cost_Animation.md) §5) |

---

## 8. FAQ

**Q: Kya sab kuch MacBook par ₹0 mein ho sakta hai?**
A: Haan, budget mode mein ([42](42_Budget_Mode_Zero_Cost_Plan.md)): Claude subscription (jo already hai) ya Ollama se script, template engine se animation, aur Mac par TTS + render. Kharcha sirf bijli ka hai, ≈ ₹2–5 per video.

**Q: 60 fps kyun nahi?**
A: Educational animation mein 30 fps kaafi smooth lagta hai. 60 fps par render time aur file size dono 2× ho jaate hain.

**Q: Kya hum ElevenLabs jaisi cloud TTS use kar sakte hain?**
A: Haan (manim-voiceover mein ElevenLabs/OpenAI/Azure/Gemini services hain). Trade-off cost, privacy aur dependency ka hai. Local bake-off pehle karo; agar local quality kam pade to cloud fallback rakho.

**Q: Ek hi video Hinglish aur English dono mein?**
A: Script ke do versions (narration alag), same scenes. Visuals mein text kam rakho (mostly formulas/numbers), taaki dono mein kaam kare. TTS aur render alag-alag hoga.

**Q: Manim ki jagah sirf HyperFrames/Remotion?**
A: Simple slides-style videos ke liye ho sakta hai, lekin maths derivations (formula morphing), graphs aur trees Manim mein bahut natural hain. Hybrid best hai.

**Q: Kya AI video model (Sora/Veo/Wan) se kuch bhi banana chahiye?**
A: Content ke liye nahi. Optional decorative B-roll ke liye hi ([23](23_Imagery_Local_Image_Generation.md) §8).

**Q: Galti video publish hone ke baad mili to?**
A: Script fix → affected scenes re-render → new upload (YouTube par same video replace nahi hota; naya upload karke purane ko unlist karo aur description/pinned comment mein correction note do). Site par naya video_id.

👉 Agla: [36_Research_Papers_And_Prior_Art.md](36_Research_Papers_And_Prior_Art.md)
