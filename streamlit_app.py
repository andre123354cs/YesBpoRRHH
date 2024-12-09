import streamlit as st
import pandas as pd
import requests

# Función para descargar el archivo CSV desde GitHub
def descargar_csv_desde_github(url):
    """Descarga un archivo CSV desde un repositorio de GitHub."""
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()  # Levanta una excepción si la descarga falla

    if response.headers.get('content-type') != 'text/csv':
        raise ValueError('El archivo no es un CSV válido.')

    return response.content

# Detalles del repositorio de GitHub
url_repositorio = "https://github.com/andre123354cs/YesBpoRRHH"
nombre_archivo = "rrhh - Hoja 1.csv"
url_archivo = f"{url_repositorio}/raw/main/{nombre_archivo}"  # Usar la rama 'main' o la rama deseada

# Intentar descargar el archivo y manejar posibles errores
try:
    contenido_csv = descargar_csv_desde_github(url_archivo)
    df = pd.read_csv(io.StringIO(contenido_csv))

    # Mostrar los primeros 5 registros del DataFrame
    st.write("Primeras 5 filas del archivo CSV:")
    st.dataframe(df.head())

except Exception as e:
    st.error(f"Error al cargar el archivo CSV: {e}")
    
