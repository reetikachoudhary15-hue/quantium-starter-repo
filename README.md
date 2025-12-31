# Pink Morsels Sales Data Processing

## Project Overview
This project processes Soul Foods transaction data to generate a clean sales dataset
focused specifically on Pink Morsels.

## Objective
- Filter data to include only Pink Morsels
- Calculate sales using quantity × price
- Combine multiple CSV files into one output file
- Keep only Sales, Date, and Region columns

## Input Data
The data folder contains three CSV files with the following columns:
- product
- quantity
- price
- date
- region

## Processing Steps
1. Read all CSV files from the data folder
2. Filter rows where product is "Pink Morsels"
3. Create a Sales column
4. Combine data into one CSV file

## Output
The final output file is:
- pink_morsels_sales.csv

Columns in output:
- Sales
- Date
- Region

## How to Run
From the root folder, run:
python process_data.py
