# Working Hours Data Set Analysis

This repository contains data sets and analysis scripts for working hours data spanning multiple years. The raw data is divided into three forms and stored in separate Excel files for each month. The analysis pipeline involves combining the data forms, performing data cleaning, and updating the main Jupyter Notebook for statistical analysis. The final analysis includes various visualizations, statistical measures, and insights into the working hours data.

## Data

The raw data is organized as follows:

- `./data`: Contains the Python script `combine_data.py`, used to combine the different data forms for each month.
- `./data/rawdata`: Contains the three forms of raw data, each stored in separate folders:
  - `data_form1`: Contains the raw data for form 1. (5.2021-9.2022)
  - `data_form2`: Contains the raw data for form 2. (10.2022-present)
  - `data_form3`: Contains the raw data for form 3. (1.2021-4.2021)

To change the input and output directories to your local machine, update the input_dir and output_dir variables with the appropriate paths.

After running `combine_data.py`, the combined data sets for each form are stored in the following files:

- `./data/rawdata/combined_dataform1.csv`
- `./data/rawdata/combined_dataform2.csv`
- `./data/rawdata/combined_dataform3.csv`

## Data Cleaning

For each data form, there is a corresponding Jupyter Notebook for data cleaning:

- `./data_cleaning1.ipynb`: Data cleaning for form 1.
- `./data_cleaning2.ipynb`: Data cleaning for form 2.
- `./data_cleaning3.ipynb`: Data cleaning for form 3.

The cleaning process involves extracting relevant columns, handling missing values, and ensuring data consistency.

## Analysis

The main analysis is performed in the `./data_analysis.ipynb` Jupyter Notebook. The analysis includes the following visualizations and statistical measures:

- Density Plot: Visualizing the distribution of total working hours with mean and median.
- Histogram: Displaying the distribution of total working hours.
- Bar Plot: Showing aggregated statistics, such as the sum of working hours per month.
- Mean Trend Over Months: Illustrating the trend of mean working hours over time.
- Heatmap: Displaying the correlations between different variables using a heatmap.
- Visual Calendar: Visual representation of working and free days on a calendar.
- Probability Mass Function (PMF): Analyzing the probability distribution of working hours.
- Cumulative Distribution Function (CDF): Analyzing the cumulative distribution of working hours.

## Final Data

The cleaned and combined data sets from each form are merged into a single CSV file:

- `./final_data.csv`

## Supporting Files

- `thinkplot.py`: A Python module for creating various statistical visualizations.
- `thinkstats2.py`: A Python module for statistical analysis.

## Usage

1. Run `combine_data.py` to combine the different data forms for each month.
2. Use the respective data cleaning Jupyter Notebooks for each data form to clean the data.
3. Run the main `data_analysis.ipynb` Jupyter Notebook to perform the statistical analysis and generate visualizations.


To process the data automatically, follow these steps based on your operating system:

### For Windows Users (using the provided batch script):

1. Open a command prompt in the repository directory.
2. Run the `run_data_processing.bat` script by typing the following command and pressing Enter:
1. The script will automatically combine the data, perform data cleaning for each form, and complete the data processing.

### For Unix/Linux/Mac Users (using the provided bash script):

1. Open a terminal in the repository directory.
2. Run the `run_data_processing.sh` script by typing the following command and pressing Enter:

Make sure to have the required libraries and dependencies installed before running the scripts and Jupyter Notebooks.