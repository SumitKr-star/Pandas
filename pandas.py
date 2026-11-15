"""
PANDAS FOR BEGINNERS
===================

This file is a commented introduction to the Pandas library.

How to use:
1. Install Pandas: python -m pip install pandas
2. Run this file: python pandas_beginner.py
3. Read the comments and try changing the examples.

Pandas is commonly used for reading, cleaning, exploring, and analysing tabular data.
"""

# ------------------------------------------------------------
# 1. IMPORT PANDAS
# ------------------------------------------------------------

# Import the pandas library.
# The name "pd" is the standard short name used by most Python developers.
import pandas as pd


# ------------------------------------------------------------
# 2. CREATE A SERIES
# ------------------------------------------------------------

# A Series is like a single column in a spreadsheet.
# Each value has an index label.
marks = pd.Series([85, 90, 78, 92])

print("\n1. SERIES")
print(marks)

# We can provide our own index labels instead of using 0, 1, 2...
student_marks = pd.Series(
    [85, 90, 78],
    index=["Aman", "Riya", "Kabir"]
)
print(student_marks)


# ------------------------------------------------------------
# 3. CREATE A DATAFRAME
# ------------------------------------------------------------

# A DataFrame is like a complete table with rows and columns.
# Here, each dictionary key becomes a column name.
data = {
    "Name": ["Aman", "Riya", "Kabir", "Neha", "Ishita"],
    "Age": [20, 21, 19, 22, 20],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Jaipur"],
    "Marks": [85, 92, 76, 88, 95]
}

df = pd.DataFrame(data)

print("\n2. DATAFRAME")
print(df)


# ------------------------------------------------------------
# 4. UNDERSTAND YOUR DATA
# ------------------------------------------------------------

# head() shows the first five rows by default.
print("\nFirst rows:")
print(df.head())

# head(2) shows only the first two rows.
print("\nFirst two rows:")
print(df.head(2))

# tail() shows the last five rows by default.
print("\nLast rows:")
print(df.tail())

# shape returns (number_of_rows, number_of_columns).
print("\nShape (rows, columns):", df.shape)

# columns displays all column names.
print("\nColumn names:", df.columns)

# info() shows column names, non-empty values, and data types.
print("\nData information:")
df.info()

# describe() gives summary statistics for numeric columns.
print("\nNumeric summary:")
print(df.describe())


# ------------------------------------------------------------
# 5. SELECT COLUMNS
# ------------------------------------------------------------

# Select one column. The result is a Series.
print("\nNames column:")
print(df["Name"])

# Select multiple columns. Use a list inside the brackets.
print("\nName and Marks columns:")
print(df[["Name", "Marks"]])


# ------------------------------------------------------------
# 6. SELECT ROWS WITH loc AND iloc
# ------------------------------------------------------------

# loc selects rows using index labels.
# Our DataFrame currently has index labels 0, 1, 2, 3, 4.
print("\nRow with label 0:")
print(df.loc[0])

# iloc selects rows using integer positions.
# Position 1 means the second row.
print("\nSecond row:")
print(df.iloc[1])

# Select rows 0 to 2 (the ending position is not included).
print("\nFirst three rows:")
print(df.iloc[0:3])


# ------------------------------------------------------------
# 7. FILTER DATA
# ------------------------------------------------------------

# A condition produces True/False values.
# Putting the condition inside df[...] keeps only matching rows.
high_marks = df[df["Marks"] >= 85]
print("\nStudents with marks of at least 85:")
print(high_marks)

# We can combine conditions:
# & means AND. Each condition must be inside parentheses.
delhi_adults = df[(df["City"] == "Delhi") & (df["Age"] >= 20)]
print("\nStudents from Delhi aged 20 or above:")
print(delhi_adults)

# | means OR. At least one condition must be True.
delhi_or_pune = df[(df["City"] == "Delhi") | (df["City"] == "Pune")]
print("\nStudents from Delhi or Pune:")
print(delhi_or_pune)

# isin() checks whether values are present in a list.
selected_cities = df[df["City"].isin(["Delhi", "Jaipur"])]
print("\nStudents from selected cities:")
print(selected_cities)


# ------------------------------------------------------------
# 8. ADD, UPDATE, AND DELETE COLUMNS
# ------------------------------------------------------------

# Add a new column by assigning values.
df["Passed"] = df["Marks"] >= 40
print("\nAfter adding Passed column:")
print(df)

# Update a value using loc (row label, column name).
df.loc[0, "Marks"] = 87
print("\nAfter updating Aman's marks:")
print(df)

# Delete a column with drop().
# axis=1 means columns. inplace=False is the default,
# so we save the returned DataFrame in a new variable.
df_without_age = df.drop("Age", axis=1)
print("\nDataFrame without Age:")
print(df_without_age)


# ------------------------------------------------------------
# 9. MISSING VALUES
# ------------------------------------------------------------

# Create a small DataFrame that contains missing values.
missing_data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Kabir", "Neha"],
    "Marks": [85, None, 76, None],
    "City": ["Delhi", "Mumbai", None, "Pune"]
})

# isna() marks missing values as True.
print("\nMissing value locations:")
print(missing_data.isna())

# isna().sum() counts missing values in each column.
print("\nMissing values per column:")
print(missing_data.isna().sum())

# dropna() removes rows that contain at least one missing value.
rows_removed = missing_data.dropna()
print("\nRows after removing missing values:")
print(rows_removed)

