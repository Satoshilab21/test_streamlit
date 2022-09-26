"""
# My first app

"""
import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt

# opens and stores a csv file as a dataframe using pandas
df = pd.read_csv('price_history.csv')
df['Date'] = pd.to_datetime(df['Date'])
names = ["ETH-BTC", "LTC-BTC", "XRP-BTC", "DOGE-BTC", "MATIC-BTC",
         "LINK-BTC", "ADA-BTC", "BNB-BTC", "TRX-BTC", "DOT-BTC", "SOL-BTC"]

# Article Title
st.header("Chase the Dragon or Hodl the Bag")

# Disclaimer
st.write("_**DISCLAIMER**: The following information is not not financial advice. This article is entirely educational in nature and should not not be taken as financial advice_")

# NOTE:
st.write("**NOTE**: This article was initially written on 9/26/2022. However, I have designed the charts in it to update over time. This will help show whether or not the initial thesis holds up over the coming years.")

# Introduction
st.write(open(f'\text\Intro.txt', 'r').read())


# SECTION 1
# sub-header for section
st.subheader("Group 1: Friends 4ever")

# Group 1 Charts
# Litecoin LTC, Namecoin NMC, Peercoin PPC, Dogecoin DOGE, Ripple XRP, Monero XMR, Ethereum ETH
names1 = ["LTC-BTC", "DOGE-BTC", "XRP-BTC", "ETH-BTC"]
charts = []

# The section below writes using the MAGIC command.
'''
The first group of cryptocurrencies to examine are: Litecoin (LTC), Dogecoin (DOGE), Ripple (XRP), Ethereum (ETH). This group contains some of the OG's in the crypto space which have been in the market with BTC over the longest period of time.
'''

# Creates Charts
for i in range(0, len(names1)):
    charts.append(alt.Chart(df).mark_line().encode(x='Date', y=f'{names1[i]}').properties(title=f'{names1[i]}'))
    st.altair_chart(charts[i], use_container_width=True)
# TO-DO: Adjust the X-axis to make sure it only shows years.
# TO-DO: Make 1 box where you look at the charts 1 by 1. Click Next to scroll through the charts.
st.write("Looking at graphs for LTC, XRP, and ETH, it is clear that after their initial hype cycle, the assets struggled to make new all time highs during the 2021 bull market. Notably, ETH did have a strong upwards movement during the bull market and gained considerably on BTC. Additionally, the gain coincides with clear project improvemets (I.E increased security with lower issuance payments). The ETH-BTC chart should be watched closely moving forward. Click the link for more on The Merge (INCLUDE ETH MERGE LINK). Unlike ETH, DOGE's dramatic upwards move was clearly **NOT** due to any project breakthroughs or merit. The rise in DOGE price can be attributed to rise in meme-stock culture alongside marketing from popular cultural figures such as Elon Musk.  \n ")
st.write(
 "TAKE AWAYS:  \n"
 "- For the average Joe, it has better to Hodl a bag of BTC rather than the the bag (hold BTC)  \n"
 "- It is possible for older coins to see dramatic price rises due to shifts in overall culture  \n")


# SECTION 2
# sub-header for section
st.subheader("Group 2: ICO Mania")

# The section below writes using the MAGIC command.
'''
The second group of cryptocurrencies to examine are: Tron (TRX), Chainlink (LINK), Cardano (ADA), Binance (BNB), Polkadot (DOT), Polygon (MATIC), and Solana (SOL). This group was primarily created during the 2017 ICO mania and throughout the following bear market.
'''

# Group 2 Charts
# Zcash ZEC, Binance BNB, Cardano ADA, TRON TRX, Algorand ALGO, Avalanche AVAX, Polkadot DOT, Solana SOL
names2 = ["TRX-BTC", "LINK-BTC", "ADA-BTC", "BNB-BTC", "DOT-BTC", "MATIC-BTC", "SOL-BTC"]
charts = []
for i in range(0, len(names2)):
    charts.append(alt.Chart(df).mark_line().encode(x='Date', y=f'{names2[i]}').properties(title=f'{names2[i]}'))
    st.altair_chart(charts[i], use_container_width=True)
st.write("Many of the charts relate closely to those shown in group 1. They start with an initial hype cycle, then struggle to recover to make new all time highs. A subtle observation here is that LINK slowly and steadily increased until it exploded upwards around August 2020. The most obvious chart here is BNB with the price exploded upwards in late 2021 and continues to hold strong.")
st.write(
 "TAKE AWAYS:  \n"
 "- Chainlink shows that cryptocurrencies created during a bear market can still have a volatile price rise to new all time highs much later  \n"
 "- BNB stands out as one of the very few cryptocurrencies to break out to new all time highs and remain there for an extended period of time  \n")

# CONCLUSION
# sub-header for section
st.subheader("Conclusion")
st.write(f'Of the {len(names)} cryptocurrencies examined, {len(names)-2} have shown that it is better to hold BTC into the next bull market instead of hoping for any specific cryptocurrency to make new all time highs. Only DOGE and BNB were able to make new all time highs and only BNB has been able to sustain the new all time high level. In short, the majority of cryptocurrency participates are better off selling off their altcoin holdings and hodling the bag (of BTC) rather than continuing to chase the dragon.')
st.write("Notable Assumptions: ")

# Link to download dataset
st.dataframe(df)