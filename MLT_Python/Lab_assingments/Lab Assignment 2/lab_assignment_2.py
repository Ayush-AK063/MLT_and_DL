"""
==================================================================================
 LAB ASSIGNMENT 2 - Visualization, Outlier Detection, Validation & Feature Scaling
==================================================================================

WHAT IS THIS FILE, AND WHO IS IT FOR?
----------------------------------------
Same as Lab Assignment 1: this is a plain Python script (a ".py" text file
full of Python instructions), written for someone who has NEVER used
Python, pandas, matplotlib, or scikit-learn before. Every step is
explained in plain English before the code, and important lines have
their own short "#" comment too.

WHERE DOES THE DATA COME FROM?
----------------------------------
This assignment says to do things like "validation checks AFTER cleaning"
- so it continues on from Lab Assignment 1, where we already cleaned the
raw Titanic dataset (filled in missing Age/Embarked, dropped the mostly-
empty Cabin column, removed the identifier-like columns PassengerId/
Name/Ticket). So this script loads the ALREADY-CLEANED file that
Lab Assignment 1 produced:
    ../Lab Assignment 1/Titanic-Dataset-Cleaned.csv
instead of the raw original CSV. If you haven't run Lab Assignment 1's
script yet, run that one first so this cleaned file actually exists.

HOW TO RUN THIS FILE
----------------------
1. Make sure Python 3 is installed.
2. Make sure these libraries are installed (run this once in your terminal
   if you don't have them yet):
        pip install pandas matplotlib scikit-learn
3. Make sure "Lab Assignment 1" has already been run at least once, so
   "Titanic-Dataset-Cleaned.csv" exists in its folder.
4. Run this script from inside THIS folder ("Lab Assignment 2"):
        python3 lab_assignment_2.py
   It will:
     - print all explanations/tables/numbers to your terminal, in order,
     - save every plot as a ".png" IMAGE FILE inside a new "plots" folder
       created next to this script (a script running in a plain terminal
       cannot "pop up" an interactive window reliably on every computer,
       so saving each plot as an image file is the most reliable way for
       you to actually open and look at every chart afterwards),
     - save two new scaled versions of the dataset as CSV files at the end
       (one Min-Max normalized, one standardized) - explained in Q4.

A NOTE ON "OR" IN THIS ASSIGNMENT (Q4)
------------------------------------------
Question 4 says to apply "either Min-Max Normalization, OR Standardization".
Rather than picking only one and skipping the other, this script deliberately
does BOTH, back-to-back, with a clear explanation of what each one does and
how their results differ - so you can see and compare both techniques
instead of only ever seeing one of them.

==================================================================================
"""

# ----------------------------------------------------------------------------
# STEP 0: IMPORT THE LIBRARIES WE NEED
# ----------------------------------------------------------------------------

# "os" -> a built-in Python toolbox for working with file paths, so this
# script can reliably find files and create folders no matter which
# directory you run it from.
import os

# "pandas" -> our table/DataFrame toolbox, exactly like in Lab Assignment 1.
import pandas as pd

# "matplotlib.pyplot" is the standard Python toolbox for DRAWING charts and
# graphs (scatter plots, bar charts, histograms, line plots, box plots,
# etc). "as plt" is just its usual short nickname, the same way "pandas"
# is nicknamed "pd".
import matplotlib.pyplot as plt

# From scikit-learn (a very popular machine-learning toolbox, imported
# using its short name "sklearn"), we import two specific tools we need
# for Question 4 (Feature Scaling):
#   - MinMaxScaler       -> squeezes numbers into the range [0, 1]
#   - StandardScaler     -> rescales numbers to have mean 0 and "spread" 1
# Both are explained in full, in plain English, right before we use them.
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Cosmetic pandas settings so printed tables are easy to read (does not
# affect any calculation, only how things look when printed). A very large
# "display.width" makes a wide table always print as ONE line per row,
# instead of pandas splitting it into two confusing stacked blocks.
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


def section(title):
    """Small helper to print a clear, easy-to-spot heading before each part
    of the output. See Lab Assignment 1's script for a full explanation of
    what a Python function/def is - the idea is identical here."""
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)


# ----------------------------------------------------------------------------
# STEP 0b: WORK OUT RELIABLE FILE PATHS, AND MAKE A FOLDER TO SAVE PLOTS INTO
# ----------------------------------------------------------------------------

# os.path.dirname(os.path.abspath(__file__)) means: "find the full path of
# THIS script file, then take just the folder part of that path". This
# gives us "this script's own folder", regardless of where you were
# standing in the terminal when you ran the "python3 ..." command.
this_script_folder = os.path.dirname(os.path.abspath(__file__))

