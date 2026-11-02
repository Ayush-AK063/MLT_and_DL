# 41 · Template Engine: Bina AI-Code Ke Animation (Zero-Cost)

> **Is file mein:** Har video ke liye AI se naya Manim code likhwane ki jagah ek **template engine**: `script.json` ke har beat mein simple **actions** likhe jaate hain (jaise "table dikhao", "Sunny rows highlight karo", "bar chart banao"), aur ek fixed, tested Python engine unhe animation mein badal deta hai. Ye budget mode ka core hai ([42](42_Budget_Mode_Zero_Cost_Plan.md)). Engine ka poora code, har action ka reference, example JSON, validator, aur test result yahan hai.

---

## 1. Idea (seedhi baat)

**Purana tareeka ([21](21_AI_Se_Manim_Code_Generation.md)):**
```
script.json → Claude har scene ka 100–250 line Python likhta hai → errors → fix → critic → fix
```
Isme tokens (paisa) bahut lagte hain, aur har video mein naye bugs aa sakte hain.

**Template engine:**
```
script.json (beats + actions JSON) → validate_actions() → TemplateScene (fixed code) → video
```
- **Python code ek baar likha aur test kiya.** Uske baad har video mein sirf **JSON data** badalta hai
- JSON likhna aasaan kaam hai, isliye **local LLM (free)** bhi achhe se kar leta hai, ya tum khud haath se kar sakte ho
- Galti ho to **validator render se pehle hi pakad leta hai** (galat action, missing id, galat number id, galat bookmark)
- Same input se hamesha same output (deterministic)

**Analogy:** Purana tareeka = har baar naya ghar banwana. Template engine = Lego blocks: blocks (actions) fixed aur tested hain, har video mein sirf unhe naye tareeke se jodna hai.

---

## 2. Kya-kya ho sakta hai (action reference)

Har action ek JSON object hai: `{"do": "<action>", ...params}`. Ek beat ke actions order mein chalte hain.

| Action | Kya karta hai | Required params | Optional | Default time |
|---|---|---|---|---|
| `title` | Upar title likhta hai | `text` | `id` (default `"title"`) | 0.8 s |
| `text` | Text label | `id`, `text` | `region` / `next_to`+`dir`+`buff`, `size`, `color` | 1.0 s |
| `math` | LaTeX formula (MathTex) | `id`, `tex` (string ya parts list) | `region` / `next_to` | 1.5 s |
| `table` | Data table (script ke `data` block se) | `id`, `data` | `region`, `color_target` (Yes/No coloring wala column) | 1.2 s |
| `highlight_rows` | Rows ko yellow karta hai | `table`, `where` (`{"Outlook":"Sunny"}`) | | 0.8 s |
| `box_rows` | Har matching row ke around box | `table`, `where` | `id` | 0.8 s |
| `glow_column` | Column flash | `table`, `column` | | 0.8 s |
| `bars` | Bar chart (values verify ids se) | `id`, `items` (`{"Outlook":"gain_outlook"}`) | `max_value`, `region` | 2.0 s |
| `crown` | Winner bar yellow | `id`, `name` | | 0.8 s |
| `tree` | Decision tree grow animation | `id`, `spec` ([19](19_Manim_Component_Library_Design.md) §9 format) | `region` | 2.5 s |
| `balls` | Entropy analogy wala balls ka dabba | `id`, `pos`, `neg` | `label`, `region` | 1.0 s |
| `bullets` | Bullet list (hidden, `reveal` se dikhegi) | `id`, `items` | `region` | 0 |
| `reveal` | Ek bullet dikhata hai | `id`, `index` | | 0.8 s |
| `box` | Kisi object ke around yellow box | `target` | `color` | 0.6 s |
| `indicate` | Object flash/highlight | `target` | | 0.7 s |
| `fade_out` | Objects hatao | `targets` (ids list ya `"all"`) | | 0.5 s |
| `clear` | Screen saaf | – | | 0.5 s |
| `timer` | Pause-and-try countdown | `seconds` | | (khud ka time) |
| `wait_bookmark` | Narration ke bookmark tak ruko | `mark` | | – |

