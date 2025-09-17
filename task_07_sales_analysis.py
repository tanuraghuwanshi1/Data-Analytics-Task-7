# Task 07: Visualizing Sales Trends and Customer Behavior
# Dataset: Superstore Sales Dataset (uploaded CSV)
# Author: Internship Task Submission

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv('superstore_sales_dataset.csv')

# Quick look at data
print(df.head())
print(df.info())

# ------------------- Exploratory Data Analysis -------------------

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sales trends over time
sales_trend = df.groupby('Order Date')['Sales'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=sales_trend, x='Order Date', y='Sales')
plt.title('Sales Trend Over Time')
plt.savefig('sample_output/sales_trend.png')
plt.close()

# Category-wise sales
plt.figure(figsize=(8,6))
sns.barplot(data=df, x='Category', y='Sales', estimator=sum)
plt.title('Total Sales by Category')
plt.savefig('sample_output/category_sales.png')
plt.close()

# Customer segmentation (top 10 customers by sales)
top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(10).reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=top_customers, x='Sales', y='Customer Name')
plt.title('Top 10 Customers by Sales')
plt.savefig('sample_output/top_customers.png')
plt.close()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['Sales','Profit','Discount','Quantity']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('sample_output/correlation_heatmap.png')
plt.close()

# Interactive line chart using Plotly
fig = px.line(sales_trend, x='Order Date', y='Sales', title='Interactive Sales Trend')
fig.write_html('sample_output/interactive_sales_trend.html')

print("Analysis complete. Charts saved in sample_output folder.")
