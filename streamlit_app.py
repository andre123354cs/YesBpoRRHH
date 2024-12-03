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

import git
import pandas as pd

# Clonar el repositorio
repo = git.Repo.clone_from('https://github.com/tu_usuario/tu_repositorio.git', 'tu_carpeta_local')

# Obtener el archivo
file_path = 'tu_carpeta_local/rrhh - Hoja 1.csv'

# Leer el archivo con pandas
df = pd.read_csv(file_path)
print(df)
