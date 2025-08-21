# Gráficos de Barras y Líneas en Streamlit: Guía Completa

Streamlit ofrece dos maneras principales de crear visualizaciones de datos: las funciones de gráfico **nativas** (`st.bar_chart`, `st.line_chart`) y el uso de librerías de gráficos más potentes como **Altair**, que se integra a la perfección con `st.altair_chart`.

---

## Gráficos Nativos de Streamlit: `st.bar_chart` y `st.line_chart`

Las funciones nativas de Streamlit son ideales para crear gráficos rápidos y sencillos con una mínima configuración. Son menos personalizables que otras opciones, pero perfectas para una visualización de datos rápida.

### Cómo Funcionan

Estas funciones son, en esencia, envoltorios (wrappers) de gráficos de la librería Vega-Lite. Esperan que los datos estén en un formato **"ancho" (wide-form)**, donde las columnas representan las series que quieres dibujar. El índice del DataFrame se utiliza para el eje X y cada columna se convierte en una serie en el eje Y.

Los datos de entrada pueden ser:
* Un DataFrame de Pandas.
* Un array de NumPy.
* Un diccionario.
* Una lista.

### `st.bar_chart` 📊

Esta función dibuja un gráfico de barras.

**Uso Básico**

Imaginemos que tienes el siguiente DataFrame de Pandas con datos de ventas trimestrales para diferentes productos:

