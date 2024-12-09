import altair as alt
import pandas as pd
import sqlite3
import streamlit as st
import pyrebase


    
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
    
