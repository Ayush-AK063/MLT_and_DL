# 20 · Visual Style Guide: Colors, Fonts, Layout

> **Is file mein:** Poore channel ka visual identity: color palette (meaning ke saath), fonts (English + Devanagari), text sizes, layout grid, named layouts, safe areas, aur motion rules. Har video isi guide ko follow karega taaki sab ek series jaisa lage.

---

## 1. Kyun style guide?

- **Consistency = trust.** 22 lectures ke videos ek "series" lagne chahiye, 22 alag projects nahi
- **Colors ka meaning ho** (visual invariants, 3Blue1Brown principle): "Yes" hamesha green, "No" hamesha red. Viewer ka dimaag ye mapping seekh leta hai aur samajhne mein kam effort lagta hai
- AI coder ko decisions kam lene padte hain, isliye galtiyan bhi kam hoti hain

---

## 2. Color palette

Dark background (aankhon ke liye aaram, equations pop karti hain, 3b1b-style).

| Token | Hex | Meaning / use |
|---|---|---|
| `BG` | `#0F1117` | Background |
| `FG` | `#E8E6E3` | Normal text, equations |
| `MUTED` | `#8B8F98` | Labels, axes, secondary info, headers |
| `ACCENT` | `#58C4DD` | Primary concept color (nodes, bars, main object) |
| `YES` | `#83C167` | Positive class / correct / "Yes" |
| `NO` | `#FC6255` | Negative class / wrong / "No" |
| `HILITE` | `#FFD84D` | **Current focus**: jo abhi bola ja raha hai |
| `WARN` | `#F5A623` | Common mistake, caution |
| `PURPLE` | `#9A72AC` | Doosra concept (jab do concepts compare ho) |

### Semantic rules
1. **HILITE (yellow) sirf "abhi" ke liye.** Jo cheez narration mein abhi aa rahi hai wahi yellow ho. Agle beat mein wapas normal color
2. **Ek concept = ek color, poore video (aur series) mein.** Entropy = ACCENT, Gain = PURPLE (agar dono saath hain)
3. **Max 3–4 colors ek screen par** (BG/FG chhod kar)
4. **Red/green ke saath shape/label bhi do** (colorblind viewers ke liye): "Yes ✓" / "No ✗", ya + / − symbols

> Ye hex values Manim ke default colors (BLUE_C, GREEN_C, RED_C) ke aas-paas hain, jo 3b1b-style videos mein familiar lagte hain. **Contrast check (WCAG formula se calculate kiya, `BG` ke against):** FG 15.2:1, HILITE 13.6:1, ACCENT 9.3:1, WARN 9.3:1, YES 8.8:1, NO 6.3:1, MUTED 5.8:1, PURPLE 4.8:1. Sab WCAG AA (4.5:1) pass karte hain. PURPLE aur MUTED sabse kam hain, isliye inhe chhote ya important text ke liye mat use karo.

---

## 3. Fonts

| Use | Font | Kyun | License |
|---|---|---|---|
| English text / labels | **Inter** | Screen ke liye bana, numbers clear (0/O, 1/l alag) | SIL OFL (free) |
| Devanagari | **Noto Sans Devanagari** | Google ka Noto, achha Unicode coverage | SIL OFL |
| Code | **JetBrains Mono** | Monospace, ligatures optional | SIL OFL |
| Maths | LaTeX default (Computer Modern) | Standard, familiar | – |

### Install (render machine par)
- Windows: font files (.ttf) par right-click → "Install for all users"
- Linux: `~/.local/share/fonts/` mein copy karo, phir `fc-cache -f`
- macOS: Font Book

> Manim `Text()` Pango use karta hai, aur Pango system fonts dhundhta hai. Font installed nahi hai to fallback font lagta hai (aur layout badal sakta hai). Isliye **render machine par fonts install karna setup ka hissa hai** ([29](29_Hardware_Environment_Setup_Windows_NVIDIA.md)).

---

## 4. Text sizes (Manim `font_size`, 1080p ke liye)

| Role | Size | Example |
|---|---|---|
| Scene title | 44 | "Outlook ka Information Gain" |
| Body / main label | 34–38 | "Sunny: 2+ / 3−" |
| Secondary label | 28 | Axis labels, table cells |
| Small (min) | 24 | Footnotes, sources |
| Equations | MathTex default (48) ya 40–44 | |

**Rule:** 24 se chhota kabhi nahi. Phone par (bahut log phone par dekhte hain) chhota text padha nahi jaata.

**Words per screen:** Ek text element max ~6–8 words. Lamba explanation narration mein jaata hai (redundancy principle).

---

## 5. Frame aur safe area

Manim frame: **14.22 × 8 units** (16:9), center (0, 0).

```
┌──────────────────────────────────────────────┐  y = +4.0
│  ┌────────────────────────────────────────┐  │  y = +3.6  ← safe area top
│  │                                        │  │
│  │                                        │  │
│  │          CONTENT SAFE AREA             │  │
│  │          |x| ≤ 6.6, |y| ≤ 3.6          │  │
│  │                                        │  │
│  │                                        │  │
│  └────────────────────────────────────────┘  │  y = −3.6
│        (captions zone: y < −3.0 avoid)       │
└──────────────────────────────────────────────┘  y = −4.0
x = −7.11                                       x = +7.11
```

