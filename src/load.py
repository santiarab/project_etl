import pandas as pd
from sqlalchemy import Engine


def save_to_postgres(name:str,df:pd.DataFrame, engine:Engine):
    try:
        df.to_sql(name, engine, if_exists='replace', index=False)
    except Exception as e:
        print(e)
