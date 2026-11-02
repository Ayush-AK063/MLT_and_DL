# 06 · Script JSON Schema Reference

> **Is file mein:** `script.json` ka har field: kya hai, required hai ya nahi, example, aur validation rules. Ye poori pipeline ka **single source of truth** hai.

---

## 1. Hierarchy

```
Topic (ek video)
 └── Scene  (teaching template ka ek block: hook, intuition, worked_example ...)
      └── Beat  (1–3 sentences narration + ek visual change)
           └── (optional) bookmarks  (beat ke andar specific word par trigger)
```

---

## 2. Top-level fields

```jsonc
{
  "schema_version": "1.0",
  "lecture": 20,
  "topic_id": "T07_information_gain",
  "title": "Information Gain: Sabse Achha Sawaal Kaise Chunein",
  "source_files": [
    "lectures/Lecture 20/07_Information_Gain_Choosing_the_Best_Attribute.md",
    "lectures/Lecture 20/10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook.md"
  ],
  "language": "hinglish",              // hinglish | english
  "target_duration_min": 11,
  "prerequisites": ["L20/T06_entropy"],
  "learning_objectives": [
    "Information gain ka formula samajhna aur har term ka matlab batana",
    "Ek attribute ka gain step-by-step calculate karna",
    "Best attribute chunna (highest gain)"
  ],
  "coverage_checklist": [              // notes ke key points; script review mein tick hote hain
    "Gain formula", "Weighted average of child entropies", "Outlook gain 0.2467",
    "Comparison with Humidity/Wind/Temperature", "ID3 picks highest gain"
  ],
  "glossary": {                        // naye terms jo is topic mein introduce honge
    "subset": "data ka hissa jo ek attribute value se bana",
    "weighted average": "size ke hisaab se average"
  },
  "data": { ... },                     // tables/numbers jo scenes use karenge (section 5)
  "verify": [ ... ],                   // har number ka Python check (section 6)
  "scenes": [ ... ]                    // section 3
}
```

| Field | Required | Type | Notes |
|---|---|---|---|
| `schema_version` | ✅ | string | Schema badle to bump karo |
| `lecture` | ✅ | int | |
| `topic_id` | ✅ | string | `T{nn}_{slug}` |
| `title` | ✅ | string | Video title / intro card |
| `source_files` | ✅ | string[] | Traceability: kahan se content aaya |
| `language` | ✅ | enum | |
| `target_duration_min` | ✅ | number | Word budget ke liye (~140 wpm) |
| `prerequisites` | ⬜ | string[] | Recap scene ke liye |
| `learning_objectives` | ✅ | string[] | 2–4 items, measurable |
| `coverage_checklist` | ✅ | string[] | Script review mein har item cover hona chahiye |
| `glossary` | ⬜ | object | |
| `data` | ⬜ | object | Shared tables/values |
| `verify` | ✅ (agar numbers hain) | array | |
| `scenes` | ✅ | array | |

---

## 3. Scene fields

```jsonc
{
  "id": "s05_worked_example",
  "type": "worked_example",            // hook | recap | intuition | definition | worked_example |
                                       // compare | visualize | pause_and_try | common_mistake |
                                       // real_world | recap_summary | intro_card | outro_card
  "title": "Outlook ka Information Gain",
  "renderer": "template",              // template (⭐ budget, doc 41) | manim (custom code) | hyperframes | image_kenburns
  "layout": "table_left_math_right",   // style guide ke named layouts (doc 20)
  "components": ["HighlightTable", "EquationSteps", "ResultBox"],
  "assets": [],                        // images (generated), icons
  "music": "calm_focus",               // optional, background bed name
  "beats": [ ... ]
}
```

| Field | Required | Notes |
|---|---|---|
| `id` | ✅ | `s{nn}_{type}` |
| `type` | ✅ | Teaching template ([03](03_Pedagogy_Teaching_Design_Principles.md)) |
| `title` | ✅ | Chapter title bhi ban sakta hai |
| `renderer` | ✅ | Kaun render karega |
| `layout` | ⬜ | Named layout ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) |
| `components` | ⬜ | Coder ko hint: library ke kaun se components |
| `beats` | ✅ | ≥ 1 |

---

## 4. Beat fields (sabse important)

