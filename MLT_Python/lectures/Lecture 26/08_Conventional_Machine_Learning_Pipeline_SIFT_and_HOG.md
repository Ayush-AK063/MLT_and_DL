# Topic 8: The Conventional Machine Learning Pipeline (SIFT, HOG)

Source: Lecture 26, slide 19 ("Conventional Machine Learning": Low-level sensing → Pre-processing → Feature extraction → Feature selection → Inference: prediction, recognition; Input (motorbike photo) → Feature Representation (e.g., SIFT, HoG, etc.) → Learning algorithm; image credited to LeCun, Bengio & Hinton). Enriched with web research (Lowe, "Distinctive Image Features from Scale-Invariant Keypoints", IJCV 2004; Dalal & Triggs, "Histograms of Oriented Gradients for Human Detection", CVPR 2005; LeCun, Bengio & Hinton, *Nature* 2015). The gradient example and the descriptor-size arithmetic are ours.

---

## 1) Technical Explanation

### The five-stage pipeline (top of the slide)

| Stage | What happens | Where we studied it |
|---|---|---|
| **Low-level sensing** | A sensor records raw data: camera pixels, microphone samples, sensor readings | Data types: [[03_Types_of_Data_Structured_SemiStructured_Unstructured]] from Lecture 5 |
| **Pre-processing** | Clean and normalise: remove noise, fill missing values, scale, crop/resize images | Lectures 6–8, e.g. [[05_Data_Preprocessing_Four_Major_Tasks]] from Lecture 6 |
| **Feature extraction** | Turn raw data into informative numbers (a feature vector) using a **hand-designed** method | [[07_Feature_Extraction_PCA_SVD_LDA]] from Lecture 10 |
| **Feature selection** | Keep only the most useful features, drop redundant/irrelevant ones | [[04_Feature_Selection_Methods_Filter_Wrapper_Embedded]] from Lecture 10 |
| **Inference: prediction, recognition** | A trained model (classifier/regressor) gives the answer | KNN, decision trees, random forest, SVM (Lectures 16–25) |

In conventional ML, **only the last stage learns from data**. The middle stages are designed by people and stay fixed.

### The bottom picture

**Input** (photo of a motorbike) → **Feature Representation** (e.g., SIFT, HoG) → **Learning algorithm**.

The representation is the hand-crafted part. The learning algorithm (e.g., an SVM) only sees the feature vector. If the features miss something important, no learning algorithm can recover it. LeCun, Bengio & Hinton (2015) describe this as the core limitation: for decades, building a pattern-recognition system required careful engineering and domain expertise to design a feature extractor that transformed raw pixels into a suitable representation.

### SIFT (Scale-Invariant Feature Transform)

- **Who/when:** David Lowe, ICCV 1999; full journal version IJCV 2004.
- **Idea:** find distinctive **keypoints** (blob-like spots that stand out at some scale) and describe the patch around each one in a way that stays the same if the image is **scaled, rotated** or the lighting changes a little.
- **Descriptor:** around each keypoint, a 4 × 4 grid of cells; in each cell, a histogram of gradient directions with 8 bins. 4 × 4 × 8 = **128 numbers** per keypoint.
- **Used for:** matching the same object across photos, panorama stitching, object recognition.

### HOG (Histogram of Oriented Gradients)

- **Who/when:** Navneet Dalal & Bill Triggs, CVPR 2005, for **pedestrian detection**.
- **Steps:**
  1. Compute the image gradient at each pixel: gₓ = I(x+1, y) − I(x−1, y), g_y = I(x, y+1) − I(x, y−1); magnitude √(gₓ² + g_y²); orientation atan2(g_y, gₓ).
  2. Split the image into small **cells** (8 × 8 pixels). In each cell, build a histogram of orientations with **9 bins** (0°–180°), each pixel voting with its gradient magnitude.
  3. Group cells into **blocks** of 2 × 2 cells and normalise each block, which makes the feature robust to lighting changes.
  4. Concatenate all block histograms into one long vector, then feed it to a **linear SVM** ([[02_What_Is_an_SVM_Hyperplane_w_x_plus_b]] from Lecture 24).
- **Size check (ours):** the standard 64 × 128 detection window has 8 × 16 cells. Blocks of 2 × 2 cells sliding by one cell give 7 × 15 = 105 blocks. Each block has 4 cells × 9 bins = 36 numbers. Total 105 × 36 = **3,780 features**.

**Tiny gradient example (ours).** A pixel whose left neighbour has brightness 50, right neighbour 200, and top and bottom neighbours both 100:
- gₓ = 200 − 50 = **150**, g_y = 100 − 100 = **0**
- magnitude = **150**, orientation = atan2(0, 150) = **0°**

The brightness changes left-to-right, so this pixel sits on a **vertical edge**. It adds 150 votes to the 0° bin of its cell's histogram. HOG describes a shape by counting how much edge there is in each direction in each small region.

### How this compares with deep learning

SIFT and HOG are clever, but they are the same for every task, they were tuned by hand over years, and they capture only low-level edge statistics. Deep networks learn edge-like detectors in their first layer anyway (Topic 5), and then keep going to textures, parts and objects. On ImageNet in 2012, a CNN that learned its features (AlexNet) beat the best SIFT-plus-classifier systems by about 10 percentage points of top-5 error, which ended the era of hand-crafted vision features. HOG is often described as one of the last major hand-designed feature extractors.

Hand-crafted features are not obsolete everywhere: they are still used where data is small, computing power is limited (embedded devices), or explainability matters.

---

## 2) Simple English Explanation

**The top row of the slide is the "old recipe" for machine learning, in five steps:**

