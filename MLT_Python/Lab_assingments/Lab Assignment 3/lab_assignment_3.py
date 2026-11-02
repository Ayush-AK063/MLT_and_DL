"""
==================================================================================
 LAB ASSIGNMENT 3 - Data Smoothing, Z-score Outlier Removal, and Normalization
==================================================================================

WHAT IS THIS FILE, AND WHO IS IT FOR?
----------------------------------------
Same style as Lab Assignments 1 and 2: a plain Python script written for a
complete beginner who has never touched Python, pandas, matplotlib, or
scikit-learn before. Every step is explained in plain English before the
code that does it, plus short "#" comments on the important lines.

WHERE DOES THE DATA COME FROM, AND HOW DO THE 3 QUESTIONS CONNECT?
------------------------------------------------------------------
This script continues the same pipeline as the earlier assignments:

    Lab Assignment 1 -> cleaned the raw Titanic data (missing values,
                         duplicates, useless columns)
    Lab Assignment 2 -> visualized it, found outliers with a box plot
                         (but did not remove them), validated it, scaled it
    Lab Assignment 3 (THIS FILE) ->
        Q1: demonstrates 3 different SMOOTHING techniques on a numeric
            column (this is a separate, standalone demonstration - it does
            NOT permanently change the main working data, since smoothing
            is being taught here as its own technique, not as a cleaning
            step we need for later questions)
        Q2: detects outliers using the Z-SCORE method (a different method
            than Lab Assignment 2's box-plot/IQR method) and this time
            ACTUALLY REMOVES them, producing a smaller, outlier-free
            dataset
        Q3: takes that outlier-free dataset from Q2 and applies SEVEN
            different normalization/scaling techniques to it, one by one

So Q1 is a standalone demo, while Q2's output directly feeds into Q3.

We load the already-cleaned CSV that Lab Assignment 1 produced:
    ../Lab Assignment 1/Titanic-Dataset-Cleaned.csv
Make sure you have run Lab Assignment 1's script at least once already, so
that file exists.

HOW TO RUN THIS FILE
----------------------
1. Make sure Python 3 is installed.
2. Make sure these libraries are installed (run once, if needed):
        pip install pandas numpy matplotlib scikit-learn
3. Run this script from inside THIS folder ("Lab Assignment 3"):
        python3 lab_assignment_3.py
   It prints all explanations and tables to the terminal, saves every
   chart as a ".png" image inside a new "plots" folder next to this
   script, and saves the outlier-free + 7-times-scaled datasets as CSV
   files at the end.

==================================================================================
"""

# ----------------------------------------------------------------------------
# STEP 0: IMPORT THE LIBRARIES WE NEED
# ----------------------------------------------------------------------------
import os                      # for building reliable file paths
import math                    # for a couple of small math functions (log10, ceil) used in Decimal Scaling
import numpy as np             # numpy = "Numerical Python" - a toolbox for fast maths on lists of numbers (arrays)
import pandas as pd            # our table/DataFrame toolbox, as in every earlier assignment
import matplotlib.pyplot as plt  # our charting toolbox, as in Lab Assignment 2

# From scikit-learn, we import the ready-made scalers we'll use in Q3.
# (A couple of the 7 normalization techniques don't have a ready-made
# scikit-learn tool, so for those we write the formula ourselves by hand -
# each one is explained fully, in plain English, right before we use it.)
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler

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
# STEP 0c: LOAD THE ALREADY-CLEANED DATASET
# ----------------------------------------------------------------------------
section("LOADING THE CLEANED DATASET FROM LAB ASSIGNMENT 1")

df = pd.read_csv(cleaned_csv_path)
print(f"Loaded cleaned dataset from: {cleaned_csv_path}")
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print("Columns:", list(df.columns))
print(df.head())


# ==================================================================================
# QUESTION 1: Apply different types of Data Smoothing, with graphs:
#   a) Using bin mean
#   b) Using bin median
#   c) Using bin boundaries
# ==================================================================================
section("QUESTION 1: DATA SMOOTHING BY BINNING (mean / median / boundaries)")

