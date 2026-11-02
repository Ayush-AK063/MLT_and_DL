# 27 · FFmpeg: Final Assembly

> **Is file mein:** Scene videos + cards + audio + music + subtitles + chapters ko jod kar final MP4 banana. Har command ka matlab, aur AAC priming / format mismatch jaisi problems ka solution. Saare commands humne locally test kiye.

---

## 1. Flow

```
renders/s01.mp4 … s09.mp4   (Manim: video + audio)
cards/intro.mp4, outro.mp4  (HyperFrames)
          │
          ├─► [A] VIDEO track: sab clips ka video concat (no audio)       → video_only.mp4
          ├─► [B] AUDIO track: sab clips ka audio WAV mein concat          → narration_full.wav
          │        → loudnorm (2-pass, −14 LUFS) → + music (ducked)        → mix.wav
          └─► [C] MUX: video_only + mix.wav (AAC ek baar) + chapters + faststart → T07.mp4
                  + T07.srt (alag file)
```

**Kyun video aur audio alag?** AAC audio ke har stream ki shuruaat mein encoder "priming" samples daalta hai. Bahut saare AAC clips ko seedha jodne par har jod par chhote offsets/gaps aa sakte hain, jo lambe video mein jud kar badh jaate hain. Audio ko **PCM (WAV) mein jod kar ek hi baar AAC encode** karne se ye problem khatam ho jaati hai ([02](02_Sync_Ka_Science_Audio_First_Timeline.md)).

---

## 2. Step 0: Sab clips ka format same karo

`-c copy` concat tabhi kaam karta hai jab sab clips ka **codec, resolution, fps, pixel format, timebase** same ho. Cards (HyperFrames) aur scenes (Manim) alag tools se aate hain, isliye pehle normalize karo:

```bash
ffmpeg -y -i cards/intro.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p" \
  -c:v libx264 -preset medium -crf 18 -g 15 -bf 2 \
  -c:a pcm_s16le -ar 48000 -ac 2 \
  norm/intro.mkv
```
| Part | Matlab |
|---|---|
| `scale=...:force_original_aspect_ratio=decrease,pad=...` | Aspect ratio bigaade bina 1920×1080 mein fit |
| `fps=30` | 30 fps |
| `format=yuv420p` | Universal pixel format |
| `-g 15 -bf 2` | GOP = fps/2 = 15, 2 B-frames (YouTube recommendation) |
| `-c:a pcm_s16le -ar 48000 -ac 2` | Intermediate audio PCM 48 kHz stereo (lossless) |
| `.mkv` | MKV container PCM audio rakh sakta hai (MP4 mein PCM support limited hai) |

> Manim renders ko bhi isi command se normalize kar sakte ho. Simple aur safe hai, bas thoda encode time lagta hai. Agar sab clips already same settings ke hain (`manim -qh --fps 30`), to video ke liye ye step skip karke direct concat kar sakte ho.

---

## 3. Step A: Video concat (concat demuxer)

```bash
# list.txt
file 'norm/intro.mkv'
file 'norm/s01.mkv'
file 'norm/s02.mkv'
file 'norm/outro.mkv'
```
```bash
ffmpeg -y -f concat -safe 0 -i list.txt -map 0:v -c:v copy video_only.mkv
```
- `-f concat`: concat demuxer (bina re-encode jodta hai)
- `-safe 0`: absolute/relative paths allow
- `-map 0:v`: sirf video
- `-c:v copy`: re-encode nahi (fast, koi quality loss nahi)

---

## 4. Step B: Audio concat + loudness + music

```bash
ffmpeg -y -f concat -safe 0 -i list.txt -map 0:a -c:a pcm_s16le -ar 48000 -ac 2 narration_full.wav
```
Phir:
1. **Loudnorm 2-pass** → `narration_norm.wav` (−14 LUFS, −1 dBTP) ([15](15_Audio_Post_Processing_Loudness_Music.md) §4)
2. **Music + ducking** → `mix.wav` ([15](15_Audio_Post_Processing_Loudness_Music.md) §6)
3. Final loudness check:
```bash
ffmpeg -i mix.wav -af ebur128=peak=true -f null - 2>&1 | grep -A8 Summary
```

---

## 5. Step C: Chapters metadata

`chapters.txt` (FFMETADATA format), times milliseconds mein (`TIMEBASE=1/1000`):
```ini
;FFMETADATA1
title=L20 T07 · Information Gain

[CHAPTER]
TIMEBASE=1/1000
START=0
END=30500
title=Hook: Pehla sawaal kaunsa?

[CHAPTER]
TIMEBASE=1/1000
START=30500
END=61000
title=Recap: Entropy

[CHAPTER]
TIMEBASE=1/1000
START=61000
END=152000
title=Intuition: Kamra saaf karna
```
Chapter boundaries = scene start times (cumulative durations se). Python se generate karo:
```python
def ffmetadata(title: str, chapters: list[tuple[str, float, float]]) -> str:
    out = [";FFMETADATA1", f"title={title}", ""]
    for name, start, end in chapters:
        out += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(round(start * 1000))}",
                f"END={int(round(end * 1000))}", f"title={name}", ""]
    return "\n".join(out)
```

