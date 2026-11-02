# 12 · TTS Setup: Chatterbox + Voice Cloning

> **Is file mein:** Chatterbox (English + Multilingual V3 with Hindi) install aur code, apni awaaz clone karne ka poora process (recording se le kar consistency tak), aur ethics/consent.

---

## 1. Chatterbox family (Resemble AI, MIT license)

| Model | Size | Languages | Kab use karein |
|---|---|---|---|
| **Chatterbox Multilingual V3** | 500M | 23 languages incl. **Hindi (`hi`)** | Hinglish/Hindi + voice cloning ⭐ |
| Chatterbox (original) | 500M | English | English with `exaggeration`/`cfg_weight` control |
| Chatterbox-Turbo | 350M | English | Fast English; paralinguistic tags jaise `[laugh]` |
| Chatterbox-Nano | 110M | English | CPU/on-device |

**Supported languages (Multilingual):** ar, da, de, el, en, es, fi, fr, he, **hi**, it, ja, ko, ms, nl, no, pl, pt, ru, sv, sw, tr, zh

**Watermark:** Har generated audio mein Resemble ka **Perth** watermark hota hai (inaudible). Ye misuse rokne ke liye hai, aur hamare use par koi asar nahi padta.

---

## 2. Install

```bash
pip install chatterbox-tts
```
Alag venv recommended hai ([11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) section 0).

---

## 3. Code

### English (original)
```python
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

model = ChatterboxTTS.from_pretrained(device="cuda")     # "cpu" / "mps" bhi
text = "Information gain tells us which question to ask first."
wav = model.generate(text, audio_prompt_path="voice_refs/my_voice_ref.wav")
ta.save("cb_en.wav", wav, model.sr)
```

### Multilingual V3 (Hindi)
```python
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

mtl = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")
text = "अब हम entropy calculate करते हैं। Answer आता है zero point nine four zero."
wav = mtl.generate(text, language_id="hi",
                   audio_prompt_path="voice_refs/my_voice_ref.wav",
                   exaggeration=0.5, cfg_weight=0.5)
ta.save("cb_hi.wav", wav, mtl.sr)
```
> `t3_model` omit karo ya `"v2"` do to legacy V2 checkpoint load hota hai.

### 🍎 Mac (Apple Silicon)
Repo mein official **`example_for_mac.py`** hai. Pattern: `device = "mps"` (warna `cpu`), aur `torch.load` ko patch karo taaki weights `map_location=torch.device(device)` ke saath load hon:
```python
import torch
device = "mps" if torch.backends.mps.is_available() else "cpu"
_orig = torch.load
torch.load = lambda *a, **k: _orig(*a, **{**k, "map_location": k.get("map_location", torch.device(device))})
# phir: ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")
```
Official example English `ChatterboxTTS` ke liye hai. Multilingual class mein same patch kaam karna chahiye, pehli baar test karo. Full example: [40](40_Mac_Apple_Silicon_Setup.md) §5.

### Parameter tuning (official tips)
| Situation | Setting |
|---|---|
| Default (zyadatar cases) | `exaggeration=0.5`, `cfg_weight=0.5` |
| Reference speaker tez bolta hai | `cfg_weight ≈ 0.3` (pacing better) |
| Expressive/dramatic | `cfg_weight ≈ 0.3`, `exaggeration ≥ 0.7` |
| Reference clip ki language ≠ `language_id` | `cfg_weight = 0` (accent transfer kam) |
| Note | Zyada `exaggeration` speech ko tez kar deta hai; `cfg_weight` kam karke compensate karo |

**Teaching voice ke liye starting point:** `exaggeration=0.4–0.5`, `cfg_weight=0.4–0.5`. Calm, clear, thoda warm.

---

## 4. Apni awaaz clone karna: poora process

### Step 1: Consent aur purpose
- Apni awaaz → koi problem nahi
- Kisi aur ki awaaz (teacher, dost) → **written consent** lo, jisme likha ho ki kahan aur kis kaam mein use hogi
- IndicF5 ki terms bhi explicitly kehti hain: sirf permission wali awaaz clone karo
- Details: [38](38_Licenses_Legal_Ethics.md)

