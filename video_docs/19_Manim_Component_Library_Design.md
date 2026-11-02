# 19 · Manim Component Library Design

> **Is file mein:** Reusable Manim components kyun zaroori hain, library ka design (API rules), har component ka code (tested), aur AI coder ko components kaise "sikhayein".

---

## 1. Kyun component library?

Code2Video aur TheoremExplainAgent dono papers mein sabse common problem **layout issues** thi: elements overlap ho jaate the ya frame ke bahar chale jaate the (TEA paper: "most videos exhibit minor issues with visual element layout"). Code2Video ne asset reuse aur visual anchors se element-layout score 0.59 → 0.91 tak improve kiya.

**Hamara solution:** AI ko har baar raw Manim se table/tree/chart banane mat do. Ek **tested library** do jisme:
- Layout pehle se sahi ho (auto-fit, safe margins)
- Style consistent ho (theme colors, fonts)
- API simple ho (AI galti kam kare)
- Har component ka "highlight" method ho (signaling principle)

**Fayda:** Pehle 2–3 topics mein library banti hai. Uske baad har topic ka code chhota, reliable aur fast banta hai.

---

## 2. Design rules (har component ke liye)

| Rule | Kyun |
|---|---|
| Component = `VGroup` subclass | Normal Manim object ki tarah move/scale/animate ho sake |
| Constructor mein data, style theme se | AI ko colors/sizes decide na karne padein |
| `fit_to(width, height)` / auto-scale | Frame se bahar na jaaye |
| Highlight methods **Animation return karein** | `self.play(table.highlight_rows(...))` |
| Koi hardcoded number nahi | Numbers verify block se strings ke roop mein aate hain |
| Docstring mein 1-line usage example | AI coder prompt mein yahi docs jaate hain |
| Deterministic (no randomness) | Same input = same frame |

---

## 3. Library structure

```
video/lib/components/
├── __init__.py          ← sab export
├── theme.py             ← colors, fonts, sizes, safe area, apply_theme()
├── layout.py            ← named layouts (regions), fit helpers
├── highlight_table.py   ← data table + row/column highlight
├── result_box.py        ← answer ke around box + label
├── equation_steps.py    ← formula step-by-step (TransformMatchingTex)
├── bar_compare.py       ← attributes ka bar chart (gain comparison)
├── tree_diagram.py      ← decision tree (nodes, edges, grow animation)
├── ball_box.py          ← entropy analogy: mixed balls ka dabba
├── pause_timer.py       ← "pause and try" countdown
├── title_card.py        ← scene title / chapter heading
└── bullet_recap.py      ← recap ke 3 points
```

---

## 4. `theme.py`

```python
from manim import *

# ---- palette (doc 20 se) ----
BG = "#0F1117"
FG = "#E8E6E3"
MUTED = "#8B8F98"
ACCENT = "#58C4DD"      # primary (blue)
YES = "#83C167"         # positive class
NO = "#FC6255"          # negative class
HILITE = "#FFD84D"      # highlight / current focus
WARN = "#F5A623"

FONT = "Inter"                 # fallback system font agar installed nahi
FONT_HI = "Noto Sans Devanagari"

SIZE_TITLE = 44
SIZE_BODY = 34
SIZE_LABEL = 28
SIZE_SMALL = 24

SAFE_X = 6.6     # |x| <= 6.6 (frame half-width ~7.11)
SAFE_Y = 3.6     # |y| <= 3.6 (frame half-height 4.0)


def apply_theme(scene: Scene) -> None:
    scene.camera.background_color = BG


def T(text: str, size: int = SIZE_BODY, color: str = FG, **kw) -> Text:
    """Theme text. Devanagari ho to Hindi font."""
    font = FONT_HI if any("ऀ" <= ch <= "ॿ" for ch in text) else FONT
    return Text(text, font_size=size, color=color, font=font, **kw)


def fit_in_safe_area(m: Mobject, max_w: float = 2 * SAFE_X, max_h: float = 2 * SAFE_Y) -> Mobject:
    if m.width > max_w:
        m.scale_to_fit_width(max_w)
    if m.height > max_h:
        m.scale_to_fit_height(max_h)
    return m
```

