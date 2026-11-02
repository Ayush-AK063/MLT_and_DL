# 11 · TTS Setup: Indic Models (IndicF5, Indic Parler-TTS, Veena)

> **Is file mein:** Hindi/Hinglish ke teen main open models ka install, code, gotchas, aur pipeline backend wrapper.

---

## 0. Common prerequisites

- **Hugging Face account + token** (teeno gated hain ya ho sakte hain: model page par terms accept karni padti hain)
  ```bash
  pip install -U huggingface_hub
  huggingface-cli login        # ya env var HF_TOKEN set karo
  ```
- **NVIDIA GPU + CUDA PyTorch** ([29](29_Hardware_Environment_Setup_Windows_NVIDIA.md))
- **Alag virtual env har model ke liye.** Ye models alag-alag `transformers`/`torch` versions maang sakte hain. Conflicts se bachne ke liye:
  ```
  envs/tts-indicf5/   envs/tts-parler/   envs/tts-veena/   envs/tts-kokoro/
  ```
  Pipeline backend ko subprocess/HTTP se call karo (section 5).

---

## 1. IndicF5 (AI4Bharat)

### Facts (model card se, 2026-10-18)
- ~0.4B params, F5-TTS architecture
- **11 languages:** Assamese, Bengali, Gujarati, **Hindi**, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu
- ~1417 hours training data (Rasa, IndicTTS, LIMMITS, IndicVoices-R)
- Output **24 kHz**
- License: card par **MIT**; access **gated** (contact info share karni hoti hai). ⚠️ Ek third-party source ke mutabik weights par attribution required hai aur commercial use restricted hai. Commercial use se pehle model card aur AI4Bharat ki terms dobara check karo
- Terms: sirf un awaazon ko clone karo jinki **explicit permission** hai

### Install
```bash
conda create -n indicf5 python=3.10 -y
conda activate indicf5
pip install git+https://github.com/ai4bharat/IndicF5.git
```

### Usage (official pattern)
```python
from transformers import AutoModel
import numpy as np
import soundfile as sf

repo_id = "ai4bharat/IndicF5"
model = AutoModel.from_pretrained(repo_id, trust_remote_code=True)

audio = model(
    "अब हम entropy calculate करते हैं।",                # bolne wala text
    ref_audio_path="voice_refs/my_voice_ref.wav",         # reference awaaz (5–15 s)
    ref_text="यह मेरी आवाज़ का एक छोटा सा नमूना है।",       # reference audio ka EXACT transcript
)

# Output int16 ho sakta hai, isliye float32 mein convert karke save karo
if audio.dtype == np.int16:
    audio = audio.astype(np.float32) / 32768.0
sf.write("out.wav", np.array(audio, dtype=np.float32), samplerate=24000)
```

> `trust_remote_code=True` ka matlab hai ki repo ka Python code tumhari machine par chalega. Ye AI4Bharat ka official repo hai, phir bhi model revision pin karo (`revision="<commit>"`).

### ⚠️ Roman-script (Hinglish) bug aur fix
**Problem:** IndicF5 generate kiye jaane wale audio ki length ko text ke **UTF-8 byte count** se estimate karta hai. Devanagari character ≈ 3 bytes, ASCII ≈ 1 byte. Isliye Roman text ko ~3× kam time milta hai, aur audio kat jaata hai ya silent aata hai.

**Fix:** `harrrshall/hinglish-tts` repo ka `inference.py` installed `f5_tts/infer/utils_infer.py` ko patch karta hai, taaki byte count ki jagah **non-whitespace character count** use ho. Patch idempotent hai (do baar lagane se kuch nahi bigadta), aur har call par `DEBUG-PATCH:` line print karta hai.

```bash
git clone https://github.com/harrrshall/hinglish-tts
cd hinglish-tts
# README ke hisaab se: HF_TOKEN set karo, phir patch status check karo
python inference.py placeholder --patch-status --ref-audio x --ref-text x --out /dev/null
```

> License note: Is repo ke `inference.py`/eval par "Free for research" likha hai (commercial ke liye author ko email karna hai), jabki sidebar Apache-2.0 dikhata hai. Commercial use se pehle clarify karo. Patch ka logic simple hai (byte count → char count), isliye zaroorat pade to apna patch khud likh sakte ho.

