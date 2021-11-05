import streamlit as st 
import pandas as pd 
st.title('AppMap')
st.markdown('Esta es una aplicación simple para ayudarte a visualizar mapas')
st.markdown('**Nota:** Esta aplicación sigue en desarrollo, cualquier bug reportarlo a [@napoles3D](https://twitter.com/napoles3D)')

filepath = 'https://raw.githubusercontent.com/napoles-uach/Pycon_cl_taller/main/meteorite-landings.csv'

#st.cache
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

df = read_csv(filepath)
st.button('click')