> Font installed na ho to Pango fallback font use karta hai (warning ke saath). Render machine par **Inter** aur **Noto Sans Devanagari** install karo ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)).

---

## 5. `HighlightTable`

Manim ka built-in `Table` bhi hai, lekin cell-level control aur highlighting ke liye ek simple grid zyada predictable hai:

```python
from manim import *
from .theme import T, FG, MUTED, HILITE, YES, NO, SIZE_SMALL, fit_in_safe_area


class HighlightTable(VGroup):
    """HighlightTable(columns, rows).to_edge(LEFT); self.play(t.highlight_rows(Outlook="Sunny"))"""

    def __init__(self, columns, rows, col_pad=0.35, cell_h=0.42, size=SIZE_SMALL,
                 color_target=None, **kw):
        super().__init__(**kw)
        self.columns, self.rows_data = list(columns), [list(r) for r in rows]
        grid = []                                          # grid[r][c] Text; r=0 header
        for r, row in enumerate([self.columns] + self.rows_data):
            line = []
            for c, val in enumerate(row):
                color = MUTED if r == 0 else FG
                if r > 0 and color_target and self.columns[c] == color_target:
                    color = YES if str(val).lower() in ("yes", "1", "+") else NO
                line.append(T(str(val), size=size, color=color, weight=BOLD if r == 0 else NORMAL))
            grid.append(line)
        # column width = us column ka sabse chauda text + padding (warna lambe headers overlap karte hain)
        col_w = [max(grid[r][c].width for r in range(len(grid))) + col_pad
                 for c in range(len(self.columns))]
        xs = np.cumsum([0] + col_w[:-1]) + np.array(col_w) / 2
        for r, line in enumerate(grid):
            for c, txt in enumerate(line):
                txt.move_to(np.array([xs[c], -r * cell_h, 0]))
                self.add(txt)
        self.cells = grid
        top = -cell_h / 2 - 0.02
        self.add(Line([0, top, 0], [sum(col_w), top, 0], color=MUTED, stroke_width=1.5))
        self.cell_h = cell_h
        self.move_to(ORIGIN)
        fit_in_safe_area(self)

    @classmethod
    def from_data(cls, block: dict, **kw):
        return cls(block["columns"], block["rows"], **kw)

    def _row_ids(self, **cond):
        idx = {c: i for i, c in enumerate(self.columns)}
        return [r for r, row in enumerate(self.rows_data, start=1)
                if all(row[idx[k]] == v for k, v in cond.items())]

    def row_group(self, **cond) -> VGroup:
        return VGroup(*[m for r in self._row_ids(**cond) for m in self.cells[r]])

    def column_group(self, name: str, include_header=True) -> VGroup:
        c = self.columns.index(name)
        start = 0 if include_header else 1
        return VGroup(*[self.cells[r][c] for r in range(start, len(self.cells))])

    def highlight_rows(self, color=HILITE, **cond) -> Animation:
        return self.row_group(**cond).animate.set_color(color)

    def glow_column(self, name: str) -> Animation:
        return Indicate(self.column_group(name), color=HILITE, scale_factor=1.08)

    def box_rows(self, color=HILITE, **cond) -> VGroup:
        """Har matching row ka ALAG box (rows non-contiguous ho sakti hain; ek bada box beech ki rows bhi gher leta)."""
        return VGroup(*[SurroundingRectangle(VGroup(*self.cells[r]), color=color, buff=0.05,
                                             stroke_width=2) for r in self._row_ids(**cond)])
```

---

## 6. `ResultBox`

```python
from manim import *
from .theme import HILITE, T, SIZE_LABEL


class ResultBox:
    """self.play(ResultBox.around(eq[2]))  |  self.play(*ResultBox.with_label(eq[2], "best!"))"""

    @staticmethod
    def around(m: Mobject, color=HILITE) -> Animation:
        return Create(SurroundingRectangle(m, color=color, buff=0.12, corner_radius=0.08))

    @staticmethod
    def with_label(m: Mobject, label: str, color=HILITE, direction=DOWN):
        box = SurroundingRectangle(m, color=color, buff=0.12, corner_radius=0.08)
        lab = T(label, size=SIZE_LABEL, color=color).next_to(box, direction, buff=0.15)
        return [Create(box), FadeIn(lab, shift=direction * 0.15)]
```

