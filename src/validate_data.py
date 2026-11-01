
import pandas as pd
import os

print("=" * 55)
print("SWYNEX - FINAL DATA VALIDATION")
print("=" * 55)

# Load cleaned dataset
file_path = "data/processed/netflix_cleaned.csv"
df = pd.read_csv(file_path)

# 1. Check dataset shape
print("\n1. DATASET SHAPE")
print(df.shape)

# 2. Check missing values
print("\n2. MISSING VALUES")
print(df.isnull().sum())

# 3. Check duplicates
print("\n3. DUPLICATE RECORDS")
print(df.duplicated().sum())

# 4. Check unique IDs
print("\n4. UNIQUE SHOW IDs")
print("Unique IDs:", df["show_id"].nunique())
print("Total records:", len(df))

# 5. Check duration units
print("\n5. DURATION UNIT COUNTS")
print(df["duration_unit"].value_counts())

# 6. Check date data type
print("\n6. DATE COLUMN TYPE")
print(pd.to_datetime(df["date_added"]).dtype)

# 7. Check file size
print("\n7. FILE INFORMATION")
print("File exists:", os.path.exists(file_path))
print("File size:", round(os.path.getsize(file_path) / 1024, 2), "KB")

print("\nVALIDATION COMPLETED!")
