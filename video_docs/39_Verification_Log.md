# 39 · Verification Log

> **Is file mein:** Docs ke facts kaise verify kiye gaye: kaun sa claim kis source se check hua, kaun sa code actually chala kar test hua, testing mein kya bugs mile aur kya fix hua, kya abhi bhi unverified hai, aur pichhli chat ke jawab mein kya correction hua.
>
> **Verification date:** 2026-10-18 · **Test machine:** macOS (Apple Silicon), Python 3.12 (scratch venv), manim 0.22.0, manim-voiceover 0.4.0, ffmpeg 8.1.2

---

## 1. Method

1. **Primary sources first:** Official docs, GitHub READMEs, Hugging Face model cards, PyPI pages, arXiv abstracts. Blogs sirf tab jab primary nahi mila, aur aise claims ko ⚠️ mark kiya
2. **Source code padha:** manim-voiceover v0.4.0 ka wheel download karke uska source padha (`base.py`, `voiceover_scene.py`, `tracker.py`, `cache.py`, `modify_audio.py`, `helper.py`, `gtts.py`, `gemini.py`)
3. **Code chala kar test kiya:** Docs ke zyadatar Python/Manim/ffmpeg snippets ko docs se hi extract karke chalaya (copy-paste galti se bachne ke liye), aur output/images dekhe
4. **Numbers recompute kiye:** Saare maths examples Python se

---

## 2. Facts verified (source ke saath)

