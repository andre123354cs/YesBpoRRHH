import streamlit as st
import pandas as pd
import requests

df = df.to_csv("rrhh - Hoja 1.csv")

# Crea un formulario para ingresar nuevos datos
with st.form("my_form"):
    fecha = st.date_input("Fecha")
    novedad = st.text_input("Novedad")
    funcionario = st.text_input("Funcionario")
    area = st.text_input("Área")
    submitted = st.form_submit_button("Agregar")

# Si se presiona el botón "Agregar", agrega los nuevos datos al DataFrame
if submitted:
    new_data = {'Fecha': [fecha], 'Novedad': [novedad], 'Funcionario': [funcionario], 'Área': [area]}
    df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

    # Guarda los cambios en el archivo CSV
    df.to_csv("rrhh - Hoja 1.csv", index=False)

    # Muestra el DataFrame actualizado
    st.dataframe(df)

    
