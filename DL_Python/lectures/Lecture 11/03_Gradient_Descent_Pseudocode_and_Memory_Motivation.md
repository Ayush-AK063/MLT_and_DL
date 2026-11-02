# Topic 3: Gradient Descent Pseudocode, and Why Memory Limits Force Mini-Batching

Source: Lecture 11 (ES532: Introduction to Deep Learning), slide 8. The byte-size calculation below was independently verified against the slide's own handwritten numbers.

---

## 1) Technical Explanation

**The pseudocode, exactly as given**:

> **Input**: parameters ($\theta$), gradient of the loss function with respect to the parameters ($d\theta$), learning rate ($\alpha$)
> **Update parameters**: $\theta = \theta - \alpha \times d\theta$
> **Output**: updated parameters ($\theta$)

This is the same update rule that has appeared in every gradient-descent-family algorithm covered so far in this repo, just written generically: $\theta$ stands for whatever parameters are being trained, $d\theta$ for the gradient (however it was computed — one example, a mini-batch, or the whole dataset), and $\alpha$ for the learning rate (called $\eta$ elsewhere in these notes — the two symbols are used interchangeably across sources).

**The handwritten annotations sort the more advanced algorithms by which base category they extend**: **Momentum**, **RMSprop**, and **Adam** are grouped together as building on **MBGD** (Mini-Batch Gradient Descent) — i.e., all three of Lecture 0's more sophisticated optimizers ([[04_Momentum]], [[08_RMSprop]], [[09_Adam]]) are, in practice, run *on top of* mini-batches rather than on single examples or the full dataset. **SGD** is separately annotated as its own category.

**Why mini-batching is a practical necessity, not just a convenience — a worked, verified example**: the diagram's side annotations mention memory constraints ("computationally expensive," "time consuming," "RAM/GPU → out of memory") and a set of numbers: $1\text{GB}=10^9$ (bytes, using the common approximation), $100$GB, "$100{,}000 \to 1$ million," "$10^{11}$ bytes," and "$1000\times1000$ pixels." Putting these together into a concrete, checkable calculation:

$$100{,}000 \text{ images} \times (1000\times1000 \text{ pixels/image}) \times 1\text{ byte/pixel} = 100{,}000 \times 1{,}000{,}000 = 10^{11} \text{ bytes}$$

$$10^{11} \text{ bytes} \div 10^9 \text{ bytes/GB} = 100\text{ GB}$$

This matches the slide's own annotated numbers exactly ($10^{11}$ bytes, $100$GB) — confirming the intended illustration: a dataset of just $100{,}000$ modestly-sized ($1000\times1000$-pixel) images already requires roughly $100$GB just to store, which is far more than fits in a typical machine's RAM or a GPU's onboard memory all at once. (Scaling to "$1$ million" images, as the slide's other annotation suggests, would require roughly $10\times$ that — around $1$TB.)

**This is precisely why mini-batching exists as a practical necessity, not just an optimization choice**: computing a gradient over the *entire* dataset (Batch Gradient Descent) would require loading all $100$GB+ into memory simultaneously — often simply impossible. Splitting the data into small mini-batches (worked through numerically in [[04_MiniBatching_a_Large_Dataset_Worked_Example]]) means only one small chunk needs to be in memory at any given time, which is exactly the "**No out of memory error**" benefit named directly on the next slide.

---

## 2) Simple English Explanation

**The pseudocode, in plain terms**: gradient descent's actual update step, no matter which variant you're using, always boils down to the same three ingredients: your current parameters, the gradient (which way is uphill, computed however you chose to compute it), and a learning rate (step size). The update is always: new parameters = old parameters − (step size × gradient). The slide's handwritten notes point out that fancier algorithms like Momentum, RMSprop, and Adam (all covered back in Lecture 0) are usually run *combined with* mini-batching in practice, not with single examples or the whole dataset at once.

**Why can't we just always use the whole dataset (Batch Gradient Descent)? A real numbers check**: the slide hints at a memory problem, with some numbers scribbled alongside — and working through them confirms a genuinely important point. Imagine $100{,}000$ images, each a modest $1000\times1000$ pixels, with just 1 byte needed per pixel:

$$100{,}000 \text{ images} \times 1{,}000{,}000 \text{ pixels each} = 100{,}000{,}000{,}000 \text{ bytes} = 100\text{ GB}$$

That's already **100 gigabytes** — likely more than fits comfortably in a computer's RAM or a graphics card's memory all at once, for a dataset that isn't even especially huge by real-world standards (a million images, as the slide's notes also suggest, would need roughly ten times that, around a terabyte). This isn't a made-up number — it exactly matches what the slide's own handwriting says.

**The takeaway**: this is exactly why mini-batching isn't just a nice speed trick — for realistically-sized datasets, trying to load *everything* into memory at once (what Batch Gradient Descent requires) genuinely doesn't fit. Splitting the data into small mini-batches, so only one small chunk needs to be loaded at a time, is often the only practical way to train at all — which is precisely the point the next topic works through with real numbers.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Pseudocode, simple shabdon mein**: gradient descent ka actual update step, chahe tum jo bhi variant use karo, hamesha same teen ingredients tak simplify ho jaata hai: tumhare current parameters, gradient (kis taraf upar hai, jaise bhi tumne compute kiya), aur ek learning rate (step size). Update hamesha ye hai: naye parameters = purane parameters − (step size × gradient). Slide ke handwritten notes point out karte hai ki fancier algorithms jaise Momentum, RMSprop, aur Adam (sab Lecture 0 mein cover kiye) practice mein usually mini-batching ke saath combined chalaye jaate hai, single examples ya poore dataset ke saath ek saath nahi.

**Hum hamesha poora dataset (Batch Gradient Descent) kyun use nahi kar sakte? Ek real numbers check**: slide ek memory problem ki taraf hint karti hai, saath mein kuch numbers scribble kiye hue — aur unhe work through karna ek genuinely important point confirm karta hai. Socho $100{,}000$ images, har ek modest $1000\times1000$ pixels ki, bas 1 byte per pixel chahiye:

$$100{,}000 \text{ images} \times 1{,}000{,}000 \text{ pixels har ek} = 100{,}000{,}000{,}000 \text{ bytes} = 100\text{ GB}$$

Ye already **100 gigabytes** hai — likely ek computer ke RAM ya graphics card ki memory mein ek saath comfortably fit hone se zyada, ek dataset ke liye jo real-world standards ke hisaab se especially huge bhi nahi hai (ek million images, jaise slide ke notes bhi suggest karte hai, usse roughly das guna chahiye hoga, lagbhag ek terabyte). Ye koi banaya hua number nahi hai — ye exactly wahi match karta hai jo slide ki apni handwriting kehti hai.

**Takeaway**: yahi exact wajah hai ki mini-batching sirf ek achhi speed trick nahi hai — realistically-sized datasets ke liye, *sab kuch* ek saath memory mein load karne ki koshish karna (jo Batch Gradient Descent ko chahiye) genuinely fit nahi hota. Data ko chhote mini-batches mein split karna, taaki ek time pe sirf ek chhota chunk load karna pade, aksar train karne ka sirf practical tarika hai — yahi exact point hai jo agla topic real numbers ke saath work through karta hai.
