"""
# My first app

"""
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# opens and stores a csv file as a dataframe using pandas
df = pd.read_csv('price_history.csv')
df['Date'] = pd.to_datetime(df['Date'])
names = ["ETH-BTC", "LTC-BTC", "XRP-BTC", "DOGE-BTC", "MATIC-BTC",
         "LINK-BTC", "ADA-BTC", "BNB-BTC", "TRX-BTC", "DOT-BTC", "SOL-BTC"]

# opens and/or stores a txt file
#intro = open('article.txt','r').read()
st.write(open('article.txt', 'r').read())

charts = []
for i in range(0,len(names)):
    charts.append(alt.Chart(df).mark_line().encode(x='Date', y=f'{names[i]}').properties(title=f'{names[i]}'))
#for i in range(0,len(names)):
    st.altair_chart(charts[i], use_container_width=True)

st.line_chart(df, x='Date', y='LTC-BTC')
st.line_chart(df, x='Date', y='ETH-BTC')
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('Cryptocurrencies in BTC over time')
# ax1.plot(df['Date'], df['LTC-BTC'])
# ax2.plot(df['Date'], df['XRP-BTC'])
# ax3.plot(df['Date'], df['ETH-BTC'])
# ax4.plot(df['Date'], df['DOGE-BTC'])
# st.pyplot(fig=fig)
st.dataframe(df)