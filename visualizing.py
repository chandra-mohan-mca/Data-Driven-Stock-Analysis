import streamlit as st
import pandas as pd
import plotly.express as px
from pymysql.cursors import DictCursor
import pymysql
import seaborn as sns
import matplotlib.pyplot as plt


# Database Connection Function

def get_connection():
    return pymysql.connect(
        host="localhost",          
        user="root",
        password="Chandru$04",
        database="powerbi",
        cursorclass=DictCursor 
    )


# Data Fetching Function

def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    cursor.close()
    return df


menu = st.sidebar.selectbox("Choose Analysis Type", 
                            ["Top 5 Gainers/Losers", 
                             "Volatility Analysis", 
                             "Cumulative Return", 
                             "Sector-wise Performance", 
                             "Stock Price Correlation"])


# Top 5 Gainers & Losers

if menu == "Top 5 Gainers/Losers":
    st.header("📊 Top 5 Gainers and Losers")

    agree = st.checkbox("Provide Monthly Breakdowns Of The Top-Performing And Worst-Performing Stocks.")
    if agree:
        st.success("Great!")

        if st.button('Click Results',key='filter_button_1'):
            
            st.balloons()

            df = fetch_data("SELECT * FROM gainer_to_5")  

            df.sort_values("Monthly_Return", ascending=False, inplace=True)

            df1=fetch_data("select * from losers_top_5")
            df1.sort_values("Monthly_Return",ascending=False,inplace=True)
    
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Top 5 Gainers")
                st.dataframe(df)
            with col2:
                st.subheader("Top 5 Losers")
                st.dataframe(df1)

            col3, col4 = st.columns(2)

            with col3:
                fig = px.bar(df, x="Ticker", y="Monthly_Return", title="Top 10 Gainers")
                st.plotly_chart(fig)
            with col4:
                fig1=px.bar(df1,x='Ticker',y='Monthly_Return',title='Top 5 Lossers')
                st.plotly_chart(fig1)




# Volatility Analysis

elif menu == "Volatility Analysis":
    st.header("📉 Top 10 Volatility Analysis")
    
    agree = st.checkbox("Visualize The Volatility Of Each Stock Over The Past Year By Calculating The Standard Deviation Of Daily Returns.")
    if agree:
        st.success("Great!")

        if st.button('Click Results',key='filter_button_2'):
            
            st.balloons()

            df2 = fetch_data("SELECT * FROM top_10_volatility")

            df2.sort_values("Volatility",ascending=False,inplace=True)
            st.dataframe(df2)

            fig = px.bar(df2, x='Ticker', y='Volatility', title="Top 10 Most Volatile Stocks")
            st.plotly_chart(fig)


#Cumulative Return Over Time

elif menu == "Cumulative Return":
    st.header("📈 Top 5 Cumulative Return")
    agree = st.checkbox("Show The Cumulative Return Of Each Stock From The Beginning Of The Year To The End.")
    if agree:
        st.success("Great!")

        if st.button('Click Results',key='filter_button_3'):
            
            st.balloons()

            df3 = fetch_data("SELECT * FROM cumulative_returns")
            df3.sort_values("Yearly_Return",ascending=False,inplace=True)
            st.dataframe(df3)
            fig = px.bar(df3, x='Ticker', y='Yearly_Return', color='Ticker',title='Cumulative Returns Over Time')
            st.plotly_chart(fig)


#Sector-wise Performance

elif menu == "Sector-wise Performance":

    st.header("🏢 Sector-Wise Performance")

    agree = st.checkbox("Provide a Breakdown of Stock Performance By Sector.")
    if agree:
        st.success("Great!")

        if st.button('Click Results',key='filter_button_4'):
            
            st.balloons()
    
            df4 = fetch_data("SELECT * FROM sector_wise_performance")
            df4.sort_values("Yearly_Return",ascending=False,inplace=True)
            st.dataframe(df4)
            fig = px.bar(df4, x='sector', y='Yearly_Return', title='Average Yearly Return by Sector')
            st.plotly_chart(fig)


# Stock Price Correlation

elif menu == "Stock Price Correlation":
    
    st.header("📊 Stock Price Correlation")


    agree = st.checkbox("Visualize the Correlation Between the StockPprices of Different Companies.")
    if agree:
        st.success("Great!")

        if st.button('Click Results',key='filter_button_3'):
            
            st.balloons()
            df = fetch_data("SELECT * FROM sector_wise_performance") 
            df.set_index(df.columns[0], inplace=True)
            fig, ax = plt.subplots(figsize=(14, 10))
            sns.heatmap(df.astype(float), cmap='RdBu_r', annot=False , center=0, ax=ax)
            st.pyplot(fig)