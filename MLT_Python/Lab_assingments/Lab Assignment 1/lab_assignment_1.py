"""
==================================================================================
 LAB ASSIGNMENT 1 - Data Cleaning on the Titanic Dataset
==================================================================================

WHAT IS THIS FILE?
-------------------
This is a normal Python script (a ".py" file). It is NOT a special format -
it is just plain text containing Python code, and you run it from top to
bottom, one line after another, exactly like reading a recipe.

WHO IS THIS FOR?
-----------------
This file assumes you have NEVER written Python before and have NEVER heard
of "pandas" or "machine learning" before. Every single step is explained in
plain English BEFORE the code that does it, and important lines also have a
short comment next to them (comments start with a "#" symbol - Python
completely ignores everything after a "#" on a line, so comments are 100%
for humans reading the code, not for the computer).

HOW TO RUN THIS FILE
----------------------
1. Make sure Python is installed on your computer (any Python 3.x version).
2. Make sure the "pandas" library is installed. If it is not installed yet,
   open your terminal and run:
        pip install pandas
3. "Titanic-Dataset.csv" lives ONE FOLDER UP from this script, directly
   inside the "Lab_assingments" folder (NOT inside this "Lab Assignment 1"
   folder). This is intentional: the same Titanic dataset will be reused
   by future lab assignments too, so it is kept in one shared place
   instead of being copy-pasted into every assignment's own folder.
4. Run the script from the terminal, from inside this folder, with:
        python3 lab_assignment_1.py
   It will print all the results (tables, numbers, explanations) directly
   in your terminal, in order, and will also save a cleaned copy of the
   dataset as "Titanic-Dataset-Cleaned.csv" in this same folder at the end.

WHAT IS A "DATASET" AND A "CSV" FILE?
----------------------------------------
A dataset is simply a big table of information - think of an Excel sheet
with rows and columns. A ".csv" file ("Comma-Separated Values") is just a
plain text way of storing that table: every row of the table is one line
of text, and every column's value is separated by a comma. pandas (a
Python library / toolbox specifically built for working with tables of
data) can read a .csv file and turn it into something called a
"DataFrame" - which is just pandas' name for "a table of data that Python
can now search, filter, calculate on, and modify".

THE DATASET WE ARE USING
---------------------------
We are using the famous "Titanic" dataset. It contains information about
891 real passengers who were on the Titanic ship, including whether they
survived the disaster or not. Each row = one passenger. Each column = one
piece of information about that passenger (their age, ticket fare, class
of travel, etc). This is one of the most commonly used beginner datasets
in all of data science because it has a nice mix of numbers, text,
missing values, and different data types - perfect for practicing data
cleaning, which is exactly what this assignment is about.

==================================================================================
"""

# ----------------------------------------------------------------------------
# STEP 0: IMPORT THE LIBRARIES WE NEED
# ----------------------------------------------------------------------------
# "import" is a Python keyword that means "load this external toolbox so I
# can use the tools/functions inside it".
# "pandas" is the toolbox for working with tables of data (DataFrames).
# "as pd" just means: from now on, instead of typing the full word
# "pandas" every time, we can type the short nickname "pd". This is a very
# common convention that almost every Python data-science program uses.
import pandas as pd

# "os" is a built-in Python toolbox for talking to the operating system.
# We only use it here to build a reliable file PATH (the "address" of a
# file on your computer), so this script can always find the shared CSV
# file correctly, no matter which folder you happen to run it from.
import os

# We also set a pandas display option so that when we print a table, it
# shows ALL the columns instead of hiding some of them with "...". This is
# purely cosmetic (just for nicer/clearer printing in the terminal) and has
# no effect on the actual data or calculations. We set "display.width" to a
# very large number so a wide table always prints as ONE line per row,
# instead of pandas splitting a wide table into two stacked blocks (with a
# confusing "\" at the end of the first block) - one single wide line is
# easier to read correctly than two blocks you have to mentally stitch
# back together row by row.
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


def section(title):
    """
    This is a small helper FUNCTION (a reusable mini-program) that we wrote
    ourselves, just to print a nice, easy-to-spot heading line before each
    part of the output, so the terminal output is easy to read.
    "def" is the Python keyword used to define (create) a new function.
    Whenever we call section("something") later in this file, Python jumps
    up here, runs these two print lines with "something" plugged in, and
    then jumps back to continue where it left off.
    """
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)


