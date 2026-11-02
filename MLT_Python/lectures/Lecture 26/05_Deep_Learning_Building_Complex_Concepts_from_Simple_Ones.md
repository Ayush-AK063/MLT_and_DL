# Topic 5: Deep Learning: Building Complex Concepts out of Simpler Ones

Source: Lecture 26, slide 12 ("Deep Learning": addresses representation learning, representations expressed in terms of simpler representations, complex concepts from simpler concepts; figure from the *Deep Learning* book, Fig. 1.2: visible layer → edges → corners and contours → object parts → CAR / PERSON / ANIMAL) and slide 18 ("Simple to Complex Features": low-level → mid-level → high-level feature → trainable classifier, from LeCun & Ranzato's ICML 2013 Deep Learning Tutorial). Slide 18 is placed here because it illustrates the same idea; the computational-graph slides 13–15 that sit between them are in Topic 6. Enriched with web research (Goodfellow et al., *Deep Learning*, 2016, ch. 1; Zeiler & Fergus, "Visualizing and Understanding Convolutional Networks", ECCV 2014).

---

## 1) Technical Explanation

### Slide 12: the definition

- Deep learning "tries to address the problem of **representation learning**."
- "Representations are **expressed in terms of other, simpler representations**."
- It "develops **complex concepts** using **simpler concepts**."

This is the answer to the catch at the end of Topic 4. Extracting high-level factors (is it a person?) directly from raw pixels is too hard in one step. Deep learning breaks it into many small steps. Each step builds a slightly more abstract representation from the one below it.

### The figure (Deep Learning book, Fig. 1.2), layer by layer

A photo of a woman enters at the bottom and passes upward through a stack of layers:

| Layer | What its units respond to | How it is computed from the layer below |
|---|---|---|
| **Visible layer** (input pixels) | raw colour values of each pixel | this is the data itself; it is called "visible" because we can observe it |
| **1st hidden layer** (edges) | edges: places where brightness changes sharply, at a given orientation | compare the brightness of neighbouring pixels |
| **2nd hidden layer** (corners and contours) | corners, curves, outlines | look for collections of edges arranged in particular ways |
| **3rd hidden layer** (object parts) | parts such as an eye, a wheel, a nose | look for particular collections of corners and contours |
| **Output** (object identity) | CAR, PERSON, ANIMAL | combine the object parts present in the image |

The layers in the middle are called **hidden** because their values are not given in the data. The model must decide which concepts are useful for explaining the relationships in the observed data. The small pictures inside the circles are real visualisations of what units in a trained network respond to. The book reproduces them from Zeiler & Fergus (2014).

**How the mapping is learned.** The function from pixels to identity is very complicated. Deep learning writes it as a **composition of many simple functions**:

  output = f⁽⁴⁾( f⁽³⁾( f⁽²⁾( f⁽¹⁾(x) ) ) )

Each fⁱ is one layer. Each layer gives a new representation of the input. All the layers are learned together from labelled examples. Nobody programs "edge" or "eye": these detectors appear because they help reduce the error on the final output ([[09_Deep_Learning_Model_and_the_Four_AI_Flowcharts]]).

### Slide 18: Simple to complex features

The figure from LeCun & Ranzato's tutorial shows a photo of a yellow car going through:

  **Low-level feature → Mid-level feature → High-level feature → Trainable classifier → output**

Below each stage is a grid of visualised feature detectors from a convolutional network trained on ImageNet:

- **Low-level:** coloured blobs and short edges at various angles (like the 1st hidden layer above).
- **Mid-level:** textures, stripes, curves, simple patterns built from those edges.
- **High-level:** detectors for object-like structures such as wheels, eyes and text patches.

Zeiler & Fergus (2014) found the same progression by projecting each unit's activation back to pixel space: the lowest layers pick up edges and colour blobs, the middle layers capture textures and repeated patterns, and the higher layers become class-specific and respond to object parts and nearly whole objects.

The key difference from the classical pipeline ([[08_Conventional_Machine_Learning_Pipeline_SIFT_and_HOG]]) is that **all four boxes are trained**, not only the last one.

### Why build in layers? (from the book and general results)

1. **Reuse.** An edge detector learned once is shared by every corner detector that uses it. Every part detector reuses the corner detectors. This makes the representation compact.
2. **Matches the world's structure.** Images are made of parts that are made of smaller parts. Speech is sounds → phonemes → syllables → words. Text is characters → words → phrases → sentences.
3. **Each step is easy.** "Is there a brightness jump here?" is easy. "Do these edges meet at a right angle?" is easy. Stacking easy steps gives a hard concept.
4. **Invariance builds up gradually.** Higher layers can respond to "wheel" regardless of the wheel's exact position and lighting. This is the disentangling of factors of variation from Topic 4.

### Connection with what we already know

A single perceptron ([[05_Perceptron_General_Architecture]] from Lecture 4) is one simple function: weighted sum, then threshold. Lecture 1 already introduced neural networks as layers of such units ([[05_Introduction_to_Neural_Networks]] from Lecture 1). Deep learning stacks many such layers, so the output of one becomes the input of the next.

---

## 2) Simple English Explanation

**Slide 12 in one line:** deep learning builds **complicated ideas out of simple ones**, step by step.

Think of how a child learns to read. First they recognise strokes, then letters made of strokes, then words made of letters, then sentences made of words. Nobody jumps straight from "ink marks" to "meaning of the sentence".

**The picture on the slide** shows a photo of a woman going up through layers of a network:

1. **Bottom (visible layer):** just the colours of the pixels. That's all the computer gets.
2. **Layer 1, edges:** small detectors notice where brightness suddenly changes, for example a dark area next to a light area. That's an edge. You find it by comparing neighbouring pixels.
3. **Layer 2, corners and outlines:** these combine edges. Two edges meeting make a corner. Many edges in a curve make an outline.
4. **Layer 3, object parts:** these combine corners and outlines into parts, like an eye, a nose or a wheel.
5. **Top (output):** combine the parts to decide: **car, person or animal?** Here: person.

The middle layers are called **hidden** because the data never tells us what they should be. The network invents them.

**The key point:** nobody programmed "edge detector" or "eye detector". We only showed the network many labelled photos. These detectors appeared by themselves because they helped it get the final answer right. Researchers (Zeiler and Fergus, 2014) later made pictures of what each layer responds to, and the little images inside the circles on the slide come from that work.

**Slide 18 shows the same idea with a yellow car:**
- **Low-level features:** colour patches and short lines at different angles.
- **Mid-level features:** stripes, curves and textures made from those lines.
- **High-level features:** wheel-like circles, grille-like patterns, parts of objects.
- **Trainable classifier:** makes the final decision.

The important word is *trainable*: in deep learning **every stage** is learned from data, not only the last one. In older systems the first stages were hand-made (Topic 8).

**Why build in layers?**
- Simple parts are re-used: one edge detector helps many corner detectors.
- The real world is built that way: objects are made of parts, words of letters, speech of sounds.
- Each step is easy on its own, but many easy steps together can solve a hard problem.
- Higher layers gradually stop caring about unimportant things like exact position or lighting.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Slide 12 ka main point:** Deep learning **complex concept ko simple concepts se** banata hai, step by step. Slide ke words: "Representation are expressed in terms of other simpler representation" aur "Develop complex concept using simpler concept." Ye representation learning ki problem ko address karne ka tareeka hai.

Socho bachcha padhna kaise seekhta hai: pehle lines/strokes, fir strokes se letters, letters se words, words se sentences. Seedha "syahi ke nishaan" se "sentence ka matlab" pe koi nahi jaata.

**Slide wali picture (Deep Learning book, Fig 1.2):** Ek aurat ki photo neeche se upar layers me jaati hai:

1. **Visible layer (input pixels):** sirf pixels ke colour values. "Visible" isliye kyunki ye data hum dekh sakte hain.
2. **1st hidden layer (edges):** jahan brightness achanak badalti hai (dark ke bagal me light), wahan edge. Ye padosi pixels ki brightness compare karke milta hai.
3. **2nd hidden layer (corners aur contours):** edges ko jodta hai. Do edges mile to corner, kai edges curve me to outline.
4. **3rd hidden layer (object parts):** corners aur contours se parts banata hai: aankh, naak, wheel.
5. **Output (object identity):** parts dekh ke decide: **CAR, PERSON ya ANIMAL?** Yahan PERSON.

Beech wali layers ko **hidden** kehte hain kyunki data me unki value di nahi hoti. Model khud decide karta hai ki kaun se concepts useful hain. Circles ke andar ki chhoti images asli trained network ki visualisation hain (Zeiler & Fergus, 2014).

**Math me:** pixels se identity tak ka function bahut complicated hai. Deep learning usko bahut saare simple functions ka **composition** bana deta hai: output = f⁽⁴⁾(f⁽³⁾(f⁽²⁾(f⁽¹⁾(x)))). Har fⁱ ek layer hai, har layer input ka naya representation deti hai. Sab layers labelled examples se ek saath seekhi jaati hain. "Edge detector" ya "eye detector" kisi ne program nahi kiya, wo khud ban gaye kyunki final answer sahi karne me madad karte hain.

**Slide 18 (Simple to Complex Features), yellow car ke saath:** Low-Level Feature → Mid-Level Feature → High-Level Feature → Trainable Classifier.
- **Low-level:** colour ke dhabbe aur alag-alag angle pe chhoti lines (edges).
- **Mid-level:** in lines se bani stripes, curves, textures.
- **High-level:** wheel jaise gol shapes, aankh jaise patterns, object ke parts.
- **Trainable classifier:** final decision.

Important word hai **trainable**: deep learning me **har stage** data se seekhi jaati hai, sirf last wali nahi. Purane systems me pehli stages haath se banti thi (Topic 8).

**Layers me kyun banate hain?**
1. **Reuse:** ek edge detector bahut saare corner detectors ke kaam aata hai.
2. **Duniya aisi hi bani hai:** object parts se, parts chhote parts se; speech me sounds → syllables → words; text me letters → words → sentences.
3. **Har step aasaan:** "yahan brightness jump hai?" aasaan sawaal hai. Aise aasaan steps jod ke mushkil concept ban jaata hai.
4. **Dheere-dheere invariance:** upar ki layers wheel ko pehchaanti hain chahe wo kahin bhi ho ya light kaisi bhi ho. Yahi Topic 4 wala factors of variation alag karna hai.

**Pehle padha hua connection:** Lecture 4 ka perceptron ek simple function hai (weighted sum + threshold). Lecture 1 me neural network ko aise units ki layers bataya tha. Deep learning bahut saari layers stack karta hai, ek ka output agle ka input.
