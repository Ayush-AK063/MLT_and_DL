# 10 · TTS Setup: Kokoro-82M

> **Is file mein:** Kokoro install (Windows/Linux/Mac), basic code, voices, speed control, long text handling, aur hamare pipeline ke `TTSBackend` interface ke saath wrapper.

---

## 1. Kokoro kya hai

- 82 million parameter ka open-weight TTS model (StyleTTS 2 based)
- **License: Apache-2.0** (weights bhi), isliye commercial use OK
- Output: **24 kHz** mono audio
- Repo: `github.com/hexgrad/kokoro`, weights: `hexgrad/Kokoro-82M` (Hugging Face)

---

## 2. Install

### Linux / WSL / Colab
```bash
pip install "kokoro>=0.9.4" soundfile
sudo apt-get install -y espeak-ng      # English OOD fallback + kuch non-English languages ke liye
```

### Windows (native)
```powershell
pip install "kokoro>=0.9.4" soundfile
# espeak-ng: GitHub releases page se *.msi installer download karke install karo
```

### macOS (Apple Silicon)
```bash
pip install "kokoro>=0.9.4" soundfile
brew install espeak-ng
export PYTORCH_ENABLE_MPS_FALLBACK=1     # official README: M1/M2/M3/M4 par GPU acceleration ke liye
```
**MLX alternative (Mac native):** `pip install mlx-audio misaki`, model `mlx-community/Kokoro-82M-bf16` ([40](40_Mac_Apple_Silicon_Setup.md) §5). Hindi ke liye pehle official `kokoro` package (`lang_code='h'`) use karo.

> **espeak-ng kyun?** Official README: "Install espeak, used for English OOD fallback and some non-English languages." Matlab jo words dictionary mein nahi hain (out-of-dictionary), unke liye fallback.

GPU: PyTorch CUDA build install karo ([29](29_Hardware_Environment_Setup_Windows_NVIDIA.md)). Kokoro CPU par bhi kaafi fast hai.

---

## 3. Basic usage (official pattern)

```python
from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code='a')        # 'a' = American English
text = "Entropy measures how mixed a dataset is."
generator = pipeline(text, voice='af_heart')
for i, (graphemes, phonemes, audio) in enumerate(generator):
    print(i, graphemes, phonemes)
    sf.write(f'{i}.wav', audio, 24000)
```

Generator text ko chunks mein todta hai (default newline par split hota hai), aur har chunk ka `(graphemes, phonemes, audio)` deta hai.

### Advanced options
```python
generator = pipeline(text, voice='af_heart', speed=1, split_pattern=r'\n+')
```
- `speed`: 1.0 normal; 0.9 thoda slow (technical content ke liye achha)
- `split_pattern`: text kahan todna hai

---

## 4. Language codes

| `lang_code` | Language |
|---|---|
| `a` | American English |
| `b` | British English |
| `e` | Spanish |
| `f` | French |
| **`h`** | **Hindi** |
| `i` | Italian |
| `j` | Japanese (`pip install misaki[ja]`) |
| `p` | Brazilian Portuguese |
| `z` | Mandarin (`pip install misaki[zh]`) |

**Rule:** `lang_code` aur voice ka prefix match hona chahiye (`h` → `hf_*`/`hm_*`).

---

## 5. Voices (VOICES.md se)

### Hindi
| Voice | Gender | Grade |
|---|---|---|
| `hf_alpha` | Female | C |
| `hf_beta` | Female | C |
| `hm_omega` | Male | C |
| `hm_psi` | Male | C |

### English (top graded)
| Voice | Grade | Notes |
|---|---|---|
| `af_heart` | A | Best overall ⭐ |
| `af_bella` | A- | |
| `af_nicole` | B- | |
| `bf_emma` | B- | British |

> Grade C ka matlab Hindi voices kam data par train hui hain. Bake-off mein compare karna hi padega.

---

## 6. Ek beat ko ek WAV mein (full audio join)

