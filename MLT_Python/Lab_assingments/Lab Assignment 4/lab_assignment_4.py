"""
==================================================================================
 LAB ASSIGNMENT 4 - Feature Selection: Correlation, Redundancy, and Distance/Similarity Measures
==================================================================================

WHAT IS THIS FILE, AND WHO IS IT FOR?
----------------------------------------
Same style as Lab Assignments 1-3: a plain Python script written for a
complete beginner who has never touched Python, pandas, matplotlib, or
scikit-learn before. Every step is explained in plain English before the
code that does it, plus short "#" comments on the important lines.

WHERE DOES THE DATA COME FROM, AND HOW DO THE 4 QUESTIONS CONNECT?
------------------------------------------------------------------
This assignment is about FEATURE SELECTION (deciding which columns of a
dataset are actually useful, and which are wasteful/duplicated) - this is
a completely different topic from cleaning (Lab 1), scaling (Lab 2), or
smoothing/outlier-removal (Lab 3), so we start fresh from Lab Assignment
1's cleaned CSV (not from Lab 3's outlier-removed or scaled versions -
feature selection here works on the whole cleaned dataset, and this
script does its own standardization later, exactly where it's needed).

    Lab Assignment 1 -> cleaned the raw Titanic data (this is what we load)
    Lab Assignment 4 (THIS FILE) ->
        SETUP : turns the two text/category columns ('Sex', 'Embarked')
                into numeric 0/1 columns, since correlation and all the
                distance/similarity formulas below only work on numbers
        Q1    : builds and visualizes the CORRELATION MATRIX of every
                feature against every other feature
        Q2    : scans that same correlation matrix for any PAIR of
                features that are "highly correlated" (i.e. saying
                almost the same thing)
        Q3    : REMOVES one feature from each highly-correlated pair
                found in Q2, producing a smaller, non-redundant feature
                set
        Q4    : goes back to the ORIGINAL feature list (before Q3's
                removal) and measures how similar/different every pair
                of features is using 6 different distance/similarity
                formulas from the lecture notes (Euclidean, Manhattan,
                Hamming, Cosine, Jaccard, SMC) - a second, independent
                way of spotting redundant features, from a totally
                different angle than plain correlation

So Q1 -> Q2 -> Q3 is one connected pipeline (correlation-based redundancy
removal), while Q4 is a separate, parallel demonstration of 6 more
redundancy-measuring techniques applied to the same dataset, so you can
compare what each technique flags.

We load the already-cleaned CSV that Lab Assignment 1 produced:
    ../Lab Assignment 1/Titanic-Dataset-Cleaned.csv
Make sure you have run Lab Assignment 1's script at least once already, so
that file exists.

HOW TO RUN THIS FILE
----------------------
1. Make sure Python 3 is installed.
2. Make sure these libraries are installed (run once, if needed):
        pip install pandas numpy matplotlib scikit-learn
3. Run this script from inside THIS folder ("Lab Assignment 4"):
        python3 lab_assignment_4.py
   It prints all explanations and tables to the terminal, saves every
   chart as a ".png" image inside a new "plots" folder next to this
   script, and saves the final, redundancy-free feature set as a CSV
   file at the end.

==================================================================================
"""

# ----------------------------------------------------------------------------
# STEP 0: IMPORT THE LIBRARIES WE NEED
# ----------------------------------------------------------------------------
import os                      # for building reliable file paths
import numpy as np             # numpy = "Numerical Python" - a toolbox for fast maths on lists of numbers (arrays)
import pandas as pd            # our table/DataFrame toolbox, as in every earlier assignment
import matplotlib.pyplot as plt  # our charting toolbox, as in Lab Assignments 2 and 3

# From scikit-learn, we import StandardScaler - the same Z-score scaling
# tool used in Lab Assignment 3, needed here so that Euclidean/Manhattan/
# Cosine distances in Question 4 aren't unfairly dominated by whichever
# original column happens to have the biggest raw numbers (e.g. 'Fare').
from sklearn.preprocessing import StandardScaler

# A very large "display.width" makes a wide table always print as ONE line
# per row, instead of pandas splitting it into two confusing stacked blocks.
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