| Claim | Source | Status |
|---|---|---|
| Manim CE latest **0.22.0** (8 Oct 2026), Python ≥ 3.11 | PyPI `manim` | ✅ |
| Manim install via uv; OS deps (macOS `cairo pkg-config`, Ubuntu libs); MiKTeX/MacTeX/TeX Live; `manim checkhealth` | docs.manim.community installation (uv) | ✅ |
| Quality flags: `-ql` 480p15, `-qm` 720p30, `-qh` 1080p60, `-qp` 1440p60, `-qk` 2160p60; `--fps`, `-r`, `-s`, `-n`, `--format png-sequence`, `manim.cfg [CLI]` | docs.manim.community configuration guide | ✅ |
| Manim v0.19.0 ne ffmpeg dependency PyAV se replace ki | Manim 0.19.0 changelog | ✅ |
| Frame 14.22 × 8 units | `config.frame_width/height` (manim 0.22 mein print kiya) | ✅ tested |
| manim-voiceover **0.4.0** (14 Jun 2026), Python ≥ 3.11, MIT, Alpha; extras list; Gemini "recommended"; CoquiService removed | PyPI + wheel source | ✅ |
| `generate_from_text` return dict format, `input_data` cache, strict pydantic validation, word_boundaries format (`AUDIO_OFFSET_RESOLUTION = 10_000_000`), bookmark regex `\w*`, linear fallback, mutagen wav/mp3 only, SoX for `global_speed`, transcription via stable-ts | v0.4.0 source code | ✅ |
| Gemini TTS default model `gemini-3.1-flash-tts-preview`, voice "Kore", 24 kHz | manim-voiceover `gemini.py` | ✅ |
| Kokoro: `pip install kokoro>=0.9.4 soundfile`, espeak-ng, `KPipeline(lang_code=…)`, `h` = Hindi, 24 kHz, Apache-2.0 | github.com/hexgrad/kokoro | ✅ |
| Kokoro Hindi voices hf_alpha/hf_beta/hm_omega/hm_psi (grade C); af_heart A, af_bella A- | HF `VOICES.md` | ✅ |
| IndicF5: install, `model(text, ref_audio_path=…, ref_text=…)`, int16→float32, 24 kHz, 11 languages, ~0.4B, MIT card, gated | HF card + GitHub README (code block exact match kiya) | ✅ (license ⚠️ conflict noted) |
| IndicF5 Roman-script UTF-8 byte bug + patch; eval scores (4.70 patched, 2.13 unpatched, Parler 3.40, Kokoro 3.90) | github.com/harrrshall/hinglish-tts README | ✅ (self-run, small eval) |
| Indic Parler-TTS: install, usage, description prompts, speakers (Rohit/Divya; Thoma/Mary), 21 languages, Apache-2.0, gated | HF card | ✅ |
| Veena: 3B Llama, SNAC 24 kHz, speakers kavya/agastya/maitri/vinaya, 4-bit NF4, latency (4090 ~200 ms), Apache-2.0 tag + "proprietary" header | HF card | ✅ (license ⚠️) |
| Chatterbox: `pip install chatterbox-tts`, Multilingual V3 (500M, `t3_model="v3"`), 23 languages incl. `hi`, `generate(text, language_id, audio_prompt_path, exaggeration, cfg_weight, …)`, tips, Perth watermark, MIT | GitHub README + `mtl_tts.py` source (signature) | ✅ |
| WhisperX: `pip install whisperx`, CUDA 12.8 toolkit note, BSD-2, Hindi align model `theainerd/Wav2Vec2-large-xlsr-hindi` | GitHub README + `alignment.py` | ✅ |
| stable-ts: `pip install -U stable-ts`, `model.align('audio.mp3', text, language='en')`, MIT, ffmpeg in PATH | GitHub README | ✅ |
| HyperFrames: Apache-2.0, Node 22+, FFmpeg, `npx hyperframes init/preview/render`, composition attributes, GSAP paused timeline in `window.__timelines`, Claude Code plugin commands, deterministic frame seek | github.com/heygen-com/hyperframes README | ✅ (framework naya hai; API change ho sakti hai) |
| Remotion license: free for individuals, ≤3-employee for-profit, non-profits, evaluation; Company License otherwise; v5 change note | GitHub `LICENSE.md` | ✅ |
| Remotion pricing: Creators $25/mo/seat, Automators $0.01/render ($100/mo min), Enterprise from $500/mo | remotion.dev pricing (search result) | ✅ (check before buying) |
| YouTube upload specs: MP4 + faststart, H.264 High, 2 B-frames, closed GOP half fps, 4:2:0, AAC-LC/Opus, 48 kHz, 1080p30 8 Mbps / 1440p30 16 Mbps | support.google.com/youtube/answer/1722171 | ✅ |
| YouTube chapters: 00:00 first, ≥3, ascending, ≥10 s | support.google.com/youtube/answer/9884579 | ✅ |
| YouTube ~−14 LUFS normalization; doesn't boost quiet audio | Multiple secondary sources (Meterplugs/Ian Shepherd 2019, Youlean) | ⚠️ widely measured, officially undocumented |
| Mayer 12 principles (+Embodiment 2020) | Multiple summaries + Mayer 2020 handout | ✅ |
| Guo, Kim & Rubin 2014: 6.9M sessions, 4 edX courses; findings | Paper abstract (L@S 2014) | ✅ (abstract) |
| "~6 minute" engagement number | – | ⚠️ abstract mein nahi; full paper check karo |
| E-learning narration ~150 wpm default; dense 110–130 | Vendor sources | ⚠️ planning figure |
| TheoremExplainAgent: 2-agent, Manim, >5 min videos, 240 theorems, 5 metrics, o3-mini 93.8% / 0.77, layout issues | arXiv 2502.19400 abstract | ✅ |
| Code2Video: tri-agent, visual anchors, layout 0.59→0.91, Claude-4-Opus best code, MMMC, TeachQuiz, MIT | arXiv 2510.01174 + GitHub README | ✅ |
| Paper2Video: authors, PaperTalker components, 101 papers, metrics | arXiv 2510.05096 + NeurIPS listing | ✅ |
| VibeVoice TTS code pulled by Microsoft (Sept 2025) | Multiple secondary sources | ✅ (secondary) |
| FLUX.1 schnell Apache-2.0, dev non-commercial; FLUX.2 klein split | Wikipedia + secondary | ✅ / ⚠️ (klein) |
| Qwen-Image Apache-2.0, 20B MMDiT, ComfyUI native | docs.comfy.org | ✅ |
| LatentSync 1.6 Apache-2.0, min 18 GB VRAM (1.5: 8 GB) | GitHub README | ✅ |
| InfiniteTalk Apache-2.0, Wan2.1-I2V-14B base, image/video-to-video, 480p/720p | GitHub README | ✅ |
| MuseTalk code MIT vs HF weights openrail tag | Project disclaimer + HF card | ⚠️ conflict noted |
| WCAG contrast ratios of palette | Computed (WCAG formula) | ✅ |

