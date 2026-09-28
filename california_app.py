import numpy as np
import streamlit as st
import joblib

obj = joblib.load('california.joblib')

model = obj['model']
cols = obj['columns']

st.title("california app⚡")
In = []
for i in cols:
    v = st.number_input(f'Enter {i} value:')
    In.append(v)

if st.button('click'):
    out = model.predict([In])
    st.success(f"The Median House value is : {out}")