# The cleaned CSV from Lab Assignment 1 lives in a sibling folder, i.e. one
# folder up, then into "Lab Assignment 1". os.path.join(...) safely glues
# folder/file names together into one valid path (it also automatically
# uses the correct slash style "/" or "\" for your operating system).
cleaned_csv_path = os.path.join(
    this_script_folder, "..", "Lab Assignment 1", "Titanic-Dataset-Cleaned.csv"
)

# This is where we will save every chart image this script produces.
plots_folder = os.path.join(this_script_folder, "plots")
# os.makedirs(..., exist_ok=True) creates that folder if it does not exist
# yet. "exist_ok=True" simply means "do not raise an error if the folder
# is already there from a previous run" - it just leaves it as is.
os.makedirs(plots_folder, exist_ok=True)


def save_current_plot(filename):
    """
    Small helper function: saves whatever chart matplotlib currently has
    "on screen" (in its invisible drawing canvas) to an image file inside
    our "plots" folder, then clears that canvas so the NEXT chart we draw
    starts fresh and does not accidentally overlap with this one.
    """
    full_path = os.path.join(plots_folder, filename)
    # plt.tight_layout() nudges the chart's margins/spacing so titles and
    # axis labels don't get cut off or overlap - purely cosmetic.
    plt.tight_layout()
    # plt.savefig(...) writes the current chart out as a real image file
    # (a .png here) that you can double-click and open like any photo.
    plt.savefig(full_path)
    # plt.close() closes/clears the current chart from memory, so the next
    # plt.plot(...)/plt.bar(...)/etc call starts a brand-new, empty chart.
    plt.close()
    print(f"  Saved plot -> plots/{filename}")


# ----------------------------------------------------------------------------
# STEP 0c: LOAD THE ALREADY-CLEANED DATASET FROM LAB ASSIGNMENT 1
# ----------------------------------------------------------------------------
section("LOADING THE CLEANED DATASET FROM LAB ASSIGNMENT 1")

