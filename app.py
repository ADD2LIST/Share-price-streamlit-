import streamlit as st

import pandas as pd

from nsepy import get_history

import matplotlib.pyplot as plt

def get_stock_data(symbol, start_date, end_date):

    # Fetch historical stock data

    stock_data = get_history(symbol=symbol,

                             index=True,

                             start=start_date,

                             end=end_date)

    return stock_data

def get_current_price(symbol):

    # Fetch current stock price

    stock_data = get_history(symbol=symbol,

                             index=True,

                             start=pd.Timestamp.now() - pd.DateOffset(1),

                             end=pd.Timestamp.now())

    current_price = stock_data['Close'].iloc[-1]

    return current_price

def plot_historical_data(stock_data):

    plt.figure(figsize=(10, 5))

    plt.plot(stock_data.index, stock_data['Close'])

    plt.xlabel('Date')

    plt.ylabel('Closing Price')

    plt.title('Historical Stock Price')

    plt.xticks(rotation=45)

    st.pyplot(plt)

def main():

    st.title('Indian Stock Price Analysis')

    # Get user input - stock symbol and date range

    symbol = st.text_input('Enter stock symbol (e.g., RELIANCE for Reliance Industries):')

    start_date = st.date_input('Enter start date:')

    end_date = st.date_input('Enter end date:')

    if st.button('Get Data'):

        if symbol:

            # Retrieve stock data

            stock_data = get_stock_data(symbol, start_date, end_date)

            if not stock_data.empty:

                # Display current stock price

                current_price = get_current_price(symbol)

                st.subheader('Current Price')

                st.write(f'Price of {symbol}: {current_price}')

                # Display historical stock data

                st.subheader('Historical Data')

                st.dataframe(stock_data.tail())

                # Plot historical data

                plot_historical_data(stock_data)

            else:

                st.write('No data available for the specified stock symbol and date range.')

        else:

            st.write('Please enter a stock symbol.')

if __name__ == '__main__':

    main()


    
            
