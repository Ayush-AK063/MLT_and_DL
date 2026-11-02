# 17 · Manim Basics: Install, Core Concepts, Rendering

> **Is file mein:** Manim Community Edition (ManimCE) zero se: kya hai, install (Windows/Linux/Mac), core concepts (Scene, Mobject, Animation, coordinate system), LaTeX, render commands, aur hamare liye zaroori tips. Last section mein ek complete mini example hai.

---

## 1. Manim kya hai?

- Python library jisme **code likh kar maths animations** banti hain
- Grant Sanderson (3Blue1Brown) ne banayi thi; **Manim Community Edition (ManimCE)** uska community-maintained version hai, aur **hum yahi use karenge**
- Latest (2026-10-18): **v0.22.0** (PyPI release: 8 Oct 2026), **Python ≥ 3.11**
- License: MIT

> ⚠️ **Do Manims hain.** `manimgl` (3b1b ka original, OpenGL-based) aur `manim` (Community). Docs, plugins (manim-voiceover) aur tutorials alag hain. Internet par code copy karte waqt check karo ki wo `from manim import *` (Community) hai, `from manimlib import *` (3b1b) nahi.

---

## 2. Install

Official docs **uv** recommend karte hain.

### Step 1: uv install
```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Step 2: System dependencies
| OS | Command |
|---|---|
| **Windows** | Kuch extra nahi. Agar "Microsoft Visual C++ required" error aaye to Microsoft C++ Build Tools ("Desktop development with C++") install karo |
| **macOS** | `brew install cairo pkg-config` |
| **Ubuntu/Debian** | `sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev` |
| **Fedora** | `sudo dnf install python3-devel pkg-config cairo-devel pango-devel` |
| **Arch** | `sudo pacman -Syu base-devel cairo pango` |

### Step 3: Project + Manim
```bash
uv init mlt-video --python 3.12
cd mlt-video
uv add manim
uv run manim checkhealth
```
> `checkhealth` dependencies check karne ke baad ek test scene render karne ke liye **y/n poochta hai** (interactive). Script/CI mein chalao to ye input ka wait karega.

### Step 4: LaTeX (formulas ke liye zaroori)
| OS | Distribution |
|---|---|
| Windows | **MiKTeX** (miktex.org) |
| macOS | **MacTeX** |
| Linux | TeX Live (`sudo apt install texlive-full`, ya chhota set) |
| Minimal | TinyTeX + required packages (amsmath, dvisvgm, standalone, ...) |

> **ffmpeg alag se install karna zaroori nahi.** Manim v0.19.0 (Jan 2025) se ffmpeg ki jagah **PyAV** library use hoti hai, jiske wheels mein ffmpeg bundled hai. Lekin hamari pipeline ke assembly step ke liye ffmpeg CLI phir bhi chahiye ([27](27_FFmpeg_Final_Assembly.md)).

### manim-voiceover bhi
```bash
uv add manim-voiceover      # v0.4.0, Python >= 3.11
```
> manim-voiceover `sox` Python package pe depend karta hai. SoX binary na ho to import par warning aati hai ("SoX could not be found!"). SoX sirf `global_speed != 1` par chahiye. Hum speed change use nahi karte, isliye warning ignore kar sakte ho, ya SoX install kar lo.

---

## 3. Core concepts

### 3.1 Scene
Ek video clip. `construct()` method mein animations likhte ho.
```python
from manim import *

class Hello(Scene):
    def construct(self):
        t = Text("Namaste MLT!")
        self.play(Write(t))
        self.wait(1)
