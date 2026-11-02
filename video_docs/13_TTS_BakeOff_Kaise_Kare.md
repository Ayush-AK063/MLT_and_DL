# 13 · TTS Bake-off: Models Ko Apne Sentences Par Test Karna

> **Is file mein:** 3–5 TTS models ko fairly compare karne ka step-by-step process: test set, automatic intelligibility score (ASR back-transcription), blind listening (MOS), scoring sheet, aur final decision.

---

## 1. Kyun bake-off?

- Online benchmarks generic hote hain, aur Hinglish ML-teaching jaisa content unme nahi hota
- Har model alag text par alag behave karta hai (Roman vs Devanagari, numbers, technical terms)
- **2–3 ghante ka test poore project (100+ ghante audio) ki quality decide karta hai**

---

## 2. Test set (30 sentences, 6 categories)

Har category mein 5 sentences. Ye actual lecture content se lo:

### A. Pure Roman Hinglish (casual explanation)
1. "Chalo ab dekhte hain ki ye tree kaise banta hai."
2. "Socho tumhare paas ek dabba hai jisme laal aur neeli balls mixed hain."
3. "Bahut log yahan confuse hote hain, aur wo bilkul theek hai."
4. "Is sawaal ka jawab dhundhne ke liye hume thoda calculation karna padega."
5. "Video ko yahan pause karo aur khud try karo."

### B. Technical terms in Hinglish
6. "Information gain batata hai ki kaunsa attribute entropy ko sabse zyada kam karta hai."
7. "Random forest mein bahut saare decision trees milke vote karte hain."
8. "K nearest neighbours algorithm mein hum naye point ke sabse paas wale padosi dekhte hain."
9. "Precision aur recall ke beech hamesha ek trade-off hota hai."
10. "Scikit learn library mein ye sirf do lines ka code hai."

### C. Numbers aur formulas (spoken form)
11. "Entropy aati hai zero point nine four zero."
12. "Gain of S comma Outlook barabar zero point two four six seven."
13. "Nine by fourteen times log base two of nine by fourteen."
14. "Accuracy eighty two percent se badh kar ninety seven point eight percent ho gayi."
15. "A U C ki value zero point seven six hai."

### D. Abbreviations / names
16. "I D three algorithm Ross Quinlan ne banaya tha."
17. "R O C curve threshold ke saath banti hai."
18. "P C A dimensionality reduction ka technique hai."
19. "Claude Shannon ne information theory di."
20. "Iris dataset mein teen classes hain: setosa, versicolor aur virginica."

### E. Devanagari + English (agar model ko chahiye)
21. "अब हम entropy calculate करते हैं।"
22. "Random forest में बहुत सारे trees vote करते हैं।"
23. "Answer आता है zero point nine four zero।"
24. "ये classification problem है, regression नहीं।"
25. "Overfitting का मतलब है ratta मारना।"

### F. Long sentence + emotion
26. "Ab tak humne entropy dekhi, information gain dekha, aur ab hum ready hain poora tree banane ke liye, step by step."
27. "Dekho kitna interesting hai! Sirf ek sawaal se aadha confusion khatam ho gaya."
28. "Ye galti mat karna, warna poora answer galat ho jayega."
29. "Ek akela tree eighty two percent sahi tha, lekin sau trees milke ninety seven point eight percent!"
30. "Aaj humne teen cheezein seekhi. Ek: entropy. Do: information gain. Teen: best attribute kaise chunein."

> Agar final script Roman mein hai to category E sirf un models ke liye hai jo Devanagari maangte hain (transliteration pipeline ke saath).

---

> 🍎 **Mac / budget mode shortlist:** Kokoro (`hf_alpha`, `hm_omega`), Chatterbox Multilingual V3 + apni awaaz, IndicF5 (patched; agar MPS/CPU par chale), Indic Parler (optional). Veena ko Mac par skip karo (4-bit NVIDIA-only). ASR check ke liye section 3 mein `whisper` ki jagah **mlx-whisper** use karo ([40](40_Mac_Apple_Silicon_Setup.md) §6). Baaki process same hai.

## 3. Automatic score: ASR back-transcription (intelligibility)

**Idea:** TTS ka audio ek strong ASR (Whisper) ko do. Agar ASR wahi text wapas likh de to model ne words saaf bole hain.

```python
# bakeoff/asr_check.py
import whisper                      # pip install openai-whisper  (ya faster-whisper)
from jiwer import cer               # pip install jiwer
import re, unicodedata

asr = whisper.load_model("large-v3")    # GPU par; chhota GPU ho to "medium"

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s.lower())
    s = re.sub(r"[^\w\s]", " ", s)
    return " ".join(s.split())

def intelligibility(wav_path: str, ref_text: str, lang: str = "hi") -> float:
    hyp = asr.transcribe(wav_path, language=lang)["text"]
    return cer(norm(ref_text), norm(hyp))     # character error rate: 0 = perfect
```

### Hinglish ka twist
Whisper Hindi audio ka transcript **Devanagari** mein de sakta hai, jabki tumhara reference Roman mein hai. Direct CER compare karoge to galat (bahut high) aayega. Options:
1. **Transliteration normalize:** Dono ko ek script mein convert karo (jaise Devanagari → Roman via `indic-transliteration` library), phir CER
2. **Multiple ASR consensus:** harrrshall ke eval ne 3 ASR (AssemblyAI, Deepgram, Groq Whisper) ka consensus aur Devanagari normalization use kiya tha
3. **Simple practical:** Whisper ko `language="en"` aur `language="hi"` dono se chalao, jo kam CER de wo lo (rough heuristic)

