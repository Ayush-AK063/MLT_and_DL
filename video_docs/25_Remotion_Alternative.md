# 25 · Remotion: Alternative (Kab Use Karein)

> **Is file mein:** Remotion kya hai, HyperFrames/Manim se comparison, license (important!), kab Remotion better choice hai, aur basic setup.

---

## 1. Remotion kya hai

- **React components se video** banane ka framework. Har frame ek React render hai (`useCurrentFrame()`)
- Mature ecosystem: captions (`@remotion/captions`), Whisper integration (`@remotion/install-whisper-cpp`, `@remotion/openai-whisper`), Lambda rendering, Player component
- Tum pehle se jaante ho, jo ek bada plus hai

```tsx
import { AbsoluteFill, useCurrentFrame, interpolate, Audio, Sequence, staticFile } from "remotion";

export const Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ background: "#0F1117", justifyContent: "center", alignItems: "center" }}>
      <h1 style={{ color: "#E8E6E3", fontSize: 96, opacity }}>Information Gain</h1>
      <Sequence from={0}>
        <Audio src={staticFile("intro_sting.wav")} volume={0.5} />
      </Sequence>
    </AbsoluteFill>
  );
};
```

---

## 2. ⚠️ License (sabse important point)

Remotion **source-available** hai, standard open-source license nahi:

| Kaun | Free? |
|---|---|
| Individuals | ✅ |
| For-profit company, **≤ 3 employees** | ✅ |
| Non-profits / not-for-profit | ✅ |
| Evaluation (abhi commercial use nahi) | ✅ |
| For-profit company with **4+ employees** | ❌ Company License chahiye |

(Ye eligibility list GitHub ke `LICENSE.md` se verify ki gayi. Usme ye bhi likha hai ki Remotion 5.0 mein license "slightly change" hoga.)

Official pricing page (2026-10-18 ko check kiya):
- **Remotion for Creators:** $25/month per seat (low-volume, coding/prompting se video creation)
- **Remotion for Automators:** $0.01 per render, $100/month minimum (video creation tools banane ke liye)
- **Enterprise:** $500/month se shuru

> Agar ye project kisi company (jaise simxr) ke under 4+ logon ke saath ho raha hai, to Remotion ke liye paid license lagega. HyperFrames (Apache-2.0) aur Manim (MIT) free hain. Latest terms ke liye remotion.dev/license dekho ([38](38_Licenses_Legal_Ethics.md)).

---

## 3. Comparison

| | Manim | HyperFrames | Remotion |
|---|---|---|---|
| Language | Python | HTML/CSS/JS (GSAP) | React/TypeScript |
| Best for | Maths animation | Templates, motion graphics | Templates, data-driven video apps, interactive players |
| LaTeX | ✅ Native | Via MathJax/KaTeX (web) | Via KaTeX/MathJax components |
| Deterministic | ✅ | ✅ (frame seek) | ✅ (frame-based render) |
| License | MIT | Apache-2.0 | Source-available (4+ employees paid) |
| Agent-friendliness | Achha (Python) | Explicitly agent ke liye designed | Achha; official AI skills/prompts bhi hain |
| Ecosystem | Maths community | Naya (2026) | Mature |
| Audio captions | manim-voiceover subcaptions | Skills | `@remotion/captions` + Whisper |

---

## 4. Kab Remotion choose karein

✅ Remotion lo agar:
- Team ≤ 3 log hai (ya license budget hai)
- Tumhe **web player** chahiye jisme video interactive ho (jaise site par embedded lecture jisme chapter navigation ho)
- Pehle se Remotion components/experience hai
- Captions ke liye TikTok-style word highlighting chahiye (built-in helpers)

❌ HyperFrames/ffmpeg lo agar:
- 4+ employee company aur license budget nahi
- Sirf simple cards + concat chahiye

**Hamara default:** Manim (content) + HyperFrames (cards) + ffmpeg (assembly). Remotion tab, jab interactive web player ya existing Remotion code ka fayda ho.

---

## 5. Agar Remotion use karo: key setup notes

```bash
npx create-video@latest
npx remotion studio                    # preview
npx remotion render <CompositionId> out/video.mp4 --codec=h264 --crf=18
```
- Default codec H.264 hai (agar `--codec` na do)
- `--crf` aur `--video-bitrate` ek saath set nahi hote
- Long videos ke liye `--concurrency` se parallel rendering (CPU cores ke hisaab se), aur Lambda se distributed rendering
- Manim ki rendered clips ko `<OffthreadVideo src={staticFile("s05.mp4")} />` se compose kar sakte ho
- Audio-first sync: composition ka `durationInFrames` = `Math.round(totalSeconds * fps)` (cumulative seconds se, [02](02_Sync_Ka_Science_Audio_First_Timeline.md))

### Remotion + Whisper captions
- `@remotion/install-whisper-cpp` → local whisper.cpp → `convertToCaptions()` (token-level timestamps ke liye newer whisper.cpp build chahiye, jo docs ke hisaab se kam stable hai)
- `@remotion/captions` ka `createTikTokStyleCaptions()` words ko "pages" mein group karta hai

👉 Agla: [26_Rendering_Performance_Parallel.md](26_Rendering_Performance_Parallel.md)
