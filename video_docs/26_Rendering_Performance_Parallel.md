# 26 · Rendering: Performance, Parallel Rendering, Time Estimates

> **Is file mein:** Manim rendering kitna time leti hai aur kyun, parallel rendering kaise karein, caching, preview vs final strategy, aur hardware ka sahi use.

---

## 1. Seedhi baat

Manim (Cairo renderer) **CPU par** frames banata hai, ek-ek karke. Ek scene ek CPU core (zyadatar) use karta hai. Isliye:
- **Ek scene ko tez karna mushkil hai**
- **Bahut saare scenes ko parallel chalana aasaan hai.** 16-core CPU par ~8–12 scenes ek saath

**Strategy:** Har topic ko 8–12 scenes mein todo (ye pedagogy ke hisaab se already hota hai), aur scenes ko parallel render karo.

---

## 2. Render time kis par depend karta hai

| Factor | Asar |
|---|---|
| Resolution | 1080p ≈ 2.25× pixels of 720p; 1440p ≈ 1.8× of 1080p |
| FPS | 60 fps = 30 fps ka 2× kaam. **Hum 30 use karte hain** |
| Objects per frame | Zyada objects → slow (har frame mein sab redraw) |
| `Text`/`MathTex` creation | Pehli baar slow (LaTeX compile / Pango); cache ke baad fast |
| `ImageMobject` (badi images) | Moderate |
| Static frames (`wait`) | Manim static frames ko efficiently handle karta hai, jo animation frames se sasta padta hai |
| Complex updaters (`always_redraw`) | Slow; zaroorat ho tabhi use karo |

> ⚠️ Exact seconds-per-frame hardware aur scene par depend karte hain. Pilot mein apne PC par naapo aur yahan likho:
> | Scene type | Duration | Render time (1080p30) | Machine |
> |---|---|---|---|
> | (pilot ke baad fill karo) | | | |

---

## 3. Preview vs final

| Stage | Command | Kyun |
|---|---|---|
| Syntax/runtime check | `manim -ql -s scene.py S05` | Sirf last frame, sabse fast |
| Layout check | `manim -ql --format png-sequence ...` ya beat-end frames | Critic ke liye |
| Preview video | `manim -ql scene.py S05` (480p15) | Timing aur flow dekhne ke liye |
| Final | `manim -qh --fps 30 scene.py S05` | 1080p30 |

**Rule:** Final render sirf tab jab preview + critic pass ho jaaye. Final render sabse mehenga step hai.

> Preview 15 fps par hota hai, final 30 par. Animation timing seconds mein hai, isliye sync dono mein same rehta hai. Bas preview mein motion thoda jerky dikhega.

---

## 4. Parallel rendering

### Simple: GNU parallel / Python multiprocessing
```python
# video/lib/render.py
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

def render_one(scene_file: str, scene_class: str, quality="h", fps=30, media_dir="media"):
    cmd = ["manim", f"-q{quality}", "--fps", str(fps), "--media_dir", media_dir,
           scene_file, scene_class]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return scene_class, p.returncode, p.stdout[-2000:] + p.stderr[-4000:]

def render_all(jobs: list[tuple[str, str]], workers: int = 8, **kw):
    results = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(render_one, f, c, **kw): c for f, c in jobs}
        for fut in as_completed(futs):
            name, rc, log = fut.result()
            results[name] = (rc, log)
            print(("✅" if rc == 0 else "❌"), name)
    return results
```

### Kitne workers?
- Start: `workers = physical_cores - 2` (OS aur baaki kaam ke liye jagah)
- 🍎 **Mac:** P-cores ke hisaab se socho (`sysctl -n hw.perflevel0.physicalcpu`). Max (12P+4E, 64 GB): 8–10 workers; M1 8 GB: 2–3. Raat ke render `caffeinate -i ...` ke saath, charger laga kar ([40](40_Mac_Apple_Silicon_Setup.md) §3, §10)
- **RAM bhi check karo:** har Manim process kuch sau MB se 1–2 GB tak le sakta hai (images/complex scenes mein zyada). 32 GB RAM par ~10–12 workers safe hain
- Agar TTS/image models GPU par saath mein chal rahe hain to CPU workers thode kam karo

### Ek lambe scene ko todna (agar zaroorat ho)
Manim `-n start,end` se animation range render kar sakta hai, lekin voiceover state (tracker time) scene ke shuru se chalti hai, isliye ye tricky hai. **Behtar:** lambe scene ko script level par hi 2 scenes mein todo.

---

## 5. Caching

| Cache | Kahan | Kya bachata hai |
|---|---|---|
| Manim partial movies | `media/videos/<file>/<quality>/partial_movie_files/` | Code ka jo hissa nahi badla, wo animations dobara render nahi hote |
| LaTeX | `media/Tex/` | Same formula dobara compile nahi hota |
| Voiceover | `media/voiceovers/cache.json` | Same text ka audio dobara nahi banta |
| Pipeline stage hashes | `out/.../.hashes.json` ([05](05_Architecture_Pipeline_Folder_Structure.md)) | Poore stages skip |

**Tip:** Har topic ka alag `--media_dir` do (`out/L20/T07/media`), taaki caches mix na hon aur purane topics ka cache delete karna aasaan ho.

> Manim ka partial-movie cache har `play()` ke hash par based hai. Agar ek beat ka audio badla (duration badli), to us beat ke animations ka `run_time` badlega aur sirf wahi re-render honge.

---

## 6. GPU ka role

| Kaam | GPU? |
|---|---|
| Manim Cairo render | ❌ CPU |
| Manim OpenGL renderer | ✅ (lekin final ke liye Cairo recommended, [17](17_Manim_Basics_Install_Concepts.md)) |
| TTS | ✅ |
| Whisper/alignment | ✅ |
| Image generation | ✅ |
| Local LLM | ✅ |
| ffmpeg encode | Optional: NVENC (`h264_nvenc`) fast hai, lekin same bitrate par x264 ki quality better hoti hai. Final master ke liye `libx264 -crf 18` |

**Workload scheduling:** GPU kaam (TTS, images) pehle batch mein chalao, phir CPU-heavy rendering. Dono ek saath chalane se thermal/power limits aur RAM pressure badhta hai.

---

## 7. Disk space

- Manim partial movies + final renders: 1080p30 animation (CRF ~18–23) aam taur par **kuch MB per minute**, lekin partial movies + multiple versions se jaldi badhta hai
- Har topic ke baad `partial_movie_files` saaf kar sakte ho (final ban jaane ke baad)
- Final masters ka backup (external drive / cloud)

> 1 lecture (10 topics × ~10 min) ke liye intermediate files ke saath ~10–30 GB plan karo. Ye rough estimate hai, apne pilot se update karo.

---

## 8. Overnight batch run

```bash
# Saare topics ka TTS (GPU), phir saare renders (CPU), phir assembly
python build_video.py L20 --stage tts
python build_video.py L20 --stage render --workers 10
python build_video.py L20 --stage assemble
```
- Logs `out/L20/logs/` mein
- Failures ki list end mein; subah sirf failed scenes dekho
- Windows: sleep mode band karo (Power settings), warna raat mein render ruk jaayega

👉 Agla: [27_FFmpeg_Final_Assembly.md](27_FFmpeg_Final_Assembly.md)
