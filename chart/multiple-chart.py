import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Configuración general
st.set_page_config(page_title="Producción semanal SEAT", layout="centered")
st.title("🚗 Producción semanal de modelos SEAT")

# Lista de modelos
modelos_seat = [
    "Ibiza", "León", "Arona", "Ateca", "Tarraco",
    "Toledo", "Mii", "Alhambra", "Cordoba", "Exeo"
]

# =========================
# 🎛️ Sidebar de controles
# =========================
st.sidebar.header("Configuración del gráfico")

modelo_seleccionado = st.sidebar.selectbox("Selecciona un modelo:", modelos_seat)

tipo_grafico = st.sidebar.radio("Tipo de gráfico:", ["Barras", "Líneas"])

orientacion = st.sidebar.radio("Orientación de barras:", ["Vertical", "Horizontal"])

color = st.sidebar.color_picker("Color del gráfico:", "#1f77b4")

# =========================
# 📊 Simular datos por modelo
# =========================
np.random.seed(42)
data_modelos = {
    modelo: pd.DataFrame({
        'Semana': np.arange(53),
        'Producción': np.random.randint(500, 3000, size=53)
    })
    for modelo in modelos_seat
}

df = data_modelos[modelo_seleccionado]

# =========================
# 📈 Construcción del gráfico
# =========================

# Eje X e Y según orientación
if orientacion == "Vertical":
    eje_x = alt.X('Semana:O', title='Semana del año', axis=alt.Axis(labelAngle=0))
    eje_y = alt.Y('Producción:Q', title='Coches fabricados', scale=alt.Scale(domain=[0, 3000]))
else:  # Horizontal
    eje_x = alt.X('Producción:Q', title='Coches fabricados', scale=alt.Scale(domain=[0, 3000]))
    eje_y = alt.Y('Semana:O', title='Semana del año', axis=alt.Axis(labelAngle=0))

# Tipo de gráfico: barra o línea
if tipo_grafico == "Barras":
    chart = alt.Chart(df).mark_bar(color=color).encode(
        x=eje_x,
        y=eje_y,
        tooltip=['Semana', 'Producción']
    )
else:
    chart = alt.Chart(df).mark_line(color=color, point=True).encode(
        x=eje_x,
        y=eje_y,
        tooltip=['Semana', 'Producción']
    )

# Configurar estilo general
chart = chart.properties(
    width=700,
    height=450,
    title=f"Producción semanal del SEAT {modelo_seleccionado}"
).configure_title(
    fontSize=20,
    anchor='start'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

# Mostrar gráfico
st.altair_chart(chart, use_container_width=True)

