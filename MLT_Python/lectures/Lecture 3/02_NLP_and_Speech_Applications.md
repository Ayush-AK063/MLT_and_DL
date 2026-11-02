# Topic 2: Natural Language & Speech Applications

Source: Lecture 3, slides 10–11 (Natural Language, Jeopardy 2011/IBM Watson).

---

## 1) Technical Explanation

The lecture organizes Natural Language / Speech applications into two groups:

**Speech Technologies:**
- **Automatic Speech Recognition (ASR)**: converting spoken audio into text (the "listening" half of an assistant like Siri).
- **Text-to-Speech (TTS) synthesis**: converting written text into spoken audio (the "talking" half).
- **Dialog systems**: managing multi-turn conversations — understanding user intent across a back-and-forth exchange, not just single commands.
- Example cited: **Siri**, which combines ASR (understanding your voice command) + language understanding (figuring out what you want) + TTS (speaking a response) + dialog management.

**Language Processing Technologies:**
- **Question Answering**: given a natural-language question, retrieving/generating a precise answer (rather than just a list of documents).
- **Machine Translation**: automatically converting text from one language to another, illustrated in the lecture with a French↔English news-article translation example ("Il est impossible aux journalistes..." → "It is impossible for journalists...").
- **Web search**: using language understanding to match a query's intent to relevant documents.
- **Text classification, spam filtering**: assigning a category (e.g., spam vs. not-spam) to a piece of text automatically.

**Jeopardy 2011 (IBM Watson)**: A landmark case study cited in the lecture — IBM's **Watson** system competed on the American quiz show *Jeopardy!* against former human champions and won, ending with $77,147 in the example shown. Watson had to parse tricky, pun-laden natural-language clues, search a massive knowledge base, generate candidate answers, and compute confidence scores fast enough to "buzz in" competitively — a landmark demonstration combining question answering, information retrieval, and real-time decision-making under uncertainty.

---

## 2) Simple English Explanation

This section covers how AI understands and produces human language, both spoken and written.

**Speech-related tools** (things like Siri use all of these together):
- **ASR (Speech Recognition)**: the computer listens to you talk and turns it into written text.
- **TTS (Text-to-Speech)**: the computer takes written text and reads it out loud in a voice.
- **Dialog systems**: software that can hold a back-and-forth conversation with you, keeping track of context (not just answering one question and forgetting everything).

**Text-related tools:**
- **Question Answering**: you ask a direct question, and the system gives you a direct answer (not just a webpage to read).
- **Machine Translation**: automatically converting a sentence from one language into another — the lecture shows a French news headline correctly translated into English.
- **Web search**: helping you find the right web pages based on what you typed.
- **Spam filtering**: automatically sorting your email into "spam" and "not spam."

**Jeopardy 2011**: A famous real-world showcase of these skills combined — IBM built a computer system called **Watson** that competed on the trivia game show Jeopardy! against former champion humans, and **won**, earning $77,147 in prize money in the example shown. This required Watson to understand tricky wordplay in the questions, search a giant amount of stored knowledge super fast, and decide with confidence when to answer — all live, under time pressure, just like a human contestant.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye section batata hai ki AI kaise **bhasha (language)** samajhta hai aur use karta hai — bolke bhi aur likh kar bhi.

**Speech (Bolne-Sunne) se related tools:**
(Siri jaise assistants inn sabko ek saath use karte hai)
- **ASR (Automatic Speech Recognition)**: Computer aapki awaaz sunkar usse **text mein convert** karta hai.
- **TTS (Text-to-Speech)**: Computer likhe hue text ko **awaaz mein bol kar** sunata hai.
- **Dialog Systems**: Software jo aapse **lagatar baat-cheet** kar sakta hai — matlab pichhle sawaal-jawaab ko yaad rakhte hue aage baat karta hai, sirf ek sawaal ka jawaab dekar bhool nahi jaata.

**Text (Likhi hui bhasha) se related tools:**
- **Question Answering**: Aap direct sawaal pucho, system aapko direct jawaab de — na ki sirf ek website ka link de jisme dhoondhna pade.
- **Machine Translation**: Ek bhasha ka sentence dusri bhasha mein automatically convert karna. Lecture mein example diya hai: French news headline ko English mein sahi tarike se translate kiya gaya hai.
- **Web Search**: Aapne jo type kiya uske hisaab se sahi webpages dhoondhna.
- **Spam Filtering**: Email ko automatically "spam" aur "normal" mein baantna.

**Jeopardy 2011 (IBM Watson ka famous example):**
Ye is section ka sabse bada real-world example hai. IBM ne ek computer system banaya jiska naam **Watson** tha, jisne **Jeopardy!** naam ke ek famous American quiz show mein purane champion insano ke saath compete kiya — aur **jeet gaya**! Example mein Watson ne $77,147 jeete.

Isme Watson ko:
- Sawaalon ke **tricky wordplay** (pheli hui bhasha, puns) ko samajhna tha
- Ek **bahut bada gyaan bhandaar (knowledge base)** super fast search karna tha
- Confidence ke saath decide karna tha ki jawaab dena hai ya nahi — aur ye sab **real-time mein**, time pressure ke saath, ek insaan contestant ki tarah.

Ye ek bada milestone tha jisne dikhaya ki AI kitna advanced ho chuka hai natural language samajhne mein.
