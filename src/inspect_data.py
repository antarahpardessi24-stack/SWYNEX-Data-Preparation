import pandas as pd
import numpy as np

print("=" * 50)
print("SWYNEX - NETFLIX DATA PREPARATION")
print("=" * 50)

# Step 1: Load dataset
file_path = "data/raw/netflix_titles.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")

# Step 2: Display dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Step 3: Display first five rows
print("\nFirst Five Records:")
print(df.head())

# Step 4: Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 5: Display dataset information
print("\nDataset Information:")
df.info()

# Step 6: Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 7: Display duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nInitial inspection completed!")
