# SWYNEX Technologies – Data Preparation

### Task 1: Netflix Movies and TV Shows Dataset

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-purple)
![Status](https://img.shields.io/badge/Project-Completed-success)

## Project Overview

This project was completed as part of my Data Science Internship at **SWYNEX Technologies**.

The objective was to prepare a publicly available dataset for data science work by performing data inspection, missing value treatment, data type correction, duplicate detection, data cleaning, and validation.

For this task, I selected the Netflix Movies and TV Shows dataset from Kaggle.

## Dataset Information

**Dataset:** Netflix Movies and TV Shows

**Source:** [Kaggle – Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

| Description | Details |
|---|---|
| Original Records | 8,807 |
| Original Columns | 12 |
| Final Records | 8,807 |
| Final Columns | 14 |
| Format | CSV |

The dataset contains information about Netflix movies and television shows, including titles, directors, cast, countries, release years, ratings, durations, and genres.

## Technologies Used

- Python
- Pandas
- NumPy
- VS Code
- Git and GitHub

## Project Workflow

### 1. Data Inspection
- Loaded the dataset using Pandas.
- Examined the number of rows and columns.
- Inspected column names and data types.
- Identified missing values.
- Checked duplicate records.

### 2. Missing Value Analysis

Missing values were identified in six columns.

| Column | Missing Records |
|---|---:|
| Director | 2,634 |
| Country | 831 |
| Cast | 825 |
| Date Added | 10 |
| Rating | 4 |
| Duration | 3 |

### 3. Data Cleaning

The following operations were performed:

- Replaced missing director, cast, and country values with `Unknown`.
- Investigated missing ratings and durations.
- Recovered three misplaced duration values from the rating column.
- Replaced unresolved missing ratings with `Unknown`.
- Converted the date_added column into datetime format.
- Converted release_year into a nullable integer type.
- Extracted numerical duration values and duration units.
- Removed unnecessary whitespace.
- Checked and removed duplicate records.

### 4. Data Validation

The cleaned dataset was independently validated to check:

- Dataset dimensions.
- Missing values.
- Duplicate records.
- Unique show IDs.
- Duration unit distribution.
- Date data types.
- Output file existence.

## Final Results

| Validation Metric | Result |
|---|---:|
| Original Records | 8,807 |
| Final Records | 8,807 |
| Total Columns | 14 |
| Duplicate Records | 0 |
| Unique Show IDs | 8,807 |
| Missing Ratings | 0 |
| Missing Duration Entries | 0 |
| Missing Dates | 10 |

### Duration Distribution

| Duration Type | Records |
|---|---:|
| Movies (Minutes) | 6,131 |
| TV Shows (Seasons) | 2,676 |
| Total | 8,807 |

The ten missing date values were intentionally preserved because reliable replacement information was unavailable.

## Repository Structure

```text
SWYNEX-Data-Preparation/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── netflix_cleaned.csv
│       └── missing_value_report.csv
│
├── src/
│   ├── inspect_data.py
│   ├── missing_analysis.py
│   ├── inspect_missing_records.py
│   ├── clean_data.py
│   └── validate_data.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

The original raw dataset is not included in this repository. It can be downloaded from the Kaggle source linked above.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/antarahpardessi24-stack/SWYNEX-Data-Preparation.git
```

### 2. Navigate to the project folder

```bash
cd SWYNEX-Data-Preparation
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

Download the Netflix dataset from Kaggle and place `netflix_titles.csv` inside:

```text
data/raw/
```

### 5. Run the scripts

```bash
python src/inspect_data.py
python src/missing_analysis.py
python src/inspect_missing_records.py
python src/clean_data.py
python src/validate_data.py
```

## Key Learnings

Through this project, I gained practical experience in:

- Data preprocessing using Python and Pandas.
- Missing value analysis and treatment.
- Data type conversion.
- Duplicate detection.
- String manipulation and regular expressions.
- Data validation and quality checks.
- Organizing data science projects.
- Using Git and GitHub for version control.

## Conclusion

This project demonstrates the complete data preparation workflow, from loading a raw dataset to cleaning, transforming, and validating the final dataset.

All 8,807 original records were preserved, and the cleaned dataset was successfully generated and validated.

I would like to thank **SWYNEX Technologies** for providing this opportunity to gain practical experience in data science and data preparation.

---

**Internship Project – SWYNEX Technologies**

**Task 1: Data Preparation**

**Developed using Python and Pandas.**