### Step 2: Recording setup
| Cheez | Recommendation |
|---|---|
| Room | Chhota kamra, parde/gadde/kapde (echo kam), AC/fan band |
| Mic | USB condenser ya achha lavalier; phone bhi chalega agar kamra shant ho |
| Distance | Mic se ~15–20 cm, side se (pop sounds kam) |
| Format | WAV, 44.1/48 kHz, 24-bit (baad mein resample) |
| Level | Peaks −12 se −6 dBFS ke beech (kabhi clip nahi) |
| Software | Audacity (free) |

### Step 3: Kya bolna hai
- **10–20 sec** ka ek clean clip (zyadatar zero-shot models ~10 s par best kaam karte hain)
- **Usi style mein bolo jo video mein chahiye:** teaching tone, Hinglish, normal pace
- Example reference script:
  > "Namaste dosto. Aaj hum machine learning ka ek bahut important concept samjhenge. Ise dhyan se dekhna, kyunki aage ke saare topics isi par based hain."
- 5–10 alag takes record karo, phir best wala choose karo

### Step 4: Clean up
```bash
# Silence trim (start/end) + mono + 24 kHz + loudness normalize
ffmpeg -i raw_take.wav -af "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,loudnorm=I=-20:TP=-2" -ac 1 -ar 24000 my_voice_ref.wav
```
- Noise reduction **halka** rakho (zyada processing se artifacts aate hain, jo model copy kar leta hai)
- Breath sounds ok hain, clicks/pops hatao

### Step 5: Transcript (IndicF5 ke liye zaroori)
Reference ka **exact** transcript likho, jo bola hai wahi ("umm" bhi agar bola hai).

### Step 6: Test
- 10 test sentences generate karo (technical + casual + numbers)
- Original recording se compare karo: kya awaaz pehchani ja rahi hai? accent sahi hai?
- Agar output mein noise/echo aa raha hai to reference clip mein bhi hoga, wahi fix karo

### Step 7: Lock karo
- Final reference clip `video/assets/voice_refs/` mein, aur uska hash `manifest.json` mein
- Poore project mein **same clip, same params, same model version**

---

## 5. Pipeline backend

```python
# envs/tts-chatterbox/server.py (pattern [11] section 5 jaisa)
import torch, torchaudio as ta
from fastapi import FastAPI
from pydantic import BaseModel
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

app = FastAPI()
mtl = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")
REF = "voice_refs/my_voice_ref.wav"
PARAMS = dict(exaggeration=0.45, cfg_weight=0.45)

class Req(BaseModel):
    text: str
    out_path: str
    language_id: str = "hi"
    seed: int = 1234

@app.post("/synth")
def synth(r: Req):
    torch.manual_seed(r.seed)                  # reproducibility
    wav = mtl.generate(r.text, language_id=r.language_id, audio_prompt_path=REF, **PARAMS)
    ta.save(r.out_path, wav, mtl.sr)
    return {"duration_s": wav.shape[-1] / mtl.sr, "sample_rate": mtl.sr}
```

`cache_key` mein `ref clip hash + PARAMS + model version + seed` sab daalo ([05](05_Architecture_Pipeline_Folder_Structure.md)).

---

## 6. Consistency problems aur fixes

| Problem | Fix |
|---|---|
| Har beat mein awaaz thodi alag | Same seed; `exaggeration` kam; reference clip lamba aur stable rakho |
| Kuch beats mein accent English-jaisa | `cfg_weight` kam karo; reference Hinglish mein ho |
| Beat ka end kat gaya | Text ke end mein punctuation; ASR check |
| Random breath/noise | Reference clean karo |
| Speed inconsistent | `cfg_weight` adjust; script mein beat lengths similar rakho |

👉 Agla: [13_TTS_BakeOff_Kaise_Kare.md](13_TTS_BakeOff_Kaise_Kare.md)