### Common rules
- **Numbers:** Text/formula mein `{num:<verify_id>}` likho, jaise `"H = {num:H_sunny}"` → `"H = 0.971"` (verify block ka `display`). **Kabhi number seedha mat likho**
- **Position:** `"region": "left_wide"` (regions: `title, body, left_half, right_half, left_wide, right_narrow, caption`, [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) ya `"next_to": "<id>", "dir": "down"`
- **Timing:** Har action ka default time hota hai (upar table). Agar beat ka audio chhota hai to engine **sab ko proportionally chhota** kar deta hai, taaki animations narration ke andar fit ho jaayein (92% budget). `"rt": 2.0` se kisi action ka time override kar sakte ho
- **Bookmark:** `{"do":"wait_bookmark","mark":"split"}` se pehle wale actions bookmark se pehle khatam hote hain, aur baad wale bookmark ke baad shuru hote hain

---

## 3. Example: script.json beat with actions

```json
{
  "id": "s05_worked_example",
  "type": "worked_example",
  "renderer": "template",
  "beats": [
    {"id": "b040", "narration": "Chalo ab Outlook ka gain nikalte hain.",
     "actions": [
       {"do": "title", "text": "Outlook ka Information Gain"},
       {"do": "table", "id": "tbl", "data": "playtennis", "region": "left_wide", "color_target": "Play"},
       {"do": "glow_column", "table": "tbl", "column": "Outlook"}]},

    {"id": "b041", "narration": "Sunny wale din five hain. <bookmark mark='split'/>Do mein tennis khela, teen mein nahi.",
     "actions": [
       {"do": "highlight_rows", "table": "tbl", "where": {"Outlook": "Sunny"}},
       {"do": "wait_bookmark", "mark": "split"},
       {"do": "text", "id": "lab", "text": "Sunny: 2+ / 3−", "region": "right_narrow"}]},

    {"id": "b042", "narration": "Iski entropy aati hai zero point nine seven one.",
     "actions": [
       {"do": "text", "id": "h", "text": "H = {num:H_sunny}", "next_to": "lab", "dir": "down"},
       {"do": "box", "target": "h"}]},

    {"id": "b043", "narration": "Ab chaaron attributes ka gain compare karte hain.",
     "actions": [
       {"do": "clear"},
       {"do": "title", "text": "Kaun jeeta?"},
       {"do": "bars", "id": "g", "max_value": 0.3,
        "items": {"Outlook": "gain_outlook", "Humidity": "gain_humidity",
                  "Wind": "gain_wind", "Temperature": "gain_temperature"}},
       {"do": "crown", "id": "g", "name": "Outlook"}]}
  ]
}
```

Scene file sirf itni hai (har scene ke liye 3 lines):
```python
from video.lib.template_engine import TemplateScene

class S05(TemplateScene):
    TOPIC_DIR = "video/out/L20/T07"
    SCENE_ID = "s05_worked_example"
```
Ye file bhi pipeline khud generate kar sakti hai (`script.json` ke scene ids se).

---

## 4. Engine ka code (`video/lib/template_engine.py`), tested

Dependencies: component library ([19](19_Manim_Component_Library_Design.md)), `place()` ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md) §6, `components/layout.py`), `LessonScene` + `PrebakedService` ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) §5–6), `to_word_boundaries` ([16](16_Word_Timestamps_Forced_Alignment_Captions.md) §6, `video/lib/align.py`). Inhi files ke saath ye code as-is chala hai (section 7).

