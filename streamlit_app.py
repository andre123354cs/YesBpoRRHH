import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MetaData",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
    )

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <img src="https://cdn-icons-png.flaticon.com/128/6429/6429114.png" alt="RRHH YesBpo Logo" width="100" height="100">
      <h1 style='color: #0f0a68; font-size: 29px;'> RRHH YesBpo</h1>
      <img src="https://tse3.mm.bing.net/th?id=OIP.mgZxMZpR_P9RB4qAfF1FXQHaGg&pid=Api&P=0&h=180" alt="Otro logo" width="100" height="100">
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)


gsheetid='14NM6hoF3dg-Veq7w1OBZEwH0B1w9kq8mxt07-apSBIc'
sheetod='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos= pd.read_csv(url)

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Contenido de la pestaña 1")

    
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


with tab2:
    st.write("Contenido de la pestaña 2")
