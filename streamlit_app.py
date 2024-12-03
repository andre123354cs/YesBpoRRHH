import altair as alt
import pandas as pd
import sqlite3
import streamlit as st
import sqlite3
import altair as alt

# Show the page title and description.
st.set_page_config(page_title="RRHH YesBpo", page_icon="🌍")
st.markdown("""
    <h1 style='text-align: left; color: #008f4c; font-size: 50px;'>🌍 RRHH YesBpo</h1>
    """, unsafe_allow_html=True)
st.markdown("""
    <h1 style='text-align: left; color: #008f4c; font-size: 20px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.title("Visualizador de archivos CSV")

# Cargar el archivo
uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo en un DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el DataFrame en una tabla
    st.dataframe(df)
