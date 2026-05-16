import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data(r'..\data\raw\Health_Inspection_Scores__2016-2019_.csv')
# print(df.head())
# print(df.info())
# print(df.describe(include="all"))
# print(df.isnull().sum())
# print(df.duplicated().sum())

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

df["inspection_score"] = df["inspection_score"].fillna(df["inspection_score"].median())
df["risk_category"] = df["risk_category"].fillna("Not Specified")
df["business_postal_code"] = df["business_postal_code"].fillna("Unknown")
df["business_latitude"] = df["business_latitude"].fillna("None")
df["business_longitude"] = df["business_longitude"].fillna("None")
df["business_location"] = df["business_location"].fillna("None")
df["business_phone_number"] = df["business_phone_number"].fillna("Unknown")
df["violation_id"] = df["violation_id"].fillna("Unknown")
df["violation_description"] = df["violation_description"].fillna("Unknown")
print(df.isnull().sum())



