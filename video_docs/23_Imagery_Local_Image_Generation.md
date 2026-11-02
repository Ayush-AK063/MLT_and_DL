# 23 · Imagery: Local Image Generation (Analogies ke Liye)

> **Is file mein:** Analogy/real-world scenes ke liye illustrations kaise banayein (local image models), kaun sa model (license ke saath), prompt style, consistency, Manim mein use karna (Ken Burns), aur kya kabhi nahi karna.

---

## 1. Kab image chahiye, kab nahi

| Situation | Use | Kyun |
|---|---|---|
| Formula, table, graph, tree, numbers | ❌ Image nahi, **Manim** | Exact aur sahi hona chahiye |
| Analogy ("doctor ke sawaal", "cricket match", "kirana dukaan") | ✅ Illustration | Emotion aur context |
| Real-world application ("hospital diagnosis", "bank fraud") | ✅ Illustration | Relatability |
| Hook ka mood set karna | ✅ (optional) | Curiosity |
| Diagram jisme labels/text ho | ❌ AI image nahi | AI text bigaadta hai; labels Manim se overlay karo |

**Golden rule:** 🚫 **AI-generated image mein koi text, number ya formula nahi.** Agar label chahiye to image ke upar Manim `Text` overlay karo.

---

## 2. Model options (local, 2026)

| Model | License | Text-in-image | Notes |
|---|---|---|---|
| **FLUX.1 [schnell]** | **Apache-2.0** ✅ | Moderate | Fast (few steps); commercial OK |
| FLUX.1 [dev] | Non-commercial | Achha | ❌ Agar monetize karna hai |
| **FLUX.2 [klein] 4B** | Apache-2.0 (reported) | – | ⚠️ klein-9B non-commercial reported. Model card check karo |
| **Qwen-Image** (20B MMDiT) | **Apache-2.0** ✅ | Strong (English/Chinese) | ComfyUI native support; quantized variants (FP8 etc.) |
| SDXL | CreativeML OpenRAIL++-M | Kamzor | Purana lekin bada ecosystem (LoRAs) |

> Licenses 2026-10-18 ko check kiye (secondary sources + Wikipedia). FLUX.2 variants ke licenses size ke hisaab se alag reported hain. **Download karne se pehle Hugging Face model card ka license field padho** ([38](38_Licenses_Legal_Ethics.md)).

### Recommendation
- **Default:** FLUX.1 schnell (fast, Apache-2.0) ya Qwen-Image (agar quality chahiye aur GPU bada hai)
- **Tool:** **ComfyUI** (node-based UI + API). Workflows JSON mein save hote hain, isliye reproducible hain
- 🍎 **Mac:** **Draw Things** (App Store, free, offline; FLUX schnell/dev, FLUX.2, Qwen-Image support listed) sabse aasaan hai. ComfyUI bhi MPS par chalta hai. Speed: secondary sources ke mutabik 16–24 GB Macs par ~15–60 s per 1024px image. Max chips tez honge
- 💰 **Budget mode:** Images optional hain. Shuru mein bina images ke (balls/tree/text visuals se analogy) videos banao ([42](42_Budget_Mode_Zero_Cost_Plan.md))

---

## 3. ComfyUI setup (outline)

```bash
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
python -m venv venv && venv\Scripts\activate      # Windows   (Linux: source venv/bin/activate)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128   # apne CUDA ke hisaab se
pip install -r requirements.txt
python main.py --listen 127.0.0.1 --port 8188
```
- Model weights `ComfyUI/models/...` folders mein jaate hain (checkpoints / diffusion_models / text_encoders / vae, model ke docs ke hisaab se)
- ComfyUI ke built-in **templates** (Qwen-Image, FLUX) se shuru karo
- Workflow ko "Save (API format)" se JSON mein export karo, phir pipeline se HTTP API call karo

### API se image banana (pipeline)
```python
import json, uuid, requests, time

COMFY = "http://127.0.0.1:8188"

def comfy_generate(workflow_api_json: dict, prompt_text: str, seed: int, out_prefix: str):
    wf = json.loads(json.dumps(workflow_api_json))       # deep copy
    # Node ids workflow-specific hain: apne export se "positive prompt" aur "seed" wale node dhundho
    wf["6"]["inputs"]["text"] = prompt_text
    wf["3"]["inputs"]["seed"] = seed
    wf["9"]["inputs"]["filename_prefix"] = out_prefix
    r = requests.post(f"{COMFY}/prompt", json={"prompt": wf, "client_id": str(uuid.uuid4())})
    r.raise_for_status()
    pid = r.json()["prompt_id"]
    while True:                                          # simple polling
        h = requests.get(f"{COMFY}/history/{pid}").json()
        if pid in h:
            return h[pid]["outputs"]
        time.sleep(1)
```
> Node ids ("6", "3", "9") sirf example hain. Har exported workflow mein alag hote hain.