```

### 3.2 Mobject (Mathematical Object)
Screen par dikhne wali har cheez:
| Mobject | Kya |
|---|---|
| `Text("...")` | Normal text (Pango se, LaTeX nahi) |
| `MathTex(r"H(S) = 0.940")` | LaTeX math |
| `Tex(r"Entropy $H$")` | LaTeX text mode |
| `Circle()`, `Square()`, `Rectangle()`, `Line()`, `Arrow()`, `Dot()` | Shapes |
| `Table(...)`, `MathTable(...)` | Tables |
| `Axes(...)`, `NumberPlane()` | Graphs |
| `BarChart(...)` | Bar chart |
| `VGroup(a, b, c)` | Group (saath mein move/arrange) |
| `SurroundingRectangle(m)` | Kisi cheez ke around box |
| `Brace(m, DOWN)` | Curly brace |

### 3.3 Animation
| Animation | Effect |
|---|---|
| `Write(m)` | Text/formula "likha" jaata hai |
| `Create(m)` | Shape draw hoti hai |
| `FadeIn(m)`, `FadeOut(m)` | Fade |
| `Transform(a, b)` | a ko b mein morph |
| `ReplacementTransform(a, b)` | Transform jisme a scene se hat jaata hai, b aa jaata hai |
| `TransformMatchingTex(a, b)` | Formula ke matching parts smoothly move karte hain ⭐ |
| `Indicate(m)` | Thoda bada + color flash (highlight) |
| `Circumscribe(m)` | Around line draw |
| `m.animate.shift(RIGHT)` | Kisi bhi property change ko animate karo |
| `LaggedStart(*anims, lag_ratio=0.2)` | Ek ke baad ek, overlap ke saath |
| `AnimationGroup(...)` | Saath mein |

```python
self.play(Write(eq), run_time=2)        # run_time = seconds
self.play(eq.animate.set_color(YELLOW))
self.wait(0.5)
```

### 3.4 Coordinate system
- Default frame: **width ≈ 14.22 units, height = 8 units** (16:9), center `ORIGIN = (0,0,0)`
- Directions: `UP`, `DOWN`, `LEFT`, `RIGHT`, `UL`, `UR`, `DL`, `DR`
- Positioning:
```python
m.to_edge(UP)                 # top edge par
m.to_corner(UL)
m.next_to(other, DOWN, buff=0.3)
m.move_to(ORIGIN)
m.shift(2 * RIGHT)
VGroup(a, b, c).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
```

### 3.5 Colors
Built-ins: `WHITE, GRAY, YELLOW, GREEN, BLUE, RED, ORANGE, PURPLE, TEAL, GOLD, ...` ya hex `"#58C4DD"`. Hamari palette: [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md).

---

## 4. LaTeX tips (MathTex)

```python
eq = MathTex(r"\text{Gain}(S, A)", "=", r"H(S)", "-", r"\sum_{v} \frac{|S_v|}{|S|} H(S_v)")
eq[2].set_color(BLUE)          # H(S) part
eq[4].set_color(ORANGE)        # summation part
```
- **Alag strings = alag parts** (index se color/highlight kar sakte ho)
- `substrings_to_isolate=["H(S)"]` se automatic split
- Raw strings (`r"..."`) use karo, warna `\f`, `\t` jaise escapes toot jaate hain
- Hindi text LaTeX mein mushkil hai, isliye Hindi/Hinglish labels ke liye `Text()` use karo (font support ke saath, [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md))

### `TransformMatchingTex` (formula step-by-step) ⭐
```python
a = MathTex("H(S)", "=", r"-\frac{9}{14}\log_2\frac{9}{14}", "-", r"\frac{5}{14}\log_2\frac{5}{14}")
b = MathTex("H(S)", "=", "0.410", "+", "0.531")
c = MathTex("H(S)", "=", "0.940")
self.play(Write(a))
self.play(TransformMatchingTex(a, b))
self.play(TransformMatchingTex(b, c))
```
Jo parts same hain (`H(S)`, `=`), wo apni jagah rehte hain; baaki morph hote hain. Viewer ko dikhta hai ki ek step se dusra kaise aaya.

> Numbers yahan bhi verify block se aane chahiye: 0.4098 → "0.410", 0.5305 → "0.531" (3 decimals), aur 0.410 + 0.531 = 0.941, lekin exact sum 0.940 hai. Isliye intermediate ko "≈" ke saath dikhao, ya 4 decimals use karo ([08](08_Math_Verification_Step.md) section 6).

---

## 5. Render commands

```bash
manim -pql scene.py Hello              # preview, 480p15 (fast), render ke baad khulega
manim -qm scene.py Hello               # 720p30
manim -qh --fps 30 scene.py Hello      # 1080p30 ✅ (hamara final)
manim -qp --fps 30 scene.py Hello      # 1440p30
manim -s -ql scene.py Hello            # sirf last frame PNG (layout check)
manim -a -qh --fps 30 scene.py         # file ke saare scenes
manim -qh --fps 30 -n 3,7 scene.py Hello   # sirf animations 3 se 7 (debug)
```

| Flag | Matlab |
|---|---|
| `-ql/-qm/-qh/-qp/-qk` | 480p15 / 720p30 / 1080p60 / 1440p60 / 2160p60 |
| `--fps 30` | FPS override (`-qh` default 60 hai) |
| `-r W,H` | Custom resolution |
| `-p` | Render ke baad open |
| `-s` | Last frame PNG |
| `-a` | Saare scenes |
| `-n a,b` | Animation range |
| `--format png-sequence` | Har frame PNG (critic ke liye useful) |
| `--disable_caching` | Cache use mat karo |
| `--media_dir PATH` | Output folder |
| `--renderer cairo\|opengl` | Renderer |

### `manim.cfg` (project defaults)
Scene file ke folder mein `manim.cfg`:
```ini
[CLI]
frame_rate = 30
pixel_width = 1920
pixel_height = 1080
background_color = #0F1117
media_dir = ./media
```
CLI flags hamesha config file ko override karte hain.

---

## 6. Output kahan jaata hai

```
media/
├── videos/scene/1080p30/Hello.mp4          ← final
├── videos/scene/1080p30/partial_movie_files/  ← har play() ka chhota clip (cache)
├── images/                                 ← -s ka PNG
├── Tex/                                    ← compiled LaTeX
└── voiceovers/                             ← manim-voiceover audio + cache.json
```

---

## 7. Renderer: Cairo vs OpenGL

| | Cairo (default) | OpenGL |
|---|---|---|
| Stability | ✅ Mature | Kam mature (kuch features alag behave karte hain) |
| Speed | CPU-bound, slow | GPU, faster preview |
| Plugins compatibility | ✅ | Kuch issues |
| **Hamara choice** | ✅ Final renders | Sirf interactive experimentation |

---

## 8. Hamare liye zaroori tips

1. **Har scene alag file ya alag class**, taaki parallel render ho sake ([26](26_Rendering_Performance_Parallel.md))
2. **`self.wait()` ki jagah voiceover ke saath sync** ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md))
3. **Text size:** body text `font_size=36–40`, labels 28–32, equations default (48) ya 40. 1080p par 24 se chhota mat karo
4. **Safe area:** Frame ke edges se ~0.5 unit andar raho (YouTube player controls aur mobile cropping)
5. **Ek waqt par kam objects:** Purane objects `FadeOut` karo
6. **Random cheezein (agar use karo) ke liye seed fix karo**, taaki render deterministic rahe
7. **Fonts:** Hindi/Devanagari ke liye `Text("...", font="Noto Sans Devanagari")`, aur font system par installed hona chahiye

---

## 9. Mini example: entropy calculation (complete, testable)

```python
from manim import *

