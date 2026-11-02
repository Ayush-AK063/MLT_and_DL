# 15 · Audio Post-Processing: Silence, Loudness, Music, Ducking

> **Is file mein:** TTS ke raw audio ko "studio quality" banana: silence trim, consistent loudness (LUFS), background music, ducking (narration ke time music dheema), aur final mix ke ffmpeg commands.

---

## 1. Seedhi baat

TTS ka raw output har beat mein thoda alag hota hai: kisi ke start mein lamba silence, kisi ki awaaz zyada tez, kisi ke end mein click. Post-processing se har beat ek jaisi lagti hai, aur poora video professional sunai deta hai.

```
raw beat.wav → trim silence → (optional) light EQ/de-click → per-beat level match
            → [timeline par jodo] → final loudnorm (−14 LUFS, −1 dBTP) → + music (ducked) → final
```

---

## 2. Silence trim (har beat)

TTS aksar start/end mein 0.1–0.5 s silence deta hai. Hum chahte hain ki **beats ke beech gap hum control karein** (`pause_after`), model nahi.

```bash
ffmpeg -y -i raw/b042.wav -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse" audio/b042.wav
```
- `areverse` trick: pehle start se silence hatao, phir reverse karke "end" ka silence hatao, aur wapas reverse
- `start_silence=0.05`: 50 ms silence chhod do, taaki words ka start na kate
- Threshold −45 dB se shuru karo; agar soft consonants kat rahe hain to −50 dB karo

Python (pydub) alternative:
```python
from pydub import AudioSegment, silence

def trim(path_in, path_out, thresh_db=-45, keep_ms=50):
    a = AudioSegment.from_wav(path_in)
    start = silence.detect_leading_silence(a, silence_threshold=thresh_db)
    end = silence.detect_leading_silence(a.reverse(), silence_threshold=thresh_db)
    a = a[max(0, start - keep_ms): len(a) - max(0, end - keep_ms)]
    a.export(path_out, format="wav")
```

> ⚠️ **Order important hai:** Trim karne ke **baad** duration naapo, kyunki animation ka `run_time` final trimmed audio se aana chahiye. Pipeline mein trim TTS stage ke turant baad hota hai, aur `durations.json` trimmed files se banta hai.

---

## 3. Per-beat level matching

Har beat ki loudness similar honi chahiye, warna beat badalte hi volume jump hota hai. Do approaches:

**A. Simple (recommended):** Har beat ko same LUFS par normalize karo (jaise −18 LUFS), aur final mix mein poore track ko −14 par le jao.
```bash
ffmpeg -y -i audio/b042.wav -af loudnorm=I=-18:TP=-2:LRA=7 -ar 24000 audio_norm/b042.wav
```
> Bahut chhote clips (< ~3 s) par loudnorm ka measurement kam reliable hota hai (EBU R128 integration window ki wajah se). Isliye per-beat normalization **halka** rakho, aur asli normalization poori timeline par karo (section 4).

**B. Better:** Pehle saare beats ek timeline mein jodo, phir poori track ko ek baar normalize karo. Per-beat sirf **peak/RMS outliers** fix karo (jaise koi beat baaki se 4 dB zyada tez hai).

---

## 4. Final loudness normalization (EBU R128, ffmpeg `loudnorm`)

### Target
| Parameter | Value | Kyun |
|---|---|---|
| Integrated loudness `I` | **−14 LUFS** | YouTube ~−14 LUFS par normalize karta hai, aur dheemi audio ko boost nahi karta |
| True peak `TP` | **−1 dBTP** | Encoding (AAC) ke baad clipping se bachne ke liye |
| Loudness range `LRA` | 7–11 | Speech ke liye narrow range theek hai |

> Podcasts aksar −16 LUFS (stereo) use karte hain. YouTube-first content ke liye −14 common hai. (Pichhli chat mein maine −16 bola tha; YouTube target ke liye −14 zyada sahi hai. [39](39_Verification_Log.md) dekho.)

### Two-pass loudnorm (accurate)
**Pass 1: measure**
```bash
ffmpeg -i narration_full.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | tail -n 12
```
Output mein `input_i`, `input_tp`, `input_lra`, `input_thresh`, `target_offset` milenge.

**Pass 2: apply (measured values ke saath, linear mode)**
```bash
ffmpeg -y -i narration_full.wav -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=-21.3:measured_TP=-4.2:measured_LRA=5.1:measured_thresh=-31.6:offset=0.2:linear=true:print_format=summary" -ar 48000 narration_final.wav
```
(Numbers example ke liye hain; Pass 1 ka output daalo.)

> ⚠️ **Gotcha (test mein dekha):** `loudnorm` filter internally audio ko **192 kHz** par upsample karta hai. Output par `-ar 48000` nahi doge to final file 192 kHz ki ban jaayegi (4× badi aur kai tools mein problem). Isliye har loudnorm command ke end mein `-ar 48000` lagao.

**Kyun 2-pass?** Single-pass loudnorm "dynamic" mode mein chalta hai aur awaaz ko thoda squash kar sakta hai. 2-pass + `linear=true` poori file par ek hi gain lagata hai, jo speech ke liye zyada natural hai.

