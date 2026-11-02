# 18 · manim-voiceover: Sync + Custom Local TTS Service

> **Is file mein:** manim-voiceover v0.4.0 kaise kaam karta hai (source code padh kar), local TTS ke liye custom `SpeechService` kaise likhein, "pre-baked audio" pattern (render ke waqt GPU model load na ho), bookmarks, aur script.json se scene banane ka pattern.

---

## 1. Facts (v0.4.0, PyPI: 14 June 2026)

| Cheez | Value |
|---|---|
| Install | `pip install manim-voiceover` (extras: `all, azure, elevenlabs, gemini, gtts, openai, pyttsx3, recorder, transcribe, translate`) |
| Python | ≥ 3.11 |
| License | MIT |
| Status | "3 - Alpha" (API badal sakta hai, isliye version pin karo) |
| Built-in services | Gemini (README mein "recommended"), Azure, gTTS, pyttsx3, OpenAI, ElevenLabs, Recorder (apni awaaz mic se) |
| Removed | `CoquiService` (0.3.x mein tha, 0.4.0 mein nahi) |
| Transcription (bookmarks ke liye) | `transcribe` extra → `stable-ts` (`stable_whisper`) + `openai-whisper` |
| Audio duration | `mutagen` se; **sirf `.wav` aur `.mp3`** (baaki extensions ko MP3 maan leta hai) |
| Speed change | `global_speed` param SoX binary use karta hai |

---

## 2. Andar se kaise kaam karta hai

```python
with self.voiceover(text="Entropy aati hai zero point nine four zero.") as tracker:
    self.play(Write(eq), run_time=tracker.duration)
```

Source code (v0.4.0) ka flow:
1. `voiceover()` → `_add_voiceover_text(text)`
2. `speech_service._wrap_generate_from_text(text)`:
   - Text ke newlines/extra spaces hata kar single-space karta hai
   - Tumhara `generate_from_text()` call hota hai, jo ek **dict** return karta hai
   - Agar dict mein `word_boundaries` nahi hain **aur** `transcription_model` set hai → Whisper (stable-ts) se audio transcribe karke word boundaries banata hai
   - `audio_callback()` hook (post-processing ke liye override kar sakte ho)
   - `global_speed != 1` → SoX se tempo change
   - Entry `cache.json` mein append hoti hai
3. `VoiceoverTracker` banta hai: `tracker.duration` = audio length; `start_t` = current scene time
4. `self.add_sound(audio_path)` → audio scene timeline mein current time par lagta hai
5. Subcaption add hota hai (agar `create_subcaption=True`)
6. Tumhare animations chalte hain
7. `with` block khatam → `wait_for_voiceover()`: audio ka baaki time `wait` ho jaata hai

### Tracker API
| Method/attr | Kya |
|---|---|
| `tracker.duration` | Audio length (sec) |
| `tracker.get_remaining_duration(buff=0)` | Abhi kitna audio baaki hai |
| `tracker.time_until_bookmark(mark, buff=0, limit=None)` | Bookmark tak kitna time |
| `self.wait_until_bookmark(mark)` | Bookmark tak wait |
| `self.wait_for_voiceover()` | Audio khatam hone tak wait |
| `self.safe_wait(d)` | Wait, lekin 1 frame se chhota ho to skip |

---

## 3. `generate_from_text()` ka return format

Built-in services (gTTS, pyttsx3) ke source se pattern:

```python
json_dict = {
    "input_text": text,            # original text (bookmarks ke saath)
    "input_data": input_data,      # cache key: dict jo output ko uniquely identify kare
    "original_audio": audio_path,  # file NAME, cache_dir ke RELATIVE (absolute path nahi)
    # optional:
    "word_boundaries": [...],      # agar tumhare paas word timing hai (doc 16 section 6)
}
```

### ⚠️ v0.4.0 strict validation
v0.4.0 har return dict ko ek **pydantic model (`strict=True`)** se validate karta hai (`services/cache.py`):
- `input_data` ek dict hona chahiye jisme **`input_text: str` required** hai (`service: str` optional, extra keys allowed)
- `word_boundaries` ke fields strict types mein: `audio_offset: int`, `text_offset: int`, `word_length: int`, `text: str`, `boundary_type: str`. Float diya to validation fail hoga
- Galat format par error aata hai: `ValueError: Invalid voiceover cache entry` (andar `ValidationError ... VoiceoverCacheEntryModel`)