print("""
WHAT IS "DATA SMOOTHING", AND WHY DO IT?
Real-world numeric data is often "noisy" - it jitters up and down a bit
due to small random fluctuations, even though there's a genuine, smoother
underlying trend. "Smoothing" means processing the data so that this small
random jitter is reduced/flattened out, while (hopefully) keeping the
real, larger pattern intact.

"BINNING" IS ONE WAY TO SMOOTH DATA - HOW IT WORKS:
  Step 1: SORT the column's values from smallest to largest.
  Step 2: Split the sorted values into consecutive groups called "bins"
          (here we use EQUAL-FREQUENCY bins, meaning every bin gets the
          same NUMBER of values in it - e.g. with a bin size of 4, values
          1-4 form bin 1, values 5-8 form bin 2, and so on).
  Step 3: replace every value inside a bin with something calculated FROM
          that bin, so all the values in the bin become smoother/closer to
          each other. This assignment asks for 3 different ways of doing
          this last step:
            a) BIN MEAN     -> replace every value in the bin with the
                               bin's average (mean).
            b) BIN MEDIAN   -> replace every value in the bin with the
                               bin's middle value (median) instead of the
                               mean (median is less pulled around by any
                               one extreme value inside that bin).
            c) BIN BOUNDARIES -> for each value, look at just the two
                               EDGE values of its bin (the smallest value
                               in the bin, and the largest value in the
                               bin), and replace it with WHICHEVER of
                               those two edges it is numerically closer
                               to. Unlike mean/median, this technique
                               always produces one of the two original
                               boundary numbers, never a "new" invented
                               number.

WHICH COLUMN, AND WHAT BIN SIZE?
We smooth the 'Fare' column (ticket price), because it is a real,
continuous numeric measurement with plenty of natural variation - a good
candidate to demonstrate smoothing on. We use a bin size of 20 (so every
20 sorted passengers form one bin) across the full column, which is small
enough to visibly show a "staircase" smoothing effect on the graph without
creating too many tiny bins to see clearly.
""")


def smooth_by_binning(sorted_values, bin_size):
    """
    Takes a NumPy array of values that is ALREADY SORTED (smallest to
    largest), and a chosen bin_size (how many values go in each bin), and
    returns THREE new arrays of the same length and order:
        bin_mean_smoothed      - every value replaced by its bin's mean
        bin_median_smoothed    - every value replaced by its bin's median
        bin_boundary_smoothed  - every value replaced by whichever bin
                                  edge (min or max of that bin) is closer
    This directly implements the 3-technique binning method taught in
    class, just written out as reusable Python code.
    """
    n = len(sorted_values)
    bin_mean_smoothed = np.zeros(n)
    bin_median_smoothed = np.zeros(n)
    bin_boundary_smoothed = np.zeros(n)

    # range(0, n, bin_size) counts 0, bin_size, 2*bin_size, 3*bin_size, ...
    # up to n - i.e. it gives us the STARTING index of every bin.
    for start in range(0, n, bin_size):
        # end is the starting index of the NEXT bin (or the very end of the
        # array for the last, possibly-smaller, leftover bin). Python
        # automatically stops slicing safely at the array's real end even
        # if "end" would technically go past it.
        end = start + bin_size
        # This slice grabs just the values that belong to the current bin.
        current_bin = sorted_values[start:end]

        bin_mean_value = current_bin.mean()
        bin_median_value = np.median(current_bin)
        bin_min = current_bin.min()
        bin_max = current_bin.max()

        # Fill in the mean/median results for every position in this bin.
        bin_mean_smoothed[start:end] = bin_mean_value
        bin_median_smoothed[start:end] = bin_median_value

        # For bin-boundary smoothing, we must decide, for EACH value
        # individually, whether it's closer to bin_min or bin_max.
        for i, value in enumerate(current_bin):
            distance_to_min = abs(value - bin_min)
            distance_to_max = abs(value - bin_max)
            if distance_to_min <= distance_to_max:
                bin_boundary_smoothed[start + i] = bin_min
            else:
                bin_boundary_smoothed[start + i] = bin_max

    return bin_mean_smoothed, bin_median_smoothed, bin_boundary_smoothed


# --- A small, easy-to-read worked example first (like a hand-calculation) ---
print("--- A small worked example first, on just 12 sample Fare values ---")
# We deliberately pick a small, sorted sample of 12 real Fare values from
# the dataset here, purely so the printed numbers below are short enough
# to read and verify by eye - exactly like a textbook worked example.
sample_fares = np.sort(df["Fare"].to_numpy())[::75][:12]  # pick 12 spread-out real values
print(f"Sample of 12 sorted Fare values: {sample_fares}")

