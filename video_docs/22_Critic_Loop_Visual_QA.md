# 22 · Critic Loop: Visual QA

> **Is file mein:** Rendered video mein layout/visual galtiyan automatically kaise pakdein. Teen layers hain: (1) geometric audit (code se bounding boxes check), (2) vision model critic (frames dekh kar), (3) human spot-check. Saath mein fix loop aur checklist.

---

## 1. Kyun?

Code chal gaya iska matlab ye nahi ki video sahi dikhta hai. Humne component library test karte waqt khud dekha ([19](19_Manim_Component_Library_Design.md) §13): code bina error ke chala, lekin table headers overlap ho rahe the aur ek label frame ke bahar ja raha tha.

Research bhi yahi kehti hai:
- **TheoremExplainAgent:** zyadatar videos mein "minor issues with visual element layout" the
- **Code2Video:** Critic agent (visual anchor prompts + multimodal feedback) se element-layout score 0.59 → 0.91 hua

---

> 💰 **Budget mode:** Layer 1 (geometric audit, free) + Layer 3 (tum khud preview 2× par dekho) kaafi hai, khaas kar template engine ke saath, kyunki components already tested hain. Layer 2 (vision critic) paid API mein images bhejta hai, isliye budget mode mein skip karo. Agar kabhi chahiye to Claude subscription (Claude Code) mein kuch frames dikha kar pucho, ya local VLM try karo.

## 2. Teen layers

| Layer | Kya pakadta hai | Cost | Kab |
|---|---|---|---|
| **1. Geometric audit** | Overlap, frame/safe-area ke bahar, chhota font | Free, deterministic | Har preview render |
| **2. Vision critic** | Clutter, readability, galat highlight, visual-narration mismatch, aesthetics | LLM tokens | Har scene ka preview |
| **3. Human** | Pedagogy, tone, "feel" | Tumhara time | Har topic ka final preview (2× speed) |

---

## 3. Layer 1: Geometric audit (code se)

Idea: Manim ko pata hai har object kahan hai. Har `play()` ke baad saare text objects ke **bounding boxes** check karo.

```python
# video/lib/layout_audit.py
from itertools import combinations
from manim import *

FRAME_X, FRAME_Y = 7.11, 4.0
SAFE_X, SAFE_Y = 6.6, 3.6
TEXT_TYPES = (Text, MarkupText, MathTex, Tex)


def _label(m):
    return getattr(m, "text", None) or getattr(m, "tex_string", None) or type(m).__name__


def _bbox(m):
    return m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1]


def _overlap_ratio(a, b):
    ax0, ax1, ay0, ay1 = _bbox(a)
    bx0, bx1, by0, by1 = _bbox(b)
    w = min(ax1, bx1) - max(ax0, bx0)
    h = min(ay1, by1) - max(ay0, by0)
    if w <= 0 or h <= 0:
        return 0.0
    smaller = min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0)) or 1e-9
    return (w * h) / smaller


class LayoutAuditMixin:
    """Scene ke saath mix karo: class S(LayoutAuditMixin, LessonScene). Har play() ke baad audit."""
    audit_overlap_threshold = 0.15
    audit_issues: list

    def play(self, *args, **kwargs):
        super().play(*args, **kwargs)
        self._audit()

    def _texts(self):
        seen, out = set(), []
        for top in self.mobjects:
            for m in top.get_family():
                if isinstance(m, TEXT_TYPES) and id(m) not in seen and m.get_fill_opacity() > 0.05:
                    seen.add(id(m))
                    out.append(m)
        return out

    def _audit(self):
        if not hasattr(self, "audit_issues"):
            self.audit_issues = []
        t = round(float(self.renderer.time), 2)
        texts = self._texts()
        for m in texts:
            x0, x1, y0, y1 = _bbox(m)
            if x0 < -FRAME_X or x1 > FRAME_X or y0 < -FRAME_Y or y1 > FRAME_Y:
                self.audit_issues.append((t, "OUT_OF_FRAME", _label(m)))
            elif x0 < -SAFE_X or x1 > SAFE_X or y0 < -SAFE_Y or y1 > SAFE_Y:
                self.audit_issues.append((t, "OUTSIDE_SAFE_AREA", _label(m)))
        for a, b in combinations(texts, 2):
            if _overlap_ratio(a, b) > self.audit_overlap_threshold:
                self.audit_issues.append((t, "TEXT_OVERLAP", f"{_label(a)!r} x {_label(b)!r}"))

    def tear_down(self):
        super().tear_down()
        issues = sorted(set(getattr(self, "audit_issues", [])))
        if issues:
            print(f"\n[LAYOUT AUDIT] {type(self).__name__}: {len(issues)} issue(s)")
            for t, kind, what in issues:
                print(f"  t={t:>6}s  {kind:<18} {what}")
```

**Use:**
```python
class S05WorkedExample(LayoutAuditMixin, LessonScene):
    ...
```
Render ke end mein report print hoti hai. Pipeline ise parse karke `preview/s05_audit.json` mein save karti hai, aur issues ko Claude fix-loop mein bhejti hai.

