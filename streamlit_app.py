import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MetaData",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
  <div style="display: flex; justify-content: Center; align-items: Center;">
    <img src="https://cdn-icons-png.flaticon.com/128/2118/2118460.png" alt="RRHH YesBpo Logo" width="100" height="100">
    <h1 style='color: #0f0a68; font-size: 29px;'> Proyecto Recursos Humanos</h1>
  </div>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)

gsheetid = '14NM6hoF3dg-Veq7w1OBZEwH0B1w9kq8mxt07-apSBIc'
sheetod = '0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos = pd.read_csv(url)

tab1, tab2 = st.tabs(["Historia", "-"])

# Convertir la columna 'Fecha' a datetime y formatearla a 'día/mes/año'
dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'], dayfirst=True)
dfDatos['Fecha'] = dfDatos['Fecha'].dt.strftime('%d/%m/%Y')
    
# Convertir la columna 'Fecha' de nuevo a datetime para el filtrado
dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'], format='%d/%m/%Y')

# Determinar el mínimo y máximo de fechas
fecha_min = dfDatos['Fecha'].min()
fecha_max = dfDatos['Fecha'].max()

with tab1:
    st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 25px;'>Aqui podemos ver la historia segun filtro</h1>
    """, unsafe_allow_html=True)
    
    # Convertir date_input results a formato datetime para comparación
    fecha_inicio = pd.to_datetime(st.date_input("Fecha de inicio", value=fecha_min, min_value=fecha_min, max_value=fecha_max), format='%d/%m/%Y')
    fecha_fin = pd.to_datetime(st.date_input("Fecha de fin", value=fecha_max, min_value=fecha_min, max_value=fecha_max), format='%d/%m/%Y')

    novedades_unicas = dfDatos['Novedad'].unique()

    # Crear un elemento de selección múltiple para elegir novedades
    novedad_seleccionada = st.multiselect('Selecciona novedades', novedades_unicas)

    df_filtrado = dfDatos
    
    if novedad_seleccionada:
        df_filtrado = df_filtrado[dfDatos['Novedad'].isin(novedad_seleccionada)]

    df_filtrado = df_filtrado[(dfDatos['Fecha'] >= fecha_inicio) & (dfDatos['Fecha'] <= fecha_fin)]
    
    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado, use_container_width=True)

    suma_tiempo = df_filtrado['Tiempo'].sum()
    st.markdown(f"""
    <p style="font-size: 20px; color: blue;">
    La totalidad del tiempo en llegadas tarde es: <b>{suma_tiempo}</b> [Minutos]
    </p>
    """, unsafe_allow_html=True)

    # Agrupar los datos por 'Funcionario' y 'Novedad'
    df_agrupado_funcionario = df_filtrado.groupby(['Funcionario', 'Novedad']).size().reset_index(name='Conteo')
    
    # Ordenar los datos por 'Funcionario' y 'Fecha'
    df_agrupado = df_filtrado.groupby(['Fecha', 'Funcionario']).size().reset_index(name='Conteo').sort_values(by='Fecha')

    df_agrupado['Fecha'] = df_agrupado['Fecha'].dt.strftime('%d/%m/%Y')

    # Crear la figura con Plotly Express (Gráfica de Barras) por Fecha
    fig_fecha = px.bar(df_agrupado, x='Fecha', y='Conteo', color='Funcionario', text_auto=True,
                       color_discrete_sequence=px.colors.qualitative.Pastel)

    # Personalizar la gráfica
    fig_fecha.update_layout(
        title_text='Conteo de Novedades por Fecha',
        xaxis_title='Fecha',
        yaxis_title='Cantidad'
    )

    # Mostrar la gráfica en Streamlit
    st.plotly_chart(fig_fecha)

    # Crear la figura con Plotly Express (Gráfica de Barras) por Funcionario
    fig_funcionario = px.bar(df_agrupado_funcionario, x='Funcionario', y='Conteo', color='Novedad', text_auto=True,
                             color_discrete_sequence=px.colors.qualitative.Pastel)

    # Personalizar la gráfica
    fig_funcionario.update_layout(
        title_text='Conteo de Novedades por Funcionario',
        xaxis_title='Funcionario',
        yaxis_title='Cantidad de Novedades'
    )

    # Mostrar la gráfica en Streamlit
    st.plotly_chart(fig_funcionario)

