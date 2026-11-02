# Topic 0: "Can You See Mistakes in the Network?" — Why Networks Are Hard to Inspect

Source: Lecture 3, slides 1–3 (Title slide; Can you see mistakes in the network? ×2). Slide 2 shows only the title (its picture is blank in the PDF); slide 3 adds four bullet points.

---

## 1) Technical Explanation

Lecture 3's title is **Perceptron** (the title slide reads "ES532: Deep Learning — Perceptron"). It opens with a question, *"Can you see mistakes in the network?"*, and four bullets:

- **It is hard to see what networks are doing.**
- *Example:* "Just move one direction in the network" — i.e. the usual picture of a network is a forward flow from input to output.
- **Flow backward information:** "in the human brain 10 times we have backward connection rather than forward connections". The slide states this as a claim; it is not verified here.
- **Deep Boltzmann machine** — named as an example of a model with such backward/bidirectional connections.

**Reading.** The slide is a motivating hook rather than a worked topic: a trained network is a large collection of numbers (weights) whose behaviour is opaque, so finding *where* it goes wrong is hard — the *interpretability* problem. And information in real neural systems (and in some models, such as Deep Boltzmann Machines) is not only forward: error/feedback information flows backward. That backward flow of error is exactly the idea that the **perceptron's learning rule** (the *Error* arrow on [[01_Recap_Perceptron_Introduction_and_Perceptron_Rule]]) and, later, backpropagation (named in Lecture 10 as the partner of gradient descent) rely on. (The slide itself does not make this connection; it is drawn here as the natural bridge to the rest of the lecture.)

A **Deep Boltzmann Machine** is a deep, undirected, probabilistic network — a different model family from the feed-forward networks studied in this course. The slide only names it.

---

## 2) Simple English Explanation

The teacher shows a neural network picture and asks: "Can you spot where it makes mistakes?" The honest answer is *no, not easily* — a network is a huge pile of numbers, and just looking at it does not tell you what it is thinking.

The slide also says that in our brains, signals do not only travel one way, forward. There are many connections going **backwards** too (the slide claims about ten times as many — a statement we haven't checked). Some network types, like the **Deep Boltzmann machine**, also pass information backward. For us, the idea to remember is: when the network makes an error, that error is sent **back** to fix the weights — that is how a perceptron learns.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Teacher ek neural network ki picture dikhakar poochte hain: "kya aap dekh sakte ho ki isme galti kahan hai?" Imaandari se jawab hai *nahi, aasani se nahi* — network numbers ka bahut bada dher hai, aur sirf dekhne se pata nahi chalta ki wo kya soch raha hai.

Slide ye bhi kehti hai ki hamare dimaag mein signals sirf aage ki taraf nahi jaate. **Peeche** ki taraf bhi bahut saare connections hain (slide ke hisaab se lagbhag das guna zyada — ye baat humne verify nahi ki). Kuch network types, jaise **Deep Boltzmann machine**, bhi information peeche bhejte hain. Hamare liye yaad rakhne wali baat: jab network galti karta hai, to wo error **peeche** bheja jaata hai taaki weights theek ho sakein — perceptron isi tarah seekhta hai.
