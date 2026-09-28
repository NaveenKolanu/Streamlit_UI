import streamlit as st

st.title("Streamlit Local Setup ⚡")
st.write("Running smoothly inside VS Code!")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome, {name}!")
