# Topic 5: Comparing Different Beta Values, Visually

Source: Lecture 12 (ES532: Introduction to Deep Learning), slide 9 (numbered **28** in the printed corner — see the note on the slide-number gap below).

---

## 1) Technical Explanation

**A note on the source material before the content itself**: this slide is numbered **28** in its printed corner, while the previous topic's slide was numbered **23** — meaning slides **24 through 27 are missing** from this PDF as supplied (four slides' worth of content isn't present in the source file). This gap is flagged here explicitly rather than silently skipped over; the content that would have filled it isn't reconstructed or guessed at, since doing so would mean inventing material not actually in the source.

**The content that is present**: three scatter plots of the same underlying noisy dataset (the same style of scatter seen in [[02_What_Is_an_Exponentially_Weighted_Moving_Average]]), each overlaid with the EWMA smoothing line $V_t = \beta \cdot V_{t-1} + (1-\beta)\cdot\theta_t$ computed at a **different value of $\beta$**:

- **$\beta=0.9$**: a smooth curve that tracks the data's overall shape without following every individual bump.
- **$\beta=0.6$**: a noticeably **less smooth**, more jagged curve that follows the raw data points more closely, with visible up-and-down wiggles.
- **$\beta=0.95$**: the **smoothest** of the three, tracking the broad trend even more loosely than the $\beta=0.9$ curve.

**Why this ordering makes sense**, directly following from [[04_General_EWMA_Formula_and_Effect_of_Beta]]: a larger $\beta$ means each new data point is blended in with a *smaller* weight, $(1-\beta)$, so any single noisy reading has less power to jerk the average around — producing a smoother curve that reacts more slowly to sudden changes. A smaller $\beta$ (like 0.6) gives new data points much more weight, $(1-\beta)=0.4$, so the average reacts quickly to each new value — tracking the noise more closely, at the cost of looking jagged.

**The slide's own final annotation, verified against this pattern**: "if $\beta>0.9$, [the curve is] much smoother, [with] increased horizontal direction [movement and] decreased vertical direction [movement]" — this is exactly the $\beta=0.95$ case shown, and confirms the general rule from [[04_General_EWMA_Formula_and_Effect_of_Beta]]: **higher $\beta$ → smoother → more horizontal, less vertical movement**, when this same tool is later applied to gradient updates in [[06_Momentum_Applied_to_Gradient_Descent_Updates]].

**The practical trade-off this implies**: too low a $\beta$ (like 0.6) doesn't smooth out enough of the noise to be useful; too high a $\beta$ risks the average lagging so far behind that it's slow to react to genuine changes in the underlying trend (not shown explicitly on this slide, but a direct consequence of the same math — a curve smooth enough to ignore noise is also, by the same mechanism, slower to notice a real shift). This is exactly why $\beta \approx 0.9$ is the standard practical default (already noted via web research back in Lecture 11's [[05_Choosing_Batch_Size_and_the_Momentum_EWMA_Preview]]) — a reasonable middle ground between these two failure modes.

---

## 2) Simple English Explanation

**A quick, honest note first**: this slide's own page number jumps from 23 straight to 28 in this deck — meaning four slides' worth of content between them is simply missing from the file the instructor supplied. That gap is being pointed out here rather than pretending nothing is missing or guessing what might have been on those slides.

**What this slide actually shows**: the same noisy, jumpy dataset from a couple of topics ago, plotted three separate times, each with a differently-smoothed EWMA line drawn over it:

- **$\beta = 0.9$**: a nicely smooth line, following the big-picture shape without chasing every wiggle.
- **$\beta = 0.6$**: a much bumpier, less smooth line — it reacts more to each individual data point, so it wiggles along with the noise more.
- **$\beta = 0.95$**: the smoothest line of the three — it barely reacts to individual bumps at all, tracking only the broadest trend.

**Why this happens**: a bigger $\beta$ means each brand-new data point only gets a small say in updating the average (since its weight is $1-\beta$, which shrinks as $\beta$ grows) — so the average changes slowly and smoothly. A smaller $\beta$ gives each new point a much bigger say, so the average jumps around more, tracking the noise more closely.

**The trade-off worth understanding**: too little smoothing (a low $\beta$) and you haven't actually gotten rid of much noise; too much smoothing (a very high $\beta$) and the average becomes sluggish, slow to notice when the real underlying trend actually shifts. That's exactly why $\beta \approx 0.9$ tends to be the standard, sensible default in practice — enough smoothing to genuinely help, without becoming too sluggish to be useful.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Pehle ek quick, honest note**: is slide ka apna page number 23 se seedha 28 pe jump karta hai is deck mein — matlab beech mein chaar slides ka content simply missing hai us file se jo instructor ne diya. Ye gap yahan point out kiya ja raha hai, pretend karne ke bajaye ki kuch missing nahi hai ya guess karne ke bajaye ki un slides mein kya ho sakta tha.

**Ye slide actually kya dikhati hai**: kuch topics pehle wala wahi noisy, jumpy dataset, teen alag baar plot kiya hua, har ek par ek differently-smoothed EWMA line draw ki hui:

- **$\beta = 0.9$**: ek nicely smooth line, big-picture shape follow karte hue har wiggle chase kiye bina.
- **$\beta = 0.6$**: ek bahut zyada bumpy, kam smooth line — ye har individual data point pe zyada react karti hai, isliye noise ke saath zyada wiggle karti hai.
- **$\beta = 0.95$**: teeno mein sabse smooth line — ye individual bumps par lagbhag react hi nahi karti, sirf sabse broad trend track karti hai.

**Ye kyun hota hai**: ek bada $\beta$ ka matlab hai har bilkul naya data point average update karne mein sirf ek chhota say pata hai (kyunki uska weight $1-\beta$ hai, jo $\beta$ badhne par shrink hota hai) — isliye average slowly aur smoothly badalta hai. Ek chhota $\beta$ har naye point ko bahut bada say deta hai, isliye average zyada bounce karta hai, noise ko zyada closely track karta hai.

**Samajhne layak trade-off**: bahut kam smoothing (kam $\beta$) aur tumne actually zyada noise se chutkara nahi paya; bahut zyada smoothing (bahut high $\beta$) aur average sluggish ho jaata hai, slow ho jaata hai notice karne mein ki asli underlying trend actually kab shift hui. Yahi exact wajah hai ki $\beta \approx 0.9$ practice mein standard, sensible default hota hai — enough smoothing jo genuinely help kare, bahut sluggish hue bina ki useful hi na rahe.
