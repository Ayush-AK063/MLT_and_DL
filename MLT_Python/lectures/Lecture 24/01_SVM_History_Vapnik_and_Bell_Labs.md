# Topic 1: History of Support Vector Machines

Source: Lecture 24, slides 1–2 (title slide "Machine Learning — Support Vector Machine", Dr. Yashwant Singh Patel, ABV-IIITM Gwalior; "History" slide with Vapnik's photo and handwritten notes "kernels 2D → 3D", "AT&T Bell Laboratories", "(1982)", "1992", "(Neural Info. Processing System)", "→ linear & non-linear classification"). Enriched with web research (history of SVMs: Vapnik & Chervonenkis' "generalized portrait", Boser–Guyon–Vapnik 1992, Cortes & Vapnik 1995).

---

## 1) Technical Explanation

### What slide 2 says

- "SVM is a classifier derived from **statistical learning theory** by **Vapnik and Chervonenkis**". The instructor added "(1982)".
- "SVMs introduced by **Boser, Guyon, Vapnik** in **COLT-92**". The instructor circled "1992". COLT is the Conference on Computational Learning Theory.
- "Initially popularized in the **NIPS** community". The instructor expanded NIPS as "Neural Information Processing Systems", now called NeurIPS. It is "now an important and active field of all Machine Learning research."
- "Special issues of Machine Learning Journal, and Journal of Machine Learning Research."
- The photo is **Vladimir Vapnik**. Other handwritten notes:
  - "**AT&T Bell Laboratories**": where the 1990s SVM work was done.
  - "**kernels: 2D → 3D**": the kernel idea of mapping data to a higher dimension ([[06_Kernels_Linear_vs_Nonlinear_and_the_Kernel_Trick]]).
  - "**→ linear & non-linear classification**": SVMs handle both.

### Fuller timeline (from web research)

