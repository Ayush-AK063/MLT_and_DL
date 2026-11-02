# 29 · Hardware aur Environment Setup (High-End PC)

> 🍎 **MacBook use kar rahe ho? (recommended budget path)** → [40_Mac_Apple_Silicon_Setup.md](40_Mac_Apple_Silicon_Setup.md) dekho. Ye file Windows/Linux + NVIDIA ke liye hai (full mode / optional).

> **Is file mein:** High-end PC (maan ke chal rahe hain Windows + NVIDIA GPU) par poora environment setup: drivers, CUDA/PyTorch, Python envs, Manim + LaTeX, Node (HyperFrames), ffmpeg, fonts, aur verification. WSL2 option bhi.

> ℹ️ Abhi tak confirm nahi hua ki PC Windows hai ya Linux, aur GPU/VRAM kitna hai. Isliye ye guide Windows + NVIDIA maan kar likhi hai, aur Linux ke notes saath mein hain. Apne specs yahan bharo:
> | Component | Value |
> |---|---|
> | OS | |
> | CPU (cores/threads) | |
> | RAM | |
> | GPU / VRAM | |
> | Storage (free) | |

---

## 1. Hardware ka role

| Component | Kaam | Kitna chahiye (recommendation) |
|---|---|---|
| **GPU (NVIDIA)** | TTS, Whisper alignment, image gen, local LLM | 16–24 GB VRAM comfortable; 12 GB par bhi chhote models chal jaate hain |
| **CPU** | Manim render (parallel), ffmpeg | Jitne zyada cores utna achha (12–16+ cores ideal) |
| **RAM** | Parallel renders + models | 32 GB minimum, 64 GB comfortable |
| **SSD** | Cache, renders, models | 500 GB+ free (models + intermediate videos) |

> NVIDIA kyun? Zyadatar TTS/ML repos CUDA (PyTorch) assume karte hain. AMD/Apple par bhi kuch chalta hai, lekin setup mushkil hota hai.

---

## 2. Option A (recommended for most): Native Windows

### 2.1 NVIDIA driver
- Latest **Game Ready / Studio driver** (nvidia.com)
- Check: `nvidia-smi` (PowerShell) → GPU naam, driver version, VRAM aur max CUDA version dikhega

### 2.2 Basic tools
```powershell
winget install Git.Git
winget install Gyan.FFmpeg            # ya ffmpeg.org se build; PATH mein add karo
winget install OpenJS.NodeJS.LTS      # Node 22+ chahiye (HyperFrames)
winget install MiKTeX.MiKTeX          # LaTeX (Manim formulas)
```
Phir check:
```powershell
git --version; ffmpeg -version; node -v; latex --version
```
> winget package IDs badal sakte hain: `winget search ffmpeg` se confirm karo.

### 2.3 uv (Python manager)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv python install 3.12
```

### 2.4 Microsoft C++ Build Tools
Kuch Python packages compile hote hain. "Desktop development with C++" workload install karo (Visual Studio Build Tools).

### 2.5 MiKTeX setting
MiKTeX Console → Settings → "Install missing packages on-the-fly: **Always**". Warna Manim render ke beech mein package install popup aata hai, ya render fail ho jaata hai (jaise `standalone.cls not found`, jo humne apni test machine par bhi dekha tha).

---

## 3. Option B: WSL2 (Ubuntu on Windows)

**Kab:** Agar koi TTS repo sirf Linux par achha chalta hai (kai ML repos Linux-first hote hain).
```powershell
wsl --install -d Ubuntu
```
WSL ke andar:
```bash
sudo apt update && sudo apt install -y build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg texlive-latex-extra texlive-fonts-extra dvisvgm espeak-ng
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- WSL2 mein NVIDIA GPU (CUDA) Windows driver ke through kaam karta hai. WSL ke andar alag Linux display driver install **mat** karo, NVIDIA ki WSL guide follow karo
- Files WSL filesystem (`~/`) mein rakho, `/mnt/c/` par nahi, warna I/O bahut slow hota hai