df = pd.read_csv(cleaned_csv_path)
print(f"Loaded cleaned dataset from: {cleaned_csv_path}")
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print("Columns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.head())

print("""
Reminder of what each remaining column means:
  Survived : 0 = did not survive, 1 = survived
  Pclass   : ticket class (1 = 1st/best, 3 = 3rd/cheapest)  -> a CATEGORY, even though it's stored as a number
  Sex      : male / female                                  -> a CATEGORY (text)
  Age      : age in years                                   -> a NUMBER
  SibSp    : number of siblings/spouses aboard               -> a NUMBER (count)
  Parch    : number of parents/children aboard                -> a NUMBER (count)
  Fare     : ticket price paid                                -> a NUMBER
  Embarked : port of boarding (C, Q, or S)                    -> a CATEGORY (text)
""")


# ==================================================================================
# QUESTION 1: Visualize the data using different plots -
# scatter plot, bar plot, histogram, line plot.
# ==================================================================================
section("QUESTION 1: VISUALIZING THE DATA WITH DIFFERENT PLOT TYPES")

print("""
Each plot type below is chosen because it is the RIGHT tool for a
particular kind of question - just like you wouldn't use a hammer to turn
a screw. We explain, for each one, WHY that plot type suits that
particular question.
""")

# ----------------------------------------------------------------------
# 1a) SCATTER PLOT: Age vs Fare, coloured by whether they survived
# ----------------------------------------------------------------------
# WHY a scatter plot here? A scatter plot puts one NUMERIC variable on the
# x-axis and another NUMERIC variable on the y-axis, drawing one dot per
# row. It is the right tool when you want to see whether TWO numeric
# columns seem to relate to each other at all (e.g. "do older passengers
# tend to pay more, or less, for their ticket?"). Here we also colour each
# dot by "Survived" (0 or 1) as a bonus, so we can visually see if
# survival seems to cluster in certain Age/Fare regions.
print("1a) Scatter plot: Age vs Fare (coloured by Survived) ...")

# plt.figure(...) starts a brand new, blank chart canvas of a chosen size
# (width=8 inches, height=6 inches here) - purely a display preference.
plt.figure(figsize=(8, 6))

# We split the data into two groups (did not survive / survived) simply
# so we can give them two different colours AND a legend label. df[df["Survived"] == 0]
# filters the table down to only the rows where the Survived column equals 0.
did_not_survive = df[df["Survived"] == 0]
survived = df[df["Survived"] == 1]

# plt.scatter(x_values, y_values, ...) draws one dot per (x, y) pair.
# "alpha=0.6" makes the dots slightly see-through, which helps when many
# dots overlap on top of each other.
plt.scatter(did_not_survive["Age"], did_not_survive["Fare"],
            alpha=0.6, label="Did not survive (0)", color="firebrick")
plt.scatter(survived["Age"], survived["Fare"],
            alpha=0.6, label="Survived (1)", color="seagreen")

# plt.xlabel/ylabel/title just add text labels to the chart so anyone
# looking at the saved image understands what it shows without needing to
# read this script.
plt.xlabel("Age (years)")
plt.ylabel("Fare (ticket price)")
plt.title("Scatter Plot: Age vs Fare, coloured by Survival")
# plt.legend() draws the little labelled colour-key box on the chart,
# using the "label=" text we gave each plt.scatter(...) call above.
plt.legend()
save_current_plot("1a_scatter_age_vs_fare.png")

print("""
   How to read this chart: most passengers cluster at low Fare values
   regardless of age, with a "tail" of higher-fare (likely 1st class)
   passengers spread across many ages. There isn't one single obvious
   straight-line relationship between Age and Fare, but you can visually
   see that a good number of the low-Fare, "everyday" passengers did NOT
   survive (more red dots low-down), which hints - just from LOOKING at
   the picture - that Fare (and by extension, ticket class) might be
   related to survival chances. A proper statistical/model-based analysis
   would come later; this plot is just a first visual clue.
""")

# ----------------------------------------------------------------------
# 1b) BAR PLOT: number of passengers who survived vs did not, split by Sex
# ----------------------------------------------------------------------
# WHY a bar plot here? A bar plot is the right tool for comparing COUNTS
# or totals across a small number of CATEGORIES (as opposed to a scatter
# plot, which needs two numeric columns). Here, "Sex" (male/female) and
# "Survived" (0/1) are both categories, so we count how many passengers
# fall into each combination and draw one bar per combination.
print("\n1b) Bar plot: passenger counts by Sex, split by Survived ...")

# pd.crosstab(a, b) builds a small cross-tabulation table: for every
# unique value of "a" (rows) and "b" (columns), it counts how many rows of
# the original data had that exact combination. Here it gives us a table
# with Sex as rows (male/female) and Survived as columns (0/1), filled
# with passenger counts.
counts_table = pd.crosstab(df["Sex"], df["Survived"])
counts_table.columns = ["Did Not Survive (0)", "Survived (1)"]
print("Counts table used for the bar plot:")
print(counts_table)

plt.figure(figsize=(7, 5))
# counts_table.plot(kind="bar", ...) is a pandas convenience shortcut that
# internally calls matplotlib to draw one group of bars per row of the
# table (here: one group for "female", one for "male"), with one bar per
# column inside each group (Did Not Survive / Survived).
counts_table.plot(kind="bar", ax=plt.gca(), color=["firebrick", "seagreen"])
# plt.gca() means "get current axes" - it just tells pandas to draw onto
# the chart canvas we already opened with plt.figure(...) above, instead
# of silently opening yet another separate one.
plt.xlabel("Sex")
plt.ylabel("Number of Passengers")
plt.title("Bar Plot: Survival Counts by Sex")
plt.xticks(rotation=0)  # keep the "male"/"female" labels horizontal, not tilted
save_current_plot("1b_bar_survival_by_sex.png")

print("""
   How to read this chart: this immediately shows a big difference between
   the two groups - far more female passengers survived than did not,
   while for male passengers it's the reverse (far more did not survive
   than did). This is one of the most well-known real patterns in the
   Titanic dataset ("women and children first").
""")

# ----------------------------------------------------------------------
# 1c) HISTOGRAM: distribution of passenger Age
# ----------------------------------------------------------------------
# WHY a histogram here? A histogram is the right tool for looking at the
# DISTRIBUTION (the overall shape/spread) of a SINGLE numeric column - it
# groups values into equal-width "bins" (e.g. 0-5 years, 5-10 years, ...)
# and draws a bar showing how many passengers fall into each bin. This
# tells us things a plain average never could, like "is Age fairly evenly
# spread, or bunched up around a particular range?".
print("\n1c) Histogram: distribution of passenger Age ...")

plt.figure(figsize=(8, 5))
# plt.hist(data, bins=20, ...) automatically splits the Age values into 20
# equal-width bins across the full min-to-max range, and counts how many
# passengers land in each bin.
plt.hist(df["Age"], bins=20, color="steelblue", edgecolor="black")
plt.xlabel("Age (years)")
plt.ylabel("Number of Passengers")
plt.title("Histogram: Distribution of Passenger Age")
save_current_plot("1c_histogram_age.png")

print(f"""
   How to read this chart: you should see a large spike right around
   {df['Age'].median():.0f} years old (that's the median Age value we used
   back in Lab Assignment 1 to fill in the 177 originally-missing Age
   entries - so of course a lot of passengers now share that exact value).
   Besides that artificial spike, most passengers genuinely fall between
   their late teens and about 40 years old, with far fewer very young
   children or elderly passengers above 60.
""")

# ----------------------------------------------------------------------
# 1d) LINE PLOT: average Fare paid, by passenger class (Pclass)
# ----------------------------------------------------------------------
# WHY a line plot here, and why THIS particular comparison? A line plot is
# the right tool when your x-axis values have a natural ORDER and you want
# to show a TREND as you move along that order (classic example: a value
# changing over time). The Titanic dataset itself has no dates or times to
# plot against, but "Pclass" (1st, 2nd, 3rd class) IS naturally ordered
# (1st class is "better than" 2nd, which is "better than" 3rd), so a line
# plot showing "average Fare as class gets worse" is a meaningful, valid
# use of a line plot even without a time axis.
print("\n1d) Line plot: average Fare by passenger class (Pclass) ...")

# df.groupby("Pclass")["Fare"].mean() groups all rows by their Pclass value
# (1, 2, or 3), then calculates the average Fare within each group.
# .sort_index() makes sure the classes come out in order 1, 2, 3 (not in
# some random order), which matters because a line plot's whole point is
# to show a trend along an ordered axis.
avg_fare_by_class = df.groupby("Pclass")["Fare"].mean().sort_index()
print("Average fare per passenger class:")
print(avg_fare_by_class)

plt.figure(figsize=(7, 5))
# marker="o" draws a small circle at every actual data point along the
# line, which makes it easy to see exactly where each class's value sits
# (rather than just a smooth line with no visible individual points).
plt.plot(avg_fare_by_class.index, avg_fare_by_class.values, marker="o", color="darkorange")
plt.xlabel("Passenger Class (Pclass)")
plt.ylabel("Average Fare Paid")
plt.title("Line Plot: Average Fare by Passenger Class")
# Force the x-axis to only show the actual class numbers (1, 2, 3), not
# fractional ticks like 1.5, 2.5, since Pclass only ever takes whole values.
plt.xticks(avg_fare_by_class.index)
save_current_plot("1d_line_avg_fare_by_class.png")

print("""
   How to read this chart: the line drops sharply from 1st class to 3rd
   class, confirming that 1st class tickets cost dramatically more on
   average than 3rd class ones - exactly what you'd expect for a "better"
   travel class, and a good sanity check that our cleaned data still makes
   real-world sense.
""")


# ==================================================================================
# QUESTION 2: Identify outliers in at least two numerical variables using a
# Box plot. Visualize the detected outliers.
# ==================================================================================
section("QUESTION 2: DETECTING OUTLIERS WITH BOX PLOTS (Age and Fare)")

print("""
WHAT IS AN "OUTLIER"?
An outlier is a data point that is unusually far away from most of the
other values in its column - so extreme that it looks like it might be a
measurement mistake, a rare/unusual real case, or at least a value that
could distort calculations like the average if not handled carefully.

WHAT IS A BOX PLOT, AND HOW DOES IT FIND OUTLIERS?
A box plot is a chart built from 5 numbers taken from a sorted column:
  - the minimum "non-outlier" value
  - Q1 (the "25th percentile" - 25% of values are below this point)
  - the median (the middle value, "50th percentile")
  - Q3 (the "75th percentile" - 75% of values are below this point)
  - the maximum "non-outlier" value
It draws a box from Q1 to Q3 (this box contains the "middle 50%" of the
data, called the IQR = Interquartile Range = Q3 - Q1), a line inside the
box for the median, and "whiskers" (thin lines) extending out to the
furthest points that are still considered normal. ANY point drawn further
out than the whiskers is flagged as an outlier and shown as an individual
dot.

The standard mathematical rule a box plot uses to decide what counts as
an outlier (called the "1.5 x IQR rule") is:
    lower_bound = Q1 - 1.5 x IQR
    upper_bound = Q3 + 1.5 x IQR
Any value BELOW lower_bound or ABOVE upper_bound is flagged as an outlier.
We will calculate this ourselves below (so you can see the exact numbers
and exact outlier rows, not just look at a picture), and then also draw
the actual box plot picture that the assignment asks for.
""")


def detect_outliers_iqr(column_name):
    """
    A reusable helper function: given the NAME of a numeric column in our
    dataframe "df", this calculates Q1, Q3, the IQR, and the lower/upper
    bounds using the 1.5 x IQR rule described above, prints a summary, and
    returns the actual rows of "df" that are flagged as outliers for that
    column.
    """
    # .quantile(0.25) and .quantile(0.75) calculate Q1 and Q3 directly -
    # pandas does the "sort the column, then find the 25%/75% mark" work
    # for us.
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f"\n--- Outlier detection for '{column_name}' ---")
    print(f"Q1 (25th percentile): {q1:.2f}")
    print(f"Q3 (75th percentile): {q3:.2f}")
    print(f"IQR (Q3 - Q1)       : {iqr:.2f}")
    print(f"Lower bound (Q1 - 1.5*IQR): {lower_bound:.2f}")
    print(f"Upper bound (Q3 + 1.5*IQR): {upper_bound:.2f}")

    # This filters df down to only the rows where the column's value is
    # either below the lower bound OR ("|" is Python's "or" for these
    # row-by-row True/False filters) above the upper bound.
    outlier_rows = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
    print(f"Number of outlier rows found in '{column_name}': {len(outlier_rows)} "
          f"out of {len(df)} total rows ({len(outlier_rows) / len(df) * 100:.1f}%)")

    return outlier_rows, lower_bound, upper_bound