---

## 4. Consistent style (series jaisa look)

Har image alag style mein hogi to video bikhra hua lagega. Consistency ke liye:

1. **Fixed style suffix** har prompt ke end mein:
   ```text
   , flat vector illustration, minimal, soft shading, dark navy background (#0F1117),
   accent colors teal (#58C4DD) green (#83C167) coral (#FC6255) yellow (#FFD84D),
   clean shapes, no text, no letters, no numbers, no watermark, 16:9
   ```
2. **Fixed seed per lecture** (ya per character, agar recurring character hai)
3. **Negative prompt** (agar model support kare): `text, letters, words, numbers, watermark, signature, logo, blurry, photorealistic`
4. **Same resolution:** 1920×1080 (ya 1344×768 bana kar upscale)
5. Optional: Ek **style LoRA** train karo (10–20 approved images se), agar series bahut lambi hai

### Recurring character (optional)
Ek friendly "student" ya "robot teacher" character jo har video mein aaye. Character consistency ke liye: same detailed description + seed, ya IP-Adapter/reference-image based tools. Ye advanced hai, isliye pehle bina character ke shuru karo.

---

## 5. Prompt examples (MLT analogies)

| Concept | Prompt (style suffix ke saath) |
|---|---|
| Decision tree / 20 questions | "a friendly doctor asking a patient questions, thought bubbles with simple symbols like thermometer and cough icon" |
| Random forest voting | "a group of diverse friends raising hands to vote, one big checkmark above the majority" |
| Overfitting (ratta) | "a student memorizing a book page by page vs another student understanding with a lightbulb" |
| KNN | "a new person arriving in a neighborhood looking at the nearest houses, houses glowing" |
| Precision vs recall | "a fishing net catching fish and some trash, two nets of different sizes" |
| Curse of dimensionality | "a person searching for a friend in a small room vs in a huge city, top-down view" |

---

## 6. Manim mein use karna

### Static image + Ken Burns (slow zoom/pan)
```python
from manim import *

class AnalogyDoctor(Scene):
    def construct(self):
        img = ImageMobject("assets/images/L20/doctor_questions.png")
        img.scale_to_fit_height(config.frame_height)     # poora frame bharo
        self.add(img)
        self.play(img.animate.scale(1.08).shift(LEFT * 0.3), run_time=6, rate_func=linear)
```
> `ImageMobject` raster image hai, isliye zyada zoom karoge to blurry hoga. Source image render resolution se kam se kam utni hi badi ho. Ken Burns ke liye 1.05–1.15× zoom kaafi hai.

### Image + Manim overlays (labels, arrows)
```python
label = Text("Sawaal 1: Bukhar hai?", font_size=34).to_edge(UP)
arrow = Arrow(label.get_bottom(), img.get_center() + UP * 0.5)
self.play(FadeIn(label), GrowArrow(arrow))
```
Text Manim se aata hai, isliye hamesha sahi spelling aur sahi font rehta hai.

### Image ko dim karna (jab uske upar content aaye)
```python
dim = Rectangle(width=config.frame_width, height=config.frame_height,
                fill_color="#0F1117", fill_opacity=0.6, stroke_width=0)
self.play(FadeIn(dim))
```

---

## 7. Image QA checklist

- [ ] Image mein koi text/letters/numbers nahi (zoom karke dekho; AI aksar chhota garbled text daal deta hai)
- [ ] Haath/ungliyan theek (AI ki common galti); dikhne wale haath kam rakho
- [ ] Cultural context sahi (Indian setting jahan analogy Indian hai)
- [ ] Style series se match karta hai
- [ ] Koi real person/brand/logo nahi
- [ ] License wale model se bana; prompt + seed + model `manifest.json` mein

---

## 8. AI video models (Wan, etc.) ke baare mein

Local AI video models (jaise Wan family) chhote B-roll clips bana sakte hain. **Hamari pipeline mein inka role bahut chhota hai:**
- Content (maths/ML) ke liye ❌: text aur numbers bigaadte hain, non-deterministic hain
- Mood B-roll (3–5 s) ke liye: optional, aur zaroorat nahi
- Static illustration + Ken Burns zyada controllable aur sasta hai

👉 Agla: [24_HyperFrames_Intro_Recap_Quiz.md](24_HyperFrames_Intro_Recap_Quiz.md)
