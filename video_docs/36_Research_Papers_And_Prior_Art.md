# 36 · Research Papers aur Prior Art

> **Is file mein:** Automated educational video generation par important research (Code2Video, TheoremExplainAgent, Paper2Video), learning-science research (Mayer, Guo et al.), unse kya seekha, aur hamare design mein kahan use hua.

---

## 1. Code2Video (Show Lab, NUS)

| | |
|---|---|
| Paper | "Code2Video: A Code-centric Paradigm for Educational Video Generation", arXiv **2510.01174** |
| Code | github.com/showlab/Code2Video (MIT) |
| Venue | NeurIPS 2025 workshop; aggregator ICML 2026 bhi list karta hai |

### Kya karta hai
Pixels generate karne ki jagah **executable Manim code** generate karta hai. **Tri-agent design** use karta hai:
1. **Planner:** topic ko storyboard mein expand karta hai
2. **Coder:** debuggable Manim code likhta hai
3. **Critic:** **visual anchor prompts** + multimodal (VLM) feedback se layout refine karta hai

### Key results/details
- TheoremExplainAgent ke benchmark par (GPT-4o ke saath): **Element Layout 0.59 → 0.91**, Visual Relevance 0.79 → 0.91. Authors iska credit code-driven generation aur asset reuse ko dete hain
- README ke mutabik best Manim code quality **Claude-4-Opus** se aayi; best VLM critic gemini-2.5-pro tha
- **MMMC benchmark:** 3Blue1Brown-style Manim tutorials se bana, 13 subjects
- **TeachQuiz metric:** video se asli knowledge transfer naapta hai, concepts ko "unlearn" aur phir video se "relearn" karwa ke
- Icons IconFinder API se aate hain, aur assets cache/reuse hote hain
- `PARALLEL_GROUP_NUM` se parallel generation

### Humne kya liya
| Code2Video idea | Hamare docs mein |
|---|---|
| Code-centric (Manim) | Poora architecture ([00](00_Seedhi_Baat_Big_Picture.md)) |
| Planner → Coder → Critic | Script passes ([07](07_Script_Generation_Prompts_With_Claude.md)), Coder ([21](21_AI_Se_Manim_Code_Generation.md)), Critic ([22](22_Critic_Loop_Visual_QA.md)) |
| Visual anchors | Named layout regions + `place()` ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) |
| Asset reuse | Component library ([19](19_Manim_Component_Library_Design.md)) |
| TeachQuiz | TeachQuiz-lite learner testing ([28](28_Quality_Assurance_Checklist.md) §10) |

---

## 2. TheoremExplainAgent (TEA)

| | |
|---|---|
| Paper | "TheoremExplainAgent: Towards Video-based Multimodal Explanations for LLM Theorem Understanding", arXiv **2502.19400**; **ACL 2025** (long paper) |

### Kya karta hai
- **Two-agent:** planner (story plan + narration) aur coding agent (Manim Python scripts)
- **Long-form** theorem explanation videos (5+ min)
- **TheoremExplainBench:** 240 theorems, multiple STEM disciplines, 5 automated evaluation metrics

### Key results
- o3-mini agent: **93.8% success rate**, overall score **0.77**
- Lekin zyadatar videos mein **"minor issues with visual element layout"** the

### Humne kya liya
- Planner/narration aur code ka alag hona
- Layout issues ka asli problem hona, jiske liye component library + audit + critic ([19](19_Manim_Component_Library_Design.md), [22](22_Critic_Loop_Visual_QA.md))

---

## 3. Paper2Video

| | |
|---|---|
| Paper | "Paper2Video: Automatic Video Generation from Scientific Papers", arXiv **2510.05096**; Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou (Show Lab, NUS); NeurIPS 2025 listing |
| Code | github.com/showlab/Paper2Video |

### Kya karta hai
- Research paper → 2–10 min presentation video
- **PaperTalker** multi-agent: slide generation (Beamer), layout refinement (Monte-Carlo tree search, NeurIPS version mein), cursor grounding, subtitles, speech synthesis, **talking head**
- Slide-by-slide parallel generation
- Benchmark: 101 papers + author-made videos/slides; metrics: Meta Similarity, PresentArena, PresentQuiz, IP Memory (v2)

### Humne kya liya
- Slide-wise/scene-wise **parallel generation** ([26](26_Rendering_Performance_Parallel.md))
- Subtitles + speech + visual alignment ka ek system ke roop mein sochna
- Talking head ko **optional** rakha ([31](31_Avatar_Talking_Head_Optional.md)). Presentation videos ke liye useful hai, maths animation ke liye zaroori nahi

---

## 4. Learning science

### Mayer: Multimedia Learning
- Book *Multimedia Learning* (2001; baad mein updated editions)
- 12 principles (+ 2020 handout mein Embodiment)
- Hamare design ka foundation ([03](03_Pedagogy_Teaching_Design_Principles.md) §2)

### Guo, Kim & Rubin (2014): "How Video Production Affects Student Engagement: An Empirical Study of MOOC Videos"
- ACM Learning @ Scale 2014, DOI 10.1145/2556325.2566239
- 6.9 million video sessions, 4 edX courses
- Findings (abstract): chhote videos zyada engaging; informal talking-head zyada engaging; Khan-style tablet drawing zyada engaging; pre-recorded classroom lectures online achhe se engage nahi karte
- ⚠️ Commonly quoted "~6 minute" number humne sirf secondary context se dekha hai, abstract mein nahi. Full paper mein check karo

---

## 5. Tools/frameworks ka context

| Tool | Context |
|---|---|
| **Manim** | Grant Sanderson (3Blue1Brown) ne banaya; Community Edition (ManimCE) community-maintained fork hai |
| **manim-voiceover** | ManimCommunity plugin; voiceovers + Whisper-based word timing for bookmarks |
| **HyperFrames** | HeyGen, open-source (Apache-2.0), 2026; "video as code for AI agents" |
| **Remotion** | React-based video, source-available license |

---

## 6. Open problems (jahan research abhi bhi kamzor hai)

1. **Hinglish TTS quality:** code-mixed TTS ke benchmarks kam aur chhote hain
2. **Layout reliability:** LLM-generated visuals mein overlap/clutter, jo abhi bhi critic loops se hi handle hota hai
3. **Pedagogical evaluation:** "Video ne kitna sikhaya" naapna mushkil hai (TeachQuiz ek attempt hai)
4. **Long-form coherence:** 1–2 ghante ke content mein consistent style aur callbacks
5. **Hinglish forced alignment:** Roman Hinglish ke liye achhe aligners nahi hain ([16](16_Word_Timestamps_Forced_Alignment_Captions.md) §5)

Hamari pipeline in sab ko engineering se handle karti hai (bake-off, components, audit, sub-beats, chapters). Lekin ye areas hain jahan naye tools aate rahenge, isliye har kuch mahine mein check karo.

---

## 7. Links

- Code2Video: https://arxiv.org/abs/2510.01174 · https://github.com/showlab/Code2Video
- TheoremExplainAgent: https://arxiv.org/abs/2502.19400 · https://aclanthology.org/2025.acl-long.332/
- Paper2Video: https://arxiv.org/abs/2510.05096 · https://github.com/showlab/Paper2Video
- Guo et al. 2014: https://www.cs.rochester.edu/hci/pubs/pdfs/edX-MOOC-video-production-and-engagement_LAS-2014.pdf
- Mayer principles summary (Mayer 2020 handout): https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf

👉 Agla: [37_Glossary_A_to_Z.md](37_Glossary_A_to_Z.md)
