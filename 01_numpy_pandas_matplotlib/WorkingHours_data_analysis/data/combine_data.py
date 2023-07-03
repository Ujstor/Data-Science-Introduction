import pandas as pd
import glob

xlsx_dir = '01_numpy_pandas_matplotlib/working_data_analysis/data/rawdata/data_form1/'
xlsx_files = glob.glob(xlsx_dir + '*.xlsx')

combined_data = pd.DataFrame()

for file in xlsx_files:
    data = pd.read_excel(file)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

output_csv = '01_numpy_pandas_matplotlib/working_data_analysis/data/combined_data1.csv'
combined_data.to_csv(output_csv, index=False)

