# Topic 5: Advantages and Disadvantages of Each Activation Function

Source: Lecture 8 (ES532: Introduction to Deep Learning), slides 25–26 (cited to https://christianmaxmike.github.io/mindnotes/ai_dl_activationFunctions.pdf). Enriched with web research on the vanishing gradient problem's origin and ReLU's history.

---

## 1) Technical Explanation

Having seen *what* the common activation functions are ([[04_Other_Activation_Functions_Tanh_ReLU_Leaky_ReLU_ELU]]), this topic covers *why* each one is or isn't a good practical choice.

**Linear** — Advantage: outputs are real-valued, no artificial binary squashing. Disadvantage: it's a straight line, so **no non-linearity can be learned** — the derivative is a constant (always 1), completely unrelated to the input $x$, so backpropagation's weight updates end up constant too. Stacking multiple linear layers collapses mathematically into a single linear layer, so a network built only from linear activations can never learn anything beyond what one linear function already could — a genuinely important limitation covered in more depth once this course reaches multi-layer networks.

**Sigmoid** — Advantages: smooth gradient (no abrupt "jumps" in the output — the exact fix from [[02_The_Sigmoid_Logistic_Function]]), output confined to $[0,1]$ so it naturally normalizes a neuron's output, and it gives clear, confident-looking predictions (very low/high values sit very close to 0/1). Disadvantages:
- **Vanishing gradient**: for very high or very low inputs, the sigmoid curve is almost completely **flat** (this is called "saturation") — so its derivative there is almost exactly zero. Since training relies on multiplying these derivatives together across layers during backpropagation, a near-zero derivative anywhere in that chain causes the useful training signal to shrink toward nothing, meaning the network barely learns anything from that point onward, or in the worst case, learns nothing at all.
- **Not zero-centered**: sigmoid's output is always positive (strictly between 0 and 1), never negative — this turns out to make optimization somewhat harder in practice (it biases the direction gradients can push weights, described in more detail once this course covers gradient-based training of multi-layer networks in depth).
- Computationally more expensive than simpler alternatives, since it requires evaluating an exponential ($e^{-x}$) at every neuron, every forward pass.

**Tanh** — Advantage: **zero-centered** (unlike sigmoid) — since its output ranges over $(-1,1)$, both strongly negative, neutral, and strongly positive input signals can all be represented naturally, without the "always positive" bias sigmoid has. Disadvantage: still suffers from the **same vanishing gradient problem** as sigmoid — it also saturates (flattens out) for very large or very small inputs, killing the gradient there just like sigmoid does.

**ReLU (Rectified Linear Unit)** — Advantages: training **converges much faster** than with sigmoid/tanh-based networks (web research: ReLU is a single comparison against zero, with no exponential to compute, so it's cheap per-neuron; empirically, networks using it have been observed to train around several times faster in terms of epochs needed, compared to sigmoid/tanh), computationally efficient, and — crucially — it **avoids the vanishing gradient problem** for positive inputs, since its derivative there is a constant 1 (not shrinking toward zero the way sigmoid/tanh's do when they saturate). Disadvantage: the **"Dying ReLU" problem** — because ReLU's derivative is exactly 0 for any negative input, if a neuron's weighted sum ends up negative during training, that neuron's gradient becomes zero, backpropagation can no longer adjust its incoming weights at all, and the neuron effectively "dies" — permanently stuck outputting 0 regardless of the input, contributing nothing further to the network. ReLU's range is $[0,\infty)$, and — like sigmoid — its output is not zero-centered either (it's always $\geq 0$).

**Leaky ReLU** — Advantages: same fast convergence and computational efficiency as ReLU, but specifically **prevents the Dying ReLU problem** — by letting a small positive slope (e.g. $\alpha = 0.01$) through even for negative inputs, a neuron's gradient is never exactly zero, so it can never fully die and always retains some ability to keep learning. Disadvantage: results can be **inconsistent**, since the extra hyperparameter $\alpha$ (which controls how much signal "leaks" through on the negative side) has to be chosen, and different values can noticeably change training behavior.

**Historical/research context beyond the slide (via web research)**:
- The **vanishing gradient problem** was first identified and named by **Sepp Hochreiter** in his 1991 diploma thesis. It was, for a long time, widely believed to make training genuinely deep networks via backpropagation essentially impossible — because as error signals get backpropagated through many layers, they get multiplied by each layer's activation derivative, and if those derivatives are consistently small (as with saturated sigmoid/tanh neurons), the signal shrinks exponentially with depth and the earliest layers barely update at all. This problem — and the search for ways around it — is one of the central threads running through the history of deep learning, and it's exactly why ReLU-family activations (which don't saturate for positive inputs) became so dominant once deeper networks started being trained routinely.
- **ReLU** itself was proposed by **Nair and Hinton in 2010**, and has since become the most widely used activation function for deep learning, precisely because of the speed and vanishing-gradient advantages described above.

---

## 2) Simple English Explanation

Now that you've seen the shapes of these activation functions, here's the practical question: which one should you actually pick, and what goes wrong with each?

**Linear** — Sounds simple and safe, but it's actually a trap for deep networks: stacking several linear layers together is mathematically no different from just having *one* linear layer. So a network built entirely of "just pass the number through" layers can never learn anything more complicated than what a single straight-line equation could already do — no matter how many layers you add.

**Sigmoid** — Gives nice, confident-looking 0-to-1 outputs, and its smoothness fixes the perceptron's harsh jump problem. But it has two real downsides: (1) at the extreme ends of its curve, it goes almost completely flat — imagine trying to walk uphill on ground that's *basically* level; you get almost no useful signal about which way to go, and a network's earlier layers can barely learn anything as a result (this is called the "vanishing gradient" problem, and it's a genuinely famous, historically important issue in deep learning); and (2) sigmoid's output is always positive, never negative, which subtly makes the whole training process a bit less efficient than it could be.

**Tanh** — Basically sigmoid's cousin, with one nice improvement: its output can be negative too (it's "zero-centered"), which helps with that inefficiency sigmoid has. But it still goes flat at the extremes just like sigmoid does, so it still suffers from the same vanishing-gradient problem.

**ReLU** — The current default choice for most deep networks, and for good reason: it's extremely cheap to compute (just "is this positive? if so keep it, if not, zero it out" — no fancy math involved), and for positive inputs it never goes flat, so it dodges the vanishing-gradient problem entirely on that side. But it has its own quirk: if a neuron's input keeps landing on the negative side during training, that neuron gets stuck outputting exactly 0 forever, contributing nothing to the network from then on — a "dead" neuron. This is called the "Dying ReLU" problem.

**Leaky ReLU** — A small patch on ReLU: instead of completely zeroing out negative inputs, it lets a tiny trickle through, so a neuron can never fully "die" — there's always at least a little signal left to keep learning from. The trade-off: you now have one more knob to tune (how much to let leak through), and getting that knob wrong can make training a bit inconsistent.

**A bit of real history worth knowing**: the "vanishing gradient" problem — where a network's earliest layers barely learn anything because the useful signal shrinks to nothing as it passes backward through many saturating (sigmoid/tanh-like) layers — was first identified way back in **1991**, by a researcher named Sepp Hochreiter. For a long stretch of AI history, this problem made people genuinely doubt whether truly deep networks could ever be trained at all. ReLU, introduced by Nair and Hinton in **2010**, was one of the key breakthroughs that helped get around this, which is a big part of why it's the default choice in most modern deep networks today.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ab jab tumne in activation functions ke shapes dekh liye, practical sawaal ye hai: kaunsa actually choose karna chahiye, aur har ek mein kya problem hai?

**Linear** — Simple aur safe lagta hai, lekin ye deep networks ke liye actually ek trap hai: kayi linear layers ko stack karna mathematically bilkul same hai jaise sirf *ek* linear layer ho. To sirf "number ko bina badle pass karo" wale layers se bana network kabhi bhi kisi single straight-line equation se zyada complicated kuch seekh hi nahi sakta — chahe tum kitne bhi layers add kar lo.

**Sigmoid** — Achhe, confident-looking 0-se-1 outputs deta hai, aur uski smoothness perceptron ki harsh jump problem fix karti hai. Lekin iske do real downsides hai: (1) uske curve ke extreme ends par, ye lagbhag pura flat ho jaata hai — socho upar ki taraf chalne ki koshish karna aisi zameen par jo *lagbhag* level hai; tumhe kis taraf jaana hai iska almost koi useful signal nahi milta, aur network ki earlier layers is wajah se lagbhag kuch seekh hi nahi pati (ise "vanishing gradient" problem kehte hai, aur ye deep learning ka ek genuinely famous, historically important issue hai); aur (2) sigmoid ka output hamesha positive hota hai, kabhi negative nahi, jo subtly poori training process ko thoda kam efficient bana deta hai.

**Tanh** — Basically sigmoid ka cousin hai, ek achhe improvement ke saath: iska output negative bhi ho sakta hai ("zero-centered" hai), jo sigmoid wali inefficiency mein help karta hai. Lekin ye bhi extremes par flat ho jaata hai bilkul sigmoid jaisa, isliye isme bhi wahi vanishing-gradient problem hoti hai.

**ReLU** — Zyadatar deep networks ke liye current default choice hai, aur achhi wajah se: ye compute karna extremely cheap hai (bas "kya ye positive hai? agar haan to rakho, agar nahi to zero kar do" — koi fancy math involved nahi), aur positive inputs ke liye ye kabhi flat nahi hota, isliye us side par vanishing-gradient problem ko poori tarah dodge kar leta hai. Lekin iski apni ek quirk hai: agar training ke dauran kisi neuron ka input baar-baar negative side pe land ho, to wo neuron forever exactly 0 output karte hue stuck ho jaata hai, tab se aage network mein kuch contribute nahi karta — ek "dead" neuron. Ise "Dying ReLU" problem kehte hai.

**Leaky ReLU** — ReLU par ek chhota patch: negative inputs ko poori tarah zero karne ke bajaye, ye ek chhota trickle pass hone deta hai, isliye koi neuron kabhi poori tarah "die" nahi ho sakta — hamesha kam se kam thoda sa signal bacha rehta hai seekhne ke liye. Trade-off: ab tumhare paas tune karne ke liye ek aur knob hai (kitna leak hone dena hai), aur us knob ko galat set karna training ko thoda inconsistent bana sakta hai.

**Thodi real history jaanna zaroori hai**: "vanishing gradient" problem — jahan network ki earliest layers lagbhag kuch seekh hi nahi pati kyunki useful signal kayi saturating (sigmoid/tanh jaisi) layers se backward pass hote hue lagbhag zero ho jaata hai — sabse pehle **1991** mein identify hui thi, ek researcher Sepp Hochreiter dwara. AI history ke ek lambe stretch tak, is problem ne logon ko genuinely doubt karaya ki kya truly deep networks kabhi train ho bhi sakti hai. ReLU, jo Nair aur Hinton ne **2010** mein introduce kiya, us cheez ko solve karne wale key breakthroughs mein se ek tha, jo ek badi wajah hai ki ye aaj bhi zyadatar modern deep networks mein default choice hai.
