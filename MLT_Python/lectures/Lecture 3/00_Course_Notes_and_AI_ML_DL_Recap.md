# Topic 0: Course Notes (Pac-Man Assignment) & AI/ML/DL Recap

Source: Lecture 3, slides 2–4 (Recap: AI/ML/DL, Assignments: Pac-Man, Maximize Your Expected Utility).

---

## 1) Technical Explanation

**Recap (slide 2)**: The lecture restates the AI/ML/DL nested hierarchy and its relationship to Data Science, exactly as covered previously — `AI ⊃ ML ⊃ DL`, with Data Science overlapping all three by adding statistics, programming, and domain expertise to extract insights and predictions from data. (Full explanation already in Lecture 2, Topic 4 — [[04_AI_ML_DL_Hierarchy_and_Data_Science]].)

**Assignments: Pac-Man (slide 3)**: The course references the classic **Pac-Man AI project**, originally developed at UC Berkeley for their introductory AI course (CS188). In this well-known assignment framework, students implement search algorithms, adversarial game-tree search (minimax, alpha-beta pruning), and later reinforcement learning agents to control Pac-Man navigating a maze while avoiding ghosts and eating pellets — a standard, hands-on way to apply AI/ML concepts (search, planning, decision-making under uncertainty) taught throughout the course. This signals that lab/assignment work in ES514 will likely draw on this well-established teaching framework.

**"Maximize Your Expected Utility" (slide 4)**: This is a short divider slide introducing the **core organizing principle behind rational-agent-based AI** (tying back to the "Act Rationally" definition of AI from Lecture 2, Topic 3 — [[03_Definitions_of_AI]]). An intelligent agent is one that, given uncertain outcomes, chooses the action that maximizes its **expected utility** — i.e., the probability-weighted average of the "value"/reward of each possible outcome. This concept threads through the rest of the lecture (game-playing agents, robotics, decision-making tools) — every application shown afterward can be understood as a system trying to maximize some expected utility (winning a game, avoiding collisions, predicting accurately, making a profitable recommendation, etc.).

---

## 2) Simple English Explanation

This is a short "housekeeping and connecting-the-dots" section before diving into the main lecture on ML applications.

- **AI/ML/DL Recap**: A quick reminder of the same nested-circles diagram from last lecture — AI is the big idea, ML is a part of it, and DL is a part of ML. (Already explained in detail in Lecture 2.)
- **Pac-Man Assignment**: The course mentions that lab assignments will likely use the famous **Pac-Man** game — a tool originally built at UC Berkeley to teach AI. Students will write code that controls Pac-Man's decisions (which way to move, how to avoid ghosts) using AI techniques.
- **"Maximize Your Expected Utility"**: This phrase is the single big idea that connects everything else in this lecture. It means: a smart/rational system, when faced with choices and uncertain outcomes, should pick the action that gives it the best expected result on average. Every example shown later in the lecture — a chess-playing AI, a self-driving car, a recommendation system — is, underneath, trying to do exactly this: pick the action that's expected to work out best.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye lecture ka shuruaati hissa hai jisme thoda "recap" aur agle topics ka connection samjhaya gaya hai.

**AI/ML/DL Recap:**
Pichhle lecture wala hi diagram phir dikhaya gaya hai — **AI sabse bada, uske andar ML, uske andar DL**, aur Data Science sabko overlap karta hai. (Ye detail mein Lecture 2 mein already cover ho chuka hai — [[04_AI_ML_DL_Hierarchy_and_Data_Science]] dekho.)

**Pac-Man Assignment:**
Course mein bataya gaya hai ki lab assignments ke liye **Pac-Man game** use hoga — ye ek famous tool hai jo UC Berkeley university ne AI sikhane ke liye banaya tha. Students Pac-Man ko control karne wala code likhenge — jaise Pac-Man ko decide karna hoga kis taraf jaana hai, ghosts (bhoot) se kaise bachna hai — ye sab AI techniques use karke.

**"Maximize Your Expected Utility" (Apni Expected Utility ko Maximum karo):**
Ye is poore lecture ka **sabse bada connecting idea** hai. Iska matlab hai:
- Agar ek smart system ke paas multiple choices hai, aur har choice ka result thoda uncertain (na-pakka) hai,
- to wo system aisa action choose karega jo **average mein sabse achha result** de.

**Simple example se samjho**: Socho aap ek lottery khel rahe ho jisme 2 options hai — Option A mein 50% chance hai ₹100 jeetne ka, Option B mein 90% chance hai ₹50 jeetne ka. "Expected value" nikaalo: Option A = 0.5 × 100 = ₹50, Option B = 0.9 × 50 = ₹45. To rational (samajhdar) player Option A choose karega kyunki uska expected value zyada hai.

Yehi concept aage jitne bhi examples aayenge lecture mein — chess khelne wala AI, self-driving car, recommendation system — sabme yehi ho raha hai: system apni **expected utility ko maximize** karne ki koshish kar raha hai.
