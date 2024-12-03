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
import pandas as pd

def guardar_novedad(fecha, nombre, novedad, observacion, archivo=None):
    """
    Guarda la novedad en un archivo CSV.
    Puedes personalizar esta función para guardar los datos en una base de datos o realizar otras acciones.
    """

    # Crear un diccionario con los datos de la novedad
    data = {'Fecha': fecha, 'Nombre': nombre, 'Novedad': novedad, 'Observación': observacion}
    if archivo:
        data['Archivo'] = archivo

    # Crear un DataFrame de pandas
    df = pd.DataFrame([data])

    # Append to an existing CSV file, or create a new one
    try:
        df.to_csv('novedades.csv', mode='a', header=False, index=False)
    except FileNotFoundError:
        df.to_csv('novedades.csv', index=False)

    st.success("Novedad guardada correctamente")

with st.form("my_form"):
    st.title("Registrar Novedad")

    fecha = st.date_input("Fecha", min_value=st.date.today())
    nombre = st.text_input("Nombre del funcionario")
    novedad = st.selectbox("Novedad", ["Ausencia", "Permiso", "Llegada Tarde", "Licencia Luto", "Licencia Maternidad", "Otro"])
    if novedad == "Otro":
        otro_novedad = st.text_input("Especificar otra novedad")

    observacion = st.text_area("Observación", max_chars=255)

    # Agregar un campo para subir archivos
    archivo = st.file_uploader("Subir archivo (opcional)")

    submitted = st.form_submit_button("Guardar")
    if submitted:
        if nombre == "":
            st.error("Por favor, ingrese el nombre del funcionario.")
        else:
            guardar_novedad(fecha, nombre, novedad, observacion, archivo)

# Mostrar un DataFrame con las novedades (opcional)
if st.checkbox("Ver novedades"):
    try:
        df = pd.read_csv('novedades.csv')
        st.dataframe(df)
    except FileNotFoundError:
        st.info("Aún no hay novedades registradas.")