- **Content:** |x| ≤ 6.6, |y| ≤ 3.6
- **Bottom ~1 unit:** YouTube captions aur player controls yahan aate hain, isliye important content y > −3.0 par rakho
- **Top-right corner:** YouTube kabhi-kabhi info cards dikhata hai, isliye wahan important cheez mat rakho

---

## 6. Named layouts (script.json mein `layout` field)

```
1. "center_focus"            2. "title_and_body"           3. "table_left_math_right"
┌──────────────────┐        ┌──────────────────┐         ┌─────────┬────────┐
│                  │        │ TITLE            │         │         │ eq 1   │
│     [OBJECT]     │        │──────────────────│         │  TABLE  │ eq 2   │
│                  │        │   body / visual  │         │         │ result │
└──────────────────┘        └──────────────────┘         └─────────┴────────┘

4. "two_compare"             5. "diagram_with_caption"     6. "formula_breakdown"
┌────────┬─────────┐        ┌──────────────────┐         ┌──────────────────┐
│   A    │    B    │        │     DIAGRAM      │         │  FULL FORMULA    │
│        │         │        │                  │         │  ↓ term 1: ...   │
│ label  │  label  │        │ caption (1 line) │         │  ↓ term 2: ...   │
└────────┴─────────┘        └──────────────────┘         └──────────────────┘
```

### Layout regions (code)
```python
# video/lib/components/layout.py
from manim import *

REGIONS = {
    "title":       dict(center=UP * 3.1,             width=12.5, height=0.9),
    "body":        dict(center=DOWN * 0.3,            width=12.5, height=5.6),
    "left_half":   dict(center=LEFT * 3.35 + DOWN * 0.3, width=6.2, height=5.6),
    "right_half":  dict(center=RIGHT * 3.35 + DOWN * 0.3, width=6.2, height=5.6),
    "left_wide":   dict(center=LEFT * 2.4 + DOWN * 0.3,  width=8.0, height=5.6),
    "right_narrow": dict(center=RIGHT * 4.6 + DOWN * 0.3, width=4.0, height=5.6),
    "caption":     dict(center=DOWN * 2.8,            width=12.0, height=0.7),
}

def place(m: Mobject, region: str, scale_down_only: bool = True) -> Mobject:
    """Mobject ko region mein fit karo (sirf chhota karo, bada nahi) aur center karo."""
    r = REGIONS[region]
    if m.width > r["width"] or not scale_down_only:
        m.scale_to_fit_width(r["width"])
    if m.height > r["height"]:
        m.scale_to_fit_height(r["height"])
    return m.move_to(r["center"])
```
AI coder ko rule: **har top-level object `place(m, region)` se position ho.** Isse objects ek dusre par overlap nahi karte aur frame ke bahar nahi jaate. Code2Video ka "visual anchor" idea bhi yahi hai: free-form coordinates ki jagah fixed anchor positions.

---

## 7. Motion rules

| Rule | Value |
|---|---|
| Normal animation duration | 0.6–1.5 s |
| Text `Write` | ~0.05 s per character, max ~2 s |
| Formula transform | 1–1.5 s |
| Scene transition | Fade 0.4–0.6 s (koi fancy wipe/spin nahi) |
| Highlight (`Indicate`) | 0.6–0.8 s |
| Easing | Manim default (`smooth`) theek hai |
| Camera movement | Kam se kam; agar zoom chahiye to `MovingCameraScene`, slow (1.5–2 s) |

**Avoid:** Spinning text, bouncing, har cheez par zoom, flashy transitions. Ye attention ko content se hata dete hain (coherence principle).

---

## 8. Visual vocabulary (recurring symbols)

| Concept | Visual |
|---|---|
| Dataset | Table ya dots ka cloud |
| Class labels | Green ✓ / Red ✗ dots |
| Split | Ek box ka do/teen boxes mein toot'na |
| "Confusion"/entropy | Mixed balls ka dabba (`BallBox`) |
| Calculation step | Formula ka morph (`TransformMatchingTex`) |
| Result | Yellow box (`ResultBox`) |
| Best choice | Crown/yellow fill (`BarCompare.crown`) |
| Common mistake | Orange warning triangle + strikethrough |
| Pause-and-try | Yellow ring countdown (`PauseTimer`) |

---

## 9. Intro / outro cards

- **Intro (3–5 s):** Lecture number + topic title + series name. Same template har video mein (HyperFrames, [24](24_HyperFrames_Intro_Recap_Quiz.md))
- **Chapter cards (1.5–2 s):** Scene title, jab bada section shuru ho
- **Outro (5–8 s):** "Agle video mein: ...", recap points

---

## 10. Thumbnail style (YouTube)

- 1280×720 ([32](32_Publishing_YouTube.md))
- Bada text (3–5 words), high contrast, ek central visual (jaise tree ya formula ka hissa)
- Same template poori series mein, lecture number corner mein

👉 Agla: [21_AI_Se_Manim_Code_Generation.md](21_AI_Se_Manim_Code_Generation.md)