# ==================================================================================
# QUESTION 1: Take a dataset of your choice and then upload or load the dataset.
# ==================================================================================
section("QUESTION 1: LOADING THE DATASET")

# pd.read_csv(...) is a pandas function that reads a .csv file from your
# computer's disk and loads it into a DataFrame (a table object in Python's
# memory that we can now work with). We are storing the result in a
# variable named "df" (short for "DataFrame" - this name is a very common
# convention in the data science world, so you will see "df" used
# everywhere in tutorials and real projects).
#
# The Titanic CSV file lives ONE FOLDER UP from this script (inside the
# shared "Lab_assingments" folder), because the same dataset will be
# reused by other lab assignments later. Building the path this way
# (instead of just writing "../Titanic-Dataset.csv" directly) makes sure
# it still works correctly even if you run this script from a different
# starting folder in your terminal.
this_script_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(this_script_folder, "..", "Titanic-Dataset.csv")
df = pd.read_csv(csv_path)

# df.shape tells us the size of the table as (number_of_rows, number_of_columns).
# It is NOT a function you "call" with parentheses - it is an attribute
# (a stored property) of the DataFrame, so we just read it directly.
print(f"The dataset has been loaded successfully.")
print(f"Number of rows (passengers): {df.shape[0]}")
print(f"Number of columns (pieces of information per passenger): {df.shape[1]}")

# df.head(5) shows us just the FIRST 5 rows of the table, so we can quickly
# eyeball what the data actually looks like without printing all 891 rows.
print("\nHere are the first 5 rows of the dataset, just to see what it looks like:")
print(df.head())

# df.dtypes shows us, for every column, what TYPE of data pandas thinks it
# contains: "int64" = whole numbers, "float64" = decimal numbers,
# "object"/"str" = text (or a mix of text and missing values).
# Knowing the data type of each column matters a lot later, because you
# handle missing numbers differently from missing text.
print("\nData type of every column (int64/float64 = numeric, object = text):")
print(df.dtypes)

# A quick plain-English description of what each column in this dataset means,
# since a total beginner won't know what "SibSp" or "Parch" mean:
print("""
What each column means (for reference while reading this script):
  PassengerId : a unique serial number given to each passenger row (1, 2, 3, ...)
  Survived    : 0 = did not survive, 1 = survived
  Pclass      : ticket class the passenger travelled in (1 = 1st/best class, 3 = 3rd/cheapest class)
  Name        : the passenger's full name
  Sex         : male / female
  Age         : the passenger's age in years
  SibSp       : number of Siblings/Spouses travelling with the passenger
  Parch       : number of Parents/Children travelling with the passenger
  Ticket      : the passenger's ticket number/code (a mix of letters and numbers)
  Fare        : how much money the passenger paid for the ticket
  Cabin       : the cabin (room) number the passenger stayed in, if known
  Embarked    : the port where the passenger boarded the ship (C, Q, or S)
""")


# ==================================================================================
# QUESTION 2: Identify the number and percentage of missing values in each
# column, and handle missing values using a suitable technique.
# ==================================================================================
section("QUESTION 2A: FINDING MISSING VALUES")

# "Missing value" means: for a given passenger (row) and a given column,
# we simply do not have that piece of information. In the raw .csv file
# these show up as empty cells; once pandas loads them, it represents a
# missing value using a special marker called "NaN" (Not a Number).
#
# df.isnull() returns a new table of the exact same shape as df, but every
# cell is now either True (this value is missing) or False (this value is
# present). Then ".sum()" on top of that adds up all the True values in
# each column (in Python, True behaves like the number 1 and False like 0
# when you add them up), which gives us a per-column COUNT of missing values.
missing_count = df.isnull().sum()

# To get a PERCENTAGE, we divide each column's missing count by the total
# number of rows (len(df) gives the number of rows in the table), then
# multiply by 100 to turn the fraction into a percentage, and round it to
# 2 decimal places using .round(2) so it is easy to read.
missing_percent = (missing_count / len(df) * 100).round(2)

# pd.DataFrame({...}) here builds a small, new, clean summary table out of
# the two Series (columns of numbers) we just calculated, so we can print
# them side by side instead of separately. The dictionary keys ("Missing
# Count", "Missing %") become the column headers of this new mini-table.
missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing %": missing_percent
})

