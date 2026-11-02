# Topic 1: Course Overview — Syllabus, Evaluation Scheme and Books

Source: Lecture 1, slides 1–5 (Title, Google Classroom, Course schema, Books ×2).

---

## 1) Technical Explanation

**Course identity.** ES532: Introduction to Deep Learning, taught by Dr. Yashwant Singh Patel, Department of Engineering Sciences, ABV-IIITM Gwalior. Credits: **3 (L-T-P: 2-0-2)** — i.e. 2 lecture hours, 0 tutorial hours and 2 practical (lab) hours per week.

**Syllabus (slide 3)** is in two blocks:

1. *Neural-network foundations* — History of Deep Learning, Deep Learning success stories, McCulloch–Pitts neuron, thresholding logic, Perceptron, Perceptron Learning Algorithm, Multilayer Perceptrons (MLPs) and their representation power, Sigmoid neurons, Feedforward Neural Networks and their representation power, Gradient Descent (GD), Momentum-based GD, Nesterov Accelerated GD, Stochastic GD, AdaGrad, RMSProp, Adam, and the linear-algebra background (eigenvalues/eigenvectors, eigenvalue decomposition, basis).
2. *Hardware / parallel programming* — GPU architecture, clock speeds, CPU/GPU comparison, heterogeneity, accelerators, parallel programming, CUDA / OpenCL / OpenACC, kernel launch parameters, thread hierarchy (warps/wavefronts, thread-blocks/workgroups, streaming multiprocessors), 1D/2D/3D thread mapping, device properties, the memory hierarchy (global/DRAM, local/shared, private, textures, constant memory), pointers, dynamic memory, multi-dimensional arrays, memory copy across devices, matrix programs and performance evaluation with different memories.

**Evaluation scheme (slide 3):** Minor exam 25% · Quizzes/Presentation/Class participation 15% · Major exam 40% · Lab evaluation 20% (total 100%).

**Books (slides 4–5).** Core: Goodfellow–Bengio–Courville *Deep Learning* (MIT Press, 2016); Friedman–Tibshirani–Hastie *The Elements of Statistical Learning*; Aggarwal *Neural Networks and Deep Learning*; Zhang–Lipton–Li–Smola *Dive into Deep Learning*; Drori *The Science of Deep Learning*; Haykin *Neural Networks and Learning Machines*; Sutton–Barto *Reinforcement Learning: An Introduction*; Bishop & Bishop *Deep Learning: Foundations and Concepts*. Slide 5 adds two more: Shane Cook *CUDA Programming: A Developer's Guide to Parallel Computing with GPUs* and Duda–Hart–Stork *Pattern Classification*.

**Where this repo stands on the syllabus:** the notes for the gradient-descent family (GD, Momentum, RMSProp, Adam…) already exist in [[01_What_Is_Gradient_Descent_and_the_Learning_Rate]] from Lecture 0 (Ruder's paper) and Lectures 10–12; the sigmoid neuron is in Lecture 8 and feedforward networks in Lecture 9. The CPU/GPU part is covered by Lecture 13.

**Note on slides 4 and 5:** slide 4 is simply an earlier version of slide 5 (same list minus the last two books); nothing is lost by merging them.

---

## 2) Simple English Explanation

This first slide-set is the "welcome and rules" part of the course.

- The course is worth 3 credits: 2 hours of classroom theory and 2 hours of lab work every week.
- The syllabus has two big halves. The first half teaches how artificial "neurons" and networks of them work and how they *learn* (the maths of gradient descent and its improved versions). The second half teaches how to run these heavy computations fast on a **GPU** (the graphics chip), because deep learning needs a huge amount of arithmetic.
- Marks: 25% minor exam, 40% major exam, 20% lab, 15% quizzes/presentations/participation.
- The slides list many reference books. The most famous one is the "Deep Learning" book by Goodfellow, Bengio and Courville — many later slides take their pictures from it.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye pehla slide-set course ka "welcome aur rules" wala hissa hai.

- Course 3 credits ka hai: har hafte 2 ghante theory aur 2 ghante lab.
- Syllabus ke do bade hisse hain. Pehle hisse mein sikhte hain ki artificial neuron aur unka network kaise kaam karta hai aur wo *seekhta* kaise hai (gradient descent aur uske improved versions ka maths). Dusre hisse mein sikhte hain ki ye bhaari computation **GPU** (graphics chip) par tez kaise chalaye, kyunki deep learning mein bahut zyada arithmetic hota hai.
- Marks: 25% minor exam, 40% major exam, 20% lab, aur 15% quizzes/presentation/class participation.
- Slides mein kaafi reference books di hain. Sabse famous Goodfellow, Bengio aur Courville ki "Deep Learning" book hai — aage ki bahut si slides ki pictures usi book se li gayi hain.
