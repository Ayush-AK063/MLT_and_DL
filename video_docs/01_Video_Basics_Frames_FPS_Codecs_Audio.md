# 01 · Video Basics: Frames, FPS, Resolution, Codecs, Audio

> **Is file mein:** Video aur audio ki har basic term, zero se. Ise padhne ke baad ffmpeg commands aur render settings ka matlab samajh aayega.

---

## 1. Video asal mein hai kya?

**Seedhi baat:** Video = bahut saari photos (frames) jo tezi se ek ke baad ek chalti hain + saath mein ek audio track.

Flipbook yaad hai? Copy ke kono par thodi-thodi alag drawings banao aur tezi se palto, to drawing "chalti" hui dikhti hai. Video bhi yahi hai.

```
Frame 0   Frame 1   Frame 2   Frame 3  ...
 [ ● ]     [  ● ]    [   ● ]   [    ● ]    ← ball right ki taraf "move" karti dikhti hai
```

---

## 2. FPS (Frames Per Second)

**FPS = ek second mein kitni photos.**

| FPS | Kahan use hota hai | Hamare liye |
|---|---|---|
| 24 | Movies (cinematic feel) | Optional |
| **30** | YouTube, education, screen recordings | ✅ **Default choice** |
| 60 | Gaming, fast motion | Zaroorat nahi, file 2× badi aur render 2× slow |

### Frame ↔ time ka formula (ye yaad rakhna)
```
frame_number = round(time_in_seconds × fps)
time_in_seconds = frame_number / fps
```
- 30 fps par 1 frame = 1/30 sec = **33.33 ms**
- 10 min video = 600 s × 30 = **18,000 frames**
- 1 ghanta = 3600 × 30 = **108,000 frames**

**Kyun important hai:** Agar audio 4.37 sec ka hai to animation 4.37 × 30 = 131.1 ≈ **131 frames** ka hona chahiye. Max error aadha frame (~17 ms) hai, jo insaan ko pata hi nahi chalta.

### Manim mein FPS
Manim ke quality presets (official docs se):

| Flag | Resolution | FPS |
|---|---|---|
| `-ql` | 854×480 | 15 |
| `-qm` | 1280×720 | 30 |
| `-qh` | 1920×1080 | **60** |
| `-qp` | 2560×1440 | 60 |
| `-qk` | 3840×2160 | 60 |

⚠️ **Dhyan do:** `-qh` default 60 fps deta hai. Hume 30 chahiye, isliye `-qh --fps 30` likhna padega ([17](17_Manim_Basics_Install_Concepts.md)).

---

## 3. Resolution aur Aspect Ratio

**Resolution = ek frame mein kitne pixels (width × height).**

| Naam | Pixels | Kab |
|---|---|---|
| 720p | 1280×720 | Fast preview |
| **1080p (Full HD)** | 1920×1080 | ✅ Default final |
| 1440p (2K) | 2560×1440 | Agar equations bahut chhote hain to sharpness ke liye |
| 4K | 3840×2160 | Zaroorat nahi, render 4× slow |

**Aspect ratio 16:9** (YouTube standard). Shorts/Reels ke liye 9:16 (vertical) alag se banana padega.

**Tip:** Creators aam taur par report karte hain ki 1440p upload karne par 1080p playback bhi sharper dikhta hai (YouTube ke higher-resolution encodes zyada bitrate/better codecs paate hain). Ye YouTube ki official guarantee nahi hai, aur trade-off ye hai ki render time ~1.8× badhega. Pehle 1080p se shuru karo, aur pilot mein dono compare kar lo.

---

## 4. Codec, Container, Pixel Format

Ye teen alag cheezein hain jo log aksar mix kar dete hain:

| Term | Matlab | Example | Analogy |
|---|---|---|---|
| **Container** | File ka "dabba" jisme video + audio + subtitles rakhe jaate hain | `.mp4`, `.mkv`, `.mov`, `.webm` | Tiffin box |
| **Video codec** | Frames ko compress karne ka tareeka | H.264 (AVC), H.265 (HEVC), AV1, VP9 | Khana pack karne ka tareeka |
| **Audio codec** | Audio compress karne ka tareeka | AAC, Opus, MP3 | |
| **Pixel format** | Har pixel ka color kaise store hota hai | `yuv420p` | |

### Hamari final settings (YouTube ki official recommendation ke hisaab se)
- **Container:** MP4, `moov atom` file ke shuru mein (`-movflags +faststart`)
- **Video:** H.264, High profile, progressive, **4:2:0 chroma** (`-pix_fmt yuv420p`)
- **GOP:** closed GOP, length = frame rate ka aadha (30 fps → 15)
- **B-frames:** 2 consecutive
- **Audio:** AAC-LC, **48 kHz**, stereo

### `yuv420p` kyun zaroori hai?
Kai tools default mein `yuv444p` bana dete hain, jo kuch players (QuickTime, phones) par chalta hi nahi. `yuv420p` sab jagah chalta hai. **Hamesha final encode mein `-pix_fmt yuv420p` lagao.**

---

## 5. Bitrate, CRF aur Quality

**Bitrate = ek second video ke liye kitna data (Mbps).** Zyada bitrate ka matlab better quality aur badi file.

YouTube ka recommended upload bitrate (SDR):

