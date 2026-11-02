# Topic 3: Worked Tree — "Will Vaibhav Suryavanshi Play Today's Cricket Match?"

Source: Lecture 20, slides 6–11 (one infographic revealed branch by branch across six slides; slides 6–10 are progressive builds, slide 11 is the finished tree). No external research needed — this is a self-contained illustration.

---

## 1) Technical Explanation

**How the slides are built.** Slides 6 → 11 show *one* figure appearing in stages:

| Slide | What is newly revealed |
|---|---|
| 6 | Root: **Match Today?** with branches *Yes* / *No* |
| 7 | *No* → leaf **NO – He Won't Play**; *Yes* → new node **Weather OK?** |
| 8 | Weather OK? → *No* → node **Rain?**; *Yes* → node **Playing XI Announced?** |
| 9 | Rain? → *Yes* → **NO (He Won't Play)**; *No* → **YES – He Plays (weather cleared)** |
| 10 | Playing XI Announced? → *No* → **NO (not in XI yet)**; *Yes* → node **Team Combination?** with branches *Not Favorable* / *Favorable* |
| 11 | Not Favorable → **NO (e.g., specialist needed)**; Favorable → **YES – He Plays**. Tagline: *"Data + Decisions = Better Outcomes"* |

**The complete tree (as plain text).**

```
Match Today?
├─ No  → NO (won't play)
└─ Yes → Weather OK?
          ├─ No  → Rain?
          │         ├─ Yes → NO
          │         └─ No  → YES (weather cleared)
          └─ Yes → Playing XI announced?
                    ├─ No  → NO (not in XI yet)
                    └─ Yes → Team combination?
                              ├─ Not favorable → NO (specialist needed)
                              └─ Favorable     → YES
```

**Reading it as rules.** Each root-to-leaf path is one if–then rule, e.g.
`IF Match Today = Yes AND Weather OK = Yes AND Playing XI = Announced AND Team Combination = Favorable THEN Play = Yes`.
The tree has **5 decision nodes** (Match Today, Weather OK, Rain, Playing XI, Team Combination) and **6 leaves** (2 YES leaves, 4 NO leaves — see table).

| Leaf | Path | Outcome |
|---|---|---|
| 1 | Match=No | NO |
| 2 | Match=Yes, Weather=No, Rain=Yes | NO |
| 3 | Match=Yes, Weather=No, Rain=No | **YES** |
| 4 | Match=Yes, Weather=Yes, XI=No | NO |
| 5 | Match=Yes, Weather=Yes, XI=Yes, Team=Not favorable | NO |
| 6 | Match=Yes, Weather=Yes, XI=Yes, Team=Favorable | **YES** |

So: 5 decision nodes, 6 leaves, depth 4 (longest path = Match → Weather → XI → Team).

**Observations worth noting.**
- Different branches ask *different* follow-up questions (the "No" side of Weather asks about Rain, the "Yes" side asks about the Playing XI). A tree is not a fixed questionnaire; the next question depends on the earlier answers.
- The order puts the most decisive question first: if there is no match at all, nothing else matters (a cheap early exit).
- This figure was drawn by hand/by the instructor — it is **not learned from data** and carries no entropy values. It introduces the *shape* of a tree before the lecture shows how ID3 learns one ([[08_Steps_of_the_ID3_Algorithm]]).
- Slight logic quirk: "Weather OK? = No" followed by "Rain? = No → YES (weather cleared)" means *bad weather but no rain* still lets him play — that is the instructor's design, not a general rule.

---

## 2) Simple English Explanation

**The story.** We want to guess: *will Vaibhav Suryavanshi play today's cricket match?* The teacher draws a tree and shows it growing on six slides, one branch at a time, so you can watch the questions pile up.

**Walk through it, question by question.**
1. **Is there a match today?**
   - **No** → he won't play. *End. (A quick exit — if there's no match, no other question matters.)*
   - **Yes** → go on to question 2.
2. **Is the weather OK?**
   - **No** → ask **Is it raining?**
     - Yes, raining → he won't play.
     - No rain → he **plays** (the weather cleared).
   - **Yes** → ask **Has the playing XI been announced?**
     - **No** → he won't play (he's not confirmed in the team yet).
     - **Yes** → ask **Is the team combination favourable?**
       - Not favourable (for example the team needs a specialist) → he won't play.
       - Favourable → he **plays**.

**Counting the tree.** There are **5 question boxes** (Match today, Weather OK, Rain, Playing XI, Team combination) and **6 answer boxes**: four say "won't play" and two say "plays". The longest path has 4 questions, so the tree is 4 levels deep.

**Every path is a rule.** For example: *If there is a match, the weather is OK, the XI is announced, and the team combination is favourable → he plays.*

**Three things to notice.**
- Different branches ask *different* next questions: the "bad weather" side asks about rain, the "good weather" side asks about the XI. A tree isn't a fixed questionnaire; the next question depends on what you already learned.
- The most decisive question is first (no match = nothing else matters).
- One slightly odd rule: bad weather but no rain still lets him play. That is the teacher's design for the story, not a general rule of cricket.

**Important.** This tree was drawn by the teacher to show the *shape* of a tree. It was **not learned from data** and has no entropy numbers. The next topics show how a computer *learns* a tree from data.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Kahani.** Hume guess karna hai: *kya Vaibhav Suryavanshi aaj ka cricket match khelega?* Sir ek tree banate hain aur 6 slides mein ek-ek branch karke dikhate hain, taaki dikhe ki sawaal kaise jud-jud kar badhte hain.

**Sawaal-dar-sawaal chalo.**
1. **Aaj match hai?**
   - **Nahi** → nahi khelega. *Khatam. (Jaldi nikas — match hi nahi hai to baaki sawaal ka matlab nahi.)*
   - **Haan** → sawaal 2.
2. **Weather theek hai?**
   - **Nahi** → poocho **Barish ho rahi hai?**
     - Haan, barish → nahi khelega.
     - Barish nahi → **khelega** (mausam saaf ho gaya).
   - **Haan** → poocho **Playing XI announce ho gayi?**
     - **Nahi** → nahi khelega (abhi team mein confirm nahi).
     - **Haan** → poocho **Team combination favourable hai?**
       - Favourable nahi (jaise team ko specialist chahiye) → nahi khelega.
       - Favourable → **khelega**.

**Tree ginti.** **5 sawaal wale boxes** hain (Match today, Weather OK, Rain, Playing XI, Team combination) aur **6 jawaab wale boxes**: chaar "nahi khelega" aur do "khelega". Sabse lambe raaste mein 4 sawaal hain, yaani tree 4 level gehra hai.

**Har raasta ek rule hai.** Jaise: *Agar match hai, weather theek hai, XI announce ho gayi aur team combination favourable hai → khelega.*

**Teen baatein dhyan do.**
- Alag branches alag agle sawaal poochti hain: "kharab weather" wali side barish poochti hai, "achha weather" wali side XI poochti hai. Tree koi fixed questionnaire nahi hai; agla sawaal is par depend karta hai ki tumne pehle kya seekha.
- Sabse decisive sawaal sabse pehle hai (match nahi = baaki kuch matter nahi karta).
- Ek thoda ajeeb rule: kharab weather par barish nahi ho to bhi khelta hai. Ye sir ne kahani ke liye banaya hai, cricket ka general rule nahi.

**Zaroori.** Ye tree sir ne tree ki *shakal* dikhane ke liye khud banaya hai. Ye data se **seekha hua nahi** hai aur ismein entropy ke numbers nahi hain. Agle topics mein dikhaya jayega ki computer data se tree kaise *seekhta* hai.