(Ye humne actual render test mein pakda: `input_data` mein `input_text` na hone par scene crash hua.)

### Cache kaise kaam karta hai
- `get_cached_result(input_data, cache_dir)` → `cache.json` mein same `input_data` wali entry mili to wahi return
- Isliye **`input_data` mein woh sab daalo jo audio ko affect karta hai**: text, model, voice, speed, seed, reference clip hash
- `get_audio_basename(input_data)` → `"<text-slug>-<sha256[:8]>"`, jo filename ke liye useful hai

---

## 4. Custom service: local TTS (HTTP server ke through)

```python
# video/lib/voiceover_service.py
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import requests
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import SpeechService


class LocalTTSService(SpeechService):
    """manim-voiceover service jo hamare local TTS server (doc 11 section 5) ko call karta hai."""

    def __init__(self, server_url: str, model_id: str, voice_id: str,
                 extra_key: dict | None = None, **kwargs):
        self.server_url = server_url
        self.model_id = model_id
        self.voice_id = voice_id
        self.extra_key = extra_key or {}
        super().__init__(**kwargs)          # global_speed, cache_dir, transcription_model ...

    def generate_from_text(self, text, cache_dir=None, path=None, **kwargs):
        if cache_dir is None:
            cache_dir = self.cache_dir
        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "local_tts",
                      "model": self.model_id, "voice": self.voice_id, **self.extra_key}

        cached = self.get_cached_result(input_data, cache_dir)
        if cached is not None:
            return cached

        audio_path = path or (self.get_audio_basename(input_data) + ".wav")
        out_abs = str(Path(cache_dir) / audio_path)
        r = requests.post(f"{self.server_url}/synth",
                          json={"text": input_text, "out_path": out_abs}, timeout=600)
        r.raise_for_status()

        return {"input_text": text, "input_data": input_data, "original_audio": audio_path}
```

Scene mein:
```python
from manim import *
from manim_voiceover import VoiceoverScene
from video.lib.voiceover_service import LocalTTSService

class S05WorkedExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(LocalTTSService(
            server_url="http://localhost:8101", model_id="indicf5-patched", voice_id="myvoice",
            extra_key={"ref_sha": "a1b2c3d4", "seed": 1234}))
        with self.voiceover(text="Chalo ab Outlook attribute ka gain nikalte hain.") as t:
            self.play(Write(Text("Gain(S, Outlook) = ?")), run_time=t.duration)
```

> ⚠️ `super().__init__(**kwargs)` zaroor call karo. Base class `cache_dir` banata hai (default: `media/voiceovers/`) aur transcription set karta hai.

---

## 5. ⭐ Pre-baked audio pattern (recommended)

**Problem:** Upar wale pattern mein render ke time TTS server chalna chahiye, aur 6 parallel renders ek hi GPU server ko hit karenge. Render aur TTS ka coupling debugging ko mushkil banata hai.

**Solution:** TTS stage mein saari audio **pehle** bana lo (`out/L20/T07/audio/b042.wav` + `durations.json`). Render ke waqt service sirf **file uthata hai**, koi model nahi chalata.

