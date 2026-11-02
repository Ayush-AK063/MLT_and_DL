# Topic 4: Formalizing the Learning Problem — Data, Model, Parameters, Algorithm, Loss

Source: Lecture 9 (ES532: Introduction to Deep Learning), slides 14–15 (numbered 17 and 19 in the printed slide corner). Enriched with web research on the universal approximation theorem, tying back to Lecture 8's "arbitrary functions" motivation.

---

## 1) Technical Explanation

Having built up the layer-by-layer machinery in [[01_Feedforward_Network_Architecture_Layers_and_Notation]] through [[03_Output_Layer_and_Full_Network_Function]], this topic assembles everything into the standard five-part framing used to describe *any* supervised machine learning problem — Data, Model, Parameters, Algorithm, and Objective/Loss.

**Data**: a set of $N$ labeled examples, $\{x_i, y_i\}_{i=1}^{N}$ — each $x_i$ an input vector, each $y_i$ its corresponding true/target output.

**Model**: the network's prediction for a given input, written out as the **full composition of every layer's function**, for the specific case of a 3-layer network ($L=3$, i.e. 2 hidden layers plus one output layer):

$$\hat{y}_i = f(x_i) = O\Big(W_3\, g\big(W_2\, g(W_1 x_i + b_1) + b_2\big) + b_3\Big)$$

Reading this from the inside out (which is also the order the actual forward computation happens in): $W_1 x_i + b_1$ is layer 1's pre-activation; $g(\cdot)$ turns it into layer 1's activation $h_1$; $W_2 h_1 + b_2$ is layer 2's pre-activation; $g(\cdot)$ again turns it into $h_2$; $W_3 h_2 + b_3$ is the output layer's pre-activation $a_3$; and finally $O(\cdot)$ turns that into the network's actual prediction $\hat{y}_i$. This single nested formula is exactly the layer-by-layer process from [[02_PreActivation_and_Activation_Equations]], just written as one expression instead of step by step.

**Parameters**: the full set of numbers the network actually needs to *learn* — collectively denoted $\theta$:

$$\theta = W_1, \dots, W_L,\ b_1, \dots, b_L \quad (L=3 \text{ in this example})$$