1. **Low-level sensing:** collect raw data. A camera records pixels, a microphone records sound.
2. **Pre-processing:** clean it up. Remove noise, fix missing values, resize photos, put numbers on the same scale (we learned this in Lectures 6–8).
3. **Feature extraction:** turn raw data into useful numbers. A human expert designs a method for this.
4. **Feature selection:** keep only the most useful numbers and throw the rest away (Lecture 10).
5. **Inference:** a trained model, like KNN, a decision tree or an SVM, gives the final answer: "it's a motorbike".

In this old recipe, **only step 5 actually learns from examples.** Steps 3 and 4 are fixed rules a person wrote.

**The bottom picture says the same thing in short:** photo → feature representation (made by a method like SIFT or HOG) → learning algorithm. If the hand-made features miss something important, even the best learning algorithm can't get it back.

**Two famous hand-made image features:**

- **SIFT** (David Lowe, 1999/2004): finds special "landmark" points in a photo and describes the area around each with 128 numbers. The clever part is that the description stays the same if the photo is zoomed or rotated. It is used for stitching panoramas and matching the same object in different photos.
- **HOG** (Dalal and Triggs, 2005): built to spot people walking in photos. It looks at every pixel and asks "which way does the brightness change here, and how strongly?" Then it divides the picture into small 8 × 8 squares and counts how much edge points in each of 9 directions. A standing person gives lots of vertical edges at the sides, for example. All the counts together (3,780 numbers for a standard 64 × 128 window) go to an SVM, which decides "person" or "not person".

**Mini example of HOG's first step:** a pixel has a dark neighbour on the left (50) and a bright one on the right (200), and the same brightness above and below (100 and 100). The left-to-right change is 200 − 50 = 150, the up-down change is 0. So the brightness changes sideways only. That means this pixel sits on an upright (vertical) edge, with strength 150.

**Why deep learning replaced this:** these methods took experts years to design and only describe simple edges. A deep network learns edge detectors by itself in its first layer, then goes on to learn textures, parts and whole objects. In 2012 such a network won the ImageNet competition by a huge margin, and most vision research switched to learned features. Hand-made features are still useful when data is small, the device is weak, or you need to explain exactly what the system looks at.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide ki upar wali row = conventional (purana) ML ka 5-step recipe:**

1. **Low-level sensing:** raw data collect karo. Camera pixels record karta hai, mic awaaz.
2. **Pre-processing:** data saaf karo: noise hatao, missing values bharo, photo resize karo, scaling (Lectures 6–8).
3. **Feature extraction:** raw data ko useful numbers (feature vector) me badlo. Ye method insaan (expert) design karta hai (Lecture 10).
4. **Feature selection:** sirf kaam ke features rakho, baaki hatao (Lecture 10).
5. **Inference (prediction, recognition):** trained model (KNN, decision tree, SVM) final answer deta hai, jaise "ye motorbike hai".

Is recipe me **sirf step 5 data se seekhta hai**. Step 3 aur 4 insaan ke banaye fixed rules hain.

**Neeche wali picture:** Input (motorbike photo) → Feature Representation (SIFT, HoG jaise method se) → Learning algorithm. Agar hand-made features me koi zaroori cheez chhoot gayi, to best learning algorithm bhi use wapas nahi la sakta. LeCun, Bengio, Hinton (2015) ne bhi yahi limitation batayi.

**SIFT (Scale-Invariant Feature Transform):** David Lowe, 1999 (journal 2004). Photo me khaas **keypoints** (landmark jaise points) dhoondhta hai, aur har keypoint ke aas-paas ko **128 numbers** se describe karta hai (4×4 grid, har cell me 8 direction bins: 4×4×8 = 128). Photo zoom ya rotate karo, description same rehta hai. Use: panorama jodna, same object alag photos me match karna.

**HOG (Histogram of Oriented Gradients):** Dalal & Triggs, 2005, **pedestrian (paidal chalte log) detection** ke liye.
1. Har pixel pe gradient: gₓ = right − left brightness, g_y = neeche − upar brightness. Magnitude = √(gₓ² + g_y²), direction = atan2(g_y, gₓ).
2. Photo ko 8×8 pixel ke **cells** me baanto. Har cell me 9 direction bins (0°–180°) ka histogram, har pixel apne magnitude jitna vote deta hai.
3. 2×2 cells ka **block** banake normalise karo, taaki light kam-zyada hone se farak na pade.
4. Sab jod ke ek lamba vector, aur use **linear SVM** (Lecture 24) ko de do.
- **Size check (humara):** 64×128 window me 8×16 cells. 2×2 blocks ek cell slide karke: 7×15 = 105 blocks. Har block 4 cells × 9 bins = 36. Total 105 × 36 = **3,780 features**.

**Chhota gradient example:** pixel ke left me brightness 50, right me 200, upar-neeche dono 100.
- gₓ = 200 − 50 = **150**, g_y = 100 − 100 = **0**
- Magnitude **150**, direction atan2(0, 150) = **0°**
Brightness sirf left-to-right badal rahi hai, matlab pixel ek **vertical edge** pe hai. Ye apne cell ke 0° bin me 150 vote daalega.

**Deep learning ne isko kyun replace kiya?** SIFT/HOG ko experts ne saalon me tune kiya, har task ke liye same rehte hain, aur sirf simple edges describe karte hain. Deep network pehli layer me edge detectors khud seekh leta hai, fir textures, parts, objects tak jaata hai (Topic 5). 2012 ImageNet me AlexNet ne SIFT-based systems ko top-5 error me lagbhag 10 percentage points se haraya, aur hand-crafted vision features ka daur khatam ho gaya. Fir bhi chhote data, kamzor device, ya jahan explain karna zaroori ho, wahan aaj bhi hand-made features use hote hain.