---

## 3. Code tested (actually run)

| Doc | Snippet | Result |
|---|---|---|
| [08](08_Math_Verification_Step.md) | `verify.py` helpers (`entropy`, `info_gain`, `Table`, `count`, `evaluate`) on PlayTennis | ✅ All values match (H=0.940286, Outlook 0.246750, Humidity 0.151836, Wind 0.048127, Temp 0.029223) |
| [14](14_Pronunciation_Text_Normalization.md) | `number_to_words`, `replace_numbers`, `apply_dict`, `validate_tts_text` | ✅ Asserts pass |
| [17](17_Manim_Basics_Install_Concepts.md) | `EntropyCalc` (MathTex) | ⚠️ Test machine par `standalone.cls` aur `dvisvgm` missing the (BasicTeX). Ye environment issue hai, code issue nahi, aur troubleshooting mein document kiya |
| [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) | `PrebakedService` + `test_prebaked.py` | ✅ (fixes ke baad) 5.03 s, mp4 + srt + wav |
| [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) | `LessonScene` with fake topic (with/without `words/`) | ✅ (fix ke baad) 6.6 s, bookmark fallback + aligned |
| [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) | `LocalTTSService` | ✅ Import OK (server ke bina render test nahi kiya) |
| [19](19_Manim_Component_Library_Design.md) | `HighlightTable`, `ResultBox`, `BarCompare`, `TreeDiagram`, `BallBox`, `PauseTimer` (render + images dekhe) | ✅ (layout fixes ke baad) |
| [19](19_Manim_Component_Library_Design.md) | `EquationSteps` | ⚠️ Not render-tested (LaTeX toolchain) |
| [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md) | `place()` | ✅ 10×10 square → 5.6×5.6 at (−3.35, −0.3) |
| [21](21_AI_Se_Manim_Code_Generation.md) | `static_check` | ✅ (fix ke baad) hardcoded number + small font dono pakde |
| [22](22_Critic_Loop_Visual_QA.md) | `LayoutAuditMixin` | ✅ Planted issues + 1 unplanned issue pakda |
| [22](22_Critic_Loop_Visual_QA.md) | `beat_end_times`, `freezedetect` | ✅ |
| [15](15_Audio_Post_Processing_Loudness_Music.md) | silence trim, `loudnorm_2pass`, ducking (`sidechaincompress`) | ✅ (fix ke baad) trim 3.2→2.1 s; −14.0 LUFS; ducked mix duration = narration |
| [16](16_Word_Timestamps_Forced_Alignment_Captions.md) | `fmt_srt`, `words_to_srt`, `to_word_boundaries` | ✅ (fix ke baad) |
| [27](27_FFmpeg_Final_Assembly.md) | normalize → concat (video/audio) → loudnorm → FFMETADATA chapters → mux → soft subs | ✅ 1920×1080 30fps yuv420p, AAC 48k, chapters, faststart, −14.0 LUFS |
| [31](31_Avatar_Talking_Head_Optional.md) | Circular PiP overlay | ✅ Image check kiya, colors sahi |
| [32](32_Publishing_YouTube.md) | `yt_chapters` | ✅ (fix ke baad) |

**Not tested (environment/hardware ki wajah se):** TTS models (GPU + gated downloads), WhisperX/stable-ts alignment, HyperFrames render, ComfyUI, Remotion, local LLMs, Windows-specific commands. Ye sab official docs ke patterns par based hain, aur pilot ([33](33_Pilot_Plan_L20_Entropy_Information_Gain.md)) mein inka pehla real run hoga.

---

## 4. Bugs jo testing mein mile (aur fix hue)

