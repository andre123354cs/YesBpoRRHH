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



    # Crear el formulario
    with st.form("my_form"):
        fecha = st.date_input("Fecha")
        nombre = st.text_input("Nombre del funcionario")
        novedad = st.selectbox("Novedad", ["Ausencia", "Permiso", "Llegada Tarde","Licencia Luto","Licencia Maternidad","Otro"])
        observacion = st.text_area("Observación")

        # Botón para enviar el formulario
        submitted = st.form_submit_button("Guardar")
        if submitted:
            guardar_novedad(fecha, nombre, novedad, observacion)
            st.success("Novedad guardada correctamente")
