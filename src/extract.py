import yfinance as yf
import pandas as pd


def extract_stock_data(ticker="HIMS", period="1y"):
    stock = yf.Ticker(ticker)

    df = stock.history(period=period)

    df.reset_index(inplace=True)

    df.to_csv(r"E:\PYCHARM\PycharmProjects\Stock_Data_Pipeline\data\raw_stock_hims_and_hers.csv", index=False)

    print("Data extracted successfully")

    return df


if __name__ == "__main__":
    extract_stock_data()