def section(title):
    """Prints a clear section heading. See Lab Assignment 1 for a full
    explanation of what a Python function/def is."""
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)


# ----------------------------------------------------------------------------
# STEP 0b: RELIABLE FILE PATHS + A FOLDER TO SAVE PLOTS INTO
# ----------------------------------------------------------------------------
this_script_folder = os.path.dirname(os.path.abspath(__file__))
cleaned_csv_path = os.path.join(
    this_script_folder, "..", "Lab Assignment 1", "Titanic-Dataset-Cleaned.csv"
)
plots_folder = os.path.join(this_script_folder, "plots")
os.makedirs(plots_folder, exist_ok=True)


def save_current_plot(filename):
    """Saves whatever chart is currently drawn to an image file inside our
    'plots' folder, then clears the canvas so the next chart starts fresh.
    (Full explanation of every line here is in Lab Assignment 2's script.)"""
    full_path = os.path.join(plots_folder, filename)
    plt.tight_layout()
    plt.savefig(full_path)
    plt.close()
    print(f"  Saved plot -> plots/{filename}")


# ----------------------------------------------------------------------------
# STEP 0c: LOAD THE CLEANED DATASET
# ----------------------------------------------------------------------------
section("LOADING THE CLEANED DATASET FROM LAB ASSIGNMENT 1")

df = pd.read_csv(cleaned_csv_path)
print(f"Loaded cleaned dataset from: {cleaned_csv_path}")
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print("Columns:", list(df.columns))
print(df.head())


# ----------------------------------------------------------------------------
# STEP 0d: TURN THE TWO TEXT COLUMNS INTO NUMBERS
# ----------------------------------------------------------------------------
section("SETUP: ENCODING 'Sex' AND 'Embarked' AS NUMBERS")

print("""
WHY DO WE NEED TO DO THIS FIRST?
Correlation and every distance/similarity formula in this assignment
(Euclidean, Manhattan, Hamming, Cosine, Jaccard, SMC) are all pure MATH
formulas - they only work on numbers, not text. Our cleaned dataset still
has two text ("category") columns: 'Sex' (male/female) and 'Embarked'
(S/C/Q, the port the passenger boarded from). So, before anything else,
we convert both into numeric 0/1 columns:

  'Sex' -> ONE new column, 'Sex_male' (1 = male, 0 = female). Since there
           are only 2 possible values, a single 0/1 column is enough to
           capture the information with no ambiguity.

  'Embarked' -> THREE new columns, one per port: 'Embarked_C',
           'Embarked_Q', 'Embarked_S' (each is 1 if the passenger boarded
           there, 0 otherwise). This standard technique is called
           "ONE-HOT ENCODING" - since Embarked has 3 possible values (not
           2), we need 3 separate 0/1 columns, exactly one of which is 1
           for any given passenger.
""")

encoded_df = df.copy()
encoded_df["Sex_male"] = (encoded_df["Sex"] == "male").astype(int)
encoded_df = pd.get_dummies(encoded_df, columns=["Embarked"], prefix="Embarked")
encoded_df = encoded_df.drop(columns=["Sex"])

# pd.get_dummies() produces True/False boolean columns on modern pandas -
# we convert those to plain 0/1 integers so every downstream formula
# (correlation, distances) sees consistent numeric types throughout.
bool_columns = encoded_df.select_dtypes(include="bool").columns
encoded_df[bool_columns] = encoded_df[bool_columns].astype(int)

print("After encoding, every column is now numeric:")
print(encoded_df.dtypes)
print(f"\nNew shape: {encoded_df.shape[0]} rows x {encoded_df.shape[1]} columns")
print(encoded_df.head())

all_feature_columns = list(encoded_df.columns)


# ==================================================================================
# QUESTION 1: Visualize Correlation Matrix of Features
# ==================================================================================
section("QUESTION 1: VISUALIZE THE CORRELATION MATRIX OF FEATURES")

