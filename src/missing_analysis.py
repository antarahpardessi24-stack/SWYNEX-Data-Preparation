
import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv("data/raw/netflix_titles.csv")

print("=" * 55)
print("SWYNEX - MISSING VALUE ANALYSIS")
print("=" * 55)

# 1. Calculate missing values
missing_count = df.isnull().sum()

# 2. Calculate missing percentage
missing_percentage = (missing_count / len(df)) * 100

# 3. Create summary report
missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage.round(2)
})

missing_report = missing_report[
    missing_report["Missing_Count"] > 0
]

print("\nMISSING VALUE SUMMARY")
print(missing_report.sort_values(
    by="Missing_Count",
    ascending=False
))

# 4. Display rows with missing ratings
print("\nRECORDS WITH MISSING RATINGS")
print(df[df["rating"].isnull()][
    ["show_id", "title", "type", "rating"]
])

# 5. Display rows with missing duration
print("\nRECORDS WITH MISSING DURATION")
print(df[df["duration"].isnull()][
    ["show_id", "title", "type", "duration"]
])

# 6. Display rows with missing dates
print("\nRECORDS WITH MISSING DATES")
print(df[df["date_added"].isnull()][
    ["show_id", "title", "date_added"]
])

# 7. Save missing value report
missing_report.to_csv(
    "data/processed/missing_value_report.csv"
)

print("\nMissing value report saved successfully!")
