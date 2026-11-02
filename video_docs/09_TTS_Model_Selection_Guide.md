# 09 · TTS Model Selection Guide

> **Is file mein:** Kaun sa Text-to-Speech model kyun: har candidate ki strengths/weaknesses, license, hardware, Hinglish support, aur final decision kaise lein.

---

## 1. Seedhi baat

Mayer ka **Voice principle** kehta hai: log friendly human voice se zyada seekhte hain, machine voice se kam. Isliye **TTS quality poore project ka sabse bada quality lever hai.** Animation kitna bhi achha ho, robotic awaaz video ko sasta bana degi.

Problem ye hai ki **Hinglish (code-mixed) TTS abhi bhi mushkil hai.** Koi ek model har jagah best nahi hai. Isliye hum 3–5 models ko apne actual sentences par test karenge ([13](13_TTS_BakeOff_Kaise_Kare.md)).

---

## 2. Candidates ek nazar mein

| Model | Size | Hindi / Hinglish | Voice cloning | License (model card) | Output | Notes |
|---|---|---|---|---|---|---|
| **Kokoro-82M** | 82M | Hindi voices (`hf_alpha`, `hf_beta`, `hm_omega`, `hm_psi`, sab grade C); English excellent (`af_heart` grade A) | ❌ | Apache-2.0 | 24 kHz | Bahut fast, CPU par bhi chalta hai. English ke liye top pick |
| **IndicF5** (AI4Bharat) | ~0.4B | 11 Indian languages incl. Hindi; Roman Hinglish par **patch ke baad** strong | ✅ (reference audio + transcript se) | Card par MIT; gated (terms accept karni padti hain). ⚠️ Ek source commercial restriction batata hai, verify karo | 24 kHz | Roman-script bug hai; harrrshall/hinglish-tts ka patch fix karta hai |
| **Indic Parler-TTS** (AI4Bharat) | ~0.9B | 21 languages incl. Hindi + English; named speakers (Hindi: Rohit, Divya recommended) | ❌ (text description se voice control) | Apache-2.0; gated | `model.config.sampling_rate` | Voice ko text se describe karte ho ("very clear audio"). Roman colloquial Hinglish par kamzor reported |
| **Veena** (Maya Research) | 3B (Llama-based) | Hindi + English + **code-mixed** | ❌ (4 fixed speakers: kavya, agastya, maitri, vinaya) | Apache-2.0 (⚠️ page header "proprietary" bhi dikhata hai) | 24 kHz (SNAC) | GPU chahiye; 4-bit quantization support; RTX 4090 par ~200 ms latency (card ke hisaab se) |
| **Chatterbox Multilingual V3** (Resemble AI) | 500M | 23 languages incl. Hindi (`hi`) | ✅ (~10 s reference clip) | MIT | `model.sr` | Har output mein Perth watermark (inaudible). Emotion control (`exaggeration`) |
| **Chatterbox-Turbo** | 350M | English only | ✅ | MIT | | English ke liye fast; `[laugh]` jaise tags |
| **Gemini TTS** (cloud) | – | Multilingual | ❌ (prebuilt voices) | Paid API | 24 kHz | manim-voiceover v0.4 ka default "recommended" service (`gemini-3.1-flash-tts-preview`, voice "Kore"). Local nahi hai, backup option |
| **XTTS-v2** (Coqui) | – | Hindi included (17 languages) | ✅ | CPML (non-commercial) | | Coqui company band ho chuki hai; license restrictive. ❌ Avoid |
| **VibeVoice** (Microsoft) | 1.5B/7B | – | – | Microsoft ne Sept 2025 mein long-form TTS code repo se hata diya (misuse ki wajah se) | | ❌ Avoid (unofficial forks risky) |
| **Higgs Audio (newer versions)** | – | – | ✅ | Newer versions non-commercial | | ❌ Agar commercial use plan hai |

