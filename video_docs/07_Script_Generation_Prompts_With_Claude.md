# 07 · Script Generation: Claude ke Saath Prompts

> **Is file mein:** Lecture notes se `script.json` banwane ka exact process: kaun sa prompt, kis order mein, review kaise karein, aur aam galtiyan.

---

## 1. Kyun Claude (local LLM nahi)?

- Script likhna = pedagogy + Hinglish + maths accuracy + JSON structure, sab ek saath. Ye high-reasoning kaam hai.
- Code2Video ke README ke mutabik unke experiments mein best Manim code quality **Claude-4-Opus** se aayi thi. Script aur code dono mein strong model ka farak dikhta hai.
- Hum already Claude Code mein lecture notes banate hain, isliye same workflow continue hoga.
- Local LLM kab use karein: [30_Local_LLMs_Kab_Aur_Kaise.md](30_Local_LLMs_Kab_Aur_Kaise.md)

---

> 💰 **Budget mode:** Ye prompts **Claude Code subscription** mein chalao (jaise lecture notes banwate ho), extra paisa nahi lagta. Pass 2 mein har beat ke saath **`actions`** bhi likhwao ([41](41_Template_Engine_Zero_Cost_Animation.md) §6 ka prompt section add karo), taaki alag code-generation step na ho. Bina Claude ke: Ollama local LLM ke liye chhote, scene-by-scene prompts [42](42_Budget_Mode_Zero_Cost_Plan.md) §4 mein hain.

## 2. Teen-pass process (ek shot mein script mat banwao)

```
Pass 1: OUTLINE   → scenes + objectives + coverage checklist     → 👤 human review
Pass 2: FULL SCRIPT → har scene ke beats (narration + visual)     → automatic validation
Pass 3: CRITIQUE  → Claude khud apni script ko rubric se check kare → fix → 👤 human final OK
```

**Kyun 3 pass?** Ek baar mein 1500 words + JSON + maths banwane par structure ya coverage mein galtiyan zyada hoti hain. Outline pehle lock karne se baaki kaam focused rehta hai. TheoremExplainAgent aur Code2Video dono bhi pehle "planner" (storyboard) aur phir detail wala approach use karte hain.

---

## 3. Pass 1: Outline prompt

`video/prompts/script_prompt.md` ka pehla hissa:

```markdown
# ROLE
Tum ek expert ML teacher aur educational video scriptwriter ho (3Blue1Brown + Khan Academy style).
Audience: Indian B.Tech/M.Tech students, Hinglish comfortable, beginner-to-intermediate.

# INPUT
Neeche lecture notes hain (Technical, Simple English, Hinglish versions):
<notes>
{{TOPIC_MD_CONTENT}}
</notes>
Pichhle topic ka summary (recap ke liye):
<previous>
{{PREVIOUS_TOPIC_SUMMARY}}
</previous>

# TASK (sirf OUTLINE, abhi beats nahi)
1. 2–4 measurable learning objectives
2. coverage_checklist: notes ke saare key points (formulas, definitions, examples, numbers). Kuch bhi miss nahi hona chahiye.
3. Scenes ki list, is fixed template ke order mein:
   hook → recap → intuition → definition → worked_example → compare/visualize →
   pause_and_try → common_mistake → (real_world) → recap_summary
   Har scene ke liye: id, type, title, 1–2 line purpose, estimated seconds, kaun se coverage items.
4. Ek analogy propose karo (intuition scene ke liye) jo Indian student ki daily life se ho,
   aur batao ki analogy kahan break hoti hai.
5. Worked example: notes ka example use karo. Agar notes mein nahi hai to ek chhota example banao
   aur clearly "NEW_EXAMPLE" mark karo.
6. Target duration: {{TARGET_MIN}} min (~140 words/min).

# OUTPUT
Sirf JSON: {"learning_objectives":[], "coverage_checklist":[], "scenes":[{"id","type","title","purpose","est_seconds","covers":[]}], "analogy":{"idea","mapping","breaks_where"}}
```