> CER perfect metric nahi hai: insaan ko samajh aane wala audio bhi spelling differences ki wajah se CER badha sakta hai. Isliye isse **red flags** pakdo (words skip/garbled), fine ranking ke liye listening test karo.

### Red flags (automatic)
| Check | Threshold | Matlab |
|---|---|---|
| Duration < 0.3 s | – | Silent/failed |
| Duration / words << expected (~0.3 s/word se kam) | – | Truncation (IndicF5 Roman bug ka symptom) |
| CER > 0.35 | tune karo | Words garbled/skipped |
| Duration >> expected | – | Repetition/looping (autoregressive models) |

---

## 4. Human score: blind listening (MOS)

**MOS = Mean Opinion Score (1–5).**

### Setup
1. Har model ke 30 outputs ko random naam do (`a7f3.wav`, ...) taaki pata na chale kaunsa model hai
2. Ek simple HTML/Python player banao jo random order mein play kare
3. 2–3 log suno (tum + 1–2 students ideal hain, kyunki asli audience wahi hain)

### Rating scale
| Score | Naturalness | Pronunciation |
|---|---|---|
| 5 | Insaan jaisa, ekdam natural | Har word sahi |
| 4 | Thoda synthetic, lekin pleasant | 1 chhoti galti |
| 3 | Clearly AI, lekin theek hai | 2–3 galtiyan |
| 2 | Robotic, distracting | Kai galtiyan |
| 1 | Unusable | Samajh nahi aata |

Plus ek binary sawaal: **"Kya tum 1 ghanta ye awaaz sun sakte ho?"** (Haan/Na). Ye sabse important sawaal hai.

---

## 5. Consistency test

Ek model ke saath **10 consecutive beats** generate karo (ek real scene ka script) aur unhe 0.25 s gaps ke saath jod kar suno:
- Awaaz har beat mein same lagti hai?
- Volume/pitch jumps?
- Lagta hai ek insaan lagaatar bol raha hai, ya 10 alag recordings?

---

## 6. Scoring sheet

| Model / Voice | Intelligibility (CER-based, 1–5) | Naturalness MOS | Tech terms (cat. B+D, 1–5) | Numbers (cat. C, 1–5) | Consistency (1–5) | 1-ghanta test | Speed (RTF) | License OK | **Weighted** |
|---|---|---|---|---|---|---|---|---|---|
| Kokoro hf_alpha | | | | | | | | ✅ | |
| Kokoro hm_omega | | | | | | | | ✅ | |
| IndicF5 (patched) + my voice | | | | | | | | ⚠️ | |
| IndicF5 (patched) + dataset ref | | | | | | | | ⚠️ | |
| Indic Parler (Rohit) | | | | | | | | ✅ | |
| Veena (agastya) | | | | | | | | ⚠️ | |
| Chatterbox ML + my voice | | | | | | | | ✅ | |

**Weights:** Intelligibility 30%, Naturalness 30%, Tech terms 15%, Consistency 15%, Speed 5%, License 5% ([09](09_TTS_Model_Selection_Guide.md)).

**RTF (Real-Time Factor)** = generation time / audio duration. RTF 0.1 ka matlab 10 s audio 1 s mein ban gaya.

---

## 7. Decision rules

1. Jis model ka "1-ghanta test" **No** hai, wo bahar (score kitna bhi ho)
2. License ⚠️ wale models tabhi chuno jab terms clarify ho jayein (ya non-commercial use hi hai)
3. Top-2 ke beech close fight ho to: **consistency** ko tie-breaker banao
4. Final model + voice + params ko lock karo aur `config.yaml` + `manifest.json` mein likho

---

## 8. Bake-off run karne ka script (outline)

```python
# bakeoff/run.py
import json, time, pathlib
from video.lib.tts.http_backend import HTTPBackend

MODELS = {
    "kokoro_hf_alpha":  HTTPBackend("http://localhost:8105", "kokoro", "hf_alpha"),
    "indicf5_myvoice":  HTTPBackend("http://localhost:8101", "indicf5", "myvoice"),
    "parler_rohit":     HTTPBackend("http://localhost:8102", "indic-parler", "rohit"),
    "veena_agastya":    HTTPBackend("http://localhost:8103", "veena", "agastya"),
    "chatterbox_myvoice": HTTPBackend("http://localhost:8104", "chatterbox-mtl-v3", "myvoice"),
}
sentences = json.load(open("bakeoff/test_set.json"))     # [{"id":1,"cat":"A","text":"..."}]
out = pathlib.Path("bakeoff/out"); out.mkdir(parents=True, exist_ok=True)

results = []
for name, be in MODELS.items():
    for s in sentences:
        p = out / f"{name}_{s['id']:02d}.wav"
        t0 = time.time()
        r = be.synth(s["text"], str(p))
        results.append({"model": name, "id": s["id"], "cat": s["cat"],
                        "dur": r.duration_s, "rtf": (time.time() - t0) / max(r.duration_s, 1e-6)})
json.dump(results, open("bakeoff/results.json", "w"), indent=1)
```
Phir `asr_check.py` se CER, aur blind player se MOS.

---

## 9. Result ko yahan record karo

> ✏️ **Bake-off result (fill after running):**
> - Date:
> - Winner (Hinglish):
> - Winner (English):
> - Params:
> - Notes:

👉 Agla: [14_Pronunciation_Text_Normalization.md](14_Pronunciation_Text_Normalization.md)
