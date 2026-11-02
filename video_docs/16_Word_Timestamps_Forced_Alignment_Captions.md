# 16 · Word Timestamps, Forced Alignment aur Captions

> **Is file mein:** Har word kis millisecond par bola gaya, ye kaise nikalein (forced alignment), kab zaroorat hai, Hinglish ki dikkatein, manim-voiceover ke bookmarks ke liye word boundaries ka format, aur SRT/VTT captions banana.

---

## 1. Seedhi baat

**Forced alignment** = "Mujhe pata hai kya bola gaya (script), batao har word kab bola gaya."

Ye **transcription (ASR) se aasaan aur zyada accurate** hai, kyunki words pehle se pata hain. Model ko sirf unki timing dhundhni hai.

### Kab chahiye?
| Use | Zaroori? |
|---|---|
| Beat-level sync | ❌ Nahi. Beat ki duration hi kaafi hai ([02](02_Sync_Ka_Science_Audio_First_Timeline.md)) |
| Bookmarks (beat ke andar specific word par animation) | ✅ Haan |
| Accurate subtitles (SRT) | ✅ Better (bina iske beat-level captions bhi chal jaate hain) |
| Karaoke-style word highlight | ✅ Haan |

**Strategy:** Pehle **beat-level** se kaam chalao. Alignment ko bookmarks + captions ke liye add karo.

---

## 2. Tools

| Tool | Kaise kaam karta hai | License | Notes |
|---|---|---|---|
| **stable-ts** | Whisper ke upar; `model.align(audio, text, language=...)` se known text align karta hai | MIT | manim-voiceover v0.4 transcription ke liye yahi use karta hai (`stable_whisper`) |
| **WhisperX** | Whisper transcription + **wav2vec2 forced alignment** | BSD-2-Clause | Hindi (`hi`) default align model: `theainerd/Wav2Vec2-large-xlsr-hindi` |
| **Montreal Forced Aligner (MFA)** | Classic HMM-based aligner | MIT | Bahut accurate (English); setup heavy |
| **TTS model ki khud ki timing** | Kuch TTS (jaise Azure) word boundaries khud dete hain | – | Hamare local models aam taur par nahi dete |
| **mlx-whisper** (Apple MLX) | Whisper on Apple Silicon; `word_timestamps=True` | MIT (ml-explore) | Mac par fast; transcription-based (known-text align nahi) |

### Recommendation
1. **stable-ts align (known text)** ✅ Primary (NVIDIA PC / koi bhi machine). manim-voiceover ke ecosystem mein already hai
2. **WhisperX** jab wav2vec2-level precision chahiye (English mein best)
3. 🍎 **Mac / budget mode:** **mlx-whisper** se word timestamps (chhote beats mein kaafi accurate), aur `to_word_boundaries()` (§6) script text se match kar deta hai. Code: [40](40_Mac_Apple_Silicon_Setup.md) §6

---

## 3. stable-ts se alignment

```bash
pip install -U stable-ts      # README: ffmpeg PATH mein hona chahiye; GPU ke liye PyTorch CUDA pehle install karo
```

```python
import stable_whisper

model = stable_whisper.load_model("medium")      # GPU par; "large-v3" zyada accurate

def align_words(wav_path: str, text: str, language: str = "en") -> list[dict]:
    result = model.align(wav_path, text, language=language)
    words = []
    for seg in result.segments:
        for w in seg.words:
            words.append({"word": w.word, "start": round(w.start, 3), "end": round(w.end, 3)})
    return words
```
Output (`words/b042.json`):
```json
[{"word":" Entropy","start":0.04,"end":0.58},
 {"word":" aati","start":0.58,"end":0.83},
 {"word":" hai","start":0.83,"end":1.01},
 {"word":" zero","start":1.12,"end":1.40}]
```

> `align()` ka exact signature aur options stable-ts version ke saath badal sakte hain. Install ke baad `help(model.align)` dekho.

---

## 4. WhisperX se alignment

```bash
pip install whisperx       # GPU ke liye CUDA toolkit 12.8 (README ke hisaab se); ffmpeg bhi chahiye
```

