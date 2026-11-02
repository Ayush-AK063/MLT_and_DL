# 14 · Pronunciation aur Text Normalization

> **Is file mein:** Script ke text ko TTS ke liye "bolne layak" banana: numbers → words, abbreviations, technical terms, pronunciation dictionary, transliteration (Roman → Devanagari), aur poora normalization pipeline code.

---

## 1. Seedhi baat

TTS model ko jo text milta hai, wo usse "padh" kar bolta hai. Agar text mein `0.940`, `AUC`, `sklearn`, `H(S)` likha hai, to model inhe galat bol sakta hai:
- `0.940` → "zero dot nine hundred forty"
- `AUC` → "awk"
- `sklearn` → "s-klern"

**Normalization** = TTS se pehle text ko exact spoken form mein badalna.

---

## 2. Teen layers of defense

```
Layer 1: Script mein hi spoken form likho          (Claude ko rule: doc 04)
Layer 2: Pronunciation dictionary auto-replace      (pronunciation.yaml)
Layer 3: Validator: koi digit/symbol bacha to ERROR (TTS se pehle)
```

---

## 3. Pronunciation dictionary (`video/pronunciation.yaml`)

```yaml
# Format: written form -> spoken form
# Case-sensitive keys; word-boundary match hota hai.
abbreviations:
  AUC: "A U C"
  ROC: "R O C"
  KNN: "K N N"
  k-NN: "K N N"
  ID3: "I D three"
  C4.5: "C four point five"
  CART: "cart"
  PCA: "P C A"
  SVD: "S V D"
  LDA: "L D A"
  SVM: "S V M"
  MLT: "M L T"
  ML: "M L"
  AI: "A I"
  TP: "true positive"
  FP: "false positive"
  TN: "true negative"
  FN: "false negative"
  TPR: "true positive rate"
  FPR: "false positive rate"
  F1: "F one"
  RF: "random forest"
  GPU: "G P U"

terms:
  sklearn: "scikit learn"
  scikit-learn: "scikit learn"
  NumPy: "num pie"
  numpy: "num pie"
  pandas: "pandas"
  matplotlib: "mat plot lib"
  Iris: "eye-ris"            # model par depend; bake-off mein check karo
  setosa: "seh-toe-sa"
  versicolor: "versi-color"
  virginica: "vir-jini-ka"
  Quinlan: "Quin-lan"
  Shannon: "Shannon"
  bootstrap: "boot strap"
  hyperparameter: "hyper parameter"
  log2: "log base two"
  log₂: "log base two"

symbols:
  "≥": " greater than or equal to "
  "≤": " less than or equal to "
  "≠": " not equal to "
  "≈": " approximately "
  "→": " "
  "%": " percent"
  "×": " times "
  "÷": " divided by "
  "σ": " sigma "
  "μ": " mu "
  "λ": " lambda "
  "θ": " theta "
  "α": " alpha "
  "β": " beta "
  "Σ": " summation "
  "π": " pi "
```

> **Phonetic spellings model-specific hain.** Kokoro ke liye "eye-ris" kaam kar sakta hai, IndicF5 ke liye "आइरिस" better ho sakta hai. Har model ke liye alag override section rakh sakte ho:
> ```yaml
> overrides:
>   indicf5:
>     Iris: "आइरिस"
> ```

---

## 4. Numbers → words

### Rules
| Input | Output | Rule |
|---|---|---|
| `0.940` | "zero point nine four zero" | Decimal ke baad har digit alag |
| `0.2467` | "zero point two four six seven" | |
| `14` | "fourteen" | Integers normal words mein |
| `97.8%` | "ninety seven point eight percent" | |
| `9/14` | "nine by fourteen" | Fraction style config se: "by" / "over" / "divided by" |
| `2+` | "two positive" | Context-specific (script mein hi likho) |
| `1948` | "nineteen forty eight" | Years ka special case (context se pata chalta hai, isliye script mein hi likho) |
| `−0.41` | "minus zero point four one" | |
| `10^5` | "ten to the power five" | |