| # | Doc | Bug | Fix |
|---|---|---|---|
| 1 | 18 | `PrebakedService` ke `input_data` mein `input_text` nahi tha, isliye v0.4.0 strict validation se `ValueError: Invalid voiceover cache entry` | `input_data` mein `input_text` + `service` add |
| 2 | 18 | Empty `word_boundaries` list falsy hone ki wajah se set nahi hoti thi, isliye `wait_until_bookmark` exception | `if "word_boundaries" in beat` |
| 3 | 18 | `LessonScene` word boundaries pass nahi karta tha, isliye bookmark beat crash | `words/` file se boundaries, warna `[]` |
| 4 | 19 | Table fixed column width, isliye lambe headers overlap | Content-based column widths |
| 5 | 19 | `box_rows` non-contiguous rows ke liye ek bada box banata tha | Har row ka alag box |
| 6 | 19 | Bar chart labels takra rahe the | Auto-shrink long labels |
| 7 | 19 | Tree edge labels ("Overcast"/"Rain") takra rahe the | Labels at 60% of edge + background |
| 8 | 08 | Pure set par `entropy` ne `-0.0` diya, isliye display check "-0" ≠ "0" | `max(0.0, …)` |
| 9 | 15 | ffmpeg 8.x: loudnorm JSON output ke beech mein aata hai, isliye regex fail | Aakhri `{…}` block parse |
| 10 | 15 | loudnorm output 192 kHz (internal upsample) | `-ar 48000` hamesha (gotcha documented) |
| 11 | 16 | `fmt_srt` 1.9996 s par ",1000" bana sakta tha | Total ms se calculate |
| 12 | 21 | `static_check` `T(..., size=20)` miss karta tha | Regex `font_size|size` |
| 13 | 32 | 1 ghante se lamba video: mixed timestamp formats | Sab h:mm:ss |
| 14 | 20 | MUTED ko "sabse kam contrast" kaha tha, jabki PURPLE kam hai | Computed values table |

---

## 5. Pichhli chat ke jawab mein corrections

| Pichhla claim | Correct |
|---|---|
| Loudness target "−16 LUFS" | YouTube-first ke liye **−14 LUFS** (−16 podcasts ka common target hai) |
| "Veena: claims unverified" | Model card mil gaya: 3B, Apache-2.0 tag (header par "proprietary" bhi), code-mixed support. Independent benchmark abhi bhi nahi mila |
| Remotion "4+ logon ki company ke liye paid" | ✅ Sahi (LICENSE.md se confirm) |
| manim-voiceover "OpenAI Whisper se word timing" | v0.4.0 mein transcription **stable-ts** (`stable_whisper`) se hoti hai, jo Whisper-based hai |

---

## 5a. Update 2 (2026-10-18): Mac + Budget mode

### Naye facts verified
| Claim | Source | Status |
|---|---|---|
| Test machine = Apple M1, 8 GB, 4P+4E CPU, 7-core GPU, macOS 26.6.2, ~29 GB free | `sysctl`, `system_profiler` | ✅ (user ka 40-core/64 GB Mac alag machine hai) |
| Kokoro: Apple Silicon GPU ke liye `PYTORCH_ENABLE_MPS_FALLBACK=1` | Kokoro README ("MacOS Apple Silicon GPU Acceleration") | ✅ |
| Chatterbox: `device="mps"` option + official `example_for_mac.py` (`torch.load` map_location patch) | Chatterbox README + repo file | ✅ (English example; Multilingual same pattern, untested) |
| F5-TTS upstream MPS auto-detect (`get_default_device`, `torch.accelerator`) + `PYTORCH_ENABLE_MPS_FALLBACK` | F5-TTS `device_utils.py`, `utils_infer.py` | ✅ (IndicF5 fork ka behaviour untested) |
| Parler: Apple Silicon par bfloat16 ke liye naya PyTorch | Parler README | ✅ |
| mlx-whisper install/usage/`word_timestamps`; `mlx-community/whisper-large-v3-turbo` repo exists | mlx-examples README + HF API | ✅ |
| mlx-audio: MIT; Kokoro/Chatterbox/CSM/Dia/Spark/Qwen3-TTS/Voxtral; `mlx-community/Kokoro-82M-bf16` exists | GitHub README + HF API | ✅ |
| Ollama macOS: `.dmg`, macOS 14+, models `~/.ollama` | docs.ollama.com/macos | ✅ |
| `qwen3-coder:30b` 19 GB, 256K ctx; 30.5B/3.3B active, Apache-2.0, non-thinking | ollama.com library + HF card | ✅ |
| Draw Things free (IAP), FLUX + Qwen-Image support | App Store listing + reviews | ✅ (secondary for model list) |
| Homebrew casks `font-inter`, `font-noto-sans-devanagari`, `font-jetbrains-mono`, `mactex-no-gui`, `basictex` exist | `brew info --cask` | ✅ |
| Manim minimal LaTeX package list | Manim install docs | ✅ |
| `tlmgr --usermode install dvisvgm` fails ("not relocatable") | Is Mac par chala kar | ✅ seen |
| `brew install dvisvgm` → texlive + openjdk dependencies | `brew deps dvisvgm` | ✅ seen |