```python
"""Template engine: script.json ke beat "actions" se Manim animation (har video ke liye naya code nahi)."""
from __future__ import annotations

import re

from manim import *

from .components.ball_box import BallBox
from .components.bar_compare import BarCompare
from .components.highlight_table import HighlightTable
from .components.layout import REGIONS, place
from .components.pause_timer import PauseTimer
from .components.theme import HILITE, MUTED, SIZE_BODY, SIZE_LABEL, SIZE_TITLE, T
from .components.tree_diagram import TreeDiagram
from .scene_base import LessonScene

# ---------------- action registry ----------------
# name -> (function, default_run_time, required_params)
ACTIONS: dict[str, tuple] = {}


def action(name: str, rt: float = 1.0, required: tuple = ()):
    def deco(fn):
        ACTIONS[name] = (fn, rt, required)
        return fn
    return deco


DIRS = {"up": UP, "down": DOWN, "left": LEFT, "right": RIGHT}
NUM_RE = re.compile(r"\{num:(\w+)\}")


def fill_numbers(scene, text: str) -> str:
    """'H = {num:H_sunny}' -> 'H = 0.971' (verify block se)."""
    return NUM_RE.sub(lambda m: scene.num(m.group(1)), text)


def position(scene, mob, p: dict):
    if "next_to" in p:
        ref = scene.objs[p["next_to"]]
        mob.next_to(ref, DIRS[p.get("dir", "down")], buff=p.get("buff", 0.3))
    else:
        place(mob, p.get("region", "body"))
    return mob


# ---------------- actions ----------------
@action("title", rt=0.8, required=("text",))
def a_title(scene, text, id="title", **p):
    mob = place(T(fill_numbers(scene, text), size=SIZE_TITLE), "title")
    scene.objs[id] = mob
    return [Write(mob)]


@action("text", rt=1.0, required=("id", "text"))
def a_text(scene, id, text, size=SIZE_BODY, color=None, **p):
    mob = T(fill_numbers(scene, text), size=size, **({"color": color} if color else {}))
    scene.objs[id] = position(scene, mob, p)
    return [FadeIn(mob, shift=UP * 0.15)]


@action("math", rt=1.5, required=("id", "tex"))
def a_math(scene, id, tex, **p):
    parts = [fill_numbers(scene, s) for s in (tex if isinstance(tex, list) else [tex])]
    mob = MathTex(*parts)
    scene.objs[id] = position(scene, mob, p)
    return [Write(mob)]


@action("table", rt=1.2, required=("id", "data"))
def a_table(scene, id, data, color_target=None, **p):
    mob = HighlightTable.from_data(scene.script["data"][data], color_target=color_target)
    scene.objs[id] = position(scene, mob, p)
    return [FadeIn(mob)]


@action("highlight_rows", rt=0.8, required=("table", "where"))
def a_highlight_rows(scene, table, where, **p):
    return [scene.objs[table].highlight_rows(**where)]


@action("box_rows", rt=0.8, required=("table", "where"))
def a_box_rows(scene, table, where, id=None, **p):
    boxes = scene.objs[table].box_rows(**where)
    if id:
        scene.objs[id] = boxes
    return [Create(boxes)]


@action("glow_column", rt=0.8, required=("table", "column"))
def a_glow_column(scene, table, column, **p):
    return [scene.objs[table].glow_column(column)]


@action("bars", rt=2.0, required=("id", "items"))
def a_bars(scene, id, items, max_value=None, **p):
    # items: {"Outlook": "gain_outlook", ...}  (verify ids -> display string + float)
    data = {name: (scene.num(vid), float(scene.num(vid))) for name, vid in items.items()}
    mob = BarCompare(data, max_value=max_value)
    scene.objs[id] = position(scene, mob, p)
    return [mob.grow()]


@action("crown", rt=0.8, required=("id", "name"))
def a_crown(scene, id, name, **p):
    return [scene.objs[id].crown(name)]


@action("tree", rt=2.5, required=("id", "spec"))
def a_tree(scene, id, spec, **p):
    mob = TreeDiagram(spec)
    scene.objs[id] = position(scene, mob, p)
    return [mob.grow()]


@action("balls", rt=1.0, required=("id", "pos", "neg"))
def a_balls(scene, id, pos, neg, label="", **p):
    mob = BallBox(pos, neg, label=label)
    scene.objs[id] = position(scene, mob, p)
    return [FadeIn(mob)]


@action("bullets", rt=0.0, required=("id", "items"))
def a_bullets(scene, id, items, **p):
    mob = VGroup(*[T("•  " + fill_numbers(scene, s), size=SIZE_BODY) for s in items])
    mob.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    scene.objs[id] = position(scene, mob, p)
    mob.set_opacity(0)
    scene.add(mob)
    return []


@action("reveal", rt=0.8, required=("id", "index"))
def a_reveal(scene, id, index, **p):
    return [scene.objs[id][index].animate.set_opacity(1)]


@action("box", rt=0.6, required=("target",))
def a_box(scene, target, color=HILITE, **p):
    return [Create(SurroundingRectangle(scene.objs[target], color=color, buff=0.12, corner_radius=0.08))]


@action("indicate", rt=0.7, required=("target",))
def a_indicate(scene, target, **p):
    return [Indicate(scene.objs[target], color=HILITE)]


@action("fade_out", rt=0.5, required=("targets",))
def a_fade_out(scene, targets, **p):
    ids = list(scene.objs) if targets == "all" else targets
    mobs = [scene.objs.pop(i) for i in ids if i in scene.objs]
    return [FadeOut(VGroup(*mobs))] if mobs else []


@action("clear", rt=0.5)
def a_clear(scene, **p):
    scene.objs.clear()
    return [FadeOut(*scene.mobjects)] if scene.mobjects else []


@action("timer", rt=0.0, required=("seconds",))
def a_timer(scene, seconds, **p):
    tm = PauseTimer(seconds=seconds).to_corner(DR)
    scene.add(tm)
    tm.run(scene)                # khud play/wait karta hai (pause_and_try ke liye)
    scene.remove(tm)
    return []


# ---------------- engine ----------------
def validate_actions(script: dict) -> list[str]:
    """Render se pehle: action names, required params, ids aur verify ids check."""
    issues, verify_ids = [], {v["id"] for v in script.get("verify", [])}
    for sc in script["scenes"]:
        defined = set()
        for b in sc["beats"]:
            for i, a in enumerate(b.get("actions", [])):
                where = f'{sc["id"]}/{b["id"]}#{i}'
                name = a.get("do")
                if name == "wait_bookmark":
                    if f"mark='{a.get('mark')}'" not in b["narration"].replace('"', "'"):
                        issues.append(f"{where}: bookmark {a.get('mark')!r} narration mein nahi")
                    continue
                if name not in ACTIONS:
                    issues.append(f"{where}: unknown action {name!r}")
                    continue
                missing = [r for r in ACTIONS[name][2] if r not in a]
                if missing:
                    issues.append(f"{where}: {name} missing {missing}")
                for key in ("table", "target", "next_to"):
                    if key in a and a[key] not in defined:
                        issues.append(f"{where}: {key}={a[key]!r} pehle define nahi hua")
                if name in ("reveal", "crown") and a.get("id") not in defined:
                    issues.append(f"{where}: id={a.get('id')!r} pehle define nahi hua")
                for vid in NUM_RE.findall(str(a)):
                    if vid not in verify_ids:
                        issues.append(f"{where}: unknown verify id {vid!r}")
                if name == "bars":
                    issues += [f"{where}: unknown verify id {v!r}" for v in a["items"].values() if v not in verify_ids]
                if "id" in a and name not in ("reveal", "crown", "fade_out"):
                    defined.add(a["id"])
                if name == "title":
                    defined.add(a.get("id", "title"))
    return issues


class TemplateScene(LessonScene):
    """Subclass sirf TOPIC_DIR aur SCENE_ID set kare; baaki sab script.json ke actions se."""

    def construct(self):
        self.objs = {}
        for b in self.scene_spec["beats"]:
            with self.beat(b["id"]) as t:
                self._run(b.get("actions", []), t)
            self.pause(b["id"])

    def _run(self, actions, tracker):
        # bookmark par segments mein todo; har segment apne time budget mein fit ho
        segments, cur = [], []
        for a in actions:
            if a.get("do") == "wait_bookmark":
                segments.append((cur, a["mark"]))
                cur = []
            else:
                cur.append(a)
        segments.append((cur, None))
        for acts, mark in segments:
            budget = (tracker.time_until_bookmark(mark) if mark
                      else tracker.get_remaining_duration())
            self._play_segment(acts, budget)
            if mark:
                self.wait_until_bookmark(mark)

    def _play_segment(self, acts, budget):
        # pehle sirf default run_times jodo (actions abhi chalao mat), phir order mein ek-ek chalao
        rts = [a.get("rt", ACTIONS[a["do"]][1]) for a in acts]
        total = sum(rts)
        scale = min(1.0, (0.92 * budget) / total) if total > 0 and budget > 0 else 1.0
        for a, rt in zip(acts, rts):
            fn = ACTIONS[a["do"]][0]
            anims = fn(self, **{k: v for k, v in a.items() if k not in ("do", "rt")})
            if anims:
                self.play(*anims, run_time=max(rt * scale, 1 / config.frame_rate))
```

