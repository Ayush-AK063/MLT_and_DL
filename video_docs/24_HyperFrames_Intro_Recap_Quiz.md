# 24 · HyperFrames: Intro, Recap aur Quiz Cards

> **Is file mein:** HyperFrames (HeyGen ka open-source HTML → MP4 framework) kya hai, kab use karein (Manim ki jagah nahi, uske saath), install, composition structure, GSAP animation, templates (intro, chapter, recap, quiz), aur pipeline integration.

---

## 1. HyperFrames kya hai

| Fact | Value (2026-10-18) |
|---|---|
| Kisne banaya | HeyGen (open-source) |
| Idea | **HTML + CSS + JS animations → deterministic MP4**. Headless Chrome har frame "seek" karke capture karta hai, aur FFmpeg encode karta hai |
| License | **Apache-2.0**, no per-render fees |
| Requirements | **Node.js 22+**, **FFmpeg** |
| Animation runtimes | GSAP (primary), Lottie, Three.js, Anime.js, CSS, WAAPI |
| AI-agent friendly | Claude Code plugin + agent skills available |
| Rendering | Local, Docker, AWS Lambda |

> Note: HyperFrames HeyGen ka AI avatar product **nahi** hai. Ye sirf rendering framework hai.

> 💰 **Budget mode:** HyperFrames free hai (Apache-2.0, Node), lekin ek aur toolchain hai. Shuru mein intro/recap/quiz cards bhi **template engine** se banao (`title`, `bullets`/`reveal`, `timer`; [41](41_Template_Engine_Zero_Cost_Animation.md)). Branded cards chahiye hon tab HyperFrames add karo.

### Manim vs HyperFrames: kaun kab
| Kaam | Tool |
|---|---|
| Equations, derivations, graphs, trees, data tables, maths animation | **Manim** |
| Intro/outro, chapter titles, recap bullet cards, quiz screens, lower-thirds, branded templates | **HyperFrames** |
| Final compositing (sab clips jodna) | **ffmpeg** (simple) ya HyperFrames (agar overlays/branding chahiye) |

**Kyun HyperFrames in cards ke liye?** Web technologies (CSS layouts, fonts, gradients) mein branded templates banana bahut aasaan hai. Devanagari fonts browser mein perfectly render hote hain, aur ek template likh kar har video ke liye sirf data badalna hota hai.

---

## 2. Install

```bash
node -v         # 22+ hona chahiye
ffmpeg -version

npx hyperframes init mlt-cards
cd mlt-cards
npx hyperframes preview      # browser mein live preview (hot reload)
npx hyperframes render       # MP4
```

### Claude Code ke saath
```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
# ya standalone agent skills:
npx skills add heygen-com/hyperframes
npx hyperframes skills update        # core skills install/update (non-interactive)
```
Phir Claude Code mein `/hyperframes` router skill creation workflows load karta hai.

---

## 3. Composition structure