# We only really care about columns that HAVE at least one missing value,
# so we filter the summary table down to just those rows, and sort them
# from the most-missing column to the least-missing column, so the worst
# offenders are immediately visible at the top.
missing_summary = missing_summary[missing_summary["Missing Count"] > 0]
missing_summary = missing_summary.sort_values("Missing Count", ascending=False)

print("Columns that contain missing values, and how much of each is missing:")
print(missing_summary)

print("""
INTERPRETATION (in plain English):
  - "Cabin" is missing for about 77% of all passengers. That is a HUGE
    proportion of the column - for more than 3 out of every 4 passengers,
    we simply have no cabin information at all.
  - "Age" is missing for about 20% of passengers (177 out of 891). That is
    a meaningful chunk, but still a clear minority of the data.
  - "Embarked" is missing for only 2 passengers out of 891 - a tiny, almost
    negligible amount.
  Each of these three columns is missing a very different AMOUNT of data,
  so (as the assignment hints) each one deserves a different, suitable
  technique for handling it - there is no single "one size fits all" fix.
""")

section("QUESTION 2B: HANDLING MISSING VALUES")

# We make a COPY of the original dataframe before we start changing it.
# This is a good habit: df.copy() creates a completely independent second
# table in memory. If we made mistakes while editing "df" directly, we
# could not easily get the original, untouched data back to compare
# against. By working on "df_clean" instead, "df" (the original) stays
# safe and unchanged the whole time.
df_clean = df.copy()

# --- Handling "Age" (a NUMERIC column, missing ~20% of the time) ---
# For a numeric column with a moderate amount of missing data, a standard,
# suitable technique is IMPUTATION: instead of deleting rows (which would
# throw away all the OTHER good information - Sex, Fare, Pclass, etc. -
# that those same 177 passengers have), we fill in the gap with a sensible
# estimated value calculated from the data we DO have.
#
# We use the MEDIAN (the middle value when all known ages are sorted from
# smallest to largest) rather than the MEAN (the mathematical average),
# because Age can have outliers (a few very old or very young passengers),
# and the median is much less affected/pulled by extreme outlier values
# than the mean is. This makes the median a more "robust" (safer) choice
# for imputing a numeric column like Age.
median_age = df_clean["Age"].median()
print(f"Median Age calculated from the known ages: {median_age}")

# df_clean["Age"].fillna(value) replaces every missing (NaN) entry in the
# "Age" column with the given value, and leaves every already-known Age
# value completely untouched. We then assign the result back into the
# same column, which overwrites it with the now-complete version.
df_clean["Age"] = df_clean["Age"].fillna(median_age)
print("-> Filled all missing 'Age' values with the median age (median imputation).")

# --- Handling "Embarked" (a CATEGORICAL/TEXT column, missing only 2 times) ---
# "Embarked" is a text/category column (its only possible values are the
# letters C, Q, or S), so calculating a "median" or "mean" makes no sense
# for it at all - you cannot average three letters. For a categorical
# column, the equivalent, suitable technique is MODE IMPUTATION: filling
# in the missing spots with the MODE, which simply means "the single
# most frequently occurring value in that column".
mode_embarked = df_clean["Embarked"].mode()[0]
# NOTE: .mode() can technically return more than one value if there is a
# tie for "most common", so it always gives back a small list/Series of
# candidates even when there's only one answer. We take [0] to grab just
# the first (and in this dataset, the only) most-common value out of it.
print(f"Most common 'Embarked' port (the mode): '{mode_embarked}'")

df_clean["Embarked"] = df_clean["Embarked"].fillna(mode_embarked)
print("-> Filled the 2 missing 'Embarked' values with the mode (mode imputation).")

# --- Handling "Cabin" (missing ~77% of the time) ---
# For "Cabin", imputing a value does not make sense at all: a cabin number
# is a unique-ish piece of information (there is no sensible "average" or
# even "most common" cabin that would be a meaningful guess for a random
# passenger), AND more importantly, 77% of the column is empty - at that
# point, whatever we invent to fill those gaps would just be noise, not
# real information, and could mislead any further analysis.
#
# The suitable technique here, per the assignment's own list of options,
# is REMOVAL - specifically, removing this ENTIRE COLUMN (not the rows),
# because it is the column itself that is unreliable, not just a few rows.
# Removing the affected ROWS instead would mean throwing away 687 out of
# 891 passengers (77% of our whole dataset!) just because of one column -
# that would be a huge, unnecessary loss of otherwise-good information in
# every other column for those passengers.
#
# df.drop(columns=[...]) removes the listed column(s) from the table.
df_clean = df_clean.drop(columns=["Cabin"])
print("-> Dropped the entire 'Cabin' column (77% missing - too unreliable to impute, "
      "and dropping rows instead would have discarded 687 otherwise-good passenger records).")

