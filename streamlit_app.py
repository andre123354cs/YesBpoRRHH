import streamlit as st
import pandas as pd
import requests

df = pd.read_csv("rrhh - Hoja 1.csv")

# Crea un formulario para ingresar nuevos datos
with st.form("my_form"):
    Fecha = st.date_input("Fecha")
    Novedad = st.text_input("Novedad")
    Funcionario = st.text_input("Funcionario")
    Area = st.text_input("Área")
    submitted = st.form_submit_button("Agregar")

# Si se presiona el botón "Agregar", agrega los nuevos datos al DataFrame
if submitted:
    new_data = {'Fecha': [Fecha], 'Novedad': [Novedad], 'Funcionario': [Funcionario], 'Area': [Area]}
    df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

    # Restablecer índice s(por si acaso)
    df.reset_index(drop=True, inplace=True)

    # Guardar los cambios en el archivo CSV en modo 'a+'
    df.to_csv("rrhh - Hoja 1.csv", index=False, mode='a+', header=False)

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    
