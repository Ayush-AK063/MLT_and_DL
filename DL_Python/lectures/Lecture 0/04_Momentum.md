# Topic 4: Momentum

Source: Lecture 0, Section 4.1 (Momentum) of Ruder's overview paper. Enriched with web research on Polyak's original 1964 "heavy ball" method.

---

## 1) Technical Explanation

SGD struggles in **ravines** — regions where the loss surface curves much more steeply in one dimension than another, which is common near local optima. In a ravine, SGD **oscillates** back and forth across the steep walls while only creeping slowly along the shallow direction toward the actual optimum (see the diagram on the site for this topic — Figure 2a shows this zig-zag pattern on a set of elliptical contour lines).

**Momentum** (Qian, 1999, building on the earlier "heavy ball" idea) fixes this by adding a fraction $\gamma$ of the *previous* update vector to the *current* update vector:

$$v_t = \gamma v_{t-1} + \eta \nabla_\theta J(\theta)$$
$$\theta = \theta - v_t$$

- $\gamma$ (the momentum term) is usually set to **0.9** or a similar value.
- $v_t$ is a running "velocity" — it accumulates a moving average of past gradients, weighted so more recent gradients matter more.

**The physical intuition** (used directly by the paper): imagine pushing a heavy ball down a hill. The ball builds up momentum as it rolls, getting faster and faster (up to a "terminal velocity" set by $\gamma < 1$, analogous to air resistance). The same thing happens to the parameter updates: the momentum term **grows** for dimensions whose gradient keeps pointing in the same direction (like the shallow direction along the ravine's floor) and **shrinks** for dimensions whose gradient keeps flipping sign (like the two steep walls of the ravine, where the gradient alternates back and forth every step). Net effect: **faster convergence** along the useful direction and **reduced oscillation** in the unhelpful direction (Figure 2b on the site shows the much straighter path this produces, compared to 2a).

**Historical origin** (via web research): this exact update rule was first proposed by **Boris Polyak in 1964** as the "heavy ball method," named for precisely this physical analogy — a heavy ball is less affected by small local bumps and curvature than a light one, because its accumulated momentum carries it through them. Polyak proved that, near the solution, the heavy-ball method **accelerates convergence** for strongly-convex problems compared to plain gradient descent. Although Nesterov later developed a version with stronger *global* acceleration guarantees (see the next topic, [[05_Nesterov_Accelerated_Gradient]]), Polyak's original, simpler heavy-ball formulation is still the one most widely used inside deep learning frameworks today, decades later — it is the literal ancestor of the `momentum` argument found in essentially every optimizer implementation.

---

## 2) Simple English Explanation

Picture SGD trying to walk down a steep, narrow canyon (a "ravine") toward the low point far ahead. Instead of walking smoothly along the canyon floor, plain SGD keeps zig-zagging: it takes a step that's mostly *sideways* (toward one canyon wall), overcorrects, takes a step mostly toward the *other* wall, overcorrects again — and only inches forward along the canyon itself with each zig-zag. It's technically making progress, but incredibly inefficiently.

**Momentum** fixes this with a simple idea borrowed from physics: instead of a lightweight ball that reacts instantly and jerkily to every little slope it feels, imagine a **heavy bowling ball** rolling down that same canyon.
- The heavy ball doesn't instantly change direction every time it feels a small sideways nudge — its own weight (its accumulated momentum from all the steps *before* now) keeps carrying it mostly forward.
- Sideways nudges that keep flipping direction (left, right, left, right — the canyon walls) mostly cancel out over time.
- Forward nudges that consistently point the same way (down the canyon) keep *adding up*, so the ball speeds up in that direction.

Net result: the ball takes a much straighter, faster path down the canyon than the light, jittery ball did — exactly what you want from an optimizer.

**Fun fact**: this "heavy ball" idea isn't new to deep learning at all — it was invented by a mathematician named **Boris Polyak all the way back in 1964**, decades before neural networks were trainable at any real scale. It's a genuinely old and well-understood piece of math that deep learning simply adopted because it works so well.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Socho SGD ek tang, gehri canyon (ravine) mein neeche door tak jaana chahta hai, jahan sabse neeche wala point hai. Lekin smoothly canyon ke beech mein chalne ke bajaye, plain SGD baar-baar zig-zag karta hai: pehle ek step zyada *sideways* leta hai (ek canyon wall ki taraf), phir overcorrect karta hai, dusri wall ki taraf jaata hai, phir wapas overcorrect — aur har zig-zag mein canyon ke andar sirf thoda sa hi aage badh paata hai. Progress ho rahi hai, lekin bahut inefficient tarike se.

**Momentum** ise physics ke ek simple idea se fix karta hai: ek halki (light) ball ke bajaye, jo har chhote se slope pe turant aur jerky tarike se react karti hai, socho ek **bhaari bowling ball** usi canyon mein neeche lud'hak (roll) rahi hai.
- Bhaari ball har chhote se sideways push par turant direction nahi badalti — uska apna weight (pichhle sab steps se accumulate hua momentum) use zyadatar aage hi le jaata hai.
- Sideways pushes jo baar-baar direction badalte hai (left, right, left, right — canyon ki walls) time ke saath mostly cancel ho jaate hai.
- Forward pushes jo consistently ek hi direction mein point karte hai (canyon ke neeche ki taraf) wo add hote jaate hai, isliye ball us direction mein speed pakad leti hai.

Result: ball ek bahut zyada straight aur fast raasta leti hai canyon ke neeche, us jittery, halki ball ke comparison mein — bilkul wahi jo ek optimizer se chahiye.

**Interesting baat**: ye "heavy ball" idea deep learning ke liye naya nahi hai — ise ek mathematician **Boris Polyak ne 1964 mein hi** invent kiya tha, neural networks ko kisi real scale pe train karne se dashko pehle. Ye genuinely purana aur well-understood math hai jise deep learning ne bas isliye adopt kiya kyunki ye kaam bahut achhe se karta hai.