**Asli test (manim 0.22.0, 2026-10-18):** Ek test scene banaya jisme jaan-boojh kar ek label frame ke edge par rakha aur do labels ek doosre par. Audit output:
```
[LAYOUT AUDIT] AuditTest: 6 issue(s)
  t=   3.0s  OUTSIDE_SAFE_AREA  Sunny:2+/3−
  t=   3.0s  TEXT_OVERLAP       'High' x 'OverlapA'
  t=   3.0s  TEXT_OVERLAP       'OverlapA' x 'OverlapB'
  t=   3.0s  TEXT_OVERLAP       'Strong' x 'OverlapA'
  t=   3.0s  TEXT_OVERLAP       'Strong' x 'OverlapB'
  t=   4.0s  OUTSIDE_SAFE_AREA  Sunny:2+/3−
```
Usne planted problems pakde, aur ek bonus problem bhi: test labels table ki last rows ("High", "Strong") se bhi takra rahe the, jo humne plan nahi kiya tha. (Note: Manim ka `Text.text` attribute spaces hata deta hai, isliye report mein "Sunny:2+/3−" dikhta hai.)

> Limitations: Ye sirf text objects ke **rectangular bounding boxes** check karta hai (shapes aur lines nahi). Diagonal text, ya intentionally overlapping cheezein (jaise text ke upar highlight box) false positive de sakti hain. Isliye threshold tune karo aur intentional overlaps ko allow-list karo.

---

## 4. Layer 2: Vision critic

### Frames nikalna
Har beat ke **end se thoda pehle** ka frame (jab us beat ke saare elements screen par hain):

```python
import json, subprocess

def beat_end_times(durations: dict, beat_ids: list[str], gaps: dict, default_gap=0.25):
    t, out = 0.0, {}
    for b in beat_ids:
        t += durations[b]
        out[b] = max(0.0, t - 0.15)          # beat end se 150 ms pehle
        t += gaps.get(b, default_gap)
    return out

def extract_frames(video: str, times: dict, out_dir: str):
    for beat, ts in times.items():
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", video,
                        "-frames:v", "1", f"{out_dir}/{beat}.png"], check=True)
```

> Preview `-ql` (480p) par render hota hai, jo critic ke liye kaafi hai aur fast bhi. Text readability ke final check ke liye kuch frames 1080p se bhi lo.

### Critic prompt (`video/prompts/critic_prompt.md`)
```markdown
Tum ek strict educational-video visual QA reviewer ho.
Har image ek beat ke end ka frame hai. Har frame ke saath us beat ki narration aur expected visual diya hai.

Har frame ke liye check karo:
1. OVERLAP: koi text/shape doosre par chadh raha hai?
2. CUTOFF: koi cheez frame edge par kat rahi hai?
3. READABILITY: koi text bahut chhota/low-contrast hai?
4. CLUTTER: screen par 4+ unrelated groups? Purani cheezein jo hat jaani chahiye thi?
5. MATCH: frame "expected visual" se match karta hai? Jo narration bol raha hai wo highlighted hai?
6. NUMBERS: screen par jo numbers hain, wo expected list se match karte hain? {{EXPECTED_NUMBERS}}
7. AESTHETICS: alignment, spacing, balance theek hai?

Output JSON:
{"frames":[{"beat":"b041","severity":"none|minor|major","issues":[{"type":"OVERLAP","detail":"...","fix_hint":"..."}]}]}
Sirf real problems report karo. Har chhoti cheez par "minor" mat do.
```

### Severity rules
| Severity | Action |
|---|---|
| `major` (overlap, cutoff, galat number, mismatch) | Auto fix-loop (Coder ko issues + frame description) |
| `minor` (spacing, aesthetics) | Batch mein fix, ya ignore |
| `none` | Pass |

---

## 5. Fix loop (critic → coder)

```python
def critic_loop(scene_id, max_rounds=2):
    for r in range(max_rounds + 1):
        video = render_preview(scene_id)                       # -ql
        audit = parse_layout_audit(scene_id)                   # layer 1
        frames = extract_frames_for(scene_id, video)
        report = claude_critic(frames, scene_spec(scene_id))  # layer 2
        majors = audit + [i for f in report["frames"] if f["severity"] == "major" for i in f["issues"]]
        if not majors:
            return "PASS"
        if r == max_rounds:
            return ("NEEDS_HUMAN", majors)
        fix_code_with_claude(scene_id, majors)
```

---

## 6. Automated checks jo video file par chalte hain

| Check | Tool | Fail condition |
|---|---|---|
| Duration match | `ffprobe` | Scene video duration vs Σ(beat durations + gaps) mein > 0.2 s farak |
| Audio present | `ffprobe -show_streams` | Audio stream missing |
| Black/frozen frames | `ffmpeg -vf blackdetect` / `freezedetect` | Unexpected long freeze (> 15 s, pause-and-try ko chhod kar) |
| Silence | `ffmpeg -af silencedetect` | Unexpected silence > 3 s |
| Resolution/fps | `ffprobe` | 1920×1080, 30 fps nahi hai |

```bash
ffmpeg -i renders/s05.mp4 -vf "freezedetect=n=0.003:d=15" -an -f null - 2>&1 | grep freeze_
ffmpeg -i renders/s05.mp4 -af "silencedetect=noise=-45dB:d=3" -vn -f null - 2>&1 | grep silence_
```

---

## 7. Layer 3: Human spot-check (har topic)

2× speed par poora topic dekho, aur ye checklist bharo:
- [ ] Koi jagah confusing lagi? (timestamp note karo)
- [ ] Koi visual narration se pehle ya baad mein aaya?
- [ ] Koi number galat dikha?
- [ ] Koi awaaz glitch?
- [ ] Pacing theek hai (bahut tez/slow)?
- [ ] Analogy kaam kar rahi hai?

Notes ko `qa_report.json` mein likho ([28](28_Quality_Assurance_Checklist.md)).

👉 Agla: [23_Imagery_Local_Image_Generation.md](23_Imagery_Local_Image_Generation.md)
