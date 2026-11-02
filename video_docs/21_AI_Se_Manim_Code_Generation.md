# 21 · AI Se Manim Code Generation

> **Is file mein:** Claude se script.json ke har scene ka Manim code kaise likhwayein: coder prompt, context mein kya dena hai, error-fix loop, common AI galtiyan, aur quality rules.

> 💰 **Budget mode note:** Default ab **template engine** hai ([41](41_Template_Engine_Zero_Cost_Animation.md)): ~80–90% scenes JSON actions se bante hain aur unke liye ye file ki zaroorat nahi. Ye file sirf un **custom scenes** (`"renderer": "manim"`) ke liye hai jo templates se nahi bante. Inka code Claude **subscription** (Claude Code) se ya local LLM (Qwen3-Coder 30B, Ollama) se likhwao. Paid API ki zaroorat nahi.

---

## 1. Flow

```
script.json (scene) + durations + component reference + style guide + example scene
        │
        ▼  Claude (Coder)
  scenes/s05_worked_example.py
        │
        ▼  manim -ql -s  (syntax/runtime check, last frame)
   error? ──yes──► traceback + code → Claude fix (max 3 tries) → human
        │no
        ▼
  preview render → critic ([22](22_Critic_Loop_Visual_QA.md))
```

---

## 2. Coder ko context mein kya dena hai

| Context | Kyun | Size |
|---|---|---|
| Scene JSON (beats, visuals, numbers) | Kya banana hai | 1–3k tokens |
| `durations.json` (is scene ke beats) | Timing budget | chhota |
| Verify block (sirf is scene ke ids) | Exact display strings | chhota |
| Component reference (auto-generated, [19](19_Manim_Component_Library_Design.md) §12) | Kya use karna hai | 1–2k |
| `LessonScene` base class API ([18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) §6) | Boilerplate | chhota |
| Style rules (short) | Colors/sizes/regions | 0.5k |
| **1 golden example scene** (pehle se approved) | Pattern copy karne ke liye | 1–2k |
| Manim version note | API mismatch se bachne ke liye | 1 line |

> **Golden example sabse powerful hai.** Pehla scene haath se (ya Claude ke saath carefully) banao aur approve karo. Baaki scenes ke liye usse example ki tarah do. LLMs examples ko instructions se zyada follow karte hain.

---

## 3. Coder prompt (`video/prompts/coder_prompt.md`)

```markdown
# ROLE
Tum ek expert Manim Community (v0.22) developer ho jo educational videos banata hai.

# TASK
Neeche diye scene spec ke liye ek Python file likho jisme ek class ho:
class {{SCENE_CLASS}}(LessonScene) with TOPIC_DIR="{{TOPIC_DIR}}", SCENE_ID="{{SCENE_ID}}".

# SCENE SPEC
{{SCENE_JSON}}

# BEAT DURATIONS (seconds, audio se naapi hui)
{{DURATIONS}}

# VERIFIED NUMBERS (screen par EXACTLY yahi strings dikhao, self.num(id) se)
{{VERIFY_SUBSET}}

# AVAILABLE API
- LessonScene: self.beat(id) [context manager, yields tracker t with t.duration],
  self.pause(id), self.num(verify_id) -> str, self.script["data"][...],
  self.wait_until_bookmark(name)
- Layout: place(mobject, region) with regions: title, body, left_half, right_half,
  left_wide, right_narrow, caption
- Theme: T(text, size), colors BG FG MUTED ACCENT YES NO HILITE WARN, sizes SIZE_TITLE/BODY/LABEL/SMALL
- Components:
{{COMPONENT_REFERENCE}}

# HARD RULES
1. Har beat ke liye EXACTLY ek `with self.beat("bXXX") as t:` block, script order mein.
   Block ke baad `self.pause("bXXX")`.
2. Block ke andar animations ka total run_time <= t.duration. Lambi animation ho to
   run_time=min(x, t.duration) ya t.duration ke fractions use karo.
3. Koi number hardcode MAT karo. Numbers self.num(id) se, data self.script["data"] se.
4. Har top-level object place(..., region) se position karo. Absolute coordinates sirf
   region ke andar chhote offsets ke liye.
5. "Current focus" ko HILITE se highlight karo; beat khatam hone par zaroorat na ho to normal karo.
6. Purane objects jo agle beat mein kaam ke nahi, FadeOut karo (screen clutter < 4 groups).
7. Font size 24 se kam nahi.
8. Sirf `from manim import *` aur hamari library imports. Koi random, koi network, koi file write nahi.
9. Bookmarks: sirf wahi use karo jo narration mein hain: {{BOOKMARKS}}.
10. Code ke upar 2-3 line comment: scene ka purpose. Har beat block ke upar 1 line comment.

# GOLDEN EXAMPLE (isi style mein likho)
{{GOLDEN_EXAMPLE}}

# OUTPUT
Sirf Python code, ek ```python block mein.
```

---

## 4. Static checks (render se pehle, free aur fast)

Claude ka code render karne se pehle ek chhota checker chalao:

```python
# video/lib/code_checks.py
import ast, re

