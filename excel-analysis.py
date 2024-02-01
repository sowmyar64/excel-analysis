
import pandas as pd
import logging as logger

# Configure logging to write messages to a file
logger.basicConfig(filename='app.log', level=logger.INFO, format='%(asctime)s - %(message)s')


try:
    # Define variables for file paths
    input_file_path = r'D:\heart.csv'
    output_file_path = r'D:\heart-excel.xlsx'

    # Debug: Output the paths for verification
    logger.debug(f'CSV file path: {input_file_path}')
    logger.debug(f'Excel file path: {output_file_path}')

    # Read the first 50 rows of the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file_path, nrows=50)

    # Debug: Output information about the DataFrame
    logger.debug(f'DataFrame shape: {df.shape}')
    logger.debug(f'DataFrame columns: {df.columns}')

    # Check if the DataFrame is empty and issue a warning
    if df.empty:
        logger.warning('The DataFrame is empty.')

    # Write the DataFrame to an Excel file
    df.to_excel(output_file_path, index=False)

    # Check if the CSV file contains fewer than 50 rows and issue a warning
    if len(df) < 50:
        logger.warning('The CSV file contains fewer than 50 rows.')

    logger.info(f'Excel file created at: {output_file_path}')

    # Read the Excel file back into a DataFrame
    df_excel = pd.read_excel(output_file_path)

    # Debug: Output information about the Excel DataFrame
    logger.debug(f'Excel DataFrame shape: {df_excel.shape}')
    logger.debug(f'Excel DataFrame columns: {df_excel.columns}')

    print("First few rows of the Excel file:")
    print(df_excel.head())

except FileNotFoundError as e:
    logger.error(f'File not found: {e}', exc_info=True)
except PermissionError as e:
    logger.error(f'Permission error: {e}', exc_info=True)
except Exception as e:
    logger.error(f'An unexpected error occurred: {e}', exc_info=True)
