import streamlit as st
import pandas as pd
import requests

# Función para leer el CSV desde GitHub
def leer_csv_github(url, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta una excepción si el estado no es 200
        content = response.json()["content"]
        decoded_content = base64.b64decode(content)
        df = pd.read_csv(io.StringIO(decoded_content.decode('utf-8')))
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error al leer el archivo CSV: {e}")
        return None

# URL del archivo CSV (reemplaza con tu URL)
url = "https://raw.githubusercontent.com/andre123354cs/YesBpoRRHH/blob/08957ddc8b75388d115858e13a6bdb70aa109e55/rrhh%20-%20Hoja%