sample_mean_smoothed, sample_median_smoothed, sample_boundary_smoothed = smooth_by_binning(
    sample_fares, bin_size=4
)
worked_example_table = pd.DataFrame({
    "Original": sample_fares,
    "Bin Mean Smoothed": sample_mean_smoothed.round(2),
    "Bin Median Smoothed": sample_median_smoothed.round(2),
    "Bin Boundary Smoothed": sample_boundary_smoothed.round(2),
})
print("\nWith 3 bins of 4 values each:")
print(worked_example_table)
print("""
Reading this small example: within each group of 4 sorted values (one
bin), "Bin Mean Smoothed" replaces all 4 with their average, "Bin Median
Smoothed" replaces all 4 with their middle value, and "Bin Boundary
Smoothed" pulls each individual value toward whichever end of its own bin
(smallest or largest) it was originally closer to.
""")

# --- Now apply the same 3 techniques across the FULL Fare column, and plot it ---
print("--- Now applying the same 3 techniques across the full 'Fare' column ---")
sorted_fare = np.sort(df["Fare"].to_numpy())
mean_smoothed, median_smoothed, boundary_smoothed = smooth_by_binning(sorted_fare, bin_size=20)

plt.figure(figsize=(10, 6))
# We plot against a simple 0, 1, 2, 3, ... position index (the x-axis here
# is just "the rank/position of a passenger once fares are sorted", not
# any real-world quantity) - this is the standard way to visualize
# smoothing: you can directly see how each smoothing technique flattens
# the natural jaggedness of the sorted original line into neat "steps".
x_positions = np.arange(len(sorted_fare))
plt.plot(x_positions, sorted_fare, label="Original (sorted)", color="lightgray", linewidth=1)
plt.plot(x_positions, mean_smoothed, label="Bin Mean Smoothed", color="steelblue")
plt.plot(x_positions, median_smoothed, label="Bin Median Smoothed", color="seagreen")
plt.plot(x_positions, boundary_smoothed, label="Bin Boundary Smoothed", color="darkorange")
plt.xlabel("Passenger rank (after sorting by Fare)")
plt.ylabel("Fare")
plt.title("Data Smoothing by Binning: Mean vs Median vs Boundary (bin size = 20)")
plt.legend()
save_current_plot("1_smoothing_full_fare_comparison.png")

# A zoomed-in version (first 100 sorted passengers) makes the "staircase"
# shape of each smoothing technique much easier to actually see, since the
# full-column plot above compresses 891 points into a small image.
plt.figure(figsize=(10, 6))
zoom = 100
plt.plot(x_positions[:zoom], sorted_fare[:zoom], label="Original (sorted)",
         color="lightgray", linewidth=1, marker=".")
plt.plot(x_positions[:zoom], mean_smoothed[:zoom], label="Bin Mean Smoothed", color="steelblue")
plt.plot(x_positions[:zoom], median_smoothed[:zoom], label="Bin Median Smoothed", color="seagreen")
plt.plot(x_positions[:zoom], boundary_smoothed[:zoom], label="Bin Boundary Smoothed", color="darkorange")
plt.xlabel("Passenger rank (after sorting by Fare)")
plt.ylabel("Fare")
plt.title("Data Smoothing by Binning - Zoomed In (first 100 sorted passengers)")
plt.legend()
save_current_plot("1_smoothing_zoomed_first_100.png")

print("""
How to read these charts: the light-gray "Original" line is jagged because
real Fare values jump around a lot even between neighbouring sorted
passengers. All three smoothing lines turn that jaggedness into flat
"steps" (one flat step per bin of 20 passengers) - Bin Mean and Bin Median
draw a SINGLE flat value across the whole step (median is slightly more
resistant to a single unusually extreme value inside a bin), while Bin
Boundary instead snaps every point to one of just two possible values (the
bin's minimum or its maximum), which is why its line looks more like sharp
up/down jumps between only two levels within a step, rather than one
perfectly flat line like mean/median smoothing.
""")


