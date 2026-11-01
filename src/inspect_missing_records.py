
import pandas as pd

# Load original dataset
df = pd.read_csv("data/raw/netflix_titles.csv")

print("=" * 60)
print("SWYNEX - MISSING RECORD INVESTIGATION")
print("=" * 60)

# 1. Missing ratings
print("\n1. TITLES WITH MISSING RATINGS")

rating_missing = df[df["rating"].isnull()]

print(rating_missing[
    ["show_id", "title", "type", "release_year", "duration"]
].to_string(index=False))


# 2. Missing durations
print("\n2. TITLES WITH MISSING DURATIONS")

duration_missing = df[df["duration"].isnull()]

print(duration_missing[
    ["show_id", "title", "type", "release_year", "rating"]
].to_string(index=False))


# 3. Missing dates
print("\n3. TITLES WITH MISSING DATES")

date_missing = df[df["date_added"].isnull()]

print(date_missing[
    ["show_id", "title", "type", "release_year"]
].to_string(index=False))


print("\nInvestigation completed!")