print("""
WHAT IS A CORRELATION MATRIX?
For every PAIR of numeric columns, the Pearson correlation coefficient
"r" (already covered in the lecture notes on measuring feature
redundancy) measures how strongly the two columns move together:

  r close to +1  -> as one column goes up, the other reliably goes up too
  r close to -1  -> as one column goes up, the other reliably goes down
  r close to  0  -> the two columns show no linear relationship

A "correlation matrix" is simply this "r" value computed for EVERY
possible pair of columns at once, arranged as a square table/grid - the
diagonal is always exactly 1.0 (any column is perfectly correlated with
itself).
""")

correlation_matrix = encoded_df.corr()
print("Full correlation matrix (rounded to 3 decimals):")
print(correlation_matrix.round(3))

# A heatmap is the standard way to VISUALIZE a correlation matrix: each
# cell is colored according to its correlation value, so strong
# relationships (very red or very blue) jump out immediately, without
# having to read every individual number in the table above.
fig, ax = plt.subplots(figsize=(9, 8))
im = ax.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(all_feature_columns)))
ax.set_yticks(range(len(all_feature_columns)))
ax.set_xticklabels(all_feature_columns, rotation=45, ha="right")
ax.set_yticklabels(all_feature_columns)
# Writing the actual number inside each cell (on top of the color) makes
# the heatmap readable precisely, not just "roughly by color".
for i in range(len(all_feature_columns)):
    for j in range(len(all_feature_columns)):
        value = correlation_matrix.iloc[i, j]
        # White text shows up better on the darkest (most saturated) red/
        # blue cells, black text shows up better on the paler, near-zero
        # cells - this simple rule keeps every number readable.
        text_color = "white" if abs(value) > 0.6 else "black"
        ax.text(j, i, f"{value:.2f}", ha="center", va="center",
                color=text_color, fontsize=8)
fig.colorbar(im, ax=ax, label="Pearson correlation (r)")
ax.set_title("Correlation Matrix Heatmap - All Encoded Titanic Features")
save_current_plot("1_correlation_matrix_heatmap.png")

print("""
How to read this heatmap: deep red cells mean strong POSITIVE
correlation, deep blue cells mean strong NEGATIVE correlation, and pale/
white cells near 0 mean the two features are essentially unrelated
(linearly). The diagonal is always deep red (value 1.00) since every
feature is perfectly correlated with itself - that's expected and not
meaningful on its own. Question 2 below digs into which OFF-diagonal
cells are strong enough to matter.
""")


# ==================================================================================
# QUESTION 2: Identify Highly Correlated Features
# ==================================================================================
section("QUESTION 2: IDENTIFY HIGHLY CORRELATED (REDUNDANT) FEATURES")

print("""
WHAT COUNTS AS "HIGHLY CORRELATED"?
There's no single universal cutoff, but a very commonly used rule of
thumb (and the one we use here) is:

    |r| > 0.7   ->   the two features are considered "highly correlated"

The "| |" (absolute value) matters: a correlation of -0.9 is just as
"highly correlated" as +0.9 - the SIGN only tells you the DIRECTION of
the relationship (do they move together or oppositely), while the SIZE
(ignoring sign) tells you the STRENGTH of the relationship, which is what
we actually care about for spotting redundancy.

WHY DOES HIGH CORRELATION MEAN "REDUNDANT"?
If two features are highly correlated, they are carrying almost the SAME
information - so keeping both barely adds anything a model couldn't
already infer from just one of them, while still costing extra
computation and (for many models) potentially causing "multicollinearity"
problems (unstable, hard-to-trust coefficients). This is exactly the
"minimizing redundancy" driver of feature selection from the lecture
notes.
""")


def find_highly_correlated_pairs(corr_matrix, threshold=0.7):
    """
    Scans a correlation matrix (a pandas DataFrame) and returns a list of
    (feature_a, feature_b, correlation_value) tuples for every PAIR of
    DIFFERENT features whose absolute correlation exceeds the threshold.
    Each pair is only returned ONCE (we don't also return the mirror-image
    duplicate, since corr(A,B) is always equal to corr(B,A)).
    """
    columns = corr_matrix.columns
    highly_correlated = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):  # j starts AFTER i, so no self-pairs and no duplicate mirror-pairs
            value = corr_matrix.iloc[i, j]
            if abs(value) > threshold:
                highly_correlated.append((columns[i], columns[j], value))
    return highly_correlated


