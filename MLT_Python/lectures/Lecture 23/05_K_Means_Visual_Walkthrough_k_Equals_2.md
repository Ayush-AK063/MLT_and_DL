# Topic 5: Visual Walkthrough of k-Means with k = 2

Source: Lecture 23, slides 9–16 (an animation sequence of a 16-point scatter: "1. Start with K centroids by putting them at random place, here k = 2"; "2. Compute distance of every point from centroid and cluster them accordingly"; "3. Adjust centroids so that they become center of gravity for given cluster"; "4. Again re-cluster every point based on their distance with centroid"; "5. Again adjust centroids"; "6. Recompute clusters and repeat this till data points stop changing clusters"; final picture with C1, C2 and the note "K? optimal clusters"). Enriched with general knowledge (perpendicular-bisector / Voronoi boundary).

---

## 1) Technical Explanation

The sequence animates Lloyd's algorithm ([[04_K_Means_Algorithm_Steps]]) on **16 unlabelled points in 2-D**. The points form three visible groups:

- a **left group** of 5 points;
- a **diagonal "tail"** of 3 points just below and to the right of the left group;
- an **upper-right group** of 8 points.

| Slide | Caption on slide | What the figure shows |
|---|---|---|
| 9 | 1. Start with K centroids by putting them at random place, here k = 2 | Two stars, **red** and **green**, placed close together near the bottom, below the data |
| 10 | (same caption) + handwritten "Distance" | Red arcs from every point to both stars show that each point's distance to each centroid is measured. A **dashed vertical line** midway between the two stars is the decision boundary. One point near the line is circled. |
| 11 | 2. Compute distance of every point from centroid and cluster them accordingly | Points left of the dashed line turn **red**: only **4** points. All **12** points to the right, including the circled one and the whole tail, turn **green**, because the green star is slightly to the right. |
| 12 | 3. Adjust centroids so that they become center of gravity for given cluster | Each star jumps to the **mean** ("centre of gravity") of its colour. Red moves into the middle of the 4 left points. Green moves up into the 12-point mass, between the upper group and the tail. |
| 13 | 4. Again re-cluster every point based on their distance with centroid | The new boundary is a **tilted** dashed line, perpendicular to the segment joining the two stars. The circled point and two of the three tail points now fall on the red side and turn **red**. One tail point stays green. |
| 14 | 5. Again adjust centroids | Red moves right and down toward the tail. Green moves up into the upper group. The boundary rotates again. |
| 15 | 6. Recompute clusters and repeat this till data points stop changing clusters | The last tail point turns red. Now **8 red, 8 green**. |
| 16 | (no caption) + handwritten "K? optimal clusters" | Final result: **C1** (red: left group + tail) and **C2** (green: upper-right group), each circled. The note asks: was k = 2 the right choice? |

### Key observations

1. **The decision boundary is the perpendicular bisector.** With Euclidean distance and two centroids μ₁ and μ₂, the points that are equally far from both satisfy ‖x − μ₁‖ = ‖x − μ₂‖. That set is the line perpendicular to the segment μ₁μ₂ through its midpoint. This is why the dashed line on slides 13–15 always crosses the dashed segment joining the stars at a right angle. With k centroids the space is cut into k convex **Voronoi cells**, which is why k-Means clusters are always convex regions.
2. **A bad start gets fixed, slowly.** The initial stars sit almost on top of each other, outside the data. So the first split (4 vs 12) is badly unbalanced. Each assign → update round shifts the boundary, and points migrate one or two at a time until nothing changes.
3. **Initialisation differs from Algorithm 16.1.** These slides place the starting centroids at **random locations in space**. Slide 6, step 1 picks **k data objects** as the starting centroids. Both are valid initialisation schemes. Picking data objects (Forgy) guarantees that no cluster starts empty.
4. **Stopping rule.** "Till data points stop changing clusters" is convergence criterion 1 in [[04_K_Means_Algorithm_Steps]].
5. **The "tail" ends up with the left group.** That happens because, with k = 2, it is closer to the left centroid. With k = 3 it might form its own cluster. Slide 16's note "**K? optimal clusters**" leads straight into choosing k ([[06_Choosing_k_SSE_and_the_Elbow_Method]]).

---

## 2) Simple English Explanation

These eight slides are like a flip-book showing k-Means at work with **two groups (k = 2)**. There are 16 dots: a small bunch on the left, a short diagonal tail of 3 dots below it, and a bigger bunch top-right.

**Slide 9: drop two markers anywhere.** A red star and a green star are placed at random, here both near the bottom and close together. They are bad starting spots, but that's fine. The algorithm will fix it.