# --- Numeric variable 1: Age ---
age_outliers, age_lower, age_upper = detect_outliers_iqr("Age")
print("A few of the actual outlier rows found for 'Age':")
print(age_outliers[["Survived", "Pclass", "Sex", "Age", "Fare"]].head(10))

# --- Numeric variable 2: Fare ---
fare_outliers, fare_lower, fare_upper = detect_outliers_iqr("Fare")
print("\nA few of the actual outlier rows found for 'Fare':")
print(fare_outliers[["Survived", "Pclass", "Sex", "Age", "Fare"]].head(10))

print("""
INTERPRETATION:
  - 'Age' outliers are mostly on the HIGH end (elderly passengers in their
    60s-80s) - genuinely unusual ages compared to the bulk of passengers,
    but still perfectly realistic human ages, not data-entry mistakes.
  - 'Fare' outliers are almost entirely very HIGH fares (some passengers
    paid dramatically more than most - these were likely 1st class
    passengers with large private suites/family bookings). Fare cannot go
    below 0 in a valid record, so there are no "too low" Fare outliers
    here.
  In both cases, these look like genuine, valid extreme values rather
  than data errors, so the appropriate handling here is normally to KEEP
  them but be aware of them (for example, remembering they exist is
  exactly why Question 4 below considers scaling techniques that reduce
  the influence of such extreme values).
""")

