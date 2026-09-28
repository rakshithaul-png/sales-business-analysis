# ==========================================
# SALES BUSINESS ANALYSIS
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_Business_Analysis_Project_Dataset (1).csv")
# Data Exploration

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print("duplicated rows:",df.duplicated().sum())
print(df[df.duplicated()])

# Data Cleaning
df_clean = df.drop_duplicates()
print("originalrows:",len(df))
print("clean rows:",len(df_clean))
print(df_clean[df_clean["Region"].isnull()])
print(df_clean[df_clean["Customer_Segment"].isnull()])
df_clean["Region"] = df_clean["Region"].fillna("Unknown")
df_clean["Customer_Segment"] = df_clean["Customer_Segment"].fillna("Unknown")
print(df_clean.isnull().sum())
df_clean["Order_Date"] = pd.to_datetime(df_clean["Order_Date"])
print(df_clean.dtypes)
print(df_clean.describe())

# Revenue by Region
region_revenue = df_clean.groupby("Region")["Revenue"].sum()
print(region_revenue)

# Revenue by Category
category_revenue = df_clean.groupby("Category")["Revenue"].sum()
print(category_revenue)

# Revenue by Product
product_revenue = df_clean.groupby("Product")["Revenue"].sum()
print(product_revenue.sort_values(ascending=False))
product_profit = df_clean.groupby("Product")["Profit"].sum()
print(product_profit.sort_values(ascending=False))
df_clean["Profit_Margin"] = (
    df_clean["Profit"] / df_clean["Revenue"]
) * 100

# Profit by Product
print(df_clean[["Product", "Revenue", "Profit", "Profit_Margin"]].head())
product_margin = df_clean.groupby("Product")["Profit_Margin"].mean()
# Profit Margin
print(product_margin.sort_values(ascending=False))
df_clean["Month"] = df_clean["Order_Date"].dt.to_period("M")
monthly_revenue = df_clean.groupby("Month")["Revenue"].sum()
print(monthly_revenue)

# Profit Margin by Product
monthly_profit = df_clean.groupby("Month")["Profit"].sum()
print(monthly_profit)

import matplotlib.pyplot as plt
# ==========================================
# DATA VISUALIZATION
# ==========================================

# Monthly Revenue Trend
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
category_revenue = df_clean.groupby("Category")["Revenue"].sum()
plt.figure()
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit by Product Category

category_revenue.plot(kind="bar")
category_profit = df_clean.groupby("Category")["Profit"].sum()
plt.figure()
category_profit.plot(kind="bar")
plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
region_revenue = df_clean.groupby("Region")["Revenue"].sum()

# Revenue by Region

plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Revenue by Customer Segment

segment_revenue = df_clean.groupby("Customer_Segment")["Revenue"].sum()
plt.figure()
segment_revenue.plot(kind="bar")
plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
product_quantity = df_clean.groupby("Product")["Quantity"].sum()
print(product_quantity.sort_values(ascending=False))
product_quantity = df_clean.groupby("Product")["Quantity"].sum()

# Quantity Sold by Product

plt.figure(figsize=(10, 6))
product_quantity.sort_values().plot(kind="barh")
plt.title("Quantity Sold by Product")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

df_clean.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned dataset saved successfully!")


