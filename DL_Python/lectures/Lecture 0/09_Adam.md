# Topic 9: Adam (Adaptive Moment Estimation)

Source: Lecture 0, Section 4.6 (Adam) of Ruder's overview paper. Enriched with web research on Adam's later refinement, AdamW.

---

## 1) Technical Explanation

**Adam** (Adaptive Moment Estimation; Kingma and Ba, 2015) is another method that computes an adaptive learning rate for each parameter. Where [[08_RMSprop]] and [[07_Adadelta]] only track a decaying average of past **squared** gradients ($v_t$ — an estimate of the gradient's **second moment**, i.e. its uncentered variance), Adam *additionally* tracks a decaying average of past (non-squared) gradients ($m_t$ — an estimate of the gradient's **first moment**, i.e. its mean), similar in spirit to [[04_Momentum]]:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$

Since $m_t$ and $v_t$ both start out initialized as vectors of zeros, they are **biased toward zero**, especially during the early time steps and especially when the decay rates $\beta_1, \beta_2$ are close to 1 (which is the typical, recommended setting). The authors correct for this with **bias-corrected** estimates:

$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1-\beta_2^t}$$

(Intuition for why this works: at $t=1$, $m_1 = (1-\beta_1)g_1$, which badly underestimates the true gradient — dividing by $1-\beta_1^1 = 1-\beta_1$ exactly cancels that shrinkage. As $t$ grows large, $\beta_1^t \to 0$, so $1-\beta_1^t \to 1$ and the correction fades away naturally, becoming negligible once the running averages are well-established.)

These bias-corrected estimates are then combined into the final **Adam update rule**:

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon}\, \hat{m}_t$$

**Recommended defaults** (from the original paper): $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. The paper reports that Adam works well empirically and compares favorably to other adaptive methods.

**Later developments beyond this 2016 paper (via web research)**: Adam became — and remains, as of 2026 — arguably the single most widely used default optimizer in deep learning, especially for training large models like transformers. However, a well-known follow-up refinement, **AdamW** (Loshchilov and Hutter, 2019), fixed a subtle bug in how the original Adam interacts with **weight decay** (a common regularization technique). In standard Adam, L2 weight decay gets folded directly into the gradient before it's divided by $\sqrt{\hat{v}_t}$ — which means parameters with historically large gradient variance end up getting *less* effective regularization than parameters with small variance, purely as an accidental side-effect of the adaptive learning-rate mechanism, not because that's actually desirable. AdamW **decouples** weight decay from the adaptive gradient update, applying it directly and uniformly to the weights instead. This turned out to noticeably improve generalization, and AdamW (not the original Adam) is now the more commonly recommended default in most modern deep learning frameworks, especially for fine-tuning large models.

---

## 2) Simple English Explanation

Adam combines the best ideas from the two previous topics into one optimizer:

- Like **RMSprop/Adadelta**, it tracks a fading memory of *how big* each dial's recent gradients have been squared, to automatically shrink the effective step for dials that have been getting large, noisy pushes.
- Like **Momentum**, it *also* tracks a fading memory of the *direction* each dial's gradient has recently been pointing, so it builds up speed in a consistent direction — same "heavy ball" idea as before.

Combining "how big" (from RMSprop-style tracking) with "which direction, building up speed" (from Momentum-style tracking) is where the name comes from: **Ada**ptive **M**oment estimation — it's tracking two different statistical "moments" (mean and variance-like quantities) of the gradient at once.

There's one more clever fix baked in: right at the very start of training, both of these running averages start at zero, which means they're artificially too small for the first several steps (like a new employee's "average performance so far" being unfairly skewed toward zero just because there's only one data point). Adam applies a mathematical correction specifically for these early steps, which naturally fades away and stops mattering once training has been running for a while.

Adam turned out to work extremely well in practice and is, as of 2026, probably the single most commonly used default optimizer across deep learning — especially for large models. A later refinement called **AdamW** fixed a subtle interaction between Adam and a common regularization trick (weight decay), and AdamW is now generally the recommended version to reach for instead of the original Adam, especially for fine-tuning big models like transformers.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Adam pichhle do topics ke best ideas ko combine karta hai ek optimizer mein:

- **RMSprop/Adadelta** ki tarah, ye ek fading memory rakhta hai ki har dial ke recent gradients *kitne bade* (squared) rahe hai, taaki jin dials ko bade, noisy pushes mil rahe hai unka effective step automatically chhota ho jaaye.
- **Momentum** ki tarah, ye *bhi* ek fading memory rakhta hai ki har dial ka gradient recently *kis direction* mein point kar raha tha, taaki wo ek consistent direction mein speed pakad sake — wahi "heavy ball" wala idea phir se.

"Kitna bada" (RMSprop-style tracking se) aur "kis direction, speed pakadte hue" (Momentum-style tracking se) ko combine karna hi naam ka source hai: **Ada**ptive **M**oment estimation — ye ek saath gradient ke do alag statistical "moments" (mean aur variance jaisi cheezein) track karta hai.

Ek aur clever fix bhi hai: training ke bilkul shuruaat mein, dono running averages zero se start hote hai, jiska matlab hai ki pehle kuch steps ke liye ye artificially bahut chhote hote hai (jaise kisi nayi employee ki "average performance so far" unfairly zero ki taraf skewed ho, bas isliye kyunki abhi sirf ek data point hai). Adam in early steps ke liye specifically ek mathematical correction lagata hai, jo naturally fade ho jaata hai jaise-jaise training aage badhti hai.

Adam practice mein bahut achha kaam karta nikla, aur 2026 tak, ye shaayad deep learning mein sabse commonly use hone wala default optimizer hai — khaaskar bade models ke liye. Ek baad wala refinement, **AdamW**, ne Adam aur ek common regularization trick (weight decay) ke beech ka ek subtle interaction fix kiya, aur AdamW ab generally recommended version hai original Adam ki jagah, khaaskar transformers jaise bade models ko fine-tune karne ke liye.
