# 08 · Math Verification Step

> **Is file mein:** Video ka har number Python se kaise verify hota hai: kyun zaroori hai, `verify.py` ka design, helper functions, example output, aur special cases (rounding, slides ki galtiyan).

---

## 1. Kyun? (seedhi baat)

LLM maths mein confident galtiyan karte hain. Ek galat number wala educational video **galat cheez sikhata hai**, aur log usse yaad kar lete hain.

Hamare lecture-notes ke kaam mein pehle bhi ye hua hai:
- L20 ki slides mein Gain(S, Outlook) = **0.2464** likha tha, jabki exact value **0.2467** hai (intermediate rounding ki wajah se)
- L19 ka AUC 0.76 humne khud compute karke confirm kiya

Isliye rule hai: **Video mein koi number tab tak nahi jaayega jab tak Python use calculate karke match na kare.**

---

## 2. Flow

```
script.json.verify[]  ──►  verify.py  ──►  verify_report.json
                              │
                              ├─ eval(expr) using helpers
                              ├─ compare with expected (tolerance)
                              ├─ check display rounding
                              └─ check spoken form == number_to_words(display)
                                        │
                          FAIL? ──► pipeline STOP + kaunsa id, expected vs actual
```

---

## 3. Helper library (`video/lib/verify.py`)

```python
"""Math verification helpers for script.json `verify` blocks."""
from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction


# ---------- basic info theory ----------
def entropy(counts: list[int], base: float = 2) -> float:
    """H = -Σ p log p over non-zero counts."""
    total = sum(counts)
    # max(0.0, ...) taaki pure set par -0.0 na aaye (warna display check "-0" != "0" fail hota hai)
    return max(0.0, -sum((c / total) * math.log(c / total, base) for c in counts if c))


def gini(counts: list[int]) -> float:
    total = sum(counts)
    return 1 - sum((c / total) ** 2 for c in counts)


# ---------- table helpers (data blocks from script.json) ----------
class Table:
    def __init__(self, block: dict):
        self.cols = block["columns"]
        self.rows = [dict(zip(self.cols, r)) for r in block["rows"]]

    def where(self, **cond) -> "Table":
        t = Table({"columns": self.cols, "rows": []})
        t.rows = [r for r in self.rows if all(r[k] == v for k, v in cond.items())]
        return t

    def counts(self, target: str) -> list[int]:
        return list(Counter(r[target] for r in self.rows).values())

    def __len__(self):
        return len(self.rows)


def count(table: Table, **cond) -> int:
    return len(table.where(**cond))


def info_gain(table: Table, attr: str, target: str) -> float:
    total = len(table)
    h_parent = entropy(table.counts(target))
    remainder = 0.0
    for value in sorted({r[attr] for r in table.rows}):
        sub = table.where(**{attr: value})
        remainder += len(sub) / total * entropy(sub.counts(target))
    return h_parent - remainder


# ---------- metrics ----------
def precision(tp, fp): return tp / (tp + fp)
def recall(tp, fn): return tp / (tp + fn)
def f1(p, r): return 2 * p * r / (p + r)
def accuracy(tp, tn, fp, fn): return (tp + tn) / (tp + tn + fp + fn)


def auc_from_scores(y_true: list[int], scores: list[float]) -> float:
    from sklearn.metrics import roc_auc_score
    return float(roc_auc_score(y_true, scores))


# ---------- distances ----------
def euclidean(a, b): return math.dist(a, b)
def manhattan(a, b): return sum(abs(x - y) for x, y in zip(a, b))
def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.hypot(*a) * math.hypot(*b))
def jaccard(a: set, b: set): return len(a & b) / len(a | b)


# ---------- safe evaluation ----------
SAFE_NAMES = {k: v for k, v in globals().items() if not k.startswith("_")}
SAFE_NAMES.update({"math": math, "Fraction": Fraction, "abs": abs,
                   "round": round, "sum": sum, "min": min, "max": max})


def evaluate(expr: str, data_tables: dict) -> float:
    env = dict(SAFE_NAMES)
    env["data"] = type("D", (), {k: Table(v) for k, v in data_tables.items()})
    return eval(expr, {"__builtins__": {}}, env)   # expr hamari apni script.json se aata hai
```

> Security note: `expr` hamari apni generated script se aata hai, bahar ke kisi user se nahi. Phir bhi `__builtins__` khaali rakha hai taaki galti se file/OS calls na chalein.

---

## 4. Checks

```python
def check_entry(entry: dict, data_tables: dict) -> dict:
    actual = evaluate(entry["expr"], data_tables)
    ok_value = abs(actual - entry["expected"]) <= entry.get("tolerance", 1e-4)

    # display rounding check: display ke decimals tak round karke compare
    disp = entry.get("display")
    ok_display = True
    if disp is not None:
        decimals = len(disp.split(".")[1]) if "." in disp else 0
        ok_display = f"{actual:.{decimals}f}" == disp

    # spoken check (agar diya hai)
    ok_spoken = True
    if "spoken" in entry and disp is not None:
        ok_spoken = normalize_spoken(entry["spoken"]) == normalize_spoken(number_to_words(disp))

    return {"id": entry["id"], "actual": actual, "expected": entry["expected"],
            "ok": ok_value and ok_display and ok_spoken,
            "ok_value": ok_value, "ok_display": ok_display, "ok_spoken": ok_spoken}
```