---

## 7. `EquationSteps` (formula derivation)

```python
from manim import *
from .theme import HILITE


class EquationSteps:
    """
    steps = EquationSteps([["H(S)", "=", r"-\tfrac{9}{14}\log_2\tfrac{9}{14}", "-", r"\tfrac{5}{14}\log_2\tfrac{5}{14}"],
                           ["H(S)", "=", "0.4098", "+", "0.5305"],
                           ["H(S)", "=", "0.940"]])
    self.play(steps.write_first()); self.play(steps.next()); self.play(steps.next())
    """

    def __init__(self, steps: list[list[str]], position=ORIGIN, font_size=44):
        self.mobs = [MathTex(*parts, font_size=font_size).move_to(position) for parts in steps]
        self.i = 0

    @property
    def current(self) -> MathTex:
        return self.mobs[self.i]

    def write_first(self) -> Animation:
        return Write(self.mobs[0])

    def next(self) -> Animation:
        a, b = self.mobs[self.i], self.mobs[self.i + 1]
        self.i += 1
        return TransformMatchingTex(a, b)

    def highlight_part(self, idx: int, color=HILITE) -> Animation:
        return Indicate(self.current[idx], color=color)
```
> `TransformMatchingTex` parts ko unke **TeX string** se match karta hai. Isliye har step mein common parts (`"H(S)"`, `"="`) **exactly same string** mein likho.

---

## 8. `BarCompare` (jaise 4 attributes ka gain)

```python
from manim import *
from .theme import T, ACCENT, HILITE, FG, MUTED, SIZE_LABEL, SIZE_SMALL


class BarCompare(VGroup):
    """BarCompare({"Outlook": ("0.2467", 0.2467), "Humidity": ("0.1518", 0.1518)}, max_value=0.3)
       value = (display_string_from_verify, float_for_height)"""

    def __init__(self, items: dict[str, tuple[str, float]], max_value=None, bar_w=0.9,
                 max_h=3.6, gap=0.6, **kw):
        super().__init__(**kw)
        max_value = max_value or max(v for _, v in items.values())
        self.bars, self.labels, self.values = {}, {}, {}
        for i, (name, (disp, val)) in enumerate(items.items()):
            h = max(0.02, max_h * val / max_value)
            bar = Rectangle(width=bar_w, height=h, fill_color=ACCENT, fill_opacity=0.9,
                            stroke_width=0).move_to([i * (bar_w + gap), h / 2, 0])
            name_t = T(name, size=SIZE_SMALL, color=MUTED).next_to(bar, DOWN, buff=0.15)
            if name_t.width > bar_w + gap * 0.8:              # lamba naam padosi label se na takraye
                name_t.scale_to_fit_width(bar_w + gap * 0.8)
            val_t = T(disp, size=SIZE_LABEL, color=FG).next_to(bar, UP, buff=0.12)
            self.bars[name], self.labels[name], self.values[name] = bar, name_t, val_t
            self.add(bar, name_t, val_t)
        self.move_to(ORIGIN)

    def grow(self, lag_ratio=0.15) -> Animation:
        anims = [AnimationGroup(GrowFromEdge(self.bars[n], DOWN), FadeIn(self.labels[n]),
                                FadeIn(self.values[n])) for n in self.bars]
        return LaggedStart(*anims, lag_ratio=lag_ratio)

    def crown(self, name: str) -> Animation:
        return AnimationGroup(self.bars[name].animate.set_fill(HILITE),
                              Indicate(self.values[name], color=HILITE))
```

---

## 9. `TreeDiagram` (decision trees ke liye)

