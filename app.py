import streamlit as st
st.title('Mi primer ejemplo :rocket:')
x=st.slider('select a value')
st.write(x, 'squared is', x*x)
st.sidebar.checkbox('Click me')

st.button('Click')
       
st.markdown(':+1:')