### Code kaise kaam karta hai (andar se)
1. `TemplateScene.construct()` scene ke har beat ke liye `with self.beat(id) as t:` kholta hai. Audio pre-baked service se lagta hai ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md))
2. Beat ke actions ko `wait_bookmark` par **segments** mein toda jaata hai
3. Har segment ka **time budget** = bookmark tak ka time (`tracker.time_until_bookmark`), ya beat ka bacha hua audio (`get_remaining_duration`)
4. Segment ke actions ke default times jode jaate hain. Agar total budget se zyada hai to sab ko ek hi factor se chhota kiya jaata hai (`scale`)
5. Actions **order mein ek-ek karke** chalte hain: function object banata hai, `self.objs[id]` mein rakhta hai, aur animations return karta hai, jo `self.play()` hoti hain
6. `timer` jaisa action khud play/wait karta hai (pause-and-try mein narration ke baad bhi chal sakta hai)
7. Beat ke baad `self.pause(id)` (`pause_after`)

---

## 5. Validator: render se pehle galtiyan pakadna

`validate_actions(script)` ye sab check karta hai:
- Action ka naam registry mein hai?
- Required params diye hain?
- `table` / `target` / `next_to` / `reveal` / `crown` jis id ko refer kar rahe hain, wo **pehle define** hua?
- `{num:...}` aur `bars.items` ke verify ids `verify` block mein hain?
- `wait_bookmark` ka mark narration mein hai?