class EntropyCalc(Scene):
    def construct(self):
        title = Text("Entropy of S", font_size=40).to_edge(UP)
        counts = MathTex(r"9\ \text{Yes},\ 5\ \text{No}", font_size=40).next_to(title, DOWN, buff=0.5)

        step1 = MathTex(r"H(S)", "=", r"-\tfrac{9}{14}\log_2\tfrac{9}{14}", "-", r"\tfrac{5}{14}\log_2\tfrac{5}{14}")
        step2 = MathTex(r"H(S)", "=", r"0.4098", "+", r"0.5305")
        step3 = MathTex(r"H(S)", "=", r"0.940")
        for s in (step1, step2, step3):
            s.move_to(ORIGIN)

        self.play(Write(title))
        self.play(FadeIn(counts, shift=DOWN * 0.2))
        self.play(Write(step1), run_time=2)
        self.wait(0.5)
        self.play(TransformMatchingTex(step1, step2))
        self.wait(0.5)
        self.play(TransformMatchingTex(step2, step3))
        box = SurroundingRectangle(step3[2], color=YELLOW, buff=0.15)
        self.play(Create(box))
        self.wait(1)
```
```bash
manim -pql entropy.py EntropyCalc
```
(Numbers: 0.4098 + 0.5305 = 0.9403 ≈ 0.940 ✅)

👉 Agla: [18_Manim_Voiceover_Sync_Custom_Local_TTS.md](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)
