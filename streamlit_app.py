import streamlit as st
import pandas as pd
import altair as alt
import requests  # For downloading the CSV from GitHub

# Streamlit app configuration (optional)
st.set_page_config(
    page_title="YesBpo RRHH - Transparencia y Claridad",
    page_icon=":chart_with_upwards_trend:",  # Example icon, adjust as needed
)

# Function to download the CSV securely from GitHub (avoiding raw URL)
def download_csv_from_github(url):
    """Downloads a CSV file from a GitHub repository URL."""
    response = requests.get(url, allow_redirects=True)  # Follow redirects
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    if response.headers.get("content-type") != "text/csv":
        raise ValueError("Expected a CSV file, but received a different content type.")

    return response.content

# GitHub repository details (replace with actual values)
github_repo_url = "https://github.com/andre123354cs/YesBpoRRHH"
csv_filename = "rrhh - Hoja 1.csv"
csv_url = f"{github_repo_url}/blob/c82891d903ce08a04340f84c6160e0f1eec8c770/{csv_filename}"



st.header("Transparencia y Claridad en RRHH YesBpo")

st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="https://cdn-icons-png.flaticon.com/128/6429/6429114.png" alt="RRHH YesBpo Logo" width="100" height="100">
    <h1 style='color: #0f0a68; font-size: 20px;'> RRHH YesBpo</h1>
    <img src="https://tse3.mm.bing.net/th?id=OIP.mgZxMZpR_P9RB4qAfF1FXQHaGg&pid=Api&P=0&h=180" alt="Otro logo" width="100" height="100">
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """,
    unsafe_allow_html=True,
)

# Display the first few rows of the DataFrame
st.dataframe(df.head(10))  # Increase or decrease the number of rows as needed

# Create interactive visualizations using Altair (optional)
# Customize charts based on your data and exploration goals
chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("column_name", title="X-axis Label"),  # Replace with actual column name
        y=alt.Y("count()", title="Count"),
        tooltip=[alt.Tooltip("column_name", title="X-axis Label"), alt.Tooltip("count()", title="Count")],
    )
)
st.altair_chart(chart)

# ------ Additional features (optional) ------

# - Add a search bar to filter the DataFrame
# - Implement sorting capabilities for specific columns
# - Allow users to download the DataFrame as a CSV/Excel file
# - Integrate with a database to persist data (if applicable)
