Security‑Aware Data Cleaning Pipeline (Python)
A structured, professional data‑cleaning workflow built using Python, Pandas, and Jupyter Notebook.
This project demonstrates how to transform a messy real‑world dataset — Health Inspection Scores (2016–2019) — into a clean, analysis‑ready format while applying secure and reliable data‑handling practices.

📌 Project Overview
This project focuses on building a reproducible, security‑aware data cleaning pipeline.
The dataset contains restaurant health inspection results, including inspection dates, scores, business names, risk categories, and violation details.

The goal is to:

Load raw data safely

Inspect and validate its structure

Clean and standardize fields

Handle missing values

Correct data types

Remove duplicates

Apply security‑aware validation rules

Export a clean dataset for analysis

🧠 Skills Demonstrated
Python (Pandas, NumPy)

Data Cleaning & Transformation

Exploratory Data Analysis (EDA)

Data Validation & Quality Checks

Secure Data Handling

Jupyter Notebook Workflow

GitHub Project Organization

📂 Folder Structure
Code
Python-Data-Cleaning/
│
├── data/
│   ├── raw/
│   │   └── health.csv
│   └── cleaned/
│       └── health_cleaned.csv
│
├── notebooks/
│   └── cleaning_pipeline.ipynb
│
├── src/
│   └── cleaning_pipeline.py
│
├── README.md
└── requirements.txt
Folder Purpose
data/raw/ → Original dataset (never modified)

data/cleaned/ → Output from the cleaning pipeline

src/ → Python scripts for the cleaning workflow

notebooks/ → EDA and visual exploration

README.md → Project documentation

requirements.txt → Python dependencies

⚙️ Pipeline Steps
1. Load & Inspect Data
Load CSV using a reusable load_data() function

Preview structure with df.head()

Inspect schema using df.info()

Identify missing values, duplicates, and data types

2. Clean Column Names
Standardize for consistency:

lowercase

remove spaces

replace spaces with underscores

3. Handle Missing Values
Fill numeric missing values with median

Fill categorical missing values with "Unknown" or "Not Specified"

Identify columns requiring special handling

4. Convert Data Types
Convert inspection dates to datetime

Convert scores to numeric

Ensure ZIP codes and IDs are strings

5. Remove Duplicates
Drop exact duplicate rows

Identify potential business‑level duplicates

6. Normalize Text Fields
Standardize business names

Strip whitespace

Fix inconsistent casing

7. Security‑Aware Validation
Apply rules to ensure data integrity:

Remove impossible scores (e.g., >100 or <0)

Remove future inspection dates

Validate risk categories

Flag suspicious or malformed entries

8. Export Cleaned Dataset
Save cleaned output to:

Code
data/cleaned/health_cleaned.csv
📊 Exploratory Data Analysis (EDA)
The Jupyter Notebook includes:

Missing value heatmaps

Score distributions

Risk category breakdowns

Before/after cleaning comparisons

Outlier detection

🚀 How to Run the Project
1. Install dependencies
Code
pip install -r requirements.txt
2. Run the cleaning script
From inside the src/ folder:

Code
python cleaning_pipeline.py
3. Open the notebook
Code
jupyter notebook notebooks/cleaning_pipeline.ipynb
🔒 Security‑Aware Focus
This project emphasizes data integrity and safe handling, including:

Avoiding modification of raw data

Validating date ranges

Ensuring numeric fields are within expected bounds

Preventing accidental exposure of sensitive fields

Creating reproducible cleaning steps

📈 Results
After cleaning:

Missing values reduced

Column names standardized

Data types corrected

Duplicate rows removed

Invalid scores filtered

Clean dataset ready for analysis or dashboarding

📬 Contact
Created by Ronald Duplessis Jr  
Aspiring Data Analyst — Healthcare & Supply Chain
GitHub: (https://github.com/CyberDuped) 
LinkedIn: (https://linkedin.com/in/rmdj)


