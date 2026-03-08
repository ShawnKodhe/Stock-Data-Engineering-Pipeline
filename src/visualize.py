import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_stock.csv")

plt.figure()

plt.plot(df["Date"], df["Close"])
plt.title("Stock Price Over Time")

plt.xticks(rotation=45)

plt.show()