Composition ek HTML file hai. Root element par composition metadata, aur har timed element ek "clip" hota hai:

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Noto+Sans+Devanagari:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body { margin: 0; background: #0F1117; }
    #root { width: 1920px; height: 1080px; position: relative; overflow: hidden;
            font-family: Inter, "Noto Sans Devanagari", sans-serif; color: #E8E6E3; }
    .center { position: absolute; inset: 0; display: grid; place-items: center; text-align: center; }
    #lecture { font-size: 40px; color: #8B8F98; letter-spacing: 4px; }
    #title { font-size: 96px; font-weight: 700; margin-top: 16px; }
    #accent { width: 0; height: 6px; background: #58C4DD; margin: 28px auto 0; }
  </style>
</head>
<body>
  <div id="root" data-composition-id="intro" data-start="0" data-width="1920" data-height="1080">
    <div class="clip center" data-start="0" data-duration="4" data-track-index="0">
      <div>
        <div id="lecture">LECTURE 20 · TOPIC 7</div>
        <div id="title">Information Gain</div>
        <div id="accent"></div>
      </div>
    </div>
    <audio class="clip" src="assets/intro_sting.wav"
           data-start="0" data-duration="4" data-track-index="1" data-volume="0.5"></audio>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({ paused: true });
    tl.from("#lecture", { opacity: 0, y: 20, duration: 0.6 }, 0.2)
      .from("#title",   { opacity: 0, y: 40, duration: 0.8 }, 0.5)
      .to("#accent",    { width: 360, duration: 0.7, ease: "power2.out" }, 1.1);
    window.__timelines = window.__timelines || {};
    window.__timelines.intro = tl;        // key = data-composition-id
  </script>
</body>
</html>
```

### Key attributes
| Attribute | Kahan | Matlab |
|---|---|---|
| `data-composition-id` | Root | Composition ka naam (GSAP timeline isi key par register hoti hai) |
| `data-start`, `data-width`, `data-height` | Root | Start time, frame size |
| `class="clip"` | Har timed element | Isse timeline par manage hota hai |
| `data-start`, `data-duration` | Clip | Kab aaye, kitni der rahe (seconds) |
| `data-track-index` | Clip | Layer/track (z-order aur organization) |
| `data-volume` | `<audio>` clip | Volume (0–1) |

### GSAP rule
Timeline **paused** banao aur `window.__timelines[<composition-id>]` par register karo. Renderer khud har frame ke time par timeline ko seek karta hai. Isi wajah se output deterministic hai (real-time playback par depend nahi karta).

> ⚠️ Upar diye attributes HyperFrames ke README/launch docs ke examples se hain. Framework naya hai aur tezi se badal raha hai. `npx hyperframes init` jo template banaye, use reference maano, aur docs ka current version dekho.

---

## 4. Hamare templates

| Template | Duration | Data |
|---|---|---|
| `intro` | 3–5 s | lecture no., topic no., title, series name |
| `chapter` | 1.5–2 s | scene title |
| `recap` | 8–15 s (narration ke saath) | 3 bullet points, har bullet narration beat par aaye |
| `quiz` | Question + options + countdown + answer reveal | question, options[], correct, countdown s |
| `outro` | 5–8 s | next topic, recap |

### Data-driven template
Template mein placeholders rakho, aur pipeline JSON se fill kare:
```js
// cards/templates/recap/data.js  (pipeline generate karti hai)
window.CARD = {
  title: "Aaj kya seekha",
  bullets: [
    { text: "Gain = pehle ka confusion − baad ka confusion", start: 0.4 },
    { text: "Outlook ka gain sabse zyada: 0.2467", start: 3.9 },
    { text: "ID3 highest-gain attribute ko root banata hai", start: 7.6 }
  ],
  audio: "../../out/L20/T07/audio/recap.wav",
  duration: 11.2
};
```
Bullet ka `start` = us bullet ke narration beat ka start time (`durations.json` se cumulative). Isse recap card bhi audio-first sync follow karta hai.

---

## 5. Pipeline integration

```python
import json, subprocess, pathlib

def render_card(template: str, data: dict, out_mp4: str, project="video/cards"):
    p = pathlib.Path(project)
    (p / "templates" / template / "data.js").write_text(
        "window.CARD = " + json.dumps(data, ensure_ascii=False) + ";", encoding="utf-8")
    subprocess.run(["npx", "hyperframes", "render"], cwd=p / "templates" / template, check=True)
    # render output path HyperFrames config/CLI flags par depend karta hai; usse out_mp4 par move karo
```
> Exact render flags (output path, fps, quality) ke liye `npx hyperframes render --help` dekho, aur unhe yahan document karo jab pilot mein setup ho.

### Format consistency (concat ke liye zaroori)
Cards ko bhi Manim scenes jaisa hi output dena chahiye: **1920×1080, 30 fps, yuv420p, same audio sample rate**. Agar HyperFrames ka output alag ho to assembly se pehle normalize karo ([27](27_FFmpeg_Final_Assembly.md)):
```bash
ffmpeg -i card.mp4 -vf "scale=1920:1080,fps=30,format=yuv420p" -c:v libx264 -crf 18 -c:a aac -ar 48000 card_norm.mp4
```

---

## 6. Kyun HeyGen ne HTML choose kiya (context)

HeyGen ke mutabik (blog coverage ke through), unhone pehle React-based Remotion try kiya tha, lekin agent ke liye guardrails badhaane par output "safe aur repetitive" ho gaya. Plain HTML par agents zyada creative output de paaye. Ye company ka claim hai, independent benchmark nahi. Hamare liye practical baat ye hai ki HTML/CSS Claude ke liye bahut familiar hai, isliye templates jaldi bante hain.

👉 Agla: [25_Remotion_Alternative.md](25_Remotion_Alternative.md)
