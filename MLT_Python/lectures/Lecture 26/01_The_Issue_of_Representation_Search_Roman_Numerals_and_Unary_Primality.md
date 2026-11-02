# Topic 1: The Issue of Representation: Searching, Roman Numerals and Unary Primality

Source: Lecture 26, slide 5 ("Issue of Representation"). Enriched with web research (Goodfellow, Bengio & Courville, *Deep Learning*, MIT Press 2016, ch. 1 and ch. 15 on representation; standard algorithm-complexity results). All worked numbers are ours and were checked with a short Python script.

---

## 1) Technical Explanation

### What the slide says

- "Representation of data in an **efficient/structured** manner is **crucial** for solving problems more effectively."
- Three examples:
  1. Searching for a set of elements in a given list (**sorted / unsorted**).
  2. Arithmetic operations on **Arabic and Roman numerals**.
  3. **Primality test** of n when n is represented as **11111…111** (n ones).
- "**Structured representation** can help in predicting future values."

### What "representation" means

A **representation** is the form in which the same information is written down or stored. The information does not change; only its format does. The key claim is:

> How hard a task is depends heavily on how the input is represented.

This is the central idea of the lecture. In ML, the "representation" of an example is its **feature vector** ([[02_Features_Labels_and_Target_Variable]] from Lecture 1). A good feature vector can make a hard problem easy for a simple model.

### Example 1: searching a sorted vs unsorted list

Task: is the number 7,349 in this list of n numbers?

| Representation | Best method | Comparisons in the worst case |
|---|---|---|
| Unsorted list | Linear search: check every element | n |
| Sorted list | Binary search: compare with the middle, discard half, repeat | ⌈log₂(n + 1)⌉ |

For n = 1,000,000:
- Linear search: up to **1,000,000** comparisons.
- Binary search: log₂(10⁶) = 19.93, so at most **20** comparisons.

Same numbers, same question. Only the arrangement changed, and the cost dropped by a factor of 50,000.

### Example 2: Arabic vs Roman numerals

The *Deep Learning* book (ch. 1) gives this exact example: dividing 210 by 6 by long division is routine in Arabic numerals but awkward in Roman numerals.

- Arabic: **210 ÷ 6 = 35**. Long division works digit by digit because the system is **positional**: each digit's place tells its value (2 hundreds, 1 ten, 0 ones), and there is a zero.
- Roman: **CCX ÷ VI = XXXV**. There is no place value and no zero, so a symbol's value depends on its neighbours (IV = 4 but VI = 6). There is no simple digit-by-digit method, so you effectively convert to another form first.

The numbers are identical. The representation decides which algorithms are available.

### Example 3: primality test in unary

Writing n as n ones is called **unary** representation. For example 13 = `1111111111111` (13 ones).

What changes:

| | Unary | Binary |
|---|---|---|
| Length of the input for n = 13 | 13 symbols | 4 bits (1101) |
| Length for n = 1,000,003 | 1,000,003 symbols | 20 bits |
| Trial division up to √n (≈ 1,000 steps for n = 1,000,003) | polynomial in the input length (√length) | exponential in the input length (≈ 2^(length/2)) |

Three lessons:

1. **Unary wastes space.** Storing a million needs a million symbols instead of 20 bits.
2. **Unary changes how "hard" a problem looks.** Measured against input length, trial division is easy in unary and exponential in binary. Complexity theory calls such algorithms "pseudo-polynomial": fast only because the input was written wastefully. (Primality in binary was finally shown to be polynomial-time by the AKS test in 2002, by a completely different method.)
3. **Some representations allow tricks.** In unary, a classic regular expression detects composites: a string of n ones is **not** prime exactly when it matches `^1?$|^(11+?)\1+$`. That pattern means "0 or 1 ones, or some block of 2+ ones repeated 2+ times", which is a factorisation n = a·b. We checked it: the numbers 1–29 that do not match are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, which are exactly the primes.

### "Structured representation can help in predicting future values"

If data is stored with its structure visible, patterns become easy to see and extrapolate. Examples:
- A daily sales list written as (date, amount) and sorted by date shows trend and seasonality. The same numbers in random order hide them.
- In ML, transforming features (e.g., log of income, or day-of-week extracted from a date) often lets a simple model predict much better (data transformation in [[03_Data_Transformation_Overview]] from Lecture 7).

### Link to the rest of the lecture

Slide 6 shows the same idea visually: one dataset that is impossible to separate with a straight line in one coordinate system and trivial in another ([[02_Choice_of_Representation_Cartesian_vs_Polar_Coordinates]]). Deep learning's main promise is to **learn** such good representations automatically instead of a human inventing them.

---

## 2) Simple English Explanation

**Representation** simply means *the way information is written down*. The information stays the same; only its form changes. The slide's point is that **the form can make a job very easy or very hard**.

