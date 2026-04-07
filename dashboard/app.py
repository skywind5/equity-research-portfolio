import streamlit as st
import yfinance as yf

st.title("Stock Analysis Dashboard")

ticker = st.text_input("Enter Stock Ticker", "META")

stock = yf.Ticker(ticker)
hist = stock.history(period="1y")

st.line_chart(hist["Close"])

st.write(stock.info)