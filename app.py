import streamlit as st
import pandas as pd
import altair as altair


st.title('DataFrame Demo')
st.sidebar.selectbox('Choose a demo', ['DataFrame Demo','Other'])
check=st.sidebar.checkbox('Show code')
df = pd.read_csv('https://github.com/napoles-uach/Pycon_cl_taller/blob/main/meteorite-landings.csv')

st.write(df)

