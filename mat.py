import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r"C:\Users\sindh\Downloads\sales_data.xlsx")


fig, axs = plt.subplots(2, 2, figsize=(12, 8))


region_sales = df.groupby("Region")["Sales"].sum()
axs[0, 0].bar(region_sales.index, region_sales.values, color="skyblue", edgecolor="black")
axs[0, 0].set_title("Total Sales by Region")
axs[0, 0].set_ylabel("Sales")
axs[0, 0].grid(axis="y", linestyle="--", alpha=0.7)

month_profit = df.groupby("Month")["Profit"].sum()
axs[0, 1].plot(month_profit.index, month_profit.values, marker="o", color="green")
axs[0, 1].set_title("Monthly Profit Trend")
axs[0, 1].set_ylabel("Profit")
axs[0, 1].grid(True)


category_sales = df.groupby("Category")["Sales"].sum()
axs[1, 0].pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%", startangle=90)
axs[1, 0].set_title("Sales Share by Category")


axs[1, 1].scatter(df["Sales"], df["Profit"], color="purple", alpha=0.7)
axs[1, 1].set_title("Sales vs Profit")
axs[1, 1].set_xlabel("Sales")
axs[1, 1].set_ylabel("Profit")
axs[1, 1].grid(True)


plt.tight_layout()
plt.show()
