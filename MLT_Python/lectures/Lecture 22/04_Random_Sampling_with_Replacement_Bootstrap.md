# Topic 4: Random Sampling with Replacement (the Bootstrap)

Source: Lecture 22, slide 12 ("Random Sampling with Replacement"). Enriched with independently computed probabilities (exact and simulated) and general statistics knowledge (out-of-bag samples, the 63.2% rule).

---

## 1) Technical Explanation

**Slide 12 — the idea.**
- Randomly sample from the training dataset **with replacement**.
- Training set **S of size m** → build new training sets by drawing **m samples at random from S with replacement** (the same sample can be picked several times).
- Example: training data **[1, 2, 3, 4, 5, 6]** may give **[1, 2, 2, 3, 6, 6]**, **[1, 2, 4, 4, 5, 6]**, **[1, 1, 1, 1, 1, 1]**, …
- All lists have length 6 but some values repeat. **We are not subsetting the data into smaller chunks** — every new set is the *same size* as the original.

**Check of the slide's examples.** All three are valid length-6 draws with replacement. The number of equally likely ordered samples is 6⁶ = **46,656**. The "all ones" sample [1,1,1,1,1,1] has probability (1/6)⁶ = **2.1×10⁻⁵** (0.0021%) — possible but extremely rare; the chance that *all six draws are the same value*, whichever value, is 6·(1/6)⁶ = **1.3×10⁻⁴** (0.013%).

**How many distinct rows does a bootstrap sample contain? (computed)**
- Probability a given row is **never** picked in m draws = (1 − 1/m)^m.
- Expected fraction of **distinct** rows = 1 − (1 − 1/m)^m: **m = 6 → 66.5%** (simulation of 100,000 draws gave 66.49% ✔), m = 100 → 63.4%, m = 1000 → 63.2%, and in the limit 1 − 1/e ≈ **63.2%**.
- So a typical bootstrap sample of m rows contains **about 63.2% of the original rows (some repeated)**; the remaining **≈ 36.8%** are left out — called **out-of-bag (OOB)** rows for that tree. (Not on the slides.) OOB rows act as a free built-in validation set: each row can be predicted by only the trees that never saw it, giving an honest error estimate without a separate test set ([[05_Bagging_Bootstrap_Aggregation]]).

**Sampling *with* vs *without* replacement.**

| | With replacement (bootstrap) | Without replacement |
|---|---|---|
| Same row repeated? | Yes | No |
| Result size m of m? | Yes, same size (but ~63% distinct) | Only a smaller subset, or the identical set |
| Independence between draws | Yes — each draw identical distribution | No |
| Use in RF | Standard (bagging) | Used by some variants / sub-sampling |

**Why do this?** Each tree sees a **different but similar** dataset, so the trees come out different. Repeats effectively give some rows a higher weight in one tree and zero weight in another — injecting diversity that decorrelates the trees ([[02_Wisdom_of_the_Crowd_Choosing_a_Phone_with_Three_Friends]]).

---

## 2) Simple English Explanation

**The lottery-ball picture.** Imagine your six data points are six numbered balls (1 to 6) in a bag. To make a **bootstrap sample**:
1. Pull out one ball and write down its number.
2. **Put the ball back** into the bag.
3. Repeat until you've written down six numbers.

Because every ball goes back, the same number can come up twice, three times, or not at all.

**Examples from the slide (data = [1, 2, 3, 4, 5, 6]).**
- [1, 2, 2, 3, 6, 6] — 2 and 6 appear twice; 4 and 5 are missing.
- [1, 2, 4, 4, 5, 6] — 4 appears twice; 3 is missing.
- [1, 1, 1, 1, 1, 1] — the same ball six times! Possible, but very unlikely: the chance is 1 in 46,656 (that's 6 × 6 × 6 × 6 × 6 × 6 equally likely lists).

**The slide's important point: it is *not* smaller.** Every new list has **exactly the same length** as the original (six). We are not chopping the data into smaller pieces. Some items appear more than once and some are left out.

**How many different items end up in a sample?** For a long list, on average only about **two-thirds (63%)** of the original items make it in; the other **one-third (37%)** are left out. (Checked: for just six items it is 66.5% — about 4 distinct numbers out of 6.) The items left out for one tree are called its **out-of-bag** items. They're handy: they work as free "exam questions" that that tree never studied.

**With replacement or without?**
- *With replacement* (the bootstrap): repeats allowed, list is the same size as the original.
- *Without replacement*: no repeats, so you can only get a smaller piece of the data.

**Why bother?** Each tree in the forest gets its own bootstrap sample, so each sees a *slightly different* version of the data — some rows twice, some rows not at all. Different data → different trees → different mistakes → a better vote. That's the "random" in random forest.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Lottery-ball ki picture.** Socho tumhare chhe data points ek thaile mein chhe numbered balls (1 se 6) hain. **Bootstrap sample** banane ke liye:
1. Ek ball nikaalo aur uska number likh lo.
2. **Ball ko wapas thaile mein daal do.**
3. Tab tak dohraao jab tak chhe numbers likh na jayein.

Kyunki har ball wapas jaati hai, ek hi number do baar, teen baar aa sakta hai, ya bilkul nahi bhi aa sakta.

**Slide ke examples (data = [1, 2, 3, 4, 5, 6]).**
- [1, 2, 2, 3, 6, 6] — 2 aur 6 do-do baar; 4 aur 5 gayab.
- [1, 2, 4, 4, 5, 6] — 4 do baar; 3 gayab.
- [1, 1, 1, 1, 1, 1] — wahi ball chhe baar! Ho sakta hai, par bahut mushkil: chance 46,656 mein se 1 (yaani 6 × 6 × 6 × 6 × 6 × 6 barabar-sambhav lists).

**Slide ki zaroori baat: ye chhota *nahi* hota.** Har nayi list ki **length bilkul original jitni** (chhe) hoti hai. Hum data ko chhote tukdon mein nahi kaat rahe. Kuch items ek se zyada baar aate hain aur kuch chhoot jaate hain.

**Ek sample mein kitne alag items aate hain?** Lambi list ke liye average mein sirf **do-tihaai (63%)** original items aate hain; baaki **ek-tihaai (37%)** chhoot jaate hain. (Check kiya: sirf chhe items ke liye 66.5% — chhe mein se lagbhag 4 alag numbers.) Ek tree ke liye jo items chhoot gaye unhe uske **out-of-bag** items kehte hain. Ye kaam ke hain: ye free "exam ke sawaal" hain jo us tree ne kabhi padhe hi nahi.

**With replacement ya without?**
- *With replacement* (bootstrap): repeats allowed, list original jitni badi.
- *Without replacement*: koi repeat nahi, isliye data ka sirf chhota tukda mil sakta hai.

**Ye sab kyun?** Forest ke har tree ko apna bootstrap sample milta hai, isliye har tree data ka *thoda alag* version dekhta hai — kuch rows do baar, kuch bilkul nahi. Alag data → alag trees → alag galtiyan → behtar vote. Random forest ka "random" yahi hai.