# ==================================================================================
# QUESTION 2: Identify outliers using Z-score and remove them.
# ==================================================================================
section("QUESTION 2: OUTLIER DETECTION AND REMOVAL USING Z-SCORE")

print("""
WHAT IS A Z-SCORE?
A Z-score tells you "how many standard deviations away from the average is
this particular value?". The formula for a value x in a column is:

    z = (x - mean_of_column) / standard_deviation_of_column

  - z = 0   means the value IS exactly the average.
  - z = 1   means the value is 1 standard deviation ABOVE the average.
  - z = -2  means the value is 2 standard deviations BELOW the average.

WHY DOES A LARGE Z-SCORE MEAN "OUTLIER"?
For data that is roughly bell-shaped (a "normal distribution"), about 99.7%
of all values naturally fall within 3 standard deviations of the mean
(this is a well-known statistics result called the "68-95-99.7 rule").
So if a value's Z-score has an ABSOLUTE VALUE greater than 3 (i.e. it is
more than 3 standard deviations away from the mean, in EITHER direction),
it is unusual enough, statistically, to be flagged as an outlier. This is
the standard, commonly used Z-score threshold, and the one we use here.

Note this is a DIFFERENT outlier-detection method than Lab Assignment 2's
box-plot/IQR method - IQR is based on percentiles/ranking (works well even
if the data is skewed), while Z-score is based on the mean and standard
deviation (works best when the data is roughly bell-shaped). Both are
valid, standard techniques; this question specifically asks us to use
Z-score.
""")


def zscore_outlier_mask(column):
    """
    Given a pandas Series of numbers, returns:
      - the Z-score of every value (as a pandas Series, same order),
      - a True/False mask that is True exactly where |z-score| > 3
        (i.e. True means "this row is an outlier for this column").
    """
    mean_value = column.mean()
    std_value = column.std()
    z_scores = (column - mean_value) / std_value
    is_outlier = z_scores.abs() > 3
    return z_scores, is_outlier


# We check BOTH numeric columns most likely to contain genuine extreme
# values: Age and Fare (the same two columns Lab Assignment 2 already
# flagged as containing IQR-based outliers).
age_z, age_is_outlier = zscore_outlier_mask(df["Age"])
fare_z, fare_is_outlier = zscore_outlier_mask(df["Fare"])

print(f"Age  -> mean={df['Age'].mean():.2f}, std={df['Age'].std():.2f}, "
      f"outliers with |z|>3: {age_is_outlier.sum()}")
print(f"Fare -> mean={df['Fare'].mean():.2f}, std={df['Fare'].std():.2f}, "
      f"outliers with |z|>3: {fare_is_outlier.sum()}")

# "|" between two True/False (boolean) columns means "OR" - so this marks
# a row as an outlier if EITHER its Age OR its Fare Z-score is extreme.
combined_outlier_mask = age_is_outlier | fare_is_outlier
outlier_rows = df[combined_outlier_mask]
print(f"\nTotal unique rows flagged as an outlier by Age and/or Fare Z-score: {len(outlier_rows)}")
print("\nThe flagged outlier rows:")
print(outlier_rows[["Survived", "Pclass", "Sex", "Age", "Fare"]])

# The "~" symbol means "NOT" - so this keeps only the rows that are NOT
# flagged as outliers, which is exactly the removal step the question asks
# for. We store this in a NEW variable so the earlier "df" (with outliers
# still in it) remains available if we ever wanted to compare against it.
df_no_outliers = df[~combined_outlier_mask].copy()
print(f"\nRow count before removal: {len(df)}")
print(f"Row count after removing Z-score outliers: {len(df_no_outliers)}")
print(f"Rows removed: {len(df) - len(df_no_outliers)}")

# A quick visual double-check: draw the Fare distribution before and after
# removing outliers, side by side, so you can literally see the extreme
# right-hand tail shrink.
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
axes[0].hist(df["Fare"], bins=30, color="lightcoral", edgecolor="black")
axes[0].set_title("Fare Distribution - BEFORE removing Z-score outliers")
axes[0].set_xlabel("Fare")
axes[0].set_ylabel("Number of Passengers")

axes[1].hist(df_no_outliers["Fare"], bins=30, color="seagreen", edgecolor="black")
axes[1].set_title("Fare Distribution - AFTER removing Z-score outliers")
axes[1].set_xlabel("Fare")
axes[1].set_ylabel("Number of Passengers")
save_current_plot("2_fare_distribution_before_after_outlier_removal.png")

