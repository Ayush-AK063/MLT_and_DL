# Topic 2: The Problem Space — Hard for Humans vs Hard for Computers

Source: Lecture 1, slides 6–11 (Introduction, Problem space — built up over six slides).

---

## 1) Technical Explanation

The lecture builds one slide up line by line:

1. **Definition.** A *problem* is "a matter or situation regarded as unwelcome or harmful and needing to be dealt with and overcome".
2. **Goal.** The target is to solve such problems **on a computer**.
3. **Category A — intellectually hard for humans, easy for a computer.** Examples: the *Travelling Salesman Problem* and *chess*. These have a precise formal statement, so a program can be written down directly (even if it is expensive to run).
4. **Category B — easy for ordinary people, hard for a computer, even to *express* formally.** Example: *identifying an object, e.g. a car, in a picture*.
5. **Focus of the course:** "Primary focus will be in the second category."

**Why Category B is hard.** A human recognises a car instantly, but cannot write down the rules he/she is using. Any hand-written rule ("it has four circular wheels") breaks on angle, lighting, occlusion, colour or model — see [[01_Traditional_vs_End_to_End_Learning_and_Hand_Designed_Features]] in Lecture 2, which uses this same "identify a car" example. Deep learning is the family of methods built for exactly this category: instead of writing the rule, the system *learns* it from examples ([[04_Problem_Solving_Strategies_for_Big_Data]], [[07_Traditional_Programming_vs_ML_and_the_AI_Hierarchy]]).

This distinction is an old observation in AI (often called *Moravec's paradox*: tasks effortless for humans, like perception, are hard for machines, while tasks hard for humans, like formal search or arithmetic, are easy for machines). The slide does not name it; it is mentioned here as extra context.

---

## 2) Simple English Explanation

Think of two kinds of problems.

- **Type 1:** problems that make *people* sweat but that a computer handles well — e.g. planning the shortest route through 20 cities, or playing chess. You can describe the rules exactly, so the computer just follows them very fast.
- **Type 2:** problems that a small child does easily but that are very hard to explain to a computer — e.g. "is there a car in this photo?" You cannot easily write rules for it, because you do not consciously know how your own brain does it.

This course is mostly about **Type 2** problems.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Do tarah ki problems sochiye.

- **Type 1:** jo insaan ko sochne par majboor kar dein par computer ke liye aasan hon — jaise 20 shehron ka sabse chhota raasta nikalna, ya chess khelna. Rules exactly bataye ja sakte hain, to computer unhe bas bahut tezi se follow karta hai.
- **Type 2:** jo ek chhota bachcha aasani se kar leta hai par computer ko samjhana bahut mushkil hai — jaise "is photo mein car hai ya nahi?" Iske rules likhna mushkil hai, kyunki hume khud nahi pata ki hamara dimaag ye kaise karta hai.

Ye course zyada tar **Type 2** problems ke baare mein hai.