```python
# video/lib/voiceover_service.py
import shutil
from pathlib import Path
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import SpeechService


class PrebakedService(SpeechService):
    """Audio pehle se bana hai; beat id se file uthao. Render ke time koi TTS nahi."""

    def __init__(self, audio_dir: str, beats: dict[str, dict], **kwargs):
        # beats: {"b042": {"narration": "...", "audio": "b042.wav", "words": [...optional...]}}
        self.audio_dir = Path(audio_dir)
        self.beats = beats
        self._by_text = {" ".join(b["narration"].split()): bid for bid, b in beats.items()}
        super().__init__(**kwargs)

    def generate_from_text(self, text, cache_dir=None, path=None, **kwargs):
        if cache_dir is None:
            cache_dir = self.cache_dir
        beat_id = kwargs.get("beat_id") or self._by_text.get(" ".join(text.split()))
        if beat_id is None:
            raise KeyError(f"Pre-baked audio nahi mila is text ke liye: {text[:60]!r}")
        beat = self.beats[beat_id]
        src = self.audio_dir / beat["audio"]
        dst_name = f"{beat_id}_{src.stat().st_size}.wav"   # size suffix: audio badla to naya naam
        dst = Path(cache_dir) / dst_name
        if not dst.exists():
            shutil.copy(src, dst)                           # cache_dir ke andar hona chahiye (relative path)
        data = {"input_text": text,
                # v0.4.0 cache validation (pydantic, strict): input_data mein "input_text" (str) REQUIRED hai
                "input_data": {"input_text": remove_bookmarks(text), "service": "prebaked",
                               "beat": beat_id, "file": dst_name},
                "original_audio": dst_name}
        if "word_boundaries" in beat:          # empty list bhi pass karo: tracker tab linear fallback use karta hai
            data["word_boundaries"] = beat["word_boundaries"]   # doc 16 section 6 format
        return data
```

> `_wrap_generate_from_text()` text ko pehle single-space karta hai, isliye lookup bhi `" ".join(text.split())` se karte hain. Bookmarks text ka hissa rehte hain; narration (bookmarks ke saath) aur script ka text exactly same hona chahiye.

### `beat_id` pass karna
`voiceover(**kwargs)` ke extra kwargs service tak jaate hain (`subcaption`, `max_subcaption_len`, `subcaption_buff` ko chhod kar). Isliye:
```python
with self.voiceover(text=B["b042"]["narration"], beat_id="b042") as t:
    ...
```
Ye text-matching se zyada robust hai (same text do beats mein ho to bhi sahi file milegi).

---

## 6. script.json se scene: helper pattern

Coder (Claude) ko har baar boilerplate na likhna pade, isliye ek base class:

```python
# video/lib/scene_base.py
import json
from pathlib import Path
from manim import *
from manim_voiceover import VoiceoverScene
from .voiceover_service import PrebakedService
from .align import to_word_boundaries          # doc 16 section 6 ka helper
from .components.theme import apply_theme


class LessonScene(VoiceoverScene):
    TOPIC_DIR: str = ""        # subclass set kare, e.g. "video/out/L20/T07_information_gain"
    SCENE_ID: str = ""         # e.g. "s05_worked_example"

    def setup(self):
        super().setup()
        apply_theme(self)                                  # background, default fonts (doc 20)
        root = Path(self.TOPIC_DIR)
        self.script = json.loads((root / "script.json").read_text(encoding="utf-8"))
        durations = json.loads((root / "audio" / "durations.json").read_text())
        self.scene_spec = next(s for s in self.script["scenes"] if s["id"] == self.SCENE_ID)
        self.B = {b["id"]: b for b in self.scene_spec["beats"]}
        self.V = {v["id"]: v for v in self.script.get("verify", [])}   # verified display numbers
        beats_audio = {}
        for bid, b in self.B.items():
            entry = {"narration": b["narration"], "audio": f"{bid}.wav"}
            words_file = root / "words" / f"{bid}.json"            # alignment stage ka output (doc 16)
            if words_file.exists():
                entry["word_boundaries"] = to_word_boundaries(
                    b["narration"], json.loads(words_file.read_text(encoding="utf-8")))
            elif "<bookmark" in b["narration"]:
                entry["word_boundaries"] = []                      # alignment nahi: linear fallback
            beats_audio[bid] = entry
        self.set_speech_service(PrebakedService(audio_dir=str(root / "audio"), beats=beats_audio))
        self.durations = durations

    def beat(self, beat_id: str):
        """with self.beat('b042') as t: ...   (narration script.json se)"""
        return self.voiceover(text=self.B[beat_id]["narration"], beat_id=beat_id)

    def num(self, verify_id: str) -> str:
        """Screen par dikhane wala verified number string."""
        return self.V[verify_id]["display"]

    def pause(self, beat_id: str):
        self.safe_wait(self.B[beat_id].get("pause_after", 0.25))
```

