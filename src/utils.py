from configparser import ConfigParser
import sqlalchemy as sa
import pandas as pd
import os
def save_to_parquet(df, save_path, partition_col=None):

    if not isinstance(df, pd.DataFrame):
        raise TypeError("The argument 'df' must be a Pandas DataFrame.")

    if partition_col is not None and not isinstance(partition_col, (str, list)):
        raise ValueError("The argument 'partition_col' must be a str or a str list.")

    directory = os.path.dirname(save_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    try:
        df.to_parquet(save_path, partition_cols=partition_col)
        print("DataFrame was successful saved in Parquet format.")
    except Exception as e:
        print(f"Error to save DataFrame in Parquet format: {str(e)}")


def connect_to_postgres(config_file_path="config.ini", section="postgres"):

    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"The configuration file '{config_file_path}' does not exist.")

    config = ConfigParser()
    config.read(config_file_path)
    conn_data = config[section]

    host = conn_data.get("host")
    port = conn_data.get("port")
    db = conn_data.get("db")
    user = conn_data.get("user")
    pwd = conn_data.get("pwd")

    url = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"

    conn = sa.create_engine(url)

    return conn