# Topic 6: Function and Design, the Summary Table, and When to Use GPUs over CPUs

Source: Lecture 13, slides 22–29 (Function; Design; When to use GPUs over CPUs — overview, (1) Deep learning, (2) High-performance computing, Autonomous vehicles; Summary of differences: CPU vs. GPU; Reading Resources).

---

## 1) Technical Explanation

**Function (slide 22).** The main difference lies in function. **A server cannot run without a CPU**: the CPU handles all the tasks needed for all software to run correctly. The **GPU supports the CPU to perform concurrent calculations**, and can complete **simple and repetitive tasks much faster** because it breaks a task into smaller components and finishes them **in parallel**.

**Design (slide 23).**

- GPUs excel at parallel processing through several cores / **ALUs**.
- **GPU cores are less powerful than CPU cores and have less memory.**
- A CPU can **switch rapidly between different instruction sets**; a GPU takes **a high volume of the *same* instructions and pushes them through at high speed**.
- Hence GPUs play an important role in **parallel computing**.

**When to use GPUs (slides 24–27).** The choice is **not either-or**: every server (or cloud instance) requires a CPU; some servers add GPUs as **additional coprocessors** for workloads they handle better — e.g. **floating-point calculations, graphics processing, data pattern matching**. Three headline use cases:

1. **Deep learning (slide 25).** Deep learning is an AI method that teaches computers to process data in a way *inspired by the human brain*; algorithms recognise complex patterns in pictures, text, sounds and other data to produce accurate insights and predictions. **GPU-based servers give high performance for machine learning, neural networks and deep-learning tasks.**
2. **High-performance computing (slide 26).** Tasks needing very high computing power — geoscientific simulations and seismic processing; financial simulations to identify portfolio risk and hedging opportunities; predictive, real-time or retrospective data-science applications in medicine, genomics and drug discovery. A GPU-based system suits these.
3. **Autonomous vehicles (slide 27).** Developing and deploying ADAS (advanced driver-assistance systems) and AV systems needs highly scalable computing, storage, networking and analytics — data collection, labelling and annotation, map development, algorithm development, simulations and verification; such workloads require GPU-based systems to run efficiently. (Self-driving cars were already one of the applications on Lecture 1's list — [[05_Applications_Vision_Cinema_Activity_Captioning_Objects_Cars]].)

**Summary table (slide 28).**

| | **CPU** | **GPU** |
|---|---|---|
| **Function** | Generalized component that handles the main processing functions of a server | Specialized component that excels at parallel computing |
| **Processing** | Designed for **serial** instruction processing | Designed for **parallel** instruction processing |
| **Design** | **Fewer, more powerful cores** | **More cores** than CPUs, but **less powerful** than CPU cores |
| **Best suited for** | General-purpose computing applications | High-performance computing applications |

**Reading resources (slide 29):** AWS "The difference between GPUs and CPUs"; a Cray User Group 2011 slide deck (Larkin); ENCCS "GPU architecture" (OpenMP/GPU); and NVIDIA's corporate timeline. These are the main sources of the deck; the URLs are on the slide.

**Rule of thumb that follows.** If the work is **many independent, identical, arithmetic-heavy operations on big arrays** (matrix products, convolutions, the weighted sums of every neuron in a layer), use a **GPU**; if it is **branchy, sequential, or needs low latency for a single task**, use a **CPU**. This explains why the algorithms of Lectures 10–12 — mini-batch gradient descent, momentum, RMSProp — are run on GPUs in practice: each mini-batch is one big batch of identical operations ([[04_MiniBatching_a_Large_Dataset_Worked_Example]], Lecture 11).

---

## 2) Simple English Explanation

- **Every computer needs a CPU** — it runs everything. A **GPU is an optional helper** that does lots of simple, repeated jobs together very fast. The GPU's workers are weaker and have less memory than the CPU's, but there are far more of them, and they all do the **same** instruction at once.
- **Use a GPU for:** deep learning (neural networks are mountains of repeated maths), big scientific and financial simulations, medicine and gene research, and self-driving-car development.
- **The summary:** CPU = general-purpose, one-thing-after-another, a few strong cores. GPU = specialist, many-things-at-once, lots of weaker cores.

The deck ends with four web links for further reading.

---

## 3) Hinglish Explanation (Beginner-Friendly)

- **Har computer ko CPU chahiye** — wo sab kuch chalata hai. **GPU ek optional madadgaar hai** jo bahut saare simple, dohraye jaane wale kaam ek saath bahut tezi se karta hai. GPU ke workers CPU ke workers se kamzor hain aur unke paas memory kam hai, par unki sankhya bahut zyada hai, aur wo sab ek hi instruction **ek saath** chalate hain.
- **GPU kab use karein:** deep learning (neural networks dohrayi jaane wale maths ke pahaad hain), bade scientific aur financial simulations, medicine aur gene research, aur self-driving gaadi ka development.
- **Saar:** CPU = general-purpose, ek-ke-baad-ek, kuch mazboot cores. GPU = specialist, kai-kaam-ek-saath, bahut saare kamzor cores.

Deck ke aakhir mein aage padhne ke liye chaar web links diye hain.
