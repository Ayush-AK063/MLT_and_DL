# 31 · Avatar / Talking Head (Optional)

> **Is file mein:** Kya video mein ek "teacher ka chehra" hona chahiye? Research kya kehti hai, local options (MuseTalk, LatentSync, InfiniteTalk), unke licenses, aur agar use karein to kaise.

---

## 1. Kya zaroori hai? (research)

| Source | Kya kehta hai |
|---|---|
| Mayer ka **Image principle** | Speaker ka chehra screen par hone se seekhna **zaroori nahi badhta** |
| Mayer ka **Embodiment** (2020 handout) | Agar on-screen character hai to human-like gestures helpful hain |
| Guo et al. 2014 (edX) | **Informal talking-head** videos zyada engaging the; Khan-style drawing bhi engaging thi |
| Paper2Video (2025) | Slides + subtitles + speech + **talking head** pipeline banaya gaya (presentation videos ke liye) |

**Matlab:** Engagement ke liye chehra thoda madad kar sakta hai, lekin seekhne ke liye **animation + narration kaafi hai.** Maths-heavy content mein screen space formulas ko dena better hai.

### Hamari recommendation
- **Default: Avatar nahi.** Poora focus animation par
- **Optional:** Intro/outro mein, ya hook/recap mein chhota picture-in-picture (PiP) corner (screen ka ~15%)
- **Kabhi nahi:** Formula/table ke upar avatar

---

## 2. Local options (2026-10-18)

| Model | Input | Kya karta hai | License | Hardware (README) |
|---|---|---|---|---|
| **MuseTalk** (Tencent Music, Lyra Lab) | Existing face **video** + audio | Lip region ko audio ke hisaab se redraw karta hai (latent inpainting, single step) | Code: MIT (project disclaimer). ⚠️ HF weights card par `creativeml-openrail-m` tag hai. Dono check karo | Real-time capable (256×256 face, paper: 30+ fps) |
| **LatentSync 1.6** (ByteDance) | Face video + audio | Diffusion-based lip sync, sharper; TREPA se temporal flicker kam | **Apache-2.0** | 1.6: min **18 GB** VRAM (1.5: 8 GB); 512 resolution training |
| **InfiniteTalk** (MeiGen-AI) | **Image** ya video + audio | Lips + head + body + expressions animate; video-to-video dubbing "unlimited length" | **Apache-2.0** | Wan2.1-I2V-14B base; heavy; fp8 option; 480p/720p |
| SadTalker | Image + audio | Purana (2023 ke baad development kam) | – | ❌ Outdated |

### Kaun sa kab
- **Apni recorded video hai** (jaise 2 min ka clip jisme tum camera ki taraf dekh kar bol rahe ho) → **LatentSync** (quality) ya **MuseTalk** (speed)
- **Sirf ek photo hai** → **InfiniteTalk** image-to-video (README: ~1 min tak achha, uske baad color shift badhta hai)
- **Lamba PiP** → Video-to-video mode with a looped base clip

---

## 3. PiP workflow (agar use karein)

```
1. Base clip record karo: 30–60 s, tum neutral expressions ke saath "bol rahe ho" (koi bhi text),
   achhi lighting, plain background (green screen ho to best)
2. Har hook/recap beat ke audio ke liye: LatentSync(base_clip_segment, beat.wav) → face clip
3. Background remove (agar green screen) → circle mask
4. ffmpeg overlay → corner mein
```

```bash
# circle-masked PiP, bottom-right, 360px
ffmpeg -i main.mp4 -i face.mp4 -filter_complex "\
[1:v]scale=360:360,format=yuva420p,geq=lum='p(X,Y)':a='if(lt(hypot(X-180,Y-180),178),255,0)'[pip]; \
[0:v][pip]overlay=W-w-60:H-h-60:shortest=1[v]" \
-map "[v]" -map 0:a -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy out_pip.mp4
```
> PiP position bottom-right hai, jahan YouTube captions bhi aate hain. Captions zone ([20](20_Visual_Style_Guide_Colors_Fonts_Layout.md)) ka dhyan rakho, ya PiP top-left rakho.

---

## 4. Ethics (zaroori)

- **Apna chehra/awaaz:** theek
- **Kisi aur ka:** written consent, aur video description mein disclose karo ("AI-generated avatar")
- Kisi real teacher/celebrity ka chehra **bina consent ke kabhi nahi**
- YouTube ki altered/synthetic content disclosure policy follow karo ([32](32_Publishing_YouTube.md), [38](38_Licenses_Legal_Ethics.md))

---

## 5. Uncanny valley warning

Achha avatar engaging lagta hai, lekin thoda sa galat avatar (lips off-sync, ajeeb aankhen) **distracting** ho jaata hai aur poore video ki credibility girata hai. Agar quality 9/10 nahi hai to avatar mat lagao. Bina avatar ke clean animation hamesha safe hai.

👉 Agla: [32_Publishing_YouTube.md](32_Publishing_YouTube.md)