**Test output** (jaan-boojh kar 4 galtiyan daal kar):
```
bookmark 'splitt' narration mein nahi
unknown action 'zoom'
unknown verify id 'H_rain'
target='nope' pehle define nahi hua
```
Sahi script par output `[]` aaya ✅

Pipeline mein ye **G4 gate** ([28](28_Quality_Assurance_Checklist.md)) ki jagah leta hai. Template scenes ke liye `static_check` ki zaroorat nahi, kyunki Python code hai hi nahi.

---

## 6. Actions JSON kaun likhega?

| Option | Cost | Quality |
|---|---|---|
| **Claude subscription** (Claude Code, jo abhi use kar rahe ho) | ₹0 extra | Best |
| **Local LLM** (Ollama, Qwen3 30B-class, Mac par) | ₹0 | Achha (JSON + reference table de do) |
| **Haath se** (khud likhna) | ₹0 | Tumhare control mein, lekin time lagta hai |

Script likhte waqt hi actions bhi likhwa lo (ek hi pass). Prompt mein ye section add karo ([07](07_Script_Generation_Prompts_With_Claude.md) Pass 2 ke saath, ya [42](42_Budget_Mode_Zero_Cost_Plan.md) ka local prompt):

```markdown
# VISUAL ACTIONS
Har beat mein "actions" list do. SIRF neeche ke actions use karo (koi naya action mat banao):
{{ACTION_REFERENCE_TABLE}}

Rules:
- Numbers kabhi seedha mat likho; "{num:<verify_id>}" use karo.
- Har object ko "id" do; baad mein usi id se refer karo (pehle define, phir use).
- Position: "region" (title, body, left_half, right_half, left_wide, right_narrow, caption)
  ya "next_to" + "dir" (up/down/left/right).
- Ek screen par max 3-4 groups; zyada ho to "clear" ya "fade_out".
- Narration mein bookmark ho to usi naam ka {"do":"wait_bookmark","mark":...} action do.
- Pause-and-try beat mein {"do":"timer","seconds":6}.
```