> **Tested (2026-10-18):** Ek fake topic folder (`script.json` + 2 sine-tone WAVs + `durations.json`) ke saath `LessonScene` render kiya. (1) Bina `words/` ke bookmark linear fallback se chala (warning ke saath); (2) `words/b041.json` (alignment output) dene par fallback warning gayi aur precise boundaries use hui. Dono runs mein video 6.6 s ka bana (2.5 + 0.3 + 3.5 + 0.4 = 6.7 s; 15 fps preview par frame rounding), aur `.srt` + `.wav` bhi bane. Pehle version mein `LessonScene` word boundaries pass nahi karta tha, isliye bookmark wala beat crash hota tha. Wo fix upar code mein hai.

Generated scene ab chhota aur readable hota hai:
```python
from video.lib.scene_base import LessonScene
from video.lib.components import HighlightTable, ResultBox
from manim import *

class S05WorkedExample(LessonScene):
    TOPIC_DIR = "video/out/L20/T07_information_gain"
    SCENE_ID = "s05_worked_example"

    def construct(self):
        table = HighlightTable.from_data(self.script["data"]["playtennis"]).to_edge(LEFT)
        with self.beat("b040") as t:
            self.play(FadeIn(table), run_time=min(1.5, t.duration))
            self.play(table.glow_column("Outlook"))
        self.pause("b040")

        with self.beat("b041") as t:
            self.play(table.highlight_rows(Outlook="Sunny"), run_time=1.0)
            self.wait_until_bookmark("split")          # word boundaries chahiye (section 7)
            label = MathTex(r"\text{Sunny}: 2^{+},\ 3^{-}").next_to(table, RIGHT, buff=1)
            self.play(Write(label))
        self.pause("b041")

        with self.beat("b042") as t:
            eq = MathTex(r"H(S_{\text{Sunny}}) =", self.num("H_sunny")).next_to(label, DOWN)
            self.play(Write(eq), run_time=min(2.0, t.duration))
            self.play(ResultBox.around(eq[1]))
        self.pause("b042")
```

---

## 7. Bookmarks

### Syntax
```text
"Pehle data dekho. <bookmark mark='formula'/>Ab formula lagate hain."
```
- Regex (source): `<bookmark\s*mark\s*=['"]\w*["']\s*/>`, isliye mark name mein **sirf letters, digits, underscore**. `mark='gain-box'` (hyphen) match **nahi** hoga, aur tag narration mein reh jaayega!
- TTS ko bhejne se pehle bookmarks hata diye jaate hain (`remove_bookmarks`)

### Word boundaries kahan se aayengi?
`wait_until_bookmark` ko word boundaries chahiye. Teen options:
1. **`transcription_model="base"`** (ya bada model) service init mein → library khud Whisper se transcribe karegi. Install: `pip install "manim-voiceover[transcribe]"`. Hinglish par accuracy check karo
2. **Hamari apni alignment** (stable-ts align / WhisperX, [16](16_Word_Timestamps_Forced_Alignment_Captions.md)) → `word_boundaries` dict mein do
3. Kuch nahi → library warning dekar **linear fallback** use karti hai (character position ke proportion se time). Chhote beats mein aksar theek rehta hai

Agar boundaries hi nahi hain (na transcription, na diye), to `wait_until_bookmark` exception deta hai: *"Word boundaries are required for timing with bookmarks..."*. Fallback sirf tab lagta hai jab `word_boundaries` key maujood ho lekin 2 se kam entries hon. Isliye bina alignment ke bhi bookmarks use karne hon to service mein empty list do:
```python
data["word_boundaries"] = []      # empty list → tracker linear fallback use karega (warning ke saath)
```
(Ye behaviour humne render karke confirm kiya: section 10.)

---

## 8. Subcaptions

- Default `create_subcaption=True`: har voiceover ka text (bookmarks hata kar) subcaption ban jaata hai, `max_subcaption_len=70` chars ke chunks mein, proportional timing ke saath
- Manim output video ke saath `.srt` likhta hai
- Captions mein spoken numbers ("zero point nine four zero") aayenge. Behtar captions ke liye: `self.voiceover(text=..., subcaption="Entropy aati hai 0.940.")` (`subcaption` kwarg), ya final SRT apni alignment se banao ([16](16_Word_Timestamps_Forced_Alignment_Captions.md))

