# This script demonstrate fundamental data science steps.
# It can be expanded by adding more complex data cleaning, feature engineering, statistical modeling, or advanced visualizaiton based on the specific project goals.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Data loading
# Replace products.csv with your actual data file path
try:
  df = pd.read_csv('products.csv')
  print("Data Loaded Successfully.")
except FileNotFoundError:
  print("Error: 'products.csv' not found. Please ensure the file is in the correct directory.")
  exit()

# 2. Data Exploration and Cleaning (Basic)"
print("\n---Intial Data Info---")
df.info()  # Python is case-sensitive so Info() will be treated as different than info()
print("\n---First 5 Rows---")
print(df.head(5))
print(df.isnull().sum())

# Cleaning: fill missing "Price" values with the mean
if 'Price' in df.columns and df['Price'].isnull().any():
  df['Price'].fillna(df['Price'].mean(), inplace=True)
  print("\nFilled missing 'Price' values with the mean.")

# 3. Data Analysis and Visualization
print("\nBasic Statistics for Numerical Columns---")
print(df.describe())

# Visualization: Distribution of Products Prices
if 'Price' in df.columns:
  plt.figure(figsize=(8,6))
  sns.histplot(df['Price'], kde=True)
  plt.title('Distribution of Product Prices')
  plt.xlabel('Price')
  plt.ylabel('Frequency')
  plt.grid(True)
  plt.show()

# Analysis: Count of products by category
if 'Category' in df.columns:
  category_counts = df['Category'].value_counts()
  print("\n---Product Counts by Category---")
  print(category_counts)


  plt.figure(figsize=(10,7))
  sns.barplot(x=category_counts.index, y= category_counts.values)
  plt.title('Number of Products per Category')
  plt.xlabel('Category')
  plt.ylabel('Number of Products')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

print("\nData Analysis Complete.")