### Known text ke saath (transcription skip karke)
```python
import whisperx

device = "cuda"
audio = whisperx.load_audio("audio/b042.wav")
duration = len(audio) / 16000                    # whisperx audio 16 kHz par load karta hai

segments = [{"text": "Entropy aati hai zero point nine four zero.", "start": 0.0, "end": duration}]
model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
result = whisperx.align(segments, model_a, metadata, audio, device, return_char_alignments=False)
words = [{"word": w["word"], "start": w.get("start"), "end": w.get("end")}
         for seg in result["segments"] for w in seg["words"]]
```
> `whisperx.align()` segments ki list leta hai, isliye apna known text ek segment ke roop mein dena kaam karta hai. Ye documented "official recipe" nahi hai. Pehli baar chala kar output check karo.

### Known limitation
WhisperX README: jo words alignment model ki dictionary mein nahi hote (jaise numbers "2014", symbols "£13.60"), unhe timestamp nahi milta. Hamare paas narration already spoken form mein hai ("zero point nine four zero"), isliye ye problem kam aayegi.

---

## 5. ⚠️ Hinglish ki dikkat

**Problem:** Hindi wav2vec2 model (`theainerd/Wav2Vec2-large-xlsr-hindi`) ki vocabulary **Devanagari characters** ki hai. Roman Hinglish text ("aati hai") ke characters uski dictionary mein nahi hain, isliye alignment fail ya bekaar hoga. English model se align karoge to Hindi words ke liye acoustic model mismatch hoga.

### Solutions (best se simple tak)
| Option | Kaise | Trade-off |
|---|---|---|
| **A. Sub-beats** ✅ | Bookmarks ki jagah beat ko chhote beats mein todo ([02](02_Sync_Ka_Science_Audio_First_Timeline.md) Tareeka C) | Alignment ki zaroorat hi nahi; har sub-beat ki duration exact |
| **B. Whisper-based (stable-ts)** | Whisper multilingual hai; `language="hi"` ya `"en"` ke saath align try karo | Accuracy model aur text par depend; test karo |
| **C. Transliterate for alignment** | Text ko Devanagari mein convert karo ([14](14_Pronunciation_Text_Normalization.md)), Hindi wav2vec2 se align karo, phir words map back karo | Complex; English words ka issue phir bhi |
| **D. Proportional estimate** | Word timing = character position / total chars × duration | Rough (±200–400 ms), lekin chhote beats mein chal jaata hai |

> manim-voiceover khud bhi bina word boundaries ke **option D** jaisa fallback use karta hai: start aur end ke beech linear mapping (`_get_fallback_word_boundaries`). Chhote beats (3–6 s) mein ye aksar "good enough" hota hai.

**Recommendation for Hinglish:** A (sub-beats) primary. B ko captions ke liye try karo. Agar quality achhi nahi to D se captions banao (beat-level captions).

---

## 6. manim-voiceover ke liye `word_boundaries` format

Agar tum khud alignment karke manim-voiceover ko word boundaries dena chahte ho (taaki `wait_until_bookmark` precise ho), to v0.4.0 source ke hisaab se format ye hai:

```python
AUDIO_OFFSET_RESOLUTION = 10_000_000          # audio_offset units: 1e-7 second (100 ns)

word_boundaries = [
    {
        "audio_offset": int(start_sec * AUDIO_OFFSET_RESOLUTION),   # word kab shuru
        "text_offset": char_index_in_text_without_bookmarks,       # text mein kahan
        "word_length": len(word),
        "text": word,
        "boundary_type": "Word",
    },
    ...
]
```

**Bookmark timing kaise nikalti hai (source se):**
1. Narration text se bookmarks hata kar har bookmark ki **character position** note hoti hai
2. `text_offset → audio_offset` ka linear interpolation banta hai (`scipy.interpolate.interp1d`)
3. Bookmark position ko interpolate karke time milta hai

Isliye `text_offset` **bookmarks hatane ke baad wale text** mein character index hona chahiye. Agar tum `transcribed_text` field nahi dete, to library maanti hai ki tumhare offsets original text ke hain.

