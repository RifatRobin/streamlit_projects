import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("Fuck OFF Bitch")

st.write("Let's *Fuck The World* :sunglasses:")

name=['Niaj','Rifat','johny','Mahi','Suja']
age=['30','26','23','22','21']
gender=['Male','Male','Male','Female','Male']

df=pd.DataFrame({
    'Name':np.sort(name),
    'Gender':np.sort(gender),
    'Age':np.sort(age),
},hide_index=True)

st.write("Main Dataframe: \n",df)

hide_df=df.drop('Gender',axis=1,hide_index=True)
st.write("Without Gender Column Dataframe: \n",hide_df)

# dplot=alt.Chart(df.drop(gender))