```jsonc
{
  "id": "b042",
  "narration": "Sunny wale din five hain. <bookmark mark='split'/>Do mein tennis khela, teen mein nahi.",
  "tts_override": null,                // agar TTS ke liye alag spelling chahiye
  "display": {
    "latex": ["\\text{Sunny}: 2^{+},\\ 3^{-}"],
    "text": [],
    "highlight": ["table.rows[Outlook=Sunny]"]
  },
  "visual": "Table ki 5 Sunny rows yellow highlight. Bookmark 'split' par '2+ / 3−' label right side mein aaye.",
  "animation_hints": ["Indicate rows", "Write label at bookmark split"],
  "numbers": ["sunny_pos", "sunny_neg"],   // verify block ke ids; screen ke numbers yahin se aate hain
  "pause_after": 0.4,
  "emphasis": false,
  "notes_for_coder": "Rows ko FadeToColor YELLOW, phir wapas normal mat karna (agle beat mein use hoga).",
  "actions": [                          // ⭐ renderer=template ke liye (doc 41): ye hi animation hai
    {"do": "highlight_rows", "table": "tbl", "where": {"Outlook": "Sunny"}},
    {"do": "wait_bookmark", "mark": "split"},
    {"do": "text", "id": "lab", "text": "Sunny: 2+ / 3−", "region": "right_narrow"}
  ]
}
```

| Field | Required | Type | Notes |
|---|---|---|---|
| `id` | ✅ | string | Topic mein unique, `b{nnn}` |
| `narration` | ✅ | string | Spoken text (Roman Hinglish). Bookmarks allowed: `<bookmark mark='name'/>` |
| `tts_override` | ⬜ | string/null | TTS ko alag text dena ho (jaise Devanagari) |
| `display.latex` | ⬜ | string[] | Screen par aane wale formulas (LaTeX) |
| `display.text` | ⬜ | string[] | Short labels (max ~6 words each) |
| `display.highlight` | ⬜ | string[] | Kya highlight karna hai (semantic reference) |
| `visual` | ✅ | string | Human-readable visual description: coder isi se code likhta hai |
| `animation_hints` | ⬜ | string[] | Manim animation suggestions |
| `numbers` | ⬜ | string[] | Is beat mein dikhne/bole jaane wale numbers ke `verify` ids |
| `pause_after` | ⬜ | number (s) | Default `config.audio.beat_gap_s` |
| `emphasis` | ⬜ | bool | Important beat: thoda zyada hold, sound cue |
| `notes_for_coder` | ⬜ | string | Extra instructions (renderer=manim) |
| `actions` | ✅ agar scene `renderer: "template"` | object[] | Visual actions ([41](41_Template_Engine_Zero_Cost_Animation.md) §2). Numbers sirf `{num:id}` se |

