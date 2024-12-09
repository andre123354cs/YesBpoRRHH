import streamlit as st
import pandas as pd
import requests

df = pd.read_csv("andre123354cs/YesBpoRRHH/rrhh - Hoja 1.csv")
st.dataframe(df)
