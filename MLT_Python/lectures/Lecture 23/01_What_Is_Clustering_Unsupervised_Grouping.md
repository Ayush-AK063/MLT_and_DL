# Topic 1: What Is Clustering? Grouping Unlabelled Data

Source: Lecture 23, slides 1–2 (title "Machine Learning — K Means Clustering"; "Clustering techniques") and slide 7 (hand-drawn scatter with clusters C1, C2 and the note "Structure / Pattern"). Enriched with general knowledge on similarity measures.

---

## 1) Technical Explanation

**Slide 2: definition.** The slide makes five points:

- Clustering "has been studied extensively for more than 40 years and across many disciplines due to its broad applications."
- "Clustering is an **unsupervised machine learning technique** used to group similar data points together **without using labelled data**. It helps discover hidden patterns or natural groupings in datasets by placing similar data points into the same cluster."
- Goal: "Discover the **natural grouping or structure** in unlabelled data **without predefined categories**."
- "Data points are assigned to clusters based on **similarity or distance measures**."
- The slide's sub-bullet: it "uses Euclidean distance, cosine similarity or other metrics depending on data type and clustering method."

**Where clustering sits in ML.** Supervised learning (classification and regression, Lectures 9–22) trains on pairs (x, y), where y is a known label. Clustering gets only x, with no y. It has no "right answer" to check against, so the algorithm has to find the structure on its own. This is the **unsupervised** paradigm from [[08_ML_Paradigms_Unsupervised_Learning]] from Lecture 3 and [[04_Labeled_vs_Unlabeled_Data]] from Lecture 1.

| | Classification (e.g. k-NN, ID3, Random Forest) | Clustering (e.g. k-Means) |
|---|---|---|
| Training data | features **and** labels | features only |
| Output | a label from a **fixed, known** set | group ids (C1, C2, …) with **no built-in meaning** |
| Evaluation | accuracy, precision/recall, ROC (Lectures 17–19) | internal measures (SSE, silhouette); no ground truth |

**Slide 7: the picture.** The slide shows a 2-D scatter with axes **f1 (X)** and **f2 (Y)**, so each point has two features. The black points form two visible blobs, and the instructor circles them as **C1** (lower-left) and **C2** (upper-right). The handwritten word "**Structure / Pattern**" is the point of the slide. Nobody told the algorithm that two groups exist. The grouping is a structure hidden in the feature values that clustering has to discover.

**Similarity and distance measures.** The bullet on slide 2 names three options:

- **Euclidean** distance: d(a,b) = √Σ(aᵢ − bᵢ)². This is the default for numeric data and the one k-Means uses implicitly, because the mean minimises squared Euclidean distance.
- **Manhattan** (city-block) distance: d(a,b) = Σ|aᵢ − bᵢ|. The worked example of this lecture uses it ([[08_Worked_Example_Eight_Points_Manhattan_Distance]]).
- **Cosine similarity**: cos θ = a·b / (‖a‖‖b‖). It compares direction rather than size. It is common for text documents and embeddings.

Lecture 16 already covered these as distance measures for k-NN ([[04_Distance_Metrics]] from Lecture 16). Clustering reuses the same metrics, but for **grouping** instead of **voting**.

**Two quality goals.** A good clustering has:

- **High intra-cluster similarity**: points inside a cluster are close to each other.
- **Low inter-cluster similarity**: different clusters are far apart.

Slide 5 states this formally for k-Means ([[03_K_Means_Definition_Objective_and_History]]).

**Typical applications** (general knowledge): customer/market segmentation, grouping similar documents or news articles, image segmentation and colour quantisation, anomaly detection (points far from every cluster), gene-expression grouping, and compressing data into a few representative prototypes. Lecture 8 also used clustering as a way to discretise a numeric attribute ([[05_Discretization_by_Clustering]] from Lecture 8).

---

## 2) Simple English Explanation

**What is clustering?** Imagine someone hands you a big box of mixed buttons and says "sort these". They don't tell you the categories. You look at size, colour and shape, and you naturally make piles of buttons that look alike. That is clustering: **putting similar things into the same pile when nobody has told you what the piles should be.**

**Why is it called "unsupervised"?** In the earlier lectures (k-NN, decision trees, random forests) every training example came with an answer, for example "this email is spam" or "this patient has the disease". The computer learned by checking itself against those answers, like a student with a teacher. In clustering **there are no answers at all**. The computer only sees the data and must find the natural groups by itself, with no teacher.

