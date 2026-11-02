# Topic 6: Concept Hierarchy

Source: Lecture 8, slides 30–33 (Concept Hierarchy ×4 — definition, price hierarchy diagram, location hierarchy, time hierarchy).

---

## 1) Technical Explanation

**Definition**: *"A concept hierarchy defines a sequence of mappings from a set of low-level concepts to higher-level, more general concepts."* This formalizes the **Generalization** technique first introduced in Lecture 7/Topic 1 of this lecture ([[01_Aggregation_Generalization_and_Feature_Construction]]) — generalization *is* the act of moving up a concept hierarchy.

**Key properties of concept hierarchies**:
- *"Many concept hierarchies are implicit within the database schema"* — i.e., the structure often already exists naturally in how data is organized (e.g., a database that stores city, state, and country as separate related fields already implies a hierarchy).
- *"Concept hierarchies may be provided manually by system users or may be automatically generated based on statistical analysis of the data distribution."*
- *"A concept hierarchy [is] a total or partial order among attributes"* — meaning the levels have a defined, consistent ordering from most specific to most general.
- *"Concept hierarchies may also be defined by discretizing or grouping values for a given dimension"* — directly connecting this topic to Discretization (Topics 3–5): discretization (turning continuous numbers into categorical bins) is itself one way of constructing a concept hierarchy level.

**Example 1 — Concept hierarchy for `price` (a numeric attribute)**: a tree structure where the top level is the full range `($0...$1000]`, which splits into five `$200`-wide bands at the next level (`$0...$200], ($200...$400], ($400...$600], ($600...$800], ($800...$1000]`), each of which further splits into two `$100`-wide bands at the bottom level (e.g., `($0...$100]` and `($100...$200]`). This demonstrates: *"A concept hierarchy for a numeric attribute can be constructed automatically or it can be created by the user"* and *"A concept hierarchy can be used for discretization"* — this is essentially a **multi-level, nested binning scheme**, where you can choose to discretize at whichever level of granularity (2 bands, 5 bands, or 10 bands) suits your analysis.

**Example 2 — Concept hierarchy for `location` (a nominal/categorical attribute)**: demonstrating that concept hierarchies aren't limited to numeric data. The hierarchy: `all` (top level) → `country` (e.g., Canada, USA) → `province_or_state` (e.g., British Columbia, Ontario under Canada; New York, Illinois under USA) → `city` (e.g., Vancouver, Victoria under British Columbia; Toronto, Ottawa under Ontario; New York, Buffalo under New York state; Chicago, Urbana under Illinois). This is the formal, generalized version of the earlier "street → city → country" generalization example from Topic 1.

**Example 3 — Concept hierarchy for `time`**: shown as a directed structure rather than a simple tree — `day → week → month → quarter → year`, but with `week` and `month` both independently rolling up toward `year` via `quarter` (month→quarter→year) and separately (week→year directly implied by the diagram's arrows) — reflecting that calendar time has genuinely **multiple valid hierarchical groupings** (a day belongs to both a specific week AND a specific month, but weeks and months don't nest cleanly into each other, since a week can span two different months).

---

## 2) Simple English Explanation

A **concept hierarchy** is a structured way of organizing information from very specific/detailed levels up to broader, more general levels — like a family tree, but for categories or ranges of data instead of people.

**Key ideas**:
- Often, this hierarchy is already hidden inside how your database is set up — you might not even need to build it from scratch, just recognize it.
- Someone can build this hierarchy by hand, or a computer can automatically figure out a sensible hierarchy just by studying how the data is spread out.
- Discretization (which you just learned) is actually **one specific way of building part of a concept hierarchy** — grouping raw numbers into categories is exactly what creates one "level" of such a hierarchy.

**Example 1 — A price hierarchy**: Imagine grouping all prices from $0 to $1000. At the top, it's just one big group ($0–$1000). One level down, you split it into 5 medium-sized bands, each $200 wide ($0–$200, $200–$400, and so on). One level further down, each of those splits again into 2 smaller $100-wide bands. You can now choose how "zoomed in" you want to be — using just 5 categories, or 10 more precise ones — depending on what you need for your analysis.

**Example 2 — A location hierarchy**: Not just numbers can be organized this way — locations can too! Starting from "all locations" at the top, you go down to Country (like Canada or the USA), then Province/State (like Ontario or New York), then finally City (like Toronto or Buffalo). This is exactly the "street → city → country" idea from earlier, shown as a full, structured tree.

**Example 3 — A time hierarchy**: Time can also be organized hierarchically — day, week, month, quarter, year — but it's a bit trickier than the other two examples, because a single week can actually span across two different months! So the "week" and "month" branches don't perfectly nest inside each other the way city-inside-state-inside-country does — they're both valid ways of grouping days, but they don't line up exactly with each other.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ek **Concept Hierarchy** information ko organize karne ka ek structured tarika hai — bahut specific/detailed levels se lekar broader, zyada general levels tak — bilkul ek family tree jaisa, lekin logo ke bajaye data ki categories ya ranges ke liye.

**Key ideas:**
- Aksar, ye hierarchy pehle se hi aapke database ke setup mein chhupi hoti hai — aapko shayad isse scratch se banana bhi na pade, bas usse pehchan na ho.
- Koi insaan hath se ye hierarchy bana sakta hai, ya computer khud data ka distribution study karke automatically ek sensible hierarchy nikal sakta hai.
- **Discretization** (jo aapne abhi seekha) actually concept hierarchy ka ek part banane ka **ek specific tarika** hai — raw numbers ko categories mein group karna exactly wahi kaam hai jo aisi hierarchy ka ek "level" banata hai.

**Example 1 — Price ki hierarchy:**
Socho aap sab prices ko $0 se $1000 tak group kar rahe ho. Sabse upar, ye bas ek bada group hai ($0-$1000). Ek level neeche, aap isse 5 medium-size bands mein baantte ho, har ek $200 wide ($0-$200, $200-$400, waghera). Ek level aur neeche, in bands mein se har ek phir se 2 chhote $100-wide bands mein baant jaata hai. Ab aap choose kar sakte ho ki aapko kitna "zoomed in" hona hai — sirf 5 categories use karke, ya 10 zyada precise wale, apni analysis ki zaroorat ke hisaab se.

**Example 2 — Location ki hierarchy:**
Sirf numbers hi nahi, locations bhi is tarah organize ho sakte hai! "All locations" se shuru karke, aap Country (jaise Canada ya USA) tak jaate ho, fir Province/State (jaise Ontario ya New York), fir aakhir mein City (jaise Toronto ya Buffalo). Ye bilkul wahi "street → city → country" wala idea hai jo pehle bataya gaya tha, ab ek pure, structured tree ke roop mein dikhaya gaya hai.

**Example 3 — Time ki hierarchy:**
Time bhi hierarchically organize ho sakta hai — day, week, month, quarter, year — lekin ye baaki 2 examples se thoda tricky hai, kyunki ek single week actually 2 alag months mein span kar sakta hai! Isliye "week" aur "month" branches ek doosre ke andar perfectly nest nahi hote jaise city-inside-state-inside-country karti hai — dono days group karne ke valid tarike hai, lekin ye ek doosre ke saath exactly align nahi hote.