**Example 1: finding a name in a list.**
- If a phone book is in random order, you may have to read every one of a million names. That is up to 1,000,000 checks.
- If it is in alphabetical order, you open it in the middle, see whether your name comes before or after, throw away half, and repeat. Halving a million about 20 times gets you down to one name, so you need **at most 20 checks**.
- Same names, same question, but sorting made it 50,000 times faster.

**Example 2: Arabic vs Roman numbers.**
- 210 ÷ 6 = 35 is easy to work out on paper, because in our normal digits each position means something (hundreds, tens, ones) and we have zero.
- In Roman numerals the same sum is CCX ÷ VI = XXXV. Roman numerals have no zero and no place value (IV is 4 but VI is 6), so you can't divide column by column. Most people would first convert to normal digits.

**Example 3: writing a number as a row of ones.**
- Writing 13 as `1111111111111` is called *unary*. It is like counting with tally marks.
- It wastes space: a million would need a million marks, while the computer's binary system needs only 20 bits.
- But it changes how hard things look. To test whether a number is prime, you try dividing by numbers up to its square root. For 1,000,003 that's about 1,000 tries. Compared with a million tally marks, 1,000 tries looks cheap. Compared with 20 bits, it looks huge. So how "difficult" a task seems depends on how the input was written.
- With tally marks you can even test primes with a pattern-matching trick: a row of n marks can be split into equal groups of 2 or more only if n is not prime. We checked: from 1 to 29 the trick picks out exactly 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

**Last point on the slide:** well-organised data helps you predict the future. Sales figures sorted by date show a rising trend or a festival spike. The same figures shuffled show nothing.

**Why this matters for deep learning:** in machine learning the "representation" of an example is the list of features we give the computer. Good features make even a simple model work well. Deep learning tries to have the computer find good features by itself.

---

## 3) Hinglish Explanation (Beginner-Friendly)

**Representation** ka matlab hai information ko *kis form me likha ya store kiya gaya hai*. Information wahi rehti hai, sirf uska format badalta hai. Slide ka main point: **format hi decide karta hai ki problem aasaan hogi ya mushkil.** ML me kisi example ka representation uske **features** hote hain.

**Example 1: List me number dhoondhna (sorted vs unsorted).**
- List unsorted hai to har element check karna padega: **linear search**, worst case me n comparisons. n = 10 lakh (1,000,000) ho to 10 lakh checks.
- List sorted hai to **binary search**: beech wala element dekho, aadhi list phek do, repeat. log₂(10⁶) = 19.93, yaani **sirf 20 checks** max.
- Same numbers, same sawaal, sirf arrangement badla aur kaam 50,000 guna kam ho gaya.

**Example 2: Arabic vs Roman numerals.**
- 210 ÷ 6 = 35 normal digits me long division se aaram se ho jaata hai, kyunki har digit ki **position** ka matlab hai (sau, das, ek) aur zero bhi hai.
- Roman me yahi sawaal CCX ÷ VI = XXXV hai. Roman me na zero hai na place value (IV = 4, par VI = 6), to column-by-column divide nahi kar sakte. Pehle normal digits me convert karna padega.
- *Deep Learning* book (Goodfellow et al.) ka chapter 1 bhi yahi 210 ÷ 6 wala example deta hai.

**Example 3: Number ko 1111…111 (n ones) ki tarah likhna.**
- Isko **unary** kehte hain, jaise tally marks. 13 = `1111111111111` (13 ones).
- Space waste hota hai: 10,00,003 ke liye 10,00,003 symbols, jabki binary me sirf 20 bits.
- Prime test ke liye √n tak divide karke dekhte hain. n = 1,000,003 ke liye lagbhag 1,000 tries. Input length 10 lakh symbols ke saamne 1,000 tries kam lagte hain (polynomial). Par 20 bits ke saamne wahi 1,000 tries bahut zyada hain (exponential). Matlab problem kitni "hard" dikhegi, wo representation par depend karta hai.
- Unary me ek mazedaar trick bhi hai: regex `^1?$|^(11+?)\1+$` tabhi match karta hai jab n prime **nahi** hai (n ko barabar groups me tod sakte hain, yaani n = a·b). Humne check kiya: 1 se 29 me jo match nahi hue wo hain 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, yaani bilkul primes.

**Last point:** "Structured representation can help in predicting future values." Sales data date ke order me ho to trend aur festival spike dikh jaata hai. Shuffle kar do to kuch samajh nahi aata. ML me bhi feature transform karne se (jaise income ka log, date se weekday nikaalna) simple model bhi achha predict karta hai (Lecture 7: [[03_Data_Transformation_Overview]]).

**Deep learning se connection:** achhe features dhoondhna hi asli kaam hai. Deep learning ka promise hai ki computer ye achha representation **khud seekh le**. Agla slide isi ko ek picture se dikhata hai (Cartesian vs polar coordinates).
