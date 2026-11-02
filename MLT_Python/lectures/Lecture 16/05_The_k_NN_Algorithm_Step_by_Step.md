# Topic 5: The k-NN Algorithm, Step by Step

Source: Lecture 16, slide 11 ("Working of K-Nearest Neighbor Algorithm" — the 5 steps) and slide 12 (section divider "Numerical Example"). Enriched with web research (ties, distance-weighted voting, complexity).

---

## 1) Technical Explanation

**The five steps (slide 11).**

1. **Determine parameter K** = number of nearest neighbors.
2. **Calculate the distance** between the query instance and **all** the training samples ([[04_Distance_Metrics]]).
3. **Sort the distances** and determine the nearest neighbors based on the **K-th minimum distance**.
4. **Gather the category Y** of the nearest neighbors.
5. Use a **simple majority** of the categories of the nearest neighbors as the label of the query instance (**classification**), or the **average** of the values of the k nearest neighbors (**regression**).

**Pseudocode.**

```
Input : training set {(x_1, y_1) ... (x_N, y_N)}, query q, integer k
for i in 1..N:
    d[i] = distance(q, x_i)
order = indices sorted by d ascending
neighbors = first k indices of order
if classification: return most frequent y among neighbors   (majority vote)
if regression    : return mean of y among neighbors
```

There is **no training step** — all the work is in steps 2–5 per query ([[02_k_NN_as_Instance_Based_Lazy_Learning]]).

**⚠️ A contradiction inside the lecture (flagged).** The note at the bottom of slide 11 reads: *"(For classification, K must be set as **even** number — so as to avoid tie during simple majority)."* But slide 3 ([[01_Nearest_Neighbor_Idea_and_Basic_Rule]]) says the opposite — k is usually chosen **odd** to avoid ties — and the 2-nearest-neighbor panel on slide 4 is itself a tie. The mathematically correct statement is **odd**: with two classes, an odd k can never split evenly, whereas an even k can (e.g. 2–2). The word "even" on slide 11 is almost certainly a slip; this note follows slide 3 and standard practice. (Caveat: with **three or more classes** even an odd k can produce a tie, e.g. 1–1–1 at k = 3, so a tie-break rule is still needed.)

**Tie-breaking options (research).** Common choices: pick the class of the single nearest tied neighbor; reduce k by one and re-vote; choose the class with the larger overall training frequency; or use **distance-weighted voting**, where each neighbor's vote is weighted by 1/distance (or 1/distance²) so closer neighbors count more — this almost always breaks ties automatically.

**Cost.** Step 2 costs O(N·m) for N training points and m features per query; step 3 costs O(N log N) if fully sorted (a partial selection of the k smallest is O(N)). Data structures like KD-trees and ball trees can speed up the search for low-dimensional data ([[08_Practical_Considerations_Scaling_Dimensionality_and_Pros_Cons]]).

**Two worked examples follow:** [[06_Worked_Example_Predicting_Movie_Genre]] (k = 1 and 3, full Euclidean distance) and [[07_Worked_Example_Paper_Tissue_Classification]] (k = 3, squared distance, a ranking table).

---

## 2) Simple English Explanation

Here is the whole recipe for k-NN in plain steps — like finding which friends to ask for restaurant advice:

1. **Decide how many friends to ask** (that's k).
2. **Measure how close** each friend's taste is to yours — you do this for *everyone* in your contact list.
3. **Line them up** from closest to farthest, and take the first k.
4. **Look at what each of them said** (their category).
5. **Go with the most popular answer.** If you're predicting a number instead of a category, take the **average** of their numbers.

That's all. There's no "learning" phase — you only do these steps when a new question arrives.

**A mistake in the slide:** at the bottom of this slide it says k must be *even* to avoid ties. That's backwards! With an even number, a tie like 2 vs 2 is possible. With an odd number (3, 5, 7…) and two choices, one choice must win. The slide on the first page of the lecture also says "odd." So trust "odd."

If a tie still happens (for example with three categories, each getting one vote), common fixes are: trust the closest neighbor, or let closer neighbors have a louder vote.

---

## 3) Hinglish Explanation (Beginner-Friendly)

k-NN ka poora recipe simple steps mein — jaise restaurant ke liye doston se advice lena:

1. **Kitne doston se poochhna hai** wo decide karo (ye hai k).
2. Har dost ka taste tumse **kitna milta hai** (distance) naapo — contact list ke **sabhi** logon ke liye.
3. Sabko **paas se door ki line** mein lagao aur pehle k utha lo.
4. Dekho un k logon ne **kya answer (category) diya**.
5. **Jo answer sabse zyada logon ne diya wahi final.** Agar category nahi balki number predict karna hai (regression), to unke numbers ka **average** le lo.

Bas itna hi! Koi alag "training" nahi hoti — ye saare steps tab chalte hain jab naya sawaal (query) aata hai.

⚠️ **Slide ki galti:** slide ke neeche likha hai "K must be set as **even** number to avoid tie." Ye ulta hai! Even k mein to 2 vs 2 jaisa tie ho sakta hai. **Odd** k (3, 5, 7...) aur 2 classes mein ek class ka majority hona pakka hai. Lecture ki slide 3 mein bhi "odd" hi likha hai aur slide 4 ka 2-NN wala figure bhi tie dikhata hai. Isliye **odd** wala rule sahi maano.

(Agar 3 ya zyada classes hon to odd k mein bhi tie ho sakta hai, jaise k=3 aur teeno ko 1-1-1 vote. Tab tie-break karte hain: sabse paas wale ka answer lo, ya paas wale neighbors ko zyada weight do — **distance-weighted voting**.)

Ab aage do numerical examples hain jahan ye 5 steps asli numbers par chalte dikhenge.