threshold = 0.7
highly_correlated_pairs = find_highly_correlated_pairs(correlation_matrix, threshold)

print(f"Scanning every feature pair for |r| > {threshold} ...\n")
if highly_correlated_pairs:
    for feature_a, feature_b, value in highly_correlated_pairs:
        print(f"  '{feature_a}'  <->  '{feature_b}'   r = {value:.3f}  (|r| = {abs(value):.3f} > {threshold})")
else:
    print("  No feature pair exceeded the threshold.")

print(f"""
WHY THIS PARTICULAR PAIR SHOWS UP:
'Embarked_C' and 'Embarked_S' come from ONE-HOT ENCODING the same original
column ('Embarked'), which only has 3 possible values (C, Q, S) and every
passenger has EXACTLY ONE of them. Since the S port is by far the most
common (646 of 891 passengers) and C is the second most common, knowing
"this passenger did NOT board at S" already makes it noticeably more
likely they boarded at C (because there are only 2 remaining options, and
C is the bigger one) - hence the strong NEGATIVE correlation between the
two one-hot columns. This is a textbook example of the well-known "dummy
variable trap": whenever you one-hot-encode a category into N columns,
those N columns are never fully independent of each other, because
knowing all-but-one of them already tells you the last one for free.
""")


# ==================================================================================
# QUESTION 3: Remove Redundant Features
# ==================================================================================
section("QUESTION 3: REMOVE REDUNDANT FEATURES")

print("""
HOW DO WE DECIDE *WHICH* FEATURE TO DROP FROM EACH PAIR?
For each highly-correlated pair identified in Question 2, we keep the
feature that is more strongly correlated with 'Survived' (our target/
label column - the thing we'd ultimately want to predict), and drop the
other, since the one more related to the actual outcome we care about is
the more useful one to keep.
""")

target_column = "Survived"
columns_to_drop = []
for feature_a, feature_b, value in highly_correlated_pairs:
    corr_a_with_target = abs(correlation_matrix.loc[feature_a, target_column])
    corr_b_with_target = abs(correlation_matrix.loc[feature_b, target_column])
    if corr_a_with_target >= corr_b_with_target:
        drop_this_one = feature_b
        keep_this_one = feature_a
    else:
        drop_this_one = feature_a
        keep_this_one = feature_b
    columns_to_drop.append(drop_this_one)
    print(f"  Pair ('{feature_a}', '{feature_b}'): "
          f"|corr with Survived| is {corr_a_with_target:.3f} for '{feature_a}' "
          f"vs {corr_b_with_target:.3f} for '{feature_b}' "
          f"-> keeping '{keep_this_one}', dropping '{drop_this_one}'")

reduced_df = encoded_df.drop(columns=columns_to_drop)

print(f"\nColumns BEFORE removal ({len(encoded_df.columns)}): {list(encoded_df.columns)}")
print(f"Columns dropped as redundant: {columns_to_drop}")
print(f"Columns AFTER removal ({len(reduced_df.columns)}): {list(reduced_df.columns)}")

print(f"""
NOTE: Dropping 'Embarked_S' here also happens to match a second, standard
data-preparation practice independent of correlation: when one-hot
encoding a category with N values, it's normal to keep only N-1 of the
dummy columns (dropping any one of them, e.g. Embarked_S), since the
dropped column's value can always be perfectly inferred from the other
N-1 columns being all 0 - keeping all N columns is mathematically
redundant by construction, which is exactly what the correlation-based
removal above caught automatically.
""")


# ==================================================================================
# QUESTION 4: Feature Selection Using Distance/Similarity Measures
# ==================================================================================
section("QUESTION 4: SIX DISTANCE/SIMILARITY MEASURES BETWEEN FEATURES")

