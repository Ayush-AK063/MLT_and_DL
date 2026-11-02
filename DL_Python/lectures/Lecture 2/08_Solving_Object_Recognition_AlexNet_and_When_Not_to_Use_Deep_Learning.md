# Topic 8: Solving Object Recognition — AlexNet (2012), and When Not to Use Deep Learning

Source: Lecture 2, slides 29–30 (Solving Object Recognition ×2, the second with the instructor's handwritten-style notes). Figure from the *Deep Learning* book. Enriched with web research (AlexNet's competition result).

---

## 1) Technical Explanation

**The chart (slides 29–30).** *ILSVRC classification error rate* (vertical axis, 0 to 0.30) for each year from **2010 to 2015**. Reading the line: about **0.28 in 2010**, ~0.26 in 2011, ~0.16 in 2012, ~0.12 in 2013, ~0.07 in 2014 and ~0.04 in 2015 — a steep, steady fall. (Values read from the plot.)

**The slide's text:** *"In 2012, Geoffrey Hinton and his students Alex Krizhevsky and Ilya Sutskever won the ImageNet Large Scale Visual Recognition Challenge with their pioneering deep convolutional neural network, AlexNet."*

Web research adds numbers: in ILSVRC-2012 **AlexNet reached a top-5 error of 15.3%, versus 26.2% for the second-best entry** — a gap of about ten percentage points, in a benchmark that had been improving by only a couple of points a year. That jump is why 2012 is called the moment deep learning "arrived" in computer vision. (The slide's plotted value for 2012 is the same ~0.16 — consistent with 15.3%.) After 2012 the winning entries were all deep networks, and the error fell below the commonly quoted ~5% human-level figure by 2015.

**Slide 30 — "when not to use a neural net" (instructor's notes, transcribed as written):**

- *Scenario where we should not use a neural net:* when you have a **very limited computational budget** → use some **shallow algorithms** instead.
- *Too much noise and not structured, e.g. understanding speech* → **use DL**.
- *Artificial and noisy data* → **do not use DL**.

**Reading these notes.** The first and third bullets are guidance on *avoiding* DL (little compute; artificial/synthetic data that is noisy), while the second says DL *suits* messy, unstructured, real-world inputs such as speech. The notes are terse; the third bullet's wording ("artificial and noisy") is ambiguous — it most plausibly means artificially generated noisy data, where the noise is not real signal that a model could learn from. General practical guidance consistent with the notes: with small datasets or tight compute, simpler methods (linear models, trees, SVMs) are often as good and much cheaper.

---

## 2) Simple English Explanation

The graph shows a competition where computers try to name what is in millions of photos. Every year the mistakes fell — but in **2012** a team led by Geoffrey Hinton with his students used a deep neural network called **AlexNet** and made far fewer mistakes than everyone else (about 15% wrong against about 26% for the next best). After that, almost everyone switched to deep networks, and by 2015 the error was around 4%.

**When not to use deep learning:**

- You don't have much computing power — use simpler, lighter methods.
- Your data is fake/artificial and noisy — deep learning won't help.
- But if the data is real, messy and unstructured (like speech), deep learning is a great choice.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Graph ek competition dikhata hai jisme computers lakhon photos mein kya hai ye batane ki koshish karte hain. Har saal galtiyan kam hoti gayin — par **2012** mein Geoffrey Hinton aur unke students ki team ne **AlexNet** naam ka deep neural network use kiya aur baaki sabse bahut kam galtiyan ki (lagbhag 15% galat, jabki doosri best team ki lagbhag 26%). Uske baad lagbhag sabne deep networks apna liye, aur 2015 tak error lagbhag 4% reh gaya.

**Deep learning kab use nahi karna:**

- Computing power kam hai — simple, halke methods use karo.
- Data artificial/nakli aur noisy hai — deep learning se fayda nahi.
- Lekin agar data asli, messy aur unstructured hai (jaise speech), to deep learning achha choice hai.