```python
from manim import *
from .theme import T, BG, ACCENT, YES, NO, FG, MUTED, SIZE_SMALL, fit_in_safe_area


class TreeDiagram(VGroup):
    """
    spec = {"label": "Outlook", "children": [
              ("Sunny", {"label": "Humidity", "children": [("High", {"leaf": "No"}), ("Normal", {"leaf": "Yes"})]}),
              ("Overcast", {"leaf": "Yes"}),
              ("Rain", {"label": "Wind", "children": [("Strong", {"leaf": "No"}), ("Weak", {"leaf": "Yes"})]})]}
    tree = TreeDiagram(spec); self.play(tree.grow())
    """

    def __init__(self, spec: dict, level_gap=1.5, leaf_gap=1.9, **kw):
        super().__init__(**kw)
        self.order = []                                   # (node_mob, edge_mob, edge_label) in BFS order
        self._leaf_x = 0.0
        self.leaf_gap, self.level_gap = leaf_gap, level_gap
        self.root = self._build(spec, depth=0, parent=None, edge_text=None)
        self.move_to(ORIGIN)
        fit_in_safe_area(self)

    def _node(self, spec):
        if "leaf" in spec:
            color = YES if spec["leaf"].lower() == "yes" else NO
            box = RoundedRectangle(width=1.1, height=0.5, corner_radius=0.12,
                                   stroke_color=color, fill_color=color, fill_opacity=0.18)
            txt = T(spec["leaf"], size=SIZE_SMALL, color=color)
        else:
            box = RoundedRectangle(width=max(1.4, len(spec["label"]) * 0.2 + 0.5), height=0.55,
                                   corner_radius=0.12, stroke_color=ACCENT,
                                   fill_color=ACCENT, fill_opacity=0.12)
            txt = T(spec["label"], size=SIZE_SMALL, color=FG)
        return VGroup(box, txt)

    def _build(self, spec, depth, parent, edge_text):
        node = self._node(spec)
        kids = spec.get("children", [])
        child_nodes = []
        for et, cs in kids:
            child_nodes.append(self._build(cs, depth + 1, None, et))
        if child_nodes:
            x = (child_nodes[0].get_x() + child_nodes[-1].get_x()) / 2
        else:
            x = self._leaf_x
            self._leaf_x += self.leaf_gap
        node.move_to([x, -depth * self.level_gap, 0])
        self.add(node)
        for (et, _), ch in zip(kids, child_nodes):
            edge = Line(node.get_bottom(), ch.get_top(), color=MUTED, stroke_width=2)
            lab = T(et, size=SIZE_SMALL - 4, color=MUTED)
            # label edge ke bahar wali side par; seedhi (vertical) edge ho to right side, line se thoda door
            # edge ke 60% point par (child ke paas edges door-door hote hain, labels takrate nahi)
            side = LEFT if ch.get_x() < node.get_x() - 1e-3 else RIGHT
            lab.next_to(edge.point_from_proportion(0.6), side, buff=0.1)
            lab.add_background_rectangle(color=BG, opacity=0.85, buff=0.04)   # line ke upar bhi padha jaaye
            self.add(edge, lab)
            ch.edge, ch.edge_label = edge, lab
        node.child_nodes = child_nodes
        return node

    def _bfs(self):
        q, out = [self.root], []
        while q:
            n = q.pop(0)
            out.append(n)
            q.extend(n.child_nodes)
        return out

    def grow(self, lag_ratio=0.25) -> Animation:
        anims = []
        for n in self._bfs():
            parts = [FadeIn(n, shift=DOWN * 0.1)]
            if hasattr(n, "edge"):
                parts = [Create(n.edge), FadeIn(n.edge_label)] + parts
            anims.append(AnimationGroup(*parts))
        return LaggedStart(*anims, lag_ratio=lag_ratio)
```

---

## 10. `BallBox` (entropy analogy)

```python
from manim import *
from .theme import YES, NO, MUTED, T, SIZE_SMALL


class BallBox(VGroup):
    """BallBox(pos=9, neg=5, label="S")  → dabba jisme 9 green + 5 red balls (grid, deterministic)"""

    def __init__(self, pos: int, neg: int, label: str = "", cols: int = 5, r: float = 0.14, **kw):
        super().__init__(**kw)
        n = pos + neg
        rows = (n + cols - 1) // cols
        balls = VGroup()
        for i in range(n):
            color = YES if i < pos else NO
            balls.add(Circle(radius=r, fill_color=color, fill_opacity=1, stroke_width=0)
                      .move_to([(i % cols) * 2.4 * r, -(i // cols) * 2.4 * r, 0]))
        balls.move_to(ORIGIN)
        box = RoundedRectangle(width=cols * 2.4 * r + 0.3, height=rows * 2.4 * r + 0.3,
                               corner_radius=0.1, stroke_color=MUTED)
        self.balls, self.box = balls, box
        self.add(box, balls)
        if label:
            self.label = T(label, size=SIZE_SMALL, color=MUTED).next_to(box, DOWN, buff=0.15)
            self.add(self.label)
```