### Validation rules (beat level)
1. `narration` mein koi raw math symbol nahi: `Σ ≥ ≤ ∑ √ ∫ | _ ^ \` → error
2. `narration` ≤ 45 words (zyada ho to beat todo)
3. Bookmark naam regex `^\w+$` (manim-voiceover sirf word characters match karta hai: `<bookmark\s*mark\s*=['"]\w*["']\s*/>`)
4. Agar `display.latex` mein koi number hai, to wo number `numbers` ke kisi verify id se match hona chahiye
5. `visual` khaali nahi ho sakta

---

## 5. `data` block (shared tables)

Worked examples ka data ek jagah rakho, taaki scenes aur verify dono same source use karein:

```jsonc
"data": {
  "playtennis": {
    "columns": ["Day","Outlook","Temperature","Humidity","Wind","PlayTennis"],
    "rows": [
      ["D1","Sunny","Hot","High","Weak","No"],
      ["D2","Sunny","Hot","High","Strong","No"],
      ["D3","Overcast","Hot","High","Weak","Yes"],
      ["D4","Rain","Mild","High","Weak","Yes"],
      ["D5","Rain","Cool","Normal","Weak","Yes"],
      ["D6","Rain","Cool","Normal","Strong","No"],
      ["D7","Overcast","Cool","Normal","Strong","Yes"],
      ["D8","Sunny","Mild","High","Weak","No"],
      ["D9","Sunny","Cool","Normal","Weak","Yes"],
      ["D10","Rain","Mild","Normal","Weak","Yes"],
      ["D11","Sunny","Mild","Normal","Strong","Yes"],
      ["D12","Overcast","Mild","High","Strong","Yes"],
      ["D13","Overcast","Hot","Normal","Weak","Yes"],
      ["D14","Rain","Mild","High","Strong","No"]
    ]
  }
}
```

(Ye Mitchell ka classic PlayTennis dataset hai jo L20 ke worked example mein use hua hai. Exact rows lecture notes/slides se confirm karo.)

---

## 6. `verify` block (har number ka proof)

```jsonc
"verify": [
  {
    "id": "H_S",
    "display": "0.940",
    "spoken": "zero point nine four zero",
    "expr": "entropy([9,5])",
    "expected": 0.9403,
    "tolerance": 0.0005
  },
  {
    "id": "gain_outlook",
    "display": "0.2467",
    "spoken": "zero point two four six seven",
    "expr": "info_gain(data.playtennis, 'Outlook', 'PlayTennis')",
    "expected": 0.2467,
    "tolerance": 0.00005
  },
  {
    "id": "sunny_pos",
    "display": "2",
    "expr": "count(data.playtennis, Outlook='Sunny', PlayTennis='Yes')",
    "expected": 2,
    "tolerance": 0
  }
]
```

| Field | Notes |
|---|---|
| `id` | Beat `numbers` isi ko refer karte hain |
| `display` | Screen par exactly kaise dikhega (rounding yahin decide hoti hai) |
| `spoken` | Narration mein kaise bola jayega (normalize step isse cross-check karta hai) |
| `expr` | Python expression jo `verify.py` ke helper functions ke saath evaluate hota hai |
| `expected` | Script likhne wale (Claude) ne kya socha |
| `tolerance` | Kitna farak allowed hai |

**Verify step 3 cheezein check karta hai** ([08](08_Math_Verification_Step.md)):
1. `eval(expr) ≈ expected` (tolerance ke andar)
2. `display` == `expected` rounded to display precision
3. `spoken` sach mein `display` ka spoken form hai (number-to-words check)

---

## 7. Poora mini example (ek scene, 4 beats)

```json
{
  "id": "s05_worked_example",
  "type": "worked_example",
  "title": "Outlook ka Information Gain",
  "renderer": "manim",
  "layout": "table_left_math_right",
  "components": ["HighlightTable", "EquationSteps", "ResultBox"],
  "beats": [
    {
      "id": "b040",
      "narration": "Chalo ab Outlook attribute ka gain nikalte hain. Outlook ki teen values hain: Sunny, Overcast aur Rain.",
      "display": {"text": ["Outlook: Sunny | Overcast | Rain"]},
      "visual": "Left mein PlayTennis table. Outlook column header glow kare. Right side title 'Gain(S, Outlook) = ?'",
      "numbers": []
    },
    {
      "id": "b041",
      "narration": "Sunny wale din five hain. <bookmark mark='split'/>Do mein tennis khela, teen mein nahi.",
      "display": {"latex": ["\\text{Sunny}: 2^{+},\\ 3^{-}"]},
      "visual": "Sunny rows yellow. Bookmark par right side label aaye.",
      "numbers": ["sunny_total", "sunny_pos", "sunny_neg"]
    },
    {
      "id": "b042",
      "narration": "Iski entropy aati hai zero point nine seven one.",
      "display": {"latex": ["H(S_{\\text{Sunny}}) = 0.971"]},
      "visual": "Label ke neeche entropy equation Write ho, 0.971 yellow box mein.",
      "numbers": ["H_sunny"],
      "pause_after": 0.6
    },
    {
      "id": "b043",
      "narration": "Overcast ke chaar din hain, aur chaaron mein tennis khela. Bilkul pure. To entropy zero.",
      "display": {"latex": ["H(S_{\\text{Overcast}}) = 0"]},
      "visual": "Overcast rows green. Equation aaye, 0 par green tick.",
      "numbers": ["overcast_total", "H_overcast"],
      "emphasis": true
    }
  ]
}
```

---

## 8. JSON Schema (machine validation)

Pipeline `jsonschema` library se validate karegi. Core schema (short version):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["schema_version","lecture","topic_id","title","source_files",
               "language","target_duration_min","learning_objectives",
               "coverage_checklist","scenes"],
  "properties": {
    "scenes": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id","type","title","renderer","beats"],
        "properties": {
          "type": {"enum": ["hook","recap","intuition","definition","worked_example",
                            "compare","visualize","pause_and_try","common_mistake",
                            "real_world","recap_summary","intro_card","outro_card"]},
          "renderer": {"enum": ["template","manim","hyperframes","image_kenburns"]},
          "beats": {
            "type": "array", "minItems": 1,
            "items": {
              "type": "object",
              "required": ["id","narration","visual"],
              "properties": {
                "id": {"type": "string", "pattern": "^b\\d{3}$"},
                "narration": {"type": "string", "minLength": 1},
                "visual": {"type": "string", "minLength": 5},
                "pause_after": {"type": "number", "minimum": 0, "maximum": 15}
              }
            }
          }
        }
      }
    }
  }
}
```

Extra checks (custom Python, schema se bahar):
- Beat ids unique aur ascending
- Narration word count ≤ 45
- Raw math symbols narration mein nahi
- Bookmark names valid aur har bookmark scene code mein use hua
- Total words / 140 ≈ `target_duration_min` (±25%)
- Har `numbers` id `verify` mein exist karta hai
- Har `coverage_checklist` item kam se kam ek beat mein mention hua (fuzzy match + human tick)
- Template scenes: `validate_actions(script)` → `[]` ([41](41_Template_Engine_Zero_Cost_Animation.md) §5)

👉 Agla: [07_Script_Generation_Prompts_With_Claude.md](07_Script_Generation_Prompts_With_Claude.md)
