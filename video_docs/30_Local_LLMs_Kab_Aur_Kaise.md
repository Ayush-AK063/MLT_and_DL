# 30 · Local LLMs: Kab Use Karein, Kab Claude

> **Is file mein:** High-end PC par local LLM chalane ka honest assessment: kaun se kaam local model achha karega, kaun se Claude ko dene chahiye, options (Ollama, llama.cpp, vLLM), aur hybrid setup.

---

## 1. Seedhi baat (honest)

Local LLMs bahut improve hue hain, lekin hamare pipeline ke **sabse mushkil kaam** (pedagogically achhi Hinglish script + bug-free Manim code + maths reasoning) mein frontier models (Claude) abhi bhi clearly aage hain.
- Code2Video ke README ke mutabik unke experiments mein best Manim code **Claude-4-Opus** se aaya tha
- Galat script ya buggy code ka matlab hai zyada fix-loops, zyada human time, aur kharab videos

**Recommendation:** Creative/reasoning kaam **Claude** ko do. Local LLM ko **high-volume, low-risk** kaam do.

---

## 2. Task-wise decision

| Task | Local LLM | Claude | Kyun |
|---|---|---|---|
| Script outline + full script | ❌ | ✅ | Pedagogy + Hinglish + accuracy |
| Self-critique of script | ⚠️ ok-ish | ✅ | |
| Manim code generation | ⚠️ (golden examples ke saath try kar sakte ho) | ✅ | Code quality aur fix-loop count |
| Code error fix (simple tracebacks) | ✅ | ✅ | Simple errors local bhi fix kar leta hai |
| Vision critic (frames) | ⚠️ (local VLMs available hain, quality check karo) | ✅ | |
| Pronunciation dictionary suggestions | ✅ | ✅ | Simple task |
| Transliteration helper / text cleanup | ✅ | | Bulk, cheap |
| YouTube title/description drafts | ✅ | ✅ | Low risk |
| Quiz MCQ generation (learner test) | ✅ (review karo) | ✅ | |
| Captions cleanup (digits wapas lana) | ✅ (ya rule-based) | | Bulk |

---

## 3. Local LLM options

| Tool | Kya | Kab |
|---|---|---|
| **Ollama** | Easiest. `ollama run <model>`, OpenAI-compatible API on `localhost:11434` | Shuruaat ke liye ✅ |
| **llama.cpp** (`llama-server`) | Fast, GGUF quantized models, full control | Solo use, max speed |
| **LM Studio** | GUI + local server | GUI pasand ho to |
| **vLLM** | High-throughput serving (batching) | Bahut saari parallel requests |

### 24 GB VRAM par kya chalta hai (rough guide, 2026 sources se)
- ~30B-class models **4-bit quantization (Q4)** mein comfortably fit hote hain (weights ~19 GB + context ke liye KV cache)
- 70B dense models sirf bahut aggressive quantization (sub-3-bit) mein, aur quality loss ke saath
- Coding ke liye sources aam taur par **Qwen-Coder family** ke ~30B-class models ya Devstral jaise models suggest karte hain

> ⚠️ Model names/sizes tezi se badalte hain. Pull karne se pehle Ollama library par exact tag check karo. Ek source ne "Qwen3-Coder 32B" likha tha jo official sizes (30B-A3B / 480B-A35B) se match nahi karta, isliye blog posts par blindly bharosa mat karo.

---

## 3a. 🍎 MacBook (64 GB unified memory) par

- **Ollama** (`.dmg`, macOS 14+) ya **LM Studio** (MLX models) ya **mlx-lm**
- **`qwen3-coder:30b`**: 19 GB, 30.5B total / 3.3B active (MoE), 256K context, **Apache-2.0**, non-thinking mode only (model card). MoE hone se Mac par fast chalta hai
- Script/actions JSON ke liye 30B-class general instruct (Qwen3 30B-A3B family) bhi achha option hai
- 64 GB mein LLM (~20 GB) + baaki kaam fit ho jaata hai, lekin LLM, TTS aur render ek saath mat chalao ([40](40_Mac_Apple_Silicon_Setup.md) §9)
- 8 GB Mac par 30B nahi chalega (max ~3–4B class). Wahan Claude subscription use karo

**Budget mode mein local LLM ka role badal jaata hai:** Template engine ([41](41_Template_Engine_Zero_Cost_Animation.md)) ki wajah se LLM ko Manim code nahi likhna, sirf **script + actions JSON** likhna hai. Ye local 30B models ke liye kaafi aasaan kaam hai, aur validator galtiyan pakad leta hai. Prompts: [42](42_Budget_Mode_Zero_Cost_Plan.md) §4.

---

## 4. Hybrid setup (recommended)

```
                    ┌─────────────────────────────┐
                    │  Claude (Claude Code / API)  │  ← script, code, critic
                    └──────────────┬──────────────┘
                                   │
pipeline (build_video.py) ─────────┤
                                   │
                    ┌──────────────┴──────────────┐
                    │  Local (Ollama, localhost)   │  ← bulk text tasks, simple fixes
                    └─────────────────────────────┘
```

Pipeline mein ek **LLM router**:
```python
# video/lib/llm.py
import requests

def local_llm(prompt: str, model: str = "qwen-coder-local", temperature: float = 0.2) -> str:
    """Ollama ka OpenAI-compatible endpoint."""
    r = requests.post("http://localhost:11434/v1/chat/completions", json={
        "model": model, "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }, timeout=600)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

ROUTES = {
    "script": "claude", "coder": "claude", "critic": "claude",
    "simple_fix": "local", "titles": "local", "pronunciation": "local", "captions": "local",
}
```

---

## 5. Agar sab local hi karna hai (privacy/cost)

Possible hai, lekin expect karo:
- Zyada fix-loop rounds (code errors)
- Script quality ke liye zyada human editing
- Component library aur golden examples **aur bhi zyada important** ho jaate hain (local model examples copy karne mein achha hai, khud se design karne mein kam)

Tips:
- Temperature low (0.1–0.3) for code
- Bahut specific prompts + golden example
- Har scene chhota rakho (kam beats)
- Static checks aur layout audit ko strict rakho

---

## 6. Cost perspective

- Claude: per-token cost; ek topic (script 3 passes + ~10 scenes code + fixes + critic) ke liye tokens hazaron se laakhon tak ja sakte hain (critic images ke saath zyada)
- Local: bijli + time; marginal cost kam
- **Real cost = human time.** Agar local model se 2× zyada fix karna pade to wo mehenga hai

> Exact token usage pilot mein naapo (Claude Code `/cost` ya API usage) aur yahan likho, taaki 22 lectures ka budget estimate ho sake.

👉 Agla: [31_Avatar_Talking_Head_Optional.md](31_Avatar_Talking_Head_Optional.md)
