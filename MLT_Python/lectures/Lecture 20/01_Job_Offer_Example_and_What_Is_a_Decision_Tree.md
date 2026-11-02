# Topic 1: The Job-Offer Example and What a Decision Tree Is

Source: Lecture 20, slides 1–3 (title slide, "Lets see the example...", "Decision Tree"). Enriched with web research (Quinlan's ID3 paper 1986, Breiman et al. CART 1984).

---

## 1) Technical Explanation

**Slide 2 — the motivating example.** A job seeker compares several offers that differ in commute distance, pay and benefits. They list each position's *features*, then derive *rules* that eliminate options:
- "If my commute is longer than an hour, then I will be unhappy."
- "If I make less than $50k, I won't be able to support my family."

The slide's punchline: *"The difficult decision of predicting future happiness can be reduced to a series of small, but increasingly specific choices."* That is exactly a decision tree: one big prediction (happy / unhappy) is broken into a chain of simple yes/no tests on features.

**Slide 3 — the definition.**
- A **decision tree** is a graph that represents choices and their results in the form of a tree.
- **Nodes** represent an event or choice; **edges** represent the **decision rules / conditions**.
- It is mostly used in machine learning and data mining applications (the slide says "using Python").

**Mapping the example onto the vocabulary.**

| Idea | Job-offer example |
|---|---|
| Feature (attribute) | commute time, salary, benefits |
| Test at a node | "commute > 1 hour?", "salary < $50k?" |
| Edge | the answer (yes / no) |
| Final outcome (leaf) | happy / unhappy (or accept / reject) |

**Why this is "supervised learning".** In ML the rules are not written by a person; they are *learned* from labelled training data (past offers and whether the person turned out happy). The learning algorithm (ID3 in this lecture, see [[05_ID3_Algorithm_History_and_Greedy_Top_Down_Idea]]) decides which question to ask first, which second, and so on.

**Historical note (research).** Decision-tree learning was formalised independently in the 1980s: Breiman, Friedman, Olshen & Stone's **CART** (1984) and J. Ross Quinlan's **ID3** (paper "Induction of Decision Trees", *Machine Learning*, 1986). Quinlan later produced **C4.5** (1993). All three build the tree top-down and greedily. Because the learned model is just a set of if–then rules, trees are among the most *interpretable* ML models.

---

## 2) Simple English Explanation

**The everyday story (slide 2).** Imagine you have several job offers. Some are close to home, some far; some pay well, some less; some have good benefits. You don't solve this in one giant leap. You make a list of what each job offers (the **features**: commute, pay, benefits) and then make small rules to throw options out:
- "If the commute is longer than an hour, I'll be unhappy" → drop that job.
- "If it pays less than $50k, I can't support my family" → drop that job too.

The teacher's key sentence: a hard decision ("will I be happy?") can be cut into a **series of small, increasingly specific choices**. That series of small choices *is* a decision tree.

**What a decision tree is (slide 3).** It is a drawing that shows choices and what follows from them, shaped like a tree turned upside down:
- Each **box (node)** is a question or an event, e.g. "Is the commute longer than 1 hour?"
- Each **arrow (edge)** is an answer or rule, e.g. "yes" or "no".
- The **ends of the branches** are the final decisions, e.g. "accept" or "decline".

**Matching the story to the words.**
| In the story | Tree word |
|---|---|
| commute time, pay, benefits | **features** (the things we know) |
| "Is the commute > 1 hour?" | a **test** at a node |
| "yes / no" | an **edge** (branch) |
| happy / unhappy, accept / decline | the **leaf** (final answer) |

**Where "machine learning" comes in.** In the story *you* invented the rules. In ML the computer invents them: it studies lots of past, labelled examples (jobs people took and whether they turned out happy) and works out which question to ask first, which second, and so on. The method this lecture teaches for that is called **ID3**.

**A bit of history.** Two groups built these methods independently in the 1980s: **CART** (1984, Breiman and colleagues) and **ID3** (1986, Ross Quinlan), followed by Quinlan's improved **C4.5** (1993). Why trees are loved: the result is just a list of if–then rules, so a person can read and trust it.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Roz-marra ki kahani (slide 2).** Maan lo tumhare paas kai job offers hain. Kisi ka office paas hai, kisi ka door; kisi ki salary achhi hai, kisi ki kam; kisi mein benefits zyada hain. Tum ek chhalaang mein decide nahi karte. Tum har job ki list banate ho ki wo kya deti hai (ye **features** hain: commute, pay, benefits) aur phir chhote-chhote rules se options hata dete ho:
- "Agar commute 1 ghante se zyada hai to main khush nahi rahunga" → wo job hata do.
- "Agar $50k se kam milta hai to ghar nahi chala paunga" → wo bhi hata do.

Sir ka main vaakya: ek mushkil decision ("kya main khush rahunga?") ko **chhote, dheere-dheere specific hote hue choices ki series** mein kaata ja sakta hai. Wahi series ek decision tree hai.

**Decision tree kya hai (slide 3).** Ye ek drawing hai jo choices aur unke natije dikhati hai, ulte tree ki shakal mein:
- Har **box (node)** ek sawaal ya event hai, jaise "Commute 1 ghante se zyada hai?"
- Har **teer (edge)** ek jawaab ya rule hai, jaise "haan" ya "nahi".
- **Branches ke aakhri sire** final decision hain, jaise "accept" ya "decline".

**Kahani ko shabdon se jodo.**
| Kahani mein | Tree ka shabd |
|---|---|
| commute, pay, benefits | **features** (jo humein pata hai) |
| "Commute > 1 ghanta?" | node par **test** |
| "haan / nahi" | **edge** (branch) |
| khush / naakhush, accept / decline | **leaf** (final jawaab) |

**Machine learning kahan aati hai.** Kahani mein rules *tumne* banaye. ML mein rules computer banata hai: wo bahut saare purane, labelled examples dekhta hai (kaun si job logon ne li aur baad mein wo khush the ya nahi) aur khud decide karta hai ki pehla sawaal kaun sa, doosra kaun sa, aur aage. Is kaam ka tareeka jo is lecture mein padhaya jayega wo **ID3** hai.

**Thoda history.** 1980s mein do groups ne alag-alag ye methods banaye: **CART** (1984, Breiman aur saathi) aur **ID3** (1986, Ross Quinlan), phir Quinlan ka behtar version **C4.5** (1993). Trees pasand kyun kiye jaate hain: natija bas if–then rules ki list hota hai, isliye insaan ise padh kar bharosa kar sakta hai.