### Code (`video/lib/normalize.py`)

```python
import re

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen " \
       "fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
DIGITS = "zero one two three four five six seven eight nine".split()


def int_to_words(n: int) -> str:
    if n < 0:
        return "minus " + int_to_words(-n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000:
        rest = n % 100
        return ONES[n // 100] + " hundred" + ("" if rest == 0 else " " + int_to_words(rest))
    for div, word in ((10**9, "billion"), (10**6, "million"), (1000, "thousand")):
        if n >= div:
            rest = n % div
            return int_to_words(n // div) + f" {word}" + ("" if rest == 0 else " " + int_to_words(rest))
    raise ValueError(n)


def number_to_words(s: str) -> str:
    """'0.940' -> 'zero point nine four zero', '-12.5' -> 'minus twelve point five'."""
    s = s.replace("−", "-").replace(",", "")
    neg = s.startswith("-")
    s = s.lstrip("-+")
    if "." in s:
        whole, frac = s.split(".", 1)
        out = int_to_words(int(whole or "0")) + " point " + " ".join(DIGITS[int(d)] for d in frac)
    else:
        out = int_to_words(int(s))
    return ("minus " if neg else "") + out


NUM_RE = re.compile(r"(?<![\w.])[-−]?\d+(?:\.\d+)?%?(?![\w.])")


def replace_numbers(text: str) -> str:
    def _sub(m):
        tok = m.group(0)
        pct = tok.endswith("%")
        words = number_to_words(tok.rstrip("%"))
        return words + (" percent" if pct else "")
    return NUM_RE.sub(_sub, text)


def normalize_spoken(s: str) -> str:
    """Comparison ke liye: lowercase, extra spaces/punctuation hatao."""
    return " ".join(re.sub(r"[^\w\s]", " ", s.lower()).split())
```

Test:
```python
assert number_to_words("0.940") == "zero point nine four zero"
assert number_to_words("97.8") == "ninety seven point eight"
assert number_to_words("14") == "fourteen"
assert replace_numbers("Accuracy 97.8% hai") == "Accuracy ninety seven point eight percent hai"
```

---

## 5. Abbreviation/term replacement

```python
import yaml

def load_dict(path="video/pronunciation.yaml", backend=None):
    d = yaml.safe_load(open(path, encoding="utf-8"))
    mapping = {}
    for section in ("abbreviations", "terms"):
        mapping.update(d.get(section, {}))
    if backend and backend in d.get("overrides", {}):
        mapping.update(d["overrides"][backend])
    return mapping, d.get("symbols", {})


def apply_dict(text: str, mapping: dict, symbols: dict) -> str:
    # Lambe keys pehle (taaki "scikit-learn" pehle match ho, "learn" baad mein)
    for k in sorted(mapping, key=len, reverse=True):
        text = re.sub(rf"(?<![\w]){re.escape(k)}(?![\w])", mapping[k], text)
    for k, v in symbols.items():
        text = text.replace(k, v)
    return " ".join(text.split())
```

---

## 6. Transliteration: Roman Hinglish → Devanagari (agar model ko chahiye)

Kuch models (IndicF5 unpatched, Kokoro Hindi voices, Veena) Devanagari input par better ho sakte hain. Lekin hamari script Roman mein hai. Solution: **sirf Hindi words ko Devanagari mein badlo, English technical words ko Latin mein rehne do.**

### Challenge
"karte" Hindi hai (→ करते), lekin "entropy" English hai (→ entropy). Machine ko kaise pata chalega?

