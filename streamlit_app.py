import altair as alt
import pandas as pd
import sqlite3
import streamlit as st
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBUxKlDXnPSeNLKYXzsp3pUxJ8giAwSkMQ",
    "authDomain": "metadata-c090e.firebaseapp.com",
    "databaseURL": "https://metadata-c090e-default-rtdb.firebaseio.com",
    "projectId": "metadata-c090e",
    "storageBucket": "metadata-c090e.appspot.com",
    "messagingSenderId": "954810311523",
    "appId": "1:954810311523:web:a6b0681e4f164b60cba956"
}

firebase = pyrebase.initialize_app(firebaseConfig)
pb_auth = firebase.auth()
db = firebase.database()  # Referencia a la base de datos


# Configuración de la página para modo ancho
st.set_page_config(layout="wide")
def interfaz():
    funcionarios = {
        "Mayra Alejandra Baron":"Sistemas",
        "Ashly Nicole Marin": "Sistemas",
        "Yuri Stefania Barahona Larios": "Marketing",
        "Valentina Velez Bedoya": "Sistemas",
        "Luisa Fernanda Duarte": "Contabilidad",
        "Andrea Florez Rodriguez": "Recursos Humanos",
        "Maria Camila Rodriguez Cadavid": "Ventas",
        "Maria Angelica Narvaez Martinez": "Marketing",
        "David Felipe Velandia": "Sistemas",
        "Leidy Johana Calle Muñoz": "Contabilidad",
        "Alejandro Collazos": "Recursos Humanos",
        "Hector Esteban Moreno Triana": "Ventas",
        "Luisa Fernanda Pita Alvarado": "Marketing",
        "Sharith Michele Sandoval Betancourt": "Sistemas",
        "Valentina Chaguala Sanchez": "Contabilidad",
        "Luisa Fernanda Sanchez Moreno": "Recursos Humanos",
        "Martha Isabel Albarracin Sierra": "Ventas",
        "Lizeth Viviana Suarez Espitia": "Marketing",
        "Juan Esteban Ariza Peña": "Sistemas",
        "Jhon Alberto Castillo Mayorga": "Contabilidad",
        "Skarleth Julio Guerrero": "Recursos Humanos",
        "Jonathan Steven Salomon Rodriguez": "Ventas",
        "Laura Geraldine Castro Hernandez": "Marketing",
        "Sergio Velez Bedoya": "Sistemas",
        "Dannia Alejandra Romero Lemus": "Marketing",
        "Braiam Alexander Narvaez Gallo": "Ventas",
        "Angie Katerin Aya Garcia": "Recursos Humanos",
        "Angie Carolina Rincon Lopez": "Contabilidad",
        "Yiseinis Alvarez Serrano": "Marketing",
        "Kiara Maria Rodriguez Garcia": "Sistemas",
        "Cristian Camilo Rojas Riaño": "Ventas",
        "Juanita Valentina Bautista Mendieta": "Recursos Humanos",
        "Jhonny Arley Cruz Triana": "Contabilidad",
        "Heidy Yulieth Mora Leon": "Marketing",
        "Andres Felipe Diaz Bolaños": "Sistemas",
        "Miguel Angel Reinstag Gutierrez": "Ventas",
        "Maycol Estiven Yepes Zambrano": "Recursos Humanos",
        "Felipe Rodriguez Sarmiento": "Contabilidad",
        "Allison Daniela Garcia Osorio": "Marketing",
        "Edwar Andres Vanegas Cortes": "Sistemas",
        "Felix Santafé": "Ventas",
        "Cristian Matías": "Recursos Humanos",
        "Francy Yulieth Guapacha Lotero": "Contabilidad",
        "Ana Miryam Gonzalez": "Marketing",
        "Luisa Fernanda Chavez": "Marketing"
    }
    lista_funcionarios = sorted(funcionarios.keys())
    
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <img src="https://cdn-icons-png.flaticon.com/128/6429/6429114.png" alt="RRHH YesBpo Logo" width="100" height="100">
      <h1 style='color: #0f0a68; font-size: 20px;'> RRHH YesBpo</h1>
      <img src="https://tse3.mm.bing.net/th?id=OIP.mgZxMZpR_P9RB4qAfF1FXQHaGg&pid=Api&P=0&h=180" alt="Otro logo" width="100" height="100">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
        """, unsafe_allow_html=True)
    df = pd.read_csv("Hoja 1.csv")
    st.dataframe(df)
    