### Naya code tested
| Doc | Code | Result |
|---|---|---|
| [41](41_Template_Engine_Zero_Cost_Animation.md) | `template_engine.py` (`TemplateScene`, 19 actions, `validate_actions`) with LessonScene + PrebakedService + components | ✅ 2 scenes rendered (14.2 s, 9.3 s); frames checked (table, highlight, bookmark label, `{num:}` numbers, bars + crown, bullets, timer) |
| [41](41_Template_Engine_Zero_Cost_Animation.md) | `validate_actions` on broken script | ✅ caught 4/4 planted errors |
| [41](41_Template_Engine_Zero_Cost_Animation.md) | `math` action | ⚠️ not rendered (no dvisvgm on test Mac) |

### Not tested (Mac)
TTS models MPS par (Kokoro/Chatterbox/IndicF5/Parler/Veena), mlx-whisper run, Ollama run, Draw Things. Inke liye 64 GB Mac par pehla run pilot mein hoga.

---

## 6. Abhi bhi unverified / tumhe check karna hai

- [ ] 64 GB MacBook ka exact chip/CPU cores ([40](40_Mac_Apple_Silicon_Setup.md) §0 commands)
- [ ] Mac par TTS models MPS par chalte hain ya nahi (Kokoro, Chatterbox ML, IndicF5, Parler)
- [ ] Template engine ka `math` action (LaTeX wali machine par)
- [ ] IndicF5 aur Veena ka exact commercial-use license
- [ ] harrrshall patch ka license (commercial ke liye)
- [ ] WhisperX ko custom (known-text) segments dena: pehli baar chala kar check karo
- [ ] HyperFrames render CLI flags (output path, fps): `npx hyperframes render --help`
- [ ] Guo et al. ka "6 minute" number (full paper)
- [ ] TTS bake-off results ([13](13_TTS_BakeOff_Kaise_Kare.md))
- [ ] Render time / token cost numbers (pilot, [33](33_Pilot_Plan_L20_Entropy_Information_Gain.md) §5)

---

## 7. Test machine par jo install hua (transparency)

Docs ka code test karne ke liye is Mac par ye hua:
- Homebrew se `cairo` + `pkgconf` (aur unki dependencies), kyunki Manim ke `pycairo` ko chahiye
- TeX Live user tree mein `standalone` + `preview` LaTeX packages (`tlmgr --usermode`)
- Scratch venv (session scratchpad mein) jisme manim 0.22.0, manim-voiceover 0.4.0, soundfile, numpy, requests
- `brew install dvisvgm` start hua tha, lekin wo poora TeX Live + Java kheench raha tha (kai GB), isliye beech mein rok diya. Usse kuch install nahi hua (verify kiya)

Hatana ho to: `brew uninstall cairo pkgconf` (agar kisi aur cheez ko nahi chahiye), aur `~/Library/texmf` folder.
