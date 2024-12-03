

import altair as alt
import pandas as pd
import sqlite3
import streamlit as st

st.markdown("""
    <h1 style='text-align: left; color: #008f4c; font-size: 50px;'>🌍 RRHH YesBpo</h1>
    """, unsafe_allow_html=True)
st.markdown("""
    <h1 style='text-align: left; color: #008f4c; font-size: 20px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)

def crear_tabla_novedades():
    conn = sqlite3.connect('novedades.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS novedades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            nombre_funcionario TEXT,
            novedad TEXT,
            observacion TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Llama a la función para crear la tabla antes de intentar seleccionar datos
crear_tabla_novedades()

# Función para establecer conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('novedades.db')
    return conn

# Clase para gestionar las operaciones de la base de datos
class NovedadesDB:
    def __init__(self):
        self.conn = get_db_connection()

    def guardar_novedad(self, fecha, nombre, novedad, observacion):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO novedades (fecha, nombre_funcionario, novedad, observacion)
            VALUES (?, ?, ?, ?)
        ''', (fecha, nombre, novedad, observacion))
        self.conn.commit()

    def obtener_novedades(self, filtro=None):
        cursor = self.conn.cursor()
        query = "SELECT * FROM novedades"
        if filtro:
            query += f" WHERE {filtro}"
        df = pd.read_sql_query(query, self.conn)
        return df

    def cerrar_conexion(self):
        self.conn.close()

# Crear una instancia de la clase NovedadesDB
db = NovedadesDB()

# Función para generar el gráfico de barras
def generar_grafico(df, titulo):
    chart = alt.Chart(df).mark_bar().encode(
        x='novedad',
        y='count()'
    ).properties(
        title=titulo
    )
    return chart

# Interfaz de usuario de Streamlit
def main():

    # Pestaña para registrar novedades
    with st.expander("Registro de Novedades "):
        with st.form("my_form"):
            fecha = st.date_input("Fecha")
            nombre = st.text_input("Nombre del funcionario")
            novedad = st.selectbox("Novedad", ["Ausencia", "Permiso", "Llegada Tarde", "Licencia Luto", "Licencia Maternidad", "Otro"])
            observacion = st.text_area("Observación")
            submitted = st.form_submit_button("Guardar")
            if submitted:
                db.guardar_novedad(fecha, nombre, novedad, observacion)
                st.success("Novedad guardada correctamente")

    # Pestaña para ver datos por funcionario
    with st.expander("Funcionarios "):
        funcionarios = db.obtener_novedades()["nombre_funcionario"].unique()
        funcionario_seleccionado = st.selectbox("Seleccionar funcionario", funcionarios)
        df_filtrado = db.obtener_novedades(f"nombre_funcionario = '{funcionario_seleccionado}'")
        st.dataframe(df_filtrado)
        st.altair_chart(generar_grafico(df_filtrado, f"Novedades de {funcionario_seleccionado}"), use_container_width=True)

    # Pestaña para ver datos consolidados
    with st.expander("Consolidado "):
        df = db.obtener_novedades()
        st.dataframe(df)
        st.altair_chart(generar_grafico(df, "Número de novedades por tipo"), use_container_width=True)

if __name__ == "__main__":
    main()