| Resolution | 24/25/30 fps | 48/50/60 fps |
|---|---|---|
| 1080p | 8 Mbps | 12 Mbps |
| 1440p | 16 Mbps | 24 Mbps |

### CRF (Constant Rate Factor)
x264 encoder mein bitrate fix karne ki jagah **quality fix** karte hain:
- CRF 0 = lossless (huge file)
- **CRF 18** = visually near-lossless ✅ (master/upload ke liye)
- CRF 23 = x264 ka default
- CRF 28 = chhoti file, quality loss dikhta hai

Animation (flat colors, sharp text) bahut achhe se compress hoti hai, isliye CRF 18 par bhi file size reasonable rehta hai.

---

## 6. Keyframes / GOP (kyun concat mein dikkat aati hai)

Video codec har frame poora store nahi karta:
- **I-frame (keyframe):** Poori photo
- **P/B-frames:** Sirf "pichhle frame se kya badla"

**GOP (Group of Pictures)** = ek I-frame se agle I-frame tak ke frames.

**Practical asar:** Jab tum alag-alag clips ko `-c copy` (bina re-encode) se jodte ho, to sab clips ka codec, resolution, fps, pixel format aur audio format **bilkul same** hona chahiye. Warna glitches aate hain. Isliye hum sab scenes ek hi settings se render karte hain ([27](27_FFmpeg_Final_Assembly.md)).

---

## 7. Audio basics

### Sample rate
**Audio ek second mein kitni baar "naapa" gaya.**

| Rate | Kahan |
|---|---|
| 22.05 / 24 kHz | Kai TTS models ka output (Kokoro, IndicF5, Veena, Gemini TTS: 24 kHz) |
| 44.1 kHz | Music CD |
| **48 kHz** | Video standard, YouTube recommended ✅ |

**Rule:** TTS ka 24 kHz audio final mix mein **48 kHz par resample** karo. ffmpeg ye automatically kar deta hai jab `-ar 48000` doge.

### Bit depth
- 16-bit = standard (CD quality)
- 24-bit / 32-bit float = editing ke liye better headroom
- TTS models aksar float32 deta hai. Intermediate files WAV (16-bit ya float) mein rakho.

### Mono vs Stereo
Narration = **mono** (ek awaaz). Final file **stereo** banao (YouTube recommended); mono ko dono channels mein copy kar dete hain.

### WAV vs MP3
- **WAV:** Uncompressed, editing ke liye ✅ (intermediate)
- **MP3/AAC:** Compressed, final delivery ke liye
- ⚠️ manim-voiceover duration sirf `.wav` aur `.mp3` se padh sakta hai. Koi aur extension diya to wo use MP3 samajh kar padhta hai aur error aata hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)).

---

## 8. Loudness: LUFS, dBTP

**Seedhi baat:** Har video ki awaaz ek jaisi "zor" ki honi chahiye, taaki viewer ko baar-baar volume na badalna pade.

| Term | Matlab |
|---|---|
| **dBFS** | Digital peak level; 0 dBFS = maximum, isse upar clipping (awaaz phat jaati hai) |
| **LUFS** | Insaan ko awaaz kitni "loud" lagti hai, uska standard measure (EBU R128 / ITU BS.1770) |
| **Integrated LUFS** | Poori file ka average loudness |
| **True Peak (dBTP)** | Asli peak, sample ke beech ke peaks bhi count hote hain |
| **LRA** | Loudness Range: sabse dheemi aur sabse tez awaaz ka farak |

### Hamara target
- **Integrated: −14 LUFS** (YouTube ~−14 LUFS par normalize karta hai; ye officially documented nahi hai, lekin widely measured hai)
- **True peak: −1 dBTP**
- YouTube **dheemi awaaz ko loud nahi karta**, sirf tez ko dheema karta hai. Isliye −14 ke aas-paas rakhna better hai.

Detail: [15_Audio_Post_Processing_Loudness_Music.md](15_Audio_Post_Processing_Loudness_Music.md)

---

## 9. Subtitles / Captions

| Format | Kya hai |
|---|---|
| **SRT** | Simple text: number, `00:00:01,000 --> 00:00:03,500`, text |
| **VTT** | Web format, SRT jaisa (decimal point `.` use karta hai) |
| **Burned-in** | Video ke pixels mein hi likha (band nahi ho sakta) |
| **Soft subs** | Alag track, viewer on/off kar sakta hai ✅ |

YouTube ke liye **SRT alag upload** karo (soft subs). Manim khud bhi `add_subcaption` se `.srt` bana deta hai.

---

## 10. Ek page summary (cheat sheet)

```
Final master:
  Container : MP4 (+faststart)
  Video     : H.264 High, 1920x1080, 30 fps, yuv420p, CRF 18, GOP 15, bf 2
  Audio     : AAC-LC, 48 kHz, stereo, ~-14 LUFS integrated, -1 dBTP
  Subs      : SRT (alag file)

Intermediate:
  TTS audio : WAV, 24 kHz mono (model output)
  Scenes    : Manim MP4, same codec/fps/resolution sab mein
```

👉 Agla: [02_Sync_Ka_Science_Audio_First_Timeline.md](02_Sync_Ka_Science_Audio_First_Timeline.md)
