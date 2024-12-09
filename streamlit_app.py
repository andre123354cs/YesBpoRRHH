import streamlit as st
import pandas as pd
import requests

df = pd.read_csv("rrhh - Hoja 1.csv")
st.dataframe(df)
