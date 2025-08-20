# Chuleta: Streamlit — Fundamentos de Python y Ejemplos Avanzados

Este documento contiene:

1. **Chuleta práctica** de Python y Streamlit
2. **Explicación completa de **``
3. **Ejemplos avanzados** para casos reales
4. **Autenticación y conexión a bases de datos**

---

## Ejemplos avanzados de Streamlit

### 1) Uso de `st.session_state` para un carrito de compras

```python
import streamlit as st

if 'carrito' not in st.session_state:
    st.session_state.carrito = []

producto = st.text_input('Producto a agregar')
if st.button('Agregar al carrito') and producto:
    st.session_state.carrito.append(producto)

st.write('Carrito actual:', st.session_state.carrito)
```

---

### 2) Integración con Plotly para gráficos interactivos

```python
import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig)
```

---

### 3) Cache de modelos de Machine Learning

```python
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

@st.cache_resource
def get_model():
    iris = load_iris()
    model = LogisticRegression(max_iter=200)
    model.fit(iris.data, iris.target)
    return model, iris

model, iris = get_model()

entrada = [
    st.number_input('Sepal length'),
    st.number_input('Sepal width'),
    st.number_input('Petal length'),
    st.number_input('Petal width')
]

if st.button('Predecir'):
    pred = model.predict([entrada])[0]
    st.write('Predicción:', iris.target_names[pred])
```

---

### 4) Uso de `lambda` en filtrado dinámico

```python
import pandas as pd
import streamlit as st

st.title('Filtrado avanzado')

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carla', 'Pedro'],
    'Edad': [23, 34, 29, 40]
})

edad_min = st.slider('Edad mínima', 0, 50, 25)
resultado = df[df['Edad'].apply(lambda e: e >= edad_min)]
st.dataframe(resultado)
```

---

### 5) Consumo de API y visualización

```python
import requests
import streamlit as st

st.title('Clima actual')
ciudad = st.text_input('Ciudad', 'Madrid')
if st.button('Obtener clima'):
    url = f'https://wttr.in/{ciudad}?format=j1'
    r = requests.get(url)
    data = r.json()
    temp = data['current_condition'][0]['temp_C']
    st.write(f'Temperatura actual en {ciudad}: {temp}°C')
```

---

### 6) Autenticación básica con usuario y contraseña

```python
import streamlit as st

# Credenciales simples (solo para pruebas)
USUARIO = "admin"
CLAVE = "1234"

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    usuario = st.text_input('Usuario')
    clave = st.text_input('Contraseña', type='password')
    if st.button('Iniciar sesión'):
        if usuario == USUARIO and clave == CLAVE:
            st.session_state.auth = True
            st.success('Sesión iniciada')
        else:
            st.error('Credenciales incorrectas')
else:
    st.success('Bienvenido al área privada')
```

---

### 7) Conexión a base de datos SQLite

```python
import sqlite3
import streamlit as st

# Conectar a base de datos (crea archivo si no existe)
conn = sqlite3.connect('datos.db')
c = conn.cursor()

# Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos
nombre = st.text_input('Nombre')
edad = st.number_input('Edad', 0, 120)
if st.button('Guardar'):
    c.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    st.success('Usuario guardado')

# Mostrar datos
c.execute('SELECT * FROM usuarios')
datos = c.fetchall()
st.dataframe(datos)
```

---

Con estos ejemplos, tienes **interactividad, visualización, cache, autenticación y conexión a BD** en Streamlit.