| Year | Milestone |
|---|---|
| 1963–64 | **Vapnik & Lerner / Vapnik & Chervonenkis** (Moscow) describe the "**generalized portrait**" algorithm: a maximum-margin linear separator. This is the original linear SVM idea. |
| 1960s–70s | **Vapnik–Chervonenkis (VC) theory**: the VC dimension and bounds on generalisation error. This is the "statistical learning theory" the slide mentions. |
| 1982 | Vapnik's book *Estimation of Dependences Based on Empirical Data* (English translation), the date the instructor wrote. It summarises the theory and the optimal separating hyperplane. |
| 1992 | **Boser, Guyon & Vapnik**, "A training algorithm for optimal margin classifiers" (COLT '92, AT&T Bell Labs). Introduces the **kernel trick**, which turns maximum-margin linear classifiers into **non-linear** ones. |
| 1995 | **Cortes & Vapnik**, "Support-Vector Networks" (*Machine Learning* journal). Introduces the **soft margin** (slack variables + parameter C) for data that is not perfectly separable. This is the form used today. |
| late 1990s–2000s | SVMs become a leading method for handwriting recognition (e.g. MNIST digits), text classification and bioinformatics. Libraries like LIBSVM appear, and scikit-learn's `SVC` is built on LIBSVM. |

**Why SVMs mattered.** They came with a theory of *why* they generalise: maximising the margin controls the model's capacity, and that comes from VC theory. They also gave a convex optimisation problem with a single global optimum, unlike neural networks of that era. Before deep learning took over (around 2012), SVMs were the state of the art on many benchmarks.

**Where this lecture fits.**
- Like the perceptron ([[03_Perceptron_Basics_and_Biological_Neuron]] from Lecture 4), an SVM is a **linear classifier** w·x + b. But it doesn't accept just any separating line. It chooses the one with the **largest margin**.
- With kernels it becomes non-linear, which solves the problem from [[06_Linear_Separability_Concept]] from Lecture 4: data that no straight line can separate.

---

## 2) Simple English Explanation

**Who invented SVMs?** The idea comes from the Russian mathematician **Vladimir Vapnik** (the man in the photo) and his colleague **Alexey Chervonenkis**. They worked on a branch of maths called **statistical learning theory**, which asks: *when can a machine that learned from examples be trusted on new examples?*

**The timeline, simply:**
- **1960s:** Vapnik and colleagues describe the first version: draw the straight line that separates two groups with the **widest possible gap**.
- **1982:** Vapnik's book (the year the teacher wrote) brings this theory to English readers.
- **1992:** At **AT&T Bell Laboratories** in the USA, Boser, Guyon and Vapnik present SVMs at the COLT-92 conference. They add the famous "**kernel trick**", a way to bend the straight line into curves by imagining the data in a higher dimension. The teacher's note "kernels 2D → 3D" points to this.
- **1995:** Cortes and Vapnik add the "**soft margin**". This lets the method put up with a few messy points instead of demanding a perfect separation, which makes it practical for real data.
- **After that:** SVMs became hugely popular in the **NIPS** (Neural Information Processing Systems) research community and in journals. For about 15 years they were among the best tools for reading handwriting, sorting text and analysing genes.

**Why people loved them.**
- They have solid maths behind them.
- Training always finds the single best answer. It doesn't get stuck like some other methods.
- They work for both **straight-line (linear)** and **curved (non-linear)** separation, as the teacher noted at the bottom of the slide.

**Connection to earlier lectures.** The perceptron (Lecture 4) also draws a straight line between two classes, but it stops at *any* line that works. An SVM insists on the line that keeps the **biggest safety gap** on both sides.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**SVM kisne banaya?** Idea Russian scientist **Vladimir Vapnik** (photo wale) aur unke saathi **Alexey Chervonenkis** ka hai. Ye **statistical learning theory** pe kaam karte the, jo poochti hai: *examples se seekhi machine pe naye examples ke liye kab bharosa kar sakte hain?*

**Timeline, seedhi bhasha mein:**
- **1963–64:** Vapnik aur saathiyon ne pehla version diya, jiska naam "generalized portrait" tha. Do groups ke beech woh seedhi line kheencho jiske dono taraf **sabse chauda gap** ho.
- **1982:** Teacher ne yahi saal likha. Vapnik ki kitaab (English translation) aayi jisne ye theory duniya tak pahunchayi.
- **1992:** USA ki **AT&T Bell Laboratories** mein Boser, Guyon aur Vapnik ne **COLT-92** conference mein SVM present kiya (teacher ne 1992 circle kiya hai).
  - Isme famous **kernel trick** aaya, jo data ko upar wale dimension mein le jaake seedhi line ko curve bana deta hai.
  - Teacher ka note "kernels 2D → 3D" isi ki taraf ishaara hai.
- **1995:** Cortes aur Vapnik ne **soft margin** joda. Ab kuch gande (noisy) points ko bardaasht karna allowed hai, perfect separation zaroori nahi. Isi se SVM real data pe kaam ka bana.
- **Uske baad:** **NIPS** community mein bahut popular hua (teacher ne likha: Neural Information Processing Systems, aaj ka NeurIPS). Machine Learning Journal aur JMLR ne special issues nikaale. Lagbhag 15 saal tak handwriting padhne, text sort karne aur genes analyse karne ke liye ye top tools mein tha. 2012 ke baad deep learning aage nikal gaya.

**Log ise kyun pasand karte the?**
- Peeche pakki maths hai, jo batati hai ki ye naye data pe kyun achha chalta hai (margin bada → model control mein).
- Training hamesha ek hi best answer pe pahunchti hai (convex problem), kahin atakti nahi.
- **Linear aur non-linear dono** tarah ka classification karta hai, jaise teacher ne slide ke neeche likha.

**Pichhle lectures se connection.** Lecture 4 ka perceptron bhi do classes ke beech seedhi line kheenchta hai, par *koi bhi* chalne wali line pe ruk jata hai. SVM ziddi hai: woh wahi line chunega jiske dono taraf **sabse bada safety gap (margin)** ho.
