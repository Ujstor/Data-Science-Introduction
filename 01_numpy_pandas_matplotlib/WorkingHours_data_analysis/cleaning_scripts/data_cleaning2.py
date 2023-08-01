import pandas as pd

# Read the input CSV file
df = pd.read_csv('data/rawdata/combined_dataform2.csv')

# Filter rows for a specific 'Personal' (id)
df = df[(df['Personal'] == 'Stipan Aleksandar')]

# Drop rows with 'Tag' values 'Beginn Arbeit' or 'Beginn Pause'
df = df.drop(df[(df['Tag'] == 'Beginn Arbeit') | (df['Tag'] == 'Beginn Pause')].index)

# Rename columns
df.rename(columns={'Personal': 'id', 'Tag': 'date', 'T.Summe': 'drive_time_min', 'T.Pause': 'pause_had_min', 'gesetzl. Pause': 'pause_should_min'}, inplace=True)

# Drop unnecessary columns
clean_columns = df.drop(['T.Summe (-Pause)', 'Verdienst', 'Soll', '+- Diff.'], axis=1)

# Convert columns to integers
clean_columns['drive_time_min'] = clean_columns['drive_time_min'].astype(int)
clean_columns['pause_had_min'] = clean_columns['pause_had_min'].astype(int)
clean_columns['pause_should_min'] = clean_columns['pause_should_min'].astype(int)

# Convert 'date' column to datetime format
clean_columns['date'] = clean_columns['date'].str.strip()
clean_columns['date'] = pd.to_datetime(clean_columns['date'], format='%d.%m.%Y', errors='coerce')

# Update DataFrame with cleaned columns
cleaned_data = clean_columns

# Calculate 'total_time_hour' column
cleaned_data['drive_time_min'] = cleaned_data['drive_time_min'] - cleaned_data['pause_should_min']
cleaned_data['total_time_hour'] = (cleaned_data['drive_time_min'] + cleaned_data['pause_should_min']) / 60

# Sort DataFrame by 'date' column
cleaned_data.sort_values(by='date', inplace=True)

# Save cleaned data to CSV file
cleaned_data.to_csv('cleaned_data2.csv', index=False)
