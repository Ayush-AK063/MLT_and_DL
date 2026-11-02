# 40 · Mac (Apple Silicon) Setup: Poori Pipeline MacBook Par

> **Is file mein:** Poori video pipeline ko MacBook (Apple Silicon: M1–M5, khaas kar 40-core GPU + 64 GB wala Max) par **bina extra kharche** chalane ka step-by-step setup: Homebrew, Python, Manim + LaTeX, ffmpeg, fonts, PyTorch (MPS), Mac par chalne wale TTS, Whisper (MLX), local LLM (Ollama / LM Studio), image generation (Draw Things), memory planning, aur heat/battery tips.
>
> Windows + NVIDIA ke liye [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) dekho. Zero-cost workflow ka overview: [42](42_Budget_Mode_Zero_Cost_Plan.md).

---

## 0. Pehle apna Mac pehchano

```bash
sysctl -n machdep.cpu.brand_string          # chip (jaise "Apple M4 Max")
sysctl -n hw.perflevel0.physicalcpu         # performance (P) cores
sysctl -n hw.perflevel1.physicalcpu         # efficiency (E) cores
echo "$(( $(sysctl -n hw.memsize) / 1073741824 )) GB RAM"
system_profiler SPDisplaysDataType | grep "Total Number of Cores"    # GPU cores
df -h /                                     # free disk
```

> ℹ️ **Note (2026-10-18):** Jis Mac par ye docs test hue wo **Apple M1, 8 GB, 4P+4E CPU, 7-core GPU, ~29 GB free disk** tha. Tumhara 40-core GPU + 64 GB wala MacBook alag machine hai. Ye guide dono ke liye hai: section 9 mein dono ka comparison hai.
>
> 40-core GPU wale Max chips (jaise M3 Max / M4 Max) mein aam taur par **16 CPU cores (12P + 4E)** hote hain. Apna exact count upar ke command se confirm karo.

### Apple Silicon kyun achha hai is kaam ke liye
| Cheez | Matlab |
|---|---|
| **Unified memory** | CPU aur GPU ek hi RAM share karte hain. 64 GB = model ke liye ~45–50 GB tak usable (macOS + apps ke baad). NVIDIA laptop GPUs mein aam taur par 8–16 GB VRAM hi hoti hai |
| **MPS (Metal Performance Shaders)** | PyTorch ka Mac GPU backend (`device="mps"`) |
| **MLX** | Apple ka apna ML framework, Apple Silicon ke liye optimized (mlx-whisper, mlx-audio, mlx-lm) |
| **Kam bijli** | Full load par bhi ~40–140 W (chip par depend), jabki gaming PC 400–700 W leta hai |

### Limitations (honest)
- **CUDA nahi hai**, isliye NVIDIA-only cheezein (`bitsandbytes` 4-bit, kuch custom CUDA kernels, TensorRT) nahi chalengi. Veena ka official 4-bit setup isi wajah se as-is nahi chalega
- MPS par kuch operations abhi supported nahi hain. Unke liye `PYTORCH_ENABLE_MPS_FALLBACK=1` set karo (wo ops CPU par chale jaate hain)
- Manim rendering CPU par hoti hai, isliye GPU cores yahan kaam nahi aate. Lekin Max chips ke 12+ P-cores parallel rendering ke liye kaafi achhe hain

---

## 1. Basic tools (Homebrew)

```bash
# Homebrew (agar nahi hai)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install git ffmpeg node espeak-ng cairo pkg-config
brew install --cask font-inter font-noto-sans-devanagari font-jetbrains-mono
```
| Package | Kis liye |
|---|---|
| `ffmpeg` | Assembly, audio processing ([27](27_FFmpeg_Final_Assembly.md)) |
| `node` | HyperFrames (Node 22+ chahiye: `node -v` check karo) |
| `espeak-ng` | Kokoro TTS ka fallback phonemizer |
| `cairo pkg-config` | Manim ke `pycairo` ke liye (official Manim docs). ✅ Is test Mac par bina iske `pycairo` build fail hua tha |
| Fonts | Style guide ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) |

> Font cask names badal sakte hain. `brew search font-inter` se confirm karo, ya fonts Google Fonts se download karke Font Book mein install karo.

### SoX (optional)
```bash
brew install sox      # manim-voiceover ki "SoX could not be found!" warning hatane ke liye (zaroori nahi)
```

---

## 2. LaTeX (formulas ke liye)

Do options hain:

| Option | Size | Kab |
|---|---|---|
| **MacTeX (full)** | Bada (kai GB) | Disk space hai to sabse simple: sab kuch included |
| **BasicTeX + packages** | Chhota | Disk kam hai (jaise 8 GB / 256 GB wale Mac) |

