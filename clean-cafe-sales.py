import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('dirty_cafe_sales.csv')

# Preview
print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):")
print(df.shape)

print("\nDataFrame Info:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicated rows:")
print(df.duplicated().sum())

print("\nGeneral statistics:")
print(df.describe(include='all'))

# Clean: Item column
print('\nITEM COLUMN')
print(df['Item'].value_counts(dropna=False))
df['Item'] = df['Item'].replace(['UNKNOWN', 'ERROR'], pd.NA)
df.dropna(subset=['Item'], inplace=True)
print('Item column after cleaning:')
print(df['Item'].value_counts(dropna=False))
print('Shape:', df.shape)

# Clean: Quantity column
print('\nQUANTITY COLUMN')
print(df['Quantity'].value_counts(dropna=False))
df['Quantity'] = df['Quantity'].replace(['UNKNOWN', 'ERROR'], pd.NA)
df.dropna(subset=['Quantity'], inplace=True)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
print('Quantity column after cleaning:')
print(df['Quantity'].value_counts(dropna=False))
print('Shape:', df.shape)

# Clean: Price Per Unit column
print('\nPRICE PER UNIT COLUMN')
print(df['Price Per Unit'].value_counts(dropna=False))
df['Price Per Unit'] = df['Price Per Unit'].replace(['UNKNOWN', 'ERROR'], pd.NA)
df.dropna(subset=['Price Per Unit'], inplace=True)
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
print('Price Per Unit column after cleaning:')
print(df['Price Per Unit'].value_counts(dropna=False))
print('Shape:', df.shape)

# Clean: Total Spent column (recalculate manually)
print('\nTOTAL SPENT COLUMN (original vs calculated)')
df['Total Spent'] = df['Total Spent'].replace(['UNKNOWN', 'ERROR'], pd.NA)
df['Total Spent Calculated'] = df['Quantity'] * df['Price Per Unit']
comparison = df[['Total Spent', 'Total Spent Calculated']].head(10)
print(comparison)
df['Total Spent'] = df['Total Spent Calculated']
df.drop(columns='Total Spent Calculated', inplace=True)
print('Shape:', df.shape)

# Clean: Payment Method column
print('\nPAYMENT METHOD COLUMN')
print(df['Payment Method'].value_counts(dropna=False))
df['Payment Method'] = df['Payment Method'].replace([np.nan, 'UNKNOWN', 'ERROR'], 'Unspecified')
print('Payment Method column after cleaning:')
print(df['Payment Method'].value_counts(dropna=False))
print('Shape:', df.shape)

# Clean: Location column
print('\nLOCATION COLUMN')
print(df['Location'].value_counts(dropna=False))
df['Location'] = df['Location'].replace([np.nan, 'UNKNOWN', 'ERROR'], 'Unspecified')
print('Location column after cleaning:')
print(df['Location'].value_counts(dropna=False))
print('Shape:', df.shape)

# Clean: Transaction Date column
print('\nTRANSACTION DATE COLUMN')
print(df['Transaction Date'].value_counts(dropna=False))
df['Transaction Date'] = df['Transaction Date'].replace(['UNKNOWN', 'ERROR'], pd.NA)
df.dropna(subset=['Transaction Date'], inplace=True)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
print('Transaction Date column after cleaning:')
print(df['Transaction Date'].value_counts(dropna=False))
print('Shape:', df.shape)

# Create temporal features: Day of Week and Month
df['Day of Week'] = df['Transaction Date'].dt.day_name()
df['Month'] = df['Transaction Date'].dt.to_period('M')

print("\nTransactions per Day of the Week:")
print(df['Day of Week'].value_counts())

print("\nTransactions per Month:")
print(df['Month'].value_counts().sort_index())

# Final summary
print("\nDATA CLEANING COMPLETE")
print("Final DataFrame shape:", df.shape)
print("Columns:", df.columns.tolist())
print("First rows:")
print(df.head())
