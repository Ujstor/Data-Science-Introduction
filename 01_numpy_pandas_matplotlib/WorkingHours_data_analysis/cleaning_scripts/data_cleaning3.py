import pandas as pd

# Read the input CSV file
df = pd.read_csv('data/rawdata/combined_dataform3.csv')

# Rename columns
df.rename(columns={'Unnamed: 0': 'id', 'Unnamed: 1': 'date', 'Unnamed: 2': 'drive_time_min', 'Unnamed: 4': 'pause_had_min'}, inplace=True)

# Filter rows for a specific 'id'
clean = df.loc[df['id'] == 'Stipan Alexander']

# Drop unnecessary columns
clean_columns = clean.drop(['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 3'], axis=1)

# Update DataFrame with cleaned columns
df = clean_columns

# Convert 'drive_time_min' column to integer
df['drive_time_min'] = df['drive_time_min'].astype(int)

# Filter out rows with 'drive_time_min' greater than 1000
df = df.drop(df[df['drive_time_min'] > 1000].index)

# Fill missing values in 'pause_should_min' column with 'pause_had_min' values
df['pause_had_min'] = df['pause_had_min'].astype(int)
df['pause_should_min'] = df['pause_had_min']

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
df['date'] = pd.to_datetime(df['date'])

# Drop rows with 'drive_time_min' less than 180
df = df.drop(df[df['drive_time_min'] < 180].index)

# Calculate 'total_time_hour' column
df['total_time_hour'] = (df['drive_time_min'] + df['pause_should_min']) / 60

# Update 'id' column to 'Stipan Aleksandar'
df['id'] = 'Stipan Aleksandar'

# Save cleaned data to CSV file
df.to_csv('cleaned_data3.csv', index=False)

