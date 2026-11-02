# Topic 4: Why Boolean Functions Matter — the Movie Example, and the Name "MLP"

Source: Lecture 7, slides 18–24 ("Again, why do we care about Boolean functions?"; "How does this help us with our original problem: which was to predict whether we like a movie or not?"; the data matrix of p's and n's; Remarks: Multilayer Perceptrons; "Multilayered Network of Perceptrons"; representation power of a single-hidden-layer MLP). Slide 25 is "Thank you".

---

## 1) Technical Explanation

**The question (slides 18–19).** Why spend a lecture on Boolean functions when the real goal is the *original problem*: **predict whether we like a movie or not**? (The movie-liking problem is the running example from the sigmoid-neuron lecture, [[01_Why_Perceptron_Thresholding_Is_Too_Harsh]], Lecture 8.)

**The data (slides 20–21).** *We are given this data about our past movie experience.* A matrix with one row per movie: the values of the **factors x₁, x₂, …, xₙ** that the decision is based on, and the label **y (like / dislike)**. The rows are split into:

- **pᵢ — points for which the output was 1** (liked), written y = 1,
- **nⱼ — points for which the output was 0** (disliked), written y = 0.

*The data may or may not be linearly separable.*

**The conclusion (slide 21).** *The proof that we just saw tells us that it is possible to have a network of perceptrons and learn the weights in this network such that for any given pᵢ or nⱼ the output of the network will be the same as yᵢ or yⱼ (i.e., we can separate the positive and the negative points).* In other words: a network with one hidden layer of enough perceptrons can fit **every training example** of a Boolean-valued problem, **even if no single line separates likes from dislikes**.

**Care needed (not stated on the slide).** (1) The theorem as proved is for **Boolean** inputs; for real-valued factors (ratings, durations) the construction must be extended — the subject of Lecture 8's "arbitrary functions" ([[00_Recap_From_Boolean_to_Arbitrary_Functions]]). (2) Fitting every training point is **not** the same as predicting new movies well (over-fitting, cf. MLT notes on generalisation); it shows only that the model class is *rich enough*. (3) The same input vector must not carry two different labels, or no function can fit.

**Remarks (slides 22–24).**

- *Networks of the form that we just saw (containing an input, output and one or more hidden layers) are called **Multilayer Perceptrons (MLP)**.*
- *More appropriate terminology would be "**Multilayered Network of Perceptrons**" but MLP is the more commonly used name.* (The units are perceptron-style neurons; the *network* is multilayer.)
- *The theorem that we just saw gives us the **representation power of an MLP with a single hidden layer**. Specifically, it tells us that an MLP with a single hidden layer can represent **any Boolean function**.*

Terminology used here ties back to [[03_Terminology_Input_Hidden_and_Output_Layers_and_Layer_Weights]] (Lecture 6) and forward to the feedforward-network notation of Lecture 9 ([[01_Feedforward_Network_Architecture_Layers_and_Notation]]).

**Typos on the slides (harmless):** "prrof", "givne", "or past movie experience" ("our"), and "(x₁,x₂,…,xₙ(" with an unbalanced bracket. Meaning is unaffected.

---

## 2) Simple English Explanation

**Why bother with logic functions?** Because our real aim is something like **"will I like this movie?"** — and that is a yes/no decision based on several yes/no-style facts about the movie.

Suppose we have a list of movies we've watched: for each, the facts (genre, actor, director, …) and whether we **liked it (1)** or **not (0)**. The liked ones are the **p**'s and the disliked ones the **n**'s. Maybe no single straight line can separate the likes from the dislikes.

The theorem we just learned says: **there is a network with a middle layer that gets every one of those past movies right**, whether or not a straight line works. That is exactly what we wanted.

(Two honest cautions: the proof is for yes/no inputs, and getting the *old* movies all right doesn't automatically mean getting *new* movies right.)

**Naming:** a network with an input layer, an output layer and one or more middle (hidden) layers is called a **Multilayer Perceptron (MLP)**. The slide says a more accurate name would be "multilayered network of perceptrons", but MLP is what everyone says. The theorem tells us a **one-hidden-layer MLP can represent any logic function.**

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Logic functions ki parwah kyun?** Kyunki hamara asli maqsad kuch aisa hai jaise **"kya mujhe ye movie pasand aayegi?"** — jo movie ke baare mein kai yes/no jaise facts par based haan/naa ka decision hai.

Maan lo hamare paas dekhi hui movies ki list hai: har ek ke liye facts (genre, actor, director, …) aur ye ki humein wo **pasand aayi (1)** ya **nahi (0)**. Pasand aayi hui movies **p** hain aur napasand wali **n**. Ho sakta hai koi ek seedhi line likes ko dislikes se alag na kar sake.

Abhi jo theorem seekha wo kehta hai: **ek beech ki layer wala network hai jo un saari purani movies ko sahi bata deta hai**, chahe seedhi line kaam kare ya nahi. Hume yahi chahiye tha.

(Do imaandaar savdhaaniyan: proof yes/no inputs ke liye hai, aur *purani* movies sahi karne ka matlab ye nahi ki *nayi* movies bhi sahi hongi.)

**Naam:** jis network mein input layer, output layer aur ek ya zyada beech (hidden) layers hon, use **Multilayer Perceptron (MLP)** kehte hain. Slide kehti hai ki sahi naam "multilayered network of perceptrons" hota, par sab MLP hi kehte hain. Theorem batata hai ki **ek-hidden-layer MLP koi bhi logic function represent kar sakta hai.**
