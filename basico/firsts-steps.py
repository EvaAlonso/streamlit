"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

""" #Ese fragmento de código hace lo siguiente:

Crea un DataFrame de pandas llamado dataframe con 10 filas y 20 columnas, llenando cada celda con un número aleatorio siguiendo una distribución normal (np.random.randn(10, 20)).
Nombra las columnas como 'col 0', 'col 1', ..., 'col 19'.
Muestra el DataFrame en Streamlit usando st.dataframe(), pero antes aplica el método .style.highlight_max(axis=0), que resalta el valor máximo de cada columna (por eje 0) en la tabla mostrada.
En resumen: genera una tabla de números aleatorios y, al visualizarla en Streamlit, resalta el valor más alto de cada columna.
"""

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

"""usando table
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

#Gráfico de líneas
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Mapa
"""_summaryGenera un DataFrame llamado map_data con 1000 filas y 2 columnas usando números aleatorios con distribución normal (np.random.randn(1000, 2)).
Divide cada columna por [50, 50] para reducir la dispersión de los datos.
Suma [37.76, -122.4] a cada fila, desplazando los puntos generados cerca de la latitud y longitud de Esparreguera, Barcelona.
Nombra las columnas como 'lat' (latitud) y 'lon' (longitud).
Muestra los puntos en un mapa usando st.map(map_data) en Streamlit.
En resumen: crea 1000 puntos aleatorios cerca de Esparreguera y los visualiza en un mapa interactivo en Streamlit._
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [41.5351, 1.8712],
    columns=['lat', 'lon'])

st.map(map_data)

""" Crea un slider interactivo en la interfaz de Streamlit con st.slider('x'), permitiendo al usuario seleccionar un valor para x (por defecto, el rango es de 0 a 100).
Muestra el valor seleccionado y su cuadrado usando st.write(x, 'squared is', x * x).
En resumen: el usuario elige un número con el slider y la app muestra ese número junto con su valor al cuadrado.
"""

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)