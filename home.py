import streamlit as st
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go
import datetime
from PIL import Image
import time
import os.path
import pickle as pkle
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HOME",
    page_icon="	🏠",
    layout="wide",
)

sidebar = st.container()
head = st.container()
dataset = st.container()

with dataset:#calling my data
    games = pd.read_csv('data\popular_games.csv')
    streamers = pd.read_csv('data\popular_streamers.csv')
    day_cycle = pd.read_csv('data\Most popular games 7 day cycle - Sheet1.csv')

with sidebar:
    st.sidebar.title("options")
    option = st.sidebar.selectbox("Which dataset",("Home","Most popular games","Most popular streamers",))


if option =="Most popular games":
   components.html("""<h1 style="text-align: center; color:#941cc7; font-size:50px; font:"Times New Roman"; ">Most popular games on Twitch</h1>"""
)
   fig3 = fig = px.pie(games, values='Peak viewers', names='Game', color='Game', title='Most popular games of all time')
   st.plotly_chart(fig3)

   fig4 = px.line(day_cycle, x='date', y='views', color='Games', title='Most popular games over the last 7 days')
   st.plotly_chart(fig4)




if option =="Most popular streamers":
    components.html(
        """<h1 style="text-align: center; color:#941cc7; font-size:50px; font:"Times New Roman"; ">Most popular streamers on Twitch</h1>"""
        )

    fig = px.bar(streamers.head(10), x='Channel', y='Peak viewers')
    st.plotly_chart(fig)
    st.markdown('''
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">The bar chart above shows the most popular streamers by peak viewers</p>
''', unsafe_allow_html=True)
    fig1 = px.bar(streamers.head(10), x='Channel', y='Followers')
    st.plotly_chart(fig1)
    st.markdown('''
        <p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">The bar chart above shows the most popular streamers by total followers</p>
        ''', unsafe_allow_html=True)





if option =="Home":

    components.html("""<h2 style="text-align: center; color:#941cc7; font-size:50px; font:"Times New Roman"; ">Twitch data visualisation project by Eriz Yusuf</h2> """)
    components.html("""<p style="color:#941cc7; font-size:14px; font:"Times New Roman"; > This is my data visualisation project for the most popular games and streamers. This sites aim is to help users understand what the most popular games on twitch and find the most popular streamers. Some people use twitch as a guide to find games they want to take an interest in</p>""")

    st.markdown('''
<h1 style="font-family: Times, serif; color: #941cc7;">Disclaimer</h1>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- I DO NOT OWN THE DATA BEING USED</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- The information was gathered from the Twitch API and Sully Gnome</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- I do not affiliate with Twitch</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- I do not promote any of the games or streamers mentioned; it's just to show the popular games and streams</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- This website is for educational purposes only</p>
''', unsafe_allow_html=True)



    st.markdown('''
<h1 style="font-family: Times, serif; color: #941cc7;">FAQ</h1>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">What Channels have you collected data for?/p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- The top 100 streamers, and the top 100 games but it has been filtered down to easily undersand.</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- Is this data accurate?</p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- This data was collected recently however data on a popular platform changes very quickly as new trends rise </p>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">- This website is for educational purposes only</p>

<h1 style="font-family: Times, serif; color: #941cc7;">Contact information</h1>
<a href="https:/https://www.twitch.tv/sireriz" style="color: #941cc7;">Twitch</a>
<p style="font-family: Times, serif; font-size: 14px; font-style: normal; font-weight: normal; color: #941cc7;">Email feel free to ask me any questions or contact me at eriz.yusuf@outlook.com</p>

''', unsafe_allow_html=True)










