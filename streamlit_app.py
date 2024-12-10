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
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <img src="https://cdn-icons-png.flaticon.com/128/6429/6429114.png" alt="RRHH YesBpo Logo" width="100" height="100">
      <h1 style='color: #0f0a68; font-size: 29px;'> RRHH YesBpo</h1>
      <img src="https://tse3.mm.bing.net/th?id=OIP.mgZxMZpR_P9RB4qAfF1FXQHaGg&pid=Api&P=0&h=180" alt="Otro logo" width="100" height="100">
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)


gsheetid='14NM6hoF3dg-Veq7w1OBZEwH0B1w9kq8mxt07-apSBIc'
sheetod='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos= pd.read_csv(url)

tab1, tab2 = st.tabs(["Historia", "Funcionarios"])

with tab1:
    st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 25px;'>Aqui podemos ver la historia segun filtro</h1>
    """, unsafe_allow_html=True)
    
    dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'])  # Ensure 'Fecha' is datetime
    
    # Convert date_input results to datetime format for comparison
    fecha_inicio = pd.to_datetime(st.date_input("Fecha de inicio"))
    fecha_fin = pd.to_datetime(st.date_input("Fecha de fin"))
    
    # Filtrar el DataFrame basado en el rango seleccionado
    if fecha_inicio and fecha_fin:
      df_filtrado = dfDatos[(dfDatos['Fecha'] >= fecha_inicio) & (dfDatos['Fecha'] <= fecha_fin)]
    else:
      df_filtrado = dfDatos.copy()
    
    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado, use_container_width=True)

    df_agrupado = df_filtrado.groupby('Novedad').size().reset_index(name='Conteo')

    # Crear la figura con Plotly Express (Gráfica de Barras)
    fig = px.bar(df_agrupado, x='Novedad', y='Conteo', color='Novedad',
                color_discrete_sequence=px.colors.qualitative.Pastel)
    
    # Personalizar la gráfica
    fig.update_layout(
        title_text='Conteo de Novedades',
        xaxis_title='Novedad',
        yaxis_title='Cantidad'
    )
    
    # Mostrar la gráfica en Streamlit
    st.plotly_chart(fig)

with tab2:
    st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 25px;'>Aqui podemos ver la historia segun filtro</h1>
    """, unsafe_allow_html=True)
    funcionarios_unicos = dfDatos['Funcionario'].unique()
    
    # Crear un elemento de selección múltiple para elegir funcionarios
    funcionario_seleccionado = st.multiselect('Selecciona funcionarios', funcionarios_unicos)

    dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'])  # Ensure 'Fecha' is datetime
    
    # Convert date_input results to datetime format for comparison
    fecha_inicio = pd.to_datetime(st.date_input("Fecha de inicio "))
    fecha_fin = pd.to_datetime(st.date_input("Fecha de fin "))
    
    # Filtrar el DataFrame basado en el rango de fechas y funcionarios seleccionados
    if fecha_inicio and fecha_fin and funcionario_seleccionado:
        df_filtrado = dfDatos[(dfDatos['Fecha'] >= fecha_inicio) &
                             (dfDatos['Fecha'] <= fecha_fin) &
                             (dfDatos['Funcionario'].isin(funcionario_seleccionado))]
    else:
        df_filtrado = dfDatos.copy()
    
    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado, use_container_width=True)