Generator multiple chunks de sakta hai. Ek beat = ek file chahiye:

```python
import numpy as np
import soundfile as sf
from kokoro import KPipeline

SR = 24000
_pipelines = {}

def kokoro_tts(text: str, out_path: str, voice: str = "af_heart",
               lang_code: str = "a", speed: float = 1.0) -> float:
    """Ek beat ka audio banao, WAV save karo, duration (sec) return karo."""
    if lang_code not in _pipelines:
        _pipelines[lang_code] = KPipeline(lang_code=lang_code)
    pipe = _pipelines[lang_code]
    chunks = [audio for _, _, audio in pipe(text, voice=voice, speed=speed, split_pattern=r'\n+')]
    audio = np.concatenate([np.asarray(c, dtype=np.float32) for c in chunks])
    sf.write(out_path, audio, SR, subtype="PCM_16")
    return len(audio) / SR
```

> `audio` torch tensor bhi ho sakta hai (version par depend). `np.asarray(c)` CPU tensor ke liye kaam karta hai; GPU tensor ho to `c.cpu().numpy()` karo.

---

## 7. Pipeline backend interface

Saare TTS backends ek hi interface follow karenge, taaki config badal kar model badal sako:

```python
# video/lib/tts/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class TTSResult:
    path: str
    duration_s: float
    sample_rate: int
    model_id: str
    voice_id: str

class TTSBackend(ABC):
    model_id: str

    @abstractmethod
    def synth(self, text: str, out_path: str) -> TTSResult: ...

    def cache_key(self) -> dict:
        """Jo bhi output ko affect karta hai, sab yahan aana chahiye."""
        return {"model": self.model_id}
```

```python
# video/lib/tts/kokoro_backend.py
from .base import TTSBackend, TTSResult
from ._kokoro_impl import kokoro_tts   # upar wala function

class KokoroBackend(TTSBackend):
    model_id = "hexgrad/Kokoro-82M"

    def __init__(self, voice="af_heart", lang_code="a", speed=1.0):
        self.voice, self.lang_code, self.speed = voice, lang_code, speed

    def synth(self, text, out_path):
        d = kokoro_tts(text, out_path, self.voice, self.lang_code, self.speed)
        return TTSResult(out_path, d, 24000, self.model_id, self.voice)

    def cache_key(self):
        return {"model": self.model_id, "voice": self.voice,
                "lang": self.lang_code, "speed": self.speed}
```

---

## 8. Tips aur gotchas

| Issue | Fix |
|---|---|
| Technical word galat bola ("sklearn") | Pronunciation dictionary: "scikit learn" ([14](14_Pronunciation_Text_Normalization.md)) |
| Numbers ajeeb bole | Script mein spoken form likho ("zero point nine four zero") |
| Hindi voice Roman text par ajeeb | Devanagari mein transliterate karke test karo; ya Hinglish ke liye dusra model |
| Beat ke end mein awaaz kat gayi | Sentence ke end mein full stop zaroor ho |
| Pace bahut tez | `speed=0.9` |
| Har beat ki shuruaat mein tone alag | Normal hai (har beat alag call); bake-off mein check karo ki kitna noticeable hai |

---

## 9. Quick test script

```python
tests = [
    ("a", "af_heart", "Information gain tells us which attribute reduces entropy the most."),
    ("h", "hf_alpha", "Ab hum entropy calculate karte hain. Answer aata hai zero point nine four zero."),
    ("h", "hf_alpha", "अब हम entropy calculate करते हैं। Answer आता है zero point nine four zero."),
]
for i, (lc, v, t) in enumerate(tests):
    d = kokoro_tts(t, f"kokoro_test_{i}.wav", voice=v, lang_code=lc)
    print(i, v, f"{d:.2f}s")
```
Teeno suno aur [13](13_TTS_BakeOff_Kaise_Kare.md) ki scoring sheet mein score karo.

👉 Agla: [11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md)
