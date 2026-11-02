# Topic 8: ML Paradigms — Unsupervised Learning (Clustering & Association Rules)

Source: Lecture 3, slides 61–66 (What is Unsupervised Learning, Clustering, Association Rules Mining, More Examples). Enriched with web research (Toloka, market basket analysis sources).

---

## 1) Technical Explanation

**What is Unsupervised Learning? (slide 61)**: *"In the unsupervised learning, we do not need to know the labels or ground truth values."* The lecture visually reinforces this by showing the same 4 vehicle images from the supervised-learning example, but with their CAR/BIKE labels **crossed out** — the same raw data, but stripped of the "experience"/ground-truth that supervised learning depends on. This is the defining contrast with Topic 7's supervised paradigm ([[07_ML_Paradigms_Supervised_Learning]]) — unsupervised learning must find structure using **only the input data (x)**, with no target/label (y) available at all.

**Clustering (slide 62)**: *"The task is to identify the patterns like group the similar objects together."* Given the same unlabeled vehicle images, an unsupervised algorithm groups the two car images together and the two bike images together — **purely based on similarity in the feature space** (e.g., shape, size, visual characteristics) — without ever being told the category names "CAR" or "BIKE." The algorithm doesn't know what to *call* each group, only that objects within a group are more similar to each other than to objects in other groups. This is the core idea behind clustering algorithms (e.g., K-means, which is later in the course syllabus).

**Association Rules Mining (slide 63)**: A second unsupervised technique — instead of grouping similar items, this discovers **co-occurrence relationships** between different items. The lecture's example: `car → helmet/cover accessory` and `motorbike → helmet`, implying rules like "customers who buy vehicle type X also tend to buy accessory Y." Enriched from research: this is the technique behind classic **Market Basket Analysis** — e.g., the canonical example rule `{bread, butter} → {eggs}` mined from supermarket transaction data, evaluated using metrics like **support** (how frequently the itemset appears) and **confidence** (how often the rule holds true when the antecedent is present). No labels are needed — the algorithm mines raw transaction data for frequently co-occurring patterns.

**More Examples of Unsupervised Learning (slides 64–66)**:
- **Customer segmentation clustering**: a crowd of differently-colored stick-figures (representing customers/data points, e.g., by purchasing behavior or demographics) is shown being automatically grouped into clusters by color/similarity, with **no predefined labels** — a classic real-world use case for market segmentation.
- **Recommendation via association ("Customers who viewed this item also viewed…")**: shown with a computer monitor followed by suggested security-camera products — this is the same association-rule-mining principle applied to e-commerce recommendation engines: "people who interact with item A also frequently interact with item B," discovered purely from behavioral co-occurrence data, without needing explicit labels about *why* the items are related.

**Summary of the Supervised vs. Unsupervised distinction (drawing together Topics 7 & 8)**:
| | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Data needed | Labelled (samples + ground-truth labels) | Unlabelled (samples only) |
| Goal | Learn a function to predict a known target | Discover hidden structure/patterns |
| Example tasks | Classification, Regression | Clustering, Association Rule Mining |
| Real-world example from lecture | CAR/BIKE classifier, house-price regression | Grouping similar vehicles, "customers who bought X also bought Y" |

---

## 2) Simple English Explanation

**Unsupervised Learning is the opposite setup from supervised learning**: you have data, but **no correct answers attached to it at all**. The lecture shows this visually — the same car/bike pictures as before, but this time with their "CAR"/"BIKE" labels crossed out. The algorithm only gets the raw pictures, with no idea what any of them are officially called.

**Clustering — finding groups without being told what the groups are**: If you give an unsupervised algorithm those unlabeled vehicle pictures, it can still notice that two of them look similar to each other (the cars) and the other two look similar to each other (the bikes) — and it will automatically group them accordingly. It won't know to *call* one group "cars" — it just knows "these two belong together, and those two belong together" based on how similar they look.