print("""
WHAT ARE WE MEASURING HERE, AND WHY?
Questions 1-3 spotted redundant features using CORRELATION. This question
uses 6 DIFFERENT formulas from the lecture notes on measuring feature
redundancy, applied the same way: to compare pairs of FEATURES (whole
columns, not individual passengers) against each other, to see if a
totally different kind of formula agrees with what correlation already
found.

We split the 10 features (from BEFORE Question 3's removal, so we can
compare against the same full set Question 1/2 used) into two groups,
since different formulas suit different kinds of data (this exact
dense-vs-sparse/binary split is in the lecture notes too):

  DENSE, CONTINUOUS features -> Pclass, Age, SibSp, Parch, Fare
      (used for Euclidean, Manhattan, and Cosine)

  BINARY (0/1) features -> Survived, Sex_male, Embarked_C, Embarked_Q,
  Embarked_S
      (used for Hamming, Jaccard, and SMC)

For the 3 dense-feature formulas, we first STANDARDIZE every column (the
same Z-score technique from Lab Assignment 3: subtract the mean, divide
by the standard deviation) - this is essential here, because otherwise
'Fare' (values up to several hundred) would completely dominate the
distance calculations over something like 'Pclass' (values only 1-3),
purely due to its bigger raw numbers, not because it's actually more
different.
""")

dense_feature_names = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
binary_feature_names = ["Survived", "Sex_male", "Embarked_C", "Embarked_Q", "Embarked_S"]

scaler = StandardScaler()
standardized_dense = pd.DataFrame(
    scaler.fit_transform(encoded_df[dense_feature_names]),
    columns=dense_feature_names,
)
binary_features = encoded_df[binary_feature_names]

print("Standardized dense features (first 5 rows):")
print(standardized_dense.head().round(3))
print("\nBinary features (first 5 rows):")
print(binary_features.head())


def pairwise_matrix(feature_names, pair_function):
    """
    Given a list of feature (column) names and a function that computes
    one number for a PAIR of columns, builds and returns the full square
    matrix (as a pandas DataFrame) of that number for every pair of
    features - reused below for all 6 distance/similarity formulas so we
    don't repeat the same looping code 6 times.
    """
    n = len(feature_names)
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            result[i, j] = pair_function(feature_names[i], feature_names[j])
    return pd.DataFrame(result, index=feature_names, columns=feature_names)


def most_extreme_off_diagonal(matrix, find_max=True):
    """Finds the (feature_a, feature_b, value) with the largest (or, if
    find_max=False, smallest) value among all OFF-diagonal cells of a
    square matrix - used to highlight the single most notable pair for
    each of the 6 measures below."""
    best = None
    for i, row_name in enumerate(matrix.index):
        for j, col_name in enumerate(matrix.columns):
            if i == j:
                continue  # skip the diagonal (a feature compared with itself)
            value = matrix.iloc[i, j]
            if best is None or (find_max and value > best[2]) or (not find_max and value < best[2]):
                best = (row_name, col_name, value)
    return best


# ----------------------------------------------------------------------
# 4(i) EUCLIDEAN DISTANCE
# ----------------------------------------------------------------------
print("""
--- (i) EUCLIDEAN DISTANCE ---
Formula: d(A, B) = sqrt( sum( (A_i - B_i)^2 ) )
The "straight-line" distance between two vectors, exactly as covered
(and hand-verified) in the lecture notes' worked example. Here, each
"vector" is one STANDARDIZED dense feature column (891 values long, one
per passenger) - so we're measuring how differently two entire columns
behave ACROSS ALL PASSENGERS AT ONCE, not comparing two individual
passengers to each other.
""")


def euclidean_distance(col_a, col_b):
    a = standardized_dense[col_a].to_numpy()
    b = standardized_dense[col_b].to_numpy()
    return np.sqrt(np.sum((a - b) ** 2))


euclidean_matrix = pairwise_matrix(dense_feature_names, euclidean_distance)
print("Euclidean distance matrix (dense features):")
print(euclidean_matrix.round(3))
closest_pair = most_extreme_off_diagonal(euclidean_matrix, find_max=False)
print(f"\nSMALLEST Euclidean distance (= most similar pair): "
      f"'{closest_pair[0]}' <-> '{closest_pair[1]}'  (distance = {closest_pair[2]:.3f})")


