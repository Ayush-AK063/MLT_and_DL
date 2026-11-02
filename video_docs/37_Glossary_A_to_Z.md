# 37 · Glossary A–Z

> **Is file mein:** Docs mein aane wale har technical shabd ka simple matlab, aur kis file mein detail hai.

| Term | Matlab (simple) | Detail |
|---|---|---|
| **AAC** | Audio compression format (YouTube recommended, AAC-LC) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Actions (template)** | script.json beat mein JSON instructions (`{"do":"table",...}`) jinse template engine animation banata hai | [41](41_Template_Engine_Zero_Cost_Animation.md) |
| **AAC priming** | AAC encoder har stream ke shuru mein kuch extra samples daalta hai; bahut saare clips copy-concat karne par chhote offsets jud sakte hain | [27](27_FFmpeg_Final_Assembly.md) |
| **Alignment (forced)** | Known text ke har word ka audio mein start/end time dhundhna | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **Analogy** | Naye concept ko familiar cheez se samjhana | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **Animation (Manim)** | Mobject mein time ke saath change (`Write`, `Create`, `Transform`) | [17](17_Manim_Basics_Install_Concepts.md) |
| **ASR** | Automatic Speech Recognition: audio → text (Whisper) | [13](13_TTS_BakeOff_Kaise_Kare.md) |
| **Aspect ratio** | Width:height (16:9 YouTube) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Audio-first** | Pehle audio banao, phir animation ko audio ki length par fit karo | [02](02_Sync_Ka_Science_Audio_First_Timeline.md) |
| **B-frame** | Video frame jo aage aur peeche dono frames se predict hota hai | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Bake-off** | Kai options ko same test par compare karke best chunna | [13](13_TTS_BakeOff_Kaise_Kare.md) |
| **Beat** | Narration ka chhota tukda (1–3 sentences) + ek visual change | [02](02_Sync_Ka_Science_Audio_First_Timeline.md), [06](06_Script_JSON_Schema_Reference.md) |
| **Bitrate** | Ek second video/audio ke liye kitna data (Mbps/kbps) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Bookmark** | Narration text mein marker (`<bookmark mark='X'/>`); us word par animation trigger | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **Burned-in subtitles** | Video pixels mein likhe subtitles (band nahi ho sakte) | [27](27_FFmpeg_Final_Assembly.md) |
| **Cache key** | Woh inputs jinke same rehne par output dobara nahi banana padta | [05](05_Architecture_Pipeline_Folder_Structure.md) |
| **Cairo** | Manim ka default (CPU) renderer library | [17](17_Manim_Basics_Install_Concepts.md) |
| **CER** | Character Error Rate: ASR text vs reference text ka farak (0 = perfect) | [13](13_TTS_BakeOff_Kaise_Kare.md) |
| **Chapters** | Video ke named sections (YouTube description / MP4 metadata) | [27](27_FFmpeg_Final_Assembly.md), [32](32_Publishing_YouTube.md) |
| **Chroma subsampling (4:2:0)** | Color information ko kam resolution par store karna; `yuv420p` | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Code-mixed** | Ek sentence mein do languages (Hinglish) | [09](09_TTS_Model_Selection_Guide.md) |
| **Codec** | Compress/decompress karne ka tareeka (H.264, AAC) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Component library** | Reusable, tested Manim objects (table, tree, chart) | [19](19_Manim_Component_Library_Design.md) |
| **ComfyUI** | Node-based local image generation tool + API | [23](23_Imagery_Local_Image_Generation.md) |
| **Concat demuxer** | ffmpeg ka bina re-encode files jodne ka tareeka (`-f concat`) | [27](27_FFmpeg_Final_Assembly.md) |
| **Container** | File format jo streams rakhta hai (MP4, MKV) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **CRF** | Constant Rate Factor: x264 quality setting (18 ≈ visually lossless) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Critic** | AI/automatic reviewer jo rendered frames mein galtiyan dhundhta hai | [22](22_Critic_Loop_Visual_QA.md) |
| **CUDA** | NVIDIA GPU par computation ka platform (PyTorch use karta hai) | [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) |
| **dBFS / dBTP** | Digital level / true peak level (0 = max) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md), [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **Deterministic** | Same input → har baar exactly same output | [00](00_Seedhi_Baat_Big_Picture.md) |
| **Devanagari** | Hindi ki script (देवनागरी) | [14](14_Pronunciation_Text_Normalization.md) |
| **Ducking** | Narration bolte waqt music automatically dheema hona | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **dvisvgm** | LaTeX output (DVI) ko SVG mein badalne ka tool; Manim MathTex ko chahiye | [35](35_Troubleshooting_FAQ.md) |
| **EBU R128** | Loudness measurement standard (LUFS) | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **espeak-ng** | Open-source phonemizer/TTS; Kokoro fallback ke liye use karta hai | [10](10_TTS_Setup_Kokoro.md) |
| **F5-TTS** | Flow-matching TTS architecture (IndicF5 isi par based) | [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) |
| **faststart** | MP4 ka metadata (moov) file ke shuru mein, taaki streaming jaldi shuru ho | [27](27_FFmpeg_Final_Assembly.md) |
| **FFMETADATA** | ffmpeg ka metadata text format (chapters ke liye) | [27](27_FFmpeg_Final_Assembly.md) |
| **ffmpeg / ffprobe** | Video/audio processing / inspection CLI tools | [27](27_FFmpeg_Final_Assembly.md) |
| **FPS** | Frames per second (hum 30 use karte hain) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Gated model** | Hugging Face model jise download karne se pehle terms accept karni padti hain | [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) |
| **Golden example** | Ek approved scene jo AI coder ko pattern ki tarah diya jaata hai | [21](21_AI_Se_Manim_Code_Generation.md) |
| **GOP** | Group of Pictures: ek keyframe se agle keyframe tak (hum 15) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **GSAP** | JavaScript animation library (HyperFrames mein) | [24](24_HyperFrames_Intro_Recap_Quiz.md) |
| **H.264** | Sabse common video codec (YouTube recommended) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Hook** | Video ka pehla 20–40 s jo curiosity jagaye | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **HyperFrames** | HTML/CSS/JS → MP4 framework (HeyGen, Apache-2.0) | [24](24_HyperFrames_Intro_Recap_Quiz.md) |
| **I-frame / keyframe** | Poora (independent) video frame | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Idempotent** | Same command do baar chalao to same result | [05](05_Architecture_Pipeline_Folder_Structure.md) |
| **Ken Burns effect** | Static image par slow zoom/pan | [23](23_Imagery_Local_Image_Generation.md) |
| **LaTeX** | Maths typesetting system (MathTex isse render hota hai) | [17](17_Manim_Basics_Install_Concepts.md) |
| **Layout audit** | Code se text objects ke overlap/out-of-frame check karna | [22](22_Critic_Loop_Visual_QA.md) |
| **loudnorm** | ffmpeg ka EBU R128 loudness normalization filter | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **LRA** | Loudness Range | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **LUFS** | Perceived loudness ki unit (target −14 integrated) | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **Manim (CE)** | Python maths animation library (Community Edition) | [17](17_Manim_Basics_Install_Concepts.md) |
| **manim-voiceover** | Manim plugin: voiceover + sync | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **manifest.json** | Har video ke saath record: kaun sa model/voice/prompt/version | [05](05_Architecture_Pipeline_Folder_Structure.md) |
| **MathTex** | Manim ka LaTeX maths object | [17](17_Manim_Basics_Install_Concepts.md) |
| **MiKTeX** | Windows ka LaTeX distribution | [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) |
| **MLX** | Apple ka ML framework (Apple Silicon ke liye); mlx-whisper, mlx-audio, mlx-lm | [40](40_Mac_Apple_Silicon_Setup.md) |
| **MoE (Mixture of Experts)** | Model jisme har token ke liye sirf kuch parameters active hote hain (jaise 30B mein 3.3B), isliye fast | [30](30_Local_LLMs_Kab_Aur_Kaise.md) |
| **MPS** | Metal Performance Shaders: PyTorch ka Mac GPU backend (`device="mps"`) | [40](40_Mac_Apple_Silicon_Setup.md) |
| **Mobject** | Manim mein screen par dikhne wali har cheez | [17](17_Manim_Basics_Install_Concepts.md) |
| **MOS** | Mean Opinion Score (1–5 listening rating) | [13](13_TTS_BakeOff_Kaise_Kare.md) |
| **moov atom** | MP4 ka index/metadata block | [27](27_FFmpeg_Final_Assembly.md) |
| **Normalization (text)** | Text ko TTS ke liye spoken form mein badalna ("0.940" → "zero point nine four zero") | [14](14_Pronunciation_Text_Normalization.md) |
| **NVENC** | NVIDIA GPU hardware video encoder | [26](26_Rendering_Performance_Parallel.md) |
| **Partial movie files** | Manim ke har `play()` ke chhote clips (cache) | [26](26_Rendering_Performance_Parallel.md) |
| **Pause-and-try** | Viewer ko khud solve karne ka moment (countdown) | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **PCM** | Uncompressed audio (WAV ke andar) | [27](27_FFmpeg_Final_Assembly.md) |
| **PiP** | Picture-in-picture (corner mein chhota video) | [31](31_Avatar_Talking_Head_Optional.md) |
| **Pre-baked audio** | Audio render se pehle bana lena; render ke waqt sirf file uthana | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **Pronunciation dictionary** | Word → spoken form mapping (`pronunciation.yaml`) | [14](14_Pronunciation_Text_Normalization.md) |
| **PyAV** | ffmpeg ki Python bindings; Manim v0.19+ isse use karta hai | [17](17_Manim_Basics_Install_Concepts.md) |
| **Quantization (4-bit)** | Model weights ko kam bits mein store karna, taaki kam VRAM mein chale | [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md), [30](30_Local_LLMs_Kab_Aur_Kaise.md) |
| **Redundancy principle** | Narration ka poora text screen par mat likho | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **Reference audio** | Voice cloning ke liye awaaz ka sample clip | [12](12_TTS_Setup_Chatterbox_Voice_Cloning.md) |
| **Remotion** | React-based video framework (source-available) | [25](25_Remotion_Alternative.md) |
| **Render** | Code se final frames/video banana | [26](26_Rendering_Performance_Parallel.md) |
| **RTF** | Real-Time Factor: generation time / audio duration | [13](13_TTS_BakeOff_Kaise_Kare.md) |
| **run_time** | Manim animation ki duration (seconds) | [17](17_Manim_Basics_Install_Concepts.md) |
| **Safe area** | Frame ka woh hissa jahan important content safe hai | [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md) |
| **Sample rate** | Audio per second kitne samples (48 kHz final) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |
| **Scene (Manim)** | Ek video clip class (`construct()`) | [17](17_Manim_Basics_Install_Concepts.md) |
| **Scene (script)** | Teaching template ka ek block (hook, intuition, ...) | [06](06_Script_JSON_Schema_Reference.md) |
| **script.json** | Single source of truth: narration + visuals + numbers | [06](06_Script_JSON_Schema_Reference.md) |
| **Segmenting** | Content ko chhote tukdon mein baantna | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **sidechaincompress** | ffmpeg filter: ek signal (voice) doosre (music) ko dabata hai | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **Signaling** | Important cheez highlight karna | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **SNAC** | Neural audio codec (Veena isse audio decode karta hai) | [11](11_TTS_Setup_Indic_Models_IndicF5_Parler_Veena.md) |
| **Soft subtitles** | Alag subtitle track/file, on/off ho sakta hai | [27](27_FFmpeg_Final_Assembly.md) |
| **SoX** | Audio processing CLI (manim-voiceover speed change ke liye) | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **SRT / VTT** | Subtitle file formats | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **stable-ts** | Whisper par based library; known text align kar sakti hai | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **Sub-beat** | Beat ko aur chhote audio tukdon mein todna (bookmarks ki jagah) | [02](02_Sync_Ka_Science_Audio_First_Timeline.md) |
| **Subcaption** | Manim ka built-in caption system (.srt output) | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **Template engine** | Fixed, tested code jo JSON actions se scenes banata hai (har video ke liye AI-code nahi) | [41](41_Template_Engine_Zero_Cost_Animation.md) |
| **Budget mode** | Bina paid API, MacBook par local pipeline (≈ ₹0) | [42](42_Budget_Mode_Zero_Cost_Plan.md) |
| **Ollama** | Local LLM chalane ka tool (OpenAI-compatible API, port 11434) | [30](30_Local_LLMs_Kab_Aur_Kaise.md), [40](40_Mac_Apple_Silicon_Setup.md) |
| **Unified memory** | Apple Silicon mein CPU + GPU ki shared RAM (64 GB = models ke liye bahut jagah) | [40](40_Mac_Apple_Silicon_Setup.md) |
| **TeachQuiz** | Code2Video ka metric: video se kitna seekha | [36](36_Research_Papers_And_Prior_Art.md) |
| **Tracker** | manim-voiceover ka object: duration, bookmarks timing | [18](18_Manim_Voiceover_Sync_Custom_Local_TTS.md) |
| **TransformMatchingTex** | Formula ke matching parts ko smoothly morph karne wali animation | [17](17_Manim_Basics_Install_Concepts.md) |
| **Transliteration** | Ek script se doosri mein likhna (Roman → Devanagari) | [14](14_Pronunciation_Text_Normalization.md) |
| **True peak** | Samples ke beech ke peaks bhi count karke maximum level | [15](15_Audio_Post_Processing_Loudness_Music.md) |
| **TTS** | Text-to-Speech | [09](09_TTS_Model_Selection_Guide.md) |
| **uv** | Fast Python package/project manager (Manim docs recommend karte hain) | [17](17_Manim_Basics_Install_Concepts.md) |
| **VGroup** | Manim mein objects ka group | [17](17_Manim_Basics_Install_Concepts.md) |
| **Verify block** | script.json mein har number ka Python check | [08](08_Math_Verification_Step.md) |
| **Visual anchor** | Fixed layout positions/regions (free coordinates ki jagah) | [20](20_Visual_Style_Guide_Colors_Fonts_Layout.md) |
| **VLM** | Vision-Language Model (images samajhne wala LLM) | [22](22_Critic_Loop_Visual_QA.md) |
| **VRAM** | GPU ki memory | [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) |
| **Watermark (Perth)** | Chatterbox ka inaudible audio watermark | [12](12_TTS_Setup_Chatterbox_Voice_Cloning.md) |
| **wav2vec2** | Speech model; WhisperX alignment ke liye use hota hai | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **Whisper / WhisperX** | OpenAI ASR model / uska word-timestamp extension | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **Word boundaries** | Har word ka audio offset + text offset (manim-voiceover format) | [16](16_Word_Timestamps_Forced_Alignment_Captions.md) |
| **WPM** | Words per minute (narration ~130–150) | [03](03_Pedagogy_Teaching_Design_Principles.md) |
| **WSL2** | Windows par Linux (Ubuntu) chalana | [29](29_Hardware_Environment_Setup_Windows_NVIDIA.md) |
| **yuv420p** | Universal pixel format (hamesha final mein) | [01](01_Video_Basics_Frames_FPS_Codecs_Audio.md) |

👉 Agla: [38_Licenses_Legal_Ethics.md](38_Licenses_Legal_Ethics.md)