> Sab license details 2026-10-18 ko model cards/sources se check kiye. Licenses badalte rehte hain, final use se pehle model card dobara dekho ([38](38_Licenses_Legal_Ethics.md)).

---

## 3. Har candidate detail mein

### 3.1 Kokoro-82M ⭐ (English ke liye default)
- **Strengths:** Chhota (82M), bahut fast, Apache-2.0 (kahin bhi deploy kar sakte ho), English voices ki quality bahut achhi
- **Weaknesses:** Hindi voices ki training kam hai (grade C); voice cloning nahi; code-mixed text par G2P (spelling → pronunciation) issues
- **Data point:** harrrshall ke Hinglish eval mein Kokoro (Hindi) ka overall intelligibility 3.90/5 tha, aur "English with Indian named entities" category mein sabse best (4.83)
- **Use:** English version ke videos, aur Hinglish ke liye baseline
- Setup: [10_TTS_Setup_Kokoro.md](10_TTS_Setup_Kokoro.md)

### 3.2 IndicF5 ⭐ (Hinglish ke liye strong candidate)
- **Kaise kaam karta hai:** F5-TTS architecture (flow matching). Tum ek **reference audio clip + uska transcript** dete ho, aur model usi awaaz/style mein naya text bolta hai
- **Strengths:** Natural Indian accent; voice cloning built-in (apni awaaz ka 5–10 s clip do)
- **Known bug:** Model synthesis duration ko text ke **UTF-8 bytes** se estimate karta hai. Devanagari char ~3 bytes ka hai aur ASCII 1 byte ka, isliye Roman text ko ~3× kam time milta hai aur audio truncate ho jaata hai. harrrshall/hinglish-tts patch byte count ko non-whitespace character count se replace karta hai
- **Eval (harrrshall, 30 sentences, 3-ASR consensus):** patched 4.70/5 overall; unpatched 2.13
- **Caveat:** Ye eval chhota hai aur self-run hai. Naturalness sirf ek native speaker ne suna tha
- Setup: [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md)

### 3.3 Indic Parler-TTS
- **Kaise:** Do inputs: (1) bolne wala text, (2) awaaz ka description ("Divya's voice is monotone yet slightly fast..., very clear audio")
- **Strengths:** Apache-2.0; bahut saari Indian languages; voice ko text se control kar sakte ho
- **Weaknesses:** Reported evals mein Roman colloquial Hinglish par kamzor; har generation mein thodi variation (consistency ke liye same description + seed fix karo)
- Setup: [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md)

### 3.4 Veena
- **Kaise:** Llama-style autoregressive model jo SNAC audio tokens generate karta hai. Prompt format: `<spk_kavya> {text}`
- **Strengths:** Hindi + English code-mixed ke liye specifically bana; 4 speakers
- **Weaknesses:** 3B params, isliye GPU chahiye; independent benchmarks kam mile; autoregressive models kabhi-kabhi words repeat/skip kar sakte hain (ASR check zaroori)
- Setup: [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md)

### 3.5 Chatterbox Multilingual V3
- **Strengths:** MIT; Hindi support; zero-shot voice cloning (~10 s clip); `exaggeration` se expressiveness control
- **Weaknesses:** Hindi par independent Hinglish eval nahi mila; watermark hamesha lagta hai (inaudible, problem nahi, bas pata hona chahiye)
- **Tip (official README):** Agar reference clip ki language aur `language_id` alag hain to `cfg_weight=0` karo, accent transfer kam hota hai
- Setup: [12](12_TTS_Setup_Chatterbox_Voice_Cloning.md)

---

## 4. Decision framework

```
                        ┌─ English video? ──────────► Kokoro (af_heart)  [backup: Chatterbox-Turbo]
                        │
Script language ────────┤
                        │                      ┌─ Apni awaaz chahiye? ─► IndicF5 (patched) ya Chatterbox-ML (bake-off)
                        └─ Hinglish video? ────┤
                                               └─ Ready-made voice?  ─► Veena / IndicF5 (dataset ref) / Indic Parler / Kokoro-hi (bake-off)
```