**Alternative (bina patch ke):** Hindi words ko Devanagari mein transliterate karo ([14](14_Pronunciation_Text_Normalization.md)). English technical words Latin mein reh sakte hain; mixed-script category mein bhi patched model ne achha score kiya tha.

### Reference audio tips
- 5–15 sec, ek hi speaker, no background noise/music
- Natural teaching tone mein bolo (jaise class mein padha rahe ho)
- `ref_text` **bilkul exact** ho (ek word bhi galat to quality girti hai)
- Same reference poore project mein use karo (consistency)
- Reference ki language/style output ko affect karti hai: Hinglish output chahiye to reference bhi Hinglish mein record karo

---

## 2. Indic Parler-TTS (AI4Bharat)

### Facts
- ~0.9B params; Parler-TTS architecture
- 21 officially supported languages incl. **Hindi aur English**
- **License: Apache-2.0**; access gated
- Do inputs: **transcript** (kya bolna hai) + **caption/description** (awaaz kaisi ho)
- Recommended speakers: Hindi **Rohit, Divya** (aur Aman, Rani); English **Thoma, Mary**

### Install
```bash
pip install git+https://github.com/huggingface/parler-tts.git
```

### Usage (official pattern)
```python
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = ParlerTTSForConditionalGeneration.from_pretrained("ai4bharat/indic-parler-tts").to(device)
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-parler-tts")
description_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

prompt = "अब हम entropy calculate करते हैं।"
description = ("Rohit's voice is clear and moderately paced, explaining like a friendly teacher, "
               "with a very close recording that has no background noise. Very clear audio.")

desc = description_tokenizer(description, return_tensors="pt").to(device)
text = tokenizer(prompt, return_tensors="pt").to(device)
generation = model.generate(
    input_ids=desc.input_ids, attention_mask=desc.attention_mask,
    prompt_input_ids=text.input_ids, prompt_attention_mask=text.attention_mask,
)
audio = generation.cpu().numpy().squeeze()
sf.write("parler_out.wav", audio, model.config.sampling_rate)
```

### Description tips (model card se)
- Speaker ka naam lo (consistency ke liye zaroori)
- "very clear audio" likhne se best quality aati hai
- Pace, pitch, expressivity describe kar sakte ho
- Transcript mein commas se chhote pauses aate hain
- **Consistency:** Poore project mein exactly same description string use karo, aur generation seed fix karo (`torch.manual_seed(…)`)

---

## 3. Veena (Maya Research)

### Facts (model card se)
- **3B** params, Llama-architecture autoregressive transformer
- Hindi + English, **code-mixed support**
- Audio codec: **SNAC**, output **24 kHz**
- Speakers: **kavya, agastya, maitri, vinaya**
- License tag: **Apache-2.0** (⚠️ page header par "proprietary" bhi dikhta hai; training data proprietary hai. Commercial use se pehle confirm karo)
- 4-bit NF4 quantization support
- Reported latency: H100 < 80 ms, A100 ~120 ms, **RTX 4090 ~200 ms**
- ⚠️ Card URL `maya-research/veena` hai, lekin code snippet `maya-research/veena-tts` load karta hai. Jo repo actually exist karta ho wahi use karo

### Install
```bash
pip install transformers torch torchaudio
pip install snac bitsandbytes
```

### Usage (card ke pattern ka simplified outline)
```python
import torch, soundfile as sf
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from snac import SNAC

model_id = "maya-research/veena-tts"   # card ke code ke hisaab se; verify karo
quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                           bnb_4bit_compute_dtype=torch.bfloat16,
                           bnb_4bit_use_double_quant=True)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quant,
                                             device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
snac_model = SNAC.from_pretrained("hubertsiuzdak/snac_24khz").eval().cuda()

speaker = "kavya"
text = "आज हम information gain सीखेंगे।"
prompt = f"<spk_{speaker}> {text}"
# ... card ke "Basic Usage" section ke hisaab se: special tokens add karo, model.generate se audio tokens lo,
#     tokens ko SNAC codes mein decode karo, snac_model.decode(...) se waveform banao
# sf.write("veena_out.wav", audio, 24000)
```

> Full generate + SNAC decode code lamba hai aur model card par diya hai. Use **as-is copy karo** (special token ids model-specific hain, guess mat karo).

### Gotchas
- Autoregressive model hai, isliye kabhi-kabhi words repeat ya skip ho sakte hain. ASR check zaroori hai ([13](13_TTS_BakeOff_Kaise_Kare.md))
- Lambe text par drift ho sakta hai, isliye beat-level chunks rakho
- Seed/temperature fix karo consistency ke liye

