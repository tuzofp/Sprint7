import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("📊 Exploración Interactiva de Datos Vehiculares")

# Cargar datos desde una ruta fija
DATA_PATH = "vehicles_us.csv"
df = pd.read_csv(DATA_PATH)

# Mostrar tabla
st.write("Vista previa de los datos:")
st.dataframe(df)

# Columnas numéricas
columnas_numericas = df.select_dtypes(include="number").columns.tolist()

# Histograma
if st.checkbox("Mostrar histograma"):
    col_hist = st.selectbox("Selecciona la columna para el histograma", columnas_numericas, key="hist")
    fig_hist = px.histogram(df, x=col_hist, nbins=30, title=f"Histograma de {col_hist}")
    st.plotly_chart(fig_hist)

# Dispersión
if st.checkbox("Mostrar gráfico de dispersión"):
    col_x = st.selectbox("Eje X", columnas_numericas, key="disp_x")
    col_y = st.selectbox("Eje Y", columnas_numericas, key="disp_y")
    fig_disp = px.scatter(df, x=col_x, y=col_y, title=f"Dispersión: {col_y} vs {col_x}")
    st.plotly_chart(fig_disp)