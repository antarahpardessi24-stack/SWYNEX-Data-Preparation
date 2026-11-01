
import pandas as pd
import numpy as np


print("=" * 60)
print("SWYNEX TECHNOLOGIES - DATA CLEANING")
print("Netflix Movies and TV Shows")
print("=" * 60)

# STEP 1: LOAD ORIGINAL DATASET

file_path = "data/raw/netflix_titles.csv"

df = pd.read_csv(file_path)

original_rows = len(df)

print("\nOriginal Dataset Shape:", df.shape)


# STEP 2: REMOVE EXTRA SPACES

for col in df.select_dtypes(include=["str"]).columns:
    df[col] = df[col].str.strip()

print("\nExtra spaces removed.")


# STEP 3: RECOVER MISPLACED DURATION VALUES

recovery_mask = (
    df["duration"].isna()
    & df["rating"].str.match(
        r"^\d+\s*min$",
        na=False
    )
)

recovered_count = recovery_mask.sum()

df.loc[recovery_mask, "duration"] = (
    df.loc[recovery_mask, "rating"]
)

df.loc[recovery_mask, "rating"] = pd.NA

print("\nRecovered misplaced durations:", recovered_count)


# STEP 4: HANDLE MISSING CATEGORICAL VALUES

columns_to_fill = [
    "director",
    "cast",
    "country",
    "rating"
]

for col in columns_to_fill:
    df[col] = df[col].fillna("Unknown")

print("\nMissing categorical values handled.")


# STEP 5: CONVERT DATE COLUMN INTO DATETIME

df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

print("\nDate column converted into datetime.")


# STEP 6: CORRECT RELEASE YEAR DATA TYPE

df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
).astype("Int64")

print("\nRelease year data type corrected.")


# STEP 7: EXTRACT NUMERICAL DURATION AND UNIT

duration_parts = df["duration"].str.extract(
    r"^\s*(?P<duration_value>\d+)\s*(?P<duration_unit>min|seasons?)\s*$",
    flags=2
)

df["duration_value"] = pd.to_numeric(
    duration_parts["duration_value"],
    errors="coerce"
).astype("Int64")

df["duration_unit"] = (
    duration_parts["duration_unit"]
    .str.lower()
    .str.rstrip("s")
)

print("\nDuration values and units extracted.")


# STEP 8: HANDLE MISSING DURATION VALUES

df["duration"] = df["duration"].fillna("Unknown")

df["duration_unit"] = (
    df["duration_unit"].fillna("Unknown")
)

print("\nMissing duration values handled.")


# STEP 9: REMOVE EXACT DUPLICATE RECORDS

duplicate_count = df.duplicated().sum()

df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicate_count)


# STEP 10: CHECK DUPLICATE SHOW IDs

duplicate_ids = df["show_id"].duplicated().sum()

print("Duplicate show IDs:", duplicate_ids)


# STEP 11: FINAL DATA VALIDATION

print("\n" + "=" * 60)
print("FINAL DATA VALIDATION")
print("=" * 60)

print("\nOriginal Records:", original_rows)
print("Final Records:", len(df))
print("Total Columns:", len(df.columns))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nRemaining Missing Values:",
      df.isnull().sum().sum())

print("\nFinal Data Types:")
print(df.dtypes)

print("\nDuration Unit Distribution:")
print(df["duration_unit"].value_counts())

# STEP 12: SAVE CLEANED DATASET

output_path = "data/processed/netflix_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Saved Location:", output_path)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)