# --- Now draw the actual box plots (the picture the assignment asks for) ---
print("\nDrawing box plots for Age and Fare, side by side ...")

# plt.subplots(1, 2, ...) creates ONE figure containing a 1-row-by-2-column
# grid of small charts ("axes") side by side, so we can show the Age box
# plot and the Fare box plot together in a single image for easy comparison.
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# axes[0].boxplot([...]) draws a box plot of the Age column into the FIRST
# (leftmost) small chart. dropna() removes any missing values before
# plotting (there shouldn't be any left after Lab Assignment 1's cleaning,
# but it's a harmless safety step). Box plots are vertical by default, so
# we don't need to pass any extra orientation option.
axes[0].boxplot(df["Age"].dropna())
axes[0].set_title("Box Plot: Age")
axes[0].set_ylabel("Age (years)")

axes[1].boxplot(df["Fare"].dropna())
axes[1].set_title("Box Plot: Fare")
axes[1].set_ylabel("Fare")

save_current_plot("2a_boxplots_age_and_fare.png")

# --- Also visualize WHICH specific points were flagged, on top of all the data ---
# This second chart makes the detected outliers extra obvious by plotting
# every passenger's Age (x-axis) and Fare (y-axis) as small grey dots, then
# drawing the flagged outlier rows again on top in bright red, so you can
# see exactly which real passengers were flagged, and by which column.
print("Drawing a scatter plot highlighting the specific outlier passengers ...")

plt.figure(figsize=(8, 6))
plt.scatter(df["Age"], df["Fare"], color="lightgray", label="Normal passengers", alpha=0.6)
plt.scatter(age_outliers["Age"], age_outliers["Fare"], color="darkorange",
            label="Age outliers", alpha=0.8, marker="^")
plt.scatter(fare_outliers["Age"], fare_outliers["Fare"], color="crimson",
            label="Fare outliers", alpha=0.6, marker="x")
plt.xlabel("Age (years)")
plt.ylabel("Fare")
plt.title("Highlighting Detected Age and Fare Outliers")
plt.legend()
save_current_plot("2b_outliers_highlighted_scatter.png")


# ==================================================================================
# QUESTION 3: Perform appropriate validation checks after cleaning.
# ==================================================================================
section("QUESTION 3: VALIDATION CHECKS AFTER CLEANING")

