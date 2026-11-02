# Topic 4: Representation Learning and Factors of Variation

Source: Lecture 26, slides 10–11 ("Representation Learning": better performance than hand design, rapid adaptation, need a good set of features, manual design nearly impossible; "Design of Features": separate out variation factors, separate sources of influence, unobserved objects/forces affecting observable quantities, speech: age, sex, accent; image: position, color, brightness). Enriched with web research (Goodfellow, Bengio & Courville, *Deep Learning*, 2016, ch. 1 and ch. 14–15; Bengio, Courville & Vincent, "Representation Learning: A Review and New Perspectives", IEEE TPAMI 2013).

---

## 1) Technical Explanation

### Slide 10: what representation learning is and why it helps

**Representation learning** means using machine learning to discover not only the mapping from representation to output, but also **the representation itself**. The slide's four points:

1. **"Learned representations often result in better performance compared to hand design."** Example: on the ImageNet image-classification benchmark, the best hand-designed-feature systems had about 26% top-5 error in 2011. AlexNet, a deep network that learned its features, got about 15–16% in 2012. Since then learned features have dominated vision, speech and language.
2. **"Allows the system to rapidly adapt to new tasks."** A learned representation can be reused. A network trained on millions of general photos has learned edges, textures and object parts. To recognise, say, X-ray abnormalities, we keep most of it and retrain only the last part with a small dataset. This is called **transfer learning** or fine-tuning. The book notes that a representation learner can find a good set of features for a simple task in minutes, or for a complex task in hours to months, while hand-designing features for a complex task can take a whole research community decades.
3. **"Need to discover a good set of features."** The goal is a feature set in which the task becomes easy, for example linearly separable, as in Topic 2.
4. **"Manual design of features is nearly impossible"** for complex raw data (millions of pixels, thousands of audio samples per second), as the car example in Topic 3 showed.

**The standard example: the autoencoder.** The book names it as the quintessential representation-learning algorithm. It has two parts:

- an **encoder** f that converts the input x into a representation h = f(x), usually smaller than x;
- a **decoder** g that converts h back, x̂ = g(h).

It is trained so that x̂ ≈ x. To reconstruct well through a narrow bottleneck, h is forced to keep the most important information about x. Nobody tells it what the features should be. A one-hidden-layer ("shallow") autoencoder is the book's example of representation learning that is *not* deep ([[07_Machine_Learning_and_AI_Venn_Diagram_and_the_Cyc_Project]]). With linear encoder and decoder and squared error, it learns the same subspace as PCA ([[04_PCA_Introduction_and_Intuition]] from Lecture 11–12), so PCA can be seen as the simplest representation learner.

### Slide 11: design of features and factors of variation

- **"Goal is to separate out variation factors."**
- **"These factors are separate sources of influence."**
- **"It may exist as an unobserved object or unobserved forces that affect an observable quantity."**
- **Speech:** factors are age, sex, accent, etc.
- **Image:** position, colour, brightness, etc.

**Meaning.** What we observe (pixel values, a sound wave) is produced by several underlying causes acting together. These causes are the **factors of variation**. Usually we cannot measure them directly; we only see their combined effect.

| Observed data | Factors of variation (hidden causes) | Factor we usually care about |
|---|---|---|
| Recording of a spoken word | speaker's age, sex, accent, speed, microphone, background noise | **which word** was said |
| Photo of a car | position in frame, angle, colour, lighting/brightness, distance, background | **is it a car?** |
| Face photo | identity, expression, pose, lighting, glasses | **whose face** |

**Why this makes AI hard.** Many factors influence *every single* data value. The book's example: the pixels of a **red car at night** can look almost black. The silhouette of a car depends on the viewing angle. A single pixel's value is a mix of object colour, lighting, shadow and position, so no single pixel tells you "car".

**What a good representation does: disentangling.** A good representation pulls these factors apart, so that one feature (or group) changes when, for example, brightness changes, and another changes when the identity changes. The task then becomes easy: use the "identity" features and **ignore** (become invariant to) the nuisance ones such as lighting and position. Bengio, Courville & Vincent (2013) call this **disentangling the factors of variation** and treat it as a central goal of representation learning.

**Link to Topic 2.** In the ring dataset, the observed (x, y) mixes two factors: distance r (which decides the class) and angle θ (irrelevant). Switching to polar coordinates separated them, so one coordinate carried the class and the other could be ignored. That is disentangling in its simplest form.

**The catch** (and the bridge to deep learning). Disentangling high-level factors (identity, accent) from raw data can be nearly as hard as solving the task. The book argues that deep learning addresses this by building complex representations out of simpler ones, layer by layer ([[05_Deep_Learning_Building_Complex_Concepts_from_Simple_Ones]]).

---

## 2) Simple English Explanation

**Slide 10: what representation learning means.**

Normally a person decides *what to measure* about the data, and the computer only learns *how to use* those measurements. In **representation learning** the computer learns both: it decides for itself what to measure (the features) and how to use them.

Why is this good? The slide gives four reasons:

1. **It usually works better than hand-made features.** In the big ImageNet photo competition, the best hand-made systems got about 26% wrong (top-5) in 2011. A deep network that learned its own features got about 15–16% wrong in 2012. Since then learned features have won almost everywhere.
2. **It adapts quickly to new jobs.** A network that learned to see edges, textures and shapes from millions of everyday photos can be re-used for a new job, like spotting problems in X-rays, by retraining only its last part on a small set. This is called *transfer learning*.
3. **We need a good set of features**, ones that make the task easy (like distance-from-centre in Topic 2).
4. **Making them by hand is nearly impossible** for photos and sound (remember the wheel in Topic 3).