def static_check(code: str, scene_spec: dict, verify_ids: set[str]) -> list[str]:
    issues = []
    tree = ast.parse(code)                                   # syntax error yahin pakda jaata hai

    # 1. har beat ka block exactly ek baar, order mein
    beat_ids = [b["id"] for b in scene_spec["beats"]]
    used = re.findall(r'self\.beat\(\s*["\'](b\d{3})["\']\s*\)', code)
    if used != beat_ids:
        issues.append(f"beat order/coverage mismatch: expected {beat_ids}, got {used}")

    # 2. num() ids valid
    for vid in re.findall(r'self\.num\(\s*["\'](\w+)["\']\s*\)', code):
        if vid not in verify_ids:
            issues.append(f"unknown verify id: {vid}")

    # 3. hardcoded decimal numbers in strings (0.940 jaise) -> num() use hona chahiye
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if re.search(r"\b\d+\.\d{2,}\b", node.value):
                issues.append(f"hardcoded number in string: {node.value!r}")

    # 4. forbidden imports/calls
    for bad in ("import random", "requests", "open(", "os.system", "subprocess"):
        if bad in code:
            issues.append(f"forbidden: {bad}")

    # 5. tiny fonts (Manim ka font_size aur hamare T() helper ka size=, dono)
    for m in re.finditer(r"\b(?:font_size|size)\s*=\s*(\d+)", code):
        if int(m.group(1)) < 24:
            issues.append(f"font_size {m.group(1)} < 24")
    return issues
```

---

## 5. Error-fix loop

```python
def generate_scene(scene_spec, ctx, max_tries=3):
    code = claude_coder(scene_spec, ctx)                     # prompt section 3
    for attempt in range(max_tries + 1):
        issues = static_check(code, scene_spec, ctx.verify_ids)
        if not issues:
            ok, log = render_check(code, quality="l", last_frame_only=True)   # manim -ql -s
            if ok:
                return code
            issues = [tail(log, 60)]                         # traceback ka last hissa
        if attempt == max_tries:
            raise NeedsHuman(scene_spec["id"], issues, code)
        code = claude_fix(code, issues, ctx)                 # "Ye errors hain, minimal change se fix karo"
```

### Fix prompt
```markdown
Neeche ek Manim scene ka code hai aur uske errors/issues. Code ko MINIMAL changes se fix karo.
Logic aur beat structure mat badlo. Sirf poora fixed code do.

<code>{{CODE}}</code>
<issues>{{ISSUES}}</issues>
<api_reminder>{{SHORT_API_NOTES}}</api_reminder>
```

**Max 3 tries kyun?** 3 tries mein fix na ho to aksar problem spec mein hoti hai (visual impossible/ambiguous). Tab insaan ko dekhna chahiye, warna loop tokens jalata rahega.

---

## 6. Common AI galtiyan (Manim mein)

| Galti | Symptom | Prevention |
|---|---|---|
| 3b1b `manimlib` API mix karna | `ImportError`, `ShowCreation` not found | Prompt: "Manim Community v0.22; `Create` not `ShowCreation`" |
| Purane API names | `TextMobject`, `TexMobject` | Same, aur golden example |
| `MathTex` mein Hindi | LaTeX error | Rule: Hindi/Hinglish text `T()` se |
| `TransformMatchingTex` parts mismatch | Ajeeb morph | `EquationSteps` component use karo |
| Objects overlap | Ganda frame | `place()` + critic |
| Animation audio se lamba | Narration ke baad bhi animation chal raha | Rule 2 + duration check |
| Sab kuch ek saath screen par | Clutter | Rule 6 |
| `self.wait()` hardcoded lambe | Dead air | Beat blocks + pause() hi use karo |
| Same object do baar add | Double rendering / flicker | Golden example pattern |
| Index-based highlighting galat part par | Galat term highlight | `substrings_to_isolate` ya parts list explicit |

---

## 7. Scene size guideline

- Ek scene file mein **max ~10–15 beats** (lamba ho to scene split karo)
- Code ~100–250 lines
- Ek scene = ek render job (parallel rendering, [26](26_Rendering_Performance_Parallel.md))

---

## 8. Version pinning

Prompt mein exact versions likho aur environment mein bhi pin karo:
```text
manim==0.22.0
manim-voiceover==0.4.0
```
LLM ki training mein purane versions ka code zyada hota hai. Explicit version + golden example se drift kam hota hai.

---

## 9. Human review: kab zaroori

| Situation | Review |
|---|---|
| Pehla scene of a new scene-type | ✅ Full review (ye golden example banega) |
| Critic ne "major" issue flag kiya | ✅ |
| Fix loop fail | ✅ |
| Baaki | Preview video 2× speed par dekh lo |

👉 Agla: [22_Critic_Loop_Visual_QA.md](22_Critic_Loop_Visual_QA.md)
