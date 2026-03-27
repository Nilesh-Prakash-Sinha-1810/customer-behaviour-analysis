import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Data preparation
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

# Customer insights
total_spending = df.groupby("Customer_ID")["Amount"].sum()
top_customers = total_spending.nlargest(2)

orders_per_customer = df.groupby("Customer_ID")["Product"].count()

# Product insights
most_popular_product = df["Product"].value_counts().idxmax()

# Category insights
revenue_per_category = df.groupby("Category")["Amount"].sum()
top_category = revenue_per_category.idxmax()

# Time insights
daily_sales = df.groupby("Date")["Amount"].sum()
best_day = daily_sales.idxmax()

# Repeat customers
repeat_customers = df["Customer_ID"].value_counts()
repeat_customers = repeat_customers[repeat_customers > 1].index

# Average order value
avg_order_value = df.groupby("Customer_ID")["Amount"].mean()

# Pivot table
pivot = pd.pivot_table(
    df,
    index="Customer_ID",
    columns="Category",
    values="Amount",
    aggfunc="sum",
    fill_value=0
)

# Print results
print("Total Spending:\n", total_spending)
print("\nTop Customers:\n", top_customers)
print("\nOrders per Customer:\n", orders_per_customer)
print("\nMost Popular Product:", most_popular_product)
print("\nTop Category:", top_category)
print("\nDaily Sales:\n", daily_sales)
print("\nBest Day:", best_day)
print("\nRepeat Customers:", list(repeat_customers))
print("\nAverage Order Value:\n", avg_order_value)
print("\nPivot Table:\n", pivot)