---

## 11. `PauseTimer` (pause-and-try)

```python
from manim import *
from .theme import T, HILITE, MUTED, SIZE_BODY, SIZE_LABEL


class PauseTimer(VGroup):
    """timer = PauseTimer(seconds=6).to_corner(DR); self.add(timer); timer.run(self)"""

    def __init__(self, seconds: int = 6, **kw):
        super().__init__(**kw)
        self.seconds = seconds
        self.ring = Circle(radius=0.55, color=HILITE, stroke_width=6)
        self.num = T(str(seconds), size=SIZE_BODY, color=HILITE).move_to(self.ring)
        self.hint = T("Pause karo, khud try karo!", size=SIZE_LABEL, color=MUTED).next_to(self.ring, LEFT, buff=0.3)
        self.add(self.ring, self.num, self.hint)

    def run(self, scene: Scene):
        for s in range(self.seconds, 0, -1):
            new = T(str(s), size=SIZE_BODY, color=HILITE).move_to(self.ring)
            scene.play(Transform(self.num, new), run_time=0.2)
            scene.wait(0.8)
```

---

## 12. Components ko AI coder tak pahunchana

Coder prompt ([21](21_AI_Se_Manim_Code_Generation.md)) mein ek **auto-generated component reference** jaata hai:

```python
# tools/component_docs.py
import inspect, video.lib.components as C

def component_reference() -> str:
    out = []
    for name in C.__all__:
        obj = getattr(C, name)
        doc = (inspect.getdoc(obj) or "").splitlines()
        sig = str(inspect.signature(obj)) if inspect.isclass(obj) else ""
        out.append(f"- {name}{sig}: {doc[0] if doc else ''}")
    return "\n".join(out)
```

Output (prompt mein jaata hai):
```
- HighlightTable(columns, rows, col_pad=0.35, ...): HighlightTable(columns, rows).to_edge(LEFT); self.play(t.highlight_rows(Outlook="Sunny"))
- BarCompare(items, max_value=None, ...): BarCompare({"Outlook": ("0.2467", 0.2467), ...}, max_value=0.3)
- TreeDiagram(spec, ...): ...
```

---

## 13. Library ko test karna

Har component ka ek **visual test scene** (`tests/test_components.py`) rakho, jo `-s` (last frame PNG) se render ho aur PNG ko "golden image" se compare kare. Library mein change ke baad test chalao, taaki purane videos ka layout na toote.

```bash
manim -s -ql tests/test_components.py TableTest TreeTest BarTest
```

> Is file ke non-LaTeX components (`HighlightTable`, `BarCompare`, `TreeDiagram`, `BallBox`, `PauseTimer`, `ResultBox.with_label`) humne manim 0.22.0 par render karke test kiye ([39](39_Verification_Log.md)).
>
> **Test mein mile layout bugs (aur fix):** Pehle version mein (1) fixed column width ki wajah se table ke lambe headers ("Temperature", "Humidity") overlap ho rahe the, isliye ab column width content se calculate hoti hai; (2) `box_rows(Outlook="Overcast")` ek hi bada box bana raha tha jo beech ki saari rows gher leta tha, isliye ab har row ka alag box banta hai; (3) bar chart mein "Temperature" label padosi se takra raha tha, isliye ab lamba label auto-shrink hota hai; (4) tree mein "Overcast" aur "Rain" edge labels takra rahe the, isliye ab labels edge ke 60% point par background ke saath lagte hain. **Yahi wajah hai ki library ko visual tests ke saath maintain karna zaroori hai.** Bina dekhe likha gaya code aksar chalta to hai, lekin dikhne mein galat hota hai. `EquationSteps` MathTex/LaTeX use karta hai; test machine par full LaTeX (`dvisvgm`) nahi tha, isliye wo render-test nahi hua. Uska API standard Manim (`MathTex`, `TransformMatchingTex`) hai.

👉 Agla: [20_Visual_Style_Guide_Colors_Fonts_Layout.md](20_Visual_Style_Guide_Colors_Fonts_Layout.md)
