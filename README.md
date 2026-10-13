# Real-World Data Cleaning Pipeline

## Project Overview
This project demonstrates a real-world data cleaning pipeline using Python and the NYC Airbnb Open Data dataset.

## Objectives
- Identify and handle missing values
- Detect duplicate records
- Validate prices and remove invalid records
- Detect price outliers using the IQR method
- Convert date columns into datetime format
- Generate a data quality report
- Visualize Airbnb listing data

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset
NYC Airbnb Open Data (2019)

Source: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

## Data Cleaning Steps
1. Loaded and inspected the dataset
2. Checked missing values
3. Filled selected missing values
4. Checked duplicate records
5. Removed listings with invalid prices
6. Detected and flagged price outliers using IQR
7. Converted the last_review column to datetime
8. Exported the cleaned dataset and quality report

## Visualizations
- Airbnb price distribution
- Room type distribution
- Listings by neighbourhood group
- Average price by room type
- Average price by neighbourhood group
- Missing values comparison
- Top 10 neighbourhoods
- Room type percentage distribution
- Price comparison heatmap
- Price outlier detection

## Output Files
- output/cleaned_airbnb_data.csv
- output/data_quality_report.csv
- visualizations/

## How to Run
1. Install the required libraries.
2. Open the Jupyter Notebook.
3. Run the cells from top to bottom.

## Author
BCA Data Science Student