# Let's now confirm that there are NO missing values left anywhere in df_clean.
print("\nMissing value count per column AFTER cleaning (should all be 0 now):")
print(df_clean.isnull().sum())

print("""
NOTE ON THE OTHER TWO TECHNIQUES MENTIONED IN THE ASSIGNMENT
(Forward/backward filling, and Removal of rows):
  - "Forward fill" (copy the previous row's value downward) and "backward
    fill" (copy the next row's value upward) are techniques best suited to
    data that has a natural ORDER, most commonly a time series (like daily
    stock prices or hourly sensor readings), where "the next reading is
    probably close to the last one" is a reasonable assumption. In the
    Titanic dataset, the rows are just a list of unrelated passengers in
    no particular meaningful order, so copying "the previous passenger's
    Age" onto a completely different, unrelated passenger would not make
    logical sense here - which is exactly why we picked median/mode
    imputation and column removal instead, as the suitable techniques for
    THIS dataset's columns.
  - "Removal of rows" (dropping any row that has a missing value anywhere)
    was intentionally avoided for Age and Embarked, for the reason
    explained above: it would throw away good, complete information in
    every other column just because of one missing cell.
""")


# ==================================================================================
# QUESTION 3: Identify duplicate records, display them, and remove
# duplicate records where appropriate.
# ==================================================================================
section("QUESTION 3: FINDING AND REMOVING DUPLICATE RECORDS")

# A "duplicate record" means two (or more) ROWS in the table that have
# IDENTICAL values in every single column - i.e., the exact same
# passenger information appears more than once.
#
# df_clean.duplicated() returns True/False for every row: True means "this
# exact row has already appeared earlier in the table" (the very first
# occurrence of a repeated row is marked False; only the later, repeated
# copies are marked True). .sum() then counts how many rows are flagged
# as duplicates.
num_duplicates = df_clean.duplicated().sum()
print(f"Number of fully duplicate rows found: {num_duplicates}")

# df_clean[df_clean.duplicated()] uses the True/False list from above to
# FILTER the table down to just the duplicate rows, so we can actually
# look at them (the assignment specifically asks us to "display" them).
duplicate_rows = df_clean[df_clean.duplicated()]
print("\nThe duplicate rows themselves (if any):")
print(duplicate_rows if len(duplicate_rows) > 0 else "(none - see explanation below)")

# We also specifically check the "PassengerId" column on its own, since it
# is supposed to be a unique ID for every passenger. If the same
# PassengerId appeared twice, that would be a strong, separate red flag
# for duplicated/duplicated-by-mistake data, even if a few other columns
# happened to differ slightly (e.g. due to a typo).
duplicate_ids = df_clean["PassengerId"].duplicated().sum()
print(f"\nNumber of repeated 'PassengerId' values (should be a unique ID per row): {duplicate_ids}")

if num_duplicates > 0:
    # drop_duplicates() removes the extra copies and keeps only the first
    # occurrence of each repeated row. We only run this if duplicates were
    # actually found, otherwise there is nothing to remove.
    df_clean = df_clean.drop_duplicates()
    print(f"-> Removed {num_duplicates} duplicate row(s). New row count: {df_clean.shape[0]}")
else:
    print("""
-> RESULT: This particular Titanic dataset does not actually contain any
   fully duplicated rows, and every PassengerId is unique (891 unique IDs
   for 891 rows). This makes sense, because PassengerId acts like a
   built-in "row number" that was assigned once per real passenger when
   this dataset was first put together, so no accidental duplicate row
   could realistically appear without also repeating a PassengerId.
   The code above (df_clean.drop_duplicates()) is still written and would
   correctly remove any duplicates if this were run on a different,
   messier dataset that did contain repeated rows - it just has nothing
   to do on this particular file.
""")


# ==================================================================================
# QUESTION 4: Identify columns that are Irrelevant / Redundant / Identifier /
# Not useful for further analysis. Remove them and explain why.
# ==================================================================================
section("QUESTION 4: IDENTIFYING AND REMOVING UNHELPFUL COLUMNS")

