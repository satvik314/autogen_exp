# filename: stock_chart.py
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Downloading stock price data for NVDA and TSLA from Yahoo Finance
nvda_data = yf.download("NVDA", start="2021-01-01")
tesla_data = yf.download("TSLA", start="2021-01-01")

# Extracting the adjusted closing prices
nvda_prices = nvda_data['Adj Close']
tesla_prices = tesla_data['Adj Close']

# Plotting the stock price change YTD
plt.plot(nvda_prices.index, nvda_prices / nvda_prices.iloc[0], label='NVDA')
plt.plot(tesla_prices.index, tesla_prices / tesla_prices.iloc[0], label='TSLA')
plt.ylabel('Price Change (YTD)')
plt.legend()
plt.grid(True)
plt.show()