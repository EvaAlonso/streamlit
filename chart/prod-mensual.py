import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Configuración general
#st.set_page_config(page_title="Producción semanal SEAT", layout="centered")
st.title("Resultados - Producción Mensual")

# Lista de modelos
modelos_seat = [
    "Ibiza", "León", "Arona","A! AU270_1"
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

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

# --- Configuración de la app ---
st.set_page_config(page_title="Dashboard de Modelos", layout="wide")

st.title("Visualización de Modelos por Semana")

# --- Simulación de datos ---
np.random.seed(42)
semanas = list(range(1, 53))
meses_dict = {
    "Enero": [1, 2, 3, 4],
    "Febrero": [5, 6, 7, 8],
    "Marzo": [9, 10, 11, 12],
    "Abril": [13, 14, 15, 16],
    "Mayo": [17, 18, 19, 20],
    "Junio": [21, 22, 23, 24],
    "Julio": [25, 26, 27, 28],
    "Agosto": [29, 30, 31, 32],
    "Septiembre": [33, 34, 35, 36],
    "Octubre": [37, 38, 39, 40],
    "Noviembre": [41, 42, 43, 44],
    "Diciembre": [49, 50, 51, 52]
}

modelos = [f"Modelo_{i+1}" for i in range(10)]
data = []
for ml in ["ML1", "ML3"]:
    for modelo in modelos:
        for semana in semanas:
            valor = np.random.randint(10, 100)
            data.append({
                "ML": ml,
                "Modelo": modelo,
                "Semana": semana,
                "Valor": valor
            })

df = pd.DataFrame(data)

# --- Interfaz de usuario ---
col1, col2, col3 = st.columns(3)

with col1:
    ml_tipo = st.radio("Selecciona línea:", ["ML1", "ML3"], horizontal=True)

with col2:
    tipo_grafico = st.selectbox("Tipo de gráfico", ["Línea", "Barras", "Torta"])

with col3:
    mes = st.selectbox("Selecciona mes", list(meses_dict.keys()))

mostrar_modelos = st.radio("¿Qué modelos mostrar?", ["Un modelo", "Todos los modelos"], horizontal=True)

if mostrar_modelos == "Un modelo":
    modelo_seleccionado = st.selectbox("Selecciona el modelo", modelos)
else:
    modelo_seleccionado = None

mostrar_acumulado = st.checkbox("Mostrar acumulado")

# --- Filtrado de datos ---
df_filtrado = df[df["ML"] == ml_tipo]
semanas_mes = meses_dict[mes]
df_filtrado = df_filtrado[df_filtrado["Semana"].isin(semanas_mes)]

if mostrar_modelos == "Un modelo":
    df_filtrado = df_filtrado[df_filtrado["Modelo"] == modelo_seleccionado]

if mostrar_acumulado:
    df_filtrado = df_filtrado.groupby(["Semana", "Modelo"], as_index=False).sum()

# --- Visualización ---
if tipo_grafico in ["Línea", "Barras"]:
    chart = alt.Chart(df_filtrado).mark_line() if tipo_grafico == "Línea" else alt.Chart(df_filtrado).mark_bar()

    chart = chart.encode(
        x=alt.X("Semana:O", title="Semana del Año"),
        y=alt.Y("Valor:Q", title="Valor acumulado" if mostrar_acumulado else "Valor"),
        color="Modelo:N",
        tooltip=["Modelo", "Semana", "Valor"]
    ).properties(
        width=800,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

elif tipo_grafico == "Torta":
    if mostrar_modelos == "Todos los modelos":
        df_pie = df_filtrado.groupby("Modelo", as_index=False).sum()
    else:
        df_pie = df_filtrado.groupby("Semana", as_index=False).sum()
        df_pie["Modelo"] = df_pie["Semana"].astype(str)

    chart = alt.Chart(df_pie).mark_arc().encode(
        theta=alt.Theta(field="Valor", type="quantitative"),
        color=alt.Color(field="Modelo", type="nominal"),
        tooltip=["Modelo", "Valor"]
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
