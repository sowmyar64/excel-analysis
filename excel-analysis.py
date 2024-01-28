
import pandas as pd


# Path to your CSV file
csv_file_path = 'D:\heart.csv'

# Read the first 50 rows of the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path, nrows=50)

# Path for the Excel file you want to create
excel_file_path = 'D:\heart-excel.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f'Excel file created at: {excel_file_path}')

# Read the Excel file back into a DataFrame
df_excel = pd.read_excel(excel_file_path)

# Print the first few rows of the DataFrame
print("First few rows of the Excel file:")
print(df_excel.head())