### MacTeX
```bash
brew install --cask mactex-no-gui
```
Install ke baad naya terminal kholo (`/Library/TeX/texbin` PATH mein aa jaata hai).

### BasicTeX + Manim ke packages
```bash
brew install --cask basictex
# naya terminal kholo, phir:
sudo tlmgr update --self
sudo tlmgr install amsmath babel-english cbfonts-fd cm-super count1to ctex doublestroke dvisvgm everysel \
  fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin mathastext microtype multitoc \
  physics preview prelim2e ragged2e relsize rsfs setspace standalone tipa wasy wasysym xcolor xetex xkeyval
```
(Package list Manim ke official "minimal LaTeX" section se hai.)

> ⚠️ **Testing mein dekha:**
> - BasicTeX par Manim ka `MathTex` pehle `standalone.cls not found` deta hai, phir `dvisvgm` not found. Upar ki list dono fix karti hai
> - `tlmgr --usermode install dvisvgm` **kaam nahi karta** ("package dvisvgm is not relocatable"), kyunki dvisvgm binary hai. Isliye `sudo` ke saath install karna padta hai
> - `brew install dvisvgm` **mat karo**: ye dependency mein poora Homebrew TeX Live + Java (kai GB) kheench leta hai. TeX ka apna dvisvgm (tlmgr se) use karo

Check:
```bash
which latex dvisvgm
```

---

## 3. Python + Manim

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12

mkdir -p ~/mlt-video/envs && cd ~/mlt-video/envs
uv venv main --python 3.12
source main/bin/activate
uv pip install "manim==0.22.0" "manim-voiceover==0.4.0" soundfile numpy pyyaml jsonschema requests pydub jiwer
manim checkhealth        # end mein test render ke liye y/n poochta hai
```
✅ manim 0.22.0 + manim-voiceover 0.4.0 is test Mac (M1, Python 3.12) par install hue aur render kiya.

### Manim render settings (Mac)
```bash
manim -ql scene.py S05                 # preview
manim -qh --fps 30 scene.py S05        # final 1080p30
```
Parallel rendering ke workers ([26](26_Rendering_Performance_Parallel.md)):
| Mac | Suggested workers |
|---|---|
| Max (12P + 4E, 64 GB) | 8–10 |
| Pro (10–12 cores, 18–36 GB) | 5–7 |
| M1/M2 base (4P + 4E, 8 GB) | 2–3 (RAM limit) |

---

## 4. PyTorch (MPS)

```bash
uv pip install torch torchaudio
python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"
```
Mac par PyTorch ka normal pip wheel hi MPS support ke saath aata hai, alag CUDA build ki zaroorat nahi.

**Har TTS script ke upar (ya shell mein):**
```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
```
Isse jo ops MPS par nahi hain wo crash karne ki jagah CPU par chal jaate hain.

---

## 5. TTS on Mac

| Model | Mac par | Kaise | Status |
|---|---|---|---|
| **Kokoro-82M** | ✅ Bahut achha | Official README: Apple Silicon GPU ke liye `PYTORCH_ENABLE_MPS_FALLBACK=1`. Ya **mlx-audio** (MLX version, `mlx-community/Kokoro-82M-bf16`) | Documented |
| **Chatterbox (English + Multilingual/Hindi)** | ✅ | Official `example_for_mac.py`: `device="mps"` + `torch.load` ko `map_location` patch | Documented (English example); Multilingual same pattern, test karo |
| **IndicF5** | ⚠️ Probably | Upstream F5-TTS `get_default_device()` MPS detect karta hai aur `PYTORCH_ENABLE_MPS_FALLBACK=1` set karta hai. IndicF5 apna pinned version use karta hai, isliye test karna padega | Test karo |
| **Indic Parler-TTS** | ⚠️ | Parler README: Apple Silicon par bfloat16 ke liye naya PyTorch chahiye | Test karo |
| **Veena (3B)** | ⚠️ | Official 4-bit `bitsandbytes` NVIDIA-only hai. 64 GB Mac par bina quantization (bf16/fp16, ~6–7 GB weights) load karke try kar sakte ho, lekin slow ho sakta hai | Experimental |
| **mlx-audio models** | ✅ | MIT license library; Kokoro, Chatterbox, CSM, Dia, Spark, Qwen3-TTS, Voxtral TTS jaise models MLX par. README Hindi ko Kokoro aur Voxtral TTS ke languages mein list karta hai | Documented |

### Kokoro (Mac)
```bash
uv venv ~/mlt-video/envs/tts-kokoro --python 3.12 && source ~/mlt-video/envs/tts-kokoro/bin/activate
uv pip install "kokoro>=0.9.4" soundfile
export PYTORCH_ENABLE_MPS_FALLBACK=1
python kokoro_test.py          # [10](10_TTS_Setup_Kokoro.md) ka code as-is
```

### Kokoro via mlx-audio (alternative, MLX native)
```bash
uv pip install mlx-audio misaki
```
```python
from mlx_audio.tts.utils import load_model
import numpy as np, soundfile as sf

