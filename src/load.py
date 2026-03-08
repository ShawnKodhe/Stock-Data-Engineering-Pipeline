import pandas as pd
from sqlalchemy import create_engine



# engine = create_engine("postgresql://postgres:EldenRing85!@localhost:5432/postgres")
#
# connection = engine.connect()
#
# connection.execute("CREATE DATABASE stocks")
def load_to_postgres():

    df = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Stock_Data_Pipeline\data\processed_stock.csv")

    engine = create_engine(
        "postgresql://postgres:EldenRing85!@localhost:5433/stocks"
    )

    df.to_sql(
        "stock_prices",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL")


if __name__ == "__main__":
    load_to_postgres()