**Slide 10: measure distances.** The teacher drew curved arrows from every dot to the stars and wrote "Distance". Every dot checks how far it is from the red star and from the green star. The dashed vertical line halfway between the stars is the "border": dots on its left are nearer red, dots on its right are nearer green.

**Slide 11: colour the dots.** Only the 4 dots left of the border become red. All the other 12 become green, even the tail, just because the green star happens to be a little to the right.

**Slide 12: move each star to the middle of its colour.** The red star jumps to the centre of the 4 red dots. The green star jumps to the centre of the 12 green dots. This is like finding the balance point, or "centre of gravity".

**Slide 13: re-colour.** The stars are in new places, so the border moves and tilts. It always sits exactly halfway between the two stars, at a right angle to the line joining them. Now some dots that were green are closer to red, so they switch: two of the tail dots and the circled dot near the old border.

**Slides 14–15: repeat.** Move the stars again, re-colour again. The last tail dot switches to red. Now it's 8 red and 8 green, and another round changes nothing, so we **stop**.

**Slide 16: the final answer.** Group C1 is the left bunch plus the tail. Group C2 is the top-right bunch. The teacher asks "**K? optimal clusters**": we *told* it to make 2 groups, but was 2 the best number? Maybe the tail deserves its own group. That question is answered next with the elbow method.

**Two things to notice:**
- The algorithm started from a silly position and still found sensible groups by repeating "colour, then move" a few times.
- Here the stars started at random spots in empty space. Slide 6 instead starts the stars on actual data points. Both ways are allowed.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye aath slides ek flip-book jaise hain jo dikhati hain ki k-Means **do groups (k = 2)** ke saath kaise kaam karta hai. Graph pe 16 dots hain: left mein ek chhota jhund (5 dots), uske neeche ek tirchhi poonchh (3 dots), aur upar-right mein bada jhund (8 dots).

**Slide 9: do markers kahin bhi rakh do.** Ek laal star aur ek hara star random jagah rakhe gaye, yahan dono neeche aur paas-paas. Ye kharab starting jagah hai, par koi baat nahi, algorithm khud sudhaar lega.

**Slide 10: distance naapo.** Teacher ne har dot se dono stars tak ghumaavdaar teer banaye aur likha "Distance". Har dot dekhta hai ki laal star se kitna door hai aur hare se kitna. Dono stars ke theek beech mein ek dashed seedhi line hai, jo "border" hai. Left wale dots laal ke paas hain, right wale hare ke paas.

**Slide 11: dots ko rang do.** Border ke left mein sirf 4 dots hain, woh laal ho gaye. Baaki 12 dots, poonchh samet, hare ho gaye, sirf isliye ki hara star thoda right mein tha. Group bahut unbalanced hain (4 vs 12).

**Slide 12: har star ko apne rang ke beech mein le jao.** Laal star 4 laal dots ke centre pe gaya. Hara star 12 hare dots ke centre pe gaya. Isko "**centre of gravity**" kehte hain, yaani balance point, jo asal mein average hai.

**Slide 13: dobara rang do.** Stars nayi jagah pe hain, to border bhi khisak ke tirchha ho gaya. Border hamesha dono stars ke theek beech mein hota hai aur unhe jodne wali line pe 90° pe khada hota hai (**perpendicular bisector**). Ab kuch hare dots laal ke zyada paas ho gaye: poonchh ke 2 dots aur woh circled dot jo purane border ke paas tha. Woh laal ho gaye.

**Slides 14–15: repeat karo.** Stars phir hile aur dots phir rang badle. Poonchh ka aakhri dot bhi laal ho gaya. Ab 8 laal aur 8 hare hain. Agle round mein kuch nahi badla, to **ruk jao** (yahi convergence hai).

**Slide 16: final jawaab.** **C1** = left wala jhund + poonchh, aur **C2** = upar-right wala jhund. Teacher ne likha "**K? optimal clusters**": humne *khud* kaha tha 2 groups banao, par kya 2 sahi number tha? Ho sakta hai poonchh ka apna alag group banna chahiye tha. Iska jawaab agla topic (elbow method) deta hai.

**Do baatein dhyan rakho:**
- Algorithm ek bekaar position se shuru hua, phir bhi "rang do → star hilao" baar-baar karke sahi groups pe pahunch gaya.
- Yahan stars khaali jagah pe random rakhe gaye, jabki slide 6 ka algorithm data ke hi k points ko starting centre banata hai. Dono tareeke chalte hain. Data point se shuru karne ka fayda ye hai ki koi cluster shuru mein khaali nahi rehta.
- Do centres ke beech ka border hamesha seedhi line hota hai, aur k centres ke saath space k "cells" (Voronoi cells) mein bant jata hai. Isliye k-Means ke clusters hamesha convex (bina andar mude) shape ke hote hain.
