# Topic 3: Deep Learning — Complex Concepts from Simpler Ones, and Computational Graphs (Depth)

Source: Lecture 2, slides 9–12 (Deep Learning; Computational Graphs ×3). Figures from the *Deep Learning* book.

---

## 1) Technical Explanation

**Slide 9 — what deep learning does.**

- It tries to address the problem of representation learning.
- Representations are expressed **in terms of other, simpler representations**.
- It develops **complex concepts using simpler concepts**.

**The slide's figure** (a photo of a person fed into a network) shows the layers of such a hierarchy: *visible layer (input pixels)* → *1st hidden layer (edges)* → *2nd hidden layer (corners and contours)* → *3rd hidden layer (object parts)* → *output (object identity: CAR / PERSON / ANIMAL)*. Each layer builds on the one before: pixels → edges → corners/contours → parts → whole object.

**Slides 10–12 — computational graphs.** A computational graph draws a computation as nodes (operations from an *element set* such as +, ×, σ) joined by edges (values). The picture computes

σ( w₁·x₁ + w₂·x₂ )

from inputs w₁, x₁, w₂, x₂: two ×-nodes multiply w₁·x₁ and w₂·x₂, a +-node adds them, and a σ-node (sigmoid) squashes the sum. Slide 11 shows the *same* function with a coarser element set: a single "Logistic Regression" node taking (w, x). Slide 12 adds the key remark:

> *Depth of architecture in terms of the length of the path from input to output. Previous shallow architecture can do computation in parallel but not sequential.*

So **depth depends on the choice of element set**: with {+, ×, σ} the graph above has depth 3 (× → + → σ); with {Logistic Regression} it has depth 1. A deep network is one whose longest input-to-output path is long, which allows *sequential* composition of steps — each step using the previous step's output — rather than only parallel ones. (The 'depth is relative to the element set' point is from the Deep Learning book's own discussion of this figure.)

Link forward: a single neuron/perceptron is the σ(w·x + b) node in this graph ([[09_What_Is_a_Perceptron_Intro_Weights_Bias_and_Applications]]), and the sigmoid is developed in Lecture 8 ([[02_The_Sigmoid_Logistic_Function]]).

---

## 2) Simple English Explanation

Deep learning builds **big ideas out of small ideas**, in layers. Look at the picture of a person:

1. The first layer only sees raw pixels.
2. The next layer finds **edges** (tiny lines).
3. The next finds **corners and curves** by combining edges.
4. The next finds **parts** (a wheel, an eye) by combining curves.
5. The last layer says "this is a car / person / animal".

The "computational graph" slides are a way to *draw* such a calculation: circles for steps (add, multiply, squash), arrows for values flowing through. The example multiplies two pairs of numbers, adds the results, and squashes with σ. **Depth** means how many steps you must do one after another. A deep model can do step after step, each using the last step's answer — a shallow one mostly does many things side by side.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Deep learning **bade ideas ko chhote ideas se, layer-by-layer banata hai**. Picture mein insaan ko dekho:

1. Pehli layer sirf raw pixels dekhti hai.
2. Agli layer **edges** (chhoti lines) dhoondhti hai.
3. Agli layer edges ko jodkar **corners aur curves** dhoondhti hai.
4. Agli layer curves ko jodkar **parts** (pahiya, aankh) dhoondhti hai.
5. Aakhri layer bolti hai "ye car / insaan / janwar hai".

"Computational graph" slides ek calculation ko *draw* karne ka tareeka hain: steps (add, multiply, squash) ke liye circles, aur values ke bahne ke liye arrows. Example do jodiyon ko multiply karta hai, results ko add karta hai, aur σ se squash karta hai. **Depth** ka matlab hai ki kitne steps aapko ek ke baad ek karne padte hain. Deep model step ke baad step kar sakta hai, har step pichle step ka answer use karta hai — shallow model zyada tar kaam saath-saath karta hai.
