import numpy as np
import pandas as pd
"""
#se crea un csv que imite la fabricación de coches en las semanas del año con un valor promedio, un valor mínimo y uno máximo
# Semilla para reproducibilidad
rng = np.random.default_rng(seed=42)

# Generar las 52 semanas
semanas = np.arange(1, 53)

# Generar la producción con media 3020, pero con recorte a entre 1920 y 5000
produccion = rng.normal(loc=3020, scale=400, size=52)
produccion = np.clip(produccion, 1920, 5000)  # Limitar valores a entre 1920 y 5000
produccion = produccion.astype(int)

# Crear DataFrame
df = pd.DataFrame({
    'Semana': semanas,
    'Producción': produccion
})

# Guardar como CSV
df.to_csv('produccion_semanal.csv', index=False)

#Ejecuta el archivo en terminal con python crearcsv.py y te creará el archivo csv
"""
#para crear dataframe con produccion por modelos
# Crear generador aleatorio
rng = np.random.default_rng(seed=42)

# Paso 1: Generar producción total semanal (52 valores)
total_produccion = rng.normal(loc=3020, scale=400, size=52)
total_produccion = np.clip(total_produccion, 1920, 5000).astype(int)

# Paso 2: Generar proporciones aleatorias para los 3 modelos por semana
# Cada fila tiene 3 proporciones que suman 1
proporciones = rng.dirichlet(alpha=[1, 1, 1], size=52)

# Paso 3: Multiplicar cada producción total semanal por sus proporciones
produccion_modelos = (total_produccion[:, np.newaxis] * proporciones).astype(int)

# Paso 4: Crear DataFrame
df_modelos = pd.DataFrame(
    produccion_modelos,
    columns=["Modelo_A", "Modelo_B", "Modelo_C"]
)
df_modelos["Semana"] = np.arange(1, 53)

# Opcional: Reordenar columnas para mejor presentación
df_modelos = df_modelos[["Semana", "Modelo_A", "Modelo_B", "Modelo_C"]]

# Mostrar las primeras filas
print(df_modelos.head())

# Guardar a CSV si quieres
df_modelos.to_csv("produccion_modelos_semanal.csv", index=False)