import streamlit as st
import pandas as pd
import altair as altair


st.title('DataFrame Demo')
st.sidebar.selectbox('Choose a demo', ['DataFrame Demo','Other'])
check=st.sidebar.checkbox('Show code')
file_name = "https://raw.githubusercontent.com/napoles-uach/Pycon_cl_taller/main/appDemo/UNdata_Export_20211101_202548548.csv"
df = pd.read_csv(file_name)

st.write(df)

country_select= st.multiselect('Choose Countries',countries , default=['Chile','Mexico'])

