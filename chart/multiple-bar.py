import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Configuración general
st.set_page_config(page_title="Producción semanal de coches Seat", layout="centered")

st.title("🚗 Producción semanal de modelos SEAT")
st.markdown("Selecciona un modelo en el panel lateral para ver su producción durante las 52 semanas del año.")

# Lista de modelos de Seat
modelos_seat = [
    "Ibiza", "León", "Arona", "Ateca", "Tarraco",
    "Toledo", "Mii", "Alhambra", "Cordoba", "Exeo"
]

# Sidebar para seleccionar modelo
modelo_seleccionado = st.sidebar.selectbox("Selecciona un modelo de coche:", modelos_seat)

# Simular datos de producción para cada modelo
# (En una app real, cargarías estos datos de una base de datos o CSV)
np.random.seed(42)
data_modelos = {}
for modelo in modelos_seat:
    produccion = np.random.randint(500, 3000, size=53)  # 53 semanas (0 a 52)
    data_modelos[modelo] = pd.DataFrame({
        'Semana': np.arange(53),
        'Producción': produccion
    })

# Obtener datos del modelo seleccionado
df = data_modelos[modelo_seleccionado]

# Crear gráfico con Altair
chart = alt.Chart(df).mark_bar(color="#0072B2").encode(
    x=alt.X('Semana:O', title='Semana del año', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Producción:Q', title='Coches fabricados', scale=alt.Scale(domain=[0, 3000])),
    tooltip=['Semana', 'Producción']
).properties(
    width=700,
    height=400,
    title=f"Producción semanal del modelo SEAT {modelo_seleccionado}"
).configure_title(
    fontSize=20,
    anchor='start'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

# Mostrar gráfico
st.altair_chart(chart, use_container_width=True)