**What slide 2 says, in plain words:**
- People have studied clustering for more than 40 years in many fields, because it is useful almost everywhere.
- It groups similar data points together without labels.
- The aim is to discover hidden groups or patterns.
- To decide what counts as "similar", it measures distance. Points that are close are similar.
- Common rulers for distance are:
  - **Euclidean distance**: the straight-line, "as the crow flies" distance.
  - **Manhattan distance**: walking along city blocks, only left/right and up/down.
  - **Cosine similarity**: checks whether two things point in the same direction. It is often used for text.

**The picture on slide 7.** There is a graph with two features, f1 along the bottom and f2 up the side. Each black square is one data point. If you just look, you can see two clumps. The teacher drew a circle around each and called them **C1** and **C2**, and wrote "**Structure / Pattern**" next to them. That is the whole idea: **the groups were already hiding in the data, and clustering's job is to find them.**

**What makes a "good" set of groups?**
- Things in the **same** group should be very alike (close together).
- Things in **different** groups should be quite different (far apart).

**Where is it used?** Some everyday examples:
- A shop splits customers into "bargain hunters", "brand lovers" and "occasional buyers" without having those labels beforehand.
- A news app groups articles that talk about the same story.
- A photo editor reduces an image to a handful of colours.
- A bank flags a transaction that doesn't fit any normal group as suspicious.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Clustering kya hai?** Socho kisi ne tumhe mixed buttons ka ek bada dabba diya aur kaha "inhe sort karo", par categories nahi batayi. Tum size, colour aur shape dekh ke khud hi ek jaise buttons ke dher bana loge. Yahi clustering hai: **jab kisi ne nahi bataya ki groups kya hone chahiye, tab bhi ek jaisi cheezon ko ek group mein rakhna.**

**Ise "unsupervised" kyun kehte hain?** Pichhle lectures (k-NN, decision tree, random forest) mein har training example ke saath answer aata tha, jaise "ye email spam hai" ya "is patient ko bimari hai". Computer un answers se khud ko check karke seekhta tha, jaise teacher wala student. Clustering mein **koi answer hi nahi hota**. Computer sirf data dekhta hai aur natural groups khud dhoondhta hai. Koi teacher nahi hai, isliye unsupervised.

**Slide 2 seedhi bhasha mein:**
- Clustering pe 40 saal se zyada se research ho rahi hai, kaafi fields mein, kyunki ye har jagah kaam aata hai.
- Ye bina labels ke similar data points ko group karta hai.
- Maksad hai chhupe hue groups ya patterns dhoondhna.
- "Similar" decide karne ke liye distance naapte hain: jo points paas hain, woh similar hain.
- Distance naapne ke common tareeke:
  - **Euclidean**: seedhi line wali doori.
  - **Manhattan**: city blocks mein chalna, sirf left/right aur up/down.
  - **Cosine similarity**: dekhta hai ki do cheezein same direction mein point kar rahi hain ya nahi. Text ke liye zyada use hota hai.

  Ye wahi distance metrics hain jo humne Lecture 16 (k-NN) mein padhe the. Bas wahan unse voting hoti thi, yahan grouping hoti hai.

**Slide 7 ki picture.** Graph pe do features hain: neeche f1 (X) aur side mein f2 (Y). Har kaala square ek data point hai. Dhyan se dekho to do jhund (clumps) dikhte hain. Teacher ne dono ke around circle banaya, unhe **C1** aur **C2** naam diya, aur likha "**Structure / Pattern**". Poori baat yahi hai ki **groups pehle se data mein chhupe the, clustering ka kaam unhe dhoondh nikalna hai.**

**Achhe clusters ki pehchaan:**
- **Same** group ke points ek dusre ke bahut paas hon. Isse kehte hain **intra-cluster similarity high**.
- **Alag** groups ek dusre se door hon. Isse kehte hain **inter-cluster similarity low**.

**Classification vs clustering, ek line mein:** classification mein labels pehle se pata hote hain (spam/not spam). Clustering mein labels hote hi nahi, aur C1, C2 sirf naam hain jinka koi pehle se tay matlab nahi hai.

**Kahan use hota hai?**
- Shop apne customers ko "discount wale", "brand wale" aur "kabhi-kabhi aane wale" groups mein baant leti hai, bina pehle se label ke.
- News app same story wale articles ko ek saath dikhata hai.
- Photo ko sirf kuch colours mein convert karna (colour quantisation).
- Bank ka koi transaction kisi normal group mein fit na ho to use suspicious flag karna.