# fillna() replaces missing values.
# Here, missing marks are replaced with the average marks.
average_marks = missing_data["Marks"].mean()
filled_data = missing_data.copy()
filled_data["Marks"] = filled_data["Marks"].fillna(average_marks)
filled_data["City"] = filled_data["City"].fillna("Unknown")
print("\nAfter filling missing values:")
print(filled_data)


# ------------------------------------------------------------
# 10. SORT DATA
# ------------------------------------------------------------

# Sort by Marks from smallest to largest.
ascending_marks = df.sort_values("Marks")
print("\nMarks: low to high:")
print(ascending_marks)

# ascending=False sorts from largest to smallest.
descending_marks = df.sort_values("Marks", ascending=False)
print("\nMarks: high to low:")
print(descending_marks)


# ------------------------------------------------------------
# 11. GROUP DATA
# ------------------------------------------------------------

# groupby() puts rows into groups with the same value.
# mean() calculates the average for each group.
city_average = df.groupby("City")["Marks"].mean()
print("\nAverage marks by city:")
print(city_average)

# agg() lets us calculate more than one summary at a time.
city_summary = df.groupby("City")["Marks"].agg(["count", "mean", "max"])
print("\nCity marks summary:")
print(city_summary)


# ------------------------------------------------------------
# 12. REMOVE DUPLICATES
# ------------------------------------------------------------

duplicate_data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Aman"],
    "City": ["Delhi", "Mumbai", "Delhi"]
})

# duplicated() identifies repeated rows.
print("\nWhich rows are duplicates?")
print(duplicate_data.duplicated())

# drop_duplicates() keeps the first copy by default.
unique_data = duplicate_data.drop_duplicates()
print("\nAfter removing duplicate rows:")
print(unique_data)


# ------------------------------------------------------------
# 13. RENAME COLUMNS AND CHANGE DATA TYPES
# ------------------------------------------------------------

# rename() changes selected column names.
renamed_df = df.rename(columns={"Name": "Student_Name", "Marks": "Score"})
print("\nRenamed columns:")
print(renamed_df)

# astype() converts a column to another data type.
# For example, convert Age to text (string).
typed_df = df.copy()
typed_df["Age"] = typed_df["Age"].astype(str)
print("\nAge data type after conversion:", typed_df["Age"].dtype)


# ------------------------------------------------------------
# 14. COMBINE DATAFRAMES
# ------------------------------------------------------------

# concat() joins DataFrames vertically (one below another) by default.
class_a = pd.DataFrame({
    "Name": ["Aman", "Riya"],
    "Marks": [85, 92]
})
class_b = pd.DataFrame({
    "Name": ["Kabir", "Neha"],
    "Marks": [76, 88]
})

all_students = pd.concat([class_a, class_b], ignore_index=True)
print("\nCombined classes:")
print(all_students)

# merge() joins tables using a common column, similar to a database join.
student_details = pd.DataFrame({
    "Name": ["Aman", "Riya", "Kabir"],
    "City": ["Delhi", "Mumbai", "Delhi"]
})
student_results = pd.DataFrame({
    "Name": ["Aman", "Riya", "Kabir"],
    "Marks": [85, 92, 76]
})

combined = pd.merge(student_details, student_results, on="Name")
print("\nMerged tables:")
print(combined)


# ------------------------------------------------------------
# 15. READ AND WRITE CSV FILES
# ------------------------------------------------------------

# CSV means Comma-Separated Values. It is a common table file format.
# to_csv() saves a DataFrame to a CSV file.
# index=False prevents Pandas from saving the row index as an extra column.
df.to_csv("students.csv", index=False)

# read_csv() loads a CSV file into a DataFrame.
loaded_df = pd.read_csv("students.csv")
print("\nData loaded from students.csv:")
print(loaded_df)


# ------------------------------------------------------------
# 16. EXCEL FILES
# ------------------------------------------------------------

# To work with Excel files, install openpyxl:
# python -m pip install openpyxl
#
# Save a DataFrame to Excel:
# df.to_excel("students.xlsx", index=False)
#
# Read an Excel file:
# excel_df = pd.read_excel("students.xlsx")


# ------------------------------------------------------------
# 17. BASIC DATE HANDLING
# ------------------------------------------------------------

date_data = pd.DataFrame({
    "Student": ["Aman", "Riya", "Kabir"],
    "Joining_Date": ["2026-01-10", "2026-02-15", "2026-03-20"]
})

# Convert text dates into Pandas datetime values.
date_data["Joining_Date"] = pd.to_datetime(date_data["Joining_Date"])

# Extract useful parts of a date.
date_data["Year"] = date_data["Joining_Date"].dt.year
date_data["Month"] = date_data["Joining_Date"].dt.month
print("\nDate information:")
print(date_data)


# ------------------------------------------------------------
# 18. QUICK PRACTICE TASKS
# ------------------------------------------------------------

# Try these tasks yourself:
#
# 1. Create a DataFrame with 5 products and their prices.
# 2. Display only the product names.
# 3. Filter products with a price greater than 500.
# 4. Add a column called "Discounted_Price".
# 5. Sort products from highest price to lowest price.
# 6. Find the average product price.
# 7. Save your DataFrame as products.csv.
#
# Tip: Try first without looking up the answer. Then use the examples above.


# ------------------------------------------------------------
# END OF BEGINNER GUIDE
# ------------------------------------------------------------

print("\nGreat work! You have completed the Pandas beginner examples.")
