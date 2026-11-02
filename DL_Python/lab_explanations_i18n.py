"""
Hand-written Technical and Hinglish rewrites of the Lab Assignment
explanation text, for the site's Lab Assignments mode.

Why this file exists: every lab_assignment_N.py script's own "#" comments
are already written in a plain, beginner-friendly register (that IS the
site's "Simple English" style, extracted automatically, at zero extra
cost - see build_labs.py's code_to_chunks()/attach_explanation_styles()).
To offer the same three reading styles the lecture notes use (Technical /
Simple English / Hinglish), we only need to hand-author the OTHER two
styles here - the actual Python code itself never changes across styles,
only the surrounding explanation prose does.

Structure:
    TRANSLATIONS = {
        <assignment number>: {
            <section id, e.g. "setup", "question-1", "wrapup">: [
                {"technical": "...", "hinglish": "..."},  # chunk index 0
                {"technical": "...", "hinglish": "..."},  # chunk index 1
                ...
            ],
            ...
        },
        ...
    }

The list for each section must be in the SAME order as the explanation
chunks appear in that section's code (build_labs.py numbers them via
"exp_index" as it parses the script top to bottom). If a section is
missing here, or a list is shorter than the real number of explanation
chunks, the missing entries just fall back to the Simple English text -
nothing breaks, it just isn't translated yet.

Multi-paragraph text: separate paragraphs with a blank line ("\n\n"),
exactly like the Simple English source text does - the site renders each
one as its own <p>. A paragraph wrapped as "@@like this@@" renders as a
bold mini-heading instead of normal body text (matches how the Simple
English text marks a "--- Handling "Age" ---" style sub-heading).
"""