print("Columns currently remaining in the dataset:")
print(list(df_clean.columns))

print("""
Let's go column by column and classify each one. Here, "further analysis"
means: if we were later trying to study or predict something about these
passengers (for example, predicting whether a passenger survived), would
this column actually help a model or a human analyst find a genuine
PATTERN, or would it just get in the way?

  PassengerId -> IDENTIFIER COLUMN.
      It is just a running serial number (1, 2, 3, ... 891) assigned to
      each row. It carries no real-world information about the passenger
      at all (a passenger's chance of survival has nothing to do with
      which row number they happened to be listed on). Its ONLY purpose
      was to uniquely label each row, similar to a roll number - useful
      for looking a specific row up, but useless as an input for finding
      patterns. -> REMOVE.

  Name -> IDENTIFIER-LIKE / NOT USEFUL IN ITS CURRENT (RAW) FORM.
      Every single name in this dataset is unique (891 different names for
      891 rows), so it behaves just like another identifier here, not
      like a genuine descriptive feature. A person's literal name (e.g.
      "Owen Harris") does not, by itself, influence survival. (Advanced
      note, beyond this assignment's scope: analysts sometimes extract the
      person's TITLE, like "Mr./Mrs./Miss/Master", out of this column,
      because a title can hint at age/gender/social status - but that
      would be creating a brand NEW column from this one, which is a
      separate technique called "feature engineering", not part of basic
      cleaning.) As it stands, in raw form, it is not useful.
      -> REMOVE.

  Ticket -> IDENTIFIER-LIKE / NOT USEFUL IN ITS CURRENT (RAW) FORM.
      This is a messy mix of letters and numbers (like "A/5 21171" or
      "PC 17599") that mostly behaves like an internal booking-office
      code rather than a meaningful, analyzable feature - it has 681
      different values across 891 rows, so it is "nearly" a unique ID in
      practice, and its exact text format does not represent any
      measurable quantity or clean category. -> REMOVE.

  Sex, Pclass, Age, SibSp, Parch, Fare, Embarked, Survived ->
      These all describe a genuine, real-world CHARACTERISTIC of the
      passenger or their journey (their gender, travel class, age, family
      size aboard, ticket price, boarding port) or the actual OUTCOME we
      would eventually want to study/predict (Survived). None of these are
      identifiers, and none of them are duplicated/redundant copies of
      each other (each one measures something genuinely different) ->
      KEEP all of these.

  REDUNDANT COLUMNS check:
      "Redundant" would mean two columns that essentially carry the SAME
      information twice, just phrased differently. In this dataset, no
      two columns are exact duplicates of each other's meaning: Pclass
      (ticket class) and Fare (price paid) are correlated in real life
      (higher class usually costs more) but they are NOT the same
      information - Fare is a fine-grained/individual number, Pclass is
      the passenger's class category, and a person's exact fare can still
      vary even within the same class (due to discounts, family group
      bookings, etc). So no column needs to be removed purely for being
      redundant here.
""")

# Now we actually perform the removal, using the reasoning explained above.
columns_to_remove = ["PassengerId", "Name", "Ticket"]
df_final = df_clean.drop(columns=columns_to_remove)

print(f"Removed columns: {columns_to_remove}")
print("\nFinal, cleaned dataset - columns remaining:")
print(list(df_final.columns))

print("\nFinal, cleaned dataset - first 5 rows:")
print(df_final.head())

print(f"\nFinal shape of the cleaned dataset: {df_final.shape[0]} rows x {df_final.shape[1]} columns")


# ==================================================================================
# SAVE THE FINAL CLEANED DATASET
# ==================================================================================
section("SAVING THE CLEANED DATASET")

# df.to_csv(filename, index=False) writes our final, cleaned DataFrame back
# out to a new .csv file on disk, so you have a permanent, ready-to-use
# copy of the cleaned data without needing to re-run this script every
# time. "index=False" tells pandas NOT to write its own internal row-number
# column into the file (we don't need an extra, meaningless numbering
# column in the saved file - we already removed PassengerId on purpose!).
output_filename = os.path.join(this_script_folder, "Titanic-Dataset-Cleaned.csv")
df_final.to_csv(output_filename, index=False)
print(f"Saved the final cleaned dataset to '{output_filename}'.")

print("\nAll 4 questions of Lab Assignment 1 are complete.")
