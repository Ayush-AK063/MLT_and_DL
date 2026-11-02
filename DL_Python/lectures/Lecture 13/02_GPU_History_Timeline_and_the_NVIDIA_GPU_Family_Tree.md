# Topic 2: GPU History — Timeline, Milestones and the NVIDIA GPU Family Tree

Source: Lecture 13, slides 5–7 (GPU History timeline; "GPU History Timeline & Development" infographic; "NVIDIA GPU Family Tree"). Slides 6 and 7 are dense picture slides (infographic style); only their large, legible labels are used below.

---

## 1) Technical Explanation

**The timeline (slide 5).** Events above and below an axis from the 1980s to 2014:

| Year | Milestone |
|---|---|
| 1980s | **Video card** |
| 1992 | **OpenGL** (graphics API) |
| 1995 | **DirectX** (graphics API) |
| 1999 | **First GPU — NVIDIA GeForce 256** |
| 2001 | **First case of scientific computing with a GPU (matrix–matrix multiplication)** |
| 2002 | The term **"GPGPU"** (general-purpose computing on GPUs); **ATI Radeon 9700** |
| 2006 | **ATI/AMD FireStream; NVIDIA Tesla GPU** |
| 2007 | **CUDA** (NVIDIA's parallel-programming platform) |
| 2009 | **OpenCL; DirectCompute**; **NVIDIA Fermi GPU** |
| 2012 | **NVIDIA Kepler GPU** |
| 2014 | **NVIDIA Maxwell GPU** |

(The vertical placement above/below the axis on the slide separates *software/APIs and concepts* from *hardware products*; the table merges them by year.)

**The narrative.** GPUs began as **fixed-function graphics hardware**; APIs (OpenGL, DirectX) standardised graphics programming; NVIDIA's GeForce 256 (1999) was marketed as the first "GPU". Around 2001–2002 researchers noticed the hardware was good at **matrix arithmetic** and began using it for non-graphics work (**GPGPU**). **CUDA (2007)** and **OpenCL (2009)** made this practical by letting programmers write general parallel programs — the very tools the syllabus names for later parts of the course ("CUDA / OpenCL / OpenACC", [[01_Course_Overview_Syllabus_Evaluation_and_Books]]). Matrix multiplication is also the core operation of neural-network layers, which is why this history leads straight to deep learning (Lecture 2's AlexNet in 2012 was trained on GPUs — background, see [[08_Solving_Object_Recognition_AlexNet_and_When_Not_to_Use_Deep_Learning]]).

**Slide 6 — "GPU History Timeline & Development" (infographic).** Eras by NVIDIA product line, with titles such as GeForce 256 (1999–2001), GeForce 3/4/FX (2002–2006), GeForce 8/9 and GTX 400/500 (2007–2012), Kepler to Maxwell (2012–2016), Pascal to Turing (2016–2020), Ampere (2020–2022), Ada Lovelace (2022–2024) and Blackwell (2025–2026). Small print on this slide is not legible enough to reproduce reliably; only the era names above are taken from it.

**Slide 7 — NVIDIA GPU family tree** (architecture timeline Kepler → Maxwell → Pascal → Turing → Ampere → Ada Lovelace → Blackwell):

| Series | Year | Architecture | Flagship shown |
|---|---|---|---|
| GTX 700 | 2013 | Kepler | GTX 780 Ti |
| GTX 900 | 2014 | Maxwell | GTX 980 Ti |
| GTX 10 | 2016 | Pascal | GTX 1080 Ti |
| RTX 20 | 2018 | Turing | RTX 2080 Ti |
| RTX 30 | 2020 | Ampere | RTX 3090 |
| RTX 40 | 2022 | Ada Lovelace | RTX 4090 |
| RTX 50 | 2025 | Blackwell | RTX 5090 |

**Flag — infographic reliability.** Slides 2–4, 6 and 7 are stylised graphics (they look like AI-generated or marketing-style infographics), not primary sources. The dated timeline (slide 5) and the product-line table above are consistent with well-known NVIDIA history, but exact specs in the small print were deliberately not copied.

---

## 2) Simple English Explanation

Where did GPUs come from?

- **1980s:** simple "video cards" just put pictures on the screen.
- **1990s:** standard graphics toolkits (OpenGL, DirectX) appeared. In **1999** NVIDIA released the GeForce 256 and called it the first **GPU**.
- **Early 2000s:** scientists realised a GPU is superb at **multiplying big tables of numbers (matrices)**, and began using it for science, not just games — called **GPGPU**.
- **2007:** NVIDIA's **CUDA** made it easy to program GPUs for general jobs; **OpenCL** (2009) did similar for any brand.
- **2009–2014:** new chip generations named **Fermi, Kepler, Maxwell**, and afterwards Pascal, Turing, Ampere, Ada Lovelace and Blackwell (the "RTX" cards from 2018 on).

Table multiplication is exactly what neural networks do all day — that's why GPUs power deep learning.

---

## 3) Hinglish Explanation (Beginner-Friendly)

GPUs kahan se aaye?

- **1980s:** simple "video cards" bas screen par picture dikhate the.
- **1990s:** standard graphics toolkits (OpenGL, DirectX) aaye. **1999** mein NVIDIA ne GeForce 256 nikala aur ise pehla **GPU** kaha.
- **2000s ki shuruaat:** scientists ko samajh aaya ki GPU **numbers ki badi tables (matrices) multiply karne** mein kamaal hai, aur unhone ise games ke alawa science mein bhi use karna shuru kiya — ise **GPGPU** kehte hain.
- **2007:** NVIDIA ke **CUDA** ne GPU ko general kaamon ke liye program karna aasan bana diya; **OpenCL** (2009) ne har brand ke liye aisa hi kiya.
- **2009–2014:** chip generations **Fermi, Kepler, Maxwell**, aur baad mein Pascal, Turing, Ampere, Ada Lovelace aur Blackwell (2018 se "RTX" cards).

Tables ka multiplication wahi hai jo neural networks din bhar karte hain — isiliye GPUs deep learning ko power karte hain.