**Association Rule Mining — finding "things that go together"**: This is a different unsupervised trick: instead of grouping similar items, it looks for patterns like "when people buy X, they also tend to buy Y." The lecture's example: people who buy a car often also get a car cover/accessory, and people who buy a motorbike often also buy a helmet. No one had to label anything "these go together" — the algorithm figured it out just by looking at what tends to happen together in the data.

**More real-life examples**:
- **Customer grouping**: a company might have data on thousands of customers with no predefined "customer types" — an unsupervised algorithm can automatically sort them into natural groups (like similar-spending customers ending up together) purely by finding patterns, without anyone telling it what the groups should be.
- **"Customers who viewed this also viewed…"**: this exact feature on shopping websites (like Amazon) is powered by the same idea as association rule mining — the system noticed that people who look at a computer monitor often also look at security cameras, purely from behavior data, and uses that pattern to make suggestions.

**In short**: Supervised learning needs an answer key; unsupervised learning has to find useful structure in the data all on its own, with no answer key at all.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Unsupervised Learning kya hai?**
Ye supervised learning ka **ulta setup** hai — humare paas data to hai, lekin **koi sahi jawaab (labels) bilkul nahi hai**. Lecture isko visually dikhata hai — wahi car/bike ki photos jo pehle the, lekin ab unke "CAR"/"BIKE" labels **kaat diye gaye hai (crossed out)**. Algorithm ko sirf raw photos milti hai, use pata nahi ki inko officially kya kehte hai.

**Clustering — bina bataye similar cheezon ko group karna**
Agar aap unsupervised algorithm ko wo unlabeled vehicle photos do, to bhi wo notice kar sakta hai ki 2 photos aapas mein similar dikhti hai (cars) aur baaki 2 aapas mein similar hai (bikes) — aur khud unko groups mein baant dega. Usko ye nahi pata hoga ki ek group ko "car" kehte hai — bas usse itna pata hai "ye do saath mein hai, wo do saath mein hai" — sirf **similarity ke basis pe**.

**Association Rule Mining — "jo cheezein saath mein aati hai" dhoondhna**
Ye ek aur unsupervised trick hai: similar cheezein group karne ke bajaye, ye pattern dhoondhta hai jaise "jab log X kharidte hai, to aksar Y bhi kharidte hai." Lecture ka example: jo log **car** kharidte hai wo aksar **car cover/accessory** bhi lete hai, aur jo log **motorbike** kharidte hai wo aksar **helmet** bhi lete hai. Kisi ne "ye saath mein jaate hai" nahi likha — algorithm ne khud data mein pattern dekh kar ye pata lagaya.

**Enriched example (asli duniya mein — Market Basket Analysis)**:
Supermarket mein ek famous example hai: `{bread, butter} → {eggs}` — matlab jo log bread aur butter saath mein khareedte hai, wo aksar eggs bhi khareedte hai. Isko measure karne ke liye 2 metrics use hote hai:
- **Support**: ye combination kitni baar aata hai transactions mein
- **Confidence**: jab pehli cheez khareedi jaati hai, to kitni baar doosri bhi khareedi jaati hai

**Aur bhi real-life examples:**
- **Customer Grouping**: Ek company ke paas hazaaron customers ka data ho sakta hai, bina kisi pehle se defined "customer type" ke. Unsupervised algorithm khud unko natural groups mein baant sakta hai (jaise similar-spending customers ek saath aa jaayein) — bina kisi ke bataye ki groups kya hone chahiye.
- **"Customers who viewed this also viewed..."**: Amazon jaisi shopping website ka ye feature bhi isi association rule mining wale idea pe based hai — system ne notice kiya ki jo log computer monitor dekhte hai, wo aksar security cameras bhi dekhte hai — sirf behavior data se, bina kisi label ke.

**Short mein yaad rakho:**
- **Supervised Learning** = Answer-key chahiye (labels ke saath)
- **Unsupervised Learning** = Bina answer-key ke, data mein khud se useful patterns dhoondhna (Clustering, Association Rules)