Python automation:
```python
import json, re, subprocess

def loudnorm_2pass(src, dst, I=-14, TP=-1, LRA=11, sr=48000):
    p1 = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-af",
                         f"loudnorm=I={I}:TP={TP}:LRA={LRA}:print_format=json",
                         "-f", "null", "-"], capture_output=True, text=True)
    # JSON block ke BAAD bhi ffmpeg lines print karta hai (ffmpeg 8.x), isliye aakhri {...} block lo
    m = json.loads(re.findall(r"\{[^{}]*\}", p1.stderr, re.S)[-1])
    af = (f"loudnorm=I={I}:TP={TP}:LRA={LRA}:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
          f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-i", src, "-af", af, "-ar", str(sr), dst], check=True)
```

---

## 5. Background music

### Kya music use karein
- **Royalty-free / license-clear** music hi use karo (YouTube Audio Library, ya jinka license explicitly allow kare). Content ID claims se bachne ke liye license ka record rakho ([38](38_Licenses_Legal_Ethics.md))
- **Style:** Calm, instrumental, no vocals, low-energy (lo-fi / ambient / soft piano)
- **Kab:** Intro, scene transitions, recap. Dense maths explanation ke time music **bahut dheema ya band** (Mayer ka coherence principle)

### Volume
- Narration ke neeche music ≈ **−20 se −30 dB** relative. Shuru mein −26 dB try karo
- Rule of thumb: agar music "notice" ho raha hai to zyada tez hai

---

## 6. Ducking (narration bole to music automatically dheema)

ffmpeg `sidechaincompress`: narration signal music ko compress karta hai.

```bash
ffmpeg -y -i narration_final.wav -stream_loop -1 -i music/calm_focus.mp3 -filter_complex "\
[1:a]volume=-18dB,aresample=48000[m]; \
[0:a]asplit=2[voice][sc]; \
[m][sc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[ducked]; \
[voice][ducked]amix=inputs=2:duration=first:normalize=0[mix]" \
-map "[mix]" -ar 48000 -ac 2 mix.wav
```
| Param | Matlab | Starting value |
|---|---|---|
| `threshold` | Narration kitni tez ho tab ducking shuru | 0.02 (~−34 dBFS) |
| `ratio` | Kitna dabana | 6–10 |
| `attack` | Kitni jaldi dabe (ms) | 20 |
| `release` | Narration ruke to kitni der mein music wapas aaye (ms) | 300–600 |
| `-stream_loop -1` | Music ko loop karo | |
| `duration=first` | Mix ki length = narration ki length | |
| `normalize=0` | `amix` inputs ko apne aap dheema na kare | |

> Ducking ke baad final mix par ek baar fir loudnorm check karo (−14 LUFS).

### Simple alternative (bina ducking)
Agar music sirf intro/outro mein hai aur narration ke time band hai, to ducking ki zaroorat nahi. Bas music ko `afade` ke saath fade-in/out karo:
```bash
ffmpeg -i music.mp3 -af "afade=t=in:st=0:d=1.5,afade=t=out:st=8.5:d=1.5,volume=-20dB" -t 10 intro_music.wav
```

---

## 7. Sound effects (subtle)

- "Result reveal" par halka "pop/ding", "pause-and-try" timer ke liye soft tick
- Volume narration se kaafi kam; har 30 s mein 1 se zyada nahi
- Over-use se video "cheap" lagta hai, isliye kam hi rakho

---

## 8. Audio QC checks (automatic)

```python
def audio_qc(path, expected_words):
    import soundfile as sf, numpy as np
    a, sr = sf.read(path)
    if a.ndim > 1:
        a = a.mean(axis=1)
    dur = len(a) / sr
    peak_db = 20 * np.log10(np.max(np.abs(a)) + 1e-9)
    rms_db = 20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-9)
    issues = []
    if dur < 0.3: issues.append("too_short")
    if dur < expected_words * 0.25: issues.append("possible_truncation")
    if dur > expected_words * 0.9: issues.append("possible_repetition")
    if peak_db > -0.5: issues.append("clipping_risk")
    if rms_db < -40: issues.append("too_quiet_or_silent")
    return {"duration": dur, "peak_db": peak_db, "rms_db": rms_db, "issues": issues}
```
(Thresholds starting points hain. ~140 wpm ka matlab ~0.43 s/word, isliye 0.25 s/word se kam truncation ka shaq hai aur 0.9 s/word se zyada repetition ka.)

---

## 9. Final mix checklist

- [ ] Har beat trimmed, durations trimmed files se
- [ ] Poori narration timeline: −14 LUFS integrated, ≤ −1 dBTP
- [ ] Music license recorded; narration ke time music ducked ya band
- [ ] 48 kHz, stereo
- [ ] Koi click/pop beat boundaries par nahi (zaroorat ho to 5–10 ms fade in/out per beat)
- [ ] Headphones aur phone speaker dono par suna

👉 Agla: [16_Word_Timestamps_Forced_Alignment_Captions.md](16_Word_Timestamps_Forced_Alignment_Captions.md)