---

## 9. Gotchas (source padh kar mili)

| Gotcha | Detail | Fix |
|---|---|---|
| Sirf WAV/MP3 duration | `get_duration` `.wav` ke alawa sab ko MP3 samajhta hai | Output `.wav` ya `.mp3` rakho |
| `original_audio` relative hona chahiye | Tracker `Path(cache_dir) / final_audio` se padhta hai | File `cache_dir` mein copy/save karo, sirf naam return karo |
| Bookmark name mein hyphen | Regex `\w*` hai | `[A-Za-z0-9_]` only |
| `global_speed` | SoX binary chahiye; awaaz ki quality girti hai | Use mat karo; TTS ke apne speed param use karo |
| SoX warning on import | `sox` Python package binary dhundhta hai | Ignore (agar speed change nahi) ya SoX install karo |
| `-s` (save last frame) mode | Subcaptions automatically off | Normal |
| Cache stale | Voice badli lekin `input_data` same | `input_data` mein voice/model/params/ref hash daalo |
| Alpha status | API badal sakta hai | `manim-voiceover==0.4.0` pin karo |

---

## 10. Minimal end-to-end test (TTS ke bina)

Pipeline test karne ke liye fake audio (sine tone) ke saath:
```python
# test_prebaked.py
import numpy as np, soundfile as sf, json, os
from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_service import PrebakedService   # upar ka class (same folder mein rakho)

os.makedirs("audio", exist_ok=True)
for bid, secs in {"b001": 2.0, "b002": 3.0}.items():
    t = np.linspace(0, secs, int(24000 * secs), endpoint=False)
    sf.write(f"audio/{bid}.wav", 0.1 * np.sin(2 * np.pi * 220 * t), 24000)

BEATS = {"b001": {"narration": "Pehla beat.", "audio": "b001.wav"},
         "b002": {"narration": "Dusra beat <bookmark mark='X'/>yahan.", "audio": "b002.wav",
                  "word_boundaries": []}}

class T(VoiceoverScene):
    def construct(self):
        self.set_speech_service(PrebakedService(audio_dir="audio", beats=BEATS))
        with self.voiceover(text=BEATS["b001"]["narration"], beat_id="b001") as t:
            self.play(Write(Text("Beat 1")), run_time=t.duration)
        with self.voiceover(text=BEATS["b002"]["narration"], beat_id="b002") as t:
            self.wait_until_bookmark("X")
            self.play(FadeIn(Text("Bookmark!").shift(DOWN)))
```
```bash
manim -ql test_prebaked.py T
ffprobe -v error -show_entries format=duration -of csv=p=0 media/videos/test_prebaked/480p15/T.mp4
# expected ≈ 5.0 s (2 + 3)
```

**Asli test result (2026-10-18, manim 0.22.0 + manim-voiceover 0.4.0, macOS):**
- Duration **5.03 s** ✅ (15 fps preview par frame rounding ki wajah se thoda upar)
- Output folder mein `T.mp4` (video + audio streams), **`T.srt`** (subcaptions) aur **`T.wav`** (scene ka poora audio) bane
- b002 par warning aayi: *"Word boundaries ... not available or are insufficient. Using fallback word boundaries."* Ye expected hai (empty list → linear fallback), aur bookmark par animation chala
- Test ke dauraan pakde gaye 2 bugs (docs mein fix kar diye): (1) `input_data` mein `input_text` required hai, (2) `word_boundaries` key empty list ho tab bhi set karni padti hai, warna `wait_until_bookmark` exception deta hai

> 💡 Manim ka `T.wav` final assembly mein kaam aata hai: har scene ka audio alag WAV mein milta hai, jise poori timeline par ek baar encode kar sakte ho ([27](27_FFmpeg_Final_Assembly.md)).

👉 Agla: [19_Manim_Component_Library_Design.md](19_Manim_Component_Library_Design.md)