Phir:
```bash
python -c "import json; from video.lib.template_engine import validate_actions; \
print(validate_actions(json.load(open('video/out/L20/T07/script.json'))))"
```
Issues aaye to LLM ko wapas do: "ye validator errors hain, JSON fix karo".

---

## 7. Test result (2026-10-18, manim 0.22.0, M1 Mac)

Ek test topic banaya: 2 scenes, 6 beats, sine-tone fake audio, PlayTennis data, verify block.

| Scene | Expected | Result |
|---|---|---|
| `s05_worked_example` (title, table, glow, highlight, bookmark, label, verified number + box, clear, bar chart + crown) | ~14.5 s (beats + pauses) | ✅ 14.2 s (15 fps preview rounding) |
| `s09_recap` (title, 3 bullets reveal with `{num:...}`, 3 s timer) | timer beat audio se lamba chalna chahiye | ✅ 9.3 s |

Frames dekh kar check kiya:
- Table left mein, Outlook column glow, Sunny rows (D1, D2, D8, D9, D11) yellow ✅
- Bookmark ke baad right side "Sunny: 2+ / 3−", uske neeche "H = 0.971" yellow box mein (number verify block se aaya) ✅
- `clear` ke baad "Kaun jeeta?" + bars 0.2467 / 0.1518 / 0.0481 / 0.0292, Outlook yellow (crown) ✅
- Recap bullets mein "Outlook ka gain sabse zyada: 0.2467" (`{num:gain_outlook}` se) ✅, aur "Pause karo, khud try karo!" timer ✅
- `math` action (MathTex) ko test machine par LaTeX `dvisvgm` na hone ki wajah se render-test nahi kiya ([40](40_Mac_Apple_Silicon_Setup.md) §2)

---

## 8. Naya action add karna

Jab kisi lecture ko naya visual chahiye (jaise ROC curve):
```python
@action("roc", rt=2.5, required=("id", "points"))
def a_roc(scene, id, points, **p):
    mob = ROCCurve(scene.script["data"][points])     # naya component (doc 19 rules ke saath)
    scene.objs[id] = position(scene, mob, p)
    return [mob.draw()]
```
1. Component banao + visual test ([19](19_Manim_Component_Library_Design.md) §13)
2. Action register karo (`@action`)
3. Action reference table update karo (section 2 + prompt)
4. Ek test scene render karke frames dekho

Library jitni badhegi, utne zyada scenes bina AI-code ke banenge.

---

## 9. Kab template kaafi nahi

Kuch visuals ek-baar ke aur complex hote hain (jaise PCA ka 3D rotation, ya ek custom proof animation). Unke liye:
- Scene ka `"renderer": "manim"` rakho aur custom code likho (Claude subscription se ya haath se, [21](21_AI_Se_Manim_Code_Generation.md))
- Baaki scenes `"renderer": "template"` hi rahenge

**Target:** ~80–90% scenes template se, aur sirf 10–20% custom. Jo custom visual baar-baar aaye, use action bana do.

---

## 10. Checklist

- [ ] Har template scene ke beats mein `actions` hain
- [ ] `validate_actions()` → `[]`
- [ ] Koi number seedha nahi likha (sab `{num:...}`)
- [ ] Preview render + frames dekhe (ya layout audit, [22](22_Critic_Loop_Visual_QA.md))
- [ ] Naye actions ka visual test hua

👉 Agla: [42_Budget_Mode_Zero_Cost_Plan.md](42_Budget_Mode_Zero_Cost_Plan.md)
