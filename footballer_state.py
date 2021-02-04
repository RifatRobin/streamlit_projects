import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np
import base64

st.title("Footballer States")


st.sidebar.header("Input Section")  # for side bar title
selected_year = st.sidebar.selectbox("Year", list(
    reversed(range(1920, 2021))))  # input of year in sidebar

# web scrapping for the footballer state data


@st.cache
def load_data(year):
    url = 'https://www.pro-football-reference.com/years/' + \
        str(year) + "/rushing.htm"
    read_data = pd.read_html(url, header=1)
    df = read_data[0]
    # Deletes repeating headers in content
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats


playerstats = load_data(selected_year)