# ----------------------------------------------------------------------
# 4(ii) MANHATTAN DISTANCE
# ----------------------------------------------------------------------
print("""
--- (ii) MANHATTAN DISTANCE ---
Formula: d(A, B) = sum( |A_i - B_i| )
Also called "city-block" distance - instead of the straight diagonal line
(Euclidean), it adds up the absolute differences directly, as if you
could only move along grid streets, never diagonally. It's less sensitive
to any single huge difference than Euclidean is (because differences
aren't squared), so it can rank feature pairs slightly differently.
""")


def manhattan_distance(col_a, col_b):
    a = standardized_dense[col_a].to_numpy()
    b = standardized_dense[col_b].to_numpy()
    return np.sum(np.abs(a - b))


manhattan_matrix = pairwise_matrix(dense_feature_names, manhattan_distance)
print("Manhattan distance matrix (dense features):")
print(manhattan_matrix.round(3))
closest_pair = most_extreme_off_diagonal(manhattan_matrix, find_max=False)
print(f"\nSMALLEST Manhattan distance (= most similar pair): "
      f"'{closest_pair[0]}' <-> '{closest_pair[1]}'  (distance = {closest_pair[2]:.3f})")


# ----------------------------------------------------------------------
# 4(iii) HAMMING DISTANCE
# ----------------------------------------------------------------------
print("""
--- (iii) HAMMING DISTANCE ---
Formula: d(A, B) = (number of positions where A_i != B_i) / total positions
Originally designed for comparing strings/binary codes of equal length -
here, for two binary (0/1) feature columns, it simply counts, passenger
by passenger, how often the two columns DISAGREE (one is 0 and the other
is 1), then divides by the total number of passengers to get a fraction
between 0 (identical on every passenger) and 1 (opposite on every
passenger).
""")


def hamming_distance(col_a, col_b):
    a = binary_features[col_a].to_numpy()
    b = binary_features[col_b].to_numpy()
    disagreements = np.sum(a != b)
    return disagreements / len(a)


hamming_matrix = pairwise_matrix(binary_feature_names, hamming_distance)
print("Hamming distance matrix (binary features):")
print(hamming_matrix.round(3))
closest_pair = most_extreme_off_diagonal(hamming_matrix, find_max=False)
print(f"\nSMALLEST Hamming distance (= most similar pair): "
      f"'{closest_pair[0]}' <-> '{closest_pair[1]}'  (distance = {closest_pair[2]:.3f})")


# ----------------------------------------------------------------------
# 4(iv) COSINE SIMILARITY
# ----------------------------------------------------------------------
print("""
--- (iv) COSINE SIMILARITY ---
Formula: cos(A, B) = (A . B) / (||A|| * ||B||)
Measures the ANGLE between two vectors, ignoring their magnitude/length
entirely - it asks "do these two columns point in the same DIRECTION
across passengers?", not "are their raw sizes similar?". A value of 1
means the two columns point in exactly the same direction (perfectly
similar pattern), 0 means they're at a right angle (unrelated), and -1
means they point in exactly opposite directions.
""")


def cosine_similarity(col_a, col_b):
    a = standardized_dense[col_a].to_numpy()
    b = standardized_dense[col_b].to_numpy()
    dot_product = np.dot(a, b)
    magnitude_a = np.sqrt(np.sum(a ** 2))
    magnitude_b = np.sqrt(np.sum(b ** 2))
    return dot_product / (magnitude_a * magnitude_b)


cosine_matrix = pairwise_matrix(dense_feature_names, cosine_similarity)
print("Cosine similarity matrix (dense features):")
print(cosine_matrix.round(3))
most_similar_pair = most_extreme_off_diagonal(cosine_matrix, find_max=True)
print(f"\nLARGEST Cosine similarity (= most similar pair): "
      f"'{most_similar_pair[0]}' <-> '{most_similar_pair[1]}'  (similarity = {most_similar_pair[2]:.3f})")