model = load_model("mlx-community/Kokoro-82M-bf16")
chunks = [np.array(r.audio) for r in model.generate(text="Entropy measures disorder.",
                                                     voice="af_heart", speed=1.0, lang_code="a")]
sf.write("out.wav", np.concatenate(chunks), 24000)
```
> README ki Kokoro language-code table mein Hindi code listed nahi tha (jabki language list mein HI hai). Hindi ke liye pehle official `kokoro` package (`lang_code='h'`) try karo.

### Chatterbox (Mac pattern, official example se)
```python
import torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

device = "mps" if torch.backends.mps.is_available() else "cpu"
_orig_load = torch.load
def _load(*a, **k):
    k.setdefault("map_location", torch.device(device))   # CUDA pe save hue weights Mac par load ho sakein
    return _orig_load(*a, **k)
torch.load = _load

mtl = ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")
wav = mtl.generate("अब हम entropy calculate करते हैं।", language_id="hi",
                   audio_prompt_path="voice_refs/my_voice_ref.wav")
ta.save("cb_hi_mac.wav", wav, mtl.sr)
```
> Official Mac example `ChatterboxTTS` (English) ke liye hai. Multilingual class par same `map_location` patch apply hona chahiye. Pehli baar chala kar confirm karo.

---

## 6. Whisper / alignment on Mac (MLX)

```bash
uv pip install mlx-whisper        # ffmpeg chahiye (brew install ffmpeg)
```
```python
import mlx_whisper

out = mlx_whisper.transcribe("audio/b042.wav",
                             path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
                             word_timestamps=True)
words = [{"word": w["word"], "start": w["start"], "end": w["end"]}
         for seg in out["segments"] for w in seg["words"]]
```
- Default model `mlx-community/whisper-tiny` hai. Accuracy ke liye bada model lo (repo names Hugging Face par mlx-community ke Whisper collection mein dekho)
- Ye **transcription** hai (known-text forced alignment nahi). Chhote beats mein word timings aam taur par kaafi achhe hote hain, aur `to_word_boundaries()` ([16](16_Word_Timestamps_Forced_Alignment_Captions.md) §6) transcribed words ko script text se match kar leta hai
- TTS bake-off ka ASR intelligibility check ([13](13_TTS_BakeOff_Kaise_Kare.md)) bhi isi se ho jaata hai
- stable-ts bhi Mac par chalta hai (PyTorch), lekin MLX version Apple Silicon par aam taur par tez hota hai

---

## 7. Local LLM on Mac

### Option A: Ollama (simplest)
- Download: ollama.com, `.dmg` kholo aur Applications mein drag karo (macOS 14 Sonoma+ chahiye). Pehli baar kholne par CLI link banane ka option deta hai
- Models `~/.ollama` mein store hote hain (bade hote hain, disk dekho)
```bash
ollama pull qwen3-coder:30b        # 19 GB; 30.5B total / 3.3B active (MoE), 256K context, Apache-2.0
ollama run qwen3-coder:30b
```
- OpenAI-compatible API: `http://localhost:11434/v1/chat/completions` ([30](30_Local_LLMs_Kab_Aur_Kaise.md) §4 ka `local_llm()` as-is chalega)
- **MoE kyun Mac par achha hai:** Har token ke liye sirf ~3.3B parameters active hote hain, isliye speed chhote model jaisi milti hai, jabki knowledge 30B jaisa rehta hai. 64 GB unified memory mein 19 GB model aaram se fit hota hai
- Qwen3-Coder sirf non-thinking mode mein chalta hai (model card). Recommended sampling: temperature 0.7, top_p 0.8, top_k 20, repetition penalty 1.05. JSON/code ke liye temperature 0.2–0.3 rakho

### Option B: LM Studio
GUI app (free, closed-source). Isme MLX-format models bhi chalte hain, aur local server bhi milta hai (OpenAI-compatible).

### Option C: mlx-lm (command line, MLX native)
`pip install mlx-lm`, phir `mlx-community` ke converted models. Developers ke liye flexible hai.

### Kaun sa model kis kaam ke liye (64 GB Mac)
| Kaam | Model class | Memory |
|---|---|---|
| Script JSON / actions JSON | 30B-class instruct (MoE, jaise Qwen3 30B-A3B family) | ~19–20 GB (Q4) |
| Code fix (simple tracebacks) | Qwen3-Coder 30B-A3B | ~19 GB |
| Pronunciation list, titles, captions cleanup | Same, ya chhota (7–8B) | 5–8 GB |

