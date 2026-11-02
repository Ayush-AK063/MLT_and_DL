# Topic 0: Recap — The Job-Offer Decision Tree and the Instructor's Handwritten Examples

Source: Lecture 22, slides 2–3 ("RECAP", two slides). Slide 3 shows the typed job-offer tree; slide 2 is the same tree icon covered in the instructor's handwriting. Builds on [[01_Job_Offer_Example_and_What_Is_a_Decision_Tree]] and [[02_Tree_Structure_Terminology_and_Where_Trees_Are_Used]] from Lecture 20.

---

## 1) Technical Explanation

**Slide 3 — the job-offer tree (typed figure).**

```
Salary at least $50,000?                       <- root node (decision node)
├─ no  → Decline offer                          <- leaf
└─ yes → Commute more than 1 hour?              <- decision node
           ├─ yes → Decline offer               <- leaf
           └─ no  → Offers free coffee?         <- decision node
                      ├─ yes → Accept offer     <- leaf
                      └─ no  → Decline offer    <- leaf
```

The figure labels the **root node**, the **decision nodes** and the **leaf nodes** — exactly the vocabulary of Lecture 20. It has 3 decision nodes, 4 leaves, depth 3; **only one path (salary ≥ 50k, commute ≤ 1 hr, free coffee) ends in "accept"**. Instructor's red marks: ✗ on each "decline" leaf, "Yes/No" on the job-offer picture, and word-labels on the three questions — *Salary*, **"Travel"** (commute) and **"Complimentary"** (free coffee) — plus **"FIKA"** (the Swedish tradition of a coffee break; the instructor's side-remark on the coffee perk).

**Slide 2 — handwritten recap notes (partly legible).** The instructor re-uses the tree to list *features* that could matter in a real job decision: **Salary, Distance from home, Job profile, Holiday, Working hrs.** Around it are several asides that show where tree-style reasoning appears in practice or in conversation. As far as it can be read:
- an aside on top-ranked AI venues (**NeurIPS, "A\*" ranking**) and on **LLM hallucination / "AI escaping"** — not developed on any later slide;
- a **food-delivery flow drawn as a decision sequence** (Zomato/Swiggy order vs. Domino's, "30 min"): ① order accepted, ② check order/customization/message, ③ added, ④ prepare pizza, ⑤ look for delivery partner (20 mins), ⑥ delivery in 53 mins, ⑦ completed, ⑧ payment/vendor;
- a small box **A–B–C–D "Safe order / Take risk"** labelled "risky step".

*Flag:* much of this handwriting is hard to read, so the details above are best-effort; none of it is used again in the lecture's technical content. The takeaway the instructor is drawing is that **a real decision is a chain of small yes/no checks on features** — a decision tree.

**Why this recap matters here.** A single tree is easy to read but *unstable* and prone to overfitting ([[02_Overfitting_vs_Underfitting_Bias_and_Variance]] from Lecture 17). Random forests, the topic of this lecture, repair that by combining many trees ([[01_What_Is_a_Random_Forest_Breiman_2001]]).

---

## 2) Simple English Explanation

**A reminder of last lecture's tree: "Should I accept this new job?"**
1. **Is the salary at least $50,000?** If **no** → decline the offer.
2. If **yes** → **Is the commute longer than 1 hour?** If **yes** → decline.
3. If **no** → **Does the office offer free coffee?** **Yes** → accept. **No** → decline.

Only *one* path ends in "accept": good salary, short commute and free coffee. Every other path ends in "decline". On the picture the top question is the **root**, each question box is a **decision node**, and each final answer is a **leaf**. The teacher put a red ✗ on each "decline" leaf, labelled the three questions **Salary**, **Travel** and **Complimentary** (the free coffee), and wrote **"FIKA"** — a Swedish word for a relaxed coffee break.

**The teacher's handwritten extras (slide 2).** Around the tree he listed features that could matter in a real job decision: salary, distance from home, job profile, holidays, working hours. He also drew a few side examples to show that everyday processes are chains of checks — for instance an online pizza order: order accepted → check the customisation → added → pizza prepared → look for a delivery partner → delivered → payment. (The handwriting is hard to read, so the details of these side notes are best-effort, and a couple of other asides — about AI conferences and AI models making things up — are not developed anywhere else in the lecture.)

**Why this recap, and why it matters today.** A single decision tree is easy to read, but it is **jumpy**: change a few of the training examples and you may get a quite different tree; and a tree grown until every box is pure may just memorise the training data. Today's topic, the **random forest**, fixes this by asking *many* trees and taking a vote.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Pichhle lecture ke tree ki yaad: "Kya mujhe ye nayi job accept karni chahiye?"**
1. **Salary kam se kam $50,000 hai?** Agar **nahi** → offer decline.
2. Agar **haan** → **Commute 1 ghante se zyada hai?** Agar **haan** → decline.
3. Agar **nahi** → **Office mein free coffee milti hai?** **Haan** → accept. **Nahi** → decline.

Sirf *ek* raasta "accept" par khatam hota hai: achhi salary, chhota commute aur free coffee. Baaki har raasta "decline" par. Picture mein sabse upar ka sawaal **root** hai, har sawaal ka box **decision node** hai, aur har final jawaab **leaf** hai. Sir ne har "decline" leaf par laal ✗ lagaya, teeno sawaalon ko **Salary**, **Travel** aur **Complimentary** (free coffee) naam diye, aur **"FIKA"** likha — Sweden ka ek shabd jiska matlab aaram wala coffee break hai.

**Sir ke haath se likhe extras (slide 2).** Tree ke aas-paas unhone wo features likhe jo asli job decision mein matter kar sakte hain: salary, ghar se doori, job profile, holidays, working hours. Saath mein kuch side examples bhi banaye ye dikhane ke liye ki roz ki cheezein bhi checks ki chain hain — jaise online pizza order: order accept → customization check → add → pizza ban raha hai → delivery partner dhoondho → delivery → payment. (Likhawat padhna mushkil hai, isliye in side notes ki details best-effort hain, aur ek-do aur baatein — AI conferences aur AI models ke jhooth bolne ke baare mein — lecture mein aur kahin develop nahi hui.)

**Ye recap kyun, aur aaj kyun zaroori.** Ek akela decision tree padhna aasan hai, par wo **jumpy** hota hai: training examples thode badlo to kaafi alag tree ban sakta hai; aur jo tree tab tak ugaya jaye jab tak har box pure na ho wo training data ko ratt sakta hai. Aaj ka topic, **random forest**, ise theek karta hai: *bahut saare* trees se poochho aur vote lo.