print("""
NOTE: Just like in Lab Assignment 2, these Z-score-flagged Age/Fare
outliers are genuine, realistic extreme values (very high fares, unusually
elderly passengers) rather than data-entry mistakes. Removing them here is
done specifically because THIS assignment asks us to practice the "detect
with Z-score, then remove" workflow end-to-end - in a real project, you
would think carefully before permanently deleting real, valid data points
just for being unusual, since it can also throw away genuinely useful
information. We proceed with the outlier-free dataset for Question 3
below, since normalization techniques (especially Min-Max and Decimal
Scaling) are themselves sensitive to extreme outliers, so cleaning them
first makes the upcoming scaling comparison clearer and fairer.
""")


# ==================================================================================
# QUESTION 3: Perform 7 different types of data normalization on the
# outlier-free dataset from Question 2.
# ==================================================================================
section("QUESTION 3: SEVEN NORMALIZATION / SCALING TECHNIQUES")

# We scale 'Age' and 'Fare' - the same two genuine numeric measurement
# columns used throughout this whole assignment series, for the same
# reasons explained in Lab Assignment 2 (SibSp/Parch are small integer
# counts with limited spread, and Pclass/Sex/Embarked are categories, not
# true continuous measurements).
columns_to_scale = ["Age", "Fare"]
work_df = df_no_outliers[columns_to_scale].copy()

print(f"Working on the OUTLIER-REMOVED data from Question 2 "
      f"({len(work_df)} rows), columns: {columns_to_scale}\n")
print("Original (unscaled) statistics:")
print(work_df.describe().round(3))

# This dictionary will collect every scaled version so we can print a
# final side-by-side comparison table at the very end.
results = {}
results["Original"] = work_df.copy()

# ----------------------------------------------------------------------
# 3a) MIN-MAX NORMALIZATION
# ----------------------------------------------------------------------
print("""
--- (a) MIN-MAX NORMALIZATION ---
Formula: x_scaled = (x - min) / (max - min)
Squeezes every value into the range [0, 1]. The smallest value in the
column becomes 0, the largest becomes 1.
""")
minmax_scaler = MinMaxScaler()
minmax_result = pd.DataFrame(
    minmax_scaler.fit_transform(work_df), columns=columns_to_scale
)
results["Min-Max"] = minmax_result
print(minmax_result.describe().round(3))

# ----------------------------------------------------------------------
# 3b) MEAN NORMALIZATION
# ----------------------------------------------------------------------
print("""
--- (b) MEAN NORMALIZATION ---
Formula: x_scaled = (x - mean) / (max - min)
This is very similar to Min-Max, but instead of shifting by the MINIMUM
value, it shifts by the column's MEAN (average) instead. The result is
centred much closer to 0 (values below the average become negative,
values above the average become positive), while still being divided by
the same (max - min) "range" as Min-Max. scikit-learn does not have a
single ready-made function for this exact formula, so we calculate it
ourselves directly with pandas/numpy - this is a good example of how,
once you understand a formula, you don't strictly need a library function
for every single technique.
""")
mean_norm_result = pd.DataFrame()
for col in columns_to_scale:
    col_min = work_df[col].min()
    col_max = work_df[col].max()
    col_mean = work_df[col].mean()
    mean_norm_result[col] = (work_df[col] - col_mean) / (col_max - col_min)
results["Mean Normalization"] = mean_norm_result
print(mean_norm_result.describe().round(3))

# ----------------------------------------------------------------------
# 3c) Z-SCORE METHOD (STANDARDIZATION)
# ----------------------------------------------------------------------
print("""
--- (c) Z-SCORE METHOD (Standardization) ---
Formula: x_scaled = (x - mean) / standard_deviation
This is the exact same Z-score formula from Question 2 - but this time we
apply it as a SCALING technique (to reshape the whole column), rather than
as an outlier-detection rule. After this transform, the column's mean
becomes 0 and its standard deviation becomes 1.
""")
zscore_scaler = StandardScaler()
zscore_result = pd.DataFrame(
    zscore_scaler.fit_transform(work_df), columns=columns_to_scale
)
results["Z-score"] = zscore_result
print(zscore_result.describe().round(3))

