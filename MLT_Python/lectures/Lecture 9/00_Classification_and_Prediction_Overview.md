# Topic 0: Classification and Prediction — Overview

Source: Lecture 9, slide 1 (Classification and Prediction).

---

## 1) Technical Explanation

Lecture 9 opens a new unit of the course: **Classification and Prediction**, two closely related but distinct forms of supervised data analysis used to build models that describe important data classes or forecast future data trends.

**Definitions given on the slide**:
- **Classification** predicts a **categorical (discrete, unordered) label** — i.e., it assigns a data point to one of a fixed, finite set of classes that have no inherent order (e.g., "spam" vs "not spam", "buys_computer = yes/no"). This is a form of **supervised learning**, distinguishing it from the unsupervised paradigms covered earlier ([[08_ML_Paradigms_Unsupervised_Learning]] from Lecture 3).
- **Prediction** models **continuous-valued functions** — i.e., it estimates a numeric quantity (e.g., a price, a temperature, a probability of failure) rather than assigning a category. In modern ML terminology this is what is usually called **regression**; the slide's use of "prediction" here is the older, classical data-mining term (this course follows the terminology of the classic Data Mining textbook tradition, e.g. Han & Kamber's *Data Mining: Concepts and Techniques*, which is also the source of the worked decision-tree example later in this lecture — see [[06_Decision_Tree_Classification_and_Induction]]).

**Named methods** (the slide lists these as families of algorithms the course will study across this and following lectures):
- **Classifiers**: decision tree classifiers, Bayesian classifiers, Bayesian belief networks, rule-based classifiers, the neural network technique (i.e., using a neural net as a classifier — connects back to [[05_Introduction_to_Neural_Networks]] from Lecture 1 and the perceptron work in Lectures 4–5), k-nearest-neighbor classifiers, and support vector machines (SVMs).
- **Prediction methods**: linear regression, nonlinear regression, and the neural network technique (a neural net can also be used for regression, not just classification).

**Applications** listed: fraud detection, target marketing, performance prediction, manufacturing, and medical diagnosis — all real-world domains where either "which category does this belong to" (classification) or "what will this numeric value be" (prediction) is the business question.

**Why this distinction matters going forward**: every algorithm named above will, in later lectures, be evaluated by *how well it separates categories* (for classifiers, e.g., accuracy, precision/recall) or *how close its numeric output is to the true value* (for predictors, e.g., mean squared error). Keeping "categorical output → classification" and "numeric output → prediction/regression" separate in your head is the single most important mental model for this whole unit.

---

## 2) Simple English Explanation

This lecture starts a brand-new topic: **Classification and Prediction**. Both are ways of using past data to make guesses about new data — but they answer different *kinds* of questions.

- **Classification** answers "**which category**?" — like "Is this email spam or not?" or "Will this customer buy a computer, yes or no?" The answer is always one of a small, fixed list of labels, and there's no natural order between them (spam isn't "bigger" or "smaller" than not-spam).
- **Prediction** answers "**how much / what value**?" — like "What will this house sell for?" or "What temperature will it be tomorrow?" The answer is a number that can be anything on a continuous scale.

Think of it like this: if the answer is a **name/category**, it's classification. If the answer is a **number**, it's prediction (today this is usually called "regression").

Many different algorithms exist for each job — decision trees, "Bayesian" methods (based on probability), rule-based systems, neural networks, k-nearest-neighbor, and support vector machines can all do classification; linear/nonlinear regression and neural networks can do prediction.

Real-life uses: catching credit card fraud, deciding who to target with an ad campaign, predicting how well a machine or employee will perform, spotting defects in manufacturing, and diagnosing diseases.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Is lecture se ek naya topic start ho raha hai: **Classification and Prediction**. Dono hi purane data ka use karke naye data ke baare mein guess lagane ke tarike hai — lekin dono alag tarah ke sawaalon ka jawab dete hai.

- **Classification** ka jawab hota hai "**kaunsi category**?" — jaise "Ye email spam hai ya nahi?" ya "Ye customer computer kharidega ya nahi, yes ya no?" Jawab hamesha kuch fixed labels mein se ek hota hai, aur unme koi order nahi hota (spam, not-spam se "bada" ya "chhota" nahi hai).
- **Prediction** ka jawab hota hai "**kitna / kya value**?" — jaise "Ye ghar kitne mein bikega?" ya "Kal ka temperature kya hoga?" Jawab ek number hota hai jo continuous scale par kuch bhi ho sakta hai.

Simple tarika yaad rakhne ka: agar jawab ek **naam/category** hai, to wo classification hai. Agar jawab ek **number** hai, to wo prediction hai (aaj-kal isse "regression" bolte hai).

Har kaam ke liye kai algorithms hai — decision trees, "Bayesian" methods (probability par based), rule-based systems, neural networks, k-nearest-neighbor, aur support vector machines — ye sab classification kar sakte hai; linear/nonlinear regression aur neural networks prediction kar sakte hai.

Real-life mein use: credit card fraud pakadna, kis customer ko ad dikhana hai decide karna, machine ya employee ka performance predict karna, manufacturing mein defects dhundna, aur bimari ka diagnosis karna.