**A classic example, the autoencoder:** imagine squeezing a photo into a short summary (the "encoder") and then trying to rebuild the photo from only that summary (the "decoder"). If the rebuilt photo looks like the original, the short summary must have kept the important information. Nobody told the computer what to keep; it found out. The very simplest version of this idea gives the same result as PCA from Lecture 11–12.

**Slide 11: factors of variation.**

What we record (a voice clip, a photo) is the result of many hidden causes mixed together. These causes are called **factors of variation**.

- **A voice recording** is shaped by the speaker's age, whether they are male or female, their accent, their speed, the microphone and the background noise. But usually we only care about one thing: *which word was said*.
- **A photo of a car** is shaped by where the car is in the picture, its colour, the brightness of the light, the angle and the background. We only care about: *is it a car?*

Why is this hard? Because every pixel is affected by all these causes at once. For example, a **red car at night** can look almost black in the photo. So no single pixel tells you "car".

**What a good representation does:** it **separates** the causes, like separating the ingredients after they have been mixed. One feature might track the lighting, another the angle, another the car's shape. Then the task becomes easy: use the shape and ignore the lighting and the position. Experts call this *disentangling*.

We already saw a tiny version in Topic 2: (x, y) mixed "distance" (which decided the colour) with "angle" (which didn't matter). Changing to (r, θ) separated them, and the problem became easy.

**The catch:** separating such hidden causes in real photos is very hard by hand. Deep learning tackles it by building up complex features out of simple ones, step by step (next topic).

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 10: Representation learning kya hai.**

Normally insaan decide karta hai ki data ka kya measure karna hai (features), aur computer sirf un features ko use karna seekhta hai. **Representation learning** me computer dono seekhta hai: kaun se features banane hain, aur unse answer kaise nikalna hai.

Slide ke chaar points:

1. **"Learned representation often result in better performance compared to hand design."** ImageNet competition me 2011 tak hand-made features wale best system ka top-5 error lagbhag 26% tha. 2012 me AlexNet (deep network, khud features seekhe) ka error lagbhag 15–16% aaya. Uske baad se vision, speech, language sab me learned features hi jeet rahe hain.
2. **"Allows the system to rapidly adapt to new task."** Jis network ne lakhon normal photos se edges, textures, shapes seekh liye, use naye kaam (jaise X-ray me problem dhoondhna) ke liye reuse kar sakte hain, sirf last part ko chhote data pe retrain karke. Isko **transfer learning** kehte hain. Book kehti hai: complex task ke liye features haath se design karne me poori research community ko dashak lag jaate hain, learning se ghanton se mahino me ho jaata hai.
3. **"Need to discover a good set of features"**: aise features jinse kaam aasaan ho jaaye (jaise Topic 2 me centre se doori).
4. **"Manual design of features is nearly impossible"**: photo aur audio jaise raw data ke liye haath se features banana lagbhag impossible (Topic 3 ka wheel example yaad karo).

**Autoencoder (classic example):** Photo ko ek chhote summary h me compress karo (**encoder**), fir sirf us summary se photo wapas banao (**decoder**). Train aise karte hain ki wapas bani photo original jaisi ho (x̂ ≈ x). Agar ho gayi, matlab summary ne important information rakh li, bina kisi ke bataye. Ek hidden layer wala "shallow autoencoder" representation learning hai par deep learning nahi. Linear version ka answer PCA (Lecture 11–12) jaisa hi aata hai.

**Slide 11: Design of features, factors of variation.**

Jo hum observe karte hain (pixels, sound wave), wo kai **chhupe hue causes** ke mix se banta hai. Inhe **factors of variation** kehte hain. Slide ke words: ye "separate sources of influence" hain, aur "unobserved object ya unobserved forces" ho sakte hain jo observable quantity ko affect karte hain.

- **Speech:** recording pe asar hai bolne wale ki age, sex (male/female), accent, speed, mic, background noise ka. Par humein aksar sirf ye chahiye: **kaun sa word bola gaya.**
- **Image:** car ki photo pe asar hai position, colour, brightness, angle, background ka. Humein chahiye: **car hai ya nahi.**

**Mushkil kyun hai?** Har ek pixel pe saare factors ek saath asar daalte hain. Book ka example: **raat me laal car** photo me lagbhag kaali dikh sakti hai. To kisi ek pixel se "car" pata nahi chalta.

**Achha representation kya karta hai:** in factors ko **alag-alag** kar deta hai (isko **disentangling** kehte hain). Ek feature lighting track kare, ek angle, ek car ka shape. Fir kaam aasaan: shape use karo, lighting aur position ignore karo.

Topic 2 me iska chhota version dekha: (x, y) me "doori" (jo class decide karti thi) aur "angle" (bekaar) mixed the. (r, θ) me badalne se dono alag ho gaye aur problem aasaan ho gayi.

**Catch:** Real photos me ye high-level factors haath se alag karna lagbhag utna hi mushkil hai jitna khud task. Deep learning iska solution deta hai: complex features ko simple features se, layer by layer, banana (agla topic).
