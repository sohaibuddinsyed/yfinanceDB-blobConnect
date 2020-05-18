import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

# print(msft.info)

# # get historical market data
# hist = msft.history(period="10d")
data_df = yf.download("MSFT", start="2020-05-01", interval="5m",end="2020-05-17")
data_df.to_csv('aapl.csv')