# ----------------------------------------------------------------------
# 4(v) JACCARD DISTANCE
# ----------------------------------------------------------------------
print("""
--- (v) JACCARD DISTANCE ---
Formula: distance(A, B) = 1 - [ (A AND B) / (A OR B) ]
The part in [ ] brackets is the "Jaccard coefficient" from the lecture
notes: treating each binary column as a SET of passengers (the ones where
that feature = 1), it's the size of the OVERLAP (passengers where BOTH
features are 1) divided by the size of the UNION (passengers where
EITHER feature is 1). Unlike Hamming, Jaccard completely IGNORES
positions where BOTH columns are 0 together - it only cares about where
at least one of the two columns is "switched on", which is exactly why
it's the standard choice for SPARSE/binary data (see the lecture notes'
dense-vs-sparse grouping).
""")


def jaccard_distance(col_a, col_b):
    a = binary_features[col_a].to_numpy().astype(bool)
    b = binary_features[col_b].to_numpy().astype(bool)
    intersection = np.sum(a & b)
    union = np.sum(a | b)
    if union == 0:
        return 0.0  # both columns are all-zero everywhere - treat as identical (distance 0)
    jaccard_coefficient = intersection / union
    return 1 - jaccard_coefficient


jaccard_matrix = pairwise_matrix(binary_feature_names, jaccard_distance)
print("Jaccard distance matrix (binary features):")
print(jaccard_matrix.round(3))
closest_pair = most_extreme_off_diagonal(jaccard_matrix, find_max=False)
print(f"\nSMALLEST Jaccard distance (= most similar pair): "
      f"'{closest_pair[0]}' <-> '{closest_pair[1]}'  (distance = {closest_pair[2]:.3f})")


# ----------------------------------------------------------------------
# 4(vi) SIMPLE MATCHING COEFFICIENT (SMC)
# ----------------------------------------------------------------------
print("""
--- (vi) SIMPLE MATCHING COEFFICIENT (SMC) ---
Formula: SMC(A, B) = (matches) / (total positions)
                    = (number of positions where A_i == B_i) / total positions
This is the "mirror image" of Hamming distance and the "complete"
counterpart to Jaccard: unlike Jaccard, SMC counts BOTH kinds of
agreement - positions where both columns are 1 AND positions where both
are 0 - as a "match". This makes SMC the right choice when a shared "0"
genuinely means something meaningful for both features (dense/complete
binary data), while Jaccard is better when a shared "0" is just "neither
feature happened to apply here" (sparse binary data) - exactly the
distinction drawn in the lecture notes.
""")


def simple_matching_coefficient(col_a, col_b):
    a = binary_features[col_a].to_numpy()
    b = binary_features[col_b].to_numpy()
    matches = np.sum(a == b)
    return matches / len(a)


smc_matrix = pairwise_matrix(binary_feature_names, simple_matching_coefficient)
print("Simple Matching Coefficient matrix (binary features):")
print(smc_matrix.round(3))
most_similar_pair = most_extreme_off_diagonal(smc_matrix, find_max=True)
print(f"\nLARGEST SMC (= most similar pair): "
      f"'{most_similar_pair[0]}' <-> '{most_similar_pair[1]}'  (SMC = {most_similar_pair[2]:.3f})")

embarked_c_s_hamming = hamming_matrix.loc["Embarked_C", "Embarked_S"]
embarked_c_s_jaccard = jaccard_matrix.loc["Embarked_C", "Embarked_S"]
embarked_c_s_smc = smc_matrix.loc["Embarked_C", "Embarked_S"]

