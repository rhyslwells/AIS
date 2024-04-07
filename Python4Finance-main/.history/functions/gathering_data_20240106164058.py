import pandas as pd
import os

def get_column_from_csv(file, col_name):
    # Reads a dataframe from the CSV file, changes index to date and returns it
    # Try to get the file and if it doesn't exist issue a warning
    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df[col_name]
    
def get_stock_df_from_csv(folder, ticker):
    # Reads a dataframe from the CSV file, changes index to date and returns it
    # Try to get the file and if it doesn't exist issue a warning
    try:
        file_path = os.path.join(folder, ticker + ".csv")
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df