**Hybrid (practical):** Manim + ffmpeg + HyperFrames native Windows par, aur TTS servers WSL mein (HTTP se baat karte hain, [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) §5). Ye bilkul theek chalta hai.

---

## 4. PyTorch + CUDA

Har TTS env mein PyTorch ka CUDA build install karo. Command **pytorch.org "Get Started"** page se lo (apne OS + CUDA version ke hisaab se), jaise:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```
Verify:
```python
import torch
print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))
```
> `cu128` sirf example hai. pytorch.org par jo current CUDA builds listed hain unme se chuno, aur driver itna naya ho ki wo CUDA version support kare (`nvidia-smi` mein "CUDA Version").

---

## 5. Environments layout

```
D:\mlt-video\
├── envs\
│   ├── main\            ← manim, manim-voiceover, pipeline (Python 3.12)
│   ├── tts-kokoro\
│   ├── tts-indicf5\     ← (conda/uv, Python 3.10 as per IndicF5 README)
│   ├── tts-parler\
│   ├── tts-veena\
│   ├── tts-chatterbox\
│   └── align\           ← stable-ts / whisperx
├── ComfyUI\             ← image generation
├── models\              ← HF cache (HF_HOME)
└── MLT_Python\          ← repo (lectures, video/)
```

```powershell
setx HF_HOME "D:\mlt-video\models\hf"       # model downloads ek jagah (C: drive na bhare)
```

### Main env
```powershell
cd D:\mlt-video\envs
uv venv main --python 3.12
main\Scripts\activate
uv pip install "manim==0.22.0" "manim-voiceover==0.4.0" soundfile numpy pyyaml jsonschema requests pydub jiwer
manim checkhealth
```

---

## 6. Fonts
Install karo (Windows: right-click → "Install for all users"):
- **Inter**
- **Noto Sans Devanagari**
- **JetBrains Mono**

Test:
```python
from manim import *
class F(Scene):
    def construct(self):
        self.add(VGroup(Text("Inter: Information Gain 0.2467", font="Inter"),
                        Text("नोटो: सूचना लाभ", font="Noto Sans Devanagari")).arrange(DOWN))
```
`manim -s -ql f.py F` → PNG kholo, dono fonts sahi dikhne chahiye.

---

## 7. SoX (optional)
manim-voiceover import par "SoX could not be found!" warning deta hai. Speed change use nahi karte to ignore karo. Install karna ho to SoX ki official site/package manager se install karo aur PATH mein daalo.

---

## 8. Verification script (sab ek saath)

```python
# tools/check_env.py
import shutil, subprocess, importlib

def ok(name, cond, extra=""):
    print(("✅" if cond else "❌"), name, extra)

for tool in ["ffmpeg", "ffprobe", "node", "latex", "dvisvgm", "git"]:
    ok(tool, shutil.which(tool) is not None)

node_v = subprocess.run(["node", "-v"], capture_output=True, text=True).stdout.strip() if shutil.which("node") else ""
ok("node >= 22", node_v.startswith("v") and int(node_v[1:].split(".")[0]) >= 22, node_v)

for mod in ["manim", "manim_voiceover", "soundfile", "numpy", "yaml", "jsonschema"]:
    try:
        m = importlib.import_module(mod)
        ok(mod, True, getattr(m, "__version__", ""))
    except Exception as e:
        ok(mod, False, str(e)[:80])

try:
    import torch
    ok("torch CUDA", torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else "")
except ImportError:
    ok("torch (main env mein optional)", True, "not installed")
```

---

## 9. Power/thermal tips
- Lambe renders ke liye **sleep/hibernate band** karo
- GPU + CPU dono full load par heat badhti hai, isliye cabinet airflow check karo
- UPS ho to achha hai (raat bhar ka render bijli jaane par ruk jaata hai, lekin Manim cache se resume ho jaata hai)

👉 Agla: [30_Local_LLMs_Kab_Aur_Kaise.md](30_Local_LLMs_Kab_Aur_Kaise.md)
