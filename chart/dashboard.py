import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import pydeck as pdk

st.set_page_config(page_title="Dashboard de Visualizaciones", layout="wide")
st.title("📊 Dashboard interactivo con Streamlit")
st.markdown("Visualizaciones personalizadas usando **Altair**, **Plotly**, y **Pydeck**.")
# instala dependencias en la terminal pip install streamlit altair plotly pydeck pandas numpy

# =======================
# 📁 Datos de ejemplo
# =======================
np.random.seed(42)

df_line = pd.DataFrame({
    'Fecha': pd.date_range('2025-08-01', periods=30),
    'Ventas': np.random.randint(100, 500, size=30)
})

df_cat = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [120, 80, 150, 100]
})

df_scatter = pd.DataFrame({
    'X': np.random.rand(100),
    'Y': np.random.rand(100),
    'Tamaño': np.random.rand(100) * 100,
    'Categoría': np.random.choice(['Grupo 1', 'Grupo 2'], size=100)
})

df_mapa = pd.DataFrame({
    'lat': [40.4168, 41.3825, 48.8566],
    'lon': [-3.7038, 2.1769, 2.3522],
    'ciudad': ['Madrid', 'Barcelona', 'París']
})

df_box = pd.DataFrame({
    'Grupo': np.random.choice(['A', 'B', 'C'], size=200),
    'Valor': np.random.normal(0, 1, 200)
})

df_heatmap = pd.DataFrame({
    'Día': np.tile(np.arange(1, 8), 24),
    'Hora': np.repeat(np.arange(0, 24), 7),
    'Valor': np.random.rand(168)
})

df_radar = pd.DataFrame({
    'Categoría': ['Velocidad', 'Fuerza', 'Agilidad', 'Resistencia', 'Técnica'],
    'Jugador 1': [80, 70, 75, 85, 90],
    'Jugador 2': [60, 85, 80, 70, 65]
})

# =======================
# 🎨 Gráfico de línea (Altair)
# =======================
st.subheader("📈 Gráfico de línea personalizado")

line_chart = alt.Chart(df_line).mark_line(point=True).encode(
    x=alt.X('Fecha:T', title='Fecha'),
    y=alt.Y('Ventas:Q', title='Ventas Diarias'),
    tooltip=['Fecha', 'Ventas']
).properties(
    width=700,
    height=300,
    title='Ventas en el tiempo'
).configure_title(fontSize=18).interactive()

st.altair_chart(line_chart, use_container_width=True)

# =======================
# 📊 Gráfico de barras (Altair)
# =======================
st.subheader("📊 Gráfico de barras")

bar_chart = alt.Chart(df_cat).mark_bar(color='orange').encode(
    x=alt.X('Categoría:N', title='Categoría'),
    y=alt.Y('Valor:Q', title='Valor'),
    tooltip=['Categoría', 'Valor']
).properties(width=500, height=300)

st.altair_chart(bar_chart, use_container_width=True)

# =======================
# 🔵 Scatter plot (Altair)
# =======================
st.subheader("🔵 Gráfico de dispersión con tamaño y color")

scatter_chart = alt.Chart(df_scatter).mark_circle(opacity=0.7).encode(
    x='X:Q',
    y='Y:Q',
    size='Tamaño:Q',
    color='Categoría:N',
    tooltip=['X', 'Y', 'Tamaño', 'Categoría']
).properties(width=700, height=400).interactive()

st.altair_chart(scatter_chart, use_container_width=True)

# =======================
# 🔥 Heatmap (Altair)
# =======================
st.subheader("🔥 Mapa de calor")

heatmap = alt.Chart(df_heatmap).mark_rect().encode(
    x=alt.X('Día:O', title='Día de la semana'),
    y=alt.Y('Hora:O', title='Hora del día'),
    color=alt.Color('Valor:Q', scale=alt.Scale(scheme='inferno')),
    tooltip=['Día', 'Hora', 'Valor']
).properties(width=600, height=400)

st.altair_chart(heatmap, use_container_width=True)

# =======================
# 📦 Boxplot (Altair)
# =======================
st.subheader("📦 Boxplot por grupo")

boxplot = alt.Chart(df_box).mark_boxplot(extent='min-max').encode(
    x='Grupo:N',
    y='Valor:Q',
    color='Grupo:N'
).properties(width=400)

st.altair_chart(boxplot, use_container_width=True)

# =======================
# 🗺️ Mapa (Pydeck)
# =======================
st.subheader("🗺️ Mapa interactivo")

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df_mapa,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=100000,
    pickable=True
)

view_state = pdk.ViewState(latitude=45, longitude=0, zoom=3)
mapa = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{ciudad}"})

st.pydeck_chart(mapa)

# =======================
# 🕸️ Radar chart (Plotly)
# =======================
st.subheader("🕸️ Gráfico de radar comparativo")

radar = px.line_polar(df_radar.melt(id_vars='Categoría', var_name='Jugador', value_name='Valor'),
                      r='Valor', theta='Categoría', color='Jugador',
                      line_close=True, template='plotly_dark')
radar.update_traces(fill='toself')

st.plotly_chart(radar, use_container_width=True)

# =======================
# 🚀 Final
# =======================
st.markdown("---")
st.success("¡Dashboard cargado con éxito!")

