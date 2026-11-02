# Topic 1: What Is Regression? Relationships and Variables

Source: Lecture 13, slides 1–3 (Regression Basics outline, "What is Regression?", Examples). Enriched with web research (history of the term "regression" — Francis Galton, 1886).

---

## 1) Technical Explanation

**Lecture outline (slide 1).** This lecture covers three things: (1) what regression is, (2) how a Simple Linear Regression analysis is done, and (3) a fully worked example.

**Relationships between variables (slide 2).** In science and data analysis, we frequently measure two or more variables on the same individual/case/object to explore the *nature of the relationship* between them. The slide names two basic categories:

- **Cause-and-effect relationships** — one variable directly causes a change in another (e.g., dosage of a drug causing a change in blood pressure).
- **Functional relationships** — a mathematical relationship that lets us *predict* what value of one variable corresponds to a given value of another, without necessarily claiming causation.

A **function** is defined on the slide as: *a mathematical relationship enabling us to predict what values of one variable (Y) correspond to given values of another variable (X)*, written **Y = f(X)**. The handwritten annotation on the slide gives a concrete instance of this: `Housing → area, Rooms, Year of development → forecast price`, i.e., a house's area, number of rooms, and how developed/old the area is are used to forecast its price. This is exactly the running example used for the rest of the lecture (home price prediction).

- **Y (dependent variable)** — also called the *response variable* or the *predicted variable*. This is the outcome we want to estimate (e.g., house price).
- **X (independent variable)** — also called the *explanatory variable* or the *predictor variable*. This is the input we use to make the prediction (e.g., area).

**Examples (slide 3).** The slide pairs up several real-world Y/X examples, each read as "**Y is a function of X**":

| Y (dependent / response) | X (independent / explanatory) |
|---|---|
| Time needed to fill a soft-drink vending machine | Number of cases needed to fill the machine |
| Tensile strength of wrapping paper | Percent of hardwood in the pulp batch |
| Percent germination of begonia seeds | Intensity of light in an incubator |
| Mean litter weight of test rats | Litter size |
| Maintenance cost of tractors | Age of the tractor |
| Repair time for a computer | Number of components that have to be changed |

The handwritten annotations on the slide connect two of these rows visually: "litter size" is marked as an independent variable example (labelled x₁, x₂, x₃ — i.e., a feature that could take many values), while "age of the tractor" and "number of components changed" are circled together as the (X, Y) pair for the tractor maintenance-cost example.

**Two kinds of explanatory variables (slide 3, bottom box).** The slide draws a distinction that matters a lot in real experimental design:

1. **Variables we can control** — e.g., in a lab setting, you can choose exactly how much light intensity to put in the incubator, or exactly how many cases to run through the vending machine. These let you run a controlled experiment.
2. **Variables over which we have little or no control** — e.g., you cannot control a tractor's age or how many components end up needing replacement; you can only observe them as they occur. Most real-world regression problems (like predicting house prices from area, which nobody "sets" experimentally) fall into this second category — we work with *observational* data, not experimentally controlled data.

**Where the word "regression" itself comes from.** The slides don't explain this, but it's a genuinely interesting and non-obvious piece of context: the term "regression" was coined by the Victorian polymath **Francis Galton** in his 1886 paper *"Regression towards Mediocrity in Hereditary Stature."* Galton studied the heights of 1,078 parent–child pairs and found that tall parents tended to have children who were tall, but *closer to the average height* than the parents were — and short parents tended to have children closer to the average too. He called this tendency of offspring to "regress" back toward the population mean **"regression toward the mean."** The statistical *technique* of fitting a line through data (what this lecture teaches) inherited its name from this unrelated-sounding biological observation, purely because Galton was the one who developed the line-fitting math to study it. So "regression" in "linear regression" has nothing to do with something getting worse or going backward in the everyday sense of the word — it's a historical accident of naming. (Source: [Regression toward the mean — Wikipedia](https://en.wikipedia.org/wiki/Regression_toward_the_mean); [Francis Galton and regression to the mean — Significance/Wiley](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2011.00509.x).)

---

## 2) Simple English Explanation

Regression is just a fancy word for: **"if I know X, can I predict Y?"**

Think about it like this — you already do this kind of thinking every day without calling it "regression." If someone tells you a mango is very heavy, you'd guess it's probably a big mango. Weight (Y) is being predicted from something you can see or measure (X, the size). That's exactly what regression formalizes with math.

