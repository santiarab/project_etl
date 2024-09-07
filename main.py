from pandas import read_parquet
from src.extract import extract_data_from_excel
from src.config import INPUT_DATA_DIR,DATA_DIR
from src.load import save_to_postgres
from src.transform import best_goal_diff
from src.utils import save_to_parquet,connect_to_postgres
from sqlalchemy import text


def main():
    df  = extract_data_from_excel(f'{INPUT_DATA_DIR}/world_cup_results.xlsx')
    save_to_parquet(df,f'{DATA_DIR}/parquet/world_cup_results.parquet')
    df_worlcup = read_parquet(f'{DATA_DIR}/parquet/world_cup_results.parquet')
    print(df.head())
    best_goal_diff(df_worlcup)
    # engine = connect_to_postgres("config.ini")
    # # with engine.connect() as conn:
    # #     query = """
    # #         insert into prueba values(2);
    # #         insert into prueba values(3);
    # #         insert into prueba values(4);
    # #         insert into prueba values(5)
    # #     """
    # #     conn.execute(text(query))
    # #     conn.commit()
    # # with engine.connect() as conn:
    # #     query = """
    # #         select * from prueba
    # #     """
    # #     result = conn.execute(text(query))
    # # print(result.fetchall())
    # save_to_postgres("df_worlcup",df_worlcup,engine)

if __name__ == "__main__":
    main()