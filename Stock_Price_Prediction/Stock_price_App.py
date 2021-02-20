# importing libraries
import yfinance as yf  # to get stock data
import streamlit as st
import pandas as pd

# header for website in markdown language
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and **volume** of Google!
""")

# Source:
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# define the ticker symbol
tickerSymbol = 'GOOGL'  # for google

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# retreive the historical prices for google ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-2-14')
print(tickerDf)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