print("""
The whole point of this question is to PROVE, with actual checks (not just
assume), that the cleaning we did in Lab Assignment 1 actually worked and
that the dataset is now in a trustworthy state. We go through each check
the assignment lists, one at a time.
""")

# --- Check 1: Do any missing values remain? ---
print("--- Check 1: Missing values ---")
missing_after = df.isnull().sum()
total_missing = missing_after.sum()
print(missing_after)
if total_missing == 0:
    print("PASSED: There are zero missing values left in any column.")
else:
    print(f"FAILED: There are still {total_missing} missing values remaining somewhere.")

# --- Check 2: Do any duplicate records remain? ---
print("\n--- Check 2: Duplicate records ---")
duplicate_count = df.duplicated().sum()
print(f"Number of fully duplicated rows: {duplicate_count}")
if duplicate_count == 0:
    print("PASSED: No duplicate rows remain.")
else:
    print(f"FAILED: {duplicate_count} duplicate row(s) still remain.")

# --- Check 3: Are the numerical values valid (sensible, not impossible)? ---
print("\n--- Check 3: Numerical values are valid ---")
# "Valid" for a count or a price means: it cannot logically be negative.
# (df["Fare"] < 0) creates a True/False column: True wherever Fare is
# negative. .sum() then counts how many True's there are (i.e. how many
# rows would be invalid).
invalid_fare = (df["Fare"] < 0).sum()
invalid_sibsp = (df["SibSp"] < 0).sum()
invalid_parch = (df["Parch"] < 0).sum()
invalid_age = (df["Age"] < 0).sum()
print(f"Negative Fare values (impossible - can't pay negative money): {invalid_fare}")
print(f"Negative SibSp values (impossible - can't have negative siblings/spouses): {invalid_sibsp}")
print(f"Negative Parch values (impossible - can't have negative parents/children): {invalid_parch}")
print(f"Negative Age values (impossible): {invalid_age}")
if invalid_fare == invalid_sibsp == invalid_parch == invalid_age == 0:
    print("PASSED: All numeric columns contain only logically valid (non-negative) values.")
else:
    print("FAILED: At least one numeric column contains impossible negative values.")

# --- Check 4: Do categorical variables only contain valid categories? ---
print("\n--- Check 4: Categorical variables contain only valid categories ---")
# For each categorical column, we define the FULL set of values that are
# actually allowed to appear (based on what we know about the Titanic and
# how this dataset was documented), then check whether anything else
# (an unexpected, invalid category) has sneaked in.
valid_sex_values = {"male", "female"}
valid_embarked_values = {"C", "Q", "S"}
valid_pclass_values = {1, 2, 3}
valid_survived_values = {0, 1}

# set(df["Sex"].unique()) collects all of the DIFFERENT values that
# actually appear in the Sex column (as a "set", which is just a
# collection with no repeated items and no particular order), so we can
# compare it against the allowed set above.
actual_sex_values = set(df["Sex"].unique())
actual_embarked_values = set(df["Embarked"].unique())
actual_pclass_values = set(df["Pclass"].unique())
actual_survived_values = set(df["Survived"].unique())

# The "-" operator between two sets means "everything in the first set
# that is NOT also in the second set" - i.e. "which actual values are
# NOT in our allowed list?". If this comes out empty, everything is valid.
unexpected_sex = actual_sex_values - valid_sex_values
unexpected_embarked = actual_embarked_values - valid_embarked_values
unexpected_pclass = actual_pclass_values - valid_pclass_values
unexpected_survived = actual_survived_values - valid_survived_values

print(f"Sex      -> values found: {actual_sex_values}      | unexpected values: {unexpected_sex or 'none'}")
print(f"Embarked -> values found: {actual_embarked_values}   | unexpected values: {unexpected_embarked or 'none'}")
print(f"Pclass   -> values found: {actual_pclass_values}     | unexpected values: {unexpected_pclass or 'none'}")
print(f"Survived -> values found: {actual_survived_values}       | unexpected values: {unexpected_survived or 'none'}")

if not (unexpected_sex or unexpected_embarked or unexpected_pclass or unexpected_survived):
    print("PASSED: Every categorical column only contains its expected, valid categories.")
else:
    print("FAILED: At least one categorical column contains an unexpected value.")