**Two kinds of relationships:**
- **Cause-and-effect**: X actually *makes* Y happen. Like, more fertilizer *causes* more crop growth.
- **Functional relationship**: X and Y just *move together in a predictable pattern*, whether or not X causes Y. Like, a tractor's age and its maintenance cost — the age doesn't "cause" the machine to break exactly, but older tractors reliably need more repairs, so if you know the age you can make a good guess about the maintenance cost.

**Y and X have other names too**, and it helps to know all of them because different books/courses use different words for the exact same thing:
- Y = "dependent variable" = "response variable" = "predicted variable" (the thing you want to find out)
- X = "independent variable" = "explanatory variable" = "predictor variable" (the thing you already know and use to guess Y)

**The examples on the slide** all follow the same pattern — a list of things you'd want to predict (Y) paired with a list of things you'd measure to predict them (X): e.g., you'd predict "repair time for a computer" (Y) from "how many components need to be changed" (X). More components to change → probably more repair time.

**Controllable vs. uncontrollable X**: sometimes you get to *choose* the value of X yourself — like in a science experiment, you decide exactly how much light to shine on seeds. Other times, X is just something that already exists and you can only observe it — like a house's area, or a tractor's age; you can't "set" a house to be 3000 sqft, you just look at houses that already are.

**Where does the name "regression" come from, and why is it a weird name?** It sounds like it should mean "going backward" or "getting worse," but that's not really what it means in ML. The name comes from a 19th-century scientist named Francis Galton, who noticed that really tall parents tend to have kids who are tall, but usually a bit shorter than the parents — closer to average height. He called this "regressing toward the average." He was the one who invented the maths for drawing that best-fit line through data to study this, so the whole technique got stuck with his word "regression," even though today we use it for totally unrelated things like predicting house prices.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Regression basically ek simple sawaal solve karta hai: **agar mujhe X pata hai, toh main Y ka andaza kaise lagaun?**

Jaise, agar koi bole "yeh ghar bahut bada hai" toh aap khud hi guess kar lete ho ki uski price bhi zyada hogi. Yahi cheez regression maths ki language mein karta hai — X (area) se Y (price) predict karna.

**Do tarah ke relationships hote hain:**
- **Cause-and-effect**: X seedha Y ko cause karta hai. Jaise zyada fertilizer dalne se crop zyada grow karta hai — fertilizer directly cause hai.
- **Functional relationship**: X aur Y sirf ek predictable pattern mein saath-saath move karte hain, cause ho ya na ho. Jaise tractor ki age aur uska maintenance cost — age directly "cause" nahi karti breakdown ko, lekin purane tractors mein generally zyada maintenance lagta hai, toh age dekh kar aap cost ka andaza laga sakte ho.

**Y aur X ke alag-alag naam bhi hote hain** — alag books/courses mein alag word use hote hain same cheez ke liye:
- Y = "dependent variable" = "response variable" = "predicted variable" (jo cheez pata karni hai)
- X = "independent variable" = "explanatory variable" = "predictor variable" (jo cheez pehle se pata hai, jisse Y guess karte hain)

**Slide ke examples** sab isi pattern mein hain — ek list hai jo predict karni hai (Y), aur ek list hai jisse predict karte hain (X). Jaise "computer repair karne mein kitna time lagega" (Y) ko predict karte hain "kitne components badalne padenge" (X) se — jitne zyada components badalne padenge, utna zyada time lagega, roughly.

**Controllable vs uncontrollable X**: kabhi-kabhi aap khud X ki value set kar sakte ho — jaise ek experiment mein aap decide karte ho ki seeds ko kitni light deni hai. Lekin kabhi-kabhi X pehle se fixed hota hai aur aap sirf observe kar sakte ho — jaise ghar ka area ya tractor ki age, aap inko "set" nahi kar sakte, jo already hai wahi dekhna padta hai.

**"Regression" naam kahan se aaya, aur yeh itna ajeeb naam kyu hai?** Sunne mein lagta hai jaise "peeche jaana" ya "kharab hona" — lekin ML mein iska yeh matlab bilkul nahi hai. Yeh naam ek 19th-century scientist Francis Galton se aaya, jisne notice kiya tha ki bahut lambe parents ke bachche bhi lambe hote hain, lekin usually parents se thoda kam lambe — average ke thoda zyada kareeb. Usne isko "regressing toward the average" bola. Wahi banda tha jisne data ke through best-fit line kheenchne ka maths invent kiya tha isi cheez ko study karne ke liye, toh poori technique ka naam uske word "regression" pe atak gaya — chahe aaj hum isse bilkul alag cheezon ke liye use karte hain, jaise ghar ki price predict karna.