# ----------------------------------------------------------------------
# 3d) DECIMAL SCALING
# ----------------------------------------------------------------------
print("""
--- (d) DECIMAL SCALING ---
Formula: x_scaled = x / 10^j
where "j" is the SMALLEST whole number that makes every scaled value's
absolute size less than 1. In practice: j = the number of digits in the
largest absolute value in the column (e.g. if the biggest value is 512,
it has 3 digits, so j = 3, and every value gets divided by 10^3 = 1000).
This simply "moves the decimal point" of every number the same number of
places to the left - the simplest of all these techniques, and one
scikit-learn also has no ready-made function for, so we calculate it
ourselves.
""")
decimal_scaling_result = pd.DataFrame()
for col in columns_to_scale:
    max_abs_value = work_df[col].abs().max()
    # math.log10(max_abs_value) tells us roughly how many digits the
    # number has (e.g. log10(512) is about 2.7). math.floor(...) + 1 turns
    # that into the correct whole number of digits (e.g. 3 for 512).
    # We guard against max_abs_value being 0 (would make log10 undefined).
    if max_abs_value == 0:
        j = 1
    else:
        j = math.floor(math.log10(max_abs_value)) + 1
    decimal_scaling_result[col] = work_df[col] / (10 ** j)
    print(f"  Column '{col}': max absolute value = {max_abs_value:.2f} -> "
          f"{j} digits -> dividing every value by 10^{j} = {10**j}")
results["Decimal Scaling"] = decimal_scaling_result
print(decimal_scaling_result.describe().round(3))

# ----------------------------------------------------------------------
# 3e) LOG TRANSFORMER
# ----------------------------------------------------------------------
print("""
--- (e) LOG TRANSFORMER ---
Formula: x_scaled = natural_log(x)   [natural log, i.e. base "e", matching
this course's convention - see Lecture 7's Log Transformer notes]
A log transform is especially useful for columns like Fare that are
strongly "right-skewed" (most values are small/cheap, but a long tail of
expensive outliers stretches the column far to the right) - taking the log
compresses that long tail down and pulls the whole distribution closer to
a symmetric, bell-like shape, which many statistical methods work better
with.

IMPORTANT REAL DATA CAVEAT WE CHECKED FOR: natural log of 0 is undefined
(mathematically, it is negative infinity), and this Titanic dataset
genuinely contains a small number of passengers with Fare = 0 (crew/staff
travelling for free, or comped tickets). Applying a plain log(x) here
would produce invalid "-inf" results for those exact rows. The standard,
safe fix - and what we use here - is "log1p", i.e. natural_log(x + 1)
instead of natural_log(x): this keeps log(0) = log(1) = 0 (a valid,
sensible number) instead of crashing into -infinity, while barely changing
the result for any larger Fare value. Age has no zero or negative values
in this dataset, so this caveat only actually matters for Fare, but we
apply log1p consistently to both columns for safety.
""")
zero_fare_count = (work_df["Fare"] == 0).sum()
print(f"(Confirmed: {zero_fare_count} passenger(s) in this outlier-removed "
      f"data have Fare = 0, which is exactly why log1p was needed instead of a plain log.)")

log_result = pd.DataFrame()
for col in columns_to_scale:
    # np.log1p(x) calculates natural_log(x + 1) directly and safely.
    log_result[col] = np.log1p(work_df[col])
results["Log Transform (log1p)"] = log_result
print(log_result.describe().round(3))

# ----------------------------------------------------------------------
# 3f) MAXABS TRANSFORMER
# ----------------------------------------------------------------------
print("""
--- (f) MAXABS TRANSFORMER ---
Formula: x_scaled = x / max(|x|)
Divides every value by the single LARGEST ABSOLUTE value in the column.
The largest-magnitude value in the column becomes exactly +1 or -1, and
every other value lands somewhere inside [-1, 1]. Since both Age and Fare
here only ever contain positive numbers, this behaves very similarly to
Min-Max in this particular case (both end up in [0, 1]) - but MaxAbs is
the better/correct choice in general specifically WHEN a column can
contain negative numbers too, since (unlike Min-Max) it doesn't shift the
data's zero point, it only rescales around the existing zero.
""")
maxabs_scaler = MaxAbsScaler()
maxabs_result = pd.DataFrame(
    maxabs_scaler.fit_transform(work_df), columns=columns_to_scale
)
results["MaxAbs"] = maxabs_result
print(maxabs_result.describe().round(3))