```python
import streamlit as st
import pandas as pd
import numpy as np

# Datos de ejemplo
data = {
    'Producto A': [220, 250, 190, 300],
    'Producto B': [180, 200, 210, 240],
    'Producto C': [300, 280, 310, 290]
}
df = pd.DataFrame(data, index=['T1', 'T2', 'T3', 'T4'])

st.write("### Gráfico de Barras con `st.bar_chart`")
st.bar_chart(df)

Resultado:
Streamlit generará automáticamente un gráfico de barras donde el eje X corresponde al índice ('T1', 'T2', 'T3', 'T4') y cada columna ('Producto A', 'Producto B', 'Producto C') es una serie de barras con un color diferente.

Personalización

La personalización en st.bar_chart es bastante limitada. Los principales parámetros que puedes ajustar son:

    width y height: Permiten especificar el ancho y el alto del gráfico en píxeles.

    use_container_width: Si se establece en True, el gráfico se expandirá para ajustarse al ancho del contenedor en el que se encuentre.

Python

# Ejemplo con personalización de tamaño
st.bar_chart(df, height=500, use_container_width=True)

No puedes cambiar directamente los colores, títulos de los ejes, la leyenda o el estilo de las barras a través de los parámetros de la función. Para eso, necesitas usar Altair.

st.line_chart 📈

Funciona de manera muy similar a st.bar_chart, pero dibuja un gráfico de líneas. Es ideal para mostrar tendencias a lo largo del tiempo o de una variable continua.

Uso Básico

Usando el mismo DataFrame de antes, podemos crear un gráfico de líneas fácilmente:
Python

import streamlit as st
import pandas as pd

# Mismos datos de ejemplo
data = {
    'Producto A': [220, 250, 190, 300],
    'Producto B': [180, 200, 210, 240],
    'Producto C': [300, 280, 310, 290]
}
df = pd.DataFrame(data, index=['T1', 'T2', 'T3', 'T4'])

st.write("### Gráfico de Líneas con `st.line_chart`")
st.line_chart(df)

Resultado:
Esto creará un gráfico con tres líneas, una para cada producto, mostrando la evolución de las ventas a lo largo de los trimestres.

Personalización

Las opciones de personalización son idénticas a las de st.bar_chart: width, height y use_container_width.
Python

# Ejemplo con personalización de tamaño
st.line_chart(df, height=400)

Gráficos con Altair: st.altair_chart

Cuando necesitas más control y personalización, Altair es la mejor opción. Es una librería de visualización declarativa en Python basada en la gramática de Vega-Lite. Te permite construir gráficos complejos de manera muy intuitiva.

Cómo Funciona

Con Altair, defines los componentes de tu gráfico (los datos, las marcas visuales como barras o líneas, y las codificaciones que mapean los datos a las propiedades visuales) y la librería se encarga del resto.

Los datos para Altair deben estar en formato "largo" (long-form), que es más flexible. En lugar de tener una columna por cada serie, tienes una columna para los valores, otra para las categorías y otra para el eje X.

Preparando los Datos

Primero, transformemos nuestro DataFrame de formato ancho a largo usando melt:
Python

df_largo = df.reset_index().melt('index', var_name='Producto', value_name='Ventas')
df_largo = df_largo.rename(columns={'index': 'Trimestre'})
# El df_largo se verá así:
#   Trimestre     Producto  Ventas
# 0        T1   Producto A     220
# 1        T2   Producto A     250
# ...     ...          ...     ...

Gráfico de Barras con Altair

Para crear un gráfico de barras, usamos mark_bar() y especificamos las codificaciones para los ejes X e Y.

Uso Básico
Python

import streamlit as st
import pandas as pd
import altair as alt

# Preparando los datos como antes
data = {
    'Producto A': [220, 250, 190, 300],
    'Producto B': [180, 200, 210, 240],
    'Producto C': [300, 280, 310, 290]
}
df = pd.DataFrame(data, index=['T1', 'T2', 'T3', 'T4'])
df_largo = df.reset_index().melt('index', var_name='Producto', value_name='Ventas')
df_largo = df_largo.rename(columns={'index': 'Trimestre'})


st.write("### Gráfico de Barras con Altair")

# Creación del gráfico
bar_chart = alt.Chart(df_largo).mark_bar().encode(
    x='Trimestre:N',  # :N indica que es una variable Nominal (categórica)
    y='Ventas:Q',     # :Q indica que es una variable Cuantitativa (numérica)
    color='Producto:N' # Asigna un color diferente para cada producto
)

st.altair_chart(bar_chart, use_container_width=True)

Resultado:
Obtendrás un gráfico de barras agrupadas, donde cada trimestre tiene una barra para cada producto, diferenciada por color.

Gráfico de Líneas con Altair

El proceso es muy similar, pero usamos mark_line().

Uso Básico
Python

st.write("### Gráfico de Líneas con Altair")

# Creación del gráfico
line_chart = alt.Chart(df_largo).mark_line().encode(
    x='Trimestre:N',
    y='Ventas:Q',
    color='Producto:N'
)

st.altair_chart(line_chart, use_container_width=True)

Opciones de Personalización Avanzada con Altair

Aquí es donde Altair realmente brilla. Puedes personalizar casi cualquier aspecto del gráfico.

1. Títulos y Etiquetas de los Ejes

Puedes cambiar los títulos de los ejes y añadir un título general al gráfico con el método properties().
Python

chart = alt.Chart(df_largo).mark_bar().encode(
    x=alt.X('Trimestre:N', title='Trimestre Fiscal'),
    y=alt.Y('Ventas:Q', title='Ventas (en miles de €)'),
    color='Producto:N'
).properties(
    title='Rendimiento de Ventas por Trimestre'
)

st.altair_chart(chart, use_container_width=True)

2. Tooltips Interactivos

Añade información que aparece al pasar el ratón por encima de los datos.
Python

chart = alt.Chart(df_largo).mark_bar().encode(
    x='Trimestre:N',
    y='Ventas:Q',
    color='Producto:N',
    tooltip=['Trimestre', 'Producto', 'Ventas'] # Lista de campos a mostrar
)

st.altair_chart(chart, use_container_width=True)

3. Orden de las Barras/Categorías

Puedes especificar un orden personalizado para las categorías en los ejes.
Python

chart = alt.Chart(df_largo).mark_bar().encode(
    x=alt.X('Trimestre:N', sort=['T4', 'T3', 'T2', 'T1']), # Orden personalizado
    y='Ventas:Q',
    color='Producto:N'
)

st.altair_chart(chart, use_container_width=True)

4. Cambio de Colores y Estilos

Puedes definir una paleta de colores personalizada usando scale.
Python

chart = alt.Chart(df_largo).mark_bar().encode(
    x='Trimestre:N',
    y='Ventas:Q',
    color=alt.Color('Producto:N', scale=alt.Scale(
        # Paleta de colores predefinida de Vega
        scheme='category10'
        # O una lista de colores personalizados
        # range=['#ff8c00', '#1f77b4', '#2ca02c']
    ))
)

st.altair_chart(chart, use_container_width=True)

5. Añadir Puntos y Texto a los Gráficos de Líneas

Puedes combinar diferentes "marcas" (marks) para crear gráficos más complejos.
Python

line = alt.Chart(df_largo).mark_line().encode(
    x='Trimestre:N',
    y='Ventas:Q',
    color='Producto:N'
)

points = alt.Chart(df_largo).mark_circle(size=100).encode(
    x='Trimestre:N',
    y='Ventas:Q',
    color='Producto:N',
    tooltip=['Producto', 'Ventas']
)

# Combinar el gráfico de líneas y los puntos
combined_chart = line + points

st.altair_chart(combined_chart, use_container_width=True)

6. Hacer el Gráfico Interactivo (Zoom y Desplazamiento)

Añade interactividad con el método interactive().
Python

chart = alt.Chart(df_largo).mark_line().encode(
    x='Trimestre',
    y='Ventas',
    color='Producto'
).interactive() # ¡Así de fácil!

st.altair_chart(chart, use_container_width=True)

Resumen: ¿Cuándo Usar Cada Uno?

Característica	Gráficos Nativos (st.bar_chart, st.line_chart)	Altair (st.altair_chart)
Facilidad de uso	⭐⭐⭐⭐⭐ Muy fácil. Una sola línea de código.	⭐⭐⭐⭐ Fácil. Requiere una sintaxis más elaborada.
Personalización	⭐ Muy limitada. Solo tamaño.	⭐⭐⭐⭐⭐ Total. Colores, ejes, títulos, tooltips, etc.
Interactividad	⭐ Limitada. Tooltips básicos por defecto.	⭐⭐⭐⭐⭐ Avanzada. Zoom, desplazamiento, selecciones.
Formato de Datos	Formato ancho.	Formato largo (más flexible).
Casos de uso	Visualización rápida, dashboards sencillos, exploración de datos inicial.	Informes detallados, aplicaciones interactivas, gráficos listos para publicación.

En resumen, empieza con las funciones nativas para visualizar tus datos rápidamente. Cuando necesites más control sobre la apariencia o la interactividad, pásate a Altair. La combinación de ambos te da una enorme flexibilidad para crear cualquier tipo de visualización que necesites en tus aplicaciones de Streamlit.