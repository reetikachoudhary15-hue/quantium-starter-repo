# Pink Morsels Sales Data Processing

## Project Overview
This project processes Soul Foods transaction data to create a clean and formatted dataset for Pink Morsels sales analysis.

The input consists of three CSV files containing daily sales data across different regions and products.

## Objective
- Filter data to include only "Pink Morsels"
- Calculate total sales per row using quantity × price
- Combine all CSV files into one output file
- Retain only relevant fields for analysis

## Input Data
The data folder contains three CSV files with the following fields:
- product
- quantity
- price
- date
- region

## Processing Steps
1. Read all CSV files from the data folder
2. Filter rows where product is "Pink Morsels"
3. Create a new column called Sales (quantity × price)
4. Keep only Sales, Date, and Region fields
5. Combine data into a single output CSV file

## Output
The final output file is:
- pink_morsels_sales.csv

This file contains the following columns:
- Sales
- Date
- Region

## How to Run
From the project root directory, run:

python process_data.py

## Tools Used
- Python
- CSV module
- Git & GitHub

