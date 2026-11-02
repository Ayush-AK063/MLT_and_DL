# Topic 7: Historical Trends — Growing Datasets, the MNIST Dataset, Connections per Neuron, Number of Neurons

Source: Lecture 2, slides 24–28 (Historical Trends: Growing Datasets ×2; The MNIST Dataset; Connections per Neuron; Number of Neurons). All figures from the *Deep Learning* book.

---

## 1) Technical Explanation

**Growing datasets (slides 24–25).** A log-scale plot of **dataset size (number of examples)** against year, from 1900 to beyond 2015, with the vertical axis running from 10⁰ to 10⁹. Labelled datasets include *Criminals* (an early-1900s study, on the order of 10³), *Iris* (1936, about 10², i.e. 150 flowers — see the Iris notes in [[04_Iris_Dataset_Features_Targets_and_Problem_Types]]), *T vs G vs F*, *Rotated T vs C*, *MNIST*, *CIFAR-10*, *ImageNet*, *ImageNet10k*, *Public SVHN*, *ILSVRC 2014*, *Canadian Hansard*, *WMT* and *Sports-1M*. Sizes rise from **hundreds of examples** to **millions and beyond** (the largest points reach roughly 10⁸–10⁹). (Slide 24 is the same slide before the figure appears; its picture is blank in the PDF.)

**MNIST (slide 26).** A grid of **handwritten digits 0–9** — a standard small benchmark (in the book: 28×28 greyscale images of digits). It sits mid-chart among the datasets above. (Image dimensions are background knowledge, not stated on the slide.)

**Connections per neuron (slide 27).** Log-scale plot: average number of connections per neuron for numbered networks over time (1950–2015), with reference lines for animal brains — **fruit fly, mouse, cat, human**. Early networks had well below 100 connections per neuron; by ~2015 some artificial networks reached the **mouse/cat** range (hundreds to roughly 10³–10⁴), approaching the animals' levels.

**Number of neurons (slide 28).** Log-scale plot (10⁻² to 10¹¹) of the **number of neurons** in numbered networks from the 1950s on, against reference lines from **sponge, roundworm, leech, ant, bee, frog, octopus** up to **human**. A blue trend line extrapolates the growth (the book puts the doubling time at roughly 2.4 years) to about **2056** to reach human-brain scale. In ~2015 networks sat around the size of a frog–bee range, far below a human's.

**Takeaway tied to slide 23:** more data + more compute + larger models = better accuracy ([[06_Content_Organization_and_History_of_Deep_Learning]]). The comparison with animal brains is a loose size analogy only; the number of neurons does not imply equal capability.

*Note on precision:* axis values above are read off the book's figures as approximate magnitudes; the slides carry no numbers beyond the axes and labels.

---

## 2) Simple English Explanation

Four charts show *why deep learning took off*:

1. **Datasets got huge.** In 1936 the famous Iris dataset had just 150 flowers. Today's image and text collections have millions or billions of examples. Neural networks learn better from more data.
2. **MNIST** is a famous practice set — thousands of handwritten digits (0–9) that a network learns to read.
3. **Connections per neuron.** Early artificial neurons were wired to very few others; modern networks have many more links per neuron, coming close to a mouse or cat's brain.
4. **Number of neurons.** Networks grew from a handful of neurons to millions — the size of a small animal's brain — but still far below a human's (the book guesses around 2056 if growth continues).

---

## 3) Hinglish Explanation (Beginner-Friendly)

Chaar charts dikhate hain ki *deep learning kyun chal nikla*:

1. **Datasets bahut bade ho gaye.** 1936 mein mashhoor Iris dataset mein sirf 150 phool the. Aaj ke image aur text collections mein lakhon-karodon examples hain. Neural networks zyada data se behtar seekhte hain.
2. **MNIST** ek mashhoor practice set hai — haath se likhe digits (0–9) ke hazaaron examples jinhe network padhna seekhta hai.
3. **Connections per neuron.** Shuruaati artificial neurons bahut kam doosre neurons se jude the; modern networks mein ek neuron ke zyada links hain, jo chuhe ya billi ke dimaag ke kareeb pahunch gaye hain.
4. **Number of neurons.** Networks ek chhoti sankhya se lakhon neurons tak gaye — chhote janwar ke dimaag jitne — par abhi bhi insaan se bahut kam (book ka andaza hai ki agar growth chalti rahi to lagbhag 2056).
