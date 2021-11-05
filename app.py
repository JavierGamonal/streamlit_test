import streamlit as st
import pandas as pd
import altair as altair


st.title('DataFrame Demo')
st.sidebar.selectbox('Choose a demo', ['DataFrame Demo','Other'])
check=st.sidebar.checkbox('Show code')
file_name = "https://raw.githubusercontent.com/napoles-uach/Pycon_cl_taller/main/appDemo/UNdata_Export_20211101_202548548.csv"
df = pd.read_csv(file_name)

#st.write(df)

country_select= st.multiselect('Choose Countries', df , default=['Chile','Mexico'])
df2=df[df['Country or Area'].isin(country_select)] 
st.subheader('Gross Production Index Number')
st.write(df2.head())

df_plot=df2[['Year','Value','Country or Area']]

c = alt.Chart(df_plot).mark_area(opacity=0.3).encode(
    x='Year',
    y='Value',
    color='Country or Area'
)

st.altair_chart(c,use_container_width=True)

if check:
    text=open('app.py').read()
    st.code(text,language='python')