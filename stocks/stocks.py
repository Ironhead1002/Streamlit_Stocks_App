import yfinance as yf
import streamlit as st
import pandas as pd


st.set_page_config(page_title='Stocks', page_icon=None, layout="centered")

st.header("""
    Stock Price
""")

symbol = st.text_input(label='Input Ticker Symbol', value='GOOGL')
data = yf.Ticker(symbol)

try :
    st.write("")
    st.write(f' #### Stock data of {data.info["shortName"]}')
    df = data.history(period='max')

    st.write(' #### Closing Price ')
    st.line_chart(df.Close)
    st.write(f'Current Price is {data.info["currentPrice"]}')
    st.write("")
    st.write("")

    st.write(' #### Volume Price ')
    st.line_chart(df.Volume)
    st.write(f'Current Volume is {data.info["volume"]}')
    st.write("")
    st.write("")

    st.write(' #### News')
    news = data.news
    for i in news:
        st.write(f' ##### {i["title"]}')
        st.write(f'Publisher: {i["publisher"]}')
        st.write(f'{i["link"]}')
        st.write("")
        st.write("")

except:
    st.write(' # Sorry No Company Found with this Symbol ')
