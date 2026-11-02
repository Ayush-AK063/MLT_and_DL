# 04 · Script Writing Guide: Hinglish Narration

> **Is file mein:** Narration script kaise likhein jo (1) samajh aaye, (2) TTS achhe se bole, aur (3) animation ke saath sync ho. Hinglish ke specific rules, numbers/formula bolne ke rules, aur before/after examples.

---

## 1. Seedhi baat

Script **padhne** ke liye nahi, **sunne** ke liye likhi jaati hai. Kaan aankh se alag kaam karta hai:
- Kaan wapas jaa kar "dobara nahi padh" sakta, isliye sentences chhote rakho
- Brackets, footnotes, tables bole nahi ja sakte
- Symbols (`Σ`, `≥`, `|Sv|`) ko shabdon mein likhna padta hai

---

## 2. Language decision: Hinglish ka kaun sa form?

Teen options hain, aur ye TTS model par depend karta hai ([09](09_TTS_Model_Selection_Guide.md)):

| Form | Example | Kab |
|---|---|---|
| **Roman Hinglish** | "Ab hum entropy calculate karte hain" | Agar chosen TTS Roman Hinglish achha bolta hai (bake-off se pata chalega) |
| **Devanagari + English words** | "अब हम entropy calculate करते हैं" | Kai Indic models (IndicF5, Veena) Devanagari par better hain; English technical words Latin mein rakho |
| **Simple English** | "Now let's calculate entropy" | English version ke liye (Kokoro `af_heart`) |

### Recommendation
- Script JSON mein narration **Roman Hinglish** mein likho, kyunki ye canonical form hai aur padhne/edit karne mein aasaan hai
- Agar TTS Devanagari mangta hai to ek **transliteration step** daalo jo Hindi words ko Devanagari mein badle aur English technical words ko waise hi rakhe ([14](14_Pronunciation_Text_Normalization.md))
- Bake-off ke baad final decide karo

> Research note: Ek independent Hinglish eval (harrrshall/hinglish-tts) mein patched IndicF5 ne pure-Roman, Devanagari aur mixed-script teeno par ~4.6–4.9/5 intelligibility diya, jabki Indic Parler-TTS colloquial Roman Hinglish par kamzor tha. Ye chhota (30 sentences ka), self-run eval hai, isliye apna test zaroori hai.

---

## 3. Sentence rules (TTS-friendly + ear-friendly)

| Rule | ❌ Bura | ✅ Achha |
|---|---|---|
| Ek sentence = ek idea | "Entropy jo ki disorder ka measure hai aur jise Shannon ne 1948 mein diya tha, wo log base 2 use karti hai kyunki..." | "Entropy disorder ka naap hai. Ise Claude Shannon ne diya tha. Isme log base 2 use hota hai. Kyun? Taaki answer bits mein aaye." |
| Max ~20 words per sentence | Lambe compound sentences | Chhote, punchy |
| Active voice | "Gain calculate kiya jaata hai" | "Hum gain calculate karte hain" |
| "Tum/hum" use karo | "Student ko samajhna chahiye" | "Tum dekho, yahan kya hua" |
| Screen ko refer karo | "Formula yeh hai" (screen ke bina samajh nahi aata) | "Screen par formula dekho: left side mein..." |
| Transitions | Achanak naya topic | "Ab tak humne X dekha. Ab sawaal ye hai..." |
| Brackets nahi | "Entropy (jo 0 se 1 ke beech hoti hai)" | "Entropy 0 se 1 ke beech hoti hai, do classes ke case mein." |

---

## 4. Numbers, symbols aur formulas ko bolna

TTS models numbers/symbols ko alag-alag tarah padhte hain. **Script mein hi spoken form likho**, aur screen ke liye alag `latex`/`display` field rakho.

### Numbers
| Screen | Narration mein likho | Kyun |
|---|---|---|
| `0.940` | "zero point nine four zero" | Bina normalization ke TTS "point nine hundred forty" ya "zero dot nine four zero" bol sakta hai |
| `0.2467` | "zero point two four six seven" | Har digit clear |
| `9/14` | "nine by fourteen" ya "nau bata chaudah" | Choose one style, poore video mein same |
| `14` | "fourteen" ya "chaudah" | Hinglish mein technical counts English mein zyada natural lagte hain |
| `2+, 3−` | "do positive, teen negative" | Symbols bolne layak nahi |
| `97.8%` | "ninety seven point eight percent" | |

> **Consistency rule:** Pure lecture ke liye ek style choose karo. Recommendation: **numbers English mein** ("zero point nine four zero"), baaki sentence Hinglish mein. Indian classrooms mein aise hi bolte hain.

### Symbols aur notation
| Screen | Spoken |
|---|---|
| `H(S)` | "H of S" / "S ki entropy" |
| `log₂` | "log base two" |
| `Σ` | "summation" / "sabka total" |
| `\|Sv\|` | "Sv ka size" |
| `p_i` | "p i" / "i-th class ki probability" |
| `≥` | "greater than or equal to" |
| `x̄` | "x bar" / "mean" |
| `σ` | "sigma" |
| `AUC` | "A U C" (letters alag) |
| `ROC` | "R O C" |
| `KNN` | "K N N" / "K nearest neighbours" |
| `ID3` | "I D three" |
| `PCA` | "P C A" |
| `sklearn` | "scikit learn" |

Ye mapping ek **pronunciation dictionary** mein jaati hai jo TTS se pehle automatically apply hoti hai ([14](14_Pronunciation_Text_Normalization.md)). Lekin pehla defense script mein hi hai.