print(f"""
SMC IS EXACTLY "1 - HAMMING DISTANCE":
Look closely at the two matrices above - for any pair of features, SMC
always equals 1 - Hamming_distance(that same pair) (e.g. 'Embarked_C' <->
'Embarked_Q': Hamming = 0.275, SMC = 0.725, and 0.275 + 0.725 = 1.000).
This makes sense from the formulas themselves: Hamming distance counts
the fraction of DISAGREEING positions, SMC counts the fraction of
AGREEING positions, and every position is either agreeing or disagreeing
- so the two always add up to exactly 1, and they will always rank pairs
identically (just "flipped").

AN IMPORTANT DISAGREEMENT WITH CORRELATION:
Question 2 flagged 'Embarked_C' and 'Embarked_S' as "highly correlated"
(r = -0.783). But look at how ALL THREE binary measures score that exact
same pair here: Hamming distance = {embarked_c_s_hamming:.3f} (close to
the maximum of 1 - i.e. very DISSIMILAR), Jaccard distance =
{embarked_c_s_jaccard:.3f} (the absolute maximum possible, 1.000), and
SMC = {embarked_c_s_smc:.3f} (close to the minimum of 0 - again very
DISSIMILAR). So Hamming/Jaccard/SMC all say the OPPOSITE of what
correlation said about this exact pair!

WHY THE DISAGREEMENT IS NOT A MISTAKE - IT'S A DIFFERENCE IN WHAT "SIMILAR"
MEANS: correlation treats a STRONG relationship in EITHER direction
(positive or negative) as "these two carry the same information, hence
redundant" - a passenger who is "not S" is quite predictably "C" here,
which is exactly why r is large in magnitude. Hamming/Jaccard/SMC, on the
other hand, are pure AGREEMENT measures - they only count how often the
two columns show the exact SAME value at the exact same passenger, and
'Embarked_C'/'Embarked_S' almost NEVER show the same value (whenever one
is 1 the other is 0, since a passenger can only board from one port) - so
these measures correctly call them maximally "different", even though
they're still highly (negatively) PREDICTABLE from each other. This is a
genuinely important lesson: "redundant" can mean different things under
different formulas, and a real feature-selection pipeline benefits from
checking more than one kind of measure, exactly as this question does.
""")

# Two side-by-side heatmap panels: dense-feature measures (Euclidean/
# Manhattan/Cosine) on the left group, binary-feature measures (Hamming/
# Jaccard/SMC) on the right group - visualizing all 6 matrices at once.
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
dense_matrices = [
    ("Euclidean Distance", euclidean_matrix, "viridis_r"),
    ("Manhattan Distance", manhattan_matrix, "viridis_r"),
    ("Cosine Similarity", cosine_matrix, "coolwarm"),
]
binary_matrices = [
    ("Hamming Distance", hamming_matrix, "viridis_r"),
    ("Jaccard Distance", jaccard_matrix, "viridis_r"),
    ("Simple Matching Coefficient", smc_matrix, "viridis"),
]
for ax, (title, matrix, cmap) in zip(axes[0], dense_matrices):
    im = ax.imshow(matrix, cmap=cmap)
    ax.set_xticks(range(len(matrix.columns)))
    ax.set_yticks(range(len(matrix.index)))
    ax.set_xticklabels(matrix.columns, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(matrix.index, fontsize=8)
    ax.set_title(title, fontsize=10)
    fig.colorbar(im, ax=ax, fraction=0.046)
for ax, (title, matrix, cmap) in zip(axes[1], binary_matrices):
    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=1)
    ax.set_xticks(range(len(matrix.columns)))
    ax.set_yticks(range(len(matrix.index)))
    ax.set_xticklabels(matrix.columns, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(matrix.index, fontsize=8)
    ax.set_title(title, fontsize=10)
    fig.colorbar(im, ax=ax, fraction=0.046)
fig.suptitle("Question 4: All 6 Distance/Similarity Measures Between Features", fontsize=13)
save_current_plot("4_all_six_distance_similarity_heatmaps.png")


# ==================================================================================
# SAVE THE OUTPUT FILES
# ==================================================================================
section("SAVING OUTPUT FILES")

encoded_path = os.path.join(this_script_folder, "Titanic-Dataset-Encoded.csv")
encoded_df.to_csv(encoded_path, index=False)
print(f"Saved fully-encoded (before redundancy removal) dataset -> {encoded_path}")

reduced_path = os.path.join(this_script_folder, "Titanic-Dataset-FeatureSelected.csv")
reduced_df.to_csv(reduced_path, index=False)
print(f"Saved final, redundancy-free feature-selected dataset -> {reduced_path}")

print(f"\nAll plots were saved inside: {plots_folder}")
print("\nAll 4 questions of Lab Assignment 4 are complete.")
