import altair as alt
import pandas as pd
import sqlite3
import streamlit as st


# Configuración de la página para modo ancho
st.set_page_config(layout="wide")

funcionarios = {
    "Juan Pérez": "Contabilidad",
    "María López": "Recursos Humanos",
    "Pedro García": "Ventas"
}
lista_funcionarios = list(funcionarios.keys())

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

def crear_tabla_novedades():
    conn = sqlite3.connect('novedade.db')
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
    conn = sqlite3.connect('novedade.db')
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
    with st.expander("Registro de Novedades 📂"):
        with st.form("my_form"):
            fecha = st.date_input("Fecha")
            nombre = st.selectbox("Selecciona un funcionario", lista_funcionarios)
            if nombre:
                st.write(f"Información de {nombre}:")
                st.write(f"Departamento: {funcionarios[nombre]}")
            novedad = st.selectbox("Novedad", ["Ausencia", "Permiso", "Llegada Tarde", "Licencia Luto", "Licencia Maternidad", "Otro"])
            observacion = st.text_area("Observación")
            submitted = st.form_submit_button("Guardar")
            if submitted:
                db.guardar_novedad(fecha, nombre, novedad, observacion)
                st.success("Novedad guardada correctamente")

    with st.expander("Funcionarios 👨🏽‍🦳"):
        df = db.obtener_novedades()

        # Selector de funcionarios (todos o uno en específico)
        funcionarios = df["nombre_funcionario"].unique()
        funcionario_seleccionado = st.selectbox("Seleccionar funcionario", [None] + list(funcionarios), index=0)

        # Selectores de fecha
        fecha_inicio = st.date_input("Fecha de inicio")
        fecha_fin = st.date_input("Fecha de fin")

        # Filtrar los datos
        if funcionario_seleccionado:
            df_filtrado = df[df['nombre_funcionario'] == funcionario_seleccionado]
        else:
            df_filtrado = df
        
        if fecha_inicio and fecha_fin:
            df_filtrado = df_filtrado[(df_filtrado['fecha'] >= str(fecha_inicio)) & (df_filtrado['fecha'] <= str(fecha_fin))]

        # Mostrar el DataFrame filtrado
        st.dataframe(df_filtrado)

        # Generar el gráfico
        st.altair_chart(generar_grafico(df_filtrado, f"Novedades de {funcionario_seleccionado or 'Todos los funcionarios'}"), use_container_width=True)
        

if __name__ == "__main__":
    main()
