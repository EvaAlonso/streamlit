import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Datos simulados
df = pd.DataFrame({
    'Día': pd.date_range(start='2025-08-01', periods=10),
    'Ventas': np.random.randint(100, 500, size=10)
})

# Visualización simple
st.subheader("Gráfico simple con st.line_chart")

# Hay que usar el índice para que la fecha esté en el eje X
st.line_chart(df.set_index('Día'), use_container_width=True)

# Visualización avanzada
st.subheader("Gráfico personalizado con Altair")

chart = alt.Chart(df).mark_line(
    point=alt.OverlayMarkDef(color='red', size=50)
).encode(
    x=alt.X('Día:T', title='Fecha'),
    y=alt.Y('Ventas:Q', title='Cantidad vendida'),
    tooltip=['Día', 'Ventas']
).properties(
    width=700,
    height=400,
    title='📈 Ventas diarias de la tienda (agosto 2025)'
).configure_title(
    fontSize=18,
    font='Helvetica',
    anchor='start',
    color='darkblue'
).configure_axis(
    grid=True,
    gridColor='lightgray',
    labelFontSize=12,
    titleFontSize=14
).configure_view(
    strokeWidth=0,
    fill='white'
)

st.altair_chart(chart, use_container_width=True)