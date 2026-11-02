# Topic 2: Simple Linear Regression — Worked Example (Home Prices)

Source: Lecture 13, slides 4–11 (home price dataset, scatter plot, best-fit line, minimizing squared error, slope/intercept). Independently verified numerically.

---

## 1) Technical Explanation

**The dataset (slide 4).** A small worked dataset of 5 houses is introduced, with a single input feature (`area`, in square feet) and a single target (`price`):

| area | price |
|---|---|
| 2600 | 550000 |
| 3000 | 565000 |
| 3200 | 610000 |
| 3600 | 680000 |
| 4000 | 725000 |

The slide's own annotation labels `area` as the input (I/P) / feature 1, and `price` as the target/Y. The question posed (slide 5): given this data, predict the price of homes with area **3300 sqft** and **5000 sqft** — values that don't appear directly in the table, so we need a model, not a lookup.

**The straight-line model.** The slide reuses the generic line equation **y = mx + b** and relabels it for this problem:

**price = m × area + b**

- **m** is the **slope** (also called the **gradient**) — how much price increases for every 1-unit increase in area.
- **b** is the **y-intercept** — the price the line would predict at area = 0 (not meaningful physically here, but mathematically necessary to position the line).
- (Slide 10 cites [mathsisfun.com/algebra/linear-equations.html](https://www.mathsisfun.com/algebra/linear-equations.html) as the source for the general y = mx + b convention.)

**Plotting and the best-fit line (slides 6–8).** When the 5 (area, price) points are plotted on a scatter plot, they roughly follow an upward trend but don't lie perfectly on any single straight line — this scatter is called the **data distribution**. Slide 6 draws one line through this scatter and calls it the "best fit" line. Slide 8 then shows *three different candidate lines* (drawn in different colours) all passing roughly through the middle of the data cloud, to make the point visually: infinitely many lines could be drawn through/near this scatter, but only **one specific line minimizes the total prediction error** — that is the "best fit" line, and simple linear regression's whole job is to find *that* one.

**How "best fit" is defined mathematically (slide 9).** For any candidate line, and for each actual data point, define:

**Δᵢ = (predicted price at that pointᵢ) − (actual price at that pointᵢ)**

This Δᵢ is the **error** (also called the *residual*) between what the line predicts and what the real data says. The slide shows this visually as the small vertical gap between a red data point and the blue line at that same x-value (labelled Δ1, Δ2 for the first two points). The best-fit line is defined as the one that:

**Minimizes Σᵢ₌₁ⁿ (Δᵢ)²**

i.e., minimizes the **sum of squared errors** across all n data points. Squaring is used (rather than just summing the raw Δᵢ, or summing |Δᵢ|) for two standard reasons that the slide doesn't spell out but are worth knowing: (1) squaring makes every error positive, so overestimates and underestimates don't cancel each other out and hide the true total error; (2) squaring is differentiable everywhere, which is what lets you solve for the minimizing m and b directly with calculus, whereas minimizing the sum of *absolute* errors is mathematically harder (this second approach exists too and is called *Least Absolute Deviations regression*, but ordinary regression by default uses squared error).

**Reading a prediction off the fitted line (slide 7).** Once the best-fit line is found, slide 7 shows the line being used to answer the original question: for **area = 3300**, tracing up to the line and across to the price axis gives a predicted price of **628715** (rounded, shown as "628715" on the slide).

**Independent verification.** The slide never shows the actual computation of m and b for this 5-point dataset (that derivation is only shown later, in the exam-grade example on slides 20–24, using the formula b = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²). Applying that exact same least-squares formula to this 5-point (area, price) dataset gives:

- **m (slope) = 135.7877** (≈ 135.79)
- **b (intercept) = 180616.44**

So the fitted line is **price = 135.7877 × area + 180616.44**. Plugging in area = 3300:

price = 135.7877 × 3300 + 180616.44 = 448,099.32 + 180,616.44 = **628,715.75**

This matches the slide's annotated "628715" essentially exactly (the slide just truncated the decimal) — confirming the annotation is a genuine least-squares fit of this data, not an arbitrary guess. Using the same fitted line for the second query, area = 5000 sqft (left as "?" on the slide):

price = 135.7877 × 5000 + 180616.44 = 678,938.5 + 180,616.44 = **≈ 859,554.79**

Note this is an **extrapolation** — 5000 sqft is outside the range of the training data (2600–4000 sqft) — so this prediction is less trustworthy than the 3300 sqft one, which falls inside the observed range.

Cross-reference: this same slope/intercept vocabulary (m, b; gradient, y-intercept) and the general line equation are formalized again in [[04_Types_of_Regression_Models_Overview]] under Simple Linear Regression, and the *formal* least-squares derivation of m and b is worked step-by-step in [[05_Least_Squares_Method_and_Worked_Example_Exam_Grades]].

---

## 2) Simple English Explanation

Here's the setup: we have 5 real (imaginary, for teaching) houses, and for each one we know its **area** and its **price**. We want a formula that, given any area — even one we've never seen before, like 3300 sqft — spits out a price prediction.

| area (sqft) | price (₹) |
|---|---|
| 2600 | 550000 |
| 3000 | 565000 |
| 3200 | 610000 |
| 3600 | 680000 |
| 4000 | 725000 |

You can see the pattern already: bigger house → bigger price, roughly. If you plot these 5 points on a graph (area on the bottom, price on the side), they roughly go up-and-to-the-right, but not in a perfectly straight line — there's some scatter/noise.

**The model is just a straight line**: `price = m × area + b`, the same "y = mx + b" you learned in school algebra. Here:
- **m (slope)** tells you: for every extra sqft of area, how much more expensive does the house get?
- **b (intercept)** is just a constant that shifts the whole line up or down so it lines up with the data (it doesn't mean "a 0 sqft house costs ₹b" — that's not realistic, it's just math).

**Which line is the "best" one?** You could draw *lots* of straight lines roughly through this scatter of points — the slide literally shows 3 different lines drawn through the same data (slide 8) to prove this point. But only one of them is truly "best": the one where, if you measure the gap between each real point and the line (called the **error**), and square each gap, and add all those squared gaps together — that total is as small as possible. This is called **minimizing the sum of squared errors**, and it's the mathematical definition of "best fit line."

Why square the errors instead of just adding them up normally? Because some points are above the line (positive error) and some are below (negative error) — if you just added them, the pluses and minuses would cancel out and you'd wrongly think the line is perfect even when it isn't. Squaring makes every error positive first, so they all genuinely count toward the total.

**Using the line to predict**: once you have the best line, you plug in any area you want. Slide 7 shows this for area = 3300 sqft: tracing up from 3300 on the x-axis to the blue line, then across to the price axis, gives **₹628,715**. I recomputed the actual best-fit line from this exact 5-point data using the standard least-squares formula, and got m ≈ 135.79 and b ≈ 180,616 — plugging area = 3300 into that gives **₹628,715.75**, matching the slide's number essentially exactly. So the slide's answer checks out.

For area = 5000 sqft (the other question the slide asks but leaves blank), the same line predicts about **₹859,555** — but this one is a bit riskier to trust, because 5000 sqft is bigger than every house in our training data (which only goes up to 4000 sqft). Predicting outside the range of data you've seen is called **extrapolation**, and it's generally less reliable.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Setup yeh hai: humare paas 5 (fake, teaching ke liye) ghar hain, aur har ghar ka **area** aur **price** pata hai. Humein ek formula chahiye jo koi bhi area doge — chahe wo pehle kabhi nahi dekha ho, jaise 3300 sqft — uska price predict kar de.

| area (sqft) | price (₹) |
|---|---|
| 2600 | 550000 |
| 3000 | 565000 |
| 3200 | 610000 |
| 3600 | 680000 |
| 4000 | 725000 |

Pattern clear hai: jitna bada ghar, utni zyada price, roughly. Agar in 5 points ko graph pe plot karo (neeche area, side mein price), toh roughly upar-daayein jaate hain, lekin bilkul straight line mein nahi — thoda scatter/noise hai.

**Model bas ek straight line hai**: `price = m × area + b`, wahi school wala "y = mx + b". Yahan:
- **m (slope)** batata hai: har extra sqft area ke liye, ghar kitna mehenga hota hai?
- **b (intercept)** bas ek constant hai jo poori line ko upar-neeche shift karta hai taaki wo data ke saath match ho jaaye (iska matlab yeh nahi ki "0 sqft ghar ki price ₹b hai" — wo realistic nahi hai, bas math ke liye zaroori hai).

**Konsi line "best" hai?** Is scatter ke through bahut saari straight lines draw ki ja sakti hain — slide mein literally 3 alag lines dikhayi gayi hain same data ke through (slide 8) yehi point prove karne ke liye. Lekin sirf ek line hi truly "best" hai: wo jismein, har real point aur line ke beech ka gap (jise **error** bolte hain) nikalo, har gap ko square karo, aur sabko add karo — us total ko sabse kam karna hai. Ise **sum of squared errors ko minimize karna** bolte hain, aur yehi "best fit line" ki mathematical definition hai.

Errors ko square kyu karte hain, seedha add kyu nahi karte? Kyunki kuch points line ke upar hote hain (positive error) aur kuch neeche (negative error) — agar seedha add karoge, toh plus-minus cancel ho jayenge aur galat lagega ki line perfect hai jabki nahi hai. Square karne se har error positive ho jaata hai, toh sab genuinely count hote hain total mein.

**Line se predict karna**: best line mil jaane ke baad, koi bhi area daal ke price nikal sakte ho. Slide 7 mein 3300 sqft ke liye yehi dikhaya hai: 3300 se upar jaake line tak, phir line se price axis tak — jawab aata hai **₹628,715**. Maine isi 5-point data se best-fit line khud nikaali standard least-squares formula se, aur mila m ≈ 135.79 aur b ≈ 180,616 — 3300 area daalne pe **₹628,715.75** aata hai, jo slide ke number se essentially exactly match karta hai. Toh slide ka answer sahi hai.

5000 sqft ke liye (dusra sawaal jo slide poochti hai par khaali chhod deti hai), same line se predict hota hai lagbhag **₹859,555** — lekin isme thoda risk hai, kyunki 5000 sqft humare training data ke sabse bade ghar (4000 sqft) se bhi bada hai. Apne dekhe hue data range se bahar predict karna **extrapolation** kehlata hai, aur yeh generally utna reliable nahi hota.
