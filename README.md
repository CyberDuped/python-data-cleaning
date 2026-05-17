# Retail Sales Data Cleaning Pipeline (Python)

## 📌 Project Summary
This project showcases a complete, end‑to‑end data cleaning and validation pipeline built in Python using Pandas and NumPy. The dataset originated from multiple inconsistent sources and contained real‑world issues such as missing values, invalid phone numbers, inconsistent text formatting, incorrect data types, duplicate records, and mismatched category/product labels.

The final output is a fully cleaned, validated, analysis‑ready dataset suitable for dashboards, exploratory analysis, and downstream reporting workflows.

---

## 🧹 Key Features

### ✔ Modular Cleaning Pipeline
- Standardized column names and normalized text fields  
- Enforced numeric and date types  
- Parsed and extracted date components (year, month, weekday)  
- Cleaned and validated phone numbers using custom logic  
- Normalized category and product labels  

### ✔ Data Quality & Validation
- Applied business‑rule checks (category ↔ product consistency)  
- Removed exact and logical duplicates  
- Filled safe categorical fields (sales_channel, region) with `"unknown"`  
- Left appropriate fields (gender, phone) as `NaN` when values were truly missing  
- Dropped rows where revenue could not be computed  

### ✔ Feature Engineering
- Calculated revenue using:  
  `quantity * unit_price * (1 - discount)`  
- Added temporal features for downstream analysis  

---

## 📁 Repository Structure

```
retail-cleaning-project/
│
├── data/
│   ├── raw_retail_sales.csv
│   └── cleaned_retail_sales.csv
│
├── src/
│   └── clean_data.py
│
└── README.md
```

---

## 🛠️ Tech Stack
- Python 3  
- Pandas  
- NumPy
- Re  

---

## 🚀 How to Run

```bash
python src/cleaning_pipeline.py
```

This executes the full cleaning pipeline and exports:

```
cleaned_retail_sales.csv
```

---

## 📊 Outcome
The final dataset is:

- Clean  
- Validated  
- Deduplicated  
- Type‑safe  
- Ready for EDA, dashboards, and reporting  

This project demonstrates practical, job‑ready data‑cleaning skills that translate directly to real analytics workflows.

---


Feel free to explore the repository or reach out with questions or suggestions.
 

GitHub: (https://github.com/CyberDuped) 
LinkedIn: (https://linkedin.com/in/rmdj)


