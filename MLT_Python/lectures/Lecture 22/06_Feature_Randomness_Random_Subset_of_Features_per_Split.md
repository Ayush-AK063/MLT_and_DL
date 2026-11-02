# Topic 6: Feature Randomness — A Random Subset of Features at Each Split

Source: Lecture 22, slide 15 ("Randomization: Feature Randomnsess" [sic]). Enriched with general knowledge of Breiman's random-feature selection and scikit-learn's `max_features` (flagged; not verified beyond what the web search confirmed about Breiman's abstract).

---

## 1) Technical Explanation

**Slide 15 — what it says.**
- In a **normal decision tree**, when it is time to split a node, we consider **every possible feature** and pick the one with the **largest gain** ([[07_Information_Gain_Choosing_the_Best_Attribute]] from Lecture 20).
- In a **random forest**, each tree can pick **only from a random subset of features** (**feature randomness**).
- That is, node splitting is based on a random subset of features.
- This **forces more variation amongst the trees**, resulting in **lower correlation across trees** and **more diversification**.

**Precision note (flag).** The slide says "for each tree", but the standard algorithm (Breiman 2001) draws a **fresh random subset at every node split**, not once per tree. The slide's own second sentence ("node splitting … is based on a random subset") matches this. (Drawing one subset per tree is a different method called the *random subspace method*.)

**Why it is needed.** Suppose one feature is very strong (like Outlook in [[10_Worked_Example_Entropy_of_Subsets_and_Information_Gain_of_Outlook]] from Lecture 20). With bagging alone, nearly every bootstrap tree would still put that feature at the root → all trees look alike → **highly correlated** → voting adds little. Forcing each split to choose among a random handful means some trees must root on *Humidity* or *Wind*, producing diverse trees. (By the variance formula ρσ² + (1 − ρ)σ²/B in [[05_Bagging_Bootstrap_Aggregation]], lowering ρ is what lowers ensemble error.) Breiman's abstract: the forest's error depends on the **strength of the individual trees** and the **correlation between them** — random features trade a little individual strength for a big drop in correlation.

**Illustration (our own, using the lecture-20 dataset).** With 4 features (Outlook, Temp, Humidity, Wind) and a subset of 2 chosen at random at the root, Outlook is available only in some of the draws (here: 3 of the 6 possible pairs contain Outlook); in the other pairs the best available feature will be Humidity (gain 0.152) or Wind (0.048) or Temp (0.029) — so the root differs across trees.

**How many features? (general knowledge, `max_features` in scikit-learn).** Common defaults: **√p** features for classification, p/3 for regression (p = number of features). Small subset → more diverse but weaker trees; large subset → stronger but more correlated. In scikit-learn's classifier the default is `max_features="sqrt"`, which we confirmed on the lecture's digits data: √64 = 8 features per split ([[08_Random_Forest_in_scikit_learn_and_the_Digits_Example]]).

**Summary of the two randomisations.**

| Source of randomness | What is random | Effect |
|---|---|---|
| **Bootstrap (bagging)** | Which *rows* each tree sees | Different training sets → different trees |
| **Feature randomness** | Which *features* each split may use | Different split choices → lower correlation |

---

## 2) Simple English Explanation

**How a normal tree picks its question (slide 15).** At every box a normal tree looks at **all** the columns and picks the one with the **biggest gain** (the best question).

**How a random forest's tree picks.** At every box it is only shown **a few randomly chosen columns**, and it must pick the best question *from those*. This is called **feature randomness** ("feature" = column).

**Why take choices away from the trees?** Suppose one column is super obvious — like Outlook in our tennis table. If every tree is allowed to see it, every tree will ask about it first, and all the trees become near-copies of each other. A vote among copies is no better than a single opinion. By hiding columns at random:
- Some trees can't use Outlook at the top, so they build their top questions around Humidity or Wind instead.
- The trees now ask *different* questions, make *different* mistakes, and so their vote is smarter.

The teacher's words: this forces **more variation** among the trees, giving **lower correlation** across trees and **more diversification**. Think of a committee: you want members with different backgrounds, not clones.

**A small tennis example (ours).** Our table has 4 columns. Suppose each question may see only 2 randomly chosen columns. There are 6 possible pairs; Outlook is in 3 of them. In the other 3 pairs (Temp+Humidity, Temp+Wind, Humidity+Wind) the best available top question would be Humidity or Wind — so different trees start with different questions.

**How many columns should each box see?** A common rule: about the **square root** of the number of columns for category problems (and about a third for number problems). Too few → trees are weak; too many → trees look alike. For the digits example later, with 64 pixel columns, a box sees √64 = 8.

**Two kinds of randomness, side by side.**
| | What is random | Effect |
|---|---|---|
| **Bootstrap (bagging)** | which *rows* each tree sees | different practice sets → different trees |
| **Feature randomness** | which *columns* each question may use | different questions → less alike trees |

**One caution about the slide's wording.** It says "each tree" picks from a random subset. In the standard method the random choice is made **fresh at every box (split)**, not just once per tree — the slide's own second sentence ("node splitting … is based on a random subset") actually says this.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Normal tree apna sawaal kaise chunta hai (slide 15).** Har box par normal tree **saare** columns dekhta hai aur **sabse bade gain** wala (sabse best sawaal) chunta hai.

**Random forest ka tree kaise chunta hai.** Har box par use sirf **kuch random chune hue columns** dikhaye jaate hain, aur use *unhi mein se* best sawaal chunna padta hai. Isse **feature randomness** kehte hain ("feature" = column).

**Trees se choices kyun cheen lein?** Maan lo ek column bahut obvious hai — jaise hamari tennis table mein Outlook. Agar har tree use dekh sakta hai, to har tree pehle usi ke baare mein poochega, aur saare trees lagbhag ek-doosre ki copy ban jayenge. Copies ke beech vote ek akeli raay jaisa hi hai. Columns random chhupa dene se:
- Kuch trees sabse upar Outlook use nahi kar paate, to wo Humidity ya Wind ke aas-paas apne upar ke sawaal banate hain.
- Ab trees *alag* sawaal poochte hain, *alag* galtiyan karte hain, aur isliye unka vote zyada smart hota hai.

Sir ke shabdon mein: isse trees ke beech **zyada variation** aata hai, **correlation kam** hota hai, aur **diversification badhta hai**. Committee ki tarah socho: tumhe alag-alag background wale members chahiye, clones nahi.

**Ek chhota tennis example (humara).** Hamari table mein 4 columns hain. Maan lo har sawaal sirf 2 random chune hue columns dekh sakta hai. 6 possible jodiyan hain; Outlook 3 mein hai. Baaki 3 jodiyon (Temp+Humidity, Temp+Wind, Humidity+Wind) mein sabse upar ka best sawaal Humidity ya Wind hoga — isliye alag trees alag sawaalon se shuru karte hain.

**Har box ko kitne columns dikhein?** Aam rule: category problems ke liye columns ki sankhya ka lagbhag **square root** (aur number problems ke liye lagbhag ek-tihaai). Bahut kam → trees kamzor; bahut zyada → trees ek jaise. Aage digits example mein, 64 pixel columns ke saath, ek box √64 = 8 dekhta hai.

**Do tarah ki randomness, saath-saath.**
| | Kya random hai | Asar |
|---|---|---|
| **Bootstrap (bagging)** | har tree kaun si *rows* dekhta hai | alag practice sets → alag trees |
| **Feature randomness** | har sawaal kaun se *columns* use kar sakta hai | alag sawaal → kam milte-julte trees |

**Slide ke shabdon par ek savdhani.** Wo kehti hai "har tree" random subset se chunta hai. Standard method mein random choice **har box (split) par naya** hota hai, sirf ek baar per tree nahi — slide ka apna doosra vaakya ("node splitting … random subset par based hai") asal mein yahi kehta hai.