`number_to_words("0.940")` → `"zero point nine four zero"` (digit-by-digit after the decimal point). Implementation [14](14_Pronunciation_Text_Normalization.md) mein hai.

---

## 5. Example: L20 Information Gain ka verify report

Asli output (Python se chala kar dekha, 2026-10-18):

| id | expr | actual | display | status |
|---|---|---|---|---|
| H_S | `entropy([9,5])` | 0.940286 | 0.940 | ✅ |
| H_sunny | `entropy([2,3])` | 0.970951 | 0.971 | ✅ |
| H_overcast | `entropy([4])` | 0.0 | 0 | ✅ |
| H_rain | `entropy([3,2])` | 0.970951 | 0.971 | ✅ |
| rem_outlook | weighted sum | 0.693536 | 0.6935 | ✅ |
| gain_outlook | `info_gain(..,'Outlook',..)` | 0.246750 | 0.2467 | ✅ |
| gain_humidity | | 0.151836 | 0.1518 | ✅ |
| gain_wind | | 0.048127 | 0.0481 | ✅ |
| gain_temperature | | 0.029223 | 0.0292 | ✅ |
| H_high (Humidity) | `entropy([3,4])` | 0.985228 | 0.985 | ✅ |
| H_normal (Humidity) | `entropy([6,1])` | 0.591673 | 0.592 | ✅ |

### Slide vs exact ka case
Slide par **0.2464** likha hai, jabki exact value **0.2467** hai (full precision: 0.246750). Ye farak intermediate values ko round karke aage calculate karne se aata hai. Jaise 0.9403 − 0.6939 = 0.2464, jabki exact remainder 0.693536 hai. Video mein kya karein?

**Rule:** Video mein **exact value** dikhao, aur agar students slides se compare karenge to ek chhota note do:
> "Slides par aapko 0.2464 dikhega. Wo rounded values se calculate hua hai. Exact value 0.2467 hai. Dono ka matlab same hai."

Ye `common_mistake` ya ek chhote "note" beat mein jaata hai. Students confuse nahi honge, aur unhe rounding ka lesson bhi milega.

---

## 6. Special cases

| Case | Kaise handle |
|---|---|
| **Intermediate rounding** | Video mein dikhaye gaye intermediate values (0.971) se agar next step calculate karein to answer exact se thoda alag aa sakta hai. Do options: (a) intermediate ko zyada decimals mein dikhao, (b) narration mein bolo "approximately". Verify mein dono values check karo |
| **Random experiments** (jaise L22 ka sklearn digits: tree 82.0% vs RF 97.8%) | `random_state` fix karo; verify mein actual experiment code chalao; version note karo (sklearn version change se thoda farak aa sakta hai) |
| **Approximations** (log values, √) | Tolerance badhao, display precision clearly decide karo |
| **Notes mein galti mili** | Pipeline fail hogi. Lecture notes bhi fix karo (site + chatbot data rebuild), aur video mein correct value |
| **Symbolic results** (derivatives, matrix ops) | `sympy` se: `expr: "sympy.simplify(...) == ..."` boolean check |
| **Graphs/plots** | Plot ka data bhi verify se aaye (jaise ROC points list) |

---

## 6a. Budget mode: verify block Python hi banaye

Local LLM maths mein aur bhi zyada galti kar sakta hai. Isliye budget mode mein ulta flow rakho: **Python numbers compute karke verify block khud generate kare**, aur LLM ko sirf ready ids + display strings diye jaayein (wo actions mein `{num:id}` likhta hai):

```python
def build_verify(data_tables: dict, specs: list[dict]) -> list[dict]:
    """specs: [{"id":"gain_outlook","expr":"info_gain(data.playtennis,'Outlook','PlayTennis')","decimals":4}]"""
    out = []
    for s in specs:
        val = evaluate(s["expr"], data_tables)
        disp = f"{val:.{s['decimals']}f}" if s.get("decimals") is not None else str(val)
        out.append({"id": s["id"], "expr": s["expr"], "expected": val, "display": disp,
                    "spoken": number_to_words(disp), "tolerance": 0})
    return out
```
`specs` ek baar topic ke worked example se banti hai (kaun se numbers chahiye). Ye kaam tum ya Claude subscription kar sakte ho. Values hamesha Python se aati hain.

## 7. Plots ke numbers bhi verified hon

Agar video mein ROC curve, bar chart, ya scatter plot hai, to plot ka data **script.json ke data block se** aana chahiye, Manim code mein hardcoded nahi. Coder ko instruction:

```text
Plot ke saare data points `script.data.<name>` se lo. Koi number code mein hardcode mat karo.
Beat ke numbers `verify[id].display` se lo (string), taaki screen par wahi dikhe jo verify hua.
```

Isse "verified number" aur "screen ka number" ek hi source se aate hain.

---

## 8. Checklist

- [ ] Har `display.latex` ka har number kisi `verify` id se aata hai
- [ ] `verify_report.json` mein 0 failures
- [ ] Slide/notes se koi mismatch ho to note beat add hua
- [ ] Random experiments ka seed aur library version manifest mein likha hai
- [ ] Plots ka data `data` block se aata hai

👉 Agla: [09_TTS_Model_Selection_Guide.md](09_TTS_Model_Selection_Guide.md)
