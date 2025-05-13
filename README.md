# Clean Cafe Sales

This project focuses on cleaning and preparing a messy dataset containing cafe sales records. The dataset includes common real-world issues such as missing values, inconsistent formatting, and placeholder entries like "UNKNOWN" and "ERROR".

## Objective

The goal is to clean and transform the dataset into a consistent and usable format for further analysis or machine learning. Steps include:
- Identifying and handling missing and invalid values
- Converting text-based numbers to numeric types
- Creating additional features for time-based analysis
- Comparing calculated and reported totals

## Dataset

The original dataset `dirty_cafe_sales.csv` contains 10,000 rows and 8 columns:
- `Transaction ID`
- `Item`
- `Quantity`
- `Price Per Unit`
- `Total Spent`
- `Payment Method`
- `Location`
- `Transaction Date`

## Cleaning Steps

1. Replaced invalid values like `"ERROR"` and `"UNKNOWN"` with proper nulls (`NaN`)
2. Dropped rows with missing essential values (e.g., `Item`, `Quantity`, `Price Per Unit`)
3. Converted string-based numerical columns to `int` or `float`
4. Recalculated `Total Spent` from `Quantity * Price Per Unit` for accuracy
5. Standardized categorical values (e.g., replacing nulls in `Payment Method` and `Location` with `"Unspecified"`)
6. Parsed and validated `Transaction Date` as a datetime object
7. Created new features: `Day of Week`, `Month`

## Output

After cleaning:
- Final dataset shape: 7,773 rows x 10 columns
- Ready for exploratory data analysis or model training


