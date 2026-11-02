# Topic 3: What is the Definition of AI?

Source: Lecture 2, slides 24, 27–29 ("What is the definition of AI?"). Enriched with web research (Russell & Norvig framework, IBM).

---

## 1) Technical Explanation

The lecture poses an open question — *"What is the definition of AI? What do you think?"* — before presenting the standard academic framework (from Russell & Norvig's *Artificial Intelligence: A Modern Approach*), which organizes all definitions of AI along **two independent axes**:

|  | **Human-centered** | **Rationality-centered** |
|---|---|---|
| **Thought process** | Systems that **think like humans** | Systems that **think rationally** |
| **Behavior** | Systems that **act like humans** | Systems that **act rationally** |

- **Think humanly**: modeling AI on cognitive science — trying to make programs whose internal reasoning process mirrors human thought (e.g., McCulloch & Pitts' Boolean circuit model of the brain).
- **Think rationally**: modeling AI on formal logic — programs that reason using correct, provably valid inference (the "laws of thought" tradition).
- **Act humanly**: the behavioral/Turing Test tradition — a system is intelligent if its behavior is indistinguishable from a human's (it doesn't matter *how* it reasons internally, only that the output looks human).
- **Act rationally**: the modern dominant view (the "rational agent" approach) — a system is intelligent if it always takes the action expected to best achieve its goals given the information it has, regardless of whether that resembles human thought or behavior.

The lecture cites **Bellman (1978)**, an example of the "think humanly" camp: *"[The automation of] activities that we associate with human thinking, activities such as decision making, problem solving, learning."*

The lecture also references **IBM's practical definition**: *"Artificial intelligence (AI) is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy."* This is a broader, industry-oriented definition emphasizing simulated capability rather than internal mechanism.

**Why this matters**: Russell & Norvig argue that the "act rationally" approach has dominated modern AI, because it is more scientifically tractable (rationality can be defined mathematically as maximizing expected outcome/utility) and doesn't require solving the much harder philosophical problem of replicating human thought exactly.

---

## 2) Simple English Explanation

Before you can build "artificial intelligence," you first need to agree on what "intelligence" even means for a machine. It turns out there isn't just one definition — researchers have historically split it into four different ways of thinking about it, based on two questions:

1. Are we judging the machine by how it **thinks** (its internal reasoning), or by how it **behaves** (what it actually does)?
2. Are we comparing it to how **humans** do things, or to what is **objectively the best/most logical** way to do things (rationality)?

Combining these two questions gives four categories:
- **Thinks like a human** — the internal process should resemble how our brains work.
- **Thinks rationally** — the internal process should follow correct logical rules, whether or not that's how humans actually think.
- **Acts like a human** — it doesn't matter how it works inside, as long as its behavior looks convincingly human (this is the basis of the famous Turing Test — could you tell if you're talking to a human or a machine?).
- **Acts rationally** — it doesn't matter how it works inside or whether it resembles humans, as long as it makes the best possible decision to reach its goal given what it knows.

Most modern AI (including the ML systems you'll study in this course) leans toward the last definition — **acting rationally** — because it's the easiest to measure and build systems around: did the AI make a good decision given the information it had?

---

## 3) Hinglish Explanation (Beginner-Friendly)

Lecture ne pehle poocha: **"AI ki definition kya hai? Aap kya sochte ho?"** — matlab pehle students se socho-samjho karvaya, fir standard academic answer diya.

AI ko define karne ke **4 tarike** hai, jo do sawalon se aate hai:
1. Hum machine ko uske **soch (thinking)** se judge kar rahe hai ya uske **kaam/behavior (acting)** se?
2. Hum use **insaan jaisa** compare kar rahe hai ya **sabse logical/best (rational)** tarike se?

In do sawalon ko combine karne se 4 categories bante hai:

1. **Think like humans (Insaan jaisa sochna)**: Machine ke andar ka process bilkul dimaag jaisa hona chahiye. (Example: McCulloch & Pitts ka brain model)

2. **Think rationally (Logical soch)**: Machine ko sahi logical rules se sochna chahiye — chahe insaan waise na sochte ho.

3. **Act like humans (Insaan jaisa behavior)**: Andar kya ho raha hai wo matter nahi karta, bas machine ka **behavior insaan jaisa dikhna chahiye**. Isi pe based hai famous **Turing Test** — agar aap pata na laga sako ki saamne insaan hai ya machine, to machine "intelligent" maani jaayegi.

4. **Act rationally (Sabse behtar decision lena)**: Andar kya ho raha hai ya insaan jaisa hai ya nahi, farak nahi padta — bas machine ko apne goal ke hisaab se **sabse achha decision** lena chahiye, jo bhi information uske paas hai uske aadhar par.

**Bellman (1978) ki definition** (jo "think humanly" category mein aati hai): *"Insaan ki soch se juda kaam automate karna — jaise decision lena, problem solve karna, seekhna."*

**IBM ki definition** (practical/industry wali): *"AI ek technology hai jo computers ko insaan jaisi learning, samajhna, problem-solving, decision-making, creativity aur khud se kaam karne ki capability deta hai."*

**Sabse important baat**: Aajkal ka zyada tar AI (jaise ye course jo aap padh rahe ho) **4th definition — "Act Rationally"** ko follow karta hai, kyunki ye sabse aasan hai measure karna: "Kya machine ne apni jaankari ke hisaab se best decision liya?" — isko mathematically define karna aasan hai, isliye researchers isi approach pe zyada kaam karte hai.
