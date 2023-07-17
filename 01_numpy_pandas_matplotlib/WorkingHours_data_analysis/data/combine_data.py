import pandas as pd
import os
import glob

input_dir = '01_numpy_pandas_matplotlib/WorkingHours_data_analysis/data/rawdata/'
output_dir = '01_numpy_pandas_matplotlib/WorkingHours_data_analysis/data/rawdata/'

for form_dir in glob.glob(input_dir + 'data_form*'):
    form_number = form_dir.split('_')[-1]
    xlsx_files = glob.glob(form_dir + '/*.xlsx')

    combined_data = pd.DataFrame()

    for file in xlsx_files:
        data = pd.read_excel(file)
        combined_data = pd.concat([combined_data, data], ignore_index=True)

    output_csv = os.path.join(output_dir, f'combined_data{form_number}.csv')
    combined_data.to_csv(output_csv, index=False)

    print(f"Combined data {form_number} saved to: {output_csv}")

