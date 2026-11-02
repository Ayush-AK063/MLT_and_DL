# Topic 3: Pre-processing Needs for Unstructured Data (Text & Images)

Source: Lecture 6, slide 10 (Need for Data Pre-processing — Unstructured Data).

---

## 1) Technical Explanation

While the previous topic focused on messiness in **structured** data (missing/noisy/inconsistent values), this slide previews the *different* kinds of pre-processing needed for **unstructured** data — specifically **text** and **images** — connecting back to the unstructured data category introduced in Lecture 5 ([[03_Types_of_Data_Structured_SemiStructured_Unstructured]] from Lecture 5).

**Unstructured Data (Text) — pre-processing steps**:
1. **Lower Case**: converting all text to lowercase, so that "Data" and "data" are treated as the same word rather than two different tokens.
2. **Normalization**: removing punctuation, special symbols, and URLs — stripping out characters/elements that usually don't carry meaningful semantic content for most NLP tasks.
3. **Stopwords Removal**: removing extremely common words that carry little distinguishing meaning — the lecture gives examples: *"of, and, the, ...."* These words appear so frequently across all documents that they add noise rather than signal for many text-analysis tasks.
4. **Stemming/Lemmatization**: reducing different grammatical forms of a word to a common base/root form. The lecture's example: `plays, playing, played → play`. (Stemming and lemmatization are related but technically distinct techniques — stemming crudely chops word endings using rules, while lemmatization uses vocabulary/grammar knowledge to find the proper dictionary root — but both achieve this same normalization goal.)

**Unstructured Data (Images) — pre-processing steps**:
1. **Read image**: loading the raw image file into a usable data format (e.g., pixel arrays).
2. **Resize image**: standardizing image dimensions, since ML models (especially neural networks) generally require fixed input sizes.
3. **Remove noise (Denoise)**: reducing random visual noise/artifacts in the image that could confuse a model.
4. **Segmentation**: partitioning the image into meaningful regions (directly connects to the "Scene Segmentation" concept from Lecture 3's Computer Vision topic, [[01_Computer_Vision_Applications]] from Lecture 3).
5. **Morphology (smoothing edges)**: applying morphological operations to clean up shapes — smoothing jagged edges, filling small holes, removing small noise specks in binary/segmented images.

**Why this distinction matters**: this slide makes explicit that "data pre-processing" isn't a one-size-fits-all recipe — the specific techniques depend entirely on the data's structure/modality. Structured (tabular) data needs value-level cleaning (covered in depth later in this lecture); text needs linguistic normalization; images need visual/pixel-level processing. This foreshadows that later lectures will likely go deeper into NLP-specific and CV-specific pipelines separately.

---

## 2) Simple English Explanation

So far, this lecture has talked about cleaning messy *tables* of data (missing values, weird numbers). But unstructured data — like text and images — needs a completely different kind of cleanup before it's ready for a model.

**Cleaning up text data:**
1. **Lower case** — turn all the text into lowercase, so "Data" and "data" aren't treated as two totally different words by the computer.
2. **Normalization** — strip out punctuation marks, weird symbols, and web links, since these usually don't help a model understand meaning.
3. **Removing stopwords** — get rid of extremely common, low-meaning words like "of," "and," "the." These words show up everywhere and don't really tell you much about what makes one piece of text different from another.
4. **Stemming/Lemmatization** — reduce different forms of the same word down to one base form. For example, "plays," "playing," and "played" all really mean the same core idea — "play" — so they get collapsed into that one form. This helps the model treat them as the same concept instead of three unrelated words.

**Cleaning up image data:**
1. **Read the image** — load it into the computer in a usable format.
2. **Resize the image** — make sure all images are the same size, since models usually need consistent input dimensions.
3. **Remove noise (Denoise)** — clean up random visual "graininess" or artifacts that could confuse the model.
4. **Segmentation** — divide the image into meaningful parts (like separating "the road" from "the sky" from "a car" in a street photo — you learned about this back in the Computer Vision lecture).
5. **Morphology (smoothing edges)** — clean up rough or jagged shapes in the image, smoothing edges and filling small gaps.

**The big takeaway**: there's no single universal "cleaning recipe" — how you clean data depends completely on what *kind* of data it is (spreadsheet numbers vs. text vs. images all need very different treatment).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab tak is lecture mein hum tables/spreadsheets wale data (missing values, ajeeb numbers) saaf karne ke baare mein baat kar rahe the. Lekin **unstructured data** — jaise text aur images — ko model ke liye taiyar karne se pehle **bilkul alag tarike ka cleanup** chahiye hota hai.

**Text Data ko saaf karna:**
1. **Lower Case (chhote letters)** — poore text ko lowercase mein badal do, taaki "Data" aur "data" ko computer 2 alag words na samjhe.
2. **Normalization** — punctuation marks, ajeeb symbols, aur web links hata do, kyunki ye usually model ko meaning samajhne mein madad nahi karte.
3. **Stopwords Removal (kam-important words hataana)** — bahut common, low-meaning words jaise "of," "and," "the" hata do. Ye words har jagah aate hai aur ye zyada nahi batate ki ek text doosre se kaise alag hai.
4. **Stemming/Lemmatization** — ek hi word ke alag-alag forms ko ek base form mein badal do. Jaise, "plays," "playing," aur "played" sab ka core matlab hai "play" — isliye inko ek hi form mein collapse kar dete hai. Isse model in teeno ko ek hi concept samajhta hai, alag-alag nahi.

**Image Data ko saaf karna:**
1. **Read Image** — image ko computer mein use-karne-layak format mein load karna.
2. **Resize Image** — sab images ka size same karna, kyunki models ko usually fixed size input chahiye hota hai.
3. **Remove Noise (Denoise)** — random visual "graininess" ya artifacts saaf karna jo model ko confuse kar sakte hai.
4. **Segmentation** — image ko meaningful parts mein baantna (jaise ek street photo mein "road," "sky," "car" ko alag-alag identify karna — ye aapne Computer Vision wale lecture mein padha tha).
5. **Morphology (edges smooth karna)** — image mein rough/jagged shapes ko saaf karna, edges ko smooth karna, chhote gaps ko bharna.

**Sabse important baat**: data clean karne ka **koi ek universal recipe nahi hai** — data kis type ka hai (spreadsheet numbers vs. text vs. images), uske hisaab se cleaning ka tarika bilkul alag hota hai.
