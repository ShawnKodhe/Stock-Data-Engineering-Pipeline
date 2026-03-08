import pandas as pd

def transform_stock_data():

    df = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Stock_Data_Pipeline\data\raw_stock.csv")

    df["Daily_Return"] = df["Close"].pct_change()

    df["MA_7"] = df["Close"].rolling(window=7).mean()
    df["MA_30"] = df["Close"].rolling(window=30).mean()

    df = df.dropna()

    df.to_csv(r"E:\PYCHARM\PycharmProjects\Stock_Data_Pipeline\data\processed_stock.csv", index=False)

    print("Data transformed successfully")

    return df


if __name__ == "__main__":
    transform_stock_data()