### Helper: alignment words → word_boundaries
```python
import re

BOOKMARK_RE = r"<bookmark\s*mark\s*=['\"]\w*['\"]\s*/>"

def to_word_boundaries(narration: str, aligned: list[dict]) -> list[dict]:
    clean = re.sub(BOOKMARK_RE, "", narration)
    out, cursor = [], 0
    for w in aligned:
        token = w["word"].strip()
        idx = clean.find(token, cursor)
        if idx == -1 or w.get("start") is None:
            continue                                  # match nahi hua; interpolation baaki ko cover karega
        out.append({"audio_offset": int(w["start"] * 10_000_000), "text_offset": idx,
                    "word_length": len(token), "text": token, "boundary_type": "Word"})
        cursor = idx + len(token)
    return out
```
Ye custom SpeechService ke return dict mein `"word_boundaries"` key ke roop mein jaata hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)).

---

## 7. Captions (SRT / VTT)

### Option 1: Manim ke subcaptions (automatic)
manim-voiceover `set_speech_service(..., create_subcaption=True)` (default) par har voiceover ka text **subcaption** ki tarah add karta hai. Lambe text ko `max_subcaption_len=70` characters ke chunks mein todta hai, aur chunks ka time characters ke proportion se baant'ta hai. Manim render ke saath video ke paas ek **`.srt`** file ban jaati hai.

- **Pro:** Zero extra kaam
- **Con:** Timing proportional hai (word-accurate nahi), aur scene-level files hain jinhe merge karna padega

### Option 2: Word timestamps se khud SRT banao (better)
```python
def fmt_srt(t: float) -> str:
    ms = int(round(t * 1000))                 # pehle total ms (warna 1.9996 s par ",1000" ban sakta hai)
    h, ms = divmod(ms, 3_600_000); m, ms = divmod(ms, 60_000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def words_to_srt(words, max_chars=42, max_dur=5.0, offset=0.0) -> str:
    """words: [{"word","start","end"}] (global timeline seconds)."""
    cues, cur = [], []
    for w in words:
        cur.append(w)
        text = "".join(x["word"] for x in cur).strip()
        if len(text) >= max_chars or cur[-1]["end"] - cur[0]["start"] >= max_dur \
                or w["word"].strip().endswith((".", "?", "!")):
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)
    lines = []
    for i, c in enumerate(cues, 1):
        start, end = c[0]["start"] + offset, c[-1]["end"] + offset
        lines += [str(i), f"{fmt_srt(start)} --> {fmt_srt(end)}",
                  "".join(x["word"] for x in c).strip(), ""]
    return "\n".join(lines)
```

### Caption style rules
| Rule | Value |
|---|---|
| Max characters per line | ~42 |
| Max lines | 2 |
| Min duration | ~1 s |
| Max duration | ~6 s |
| Line break | Sentence/phrase boundary par |
| Numbers in captions | **Digits** mein ("0.940"), spoken words mein nahi. Captions padhne ke liye hain, isliye yahan display form use karo |

> Captions ke liye `narration` ki jagah ek **`caption_text`** banao jisme numbers wapas digits mein hon ("zero point nine four zero" → "0.940"). Ye `verify` block ke `display` ↔ `spoken` mapping se automatically ho sakta hai.

### Global timeline
Har beat ke words relative (beat start = 0) hote hain. Final SRT ke liye har beat ka **global start time** add karo (`durations.json` + gaps se cumulative, [02](02_Sync_Ka_Science_Audio_First_Timeline.md)).

---

## 8. Checklist

- [ ] Beat-level sync pehle; alignment sirf bookmarks/captions ke liye
- [ ] Hinglish ke liye sub-beats prefer kiye
- [ ] Bookmarks ke `text_offset` bookmark-free text par based hain
- [ ] Captions mein numbers digits mein
- [ ] SRT global timeline par (offsets sahi)
- [ ] YouTube par SRT alag upload (soft subs)

👉 Agla: [17_Manim_Basics_Install_Concepts.md](17_Manim_Basics_Install_Concepts.md)