# ----------------------------------------------------------------------
# 3g) INTERQUARTILE / ROBUST SCALER
# ----------------------------------------------------------------------
print("""
--- (g) INTERQUARTILE SCALER / ROBUST SCALER ---
Formula: x_scaled = (x - median) / (Q3 - Q1)
Instead of using the mean/min/max (all of which can be dragged around a
lot by a single extreme outlier), this technique centres the data using
the MEDIAN, and scales it using the IQR (Q3 - Q1, the width of just the
"middle 50%" of the data - see Lab Assignment 2's Q2 for a full
explanation of Q1/Q3/IQR). Because the median and IQR both ignore the most
extreme values by design, this scaler is far less affected by outliers
than any of the other 6 techniques above - which is exactly why it's
called "Robust" (robust = "not easily thrown off by unusual/extreme
values").
""")
robust_scaler = RobustScaler()
robust_result = pd.DataFrame(
    robust_scaler.fit_transform(work_df), columns=columns_to_scale
)
results["Robust (IQR)"] = robust_result
print(robust_result.describe().round(3))

# ----------------------------------------------------------------------
# FINAL SIDE-BY-SIDE COMPARISON (using Fare only, since it's the more
# skewed/outlier-prone of our two columns, so differences are most visible)
# ----------------------------------------------------------------------
section("SIDE-BY-SIDE COMPARISON OF ALL 7 TECHNIQUES (Fare column, first 5 rows)")

comparison_table = pd.DataFrame({
    name: result_df["Fare"].head(5).values for name, result_df in results.items()
})
print(comparison_table.round(3))

print("""
How to read this comparison: notice how differently the SAME 5 original
Fare values end up looking depending on which technique is used - some
techniques (Min-Max, MaxAbs) force everything into a tight [0, 1] range,
Z-score and Robust can produce small negative numbers, Decimal Scaling
just shifts the decimal point without changing the overall "shape" of the
numbers at all, and Log Transform visibly compresses big values much more
aggressively than small ones. There is no single "best" technique for
every situation - which one to use depends on the shape of your data
(especially how skewed it is, and how many outliers it has) and on which
downstream machine learning algorithm you plan to use next.
""")

# A bar chart comparing how each technique reshapes just the Fare column's
# mean and standard deviation, so the differences are visible at a glance.
means = [result_df["Fare"].mean() for result_df in results.values()]
stds = [result_df["Fare"].std() for result_df in results.values()]
labels = list(results.keys())

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].bar(labels, means, color="cornflowerblue")
axes[0].set_title("Mean of 'Fare' After Each Scaling Technique")
axes[0].set_ylabel("Mean")
axes[0].tick_params(axis="x", rotation=45)

axes[1].bar(labels, stds, color="salmon")
axes[1].set_title("Standard Deviation of 'Fare' After Each Scaling Technique")
axes[1].set_ylabel("Standard Deviation")
axes[1].tick_params(axis="x", rotation=45)
save_current_plot("3_scaling_techniques_mean_std_comparison.png")


# ==================================================================================
# SAVE THE OUTPUT FILES
# ==================================================================================
section("SAVING OUTPUT FILES")

outlier_free_path = os.path.join(this_script_folder, "Titanic-Dataset-NoOutliers.csv")
df_no_outliers.to_csv(outlier_free_path, index=False)
print(f"Saved outlier-free dataset (Question 2 result) -> {outlier_free_path}")

for name, result_df in results.items():
    if name == "Original":
        continue
    # Turn a readable name like "Log Transform (log1p)" into a safe
    # filename like "Log_Transform_log1p" (no spaces, brackets, etc).
    safe_name = "".join(ch if ch.isalnum() else "_" for ch in name).strip("_")
    output_path = os.path.join(this_script_folder, f"Titanic-Scaled-{safe_name}.csv")
    result_df.to_csv(output_path, index=False)
    print(f"Saved '{name}' scaled Age/Fare columns -> {output_path}")

print(f"\nAll plots were saved inside: {plots_folder}")
print("\nAll 3 questions of Lab Assignment 3 are complete.")
