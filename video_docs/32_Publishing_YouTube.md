# 32 · Publishing: YouTube (aur Site Embedding)

> **Is file mein:** YouTube upload settings (official recommendations), chapters, subtitles, title/description template, thumbnail, playlist structure, AI disclosure, aur existing MLT site mein embed karna.

---

## 1. Upload file settings (YouTube official recommended specs)

| Setting | Value |
|---|---|
| Container | **MP4**, no edit lists, **moov atom at front** (`-movflags +faststart`) |
| Video codec | **H.264**, progressive, **High Profile**, CABAC |
| B-frames | 2 consecutive |
| GOP | **Closed GOP, half the frame rate** (30 fps → 15) |
| Bitrate | Variable; 1080p @ 24–30 fps: **8 Mbps** recommended; 1440p @ 24–30: **16 Mbps** |
| Chroma | **4:2:0** (`yuv420p`) |
| Frame rate | Jis rate par content bana, wahi (hamare liye 30) |
| Audio codec | **AAC-LC** (ya Opus) |
| Audio channels | Stereo (ya stereo + 5.1) |
| Audio sample rate | **48 kHz** |

Hamara final encode ([27](27_FFmpeg_Final_Assembly.md) §6) in sab ko follow karta hai. CRF 18 aam taur par flat animation ke liye recommended bitrate ke aas-paas ya neeche hi rehta hai, jo theek hai (YouTube re-encode karta hai, aur high-quality source hi matter karta hai).

---

## 2. Chapters (description mein)

YouTube rules (official):
- Pehla timestamp **00:00** hona chahiye
- Kam se kam **3 timestamps**
- **Ascending order**
- Har chapter **≥ 10 seconds**
- Format: har line mein timestamp + title

```text
00:00 Hook: Pehla sawaal kaunsa?
00:30 Recap: Entropy
01:01 Intuition: Kamra saaf karna
02:32 Gain ka formula
04:12 Worked example: Outlook ka gain
07:35 Kaun jeeta? (comparison)
08:40 Pause & try: Wind ka gain
09:45 Common mistake
10:25 Recap
```
Ye pipeline `chapters` data se auto-generate karti hai (scene start times). Embedded MP4 chapters (FFMETADATA) offline players ke liye hain. YouTube description wale chapters use karta hai.

```python
def yt_chapters(chapters: list[tuple[str, float]]) -> str:
    long_video = chapters[-1][1] >= 3600            # 1 ghante se lamba: sab timestamps h:mm:ss mein (consistent)
    def ts(s):
        s = int(s)
        return f"{s // 3600}:{s % 3600 // 60:02}:{s % 60:02}" if long_video else f"{s // 60:02}:{s % 60:02}"
    assert chapters[0][1] == 0, "pehla chapter 00:00 par"
    assert len(chapters) >= 3
    for (_, a), (_, b) in zip(chapters, chapters[1:]):
        assert b - a >= 10, "har chapter >= 10 s"
    return "\n".join(f"{ts(t)} {name}" for name, t in chapters)
```
> Last chapter ki length bhi ≥ 10 s honi chahiye (video end tak). Function sirf beech wale check karta hai, isliye total duration ke saath last bhi check karo.

---

## 3. Subtitles

- `T07.srt` upload karo: YouTube Studio → Subtitles → Add language → Upload file (with timing)
- Language: Hinglish ke liye "Hindi" ya "English" choose karna padega (YouTube par "Hinglish" alag language nahi hai). Roman script captions ke saath **English** zyada practical hai; Devanagari captions ke liye Hindi
- Captions mein numbers digits mein ([16](16_Word_Timestamps_Forced_Alignment_Captions.md) §7)
- Bonus: English translation captions (Claude se translate + review), jo non-Hindi viewers ke liye hain

---

## 4. Title / description template

**Title** (≤ 70 chars visible):
```
Information Gain Explained (Hinglish) | Decision Trees | MLT L20 · T7
```

**Description:**
```text
Information Gain kya hai aur ID3 algorithm best attribute kaise chunta hai? Is video mein hum
PlayTennis dataset par step-by-step Outlook ka gain (0.2467) calculate karte hain.

📚 Lecture 20 · Topic 7 | Machine Learning Techniques (ES514)
📝 Notes: <site link>

⏱️ Chapters
00:00 Hook ...
(auto)

🔗 Pichhla: Entropy <link> | Agla: ID3 steps <link>

ℹ️ Narration AI voice se generate hui hai (local TTS), aur animations code (Manim) se bani hain.
   Saare numbers Python se verify kiye gaye hain.

Music: <title> by <artist> (<license>)
```

---

## 5. AI / synthetic content disclosure

YouTube creators se realistic altered/synthetic content (jaise realistic AI awaaz ya chehra jo asli lag sake) disclose karwata hai (Studio mein upload ke time "Altered content" setting). Hamare case mein:
- **AI narration (TTS)** + **apni cloned awaaz**: disclosure honest aur safe choice hai
- Animated maths visuals: aam taur par disclosure ki category mein nahi aate
- Policy details badalti rehti hain: upload ke time YouTube Help Center ka current guidance dekho

Description mein ek line likhna ("Narration AI-generated hai") trust banata hai.

---

## 6. Thumbnail

| Spec | Value |
|---|---|
| Resolution | 1280×720 (16:9) |
| Format | JPG/PNG |
| Text | 3–5 words, bada, high contrast |
| Visual | Ek central element (tree, formula ka hissa, bar chart) |
| Consistency | Series template: same font/colors, corner mein "L20" |

Manim se hi thumbnail bana sakte ho (`manim -s -r 1280,720 thumb.py Thumb`), isliye style automatically consistent rehti hai.

---

## 7. Playlist structure

```
📁 MLT (ES514) · Full Course (Hinglish)
   ├── L1 · Introduction to ML        (playlist ya full-lecture video)
   ├── ...
   └── L22 · Random Forest
📁 L20 · Decision Trees & ID3 (topic-wise)
   ├── T01 Job offer example
   ├── ...
   └── T10 Outlook gain worked example
```
- **Topic videos** (8–20 min) = main content
- **Full lecture video** (1–2 hr) = binge/revision ke liye, chapters ke saath

---

## 8. Existing MLT site mein embed

Site (`MLT_Python/site/`) ke har topic page par video embed:
```html
<div class="video-wrap" style="position:relative;padding-top:56.25%">
  <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID?rel=0"
          title="Information Gain" loading="lazy"
          style="position:absolute;inset:0;width:100%;height:100%;border:0"
          allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
- `youtube-nocookie.com` privacy-enhanced mode hai
- Video IDs ko `build_site.py` ke data mein ek field ke roop mein add karo (jaise topic metadata mein `video_id`), taaki rebuild par embed apne aap aaye
- Chatbot data (`build_chat_data.py`) mein bhi video link daal sakte ho ("is topic ka video yahan hai")

---

## 9. Publish checklist
- [ ] [28](28_Quality_Assurance_Checklist.md) ka G7 pass
- [ ] Title, description, chapters, tags
- [ ] SRT uploaded
- [ ] Thumbnail
- [ ] Playlist(s) mein add
- [ ] AI disclosure (Studio setting + description line)
- [ ] Music attribution
- [ ] Site par embed + rebuild
- [ ] Visibility: pehle **Unlisted**, 1–2 logon se feedback, phir Public

👉 Agla: [33_Pilot_Plan_L20_Entropy_Information_Gain.md](33_Pilot_Plan_L20_Entropy_Information_Gain.md)
