import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path, skiprows=1)
    return df

df = load_data(r'..\data\raw\Retail_Sales_Transactions_2024-2025_raw.csv')


# Inspect the Dataset
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.shape)

# Clean Column Names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)
df = df.dropna(how="all")
df = df.reset_index(drop=True)

# Convert Numeric Columns to Numbers
numeric_cols= ["quantity", "unit_price", "discount"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Clean text columns
text_cols = [
    "customer_name",
    "gender",
    "category",
    "product",
    "product_name_duplicate",
    "sales_channel",
    "region"
]

for col in text_cols:
    df[col] = (
        df[col]
        .astype(str)            # convert to string so .str methods don't break
        .str.strip()            # remove leading/trailing spaces
        .str.lower()            # normalize casing
        .str.replace(r"\s+", " ", regex=True) # collapse multiple spaces
    )

# Standardize Known Categories
df["category"] = df["category"].replace({
    "groceries": "groceries",
    "electronics": "electronics",
    "clothing": "clothing",
    "furniture": "furniture"
})

# Fix Gender Values
df["gender"] = df["gender"].replace({
    "male": "male",
    "female": "female",
    "": None,
    "nan": None
})

df = df.drop(columns=["product_name_duplicate"])

# Validate Region Values
df["region"] = df["region"].replace({
    "north": "north",
    "south": "south",
    "east": "east",
    "west": "west",
    "": None,
    "nan": None
})

# Validate Sales Channel
df["sales_channel"] = df["sales_channel"].replace({
    "retail": "retail",
    "wholesale": "wholesale",
    "online": "online",
    "": None,
    "nan": None
})



# Validate Numeric Ranges
df["quantity"] = df["quantity"].clip(lower=0)
df["unit_price"] = df["unit_price"].clip(lower=0)
df["discount"] = df["discount"].clip(lower=0)

# Fix negative or invalid numeric values
df["quantity"] = df["quantity"].clip(lower=0)
df["unit_price"] = df["unit_price"].clip(lower=0)

# It seems right to create a Revenue Column
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"] /100)

# Recalculate revenue
df = df[df["quantity"].notna() & df["unit_price"].notna()]
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])

# Convert order_id to clean string format
df["order_id"] = df["order_id"].astype("Int64").astype(str)

# Convert the date column
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%m-%d-%Y",
    errors="coerce"
)

# Extract useful date parts
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["weekday"] = df["order_date"].dt.day_name()

# Clean Phone Numbers
# Best practice is to write a reusable function that handles all the weird cases

import re
def clean_phone(phone):
    if pd.isna(phone):
        return None
    # Convert to string
    phone = str(phone).strip()

    # Remove everything except digits
    digits = re.sub(r"\D", "", phone)

    # Remove leading country code "91" if present
    if digits.startswith("91") and len(digits) > 10:
        digits = digits[2:]

    # Remove leading negative sign if exists
    digits = digits.lstrip("0") if digits.startswith("0") else digits 

    # If after cleaning we don't have exactly 10 digits ➡️ invalid
    if len(digits) != 10:
        return None
    
    return digits

df["phone"] = df["phone"].apply(clean_phone)


# Handling Missing Values
df = df[df["quantity"].notna()]
df["discount"] = df["discount"].fillna(0)
df["sales_channel"] = df["sales_channel"].fillna("unknown")
df["region"] = df["region"].fillna("unknown")
# Drop rows where revenue cannot be computed
df = df[df["quantity"].notna() & df["unit_price"].notna()]
# Recalculate revenue
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
# Fill missing price with median price per product
df["unit_price"] = df.groupby("product")["unit_price"].transform(lambda x: x.fillna(x.median()))
df = df[df["order_date"].notna()]


# If row is missing MOST of the field, drop it
df = df.dropna(thresh=5)

# Remove duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["order_id"], keep="first") # Order ID numbers should be uniquie.  If they are duplicate we will delete second and keep the first
df = df.drop_duplicates(
    subset=["customer_name", "product", "order_date"],
)

# Reset index after cleaning
df = df.reset_index(drop=True)

# Define valid mapping
valid_map = {
    "clothing": ["jacket", "shirt", "jeans"],
    "groceries": ["bananas", "apples", "rice"],
    "electronics": ["laptop", "mobile", "tablet"],
    "furniture": ["chair", "desk", "sofa"]
}

invalid_rows = []

for category, products in valid_map.items():
    mask = (df["category"] == category) & (~df["product"].isin(products))
    invalid_rows.append(df[mask])

invalid_df = pd.concat(invalid_rows)



df.to_csv(r"..\data\cleaned\Retail_Sales_Transactions_2024-2025_raw.csv", index=False)