### Human review (Pass 1)
- [ ] Coverage checklist mein notes ka har important point hai?
- [ ] Analogy sahi aur relatable hai?
- [ ] Duration realistic hai?
- [ ] Order logical hai?

---

## 4. Pass 2: Full script prompt

```markdown
# ROLE
(same as above)

# INPUT
Approved outline:
<outline>{{OUTLINE_JSON}}</outline>
Notes:
<notes>{{TOPIC_MD_CONTENT}}</notes>
Schema:
<schema>{{SCRIPT_SCHEMA_SUMMARY}}</schema>
Available Manim components (inhi ko prefer karo):
<components>{{COMPONENT_LIST_WITH_ONE_LINE_DOCS}}</components>
Pronunciation rules:
<pronunciation>{{PRONUNCIATION_RULES}}</pronunciation>

# HARD RULES
- Narration Roman Hinglish mein; technical terms English mein; numbers English words mein
  ("zero point nine four zero"). Poore script mein ek hi number style.
- Narration mein KOI raw symbol nahi (Σ, ≥, |S|, _, ^). Formulas ko shabdon mein bolo.
- Har beat: 1–3 sentences, max 45 words, ek visual change.
- Har sentence max ~20 words.
- Screen par narration ka poora text MAT likho (redundancy). display mein sirf formula/keywords/numbers.
- Har formula: pehle poora dikhao, phir har term alag beat mein highlight + explain.
- Har calculation step alag beat.
- Har number jo screen par ya narration mein aaye, uska verify entry banao (expr + expected + display + spoken).
- Bookmarks sirf tab jab ek beat ke andar timing zaroori ho; naam sirf [A-Za-z0-9_].
- Har scene ke liye layout aur components suggest karo.
- Tone: dost jaisa senior. "simply/obviously/trivial" mat bolo.
- Pause-and-try scene mein: sawaal → pause_after 6–8 s → solution beats.

# OUTPUT
Poora script.json (schema ke hisaab se), aur kuch nahi.
```

---

## 5. Pass 3: Self-critique prompt

```markdown
Neeche ek video script hai. Is rubric se har point ko 1–5 score do, problems list karo, phir FIXED script do.

RUBRIC
1. Coverage: coverage_checklist ka har item kisi beat mein hai?
2. Correctness: koi factual/maths galti? (verify entries ke expr dobara socho)
3. Clarity: koi symbol bina define kiye use hua?
4. Pacing: koi beat > 45 words? koi screen > 15 s bina change?
5. Redundancy: display mein narration ka poora sentence to nahi?
6. Engagement: hook pehle 30 s mein? pause_and_try hai? analogy concrete hai?
7. TTS-friendliness: raw symbols, brackets, abbreviations jo galat bole ja sakte hain?
8. Sync-readiness: har beat ka visual specific hai (coder bina guess kiye bana sake)?

OUTPUT FORMAT:
{"scores":{...}, "problems":[{"beat":"b041","issue":"...","fix":"..."}], "fixed_script":{...}}
```

---

## 6. Claude Code mein practical workflow

Claude Code session mein (jaise abhi lecture notes banate ho):

```text
User: "L20 T07 ka video script banao. Pass 1 outline dikhao."
  → Claude notes padhta hai, outline JSON deta hai, out/L20/T07/outline.json mein save karta hai
User: (review) "Analogy change karo, cricket wali use karo. Baaki OK."
  → Claude updates
User: "Pass 2 + Pass 3 karo."
  → script.json banta hai, validation chalti hai (python -m video.lib.validate)
  → verify chalta hai (python build_video.py L20 T07 --stage verify)
  → koi fail ho to Claude fix karta hai
User: (final read) "OK, TTS stage chalao."
```

### Automation option: Claude API / Agent SDK
Jab 22 lectures batch mein karne hon, to ye passes script se chal sakte hain (Claude API ya Claude Agent SDK). Lekin **pehle 3–5 topics manually Claude Code mein karo**, taaki prompts tune ho jaayein.

