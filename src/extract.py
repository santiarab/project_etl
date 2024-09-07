import pandas as pd

def extract_data_from_excel(excel_file) -> pd.DataFrame :
    try:
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        print(e)

def extract_data_from_parquet(excel_file) -> pd.DataFrame :
    try:
        df = pd.read_parquet(excel_file)
        return df
    except Exception as e:
        print(e)