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

import streamlit as st

def guardar_novedad(fecha, nombre, novedad, observacion):
    # Aquí implementarías la lógica para guardar los datos
    # ... (validar datos, conectar a la base de datos, etc.)
    st.success("Novedad guardada correctamente")

with st.form("my_form"):
    st.write("Registrar Novedad")

    fecha = st.date_input("Fecha", min_value=st.date.today())  # Limitar a fechas a partir de hoy
    nombre = st.text_input("Nombre del funcionario")
    novedad = st.selectbox("Novedad", ["Ausencia", "Permiso", "Llegada Tarde", "Licencia Luto", "Licencia Maternidad", "Otro"])
    if novedad == "Otro":
        otro_novedad = st.text_input("Especificar otra novedad")

    observacion = st.text_area("Observación", max_chars=255)  # Limitar la longitud

    submitted = st.form_submit_button("Guardar")
    if submitted:
        if nombre == "":
            st.error("Por favor, ingrese el nombre del funcionario.")
        else:
            # Validar otros campos
            guardar_novedad(fecha, nombre, novedad, observacion)
