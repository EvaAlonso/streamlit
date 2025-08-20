import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#cargar el csv

df = pd.read_csv('produccion_semanal.csv')
st.title('Produción semanal ')

#Mostrar la tabla
st.dataframe(df)
#Mostrar la gráfica en línea
st.line_chart(df.set_index('Semana'))


# Mostrar gráfica de barras
st.bar_chart(data=df, x='Semana', y='Producción')

# Crear generador aleatorio
rng = np.random.default_rng(seed=42)

# Paso 1: Generar producción total semanal (52 valores)
total_produccion = rng.normal(loc=3020, scale=400, size=52)
total_produccion = np.clip(total_produccion, 1920, 5000).astype(int)

# Paso 2: Generar proporciones aleatorias para los 3 modelos por semana
proporciones = rng.dirichlet(alpha=[1, 1, 1], size=52)

# Paso 3: Multiplicar cada producción total semanal por sus proporciones
produccion_modelos = (total_produccion[:, np.newaxis] * proporciones).astype(int)

# Paso 4: Crear DataFrame
df_modelos = pd.DataFrame(
    produccion_modelos,
    columns=["Modelo_A", "Modelo_B", "Modelo_C"]
)
df_modelos["Semana"] = np.arange(1, 53)

# Reordenar columnas para mejor presentación
df_modelos = df_modelos[["Semana", "Modelo_A", "Modelo_B", "Modelo_C"]]

# Mostrar los datos (opcional)
st.dataframe(df_modelos)

# Crear un DataFrame para la gráfica de barras apiladas, .melt Convierte el DataFrame a formato largo para que sea más fácil graficar con Altair. Cada fila tendrá una semana, el modelo de coche y la producción correspondiente
df_modelos_melted = df_modelos.melt(id_vars=["Semana"], 
                                    value_vars=["Modelo_A", "Modelo_B", "Modelo_C"],
                                    var_name="Modelo", 
                                    value_name="Producción")

# Crear la gráfica de barras apiladas
chart = alt.Chart(df_modelos_melted).mark_bar().encode(
    x='Semana:O',  # Eje X con las semanas
    y='Producción:Q',  # Eje Y con la producción
    color='Modelo:N',  # Diferentes colores por modelo
    tooltip=['Semana', 'Modelo', 'Producción']  # Mostrar valores en el hover
).properties(
    width=600,
    height=400
)
"""Personalización avanzada de la gráfica de barras apiladas
chart = alt.Chart(df_modelos_melted).mark_bar().encode(
    x=alt.X('Semana:O', title='Semana', axis=alt.Axis(labelFontSize=14, titleFontSize=16, labelAngle=0)),  # Personaliza el eje X
    y=alt.Y('Producción:Q', title='Producción de Coches', axis=alt.Axis(labelFontSize=14, titleFontSize=16)),  # Personaliza el eje Y
    color=alt.Color('Modelo:N', scale=alt.Scale(domain=["Modelo_A", "Modelo_B", "Modelo_C"], range=["#FF8C00", "#1E90FF", "#32CD32"])),  # Colores personalizados
    tooltip=['Semana', 'Modelo', 'Producción'],  # Tooltip con más detalles
).properties(
    title="Producción Semanal de Coches por Modelo",  # Título de la gráfica
    width=700,
    height=400
).configure_title(
    fontSize=20,  # Tamaño de la fuente del título
    anchor='middle',  # Alineación del título
    font='Arial'  # Tipo de fuente
).configure_axis(
    labelFontSize=12,  # Tamaño de las etiquetas del eje
    titleFontSize=14,  # Tamaño del título de los ejes
    grid=True,  # Mostrar líneas de la cuadrícula
    gridColor='lightgray',  # Color de las líneas de la cuadrícula
    gridOpacity=0.3  # Opacidad de la cuadrícula
).configure_view(
    strokeWidth=0  # Eliminar el borde de la vista
).interactive()  # Activar la interactividad (por ejemplo, zoom)

"""
# Mostrar la gráfica
st.altair_chart(chart)