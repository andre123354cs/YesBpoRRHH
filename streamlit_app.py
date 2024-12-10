import streamlit as st
import pandas as pd
import plotly.express as px


st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Appsheet </h1>
    """, unsafe_allow_html=True)


gsheetid='14NM6hoF3dg-Veq7w1OBZEwH0B1w9kq8mxt07-apSBIc'
sheetod='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos= pd.read_csv(url)


dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'])  # Ensure 'Fecha' is datetime

# Convert date_input results to datetime format for comparison
fecha_inicio = pd.to_datetime(st.date_input("Fecha de inicio"))
fecha_fin = pd.to_datetime(st.date_input("Fecha de fin"))

# Filtrar el DataFrame basado en el rango seleccionado
if fecha_inicio and fecha_fin:
  df_filtrado = dfDatos[(dfDatos['Fecha'] >= fecha_inicio) & (dfDatos['Fecha'] <= fecha_fin)]
else:
  df_filtrado = dfDatos.copy()

# Mostrar el DataFrame filtrado
st.dataframe(df_filtrado, use_container_width=True)
