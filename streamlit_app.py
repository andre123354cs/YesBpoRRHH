import streamlit as st
import pandas as pd
import requests

df = pd.read_csv("https://github.com/andre123354cs/YesBpoRRHH/blob/08957ddc8b75388d115858e13a6bdb70aa109e55/rrhh%20-%20Hoja%201.csv
")
st.dataframe(df)
columnas = df.columns

# Crea un formulario dinámico
with st.form("my_form"):
    datos = {}
    for columna in columnas:
        if columna == "Fecha":
            datos[columna] = st.date_input(columna)
        else:
            datos[columna] = st.text_input(columna)

    submitted = st.form_submit_button("Agregar")

# Si se presiona el botón "Agregar", agrega los nuevos datos al DataFrame
if submitted:
    new_data = pd.DataFrame(datos, index=[0])
    df = pd.concat([df, new_data], ignore_index=True)

    # Guarda los cambios en el archivo CSV
    df.to_csv("https://github.com/andre123354cs/YesBpoRRHH/blob/08957ddc8b75388d115858e13a6bdb70aa109e55/rrhh%20-%20Hoja%201.csv
", index=False)

    # Muestra el DataFrame actualizado
    st.dataframe(df)


    
