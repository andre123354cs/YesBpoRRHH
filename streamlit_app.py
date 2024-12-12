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

tab1, tab2 = st.tabs(["Historia", "Funcionarios"])

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

    df_filtrado = dfDatos[(dfDatos['Fecha'] >= fecha_inicio) &
                              (dfDatos['Fecha'] <= fecha_fin) ]
    
    if novedad_seleccionada:
        df_filtrado = dfDatos[dfDatos['Novedad'].isin(novedad_seleccionada)]

    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado, use_container_width=True)

    suma_tiempo = df_filtrado['Tiempo'].sum()
    st.markdown(f"""
    <p style="font-size: 20px; color: blue;">
    La totalidad del tiempo en llegadas tarde es: <b>{suma_tiempo}</b> [Minutos]
    </p>
    """, unsafe_allow_html=True)

    df_agrupado = df_filtrado.groupby(['Funcionario', 'Fecha']).size().reset_index(name='Conteo')

    # Crear la figura con Plotly Express (Gráfica de Barras)
    fig = px.bar(df_agrupado, x='Fecha', y='Conteo', color='Funcionario', text_auto=True,
                 color_discrete_sequence=px.colors.qualitative.Pastel)

    # Personalizar la gráfica
    fig.update_layout(
        title_text='Conteo de Novedades',
        xaxis_title='Fecha',
        yaxis_title='Cantidad'
    )

    # Mostrar la gráfica en Streamlit
    st.plotly_chart(fig)

with tab2:
    st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 25px;'>Aqui podemos ver la historia por persona</h1>
    """, unsafe_allow_html=True)

    funcionarios_unicos = dfDatos['Funcionario'].unique()
    
    # Crear un elemento de selección múltiple para elegir funcionarios
    funcionario_seleccionado = st.multiselect('Selecciona funcionarios', funcionarios_unicos)

    # Convertir date_input results a formato datetime para comparación
    fecha_inicio_func = pd.to_datetime(st.date_input("Fecha de inicio", value=fecha_min, key='fecha_inicio_func', min_value=fecha_min, max_value=fecha_max))
    fecha_fin_func = pd.to_datetime(st.date_input("Fecha de fin", value=fecha_max, key='fecha_fin_func', min_value=fecha_min, max_value=fecha_max))

    # Filtrar el DataFrame basado en el rango de fechas y funcionarios seleccionados
    if fecha_inicio_func and fecha_fin_func and funcionario_seleccionado:
        df_filtrado = dfDatos[(dfDatos['Fecha'] >= fecha_inicio_func) &
                              (dfDatos['Fecha'] <= fecha_fin_func) &
                              (dfDatos['Funcionario'].isin(funcionario_seleccionado))]
    else:
        df_filtrado = dfDatos.copy()

    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado, use_container_width=True)


