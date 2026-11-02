# Topic 3: What Is the Difference Between a CPU and a GPU? — Definitions and the Cache/Memory Hierarchy

Source: Lecture 13, slides 8–10 (What's the difference between GPUs and CPUs? — CPU definition with handwritten "Core vs Thread" and "Multicore vs Multithreading"; the cache-hierarchy figure from GeeksforGeeks with handwritten sizes; the CPU + GPU definition slide).

---

## 1) Technical Explanation

**Definitions (slides 8, 10).**

- **CPU (central processing unit):** a hardware component that is *the core computational unit in a server*; it handles *all types of computing tasks* required for the operating system and applications to run.
- **GPU (graphics processing unit):** *a similar hardware component but more specialized*. It can more efficiently handle **complex mathematical operations that run in parallel** than a general CPU. *Initially created for graphics rendering in gaming and animation, its uses now extend far beyond that.*

**Instructor's handwritten notes on slide 8:** **"Core vs Thread"** and **"Multicore vs Multithreading"** — flags for concepts to keep distinct:

- a **core** is a physical processing unit; a **thread** is a stream of instructions a core executes (or a core can interleave several, "hardware threads");
- **multicore** means several cores working truly simultaneously; **multithreading** means running several threads, possibly time-sliced on one core. (The slide gives only the headings; these one-line explanations are standard background.)

**The memory hierarchy figure (slide 9, source: GeeksforGeeks "cache memory").** A CPU chip shows two **cores**, each with its own **L1 cache** and **L2 cache** (the handwritten word "Buffer" is added), a shared **L3 cache**, then off-chip **Random Access Memory (RAM)** and **mass storage (HDD, SSD…)**. Two arrows:

- **Bandwidth increase** toward the CPU core (faster, closer memory has higher bandwidth),
- **Latency / capacity increase** away from the core (farther memory is slower but larger).

Handwritten typical sizes: **L1 ≈ 32–128 KB, L2 ≈ 256 KB–2 MB, L3 ≈ 2–64 MB**, plus the labels "local miss", "global miss" and "access time: hit ratio, miss ratio". Meaning: a *hit* means the data was found in that cache level, a *miss* means it must be fetched from the next, slower level; the average access time depends on the hit ratio (the more hits, the closer to the fast-cache speed).

**Why this matters for deep learning.** Training repeatedly moves large arrays (weights, mini-batches) between slow and fast memory; the memory-sizing example of [[03_Gradient_Descent_Pseudocode_and_Memory_Motivation]] (Lecture 11: 100 GB for 100,000 large images) is exactly this pressure.

---

## 2) Simple English Explanation

- The **CPU** is the computer's all-rounder brain: it runs the operating system and every program.
- The **GPU** is a **specialist** that is much better at doing **lots of the same kind of maths at once**. It started out drawing game graphics but is now used for much more.

The teacher also wrote two reminders: a **core** (a real processing unit) is not the same as a **thread** (one line of work), and **multicore** (many cores) is not the same as **multithreading** (many lines of work).

The picture shows **memory like a ladder**: tiny, super-fast caches (L1, then L2, then L3) right next to the processor, then bigger but slower RAM, then very big and very slow disks. Closer = faster but smaller. When the processor needs data and finds it in the cache, that's a **hit** (fast); if not, a **miss** (it must go down the ladder and wait).

---

## 3) Hinglish Explanation (Beginner-Friendly)

- **CPU** computer ka all-rounder dimaag hai: wo operating system aur har program chalata hai.
- **GPU** ek **specialist** hai jo **ek jaise maths ke bahut saare kaam ek saath** karne mein kahin behtar hai. Ye game graphics banane se shuru hua tha par ab bahut kuch mein use hota hai.

Teacher ne do reminders bhi likhe: **core** (asli processing unit) **thread** (kaam ki ek line) se alag hai, aur **multicore** (kai cores) **multithreading** (kaam ki kai lines) se alag hai.

Picture **memory ko seedhi ki tarah** dikhati hai: processor ke bilkul paas chhote, bahut tez caches (L1, phir L2, phir L3), phir bada par dheema RAM, phir bahut bade aur bahut dheemi disks. Jitna paas, utna tez par chhota. Jab processor ko data chahiye aur wo cache mein mil jaye to wo **hit** hai (tez); na mile to **miss** (neeche seedhi par jaana padta hai aur intezaar karna padta hai).
