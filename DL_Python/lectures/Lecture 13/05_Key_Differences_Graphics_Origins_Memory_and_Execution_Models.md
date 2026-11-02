# Topic 5: Key Differences — Graphics Origins, Memory Models and Execution Styles

Source: Lecture 13, slides 18–21 (Key differences: CPUs vs. GPUs ×2; the CPU-vs-GPU memory/control comparison; the CPU-vs-GPU execution-style comparison).

---

## 1) Technical Explanation

**Why GPUs appeared (slide 18).**

- The arrival of **computer graphics and animation** produced the first **compute-intensive workloads that CPUs were simply not designed to handle**.
- Example: video-game animation had to process data to display **thousands of pixels — each with its own colour, light intensity and movement**.
- **Geometric mathematical calculations on CPUs** of the time caused performance issues.

**What changed (slide 19).** Hardware makers recognised that **offloading common multimedia-oriented tasks could relieve the CPU and increase performance**. Today GPU workloads cover several compute-intensive applications, including **machine learning and AI — more efficiently than CPUs**.

**Memory and control comparison (slide 20).**

| CPU | GPU |
|---|---|
| **Large memory, directly accessible** | **Relatively small memory, must be managed by the CPU** |
| **Each core has its own, independent control logic** → allows independent execution | **Groups of compute cores share control logic** → saves space, power, … |
| **Coherent caches between cores** → can share and synchronise | **Shared cache and synchronisation within groups**; *none between groups* |

**Execution-style comparison (slide 21).**

| CPU | GPU |
|---|---|
| Tuned for **serial execution with short vectors** | Tuned for **highly parallel execution** |
| **Multiple independent threads** of execution | **Threads work in lockstep within groups** — much like vectors |
| **Branch prediction** | **Serialises branchy code** (when threads in a group take different `if` paths, the paths run one after another) |
| **Memory latency hidden by cache and prefetching** — requires regular data-access patterns | **Memory latency hidden by swapping away stalled threads** — requires 1000s of concurrent threads |

**Reading the contrast.** The CPU fights waiting with **cleverness** (caches, prediction, prefetching); the GPU fights waiting with **abundance** (when some threads stall on memory, switch to others — it always has thousands to run). The GPU's *lockstep groups* ("warps" in NVIDIA terms — a later topic of the course) explain why neural-network code, which applies the **same operation to huge arrays**, runs well, and why heavily branching code does not.

---

## 2) Simple English Explanation

**Why GPUs were invented:** early computers struggled to draw video games, where **thousands of tiny dots (pixels)** each need their own colour and brightness worked out. So engineers moved the picture-drawing maths to a separate chip. Later people noticed the same chip was great for **machine learning** too.

**The CPU style:** a few clever workers, each with their own instructions, lots of fast memory nearby, and tricks like *guessing* what comes next (branch prediction) and *fetching ahead* (prefetching) to avoid waiting.

**The GPU style:** thousands of simple workers that **move in teams, doing the same step together** (like a marching band). They share instructions within a team, have less memory (managed by the CPU), and if a team hits an "if this, do that, otherwise do the other" situation, the options are done one after another, which wastes time. They don't avoid waiting by being clever — they simply switch to another team that's ready, so they need **thousands of teams** to stay busy.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**GPU kyun bana:** shuruaati computers video games draw karne mein struggle karte the, jahan **hazaaron chhote dots (pixels)** ka rang aur brightness nikaalna padta hai. To engineers ne picture-banane wala maths ek alag chip ko de diya. Baad mein logon ne dekha ki wahi chip **machine learning** ke liye bhi bahut achha hai.

**CPU ka style:** kuch chalaak workers, har ek ke apne instructions, paas mein bahut tez memory, aur tricks jaise agla kya hoga ye *andaza lagana* (branch prediction) aur *pehle se laa kar rakhna* (prefetching) taaki intezaar na karna pade.

**GPU ka style:** hazaaron simple workers jo **teams mein chalte hain, ek hi step saath mein karte hain** (marching band ki tarah). Wo team ke andar instructions share karte hain, unke paas memory kam hoti hai (jo CPU manage karta hai), aur agar team ke saamne "agar ye ho to ye karo, warna wo" aa jaye to options ek ke baad ek kiye jaate hain, jisse samay barbaad hota hai. Wo intezaar chalaaki se nahi bachate — bas dusri taiyaar team par switch kar jaate hain, isliye unhe **hazaaron teams** chahiye taaki wo busy rahein.