---

## 6. Step D: Final mux + encode

```bash
ffmpeg -y -i video_only.mkv -i mix.wav -i chapters.txt \
  -map 0:v -map 1:a -map_metadata 2 -map_chapters 2 \
  -c:v copy \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  -shortest \
  T07.mp4
```
| Part | Matlab |
|---|---|
| `-map 0:v -map 1:a` | Video pehli file se, audio doosri se |
| `-map_metadata 2 -map_chapters 2` | Title + chapters teesri file (FFMETADATA) se |
| `-c:v copy` | Video already H.264 hai |
| `-c:a aac -b:a 192k` | AAC-LC 192 kbps (speech + music ke liye kaafi) |
| `-movflags +faststart` | `moov` atom file ke shuru mein (YouTube recommendation; streaming jaldi shuru hoti hai) |
| `-shortest` | Video/audio mein jo chhota ho, wahan khatam (safety) |

### Agar video ko bhi final encode karna hai (ek hi command mein)
```bash
ffmpeg -y -i video_only.mkv -i mix.wav -i chapters.txt \
  -map 0:v -map 1:a -map_metadata 2 -map_chapters 2 \
  -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p -g 15 -bf 2 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart \
  T07.mp4
```

---

## 7. Subtitles

**Soft subs (recommended):** SRT ko alag rakho aur YouTube par upload karo ([32](32_Publishing_YouTube.md)).

MP4 ke andar soft subtitle track (offline players ke liye):
```bash
ffmpeg -i T07.mp4 -i T07.srt -map 0 -map 1 -c copy -c:s mov_text -metadata:s:s:0 language=hin T07_subs.mp4
```

**Burned-in** (Shorts/Reels ke liye, jahan soft subs nahi chalte):
```bash
ffmpeg -i T07.mp4 -vf "subtitles=T07.srt:force_style='FontName=Inter,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,BorderStyle=3'" -c:a copy T07_burned.mp4
```
> Windows par `subtitles=` filter mein path escaping tricky hai (`C\:/path/file.srt`). Relative path aur simple naam use karo.

---

## 8. Full lecture video (saare topics jodna)

```bash
# lecture_list.txt
file 'out/L20/T01_job_offer/T01.mp4'
file 'out/L20/T02_tree_terms/T02.mp4'
...
```
Topics ke final MP4 mein AAC audio hai. Wahi priming problem dobara aa sakti hai, isliye do options hain:
1. **Recommended:** Har topic ka `video_only.mkv` + `mix.wav` rakho, aur poore lecture ka video + audio **wahi Step A–D process** se banao (audio ek hi baar encode)
2. **Quick:** `-c copy` concat of MP4s. Chhote offsets aa sakte hain; lambe video mein sync check karo

Lecture-level chapters: har topic ek chapter (aur optionally har scene sub-chapter).

---

## 9. Verification commands

```bash
# Duration
ffprobe -v error -show_entries format=duration -of csv=p=0 T07.mp4
# Streams
ffprobe -v error -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels -of compact T07.mp4
# Chapters
ffprobe -v error -show_chapters -of compact T07.mp4
# Loudness
ffmpeg -i T07.mp4 -af ebur128=peak=true -vn -f null - 2>&1 | grep -A8 Summary
# faststart (moov atom pehle?)
ffprobe -v trace T07.mp4 2>&1 | grep -m3 -E "type:'(moov|mdat)'"
```

---

## 10. Asli test (2026-10-18, ffmpeg locally)

Humne is file ke commands do chhote Manim test renders (480p15, sine-tone audio ke saath) par chala kar dekhe: normalize → video concat → audio concat → loudnorm (2-pass, [15](15_Audio_Post_Processing_Loudness_Music.md) ka Python function) → chapters → final mux → soft subs. ffmpeg version 8.1.2.

**Result (`ffprobe` output):**
```
duration      10.07 s            (5.03 + 5.03 + rounding ✅)
video         h264 1920x1080 yuv420p 30/1      ✅ (480p15 input se upscale + fps convert)
audio         aac 48000 Hz 2 ch                ✅
chapters      0.000–5.030 "Scene one", 5.030–10.070 "Scene two"   ✅
loudness      I: -14.0 LUFS                    ✅
faststart     moov atom mdat se pehle          ✅
soft subs     mov_text track add hua           ✅
```
Test se mile 2 fixes (docs mein update kar diye):
1. ffmpeg 8.x mein loudnorm ka JSON block output ke **beech** mein aata hai (baad mein aur lines hoti hain), isliye parse karne ke liye aakhri `{...}` block lena padta hai
2. `loudnorm` internally **192 kHz** par upsample karta hai, isliye output par `-ar 48000` zaroori hai

> Note: Chapters wali MP4 mein ffprobe ek extra `bin_data` (data) stream dikhata hai. Ye MP4 ka chapter track hai, normal hai.

👉 Agla: [28_Quality_Assurance_Checklist.md](28_Quality_Assurance_Checklist.md)
