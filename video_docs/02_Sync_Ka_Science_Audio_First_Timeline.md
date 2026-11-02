# 02 · Sync Ka Science: Audio-First Timeline

> **Is file mein:** Audio aur animation "perfect sync" mein kaise rehte hain: concept, maths, teen levels of sync, aur aam galtiyan.

---

## 1. Problem kya hai?

Tumhe chahiye ki jab narrator bole "**ab ye entropy 0.940 aati hai**", theek usi waqt screen par `0.940` highlight ho. Na pehle, na baad mein.

Do tareeke hain:

| Approach | Kaise | Problem |
|---|---|---|
| ❌ **Video-first** | Pehle animation banao (jaise 5 sec), phir audio ko 5 sec mein fit karo | Audio stretch/squeeze karna padta hai, awaaz chipmunk ya slow-motion jaisi lagti hai. Ya beech mein silence/overlap aata hai |
| ✅ **Audio-first** | Pehle audio banao, uski duration naapo (4.37 s), phir animation ko 4.37 s ka banao | Koi problem nahi. Animation ki speed badalna free hai, koi quality loss nahi |

**Golden rule:** 🎙️ **Audio master clock hai. Video audio ke peeche chalta hai.**

Animation ka `run_time` ek number hai. Use 2.1 s karo ya 4.37 s, quality par koi asar nahi padta. Awaaz ki speed badloge to quality kharab hogi.

---

## 2. Teen levels of sync

### Level 1: Beat-level sync (90% kaam isi se ho jata hai) ✅
Narration ko chhote **beats** mein todo. Ek beat = 1–3 sentences = ek visual idea.

```
Beat 07: "Sunny wale din 5 hain: 2 mein tennis khela, 3 mein nahi."
         → Visual: table ki Sunny rows highlight, "2+ / 3−" likha aaye
         → Audio: beat_07.wav = 3.84 s
         → Animation run_time = 3.84 s
```

Har beat ka audio alag file hai, aur har beat ka animation usi file ki duration ka hai. Beat khatam hone par next beat start. **Drift possible hi nahi**, kyunki har beat par clock "reset" hoti hai.

### Level 2: Bookmark sync (beat ke andar ek specific word par)
Kabhi ek beat ke andar hi ek specific shabd par kuch hona chahiye:

```
"Total entropy <bookmark mark='E'/>zero point nine four zero hai."
```
Jab narrator "zero point..." bolna shuru kare, tab `0.940` appear ho.

Iske liye **word-level timestamps** chahiye (kaun sa word kis millisecond par bola gaya). Ye forced alignment se milte hain ([16](16_Word_Timestamps_Forced_Alignment_Captions.md)). manim-voiceover isko `self.wait_until_bookmark("E")` se support karta hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)).

### Level 3: Word-level karaoke (har word highlight)
Subtitles mein har bola gaya word highlight hona (TikTok style). Educational video mein zaroori nahi, kabhi-kabhi distracting bhi hota hai. **Optional.**

### Recommendation
- **Default:** Level 1 (beat-level). Script likhte waqt hi beats chhote rakho, taaki bookmarks ki zaroorat kam pade.
- **Level 2 tab use karo** jab ek lambe sentence mein 2–3 cheezein alag-alag waqt par appear karni hon.
- **Level 3:** sirf captions file ke liye.

---

## 3. Timeline ka maths

### Beat ki start time
```
start(beat_i) = Σ (duration(beat_j) + gap_j)   for j < i
```
`gap` = beats ke beech chhota sa pause (jaise 0.25 s), jo saans lene jaisa natural lagta hai.

### Frame number
```
start_frame(beat_i) = round(start(beat_i) × 30)
```

### Rounding error accumulate kyun nahi hota?
Agar har beat ka frame count alag-alag round karke jodoge to error badhta jaata hai:
```
❌ frames_total = Σ round(d_i × 30)       ← har beat par ±0.5 frame error, 200 beats par ±100 frames tak!
✅ start_frame_i = round(cumulative_time_i × 30)   ← error hamesha ≤ 0.5 frame
```
**Rule:** Hamesha **cumulative seconds** se frame nikalo, alag-alag rounded frames ko mat jodo.

Manim internally time ko seconds mein track karta hai (`renderer.time`), isliye scene ke andar ye problem apne aap handle ho jati hai. Lekin agar tum ffmpeg/HyperFrames mein khud timeline banao to ye rule yaad rakhna.

### Example (real numbers)
| Beat | Duration (s) | Gap | Cumulative start (s) | Start frame @30 |
|---|---|---|---|---|
| 1 | 4.37 | 0.25 | 0.00 | 0 |
| 2 | 3.84 | 0.25 | 4.62 | 139 |
| 3 | 6.10 | 0.40 | 8.71 | 261 |
| 4 | 2.95 | 0.25 | 15.21 | 456 |

---

## 4. Animation ke andar time kaise baantein