TRANSLATIONS = {

    # ============================================================
    # LAB ASSIGNMENT 1 — Data Cleaning on the Titanic Dataset
    # ============================================================
    1: {

        "setup": [
            {
                "technical":
                    "@@STEP 0: IMPORT THE REQUIRED LIBRARIES@@\n\n"
                    "The script begins by importing pandas, the standard Python library for "
                    "tabular data manipulation, aliased as pd per near-universal community "
                    "convention. An import statement binds an external module's namespace into "
                    "the current script so its functions and classes become callable.",
                "hinglish":
                    "@@STEP 0: ZAROORI LIBRARIES IMPORT KARNA@@\n\n"
                    "Script sabse pehle pandas import karta hai — Python ki standard library jo "
                    "tabular (table-shaped) data ke saath kaam karne ke liye bani hai, aur ise "
                    "convention ke hisaab se pd naam se alias kiya jaata hai. Import statement "
                    "kisi external module ke functions/classes ko current script mein use karne "
                    "layak bana deta hai.",
            },
            {
                "technical":
                    "The os module (Python's standard-library interface to the operating system) "
                    "is imported solely to construct a filesystem path programmatically, so the "
                    "script resolves the shared CSV's location correctly regardless of the "
                    "process's current working directory at invocation time.",
                "hinglish":
                    "os module (Python ki standard library jo operating system se baat karti hai) "
                    "sirf isliye import kiya gaya hai taaki ek file path programmatically banaya "
                    "ja sake — isse script har baar shared CSV ko sahi jagah dhoond legi, chahe "
                    "tum ise kisi bhi folder se run karo.",
            },
            {
                "technical":
                    "Two pandas display options are configured purely for output presentation: "
                    "display.max_columns=None disables column truncation in printed DataFrames, "
                    "and display.width is set to a large value so a wide row prints on a single "
                    "line rather than being wrapped by pandas into stacked column blocks joined "
                    "by a backslash continuation marker. Neither option affects the underlying "
                    "data or any computation.",
                "hinglish":
                    "Do pandas display options set kiye gaye hai — sirf output ko readable banane "
                    "ke liye. display.max_columns=None ka matlab hai koi bhi column '...' mein "
                    "chhupega nahi, aur display.width ko bada rakha hai taaki wide table ek hi "
                    "line mein print ho, do stacked blocks mein '\\' ke saath split hokar confuse "
                    "na kare. In dono ka actual data ya calculation par koi asar nahi padta.",
            },
        ],

        "question-1": [
            {
                "technical":
                    'pd.read_csv() parses the CSV file into a pandas DataFrame — an in-memory, '
                    "two-dimensional, labeled data structure with rows and typed columns. The "
                    'result is assigned to the identifier df, the conventional variable name '
                    "for a primary DataFrame in data-science code.\n\n"
                    "The CSV path is resolved relative to the script's own file location "
                    '(one directory up, inside the shared Lab_assingments folder), rather than '
                    "relative to the process's current working directory, since the same "
                    "dataset is intentionally shared across multiple lab assignments and must "
                    "resolve correctly regardless of the invocation context.",
                "hinglish":
                    'pd.read_csv() CSV file ko parse karke ek pandas DataFrame banata hai — ek '
                    "in-memory, two-dimensional, labeled data structure jisme rows aur typed "
                    'columns hote hai. Result "df" variable mein store hota hai, jo data-science '
                    "code mein primary DataFrame ke liye conventional naam hai.\n\n"
                    "CSV ka path script ki apni file location ke relative resolve hota hai (ek "
                    "folder upar, shared Lab_assingments folder ke andar), na ki jahan se script "
                    "run kiya gaya us current working directory ke relative — kyunki yehi dataset "
                    "jaan-boojh kar kai lab assignments mein share kiya gaya hai, isliye ye kahin "
                    "se bhi run karo to sahi resolve hona chahiye.",
            },
            {
                "technical":
                    "df.shape is an attribute (not a method) that returns a tuple "
                    "(n_rows, n_columns) describing the DataFrame's dimensions — accessed "
                    "without parentheses since it is a stored property rather than a callable.",
                "hinglish":
                    "df.shape ek attribute hai (method nahi), jo (n_rows, n_columns) — ek tuple "
                    "— return karta hai jisse DataFrame ka size pata chalta hai. Ise bina "
                    "parentheses ke access karte hai kyunki ye ek stored property hai, koi "
                    "callable function nahi.",
            },
            {
                "technical":
                    "df.head(5) returns the first n rows of the DataFrame (n=5 by default when "
                    "called without an argument), letting you inspect the schema and sample "
                    "values without materializing the full 891-row table in the terminal.",
                "hinglish":
                    "df.head(5) DataFrame ki pehli n rows return karta hai (bina argument diye "
                    "default n=5 hota hai), taaki tum bina 891 rows print kiye hi schema aur "
                    "sample values dekh sako.",
            },
            {
                "technical":
                    'df.dtypes reports the inferred data type of every column: int64 for whole '
                    "numbers, float64 for decimal numbers, and object/str for text (or a mixed "
                    "column containing missing values). Correctly identifying each column's dtype "
                    "matters because missing-value handling strategy differs between numeric and "
                    "categorical columns.",
                "hinglish":
                    "df.dtypes har column ka inferred data type batata hai: int64 (poore "
                    "numbers), float64 (decimal numbers), aur object/str (text, ya koi column "
                    "jisme missing values bhi mix hai). Har column ka sahi dtype pehchanna "
                    "zaroori hai kyunki numeric aur categorical columns mein missing-value handle "
                    "karne ki strategy alag hoti hai.",
            },
            {
                "technical":
                    "A brief data dictionary is provided for domain context, since correctly "
                    'interpreting abbreviated column names such as SibSp and Parch is a '
                    "prerequisite for any downstream decision in this pipeline.",
                "hinglish":
                    "Yahan ek chhota data dictionary diya gaya hai domain context ke liye, "
                    'kyunki SibSp aur Parch jaise abbreviated column names ko sahi samajhna is '
                    "pure pipeline ke aage ke har decision ke liye zaroori hai.",
            },
        ],

        "question-2": [
            {
                "technical":
                    'A "missing value" is a cell with no recorded observation for a given '
                    "(row, column) pair. pandas represents this internally with the sentinel NaN "
                    "(Not a Number), regardless of whether the column's other values are numeric "
                    "or textual.\n\n"
                    "df.isnull() returns a boolean DataFrame of identical shape to df, where each "
                    "cell is True if missing and False otherwise. Chaining .sum() aggregates each "
                    "column's True count (Python's bool subtype coerces to 1/0 under arithmetic "
                    "operations), yielding a per-column missing-value count.",
                "hinglish":
                    '"Missing value" ka matlab hai ek cell jisme kisi (row, column) pair ke liye '
                    "koi observation record hi nahi hai. pandas ise internally ek sentinel value "
                    "NaN (Not a Number) se represent karta hai — chahe us column ki baaki values "
                    "numeric ho ya text.\n\n"
                    "df.isnull() df ke bilkul same shape ka ek boolean DataFrame return karta hai, "
                    "jisme har cell True (missing) ya False (present) hota hai. Uske baad "
                    ".sum() chain karne se har column ke True values ka count aa jaata hai "
                    "(Python mein bool, arithmetic operations mein 1/0 mein convert ho jaata "
                    "hai), jisse per-column missing-value count mil jaata hai.",
            },
            {
                "technical":
                    "The percentage is derived by dividing each column's missing count by "
                    "len(df) (total row count), scaling by 100, and rounding to 2 decimal places "
                    "via .round(2) for readability.",
                "hinglish":
                    "Percentage nikalne ke liye har column ka missing count len(df) (total row "
                    "count) se divide karte hai, 100 se multiply karte hai, aur readability ke "
                    "liye .round(2) se 2 decimal places tak round kar dete hai.",
            },
            {
                "technical":
                    "pd.DataFrame({...}) constructs a new summary DataFrame from the two "
                    "previously computed Series, so both metrics can be inspected side by side "
                    "in one table. The dictionary keys become that new DataFrame's column labels.",
                "hinglish":
                    "pd.DataFrame({...}) do pehle se calculate ki hui Series se ek naya summary "
                    "DataFrame banata hai, taaki dono metrics ek hi table mein side by side dekhi "
                    "ja sake. Dictionary ki keys us naye DataFrame ke column labels ban jaati hai.",
            },
            {
                "technical":
                    "The summary is boolean-filtered to rows where Missing Count > 0 (columns "
                    "with zero missing values are dropped from the view), then sorted descending "
                    "so the most-affected columns surface first.",
                "hinglish":
                    "Summary table ko boolean-filter karke sirf un rows tak limit kiya jaata hai "
                    "jahan Missing Count > 0 ho (zero-missing columns view se hat jaate hai), fir "
                    "descending order mein sort kiya jaata hai taaki sabse zyada affected columns "
                    "sabse upar dikhein.",
            },
            {
                "technical":
                    "df.copy() is called before any mutation to create an independent deep copy "
                    "in memory, decoupled from the original df. This is standard defensive "
                    "practice: it preserves an unmodified baseline for comparison and prevents "
                    "accidental in-place corruption of the source data during iterative cleaning.",
                "hinglish":
                    "Koi bhi mutation karne se pehle df.copy() call kiya jaata hai, jo memory mein "
                    "ek independent deep copy banata hai, original df se alag. Ye ek standard "
                    "defensive practice hai: isse ek unmodified baseline compare karne ke liye "
                    "bacha rehta hai, aur cleaning ke dauraan source data accidentally corrupt "
                    "hone se bach jaata hai.",
            },
            {
                "technical":
                    '@@Handling "Age" (a numeric column, ~20% missing)@@\n\n'
                    "For a numeric column with a moderate missing-value proportion, imputation "
                    "is the standard technique — replacing each missing cell with a statistically "
                    "derived estimate rather than discarding the entire row (which would also "
                    "sacrifice every other, fully-observed feature for that record).\n\n"
                    "The median is chosen over the mean because Age's distribution contains "
                    "outliers, and the median (the 50th percentile) is a robust statistic — "
                    "unlike the mean, it is not pulled toward extreme values, making it the "
                    "safer central-tendency estimator for imputation here.",
                "hinglish":
                    '@@"Age" handle karna (ek numeric column, ~20% missing)@@\n\n'
                    "Ek numeric column jisme moderate amount mein missing values ho, uske liye "
                    "standard technique imputation hoti hai — har missing cell ko ek "
                    "statistically-derived estimate se replace karna, poori row delete karne ke "
                    "bajaye (jisse us record ki baaki saari, fully-observed features bhi waste ho "
                    "jaati).\n\n"
                    "Mean ki jagah median isliye choose kiya gaya hai kyunki Age ki distribution "
                    "mein outliers hai, aur median (50th percentile) ek robust statistic hai — "
                    "mean ki tarah extreme values ki taraf khinchta nahi, isliye yahan imputation "
                    "ke liye safer central-tendency estimator hai.",
            },
            {
                "technical":
                    "Series.fillna(value) replaces every NaN entry in that column with the given "
                    "value while leaving all non-null entries untouched; reassigning to the same "
                    "column label overwrites it with the completed version.",
                "hinglish":
                    "Series.fillna(value) us column ke har NaN entry ko diye gaye value se "
                    "replace kar deta hai, baaki saari non-null entries ko chhue bina. Result ko "
                    "wapas usi column label mein assign karne se wo column complete version se "
                    "overwrite ho jaata hai.",
            },
            {
                "technical":
                    '@@Handling "Embarked" (a categorical column, 2 missing)@@\n\n'
                    "Embarked is categorical (its domain is restricted to {C, Q, S}), so mean or "
                    "median imputation is mathematically undefined — there is no arithmetic "
                    "average of categorical labels. The categorical analogue is mode imputation: "
                    "filling missing entries with the modal (most frequent) category.",
                "hinglish":
                    '@@"Embarked" handle karna (ek categorical column, 2 missing)@@\n\n'
                    "Embarked categorical hai (iski domain sirf {C, Q, S} tak limited hai), "
                    "isliye mean ya median imputation mathematically hi undefined hai — "
                    "categorical labels ka koi arithmetic average nahi hota. Categorical column "
                    "ke liye equivalent technique mode imputation hai: missing entries ko modal "
                    "(sabse zyada frequent) category se fill karna.",
            },
            {
                "technical":
                    "Series.mode() can return multiple values in the event of a tie, so it "
                    "always returns a Series of candidates even when a unique mode exists; "
                    "indexing [0] extracts the first (here, the only) modal value.",
                "hinglish":
                    "Series.mode() tie hone ki soorat mein multiple values bhi return kar sakta "
                    "hai, isliye ye hamesha ek Series of candidates return karta hai — chahe "
                    "unique mode hi kyun na ho. [0] index lagane se pehli (aur yahan, akeli) "
                    "modal value nikal aati hai.",
            },
            {
                "technical":
                    '@@Handling "Cabin" (~77% missing)@@\n\n'
                    "Imputation is inappropriate here on two grounds: Cabin values are near-"
                    "unique identifiers with no meaningful central tendency, and at ~77% "
                    "missing, any imputed value would constitute fabricated signal rather than "
                    "recovered information, degrading rather than improving data quality.\n\n"
                    "The appropriate remediation is column-level removal rather than row-level "
                    "removal, since the unreliability is intrinsic to the column itself. Dropping "
                    "the affected rows instead would discard 687 of 891 records (~77% of the "
                    "dataset) purely due to one column, sacrificing otherwise complete data in "
                    "every other feature.\n\n"
                    "DataFrame.drop(columns=[...]) removes the specified column(s) from the "
                    "DataFrame.",
                "hinglish":
                    '@@"Cabin" handle karna (~77% missing)@@\n\n'
                    "Yahan imputation do wajah se appropriate nahi hai: Cabin values near-unique "
                    "identifiers hai jinka koi meaningful central tendency nahi hota, aur ~77% "
                    "missing hone ki wajah se koi bhi imputed value fabricated signal hogi, "
                    "recovered information nahi — jo data quality ko behtar nahi, kharaab karegi.\n\n"
                    "Sahi remedy row-level removal nahi, balki column-level removal hai, kyunki "
                    "unreliability khud us column ke andar hi hai. Agar iski jagah affected rows "
                    "hata di jaayein, to 891 mein se 687 records (~77% dataset) sirf ek column ki "
                    "wajah se waste ho jaayenge, jabki baaki har feature mein wo data complete "
                    "tha.\n\n"
                    "DataFrame.drop(columns=[...]) diye gaye column(s) ko DataFrame se remove "
                    "kar deta hai.",
            },
            {
                "technical":
                    "A final isnull().sum() verification confirms zero remaining missing values "
                    "across all columns of df_clean, closing the missing-data-handling loop.",
                "hinglish":
                    "Ek final isnull().sum() verification confirm karta hai ki df_clean ke har "
                    "column mein ab zero missing values bache hai — missing-data-handling ka loop "
                    "yahan close ho jaata hai.",
            },
        ],

        "question-3": [
            {
                "technical":
                    'A "duplicate record" is a row whose values are identical, column for '
                    "column, to another row in the table.\n\n"
                    "DataFrame.duplicated() returns a boolean mask across rows: False for a "
                    "row's first occurrence, True for every subsequent identical occurrence. "
                    "Chaining .sum() over this mask yields the total duplicate-row count.",
                "hinglish":
                    '"Duplicate record" ek aisi row hai jiski values, column-by-column, table ki '
                    "kisi doosri row se bilkul identical hai.\n\n"
                    "DataFrame.duplicated() rows ke across ek boolean mask return karta hai: kisi "
                    "row ki pehli occurrence ke liye False, aur uske baad har identical repeat "
                    "occurrence ke liye True. Is mask par .sum() chain karne se total "
                    "duplicate-row count mil jaata hai.",
            },
            {
                "technical":
                    "Boolean-indexing df_clean with df_clean.duplicated() filters the DataFrame "
                    "down to only the flagged duplicate rows, satisfying the requirement to "
                    "explicitly display them.",
                "hinglish":
                    "df_clean ko df_clean.duplicated() se boolean-index karne se DataFrame filter "
                    "hokar sirf flagged duplicate rows tak reh jaata hai — isse assignment ki "
                    "requirement puri hoti hai ki duplicates ko explicitly display kiya jaaye.",
            },
            {
                "technical":
                    "PassengerId is additionally checked in isolation, since it is intended as a "
                    "unique identifier; a repeated PassengerId would be a strong independent "
                    "signal of duplicated or corrupted data even if minor discrepancies existed "
                    "elsewhere in the row.",
                "hinglish":
                    "PassengerId ko alag se bhi check kiya jaata hai, kyunki ye ek unique "
                    "identifier hone ke liye bana hai; agar koi PassengerId repeat ho jaaye, to "
                    "ye duplicated ya corrupted data ka ek strong, independent signal hoga — "
                    "chahe row ke baaki hisson mein chhote-mote farak kyun na ho.",
            },
            {
                "technical":
                    "DataFrame.drop_duplicates() retains only the first occurrence of each "
                    "repeated row, discarding subsequent duplicates; it is invoked conditionally, "
                    "only when duplicates were actually detected.",
                "hinglish":
                    "DataFrame.drop_duplicates() har repeated row ki sirf pehli occurrence ko "
                    "rakhta hai, baaki duplicates hata deta hai; ise conditionally call kiya "
                    "jaata hai, sirf tab jab duplicates actually detect hue ho.",
            },
        ],

        "question-4": [
            {
                "technical":
                    "The actual removal is executed here, implementing the column-classification "
                    "rationale established above.",
                "hinglish":
                    "Yahan actual removal execute hoti hai, upar establish ki gayi "
                    "column-classification reasoning ko implement karte hue.",
            },
        ],

        "wrapup": [
            {
                "technical":
                    "DataFrame.to_csv(filename, index=False) serializes the cleaned DataFrame "
                    "back to disk as a persistent .csv file, avoiding the need to re-run the "
                    "pipeline to obtain the cleaned data again. index=False suppresses writing "
                    "pandas' internal row-index as an extra column, since a synthetic numbering "
                    "column is redundant here — PassengerId was already deliberately dropped.",
                "hinglish":
                    "DataFrame.to_csv(filename, index=False) cleaned DataFrame ko disk par ek "
                    "persistent .csv file ke roop mein save kar deta hai, taaki cleaned data "
                    "dobara paane ke liye poori pipeline re-run na karni pade. index=False "
                    "pandas ke internal row-index ko ek extra column ke roop mein likhne se "
                    "rok deta hai, kyunki ek synthetic numbering column yahan redundant hai — "
                    "PassengerId to hum pehle hi jaan-boojh kar drop kar chuke hai.",
            },
        ],
    },

    # ============================================================
    # LAB ASSIGNMENT 2 — Visualization, Outlier Detection,
    # Validation & Feature Scaling
    # ============================================================
    2: {

        "setup": [
            {
                "technical":
                    "@@STEP 0: IMPORT THE REQUIRED LIBRARIES@@\n\n"
                    "os is the standard-library module for filesystem operations, imported here "
                    "so the script can resolve paths and create directories reliably regardless "
                    "of the invoking process's working directory.",
                "hinglish":
                    "@@STEP 0: ZAROORI LIBRARIES IMPORT KARNA@@\n\n"
                    "os standard-library ka module hai jo filesystem operations ke liye hota "
                    "hai — ise isliye import kiya gaya hai taaki script paths reliably resolve "
                    "kar sake aur folders bana sake, chahe process kisi bhi working directory se "
                    "invoke kiya gaya ho.",
            },
            {
                "technical":
                    "pandas is imported for tabular data structures, exactly as in Lab "
                    "Assignment 1.",
                "hinglish":
                    "pandas ko tabular data structures ke liye import kiya gaya hai, bilkul Lab "
                    "Assignment 1 ki tarah.",
            },
            {
                "technical":
                    "matplotlib.pyplot is the standard plotting API in the Python data-science "
                    "stack, used here for every chart type this assignment requires (scatter, "
                    "bar, histogram, line, box plot). It is aliased as plt by the same convention "
                    "pandas is aliased as pd.",
                "hinglish":
                    "matplotlib.pyplot Python data-science stack ki standard plotting API hai, "
                    "jo is assignment ke har chart type (scatter, bar, histogram, line, box plot) "
                    "ke liye use hoti hai. Ise plt naam se alias kiya gaya hai, bilkul pandas ko "
                    "pd alias karne wale convention ki tarah.",
            },
            {
                "technical":
                    "From scikit-learn (imported under its conventional alias sklearn), two "
                    "specific transformers required for Question 4 (Feature Scaling) are "
                    "imported: MinMaxScaler, which rescales values into the [0, 1] interval, and "
                    "StandardScaler, which transforms a column to zero mean and unit variance. "
                    "Both are explained in full detail immediately before their use.",
                "hinglish":
                    "scikit-learn se (jise conventionally sklearn alias diya jaata hai), Question "
                    "4 (Feature Scaling) ke liye zaroori do specific transformers import kiye "
                    "gaye hai: MinMaxScaler, jo values ko [0, 1] interval mein rescale karta hai, "
                    "aur StandardScaler, jo ek column ko zero mean aur unit variance mein "
                    "transform karta hai. Dono ko unke use hone se pehle hi detail mein explain "
                    "kiya gaya hai.",
            },
            {
                "technical":
                    "Two pandas display options are set purely for presentation: unrestricted "
                    "column display, and a large display.width so a wide row always prints on a "
                    "single line rather than being split into stacked, backslash-joined blocks.",
                "hinglish":
                    "Do pandas display options sirf presentation ke liye set kiye gaye hai: "
                    "columns ka unrestricted display, aur ek bada display.width taaki wide row "
                    "hamesha ek hi line mein print ho, backslash-joined stacked blocks mein split "
                    "hone ke bajaye.",
            },
            {
                "technical":
                    "@@STEP 0b: DERIVE RELIABLE FILE PATHS AND CREATE A PLOTS DIRECTORY@@\n\n"
                    "os.path.dirname(os.path.abspath(__file__)) resolves the absolute path of "
                    "this script file and takes just its containing directory — i.e., \"this "
                    "script's own folder\" — independent of the shell's current working "
                    "directory at invocation time.",
                "hinglish":
                    "@@STEP 0b: RELIABLE FILE PATHS NIKALNA AUR PLOTS FOLDER BANANA@@\n\n"
                    "os.path.dirname(os.path.abspath(__file__)) is script file ka absolute path "
                    "resolve karke sirf uska containing directory nikalta hai — matlab \"is "
                    "script ka apna folder\" — chahe script jis bhi working directory se run kiya "
                    "gaya ho.",
            },
            {
                "technical":
                    "The cleaned CSV produced by Lab Assignment 1 resides in a sibling directory "
                    "(one level up, then into \"Lab Assignment 1\"). os.path.join(...) "
                    "concatenates path segments safely and portably, using the correct separator "
                    "for the host operating system.",
                "hinglish":
                    "Lab Assignment 1 se bani cleaned CSV ek sibling directory mein hoti hai (ek "
                    "level upar, fir \"Lab Assignment 1\" ke andar). os.path.join(...) path "
                    "segments ko safely aur portably jodta hai, host operating system ke sahi "
                    "separator ka use karke.",
            },
            {
                "technical":
                    "This is the target directory every generated chart image will be written "
                    "into.",
                "hinglish":
                    "Yahi wo target directory hai jisme har generate hui chart image save hogi.",
            },
            {
                "technical":
                    "os.makedirs(..., exist_ok=True) creates the directory if absent; "
                    "exist_ok=True suppresses the exception that would otherwise be raised if "
                    "the directory already exists from a prior run.",
                "hinglish":
                    "os.makedirs(..., exist_ok=True) directory ko banata hai agar wo pehle se "
                    "nahi hai; exist_ok=True us exception ko suppress kar deta hai jo warna tab "
                    "raise hoti jab directory pehle se kisi purani run se already exist karti.",
            },
            {
                "technical":
                    "plt.tight_layout() adjusts subplot spacing/margins so titles and axis "
                    "labels are not clipped or overlapping — a purely cosmetic layout call.",
                "hinglish":
                    "plt.tight_layout() subplot ki spacing/margins adjust karta hai taaki titles "
                    "aur axis labels clip ya overlap na ho — ye ek purely cosmetic layout call "
                    "hai.",
            },
            {
                "technical":
                    "plt.savefig(...) serializes the currently active figure to disk as an image "
                    "file (.png here), producing a persistent artifact independent of the Python "
                    "process.",
                "hinglish":
                    "plt.savefig(...) currently active figure ko disk par ek image file (.png) "
                    "ke roop mein serialize kar deta hai, jo Python process se independent, ek "
                    "persistent artifact ban jaati hai.",
            },
            {
                "technical":
                    "plt.close() releases the current figure from memory, ensuring the next "
                    "plt.plot(...)/plt.bar(...)/etc call begins drawing onto a fresh, empty "
                    "canvas rather than accumulating onto the previous figure.",
                "hinglish":
                    "plt.close() current figure ko memory se release kar deta hai, isse "
                    "confirm hota hai ki agli plt.plot(...)/plt.bar(...)/etc call ek fresh, empty "
                    "canvas par draw karegi, purani figure ke upar accumulate hone ke bajaye.",
            },
            {
                "technical":
                    "@@STEP 0c: LOAD THE PRE-CLEANED DATASET FROM LAB ASSIGNMENT 1@@",
                "hinglish":
                    "@@STEP 0c: LAB ASSIGNMENT 1 SE PRE-CLEANED DATASET LOAD KARNA@@",
            },
        ],

        "question-1": [
            {
                "technical":
                    "@@(a) Scatter plot: Age vs. Fare, coloured by survival outcome@@\n\n"
                    "A scatter plot maps one numeric variable to the x-axis and a second numeric "
                    "variable to the y-axis, rendering one point per observation. It is the "
                    "appropriate choice for examining whether an association exists between two "
                    "continuous variables (e.g., does Fare correlate with Age?). Colour-encoding "
                    "each point by the binary Survived label overlays a categorical dimension, "
                    "letting any visual clustering of survival outcomes across the Age/Fare plane "
                    "be inspected at a glance.",
                "hinglish":
                    "@@(a) Scatter plot: Age vs Fare, Survival ke hisaab se colour kiya gaya@@\n\n"
                    "Scatter plot ek numeric variable ko x-axis par aur doosre numeric variable "
                    "ko y-axis par map karta hai, har observation ke liye ek point draw karte "
                    "hue. Ye tab sahi choice hota hai jab check karna ho ki do continuous "
                    "variables ke beech koi association hai ya nahi (jaise, kya Fare aur Age "
                    "correlate karte hai?). Har point ko binary Survived label se colour karne se "
                    "ek categorical dimension overlay ho jaati hai, jisse Age/Fare plane par "
                    "survival outcomes ka koi visual clustering hai ya nahi, wo ek nazar mein "
                    "dikh jaata hai.",
            },
            {
                "technical":
                    "plt.figure(figsize=...) initializes a new, blank figure canvas of the "
                    "specified dimensions (in inches) — a display preference with no bearing on "
                    "the underlying data.",
                "hinglish":
                    "plt.figure(figsize=...) di gayi dimensions (inches mein) ka ek naya, blank "
                    "figure canvas initialize karta hai — ye sirf ek display preference hai, "
                    "underlying data par iska koi asar nahi.",
            },
            {
                "technical":
                    'The data is partitioned into two subsets by boolean indexing on Survived, '
                    "solely to assign each subset a distinct colour and legend label in separate "
                    "plt.scatter() calls. df[df[\"Survived\"] == 0] filters to rows where the "
                    "boolean condition evaluates True.",
                "hinglish":
                    "Data ko Survived par boolean indexing karke do subsets mein baanta jaata "
                    "hai, sirf isliye taaki alag plt.scatter() calls mein har subset ko ek "
                    'distinct colour aur legend label diya ja sake. df[df["Survived"] == 0] '
                    "filter karke sirf wahi rows deta hai jahan boolean condition True evaluate "
                    "hoti hai.",
            },
            {
                "technical":
                    "plt.scatter(x, y, ...) renders one marker per (x, y) pair. The alpha=0.6 "
                    "parameter sets partial transparency, which improves legibility when many "
                    "points overplot in a dense region.",
                "hinglish":
                    "plt.scatter(x, y, ...) har (x, y) pair ke liye ek marker render karta hai. "
                    "alpha=0.6 parameter partial transparency set karta hai, jisse legibility "
                    "improve hoti hai jab kisi dense region mein bahut saare points overlap kar "
                    "rahe ho.",
            },
            {
                "technical":
                    "plt.xlabel/ylabel/title annotate the figure with descriptive text, so the "
                    "saved image is self-explanatory without requiring the reader to consult the "
                    "source code.",
                "hinglish":
                    "plt.xlabel/ylabel/title figure ko descriptive text se annotate karte hai, "
                    "taaki saved image khud-explanatory ho aur reader ko samajhne ke liye source "
                    "code dekhne ki zaroorat na pade.",
            },
            {
                "technical":
                    "plt.legend() renders the colour-key box, sourcing its labels from the "
                    "label= keyword argument supplied to each preceding plt.scatter() call.",
                "hinglish":
                    "plt.legend() colour-key box render karta hai, jiske labels har pehle wale "
                    "plt.scatter() call ko diye gaye label= keyword argument se aate hai.",
            },
            {
                "technical":
                    "@@(b) Bar plot: survival counts by sex@@\n\n"
                    "A bar plot is the appropriate chart for comparing aggregate counts across a "
                    "small number of discrete categories — unlike a scatter plot, it does not "
                    "require two numeric axes. Since Sex (male/female) and Survived (0/1) are "
                    "both categorical, tabulating passenger counts per combination and rendering "
                    "one bar per combination is the natural visualization.",
                "hinglish":
                    "@@(b) Bar plot: Sex ke hisaab se survival counts@@\n\n"
                    "Bar plot ek chhoti si list of discrete categories ke across aggregate counts "
                    "compare karne ke liye sahi chart hai — scatter plot ke ulat, isme do numeric "
                    "axes ki zaroorat nahi hoti. Chunki Sex (male/female) aur Survived (0/1) dono "
                    "categorical hai, har combination ke passenger counts tabulate karke ek bar "
                    "per combination render karna hi natural visualization hai.",
            },
            {
                "technical":
                    'pd.crosstab(a, b) builds a contingency table: for every unique combination '
                    "of a's values (rows) and b's values (columns), it counts matching rows in "
                    "the source data. Here it produces a Sex × Survived contingency table of "
                    "passenger counts.",
                "hinglish":
                    "pd.crosstab(a, b) ek contingency table banata hai: a ki values (rows) aur b "
                    "ki values (columns) ke har unique combination ke liye, ye source data mein "
                    "matching rows count karta hai. Yahan ye Sex × Survived ka ek contingency "
                    "table banata hai jisme passenger counts hote hai.",
            },
            {
                "technical":
                    "DataFrame.plot(kind=\"bar\", ...) is a pandas convenience wrapper around "
                    "matplotlib that draws one group of bars per row of the table (one group for "
                    "\"female\", one for \"male\"), with one bar per column within each group.",
                "hinglish":
                    "DataFrame.plot(kind=\"bar\", ...) ek pandas convenience wrapper hai jo "
                    "matplotlib ko internally call karta hai aur table ki har row ke liye bars ka "
                    "ek group draw karta hai (\"female\" ke liye ek group, \"male\" ke liye ek), "
                    "har group ke andar har column ke liye ek bar.",
            },
            {
                "technical":
                    'plt.gca() ("get current axes") directs pandas to draw onto the figure '
                    "canvas already opened via plt.figure() above, rather than implicitly "
                    "creating a separate figure.",
                "hinglish":
                    'plt.gca() ("get current axes") pandas ko batata hai ki upar plt.figure() se '
                    "khole gaye figure canvas par hi draw kare, kisi alag figure ko implicitly "
                    "create karne ke bajaye.",
            },
            {
                "technical":
                    "@@(c) Histogram: distribution of passenger Age@@\n\n"
                    "A histogram is the appropriate chart for visualizing the distribution — "
                    "shape and spread — of a single numeric variable. It partitions the value "
                    "range into equal-width bins and renders a bar per bin proportional to the "
                    "count of observations falling within it, revealing structure (skewness, "
                    "modality, spread) that a summary statistic alone cannot convey.",
                "hinglish":
                    "@@(c) Histogram: passenger Age ki distribution@@\n\n"
                    "Histogram ek single numeric variable ki distribution — shape aur spread — "
                    "visualize karne ke liye sahi chart hai. Ye value range ko equal-width bins "
                    "mein baant deta hai aur har bin ke liye ek bar draw karta hai jo us bin mein "
                    "aane wali observations ke count ke proportional hoti hai — isse structure "
                    "(skewness, modality, spread) dikhta hai jo akela summary statistic nahi "
                    "dikha sakta.",
            },
            {
                "technical":
                    "plt.hist(data, bins=20, ...) partitions the Age values into 20 equal-width "
                    "bins spanning the full observed range, and counts observations per bin.",
                "hinglish":
                    "plt.hist(data, bins=20, ...) Age values ko poore observed range mein 20 "
                    "equal-width bins mein baant deta hai, aur har bin mein observations count "
                    "karta hai.",
            },
            {
                "technical":
                    "@@(d) Line plot: average Fare by passenger class@@\n\n"
                    "A line plot is appropriate when the x-axis has a natural ordering and the "
                    "goal is to depict a trend across that order — canonically a value changing "
                    "over time, but any ordinal axis qualifies. Pclass (1st/2nd/3rd) is ordinal "
                    "even without a time dimension, so plotting average Fare against ordered "
                    "class is a valid, meaningful use of a line plot.",
                "hinglish":
                    "@@(d) Line plot: passenger class ke hisaab se average Fare@@\n\n"
                    "Line plot tab sahi hota hai jab x-axis ka koi natural ordering ho aur goal "
                    "us order ke across ek trend dikhana ho — classic example time ke saath "
                    "badalti value hai, lekin koi bhi ordinal axis qualify karta hai. Pclass "
                    "(1st/2nd/3rd) bina kisi time dimension ke bhi ordinal hai, isliye ordered "
                    "class ke against average Fare plot karna line plot ka ek valid, meaningful "
                    "use hai.",
            },
            {
                "technical":
                    'df.groupby("Pclass")["Fare"].mean() groups observations by their Pclass '
                    "value and computes the within-group mean Fare. .sort_index() enforces "
                    "ascending class order (1, 2, 3), which matters because a line plot's entire "
                    "purpose is to depict a trend along an ordered axis.",
                "hinglish":
                    'df.groupby("Pclass")["Fare"].mean() observations ko unke Pclass value ke '
                    "hisaab se group karta hai aur har group ka mean Fare calculate karta hai. "
                    ".sort_index() classes ko ascending order (1, 2, 3) mein le aata hai, jo "
                    "zaroori hai kyunki line plot ka pura purpose hi ek ordered axis ke along "
                    "trend dikhana hota hai.",
            },
            {
                "technical":
                    "marker=\"o\" renders an explicit marker at every actual data point along "
                    "the line, making each class's exact value identifiable rather than only "
                    "showing an unmarked interpolated line.",
                "hinglish":
                    "marker=\"o\" line ke har actual data point par ek explicit marker render "
                    "karta hai, jisse har class ki exact value pehchani ja sakti hai, sirf ek "
                    "bina-marker wali interpolated line dikhane ke bajaye.",
            },
            {
                "technical":
                    "The x-axis ticks are constrained to the actual class values (1, 2, 3) "
                    "rather than allowing matplotlib to auto-generate fractional ticks (1.5, "
                    "2.5, ...), since Pclass is inherently a small set of discrete integers.",
                "hinglish":
                    "x-axis ke ticks ko actual class values (1, 2, 3) tak hi constrain kiya gaya "
                    "hai, matplotlib ko fractional ticks (1.5, 2.5, ...) auto-generate karne "
                    "dene ke bajaye, kyunki Pclass inherently discrete integers ka ek chhota set "
                    "hai.",
            },
        ],

        "question-2": [
            {
                "technical":
                    "Series.quantile(0.25) and .quantile(0.75) compute Q1 and Q3 directly, using "
                    "pandas' built-in percentile-interpolation implementation, rather than "
                    "requiring a manual sort-and-index computation.",
                "hinglish":
                    "Series.quantile(0.25) aur .quantile(0.75) Q1 aur Q3 seedhe compute karte "
                    "hai, pandas ke built-in percentile-interpolation implementation ka use "
                    "karke — manually sort-aur-index karne ki zaroorat nahi padti.",
            },
            {
                "technical":
                    'This boolean-filters df down to rows where the column value lies outside '
                    "[lower_bound, upper_bound] — the \"|\" operator is Python's element-wise "
                    "logical OR across two boolean Series.",
                "hinglish":
                    "Ye df ko boolean-filter karke sirf unhi rows tak limit karta hai jahan "
                    "column value [lower_bound, upper_bound] range se bahar ho — \"|\" operator "
                    "do boolean Series ke beech Python ka element-wise logical OR hai.",
            },
            {
                "technical": "@@Numeric variable 1: Age@@",
                "hinglish": "@@Numeric variable 1: Age@@",
            },
            {
                "technical": "@@Numeric variable 2: Fare@@",
                "hinglish": "@@Numeric variable 2: Fare@@",
            },
            {
                "technical": "@@Rendering the box plots the assignment requires@@",
                "hinglish": "@@Assignment mein maange gaye box plots draw karna@@",
            },
            {
                "technical":
                    "plt.subplots(1, 2, ...) constructs a single figure containing a 1×2 grid of "
                    "axes, enabling the Age and Fare box plots to be rendered side by side within "
                    "one image for direct visual comparison.",
                "hinglish":
                    "plt.subplots(1, 2, ...) ek hi figure banata hai jisme 1×2 grid of axes "
                    "hoti hai, jisse Age aur Fare ke box plots ek hi image mein side by side "
                    "render ho jaate hai direct visual comparison ke liye.",
            },
            {
                "technical":
                    "axes[0].boxplot([...]) renders the Age column's box plot in the first "
                    "(leftmost) axes. dropna() strips any missing values prior to plotting "
                    "(a defensive no-op here, since Lab Assignment 1's cleaning already "
                    "eliminated them). Box plots default to a vertical orientation, so no "
                    "explicit orientation argument is required.",
                "hinglish":
                    "axes[0].boxplot([...]) pehli (leftmost) axes mein Age column ka box plot "
                    "render karta hai. dropna() plotting se pehle koi bhi missing values hata "
                    "deta hai (yahan ye ek defensive no-op hai, kyunki Lab Assignment 1 ki "
                    "cleaning unhe pehle hi hata chuki hai). Box plots default roop se vertical "
                    "orientation mein hote hai, isliye koi explicit orientation argument dene ki "
                    "zaroorat nahi.",
            },
            {
                "technical":
                    "@@Additionally visualizing exactly which points were flagged, overlaid on "
                    "the full data@@\n\n"
                    "This second figure makes the flagged outliers unambiguous by plotting every "
                    "passenger's Age/Fare as a faint grey point, then overplotting the flagged "
                    "outlier rows in a distinct colour — making it immediately clear which "
                    "specific records were flagged, and by which variable.",
                "hinglish":
                    "@@Ye bhi dikhana ki exactly kaunse points flag hue, poore data ke upar@@\n\n"
                    "Ye doosri figure flagged outliers ko bilkul clear kar deti hai — har "
                    "passenger ke Age/Fare ko ek halke grey point ke roop mein plot karke, fir "
                    "flagged outlier rows ko ek alag colour mein upar se plot karke — isse turant "
                    "saaf ho jaata hai ki kaunse specific records flag hue, aur kis variable ki "
                    "wajah se.",
            },
        ],

        "question-3": [
            {
                "technical": "@@Check 1: Do any missing values remain?@@",
                "hinglish": "@@Check 1: Kya koi missing values abhi bhi bache hai?@@",
            },
            {
                "technical": "@@Check 2: Do any duplicate records remain?@@",
                "hinglish": "@@Check 2: Kya koi duplicate records abhi bhi bache hai?@@",
            },
            {
                "technical": "@@Check 3: Are the numeric values valid (logically possible)?@@",
                "hinglish": "@@Check 3: Kya numeric values valid hai (logically possible)?@@",
            },
            {
                "technical":
                    'A count or a monetary amount is "valid" only if non-negative. '
                    '(df["Fare"] < 0) produces a boolean Series, True wherever Fare is negative; '
                    ".sum() aggregates this into a count of invalid rows.",
                "hinglish":
                    'Ek count ya monetary amount tabhi "valid" hai jab wo non-negative ho. '
                    '(df["Fare"] < 0) ek boolean Series banata hai, jo True hota hai jahan bhi '
                    "Fare negative ho; .sum() ise aggregate karke invalid rows ka count de deta "
                    "hai.",
            },
            {
                "technical": "@@Check 4: Do categorical variables contain only valid categories?@@",
                "hinglish": "@@Check 4: Kya categorical variables mein sirf valid categories hai?@@",
            },
            {
                "technical":
                    "For each categorical column, the complete set of legitimately allowed "
                    "values is defined from domain knowledge (what the Titanic dataset's "
                    "documentation specifies), and the observed values are checked for anything "
                    "outside that set.",
                "hinglish":
                    "Har categorical column ke liye, domain knowledge se (Titanic dataset ki "
                    "documentation jo bataati hai us hisaab se) legitimately allowed values ka "
                    "poora set define kiya jaata hai, aur observed values ko check kiya jaata hai "
                    "ki us set se bahar to kuch nahi hai.",
            },
            {
                "technical":
                    'set(df["Sex"].unique()) collects the distinct values actually present in '
                    "the Sex column into a set (an unordered collection with no duplicates), "
                    "enabling a direct comparison against the allowed set.",
                "hinglish":
                    'set(df["Sex"].unique()) Sex column mein actually present distinct values ko '
                    "ek set (ek unordered collection jisme duplicates nahi hote) mein collect "
                    "karta hai, jisse allowed set ke against direct comparison ki ja sake.",
            },
            {
                "technical":
                    'The "-" (difference) operator between two sets returns every element of '
                    "the first set absent from the second — i.e., which observed values are NOT "
                    "in the allowed list. An empty result confirms validity.",
                "hinglish":
                    'Do sets ke beech "-" (difference) operator pehle set ka har wo element '
                    "return karta hai jo doosre set mein absent hai — matlab, kaunsi observed "
                    "values allowed list mein NAHI hai. Empty result validity confirm karta hai.",
            },
            {
                "technical": "@@Check 5: Are date fields correctly formatted?@@",
                "hinglish": "@@Check 5: Kya date fields sahi format mein hai?@@",
            },
            {
                "technical": "@@Check 6: Do values fall within reasonable, domain-specific ranges?@@",
                "hinglish": "@@Check 6: Kya values reasonable, domain-specific ranges ke andar hai?@@",
            },
            {
                "technical":
                    "No verified human lifespan on record exceeds ~122 years, and this dataset "
                    "describes a 1912 passenger voyage, so any Age exceeding roughly 100 would be "
                    "highly implausible; Age is also, trivially, non-negative by domain "
                    "definition.",
                "hinglish":
                    "Koi bhi verified human lifespan record par ~122 saal se zyada nahi hai, aur "
                    "ye dataset 1912 ke ek passenger voyage ka hai, isliye roughly 100 se zyada "
                    "koi bhi Age highly implausible hogi; Age domain-definition ke hisaab se "
                    "trivially non-negative bhi honi chahiye.",
            },
            {
                "technical":
                    "Fare cannot be negative by definition. As an additional sanity bound, the "
                    "highest documented genuine Titanic fare (a first-class parlour suite) was "
                    "approximately 512; a generous margin of 600 above the known historical "
                    "maximum is used as the upper threshold here.",
                "hinglish":
                    "Fare definition ke hisaab se negative nahi ho sakta. Ek additional sanity "
                    "bound ke roop mein, sabse zyada documented genuine Titanic fare (ek "
                    "first-class parlour suite) approximately 512 tha; yahan known historical "
                    "maximum se upar ek generous margin ke roop mein 600 ko upper threshold "
                    "banaya gaya hai.",
            },
            {
                "technical":
                    "Pclass is constrained by domain definition to {1, 2, 3} — no fourth class "
                    "exists in this schema.",
                "hinglish":
                    "Pclass domain-definition ke hisaab se sirf {1, 2, 3} tak hi constrained hai "
                    "— is schema mein koi 4th class exist hi nahi karti.",
            },
        ],

        "question-4": [
            {
                "technical":
                    "@@(a) Min-Max normalization@@",
                "hinglish":
                    "@@(a) Min-Max normalization@@",
            },
            {
                "technical":
                    "MinMaxScaler() instantiates a stateful transformer object: .fit(...) learns "
                    "the column's min/max from the training data, and .transform(...) applies "
                    "that learned scaling. .fit_transform(...) is a convenience method performing "
                    "both steps in one call.",
                "hinglish":
                    "MinMaxScaler() ek stateful transformer object banata hai: .fit(...) "
                    "training data se column ka min/max seekhta hai, aur .transform(...) us "
                    "seekhe hue scaling ko apply karta hai. .fit_transform(...) ek convenience "
                    "method hai jo dono steps ek hi call mein kar deta hai.",
            },
            {
                "technical":
                    "df[columns_to_scale] projects the selected 4 columns as their own "
                    "sub-DataFrame. fit_transform(...) on this returns a plain NumPy array of "
                    "scaled values (not a pandas object), which is immediately wrapped back into "
                    "a labeled DataFrame via pd.DataFrame(..., columns=...).",
                "hinglish":
                    "df[columns_to_scale] selected 4 columns ko unke apne sub-DataFrame ke roop "
                    "mein project karta hai. Is par fit_transform(...) call karne se scaled "
                    "values ka ek plain NumPy array return hota hai (pandas object nahi), jise "
                    "turant pd.DataFrame(..., columns=...) se wapas ek labeled DataFrame mein "
                    "wrap kar diya jaata hai.",
            },
            {
                "technical":
                    "@@(b) Standardization@@",
                "hinglish":
                    "@@(b) Standardization@@",
            },
        ],

        "wrapup": [],
    },

    # ============================================================
    # LAB ASSIGNMENT 3 — Data Smoothing, Z-score Outlier Removal,
    # and Normalization
    # ============================================================
    3: {

        "setup": [
            {
                "technical": "@@STEP 0: IMPORT THE REQUIRED LIBRARIES@@",
                "hinglish": "@@STEP 0: ZAROORI LIBRARIES IMPORT KARNA@@",
            },
            {
                "technical":
                    "The ready-made scalers required for Question 3 are imported from "
                    "scikit-learn. Two of the seven normalization techniques have no ready-made "
                    "scikit-learn transformer, so those two are implemented by hand from their "
                    "formulas instead — each is explained in full immediately before its use.",
                "hinglish":
                    "Question 3 ke liye zaroori ready-made scalers scikit-learn se import kiye "
                    "gaye hai. Saat normalization techniques mein se do ke liye koi ready-made "
                    "scikit-learn transformer nahi hai, isliye unhe unke formulas se hand-se "
                    "implement kiya gaya hai — har ek ko uske use hone se pehle hi poori tarah "
                    "explain kiya gaya hai.",
            },
            {
                "technical":
                    "A large display.width forces a wide table to always render as one line per "
                    "row, rather than pandas splitting it into two confusing stacked blocks.",
                "hinglish":
                    "Ek bada display.width wide table ko hamesha ek hi line-per-row mein render "
                    "hone ke liye force karta hai, pandas ise do confusing stacked blocks mein "
                    "todne ke bajaye.",
            },
            {
                "technical": "@@STEP 0b: RELIABLE FILE PATHS + A PLOTS DIRECTORY@@",
                "hinglish": "@@STEP 0b: RELIABLE FILE PATHS + EK PLOTS DIRECTORY@@",
            },
            {
                "technical": "@@STEP 0c: LOAD THE PRE-CLEANED DATASET@@",
                "hinglish": "@@STEP 0c: PRE-CLEANED DATASET LOAD KARNA@@",
            },
        ],

        "question-1": [
            {
                "technical":
                    "range(0, n, bin_size) generates 0, bin_size, 2×bin_size, 3×bin_size, ..., up "
                    "to n — i.e., the starting index of every bin.",
                "hinglish":
                    "range(0, n, bin_size) 0, bin_size, 2×bin_size, 3×bin_size, ..., n tak "
                    "generate karta hai — matlab har bin ka starting index.",
            },
            {
                "technical":
                    "end marks the starting index of the next bin (or the array's true end for "
                    "the final, potentially smaller, leftover bin). Python's slicing safely caps "
                    "at the array's actual length even if end technically exceeds it.",
                "hinglish":
                    "end agle bin ka starting index batata hai (ya last, potentially chhote, "
                    "leftover bin ke liye array ka asli end). Python ki slicing safely array ki "
                    "actual length tak hi limit rehti hai, chahe end technically usse zyada ho.",
            },
            {
                "technical":
                    "This slice extracts exactly the values belonging to the current bin.",
                "hinglish":
                    "Ye slice current bin ki exactly wahi values nikaalta hai jo usme belong "
                    "karti hai.",
            },
            {
                "technical":
                    "The computed mean/median value is broadcast into every position within this "
                    "bin.",
                "hinglish":
                    "Calculate kiya gaya mean/median value is bin ke andar har position mein "
                    "broadcast (bhar diya) kar diya jaata hai.",
            },
            {
                "technical":
                    "For bin-boundary smoothing, each value must be individually compared to "
                    "determine whether it is nearer to bin_min or bin_max.",
                "hinglish":
                    "Bin-boundary smoothing ke liye, har value ko individually compare karna "
                    "padta hai ye decide karne ke liye ki wo bin_min ke zyada kareeb hai ya "
                    "bin_max ke.",
            },
            {
                "technical":
                    "@@A small, hand-calculation-style worked example first@@",
                "hinglish":
                    "@@Pehle ek chhota, hand-calculation-jaisa worked example@@",
            },
            {
                "technical":
                    "A small, sorted sample of 12 real Fare values is deliberately selected here, "
                    "purely so the printed figures below stay short enough to verify by manual "
                    "inspection — the same convention any textbook worked example follows.",
                "hinglish":
                    "Yahan jaan-boojh kar 12 real Fare values ka ek chhota, sorted sample select "
                    "kiya gaya hai, sirf isliye taaki neeche print hone wale numbers manual "
                    "inspection se verify karne layak chhote rahein — bilkul jaise kisi textbook "
                    "ka worked example follow karta hai.",
            },
            {
                "technical":
                    "@@Now applying the same 3 techniques across the entire Fare column, and "
                    "plotting the result@@",
                "hinglish":
                    "@@Ab yehi 3 techniques poore Fare column par apply karke, result plot karna@@",
            },
            {
                "technical":
                    'The plot uses a plain 0, 1, 2, 3, ... position index on the x-axis (this is '
                    'just "a passenger\'s rank once fares are sorted", not a real-world '
                    "quantity) — the standard way to visualize smoothing, since it directly shows "
                    "how each technique flattens the sorted line's natural jaggedness into "
                    'discrete "steps".',
                "hinglish":
                    "Plot x-axis par ek plain 0, 1, 2, 3, ... position index use karta hai (ye "
                    'bas "fares sort hone ke baad ek passenger ka rank" hai, koi real-world '
                    "quantity nahi) — smoothing visualize karne ka standard tarika, kyunki ye "
                    "seedhe dikhata hai ki har technique sorted line ki natural jaggedness ko "
                    'discrete "steps" mein kaise flatten karti hai.',
            },
            {
                "technical":
                    'A zoomed-in view (the first 100 sorted passengers) makes each technique\'s '
                    '"staircase" shape substantially easier to inspect, since the full-column '
                    "plot compresses all 891 points into a small image, obscuring fine detail.",
                "hinglish":
                    'Ek zoomed-in view (pehle 100 sorted passengers) har technique ki "staircase" '
                    "shape ko dekhna kaafi aasan bana deti hai, kyunki full-column plot saare "
                    "891 points ko ek chhoti image mein compress kar deta hai, jisse fine detail "
                    "chhup jaati hai.",
            },
        ],

        "question-2": [
            {
                "technical":
                    "Both numeric columns most likely to contain genuine extreme values are "
                    "checked: Age and Fare — the same two columns Lab Assignment 2 already "
                    "flagged as containing IQR-based outliers, now re-examined under a different "
                    "detection method.",
                "hinglish":
                    "Dono numeric columns check kiye jaate hai jinme genuine extreme values "
                    "hone ka sabse zyada chance hai: Age aur Fare — wahi do columns jo Lab "
                    "Assignment 2 ne pehle hi IQR-based outliers ke roop mein flag kiye the, ab "
                    "ek alag detection method ke through dobara examine kiye ja rahe hai.",
            },
            {
                "technical":
                    '"|" between two boolean columns is Python\'s element-wise logical OR - so a '
                    "row is marked an outlier if EITHER its Age Z-score OR its Fare Z-score is "
                    "extreme.",
                "hinglish":
                    '"|" do boolean columns ke beech Python ka element-wise logical OR hai — to '
                    "koi row outlier tab mark hoti hai jab uska Age Z-score YA Fare Z-score, "
                    "in dono mein se koi bhi extreme ho.",
            },
            {
                "technical":
                    'The "~" (bitwise NOT / logical negation) operator inverts the boolean mask, '
                    "retaining only rows NOT flagged as outliers — precisely the removal step the "
                    'question requires. The result is assigned to a NEW variable so the original '
                    '"df" (outliers still included) remains available for comparison.',
                "hinglish":
                    '"~" (bitwise NOT / logical negation) operator boolean mask ko invert kar '
                    "deta hai, sirf wahi rows rakhta hai jo outlier flag NAHI hui hai — bilkul "
                    "wahi removal step jo question maangta hai. Result ko ek NAYE variable mein "
                    'assign kiya jaata hai taaki original "df" (jisme outliers abhi bhi hai) '
                    "comparison ke liye available rahe.",
            },
            {
                "technical":
                    "A visual sanity check renders the Fare distribution before and after "
                    "outlier removal side by side, making the shrinkage of the extreme "
                    "right-hand tail directly observable.",
                "hinglish":
                    "Ek visual sanity check outlier removal se pehle aur baad ki Fare "
                    "distribution ko side by side render karta hai, jisse extreme right-hand "
                    "tail ka shrink hona directly dikh jaata hai.",
            },
        ],

        "question-3": [
            {
                "technical":
                    "Age and Fare are the columns scaled — the same two genuine continuous "
                    "measurement columns used throughout this assignment series, for the reasons "
                    "already established in Lab Assignment 2 (SibSp/Parch are low-cardinality "
                    "integer counts with limited spread; Pclass/Sex/Embarked are categorical, not "
                    "true continuous measurements).",
                "hinglish":
                    "Age aur Fare hi wo columns hai jo scale kiye jaate hai — wahi do genuine "
                    "continuous measurement columns jo is poori assignment series mein use hue "
                    "hai, Lab Assignment 2 mein establish ki gayi wajahon se (SibSp/Parch "
                    "low-cardinality integer counts hai limited spread ke saath; Pclass/Sex/"
                    "Embarked categorical hai, true continuous measurements nahi).",
            },
            {
                "technical":
                    "This dictionary accumulates every scaled version of the data, so a final "
                    "side-by-side comparison table can be printed at the end.",
                "hinglish":
                    "Ye dictionary data ke har scaled version ko accumulate karti hai, taaki "
                    "aakhir mein ek final side-by-side comparison table print ki ja sake.",
            },
            {
                "technical": "@@(a) Min-Max normalization@@",
                "hinglish": "@@(a) Min-Max normalization@@",
            },
            {
                "technical": "@@(b) Mean normalization@@",
                "hinglish": "@@(b) Mean normalization@@",
            },
            {
                "technical": "@@(c) Z-score method (standardization)@@",
                "hinglish": "@@(c) Z-score method (standardization)@@",
            },
            {
                "technical": "@@(d) Decimal scaling@@",
                "hinglish": "@@(d) Decimal scaling@@",
            },
            {
                "technical":
                    "math.log10(max_abs_value) yields the approximate order of magnitude — "
                    "roughly, the digit count — of the value (e.g., log10(512) ≈ 2.7). "
                    "math.floor(...) + 1 converts this into the correct integer digit count "
                    "(e.g., 3 for 512). A guard against max_abs_value being 0 prevents an "
                    "undefined log10(0) call.",
                "hinglish":
                    "math.log10(max_abs_value) value ka approximate order of magnitude deta hai "
                    "— roughly, digits ki count (jaise, log10(512) ≈ 2.7). math.floor(...) + 1 "
                    "ise sahi integer digit count mein convert kar deta hai (jaise, 512 ke liye "
                    "3). max_abs_value ke 0 hone ke against ek guard lagaya gaya hai taaki "
                    "undefined log10(0) call na ho.",
            },
            {
                "technical": "@@(e) Log transformer@@",
                "hinglish": "@@(e) Log transformer@@",
            },
            {
                "technical":
                    "np.log1p(x) computes natural_log(x + 1) directly, in a single, numerically "
                    "safe operation.",
                "hinglish":
                    "np.log1p(x) natural_log(x + 1) ko seedhe, ek single, numerically safe "
                    "operation mein calculate kar deta hai.",
            },
            {
                "technical": "@@(f) MaxAbs transformer@@",
                "hinglish": "@@(f) MaxAbs transformer@@",
            },
            {
                "technical": "@@(g) Interquartile / Robust scaler@@",
                "hinglish": "@@(g) Interquartile / Robust scaler@@",
            },
            {
                "technical":
                    "Final side-by-side comparison (Fare only, since it is the more skewed, "
                    "more outlier-prone of the two columns, making differences most visible).",
                "hinglish":
                    "Final side-by-side comparison (sirf Fare, kyunki ye dono columns mein "
                    "zyada skewed aur zyada outlier-prone hai, isliye differences sabse zyada "
                    "clearly dikhte hai).",
            },
            {
                "technical":
                    "A bar chart compares how each technique reshapes the Fare column's mean and "
                    "standard deviation, making the differences visible at a glance.",
                "hinglish":
                    "Ek bar chart compare karta hai ki har technique Fare column ke mean aur "
                    "standard deviation ko kaise reshape karti hai, jisse differences ek nazar "
                    "mein dikh jaate hai.",
            },
        ],

        "wrapup": [
            {
                "technical":
                    'A human-readable name such as "Log Transform (log1p)" is converted into a '
                    'filesystem-safe filename such as "Log_Transform_log1p" (no spaces, '
                    "brackets, or other characters a filename cannot contain).",
                "hinglish":
                    'Ek human-readable naam jaise "Log Transform (log1p)" ko ek filesystem-safe '
                    'filename jaise "Log_Transform_log1p" mein convert kiya jaata hai (koi '
                    "spaces, brackets, ya aise characters nahi jo ek filename mein allowed nahi "
                    "hote).",
            },
        ],
    },

}