# --- Check 5: Are dates correctly formatted? ---
print("\n--- Check 5: Dates are correctly formatted ---")
print("""
This particular Titanic dataset does NOT contain any date/time column at
all (no "date of travel", "date of birth", etc. is recorded) - so this
specific check does not literally apply to this dataset. We flag this
honestly rather than skip the question, and show below the GENERAL
technique you WOULD use if a date column existed, so the method itself is
still demonstrated.

If a column called, say, "Booking_Date" existed, you would do:

    df["Booking_Date_parsed"] = pd.to_datetime(df["Booking_Date"], errors="coerce")
    invalid_dates = df["Booking_Date_parsed"].isnull().sum()

pd.to_datetime(...) tries to convert every value in that column into a
proper Python "datetime" value. Any text that does NOT look like a valid
date (e.g. "31/13/2020", or "hello", or a typo) fails to convert.
"errors='coerce'" tells pandas: "if a value can't be converted, don't
crash the whole program - just put a missing value (NaN) there instead".
Counting how many NaNs appear AFTER this conversion (that weren't already
missing BEFORE it) tells you exactly how many rows had a badly-formatted
date.
""")

# --- Check 6: Do values lie within reasonable, domain-specific ranges? ---
print("--- Check 6: Domain-specific reasonable ranges ---")
print("""
"Domain-specific" means using REAL-WORLD KNOWLEDGE about what these
numbers are allowed to realistically be - not just "is it negative or
not", but "does this number make sense for a real human being on a real
ship in 1912?".
""")
# Age: no verified human on record has ever exceeded ~122 years, and this
# was a passenger ship in 1912, so anything above roughly 100 would be
# extremely suspicious, and Age obviously cannot be negative either.
unreasonable_age = df[(df["Age"] < 0) | (df["Age"] > 100)]
print(f"Passengers with an unreasonable Age (below 0 or above 100): {len(unreasonable_age)}")

# Fare: cannot be negative. As an extra sanity check, the highest
# confirmed real Titanic ticket fare (a first-class parlour suite) was
# around 512 - so anything drastically higher than that would be
# suspicious. We use 600 here as a generous safety margin above the
# known historical maximum.
unreasonable_fare = df[(df["Fare"] < 0) | (df["Fare"] > 600)]
print(f"Passengers with an unreasonable Fare (below 0 or above 600): {len(unreasonable_fare)}")

# Pclass should only ever be 1, 2, or 3 - there is no "4th class".
unreasonable_pclass = df[~df["Pclass"].isin([1, 2, 3])]
print(f"Passengers with an unreasonable Pclass (not 1, 2, or 3): {len(unreasonable_pclass)}")

if len(unreasonable_age) == 0 and len(unreasonable_fare) == 0 and len(unreasonable_pclass) == 0:
    print("PASSED: All checked columns fall within reasonable, real-world ranges.")
else:
    print("FAILED: At least one value falls outside a reasonable real-world range.")


# ==================================================================================
# QUESTION 4: Feature Scaling - apply Min-Max Normalization AND
# Standardization (both, back to back, on the same chosen columns).
# ==================================================================================
section("QUESTION 4: FEATURE SCALING (Min-Max Normalization AND Standardization)")

print("""
WHAT IS "FEATURE SCALING" AND WHY DO IT AT ALL?
Different numeric columns in this dataset live on very different scales:
Age ranges roughly 0-80, while Fare ranges roughly 0-512 (and SibSp/Parch
are small counts, usually 0-8). Many machine learning algorithms (like
k-nearest-neighbors, or anything using distances/gradients) can end up
being unfairly dominated by whichever column happens to have the LARGEST
raw numbers - not because that column is actually more important, but
purely because of the units it happens to be measured in. Feature scaling
puts every chosen numeric column onto a comparable scale, so no column
unfairly dominates just because of its raw size.

WHICH COLUMNS ARE "APPROPRIATE" TO SCALE HERE?
We select: Age, Fare, SibSp, Parch.
  - These are all genuinely continuous/count-based NUMERIC measurements.
We deliberately do NOT scale:
  - "Survived" -> this is the outcome/label (0 or 1) we would eventually
    want to predict, not an input measurement - scaling a label doesn't
    make sense and would only confuse its meaning (0 = no, 1 = yes).
  - "Pclass" -> although stored as a number (1, 2, 3), it is really a
    CATEGORY (which class of ticket), not a measured quantity where
    "2" is meaningfully "twice as much" as "1" - scaling it numerically
    would misleadingly treat it like a true measurement.
  - "Sex", "Embarked" -> these are text categories, not numbers at all,
    so numeric scaling does not apply to them (they would first need a
    different technique entirely, called "encoding", which is outside
    this assignment's scope).
""")

columns_to_scale = ["Age", "Fare", "SibSp", "Parch"]
print(f"Columns selected for scaling: {columns_to_scale}")

print("\nOriginal (unscaled) statistics for these columns:")
print(df[columns_to_scale].describe().round(2))