These are precisely the unknowns the slide poses as open questions right before this framing: "$W_i = ?$", "$h_i = ?$" (note: $h_i$ is *computed* from $\theta$ and $x$, not itself directly learned — it's the weights and biases that are the actual learnable parameters), "$b_i = ?$".

**Algorithm**: **Gradient Descent with Backpropagation** — named explicitly here as the method this course will use to actually find good values for $\theta$ (backpropagation itself — the algorithm for efficiently computing the gradients needed by gradient descent, layer by layer, through a network like this — is a separate, deeper topic for a later lecture not yet in this repo; gradient descent itself, the general optimization method, is already covered in this repo's Lecture 0, e.g. [[01_What_Is_Gradient_Descent_and_the_Learning_Rate]]).

**Objective/Loss/Error function**: a concrete example is given — squared error, averaged over all $N$ data points and all $k$ output dimensions:

$$\min_\theta \ \frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{k} (\hat{y}_{ij} - y_{ij})^2$$

and stated in general form as $\min_\theta \mathcal{L}(\theta)$, where $\mathcal{L}(\theta)$ is "some function of the parameters" — i.e., the specific squared-error formula above is just *one* possible choice of loss function, not the only one.

**An important distinction the slide's own annotation draws, worth stating explicitly**: a **loss function** technically refers to the error for a **single data point**; the **aggregate** of that loss over an entire dataset (summed or averaged across all $N$ points, as in the formula above) is more precisely called the **cost function**. In casual usage (including elsewhere in these notes and in most of the field), "loss" and "cost" are often used interchangeably, but the slide flags the precise distinction, so it's worth knowing.

**Tying this back to Lecture 8's motivating question (via web research)**: Lecture 8 opened by asking whether a network could **approximately represent arbitrary functions** $y=f(x)$ (see [[00_Recap_From_Boolean_to_Arbitrary_Functions]] from Lecture 8). The composed function shown here — layers of weighted sums and biases, each passed through a non-linear activation $g$, stacked $L$ times — is exactly the mathematical object that answers that question. This is formalized by the **Universal Approximation Theorem**: Cybenko (1989) proved it specifically for sigmoid-type activations, and Hornik, Stinchcombe, and White (1989) proved a more general version for a broad class of bounded, non-constant, continuous activation functions (with related independent results the same year by Funahashi). The theorem states, roughly, that a feedforward network with even just **one** sufficiently wide hidden layer can approximate any continuous function on a bounded domain to arbitrary accuracy. This doesn't say *how* to find the right weights (that's what gradient descent and backpropagation are for) — but it's the theoretical justification for why building networks out of exactly this kind of layered, non-linearly-activated structure is a reasonable strategy for the "arbitrary function" problem posed back in Lecture 8.

---

## 2) Simple English Explanation

This topic pulls together everything from earlier in this lecture into the standard five-question checklist used to describe any machine-learning problem:

**1. Data — what examples do we have to learn from?** A collection of $N$ input-answer pairs: here's an input, here's what the correct answer should have been, repeated $N$ times.

**2. Model — what's our guess-making machine?** This is literally just the whole feedforward network from the earlier topics, written out as one big nested formula: take the input, run it through layer 1's weighted-sum-plus-squash, feed that into layer 2's weighted-sum-plus-squash, and so on, ending with the special output-layer squash — and whatever pops out the other end is the model's prediction.

**3. Parameters — what exactly are we trying to learn/tune?** All the weights and biases in every layer, collectively. These are the actual "dials" the training process adjusts. (Note: the in-between values like $h_i$ aren't dials you tune directly — they're just calculated results, along the way, from the real dials, the weights and biases.)

**4. Algorithm — how do we tune those dials?** Gradient descent (from earlier in this repo) combined with a technique called backpropagation, which is specifically how you efficiently figure out gradients for a multi-layer network like this — backpropagation itself is a topic for a future lecture.

**5. Loss/Objective — how do we measure "how wrong" we currently are?** One common way: for each output number, measure how far off it is from the correct answer, square that difference (so it's always positive and big misses count extra), and average that over every output and every training example. The training goal is simply to find the parameter values that make this "wrongness" number as small as possible.

**A small but useful vocabulary distinction**: technically, "loss" means the wrongness for just *one* example, while "cost" means the wrongness averaged/summed across the *whole* dataset. People often use the words loosely and interchangeably, but it's good to know the precise difference exists.

**Why this all connects back to the very first question this course asked**: back in Lecture 8, the course asked whether a network could represent basically *any* arbitrary function, not just simple yes/no ones. It turns out mathematicians proved, decades ago (Cybenko in 1989, and Hornik/Stinchcombe/White the same year), that a network built exactly like this — layers of weighted combinations, each squashed through a non-linear function like sigmoid — really can approximate essentially any reasonable function, given enough neurons. That famous result is called the **Universal Approximation Theorem**, and it's the theoretical reason this whole layered structure is worth building in the first place. It doesn't tell you *how* to actually find the right weights — that's the job of the training algorithm — but it guarantees that the right weights, in principle, exist to solve whatever the arbitrary-function problem happens to be.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye topic is lecture mein pehle se aayi sab cheezon ko ek standard five-question checklist mein pull together karta hai, jo kisi bhi machine-learning problem ko describe karne ke liye use hoti hai:

**1. Data — hamare paas seekhne ke liye kaunse examples hai?** $N$ input-answer pairs ka ek collection: ye raha input, ye sahi answer hona chahiye tha, ise $N$ baar repeat karo.

**2. Model — hamari guess-making machine kya hai?** Ye literally poora feedforward network hai jo pichle topics se aaya, ek bade nested formula ki tarah likha hua: input lo, use layer 1 ke weighted-sum-plus-squash se guzaro, us result ko layer 2 ke weighted-sum-plus-squash mein feed karo, waghera, aakhir mein special output-layer squash ke saath end karte hue — aur doosri taraf se jo bhi nikle wahi model ki prediction hai.

**3. Parameters — hum exactly kya seekhne/tune karne ki koshish kar rahe hai?** Har layer ke saare weights aur biases, collectively. Yahi actual "dials" hai jo training process adjust karta hai. (Note: beech ke values jaise $h_i$ direct tune karne wale dials nahi hai — wo bas calculated results hai, raaste mein, real dials, matlab weights aur biases, se.)

**4. Algorithm — hum un dials ko kaise tune karte hai?** Gradient descent (is repo mein pehle padha) combined with ek technique jise backpropagation kehte hai, jo specifically ye batati hai ki is tarah ke multi-layer network ke liye gradients efficiently kaise figure out karein — backpropagation khud ek future lecture ka topic hai.

**5. Loss/Objective — hum "kitne galat hai" ye kaise measure karte hai?** Ek common tarika: har output number ke liye, ye measure karo ki wo sahi answer se kitna door hai, us difference ko square karo (taaki ye hamesha positive rahe aur badi galtiyan zyada count ho), aur ise har output aur har training example ke upar average karo. Training ka goal bas ye parameter values dhoondhna hai jo is "wrongness" number ko jitna ho sake chhota karein.

**Ek chhoti lekin useful vocabulary distinction**: technically, "loss" ka matlab hai sirf *ek* example ki wrongness, jabki "cost" ka matlab hai poore dataset mein average/sum ki hui wrongness. Log aksar ye words loosely aur interchangeably use karte hai, lekin jaanna achha hai ki precise farak exist karta hai.

**Ye sab is course ke bilkul pehle sawaal se kaise connect hota hai**: Lecture 8 mein, course ne puchha tha ki kya ek network basically *kisi bhi* arbitrary function ko represent kar sakta hai, sirf simple yes/no wale nahi. Ye nikla ki mathematicians ne dashko pehle prove kar diya tha (Cybenko ne 1989 mein, aur Hornik/Stinchcombe/White ne usi saal), ki ek network jo bilkul isi tarah bana ho — weighted combinations ki layers, har ek ko ek non-linear function jaise sigmoid se squash kiya hua — genuinely lagbhag kisi bhi reasonable function ko approximate kar sakta hai, agar enough neurons hon. Us famous result ko **Universal Approximation Theorem** kehte hai, aur yahi theoretical wajah hai ki ye poora layered structure banana worth hai. Ye ye nahi batata ki sahi weights actually kaise dhoondhe — wo training algorithm ka kaam hai — lekin ye guarantee karta hai ki sahi weights, principle mein, exist karte hai jo bhi arbitrary-function problem ho use solve karne ke liye.