### Formula ko bolne ka pattern
**Kabhi poora formula ek saans mein mat bolo.** Pattern:
1. Poora formula screen par dikhao, aur narrator bole: "Ye hai information gain ka formula."
2. Left side highlight: "Left mein Gain of S comma A, yaani attribute A se kitna faayda hua."
3. Pehla term highlight: "Pehla hissa H of S, poore data ki entropy."
4. Dusra term highlight: "Phir hum minus karte hain har subset ki weighted entropy."
5. Weight highlight: "Ye weight hai, subset ka size divide by total size."
6. Recap: "Matlab: pehle kitna confusion tha, minus baad mein kitna bacha."

Har step = alag beat = alag highlight. Ye **signaling** + **segmenting** dono hai.

---

## 5. Lecture notes se script kaise banaayein

Hamare lecture notes mein har topic ke 3 versions hain (Technical, Simple English, Hinglish). Script ke liye:

| Notes ka hissa | Script mein use |
|---|---|
| **Technical** | Facts, formulas, exact numbers ka source of truth |
| **Simple English** | Explanation ka flow, analogies |
| **Hinglish** | Tone aur phrasing ka reference |
| Worked examples / tables | `worked_example` scenes ka data |
| `[[links]]` | Recap scenes ke liye (pichhle topic ka reference) |
| "Research enrichment" | `real_world` scene ya "fun fact" |

**Important:** Notes ko seedha copy-paste mat karo. Notes padhne ke liye likhe gaye the; script sunne ke liye likhni hai. Rewrite karo.

---

## 6. Before / After examples

### Example 1: Entropy definition
❌ **Notes-style (bura narration):**
> "Entropy H(S) = −Σ pᵢ log₂ pᵢ, where pᵢ is the proportion of examples in class i; for binary classification it ranges in [0, 1]."

✅ **Script-style:**
> Beat 1: "Ab ek formula dekhte hain jo confusion ko number mein badal deta hai."
> Beat 2: "Isse entropy kehte hain. Symbol hai H of S."
> Beat 3: "Har class ke liye hum uski probability lete hain. Use p i kehte hain."
> Beat 4: "Phir p i ko multiply karte hain log base two of p i se."
> Beat 5: "Sab classes ka total lete hain, aur aage minus laga dete hain."
> Beat 6: "Minus kyun? Kyunki log of fraction negative hota hai, aur hume positive answer chahiye."
> Beat 7: "Do classes ho to entropy zero se one ke beech aati hai. Zero matlab bilkul pure, one matlab full confusion."

### Example 2: Calculation
❌ "H(S) = −(9/14)log₂(9/14) − (5/14)log₂(5/14) = 0.940"

✅
> Beat 1: "Hamare paas fourteen din hain. Nine din tennis khela, five din nahi."
> Beat 2: "To yes ki probability hai nine by fourteen, aur no ki five by fourteen."
> Beat 3: "Pehla term: nine by fourteen, times log base two of nine by fourteen. Ye aata hai minus zero point four one."
> Beat 4: "Dusra term: five by fourteen, times log base two of five by fourteen. Ye aata hai minus zero point five three."
> Beat 5: "Dono jodo aur minus lagao. Entropy aati hai zero point nine four zero."
> Beat 6: "Ye one ke kaafi paas hai. Matlab data kaafi mixed hai."

(Calculation check: (9/14)·log₂(9/14) = −0.4098, (5/14)·log₂(5/14) = −0.5305, total 0.9403 ✅. Ye [08](08_Math_Verification_Step.md) wale step mein automatically verify hota hai.)

---

## 7. Hook likhne ke formulas

| Formula | Example |
|---|---|
| **Paradox** | "Ek tree jo khud sawaal poochna seekhta hai. Kaise?" |
| **Real problem** | "Doctor ke paas 100 symptoms hain. Pehle kaun sa check kare?" |
| **Challenge** | "Is table ko dekh kar 10 second mein batao: tennis khelenge ya nahi?" |
| **Callback** | "Pichhli baar humne entropy naapi. Par usse decision kaise lein?" |
| **Surprising number** | "Ek akela tree 82% sahi. 100 trees milke 97.8%. Kaise?" (L22 ka real experiment) |

---

## 8. Recap likhne ka formula

```
"Aaj humne teen cheezein seekhi:
 Ek: [concept 1, ek line]
 Do: [concept 2, ek line]
 Teen: [concept 3, ek line]
 Agle video mein: [teaser]"
```
Max 3 points. Har point ke saath screen par ek chhota icon/visual.

---

## 9. Tone guide

- **Dost jaisa senior**, professor jaisa nahi
- Excitement real ho: "Dekho kitna interesting hai!" sirf tab bolo jab sach mein kuch interesting ho
- **Galti normal hai:** "Bahut log yahan confuse hote hain, aur wo theek hai"
- Har 4–5 beats ke baad ek chhota human touch: sawaal, mazaak, ya callback
- **Avoid:** "Simply", "obviously", "it's trivial" (beginner ko bura lagta hai)

---

## 10. Script review checklist

- [ ] Har sentence < ~20 words
- [ ] Koi raw symbol narration mein nahi (sab spoken form mein)
- [ ] Numbers ka ek hi style poore script mein
- [ ] Har beat ka ek clear visual (`visual` field khaali nahi)
- [ ] Hook pehle 30 sec mein
- [ ] Pause-and-try maujood
- [ ] Total words ≈ target duration × 140
- [ ] Har number `verify` block se match karta hai ([08](08_Math_Verification_Step.md))
- [ ] Notes ke saare key points cover hue (coverage checklist, [07](07_Script_Generation_Prompts_With_Claude.md))

👉 Agla: [05_Architecture_Pipeline_Folder_Structure.md](05_Architecture_Pipeline_Folder_Structure.md)
