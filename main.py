import yfinance as yf
from datetime import datetime, timedelta

x=datetime.now()
date_N_days_ago = datetime.now() - timedelta(days=7)


msft = yf.Ticker("MSFT")

# get stock info

# print(msft.info)

# # get historical market data
# hist = msft.history(period="10d")
data_df = yf.download("MSFT", start=date_N_days_ago.strftime("%Y"+"-"+"%m"+"-"+"%d"), interval="1m", end=x.strftime("%Y"+"-"+"%m"+"-"+"%d"))
data_df.to_csv('ds.csv')