### Scoring criteria (bake-off mein)
| Criterion | Weight | Kaise naapein |
|---|---|---|
| Intelligibility (sahi words bole?) | 30% | ASR back-transcription CER ([13](13_TTS_BakeOff_Kaise_Kare.md)) |
| Naturalness (insaan jaisa?) | 30% | Blind listening, 1–5 MOS |
| Technical terms (entropy, AUC, sklearn) | 15% | Specific test sentences |
| Consistency (har beat mein same awaaz?) | 15% | 10 beats lagaatar suno |
| Speed (generation time) | 5% | Real-time factor |
| License | 5% | Commercial OK? |

---

## 5. Practical recommendations

1. **Pehle bake-off, phir commit.** 2–3 ghante ka bake-off poore project ke 100+ ghante ke audio ki quality decide karta hai.
2. **Ek video mein ek hi model + ek hi voice.** Beech mein model badalne se awaaz badal jaati hai.
3. **Voice cloning ke liye apni awaaz best hai.** Tumhari (ya tumhare teacher ki, **written consent ke saath**) 10–30 s ki clean recording. Students ko familiar awaaz achhi lagti hai.
4. **Reference clip quality = output quality.** Shant kamra, achha mic, no echo, 24 kHz+, natural pace.
5. **Har model version pin karo** (`manifest.json`), kyunki model update se awaaz badal sakti hai.
6. **Fallback rakho:** Agar local Hinglish quality kam padi to cloud (Gemini TTS / ElevenLabs) ek option hai, cost aur privacy trade-off ke saath.

---

## 5a. 🍎 Mac (Apple Silicon) par kaun sa chalega

| Model | Mac par | Note |
|---|---|---|
| Kokoro | ✅ | `PYTORCH_ENABLE_MPS_FALLBACK=1` (official README) ya mlx-audio |
| Chatterbox ML (Hindi + clone) | ✅ | Official `example_for_mac.py` pattern (`device="mps"` + `torch.load` map_location patch) |
| IndicF5 | ⚠️ Test karo | Upstream F5-TTS MPS auto-detect karta hai; IndicF5 ka pinned version alag ho sakta hai |
| Indic Parler | ⚠️ Test karo | Apple Silicon par bfloat16 ke liye naya PyTorch (Parler README) |
| Veena | ⚠️ / ❌ | Official 4-bit `bitsandbytes` NVIDIA-only; 64 GB Mac par full-precision try kar sakte ho |
| mlx-audio models (Kokoro, Qwen3-TTS, Voxtral TTS, ...) | ✅ | MLX native (MIT library) |

**Budget mode bake-off shortlist (Mac):** Kokoro (`hf_alpha`/`hm_omega`), Chatterbox ML + apni awaaz, IndicF5 (patched, agar MPS par chal jaye). Setup: [40](40_Mac_Apple_Silicon_Setup.md) §5.

---

## 6. Hardware estimate

| Model | Approx VRAM | CPU possible? |
|---|---|---|
| Kokoro-82M | Bahut kam (CPU par bhi theek) | ✅ |
| IndicF5 (0.4B) | Modest (consumer GPU theek) | Slow |
| Indic Parler (0.9B) | Modest | Slow |
| Chatterbox ML (500M) | Modest | Slow (`cpu`/`mps` supported) |
| Veena (3B) | 4-bit mein consumer GPU (RTX 4090 tested per card) | ❌ practically |

> ⚠️ Exact VRAM numbers official cards par nahi diye hain. Apne GPU par `nvidia-smi` se naapo aur yahan update karo.

👉 Setup files: [10 Kokoro](10_TTS_Setup_Kokoro.md) · [11 Indic models](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) · [12 Chatterbox](12_TTS_Setup_Chatterbox_Voice_Cloning.md) · [13 Bake-off](13_TTS_BakeOff_Kaise_Kare.md)