Ek beat ka audio 6.10 s hai, aur usme 3 animations chahiye: table highlight, formula likhna, result box. Teen tareeke hain:

### Tareeka A: Proportional split (simple)
```python
with self.voiceover(text=beat.narration) as t:
    self.play(Indicate(row), run_time=t.duration * 0.25)
    self.play(Write(formula), run_time=t.duration * 0.50)
    self.play(Create(box), run_time=t.duration * 0.25)
```

### Tareeka B: Bookmarks (precise)
```python
with self.voiceover(text="Sunny rows dekho. <bookmark mark='F'/>Formula lagao. <bookmark mark='R'/>Result 0.971.") as t:
    self.play(Indicate(row))
    self.wait_until_bookmark("F")
    self.play(Write(formula))
    self.wait_until_bookmark("R")
    self.play(Create(box))
```

### Tareeka C: Sub-beats (sabse robust) ✅
Beat ko hi 3 chhote beats mein tod do, har ek ka apna audio. Isme word alignment ki zaroorat hi nahi padti. Hinglish ke liye ye sabse safe hai, kyunki Hinglish par alignment models kamzor hain ([16](16_Word_Timestamps_Forced_Alignment_Captions.md)).

**Trade-off:** Sub-beats ke beech micro-pauses aate hain. Agar TTS har chhote chunk ko alag intonation de to thoda "tukdon mein" bolta hua lag sakta hai. Bake-off mein ye bhi check karna ([13](13_TTS_BakeOff_Kaise_Kare.md)).

---

## 5. "Hold" aur "Breathing room"

Insaan ko samajhne ke liye waqt chahiye:
- **Naya formula aane ke baad:** 0.5–1.5 s silence + formula screen par rahe
- **Important result ke baad:** 1 s pause
- **Pause-and-try question:** 5–10 s (countdown timer dikhao)
- **Scene change se pehle:** 0.3–0.5 s

Ye pauses script JSON mein `pause_after` field se control hote hain ([06](06_Script_JSON_Schema_Reference.md)). Audio mein silence add karna (ffmpeg/pydub se) ya Manim mein `self.wait(x)` lagana, dono chalega.

---

## 6. Common sync galtiyan

| Galti | Symptom | Fix |
|---|---|---|
| Poora topic ek TTS call mein | Beech mein awaaz badalti hai, sync drift | Beats mein todo |
| Audio speed change (`global_speed`) | Awaaz unnatural lagti hai | TTS model ka apna `speed` param use karo, ya script chhoti karo |
| Frames alag-alag round karke jodna | Lambe video mein 1–3 sec ka drift | Cumulative time se frame nikalo |
| Audio sample rate mismatch (24k vs 48k) concat mein | Pitch/speed galat, ya clicks | Final mix mein sab ko 48 kHz par resample karo |
| AAC encoder priming delay | Har clip ke start par ~20–40 ms ka offset, concat ke baad jud kar badhta hai | Clips ko audio ke bina concat karo, audio ek hi baar poori timeline par lagao (ya WAV/PCM intermediate rakho) ([27](27_FFmpeg_Final_Assembly.md)) |
| Animation audio se lamba | Narrator chup, animation chal raha (awkward) | `run_time` ko `t.duration` se cap karo |
| Animation audio se chhota | Screen freeze, awaaz chal rahi | Normal hai, `voiceover` block khud baaki time wait kar leta hai |

> **AAC priming note:** AAC encoders har stream ke start mein kuch "priming samples" daalte hain. Isliye bahut saare chhote AAC clips ko `-c copy` se jodne par chhoti-chhoti gaps/offsets jud sakti hain. Safe tareeka: final timeline par audio ek hi baar encode karo. Detail [27](27_FFmpeg_Final_Assembly.md) mein.

---

## 7. manim-voiceover andar se kya karta hai (source code padh kar)

v0.4.0 ka source padhne par ye flow milta hai:
1. `with self.voiceover(text=...) as tracker:` call hua
2. Speech service `generate_from_text()` chalata hai, audio file banti hai (cache mein hai to wahi use hoti hai)
3. `tracker.duration` = audio file ki length (`mutagen` library se padhi jaati hai)
4. `self.add_sound(audio_path)`: audio current scene time par timeline mein lag jaata hai
5. Tumhare animations chalte hain
6. Block khatam hone par `wait_for_voiceover()`: agar audio abhi baaki hai to utna `wait` khud ho jaata hai

Matlab **audio-first wala pattern library mein hi built-in hai.** Hume bas local TTS ka wrapper likhna hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)).

---

## 8. Ek line mein yaad rakho

> **Pehle bolo, phir dikhao. Audio ki duration naapo, animation ko utna hi lamba banao. Cumulative time se frames nikalo. Audio ek hi baar final timeline par encode karo.**

👉 Agla: [03_Pedagogy_Teaching_Design_Principles.md](03_Pedagogy_Teaching_Design_Principles.md)
