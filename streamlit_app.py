

import streamlit as st
import pandas as pd

# Get the raw content URL for the GitHub file
url = "https://raw.githubusercontent.com/andre123354cs/YesBpoRRHH/blob/08957ddc8b75388d115858e13a6bdb70aa109e55/rrhh%20-%20Hoja%201.csv"

try:
  # Read the CSV data using pandas
  df = pd.read_csv(url)

  # Display the DataFrame in Streamlit
  st.dataframe(df)

except Exception as e:
  # Handle potential errors (e.g., network issues, invalid URL)
  st.error(f"Error reading the CSV file: {e}")
