import pandas as pd
import logging as logger

# Configure logging to write messages to a file
logger.basicConfig(filename='app.log', level=logger.INFO, format='%(asctime)s - %(message)s')


def read_csv_and_create_excel(input_file_path, output_file_path):
    """
    Read the first 50 rows of the CSV file, write to an Excel file, and log information.
    """
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


def read_excel_file(excel_file_path):

    # Read the Excel file back into a DataFrame
    df_excel = pd.read_excel(excel_file_path)

    # Debug: Output information about the Excel DataFrame
    logger.debug(f'Excel DataFrame shape: {df_excel.shape}')
    logger.debug(f'Excel DataFrame columns: {df_excel.columns}')


def main():
    # Define variables for file paths
    input_file_path = r'D:\heart.csv'
    output_file_path = r'D:\heart-excel.xlsx'

    # Process CSV and create Excel file
    read_csv_and_create_excel(input_file_path, output_file_path)

    # Process the created Excel file
    read_excel_file(output_file_path)


if __name__ == "__main__":
    main()
