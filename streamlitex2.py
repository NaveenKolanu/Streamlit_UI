import streamlit as st

a = st.number_input('Enter n1:')
b = st.number_input('Enter n2:')

st.button('click')
st.write(f'The addition of {a} and {b} is : {a+b}')