---

## 7. Common galtiyan aur fixes

| Galti | Example | Prompt fix |
|---|---|---|
| Notes copy-paste | Narration mein "where pᵢ is the proportion..." | "Notes padhne ke liye the; script sunne ke liye. Rewrite karo." |
| Symbols narration mein | "H(S) = 0.940 hai" | Hard rule + validator |
| Ek beat mein 3 calculations | | "Har arithmetic step alag beat" |
| Display mein lamba text | "Entropy is a measure of disorder in data" screen par | "display.text max 6 words" |
| Numbers ki rounding inconsistent | 0.94 kahin, 0.940 kahin | verify `display` hi canonical; validator check |
| Analogy galat mapping | "Entropy = temperature" (misleading) | Pass 1 human review |
| Hinglish mein formal Hindi | "Hum soochna labh ki ganana karenge" | "Hindi shabd wahi jo Indian classroom mein bole jaate hain; technical terms English mein" |
| Vague visual | "Show the formula" | "visual itna specific ho ki coder bina guess kiye bana sake: kya, kahan, kaunsa color, kab" |

---

## 8. Outline ka example (L20 · T07 Information Gain)

```json
{
  "learning_objectives": [
    "Information gain formula ke har term ka matlab batana",
    "Outlook attribute ka gain 0.2467 step-by-step nikalna",
    "Samajhna ki ID3 highest-gain attribute ko root banata hai"
  ],
  "coverage_checklist": [
    "Gain(S,A) = H(S) − Σ (|Sv|/|S|) H(Sv)",
    "Weighted average kyun (bade subset ka zyada asar)",
    "H(S) = 0.940 recap",
    "Sunny 2+/3− H=0.971; Overcast 4+/0− H=0; Rain 3+/2− H=0.971",
    "Weighted sum = 0.6935; Gain(Outlook)=0.2467",
    "Humidity 0.1518, Wind 0.0481, Temperature 0.0292",
    "Outlook root banta hai"
  ],
  "scenes": [
    {"id":"s01_hook","type":"hook","title":"Pehla sawaal kaunsa?","est_seconds":30},
    {"id":"s02_recap","type":"recap","title":"Entropy: 10 second recap","est_seconds":30},
    {"id":"s03_intuition","type":"intuition","title":"Kamra saaf karna","est_seconds":90},
    {"id":"s04_definition","type":"definition","title":"Gain ka formula","est_seconds":100},
    {"id":"s05_worked_example","type":"worked_example","title":"Outlook ka gain","est_seconds":200},
    {"id":"s06_compare","type":"compare","title":"Kaun jeeta?","est_seconds":60},
    {"id":"s07_pause_and_try","type":"pause_and_try","title":"Wind ka gain tum nikalo","est_seconds":60},
    {"id":"s08_common_mistake","type":"common_mistake","title":"Weight bhoolna","est_seconds":40},
    {"id":"s09_recap_summary","type":"recap_summary","title":"Aaj kya seekha","est_seconds":30}
  ],
  "analogy": {
    "idea": "Mixed laal-neeli balls ka bada dabba; ek sawaal (jaise 'Outlook kya hai?') se 3 chhote dabbe bante hain",
    "mapping": "Dabba = dataset, balls ka color = class, dabba kitna mixed = entropy, sawaal ke baad kitna 'sorted' hua = gain",
    "breaks_where": "Real data mein attributes ke beech correlation hota hai; analogy ek time par ek hi sawaal dikhati hai"
  }
}
```

(Sab numbers [08](08_Math_Verification_Step.md) mein Python se verify kiye gaye: H(S)=0.9403, Outlook gain=0.2467, Humidity=0.1518, Wind=0.0481, Temperature=0.0292.)

👉 Agla: [08_Math_Verification_Step.md](08_Math_Verification_Step.md)