> ⚠️ Model names tezi se badalte hain. `ollama.com/library` par current tags dekho. Upar ka `qwen3-coder:30b` tag aur size 2026-10-18 ko verify kiya.

---

## 8. Image generation on Mac

| Tool | Kya | License/cost |
|---|---|---|
| **Draw Things** (App Store) | Native Mac app; FLUX.1 schnell/dev, FLUX.2, Qwen-Image support (App Store listing/reviews ke hisaab se); offline | Free (in-app purchases), closed-source |
| **ComfyUI** | [23](23_Imagery_Local_Image_Generation.md) wala workflow; PyTorch MPS par chalta hai | Free, open-source |

- Model license wahi rehta hai jo [38](38_Licenses_Legal_Ethics.md) mein hai: **FLUX.1 schnell (Apache-2.0)** ya **Qwen-Image (Apache-2.0)** lo; FLUX.1 dev non-commercial hai
- Speed: secondary sources ke mutabik 16–24 GB Macs par ek 1024px FLUX image ~15–60 s leti hai. Max chips isse tez honge
- Budget mode mein images optional hain ([42](42_Budget_Mode_Zero_Cost_Plan.md)): pehle bina images ke videos banao

---

## 9. Memory planning

### 64 GB Max (tumhara target machine)
| Cheez | Approx memory |
|---|---|
| macOS + browser + editor | 8–12 GB |
| Local LLM (30B MoE, Q4) | ~19–22 GB |
| TTS model (Kokoro / Chatterbox / IndicF5) | 1–6 GB |
| Manim worker (har ek) | ~0.5–1.5 GB |
| ffmpeg | chhota |

**Rule:** Ek waqt par ek "bhari" kaam:
1. **LLM phase:** script / actions JSON banao → LLM band karo (`ollama stop <model>`)
2. **TTS phase:** saari audio → TTS server band
3. **Render phase:** 8–10 Manim workers

Teeno saath chalane se swap (disk par memory) shuru hota hai aur sab slow ho jaata hai.

### 8 GB M1 (jis par docs test hue)
| Kaam | Possible? |
|---|---|
| Manim render | ✅ (2–3 workers) |
| Kokoro TTS | ✅ |
| Chatterbox (500M) | ⚠️ Shayad (tight) |
| IndicF5 / Parler | ⚠️ Tight |
| Veena 3B | ❌ |
| 30B LLM | ❌ (max ~3–4B class models) |
| FLUX images | ❌ practically (bahut slow / memory) |

> 8 GB Mac par: script aur JSON Claude subscription se banao, TTS Kokoro se, render local. Bhari kaam 64 GB wale Mac par karo.

---

## 10. Heat, battery aur raat ke renders

```bash
caffeinate -i python build_video.py L20 --stage render --workers 8
```
- `caffeinate -i` command chalne tak Mac ko idle sleep se rokta hai (lid band karne par sleep hone se ye nahi rokta; external display/power setup ho to clamshell mode alag cheez hai)
- **Charger lagao.** Battery par macOS performance kam kar sakta hai, aur battery bhi garam hoti hai
- Laptop **stand** par rakho (neeche hawa), bed/takiye par nahi
- Max chips sustained load par fans tez chalayenge, ye normal hai
- Battery health ke liye: System Settings → Battery mein "Optimized Battery Charging" ON rakho

---

## 11. Mac environment check

```bash
python - <<'EOF'
import shutil, importlib, subprocess
def ok(n, c, x=""): print(("✅" if c else "❌"), n, x)
for t in ["ffmpeg", "ffprobe", "node", "latex", "dvisvgm", "espeak-ng", "ollama"]:
    ok(t, shutil.which(t) is not None)
for m in ["manim", "manim_voiceover", "soundfile", "numpy", "yaml"]:
    try:
        mod = importlib.import_module(m); ok(m, True, getattr(mod, "__version__", ""))
    except Exception as e:
        ok(m, False, str(e)[:60])
try:
    import torch; ok("torch MPS", torch.backends.mps.is_available(), torch.__version__)
except ImportError:
    ok("torch (TTS env mein)", True, "main env mein optional")
EOF
```

---

## 12. Folder layout (Mac)

```
~/mlt-video/
├── envs/
│   ├── main/            ← manim + pipeline
│   ├── tts-kokoro/
│   ├── tts-chatterbox/
│   ├── tts-indicf5/
│   └── align/           ← mlx-whisper
└── (models: ~/.ollama, ~/.cache/huggingface)
MLT_&_DL/MLT_Python/video/   ← pipeline code + out/
```
External SSD ho to `HF_HOME` aur Ollama models wahan rakh sakte ho, taaki internal disk na bhare:
```bash
export HF_HOME=/Volumes/SSD/hf
```

👉 Agla: [41_Template_Engine_Zero_Cost_Animation.md](41_Template_Engine_Zero_Cost_Animation.md)