# ----------------------------------------------------------------------
# 4a) MIN-MAX NORMALIZATION
# ----------------------------------------------------------------------
print("""
--- METHOD 1: MIN-MAX NORMALIZATION ---
Formula (applied to every value "x" in a column):
    x_scaled = (x - min(column)) / (max(column) - min(column))
This SQUEEZES every value in the column into the range [0, 1] - the
smallest original value becomes exactly 0, the largest original value
becomes exactly 1, and everything else lands proportionally in between.
It's useful when you want every feature bounded within a fixed, known
range, but it is quite sensitive to outliers (a single extreme max/min
value stretches or squashes everything else).
""")

# MinMaxScaler() creates a "scaler" object - think of it as a small
# machine that first needs to LEARN the min and max of your data
# (via .fit(...)), and can then actually TRANSFORM values using what it
# learned (via .transform(...)). ".fit_transform(...)" conveniently does
# both steps in a single call.
minmax_scaler = MinMaxScaler()

# df[columns_to_scale] pulls out just those 4 columns as their own small
# table. fit_transform(...) on that returns a plain NumPy array of the
# scaled numbers (not a pandas table), so we immediately wrap it back
# into a nicely-labelled DataFrame using pd.DataFrame(..., columns=...).
minmax_scaled_values = minmax_scaler.fit_transform(df[columns_to_scale])
df_minmax = df.copy()
df_minmax[columns_to_scale] = minmax_scaled_values

print("Min-Max normalized statistics (every column's min should now be 0.0, max should be 1.0):")
print(df_minmax[columns_to_scale].describe().round(3))

print("\nFirst 5 rows after Min-Max normalization (compare to the original table above):")
print(df_minmax[columns_to_scale].head())

# ----------------------------------------------------------------------
# 4b) STANDARDIZATION
# ----------------------------------------------------------------------
print("""
--- METHOD 2: STANDARDIZATION (Z-score scaling) ---
Formula (applied to every value "x" in a column):
    x_scaled = (x - mean(column)) / standard_deviation(column)
This RE-CENTRES every column so its average becomes exactly 0, and
RE-SCALES it so its standard deviation (a measure of how spread out the
values are) becomes exactly 1. Unlike Min-Max, standardized values are
NOT bounded to a fixed [0, 1] range - they can still go quite negative or
quite positive, but a value's sign and size now directly tell you "how
many standard deviations above or below the average is this value?",
which is generally LESS sensitive to a handful of extreme outliers than
Min-Max normalization is.
""")

standard_scaler = StandardScaler()
standardized_values = standard_scaler.fit_transform(df[columns_to_scale])
df_standardized = df.copy()
df_standardized[columns_to_scale] = standardized_values

print("Standardized statistics (every column's mean should now be ~0.0, std should be ~1.0):")
print(df_standardized[columns_to_scale].describe().round(3))

print("\nFirst 5 rows after Standardization (compare to the original table above):")
print(df_standardized[columns_to_scale].head())

print("""
COMPARING THE TWO METHODS SIDE BY SIDE (using 'Fare' as the example,
since it has the most extreme outliers of our 4 chosen columns):
  - The single highest Fare value in the ORIGINAL data becomes exactly
    1.0 under Min-Max Normalization (by definition, since Min-Max always
    maps the maximum value to 1.0) - and because that one Fare value is
    such an extreme outlier, it drags the max upward, so most OTHER
    passengers' Min-Max-scaled fares end up bunched very close to 0.
  - Under Standardization, that same extreme Fare value simply becomes a
    large POSITIVE number (many standard deviations above the mean, with
    no fixed upper limit of 1.0 it has to squeeze everything else under),
    so the rest of the passengers' standardized fares are spread out more
    naturally around 0, without being squashed together by that one
    outlier.
  This is exactly why, in practice, Standardization is generally the
  safer default choice on data with outliers (like Fare here), while
  Min-Max Normalization is more often preferred when you specifically
  need every value guaranteed to sit within a fixed [0, 1] range (for
  example, some neural network input layers expect this).
""")


# ==================================================================================
# SAVE BOTH SCALED VERSIONS OF THE DATASET
# ==================================================================================
section("SAVING BOTH SCALED DATASETS")

minmax_output_path = os.path.join(this_script_folder, "Titanic-Dataset-MinMaxScaled.csv")
standardized_output_path = os.path.join(this_script_folder, "Titanic-Dataset-Standardized.csv")

df_minmax.to_csv(minmax_output_path, index=False)
df_standardized.to_csv(standardized_output_path, index=False)

print(f"Saved Min-Max normalized dataset -> {minmax_output_path}")
print(f"Saved standardized dataset       -> {standardized_output_path}")

print(f"\nAll plots were saved inside: {plots_folder}")
print("\nAll 4 questions of Lab Assignment 2 are complete.")
