# 38 · Licenses, Legal aur Ethics

> **Is file mein:** Har tool/model ka license (commercial use OK hai ya nahi), voice cloning consent, music copyright, AI disclosure, aur lecture content (slides) ke rights. **Ye legal advice nahi hai.** Agar videos monetize ya commercially use karne hain to licenses ko primary source par khud verify karo, aur zaroorat ho to legal advice lo.

---

## 1. Quick table (2026-10-18 ko check kiya)

| Tool / model | License | Commercial use | Notes / caveats |
|---|---|---|---|
| **Manim Community** | MIT | ✅ | |
| **manim-voiceover** | MIT | ✅ | Cloud services (Gemini/Azure/OpenAI/ElevenLabs) ke apne terms hain |
| **HyperFrames** | Apache-2.0 | ✅ | No per-render fees |
| **Remotion** | Remotion License (source-available) | ✅ individuals, ≤3-employee for-profit, non-profits; ❌ 4+ employees → Company License | v5.0 mein license "slightly change" hoga (LICENSE.md) |
| **ffmpeg** | LGPL/GPL (build par depend) | ✅ (tool ke roop mein use) | Agar ffmpeg ko apne product ke saath distribute karo to license obligations hain; sirf videos banane mein koi issue nahi |
| **Kokoro-82M** | Apache-2.0 (weights bhi) | ✅ | |
| **IndicF5** | MIT (HF card) | ⚠️ | Gated; ek third-party source attribution + commercial restriction batata hai. **Verify karo** |
| **Indic Parler-TTS** | Apache-2.0 | ✅ | Gated (terms accept) |
| **Veena** | Apache-2.0 (tag) | ⚠️ | Page header "proprietary" bhi dikhata hai. **Verify karo** |
| **Chatterbox (all)** | MIT | ✅ | Perth watermark built-in |
| **harrrshall/hinglish-tts patch** | Conflict: "Free for research" vs Apache-2.0 sidebar | ⚠️ | Commercial ke liye author se clarify karo, ya apna patch likho |
| **XTTS-v2** | CPML (non-commercial) | ❌ | |
| **Higgs Audio (newer)** | Non-commercial (reported) | ❌ | |
| **VibeVoice** | TTS code Microsoft ne hata diya (Sept 2025) | ❌ avoid | |
| **Whisper (OpenAI)** | MIT | ✅ | |
| **stable-ts** | MIT | ✅ | |
| **WhisperX** | BSD-2-Clause | ✅ | Alignment models (wav2vec2 HF) ke apne licenses check karo |
| **FLUX.1 [schnell]** | Apache-2.0 | ✅ | |
| **FLUX.1 [dev]** | Non-commercial | ❌ (bina BFL license ke) | |
| **FLUX.2 [klein]** | 4B: Apache-2.0 (reported); 9B: non-commercial (reported) | ⚠️ | Model card check karo |
| **Qwen-Image** | Apache-2.0 | ✅ | |
| **SDXL** | CreativeML OpenRAIL++-M | ✅ (use restrictions ke saath) | |
| **MuseTalk** | Code MIT; HF weights card `creativeml-openrail-m` | ⚠️ | Dono check karo |
| **LatentSync** | Apache-2.0 | ✅ | |
| **InfiniteTalk** | Apache-2.0 | ✅ | Base Wan2.1 ka license bhi check karo |
| **Fonts (Inter, Noto, JetBrains Mono)** | SIL OFL | ✅ | |
| **Qwen3-Coder-30B-A3B** (local LLM) | Apache-2.0 | ✅ | HF model card |
| **Ollama** | MIT (open-source) | ✅ | Models ke apne licenses alag hain |
| **LM Studio** | Free, proprietary | ✅ (app terms ke hisaab se) | Closed-source |
| **mlx-whisper** (ml-explore/mlx-examples) | MIT | ✅ | Whisper weights MIT |
| **mlx-audio** | MIT | ✅ | Har model ka apna license (Kokoro Apache-2.0 etc.) |
| **Draw Things** (Mac app) | Free (in-app purchases), closed-source | ✅ (output license = jo model use kiya, jaise FLUX schnell Apache-2.0) | App Store |

> **Model output ka copyright:** AI-generated audio/images ke copyright ka legal status jurisdiction ke hisaab se alag aur abhi evolving hai. Practical rule: jo license model ko commercially use karne deta hai, uske output videos mein use karna aam taur par theek hai. Lekin "exclusive ownership" assume mat karo.

---

## 2. Voice cloning: consent rules

1. **Apni awaaz:** ✅
2. **Kisi aur ki awaaz (teacher, dost, family):**
   - **Written consent** lo, jisme ye sab likha ho: kis cheez ke liye (MLT/DL lecture videos), kahan publish hoga (YouTube, site), kitne time tak, aur consent wapas lene ka tareeka
   - Unhe sample video dikhao
3. **Celebrity/public figure/kisi bhi real insaan ki awaaz bina consent:** ❌ **kabhi nahi** (legal + ethical dono problem)
4. IndicF5 ki terms explicitly kehti hain ki sirf explicit permission wali awaaz clone karo
5. Reference clips aur consent document `video/assets/voice_refs/` ke saath safely store karo (aur public repo mein mat daalo)

---

## 3. Lecture content (slides, sir ka material)

- Videos lecture notes par based hain, aur notes slides par based hain
- **Agar slides/course material institute ya professor ka hai,** to public YouTube par publish karne se pehle **permission lo** (ya kam se kam informed rakho). Ye respect aur legal clarity dono ke liye hai
- Slides ke images/figures directly video mein copy mat karo. Hum apne visuals Manim se banate hain, jo naya expression hai
- Course name/code use karna theek hai, lekin "official" hone ka claim mat karo (jab tak official na ho)
- Third-party content (dataset images, examples) ka attribution do (jaise "PlayTennis dataset: Mitchell, *Machine Learning*, 1997")

---

## 4. Music

- **Sirf license-clear music:** YouTube Audio Library (YouTube Studio ke andar; har track ke attribution requirements dekho), ya Creative Commons tracks jinka license allow kare (CC BY: attribution chahiye; CC BY-NC: non-commercial only)
- License + source URL har track ke liye `assets/music/LICENSES.md` mein likho
- Content ID claim aaye to proof ready rahega

---

## 5. AI disclosure

- YouTube realistic altered/synthetic content ke liye disclosure maangta hai (Studio upload flow mein setting)
- Hamare videos mein AI narration hai (aur optional cloned voice/avatar). **Disclose karo**, ye honest bhi hai aur trust bhi banata hai
- Description mein line: "Narration AI-generated (local TTS); animations code se bani hain; numbers Python se verified"
- Policy details badalti rehti hain, isliye upload ke time current YouTube Help Center guidance dekho

---

## 6. Privacy

- Local pipeline ka fayda ye hai ki notes/audio bahar nahi jaate (TTS, images, alignment sab local)
- Claude (script/code) ko lecture notes bheje jaate hain. Agar course material sensitive/unpublished hai to institute ki policy check karo
- Students ke naam/data videos mein mat daalo (jaise TeachQuiz testers ke results)

---

## 7. Checklist (har naye tool/model se pehle)

- [ ] Model card / LICENSE file **primary source** par padha (blog par nahi)
- [ ] Commercial use allowed? Attribution required?
- [ ] Gated terms (voice cloning restrictions) samjhe?
- [ ] `manifest.json` mein model + version + license record
- [ ] Agar ⚠️ hai to decision documented (kyun use kiya / nahi kiya)

👉 Agla: [39_Verification_Log.md](39_Verification_Log.md)
