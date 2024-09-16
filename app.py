import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st

# Get today's date and calculate start date (360 days ago)
today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

# Streamlit app
st.title("Real-time Stock Price Data")

# User input for company symbol
ticker_symbol = st.text_input("Enter Any Company Ticker Symbol (e.g. AAPL, TSLA):")

# Download data and check if ticker is valid
if ticker_symbol:
    try:
        data = yf.download(ticker_symbol, start=start_date, end=end_date)

        if not data.empty:
            # Plot the stock data
            fig, ax = plt.subplots(figsize=(12, 8))
            data['Close'].plot(ax=ax, title=f"{ticker_symbol.upper()} Stock Prices", fontsize=12)
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.grid()
            plt.legend(["Close Price"])
            
            # Display the plot
            st.pyplot(fig)
        else:
            st.error("No data found for the entered ticker symbol.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter a company ticker symbol.")