---

## 3a. 🍎 Mac (Apple Silicon) notes

| Model | Mac par kaise try karein |
|---|---|
| **IndicF5** | `export PYTORCH_ENABLE_MPS_FALLBACK=1`. Upstream F5-TTS ka `get_default_device()` MPS detect karta hai. IndicF5 apna pinned F5 version use karta hai, isliye pehli baar chala kar dekho ki `mps` par chalta hai ya CPU par gir jaata hai. CPU par bhi 0.4B model chal jaata hai, bas slow |
| **Indic Parler-TTS** | `device = "mps" if torch.backends.mps.is_available() else "cpu"`. Parler README ke mutabik Apple Silicon par bfloat16 ke liye naya PyTorch chahiye. Problem aaye to `torch_dtype=torch.float32` se load karo |
| **Veena** | Card ka 4-bit `BitsAndBytesConfig` NVIDIA-only hai. 64 GB Mac par `quantization_config` hata kar `torch_dtype=torch.float16`/`bfloat16`, `device_map="mps"` se try kar sakte ho (3B ≈ 6–7 GB weights). SNAC decoder ko `.to("mps")`. Experimental: speed aur stability test karo. 8 GB Mac par ❌ |

> Mac par server pattern (section 5) waise hi chalta hai. Bas har env mein PyTorch normal pip se install karo (MPS built-in hai). Detail: [40](40_Mac_Apple_Silicon_Setup.md).

---

## 4. Teeno ka quick comparison

| | IndicF5 | Indic Parler | Veena |
|---|---|---|---|
| Voice control | Reference audio (clone) | Text description | 4 fixed speakers |
| Apni awaaz | ✅ | ❌ | ❌ |
| Roman Hinglish | Patch ke baad strong (reported) | Kamzor (reported) | Code-mixed claimed |
| Size | 0.4B | 0.9B | 3B |
| License | MIT card (⚠️ check) | Apache-2.0 | Apache-2.0 (⚠️ check) |
| Determinism | Medium | Medium (seed fix karo) | Medium (seed fix karo) |

---

## 5. Pipeline integration: TTS server pattern

Alag envs ki wajah se har model ko ek chhote **local HTTP server** ke roop mein chalao. Pipeline sirf HTTP call karegi:

```python
# envs/tts-indicf5/server.py  (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np, soundfile as sf
from transformers import AutoModel

app = FastAPI()
model = AutoModel.from_pretrained("ai4bharat/IndicF5", trust_remote_code=True)
REF_AUDIO = "voice_refs/my_voice_ref.wav"
REF_TEXT = "..."

class Req(BaseModel):
    text: str
    out_path: str

@app.post("/synth")
def synth(r: Req):
    audio = model(r.text, ref_audio_path=REF_AUDIO, ref_text=REF_TEXT)
    audio = np.asarray(audio)
    if audio.dtype == np.int16:
        audio = audio.astype(np.float32) / 32768.0
    sf.write(r.out_path, audio.astype(np.float32), 24000, subtype="PCM_16")
    return {"duration_s": len(audio) / 24000, "sample_rate": 24000}
```

```bash
uvicorn server:app --port 8101      # IndicF5
# Parler 8102, Veena 8103, Chatterbox 8104, Kokoro 8105
```

```python
# video/lib/tts/http_backend.py
import requests
from .base import TTSBackend, TTSResult

class HTTPBackend(TTSBackend):
    def __init__(self, url, model_id, voice_id, extra_key=None):
        self.url, self.model_id, self.voice_id = url, model_id, voice_id
        self.extra_key = extra_key or {}

    def synth(self, text, out_path):
        r = requests.post(f"{self.url}/synth", json={"text": text, "out_path": out_path}, timeout=600)
        r.raise_for_status()
        j = r.json()
        return TTSResult(out_path, j["duration_s"], j["sample_rate"], self.model_id, self.voice_id)

    def cache_key(self):
        return {"model": self.model_id, "voice": self.voice_id, **self.extra_key}
```

**Fayda:** Model GPU par ek baar load hota hai aur saare beats us par chalte hain. Pipeline ka main env halka rehta hai.

👉 Agla: [12_TTS_Setup_Chatterbox_Voice_Cloning.md](12_TTS_Setup_Chatterbox_Voice_Cloning.md)
