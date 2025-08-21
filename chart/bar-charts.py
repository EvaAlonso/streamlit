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
#Personalización avanzada de la gráfica de barras apiladas
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


# Mostrar la gráfica
st.altair_chart(chart)

"""ejemplo completo en Streamlit + Altair, con varias opciones de interactividad y personalización:
Selección de columna para el eje Y.
Colores personalizados.
Ordenar las barras.
Tooltips con info extra.
Etiquetas sobre las barras.
Opción de gráfico de barras horizontal o vertical.
Ajuste de tamaño."""


# -----------------------------
# Datos de ejemplo
# -----------------------------
df = pd.DataFrame({
    "fruta": ["manzana", "plátano", "uva", "pera", "cereza"],
    "ventas": [10, 20, 15, 8, 12],
    "precio_promedio": [1.2, 0.8, 2.5, 1.5, 3.0],
    "stock": [50, 40, 30, 20, 10]
})

st.title("📊 Ejemplo completo: Altair + Streamlit")

# -----------------------------
# Controles de usuario
# -----------------------------
y_axis = st.selectbox(
    "📈 Selecciona la métrica a graficar:",
    ["ventas", "precio_promedio", "stock"]
)

orientation = st.radio(
    "📐 Orientación de las barras:",
    ["Vertical", "Horizontal"]
)

order = st.checkbox("🔀 Ordenar de mayor a menor", value=True)

color_scheme = st.selectbox(
    "🎨 Selecciona paleta de colores:",
    ["category10", "category20", "dark2", "set1", "set2"]
)

# -----------------------------
# Construcción del gráfico
# -----------------------------
# Definir eje X y Y según orientación
if orientation == "Vertical":
    x = alt.X("fruta", sort="-y" if order else None, title="Fruta")
    y = alt.Y(y_axis, title=y_axis.capitalize())
else:
    x = alt.X(y_axis, title=y_axis.capitalize())
    y = alt.Y("fruta", sort="-x" if order else None, title="Fruta")

# Crear gráfico base
chart = (
    alt.Chart(df)
    .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
    .encode(
        x=x,
        y=y,
        color=alt.Color("fruta", scale=alt.Scale(scheme=color_scheme), legend=None),
        tooltip=["fruta", y_axis, "precio_promedio", "stock"]  # tooltip con más info
    )
    .properties(width=600, height=400)
)

# Añadir etiquetas de texto (solo para orientación vertical)
if orientation == "Vertical":
    text = chart.mark_text(
        align="center",
        baseline="bottom",
        dy=-3
    ).encode(
        text=y_axis
    )
    chart = chart + text

# Mostrar gráfico
st.altair_chart(chart, use_container_width=True)
#🔹 ¿Qué puedes hacer aquí?
#✅ Cambiar la métrica (ventas, precio, stock).
#✅ Cambiar la orientación (barras verticales u horizontales).
#✅ Elegir si las barras se ordenan o no.
#✅ Escoger la paleta de colores.
#✅ Pasar el mouse y ver tooltips con más info.
#✅ Ver las etiquetas de valores encima de las barras.