import streamlit as st
import pandas as pd
import requests

df = pd.read_csv('https://ram.githubusercontent.com/andre123354cs/YesBpoRRHH/blame/81a717662392571d3f3707d5f0651e4f9b8913e0/rrhh%20-%20Hoja%201.csv')
st.dataframe(df)