### Approach
1. **English word list:** Ek list jisme saare technical terms + common English words hon (`terms_en.txt`: entropy, gain, attribute, tree, dataset, ...). Script ke `glossary` aur pronunciation dict se auto-build karo
2. **Baaki words → transliteration model:** AI4Bharat ka **IndicXlit** (Roman → Indic script; Apache-2.0) ya `indic-transliteration` library (rule-based schemes like ITRANS; colloquial Roman spelling ke liye less accurate)
3. **Manual overrides:** Common words jo galat transliterate hote hain (`hai` → है, `hain` → हैं, `nahi` → नहीं)

```python
COMMON = {"hai": "है", "hain": "हैं", "nahi": "नहीं", "aur": "और", "ka": "का", "ki": "की",
          "ke": "के", "ko": "को", "se": "से", "mein": "में", "ye": "ये", "wo": "वो",
          "hum": "हम", "tum": "तुम", "ab": "अब", "ek": "एक", "do": "दो", "teen": "तीन",
          "karte": "करते", "dekhte": "देखते", "aata": "आता", "aati": "आती", "chalo": "चलो"}

def to_mixed_script(text: str, english_terms: set[str], xlit) -> str:
    out = []
    for tok in re.findall(r"\w+|[^\w\s]", text):
        low = tok.lower()
        if low in english_terms or not tok.isalpha():
            out.append(tok)
        elif low in COMMON:
            out.append(COMMON[low])
        else:
            out.append(xlit(tok))          # IndicXlit ya fallback
    return re.sub(r"\s+([।,.!?])", r"\1", " ".join(out))
```

> ⚠️ Ambiguity: "do" Hindi mein "दो" (two/give) hai, lekin English "do" bhi hai. Context-based decisions mushkil hain. Isliye **Layer 1 (script mein clear likhna)** sabse important hai, aur bake-off mein dono forms (Roman vs mixed) test karo. Jo model Roman hi achha bole, uske liye transliteration ki zaroorat hi nahi.

---

## 7. Validator (TTS se pehle last check)

```python
BAD = re.compile(r"[\d=^_\\|{}<>Σ∑√∫≥≤≠≈×÷]")

def validate_tts_text(beat_id: str, text: str) -> None:
    clean = re.sub(r"<bookmark\s*mark\s*=['\"]\w*['\"]\s*/>", "", text)   # bookmarks allowed
    m = BAD.search(clean)
    if m:
        raise ValueError(f"{beat_id}: TTS text mein unspoken symbol '{m.group(0)}' bacha: {clean!r}")
```

---

## 8. Poora normalization pipeline

```python
def normalize_for_tts(beat: dict, backend: str, mapping, symbols, english_terms, xlit, form: str) -> str:
    text = beat.get("tts_override") or beat["narration"]
    text = apply_dict(text, mapping, symbols)     # abbreviations, terms, symbols
    text = replace_numbers(text)                  # bacha hua koi digit
    if form == "devanagari_mixed":
        text = to_mixed_script(text, english_terms, xlit)
    validate_tts_text(beat["id"], text)
    return text
```

> **Bookmarks ka dhyan:** manim-voiceover bookmarks (`<bookmark mark='X'/>`) ko narration mein rakhta hai aur TTS ko bhejne se pehle khud hata deta hai (`remove_bookmarks`). Lekin agar tum audio pehle se bana rahe ho ("pre-baked", [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md)), to TTS ko bhejne se pehle bookmarks **tum khud hatao**, aur word alignment ke liye unki character positions yaad rakho.

---

## 9. Pronunciation QA loop

1. Har naye lecture ke script mein naye technical words dhundho (glossary + capitalized words + English words not in dictionary)
2. Unka chhota test audio banao: "Aaj hum {word} ke baare mein seekhenge."
3. Suno, aur galat ho to `pronunciation.yaml` mein add karo
4. Dictionary har lecture ke saath badhti jaayegi, aur baad ke lectures mein kaam kam hota jayega

👉 Agla: [15_Audio_Post_Processing_Loudness_Music.md](15_Audio_Post_Processing_Loudness_Music.md)
