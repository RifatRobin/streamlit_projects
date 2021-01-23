import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Stock Price App
The stock **Closing Price** and **Volume** of google and Apple.

""")

tsApple = 'AAPL'
ts = 'GOOGL'

tdApple = yf.Ticker(tsApple)
td = yf.Ticker(ts)

tDf = td.history(period='id', start='2010-1-1', end='2020-1-1')
tDfApple = td.history(period='id', start='2010-1-1', end='2020-1-1')

st.write("""
# Google  *(2010-2020)*  

## Closing
         """)

st.line_chart(tDf.Close)
st.write("""
## Volume
         """)
st.line_chart(tDf.Volume)


st.write("""
# Apple  *(2010-2020)*

## Closing
         """)
st.line_chart(tDf.Close)
st.write("""
## Volume
         """)
st.line_chart(tDf.Volume)
